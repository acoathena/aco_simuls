#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:24:41 2021

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


import numpy as np

def eef(r,HEW):
    """
    Calculates the Enclosed Energy Fraction out to a radius r given a Half Energy Width HEW,
        assumes a gaussian shape of the Point Spread Function (PSF)

    Parameters
    ----------
    r : FLOAT
        radius out to which to integrate the PSF (arcsec)
    HEW : FLOAT
        Half Energy Width of the PSF (in arcsec)

    Returns
    -------
    eef: FLOAT
       Enclosed Energy Fraction [0,1]

    """

    x= 4.0 * np.log(2.0) * (r/HEW)**2
    eef=1.0-np.exp(-x)
    return eef