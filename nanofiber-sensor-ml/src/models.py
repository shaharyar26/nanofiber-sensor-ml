"""
Reusable GPR model functions — imported by notebooks and Streamlit app.
"""
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, WhiteKernel, ConstantKernel as C


def build_kernel():
    return (
        C(1.0, constant_value_bounds=(0.01, 100))
        * Matern(length_scale=0.5, nu=2.5, length_scale_bounds=(0.01, 10))
        + WhiteKernel(noise_level=0.01, noise_level_bounds=(1e-5, 1))
    )


def fit_gpr(X_log, y, noise_sd, n_restarts=10, random_state=42):
    """Fit GPR model. X_log = log10(pressure), noise_sd = per-point SD."""
    gpr = GaussianProcessRegressor(
        kernel=build_kernel(),
        alpha=noise_sd**2,
        n_restarts_optimizer=n_restarts,
        normalize_y=True,
        random_state=random_state,
    )
    gpr.fit(X_log, y)
    return gpr


def predict(gpr, pressure_kpa):
    """Predict sensitivity at given pressures (kPa). Returns mean, std, ci95."""
    X_q = np.log10(np.atleast_1d(pressure_kpa)).reshape(-1, 1)
    mu, std = gpr.predict(X_q, return_std=True)
    return np.clip(mu, 0, None), std, 1.96 * std
