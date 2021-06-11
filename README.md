# aco_simuls



[![DOI](https://zenodo.org/badge/352657169.svg)](https://zenodo.org/badge/latestdoi/352657169) [![CodeFactor](https://www.codefactor.io/repository/github/acoathena/aco_simuls/badge/main)](https://www.codefactor.io/repository/github/acoathena/aco_simuls/overview/main) 

Simulation tools developed by the [Athena Community Office](https://www.the-athena-x-ray-observatory.eu/) to determine the flux sensitivity in a given energy band for a given instrument of the Athena X-ray mission as a function of exposure time.

The programm can be run either executing (cell-by-cell) the jupyter-notebook ``Athena_Xray_flux_vs_expTime.ipynb`` or running the notebook from the command line. 

Before running the program, users need to install locally [HEASOFT](https://heasarc.gsfc.nasa.gov/docs/software/heasoft/) with [PyXspec](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/).

---

**Running the code**  
To run this notebook from the command line, use the script ``execute_notebook.py`` as follows:

    1.- Install [papermill](https://papermill.readthedocs.io/en/latest/)
    2.- Select the apropriate parameters in the script ``execute_notebook_inpars.py`` or read them 
    from the command line using in this case ``execute_notebook_outpars.py``
    3.- Run in command line:
        > python execute_notebook_inpars.py
    or
        > python execute_notebook_outpars.py --rmffile my.rmf --arffile my.arf --bgdfile my.bgdfile ...... 

**Input parameters**  
The meaning of the input parameters is as follows:

`rmffile` (str): Filename with full path of the response file for the source spectrum  
`arffile` (str): Filename with full path of the auxiliary matrix file for the source spectrum  
`bgdfile` (str): Filename with full path of sum background spectrum that it includes all components  
`HEW` (float): HEW of the PSF in arcsec (def. 5.7, WFI Field of View average for on-axis HEW=5 arcsec, for X-IFU or WFI on axis use 5 arcsec)  
`fHEW` (float): Extraction radius for the source in units of fraction of the HEW (default=1.0)  
`bgdArea` (float): Backtround extraction area (arcsec², default 78.54)  
`prob` (float): Detection significance for limits (default=1-1e6)  
`Emin` (float): Lower bound of the energy interval (keV, default 2.0)  
`Emax` (float): Upper bound of the energy interval (keV, default 10.0)  
`NHGal` (float): Foreground Galactic column density (1e22 cm-2, default 0.018)  
`NH` (float): Column density (1e22cm-2, default 0.020)  
`Gamma` (float): Power law photon index (default 2.0)  
`z` (float): Redshift (default 0)  
`tmin` (float): Minimum value of the exposure time (s; default=1e2)  
`tmax` (float): Maximum value of the exposure time (s; default=1e8)  
`nt` (int): Number of exposure time values to explore (default=100)  
`SXlim` (float): Confusion flux hard limit (cgs, default 1.21e-16 appropriate for 0.5-2 keV, 
for 2-10 keV use instead 2e-17 -James Aird, private communication-). This limit is a conservative 
assumption for the limit achieved over the entire field-of-view in the 0.5-2keV band. Different limits 
should be adopted depending on the desired sensitivity.  
`outfile` (str): Filename with the output exposure time and flux limits (default 'outfile.txt')  
`pngfile` (str): Filename with a plot with the above values (default 'pngfile.png')  
  
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

    - Athena/WFI point source, FoV-averaged (0.5-2 keV):

    > python execute_notebook_outpars.py --rmffile athena_wfi_rib2.3_B4C_20210218_wo_filter_FovAvg.rsp
    --arffile " " --bgdfile athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_wo_filter_FovAvg.pha --HEW 5.7
    --fHEW 0.67 --bgdArea 78.54 --prob 0.999999 --Emin 0.5 --Emax 2.0 --NHGal 0.018 --NH 0.020
    --Gamma 2.0 --z 6.0 --tmin 1e2 --tmax 1e8 --nt 100 --SXlim 2.0e-17
    --outfile FluxvsTexp_bgd_WFI_05_2keV.topcat --pngfile FluxvsTexp_bgd_WFI_05_2keV.png

    - Athena/WFI point source on-axis (2-10 keV):

    > python execute_notebook_outpars.py --rmffile athena_wfi_rib2.3_B4C_20210218_wo_filter_OnAxis.rsp
    --arffile " " --bgdfile athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_wo_filter_OnAxis.pha --HEW 5.7
    --fHEW 0.67 --bgdArea 78.54 --prob 0.999999 --Emin 2.0 --Emax 10.0 --NHGal 0.018 --NH 0.020
    --Gamma 2.0 --z 6.0 --tmin 1e2 --tmax 1e8 --nt 100 --SXlim 1.21e-16
    --outfile FluxvsTexp_bgd_WFI_2_10keV.topcat --pngfile FluxvsTexp_bgd_WFI_2_10keV.png

    - Athena/X-IFU point source (0.5-2 keV):

    > python execute_notebook_outpars.py --rmffile XIFU_CC_BASELINECONF_2018_10_10.rmf
    --arffile XIFU_CC_BASELINECONF_2018_10_10.arf
    --bgdfile Total_pointsources_XIFU_CC_BASELINECONF_2018_10_10.pha --HEW 5.7
    --fHEW 0.67 --bgdArea 78.54 --prob 0.999999 --Emin 0.5 --Emax 2.0 --NHGal 0.018 --NH 0.020
    --Gamma 2.0 --z 6.0 --tmin 1e2 --tmax 1e8 --nt 100 --SXlim 2.0e-17
    --outfile FluxvsTexp_bgd_XIFU_05_2keV.topcat --pngfile FluxvsTexp_bgd_XIFU_05_2keV.png
       
---

**Instruments files (response matrices and background files):**

    Athena/WFI: https://www.mpe.mpg.de/ATHENA-WFI/response_matrices.html
    Athena/X-IFU: http://x-ifu.irap.omp.eu/resources/for-the-community

**References for XSPEC**

    [XSPEC quick tutorial](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/quick.html)
    [XSPEC extended tutorial](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/extended.html)
    [XSPEC class reference](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/classes.html)
    [XSPEC python interface documentation](https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/PyXspec.pdf)
   
---
---

## Instituto de Física de Cantabria (CSIC-UC)

Funded by Agencia Estatal de Investigación, Unidad de Excelencia María de Maeztu, ref. MDM-2017-0765  
Funded by the Spanish Ministry MCIU under project RTI2018-096686-B-C21 (MCIU/AEI/FEDER, UE), co-funded by FEDER funds.  

![logos](./logos/logos_small.png)
