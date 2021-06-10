#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:28:40 2021

@authors: F.J. Carrera, S. Martinez-Núñez
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
"""

from xspec import Model, FakeitSettings

def getModelCR(AllModels,AllData,smodel,pars,rmffile,arffile,intervals,sname='mod1234',Texp=1e9):
    """
           Count rate for the given spectral model in the given energy interval(s)

    Parameters
    ----------
    AllModels : pyXspec container
        PyXspec automatically creates a single object of xspec.ModelManager, named AllModels
    AllData : pyXspec parameter
        Spectral data container. PyXspec automatically creates a single object of class xspec.DataManager, named AllData
    smodel : pyXspec container
        The model expression string, using full component names
    pars : LIST
        Parameters of the given spectral model
    rmffile : STRING
        Filename with full path of the response file for the source spectrum
    arffile : STRING
        Filename with full path of the auxiliary response file for the source spectrum
    intervals : LIST of lists
        Energy interval as: [Emin, Emax]
        Emin (float): Lower bound of the energy interval (keV)
        Emax (float): Upper bound of the energy interval (keV)
        e.g., [[0.5,2.0]] for 0.5-2keV
              [[0.5,2.0],[2.0,10.0]] for 0.5-2 keV and 2-10 keV
    sname : STRING, optional
        Name of the spectral model. The default is 'mod1234'
    Texp : FLOAT, optional
        Exposure time in s. The default is 1e9

    Returns
    -------
    countrates : FLOAT
        Count rate for the given spectral model in the given energy interval(s) in counts per second

    """

    mymodel=Model(smodel,sname)
    AllModels.setPars(mymodel,pars)

    if (len(arffile)==0):

        rspfile=rmffile
        fs1=FakeitSettings(rspfile,exposure=Texp)
    else:
        fs1=FakeitSettings(rmffile, arffile, exposure=Texp)

    AllData.fakeit(1,fs1,applyStats=False,noWrite=True)

    spec=AllData(1)
    countrates=[]
    for i in range(len(intervals)):
        spec.notice("all")
        srange="0.0-{} {}-**".format(intervals[i][0],intervals[i][1])
        spec.ignore(srange)
        countrates.append(spec.rate[3])

    AllModels-=sname
    del fs1
    AllData -= spec
    del spec

    return countrates

def getModelLum(AllModels,smodel,pars,intervals,z,sname='mod1234'):
    """
    Luminosity in the required energy intervals

    Parameters
    ----------
    AllModels : pyXspec container
        PyXspec automatically creates a single object of xspec.ModelManager, named AllModels
    smodel : pyXspec container
        The model expression string, using full component names
    pars : LIST
        Parameters of the given spectral model
    intervals :LIST of lists
        Energy interval as: [Emin, Emax]
        Emin (float): Lower bound of the energy interval (keV, default 2.0)
        Emax (float): Upper bound of the energy interval (keV, default 10.0)
        e.g., [[0.5,2.0]] for 0.5-2keV
              [[0.5,2.0],[2.0,10.0]] for 0.5-2 keV and 2-10 keV
    z : FLOAT
        Redshift (default 0)
    sname : STRING, optional
        Name of the spectral model. The default is 'mod1234'.

    Returns
    -------
    luminosities : pyXspec attribute
        Luminosity(ies) in the required energy interval(s) in erg s-1 units

    """
    mymodel=Model(smodel,sname)
    AllModels.setPars(mymodel,pars)
    AllModels.setEnergies("0.01 100 10000")
    luminosities=[]

    for i in range(len(intervals)):
        AllModels.calcLumin('{0:f} {1:f} {2:f}'.format(intervals[i][0],intervals[i][1],z))
        lum=AllModels(1,sname).lumin[0]*1e44
        luminosities.append(lum)

    AllModels.setEnergies("reset")
    AllModels-=sname

    return luminosities

def getModelFlux(AllModels,smodel,pars,intervals,sname='mod1234'):
    """

    Flux for the given model in the required band in cgs units (erg cm-2 s-1)

    Parameters
    ----------
    AllModels : pyXspec container
        PyXspec automatically creates a single object of xspec.ModelManager, named AllModels
    smodel : pyXspec container
        The model expression string, using full component names
    pars : LIST
        Parameters of the given spectral model
    intervals :LIST of lists
        Energy interval as: [Emin, Emax]
        Emin (float): Lower bound of the energy interval (keV, default 2.0)
        Emax (float): Upper bound of the energy interval (keV, default 10.0)
        e.g., [[0.5,2.0]] for 0.5-2keV
              [[0.5,2.0],[2.0,10.0]] for 0.5-2 keV and 2-10 keV
    sname : STRING, optional
        Name of the spectral model. The default is 'mod1234'

    Returns
    -------
    fluxes : pyXspec attribute
       Flux(es) in required energy interval(s) in erg cm-2 s-1

    """

    mymodel=Model(smodel,sname)
    AllModels.setPars(mymodel,pars)
    AllModels.setEnergies("0.01 100 10000")

    fluxes=[]
    for i in range(len(intervals)):
        AllModels.calcFlux('{0:f} {1:f}'.format(intervals[i][0],intervals[i][1]))
        flux=AllModels(1,sname).flux[0]
        fluxes.append(flux)

    AllModels.setEnergies("reset")
    AllModels-=sname

    return fluxes