import papermill as pm
import argparse

progname = "Athena_Xray_flux_vs_expTime"
if __name__ == "__main__":
    desc='{}: Calculates the flux sensitivity in a given band as a function of exposure time '.format(progname)
    parser=argparse.ArgumentParser(description=desc)

    parser.add_argument("--rmffile",type=str, required=True,
                        help="Filename with full path of the response file for the source spectrum (required argument)"
    )
    parser.add_argument("--arffile",type=str, required=True,
                        help="Filename with full path of the auxiliary matrix file for the source spectrum (required argument)"
    )
    parser.add_argument("--bgdfile",type=str, required=True,
                        help="Filename with full path of background spectrum (required argument)"
    )
    parser.add_argument("--HEW",type=float, required=False,default=5.7,
                        help="HEW of the PSF in arcsec (default 5.7)"
    )
    parser.add_argument("--fHEW",type=float, required=False,default=1.0,
                        help="Extraction radius for the source in units of fraction of the HEW"
    )
    parser.add_argument("--bgdArea",type=float, required=False,default=78.54,
                        help="Backtround extraction area (arcsec2, default 78.54)"
    )
    parser.add_argument("--prob",type=float, required=False,default=1-1e6,
                        help="Detection probability for limits (default {})".format(1-1e-6)
    )
    parser.add_argument("--Emin",type=float, required=False,default=2.0,
                        help="Lower bound of the energy interval (keV, default 2.0)"
    )
    parser.add_argument("--Emax",type=float, required=False,default=10.0,
                        help="Upper bound of the energy interval (keV, default 10.0)"
    )
    parser.add_argument("--NHGal",type=float, required=False,default=0.018,
                        help="Foreground Galactic column density (1e22 cm-2, default 0.018)"
    )
    parser.add_argument("--NH",type=float, required=False,default=0.020,
                        help="Column density (1e22cm-2, default 0.020)")
    parser.add_argument("--Gamma",type=float, required=False,default=2.0,
                        help="Power law photon index (default 2.0)"
    )
    parser.add_argument("--z",type=float, required=False,default=0.0,
                        help="Redshift (default 0)"
    )
    parser.add_argument("--tmin",type=float, required=False,default=1e2,
                        help="Minimum value of the exposure time (s)"
    )
    parser.add_argument("--tmax",type=float, required=False,default=1e8,
                        help="Maximum value of the exposure time (s)")
    parser.add_argument("--nt",type=int, required=False,default=100,
                        help="Number of exposure time values to explore"
    )
    parser.add_argument("--SXlim",type=float, required=False,default=1.21e-16,
                        help="Confusion flux limit (cgs, default 1.21e-16)"
    )
    parser.add_argument("--outfile",type=str, required=False,default='outfile.txt',
                        help='Filename with the output exposure time and flux limits (default: outfile.txt)'
    )
    parser.add_argument("--pngfile",type=str, required=False,default='pngfile.png',
                        help='Filename with a plot with the above values (default pngfile.png)')

    inargs=parser.parse_args()

    dict_params = dict(
        rmffile=inargs.rmffile,
        arffile=inargs.arffile,
        bgdfile=inargs.bgdfile,
        HEW=inargs.HEW,
        fHEW=inargs.fHEW,
        prob=inargs.prob,
        bgdArea=inargs.bgdArea,
        Emin=inargs.Emin,
        Emax=inargs.Emax,
        NHGal=inargs.NHGal,
        NH=inargs.NH,
        Gamma=inargs.Gamma,
        z=inargs.z,
        tmin=inargs.tmin,
        tmax=inargs.tmax,
        nt=inargs.nt,
        SXlim=inargs.SXlim,
        outfile=inargs.outfile,
        pngfile=inargs.pngfile
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

