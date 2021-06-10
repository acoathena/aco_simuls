import papermill as pm

#
# Jupyter notebook Parameters definition
#
rmffile = "None"  # Filename with full path of the response file for the source spectrum
arffile = "None"  # Filename with full path of the auxiliary matrix file for the source spectrum
bgdfile = "None"  # Filename with full path of background spectrum
HEW = 5.7         # HEW of the PSF in arcsec
fHEW = 1.0        # Extraction radius for the source in units of fraction of the HEW
bgdArea = 78.54   # Background extraction area (arcsec2)
prob = 1.e-6      # Detection probability for limits (default=1-1e6)
Emin = 2.0        # Lower bound of the energy interval (keV)
Emax = 10.0       # Upper bound of the energy interval (keV)
NHGal = 0.018     # Foreground Galactic column density (1e22 cm-2)
NH = 0.020        # Column density (1e22cm-2)
Gamma =2.0        # Power law photon index
z = 0.            # Redshift
tmin = 1.e2       # Minimum value of the exposure time (s)
tmax = 1.e8       # Maximum value of the exposure time (s)
nt = 100          # Number of exposure time values to explore
SXlim = 1.21e-16  # Confusion flux limit (cgs)
outfile = 'outfile.txt' # Filename with the output exposure time and flux limits
pngfile = 'pngfile.png' # Filename with a plot with the above values


dict_params = dict(
    rmffile=rmffile,
    arffile=arffile,
    bgdfile=bgdfile,
    HEW=HEW,
    fHEW=fHEW,
    prob=prob,
    bgdArea=bgdArea,
    Emin=Emin,
    Emax=Emax,
    NHGal=NHGal,
    NH=NH,
    Gamma=Gamma,
    z=z,
    tmin=tmin,
    tmax=tmax,
    nt=nt,
    SXlim=SXlim,
    outfile=outfile,
    pngfile=pngfile
)

print("Running jupyter-notebook")
pm.execute_notebook(
    'Athena_Xray_flux_vs_expTime.ipynb',
    'output_notebook.ipynb',
    parameters = dict_params
)
print("=====================")
print("Processing terminated")
print("=====================")


