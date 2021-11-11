# =============================================================================#
#                          MODEL DEFINITION FILE                              #
# =============================================================================#
import numpy as np
import bilby

# -----------------------------------------------------------------------------#
# Function defining the model.                                                #
#                                                                             #
#  pDict       = Dictionary of parameters, created by parsing inParms, below. #
#  lamSqArr_m2 = Array of lambda-squared values                               #
#  quArr       = Complex array containing the Re and Im spectra.              #
# -----------------------------------------------------------------------------#
def model(pDict, lamSqArr_m2):
    """Simple Faraday thin source."""

    # Calculate the complex fractional q and u spectra
    pArr = pDict["fracPol"] * np.ones_like(lamSqArr_m2)
    quArr = pArr * np.exp(
        2j * (np.radians(pDict["psi0_deg"]) + pDict["RM_radm2"] * lamSqArr_m2)
    )

    return quArr


# -----------------------------------------------------------------------------#
# Parameters for the above model.                                             #
#                                                                             #
# Each parameter is defined by a dictionary with the following keywords:      #
#   parname    ...   parameter name used in the model function above          #
#   label      ...   latex style label used by plotting functions             #
#   value      ...   value of the parameter if priortype = "fixed"            #
#   bounds     ...   [low, high] limits of the prior                          #
#   priortype  ...   "uniform", "normal", "log" or "fixed"                    #
#   wrap       ...   set > 0 for periodic parameters (e.g., for an angle)     #
# -----------------------------------------------------------------------------#
priors = {
    "fracPol": bilby.prior.Uniform(
        minimum=0.001, maximum=1.0, name="fracPol", latex_label="$p$"
    ),
    "psi0_deg": bilby.prior.Uniform(
        minimum=0,
        maximum=180.0,
        name="psi0_deg",
        latex_label="$\psi_0$ (deg)",
        boundary="periodic",
    ),
    "RM_radm2": bilby.prior.Uniform(
        minimum=-1100.0,
        maximum=1100.0,
        name="RM_radm2",
        latex_label="RM (rad m$^{-2}$)",
    ),
}
