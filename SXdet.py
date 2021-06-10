#!/usr/bin/env python3
"""
Created on Fri Mar 19 20:32:20 2021

@author: @author: F.J. Carrera, S. Martinez-Núñez

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

from enclosed_energy_fraction import eef
import numpy as np
from stats import get_sdet

def SXdet_f(f,t,HEW,bgdRate,bgdArea,CR1,SX1,prob):
    """
    Function to calculate the flux of a source that would be detected above a background countrate 'bgdRate'
       with detection significance 'prob', taking into account the exposure time, the PSF and the
       relative extraction areas

    Parameters
    ----------
    f : FLOAT
        Extraction radius for the source in units of fraction of the HEW
    t : FLOAT
        Exposure time (s)
    HEW : FLOAT
        Half Energy Width of the Point Spread Function (PSF) in arcsec
    bgdRate : FLOAT
        background count rate over the background extraction area (ct/s)
    bgdArea : FLOAT
        Background extraction area
    CR1 : FLOAT
        Countrate for unit normalization of the model (ct/s)
    SX1 : FLOAT
        Flux for unit normalization of the model (cgs)
    prob: FLOAT
       Detection significance

    Returns
    -------
    SXdet : FLOAT
        Flux sensitivity (cgs)

    """

    r=f*HEW
    EEFr=eef(r,HEW)
    sArea=np.pi*r**2
    Cbgd=bgdRate*sArea/bgdArea *t

    Cdet=get_sdet(Cbgd,prob=prob,flag=0)
    factor=(Cdet/(t*EEFr))/CR1
    SXdet=SX1*factor
    return SXdet
