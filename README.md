[![DOI](https://zenodo.org/badge/352657169.svg)](https://zenodo.org/badge/latestdoi/352657169) [![CodeFactor](https://www.codefactor.io/repository/github/acoathena/aco_simuls/badge/main)](https://www.codefactor.io/repository/github/acoathena/aco_simuls/overview/main) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/062a6019b14646a682320d2187b281f6)](https://www.codacy.com/gh/acoathena/aco_simuls/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=acoathena/aco_simuls&amp;utm_campaign=Badge_Grade)

#### Achievements
[![SQAaaS badge](https://github.com/EOSC-synergy/SQAaaS/raw/master/badges/badges_150x116/badge_software_bronze.png)](https://eu.badgr.com/public/assertions/fH9-pDR2SKCi3Hb9MfO58A "SQAaaS bronze badge achieved") 

This repository contains the following simulation tools developed by the [Athena Community Office](https://www.the-athena-x-ray-observatory.eu/):

# NewAthena Xray flux vs exposure Time

Determine the flux sensitivity in a given energy band for a given instrument of the Athena X-ray mission as a function of exposure time.

The simulations can be done either running the notebook from the command line or executing (cell-by-cell) the jupyter-notebook ``Athena_Xray_flux_vs_expTime.ipynb``. For this case, the first cell also contains the option to make plots interactive by using ``matplotlib widgets`` in a jupyter-lab (provided [``ipympl``](https://github.com/matplotlib/ipympl) is installed. Simply uncomment the lines:

```import ipywidgets as widgets```   
```%matplotlib widget```


Before running the program, users need to install locally [HEASOFT](https://heasarc.gsfc.nasa.gov/docs/software/heasoft/) with [PyXspec](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/).

---

## Running the notebook 

You can run the notebook interactively (cell by cell using Jupyter Lab/Notebook, Visual Studio Code or your preferred IDE).   
To run the notebook end-to-end from the command line, use the script <code>execute_notebook.py</code>:

   <code> > python execute_notebook.py --rmffile my.rmf --arffile my.arf --bgdfile my.bgdfile ...... </code>  
   

**Input parameters**  
The meaning of the input parameters is as follows:

* __rmffile__ (str): Filename with full path of the response file for the source spectrum  
* __arffile__ (str): Filename with full path of the auxiliary matrix file for the source spectrum  
* __bgdfile__ (str): Filename with full path of sum background spectrum that it includes all components  
* __HEW__ (float): HEW of the PSF in arcsec (default 9.0)
* __fHEW__ (float): Extraction radius for the source in units of fraction of the HEW (default=1.0)   
* __bgdArea__ (float): Backtround extraction area (arcsec2, default 254.5)  
* __prob__ (float): Detection significance for limits (default=1-10⁻⁶)  
* __Emin__ (float): Lower bound of the energy interval (keV, default 2.0)  
* __Emax__ (float): Upper bound of the energy interval (keV, default 10.0)  
* __NHGal__ (float): Foreground Galactic column density (1e22 cm-2, default 0.018)  
* __NH__ (float): Column density (10²²cm⁻², default 0.020)  
* __Gamma__ (float): Power law photon index (default 2.0)  
* __z__ (float): Redshift (default 0)  
* __tmin__ (float): Minimum value of the exposure time (s; default=100)  
* __tmax__ (float): Maximum value of the exposure time (s; default=10⁸)  
* __nt__ (int): Number of exposure time values to explore (default=100)  
* __SXlim__ (float): Confusion flux hard limit (cgs, default 5.1e-17 appropriate for 0.5-2 keV -James Aird, private communication-). Different limits should be adopted depending on the desired sensitivity. 
* __outfile__ (str): Filename with the output exposure time and flux limits (default 'outfile.txt')  
* __pngfile__ (str): Filename with a plot with the above values (default 'pngfile.png')  

**Processing steps used in the code:**

    1. Importing libraries  
    2. Defining input parameters, derived parameters and Xspec parameters  
    3. Gettting background count rate in the reference band normalized to the source area  
    4. Determining counts, flux (cgs units; erg cm-2 s-1), confusion flux (cgs), 
    optimum extraction flux (cgs) & optimum extraction radius (arcsec) in the reference 
    band over a loop of exposure times  
    5. Output file with results: the information provided by the outpufile comprises: 
    Time_s, Flux_cgs, Flux_confusion_cgs, FluxOptimumExtraction_cgs & RadiusOptimumExtraction_arcsec  
    6. Plotting limiting sensitivity vs exposure time  

**Ready-to-use Examples:**  

    #  Athena Flux and Counts Determination

This program determines the flux sensitivity in a given energy band for a given instrument of the Athena X-ray mission as a function of exposure time

Authors: F.J. Carrera, S. Martínez-Núñez, M.T. Ceballos

**Athena Community Office**  
**Instituto de Física de Cantabria (CSIC-UC)**  
Funded by Agencia Estatal de Investigación, Unidad de Excelencia María de Maeztu, ref. MDM-2017-0765  
Funded by the Spanish Ministry MCIU under project RTI2018-096686-B-C21 (MCIU/AEI/FEDER, UE), co-funded by FEDER funds.    
Funded by the Spanish Ministry MCIU under project PID2021-122955OB-C41 funded by MICIU/AEI/
10.13039/501100011033 and by ERDF/EU.     
Funded by the Spanish Ministry MCIU under project PID2024-155779OB-C31 funded by MICIU/AEI/
10.13039/501100011033 and by ERDF/EU.


![logos](logos/logo_grant.jpg)

>__LICENSE__: This is free software: you can redistribute it and/or modify it under the terms of the  
>GNU General Public License as published by the Free Software Foundation, either version  
>3 of the License, or any later version. This software is distributed in the hope that it  
>will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of  
>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
>See the GNU General Public License for more details.  
>For a copy of the GNU General Public License see <http://www.gnu.org/licenses/>.

## Input Parameters:

* __rmffile__ (str): Filename with full path of the response file for the source spectrum  
* __arffile__ (str): Filename with full path of the auxiliary matrix file for the source spectrum  
* __bgdfile__ (str): Filename with full path of sum background spectrum that it includes all components  
* __HEW__ (float): HEW of the PSF in arcsec (default 9.0)
* __fHEW__ (float): Extraction radius for the source in units of fraction of the HEW (default=1.0)   
* __bgdArea__ (float): Backtround extraction area (arcsec2, default 254.5)  
* __prob__ (float): Detection significance for limits (default=1-10⁻⁶)  
* __Emin__ (float): Lower bound of the energy interval (keV, default 2.0)  
* __Emax__ (float): Upper bound of the energy interval (keV, default 10.0)  
* __NHGal__ (float): Foreground Galactic column density (1e22 cm-2, default 0.018)  
* __NH__ (float): Column density (10²²cm⁻², default 0.020)  
* __Gamma__ (float): Power law photon index (default 2.0)  
* __z__ (float): Redshift (default 0)  
* __tmin__ (float): Minimum value of the exposure time (s; default=100)  
* __tmax__ (float): Maximum value of the exposure time (s; default=10⁸)  
* __nt__ (int): Number of exposure time values to explore (default=100)  
* __SXlim__ (float): Confusion flux hard limit (cgs, default 5.1e-17 appropriate for 0.5-2 keV -James Aird, private communication-). Different limits should be adopted depending on the desired sensitivity. 
* __outfile__ (str): Filename with the output exposure time and flux limits (default 'outfile.txt')  
* __pngfile__ (str): Filename with a plot with the above values (default 'pngfile.png')  

## Processing steps:
    
   1. Importing libraries  
   2. Defining input parameters, derived parameters and Xspec parameters  
   3. Gettting background count rate in the reference band normalized to the source area  
   4. Determining counts, flux (cgs units - erg cm-2 s-1 -), confusion flux (cgs), optimum extraction flux (cgs) & optimum extraction radius (arcsec) in the reference band over a loop of exposure times  
   5. Output file with results: the information provided by the outpufile comprises: Time_s, Flux_cgs, Flux_confusion_cgs, FluxOptimumExtraction_cgs & RadiusOptimumExtraction_arcsec  
   6. Plotting limiting sensitivity vs exposure time: to make interactive plots (using matplotlib ``widgets`` provided ``ipympl`` is installed for jupyter-lab / VS Code) simply uncomment the lines:
   
      <code> import ipywidgets as widgets </code>  
      <code> %matplotlib widget  </code>

      
## Running the notebook 

You can run the notebook interactively (cell by cell using Jupyter Lab/Notebook, Visual Studio Code or your preferred IDE).   
To run the notebook end-to-end from the command line, use the script <code>execute_notebook.py</code>:

   <code> > python execute_notebook.py --rmffile my.rmf --arffile my.arf --bgdfile my.bgdfile ...... </code>  
   

### Examples:

   1. Athena/WFI point source, FoV-averaged (0.5-2 keV): 
    
    > python3 execute_notebook.py --rmffile NewAthena_WFI_13rows_LDA_wo_filter_FoVAvg_20260213.rsp  \
    --arffile " " --bgdfile NewAthena_WFI_13rows_LDA_20260410_bkgd_photon_wo_filter_FoVAvg.pha --HEW 9.0  \  
    --fHEW 0.67 --bgdArea 254.5 --prob 0.999999 --Emin 0.5 --Emax 2.0 --NHGal 0.018 --NH 0.020 \
    --Gamma 2.0 --z 6.0 --tmin 1e2 --tmax 1e8 --nt 100 --SXlim 5.1e-17 \  
    --outfile FluxvsTexp_bgd_WFI_05_2keV.topcat --pngfile FluxvsTexp_bgd_WFI_05_2keV.png                
     
   2. Athena/X-IFU point source (0.5-2 keV):
    
    > python3 execute_notebook.py --rmffile new_athena_xifu_rb_4eV_gaussian.rmf  \
    --arffile new_athena_xifu_rb_optical_filter.arf \
    --bgdfile new_athena_xifu_rb_nxb_1amin2.pha --HEW 9.0 \
    --fHEW 0.67 --bgdArea 78.54 --prob 0.999999 --Emin 0.5 --Emax 2.0 --NHGal 0.018 --NH 0.020  \
    --Gamma 2.0 --z 6.0 --tmin 1e2 --tmax 1e8 --nt 100 --SXlim 5.1e-17 \
    --outfile FluxvsTexp_bgd_XIFU_05_2keV.topcat --pngfile FluxvsTexp_bgd_XIFU_05_2keV.png \
    

The output (PNG) figures of these examples can be found in the ``test_examples`` folder.

---

**Instruments files (response matrices and background files):**

    [Athena/WFI matrices and background files](https://www.mpe.mpg.de/ATHENA-WFI/response_matrices.html)
    [Athena/X-IFU matrices and background files](http://x-ifu.irap.omp.eu/resources/for-the-community)

**References for XSPEC**

    [XSPEC quick tutorial](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/quick.html)
    [XSPEC extended tutorial](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/extended.html)
    [XSPEC class reference](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/classes.html)
    [XSPEC python interface documentation](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/PyXspec.pdf)
   
---
---

### Instituto de Física de Cantabria (CSIC-UC)

Grant PID2021-122955OB-C41 funded by MCIN/AEI/10.13039/501100011033 and by “ERDF A way of making Europe”

![logos](./logos/logos_small.png)
