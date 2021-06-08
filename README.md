# aco_simuls

Simulation tools developed by the Athena Community Office to determine the flux sensitivity in a given energy band for a given instrument of the Athena X-ray mission as a function of exposure time.

The programm can be run either executing the jupyter-notebook Athena_Xray_flux_vs_expTime.ipynb or running the notebook from the command line. 

Before excuting the program, users need to install locally HEASOFT with pyxspec.

To run this notebook from the command line, use the script execute_notebook.py:

    Install papermill (https://papermill.readthedocs.io/en/latest/)
    Select the apropriate parameters in the script execute_notebook_inpars.py or read them from the command line using execute_notebook_outpars.py
    Run in command line
     > python execute_notebook_inpars.py 
    or
     > python execute_notebook_outpars.py --rmffile my.rmf --arffile my.arf --bgdfile my.bgdfile ...... 

Examples:

    Athena/WFI point source, FoV-averaged:

    > python execute_notebook_outpars.py --rmffile athena_wfi_rib2.3_B4C_20210218_wo_filter_FovAvg.rsp
    --arffile " " --bgdfile athena_wfi_rib2.3_B4C_20190502_bkgd_sum_psf_wo_filter_FovAvg.pha --HEW 5.7
    --fHEW 0.67 --bgdArea 78.54 --prob 0.999999 --Emin 0.5 --Emax 2.0 --NHGal 0.018 --NH 0.020
    --Gamma 2.0 --z 6.0 --tmin 1e2 --tmax 1e8 --nt 100 --SXlim 2.0e-17
    --outfile FluxvsTexp_bgd_WFI_05_2keV.topcat --pngfile FluxvsTexp_bgd_WFI_05_2keV.png

    Athena/WFI point source on-axis:

    > python execute_notebook_outpars.py --rmffile athena_wfi_rib2.3_B4C_20210218_wo_filter_OnAxis.rsp
    --arffile " " --bgdfile athena_wfi_rib2.3_B4C_20190502_bkgd_sum_psf_wo_filter_OnAxis.pha [...]

    Athena/X-IFU point source:

    > python execute_notebook_outpars.py --rmffile XIFU_CC_BASELINECONF_2018_10_10.rmf
    --arffile XIFU_CC_BASELINECONF_2018_10_10.arf
    --bgdfile Total_pointsources_XIFU_CC_BASELINECONF_2018_10_10.pha [...]

Instruments files (response matrices and background files):

    Athena/WFI: https://www.mpe.mpg.de/ATHENA-WFI/response_matrices.html
    Athena/X-IFU: http://x-ifu.irap.omp.eu/resources/for-the-community

References for XSPEC

    XSPEC quick tutorial https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/quick.html
    XSPEC extended tutorial https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/extended.html
    XSPEC class reference https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/html/classes.html
    XSPEC python interface documentation https://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/python/PyXspec.pdf
   
**Instituto de Física de Cantabria (CSIC-UC)**  

Funded by Agencia Estatal de Investigación, Unidad de Excelencia María de Maeztu, ref. MDM-2017-0765  
Funded by the Spanish Ministry MCIU under project RTI2018-096686-B-C21 (MCIU/AEI/FEDER, UE), co-funded by FEDER funds.  

![logos](./logos/logos_small.png)
