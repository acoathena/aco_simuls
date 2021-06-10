#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:26:43 2021

@authors: F.J. Carrera

Athena Community Office
Instituto de Física de Cantabria (CSIC-UC)
Funded by Agencia Estatal de Investigación, Unidad de Excelencia María de Maeztu, ref. MDM-2017-0765
Funded by the Spanish Ministry MCIU under project RTI2018-096686-B-C21 (MCIU/AEI/FEDER, UE), co-funded by FEDER funds.

This is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.
This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
For a copy of the GNU General Public License see
<http://www.gnu.org/licenses/>.

# ################################################################################################################


Set of functions implementing equations for the detection of a source above a given level of background counts B
    with a significance of detection prob, using Poisson probability

  The Poisson probability of getting n counts when the expected values is mu is given by P_mu(n)=exp(-mu)*mu**n/n!

  If mu is the expected value in a poisson distribution and k is a particular value:

     gammainc(k,0.0,mu)=sum_n=k^inf(exp(-mu)*mu**n/n!)==1-sum_n=0^(k-1){P_mu(n)}

     i.e. the Poisson probability of obtaining a value k or higher when the expected value is mu
            gammainc is the incomplete gamma function defined below

  It also uses the library scipy.stats.poisson
      https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
    poisson.sf(k,mu)=sum_n=k+1_inf{P_mu(n)}
       i.e. the Poisson probability of obtaining a value higher than k when the expected value is mu
    poisson.isf(prob,mu) is the inverse of poisson.sf: returns the value of k for which the sum just above is prob

  The parameter flag allows to choose between calculating probabilities using gammainc (flag=0)
      or poisson (flag=1, default).
  The difference is that flag=1 does not include the limiting value in the sum, while flag=0 does.
      Output of flag=1 produces "jumps" at discrete values of the limiting value


"""

from mpmath import gammainc
import numpy as np
from scipy.special import erf
from scipy.optimize import root
from scipy.stats import poisson


def gammainc_here(x,a,b,prob):
    """
    Wrapper around the "regularized" mpmath incomplete Gamma function gammainc
          https://mpmath.org/doc/current/functions/expintegrals.html

        gammainc(z,a,b,regularized=True)=int_a^b(t**(z-1)*exp(-t))/Gamma(z)
              where Gamma(z)=int_0^inf(t**(z-1)*exp(-t))


        Implemented because the numpy version gave problems for high values of the arguments
        Cast as numpy float64 on output because the original mpmath object gave problems with numpy calculations
            down the line
        It actually returns gammainc-prob, so that it can be used to:
            - return simply gammainc when prob=0
            - find values of x for which gammainc=prob

    Parameters
    ----------
    x : COMPLEX
        value of the variable at which to calculate the function
    a : FLOAT
        lower limit of the integral
    b : FLOAT
        upper limit of the integral
    prob : FLOAT
        value to subtract from the integral, set to 0 to just get gammainc [0,1]

    Returns
    -------
    gi : NUMPY FLOAT64
        value of the "regularized" gamma function for the input parameters - prob

    """

    # plain call to gammainc with the provided arguments in the same order

    gi=gammainc(x[0],a,b,regularized=True)-prob
    return np.float64(gi)


def get_kdet(B,prob=None,flag=1):
    """
    Given background counts B and a significance of detection prob,
        returns the counts k0 for which, for an expected value of B,
           the probability of detecting more >k0 counts (flag=1) or >=k0 counts (flag=0) is 1-prob

    Parameters
    ----------
    B : FLOAT
        Background counts in the detection area
    prob : FLOAT, optional
        Detection significance. The default is None, with internally translates into 5 sigma probability [0,1]
    flag : INT, optional
        Allows choosing betwen using gammainc (0) or poisson (1). The default is 1.

    Returns
    -------
    kdet : FLOAT
        Value of the observed counts with a probability <1-prob of being observed when expecting B

    """
    # default prob value 5sigma
    if(prob is None):
        prob=erf(5.0/np.sqrt(2))

    if (flag==0):
        # using gammainc
        kdet=root(gammainc_here,x0=B,tol=(1.0-prob)/10.0,args=(0.0,B,1.0-prob)).x[0]
    else:
        # using poisson
        kdet=poisson.isf(1-prob,B)

    return kdet


def get_sdet(B,prob=None,t=1.0,EEF=1.0,flag=1):
    """
    Given background counts B and significance of detection prob, defining C=sdet*t*EEF,
        returns the countrate sdet for which, for an expected value of B,
           the probability of detecting more >B+C counts (flag=1) or >=B+C counts (flag=0) is 1-prob

    Parameters
    ----------
    B : FLOAT
        Background counts in the detection area
    prob : FLOAT, optional
        Detection significance. The default is None, with internally translates into 5 sigma probability
    t : FLOAT, optional
        Exposure time in seconds. The default is 1.0.
    EEF : FLOAT, optional
        Enclosed Energy Fraction of the source in the detection area. The default is 1.0.
    flag : INT, optional
        Allows choosing betwen using gammainc (0) or poisson (1). The default is 1.

    Returns
    -------
    sdet : FLOAT
        countrate sdet for which, for an expected value of B,
           the probability of detecting more >B+C counts (flag=1) or >=B+C counts (flag=0) is 1-prob

    """

    if(prob is None):
        prob=erf(5.0/np.sqrt(2))

    tau=t*EEF
    kdet=get_kdet(B,prob,flag=flag)
    sdet=(kdet-B)/tau

    return sdet


def get_Pdet(B,s,prob=None,t=1.0,EEF=1.0,flag=1):
    """
    Given background counts B, a source with countrate s, a significance of detection prob,
          exposure time t and Enclosed Energy Fraction EEF,
        returns the probability of detecting that source above that background with significance prob or higher

    Parameters
    ----------
    B : FLOAT
        Background counts in the detection area
    s : FLOAT
        Total countrate of the source
    prob : FLOAT, optional
        Detection probability. The default is None, with internally translates into 5 sigma probability
    t : FLOAT, optional
        Exposure time in seconds. The default is 1.0.
    EEF : FLOAT, optional
        Enclosed Energy Fraction of the source in the detection area. The default is 1.0.
    flag : INT, optional
        Allows choosing betwen using gammainc (0) or poisson (1). The default is 1.

    Returns
    -------
    Pdet : FLOAT
        Probability of detection of a source with countrate s above a background B with significance prob or higher

    """

    if(prob is None):
        prob=erf(5.0/np.sqrt(2))

    tau=t*EEF
    kdet=get_kdet(B,prob,flag)
    if (flag==0):
        Pdet=gammainc_here([kdet],0.0,B+s*tau,0.0)
    else:
        Pdet=poisson.sf(B+s*tau,kdet)
    return Pdet
