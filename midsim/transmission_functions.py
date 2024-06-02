import numpy as np

def transmission_function_homogeneous(thickness, x, y, wavelength, delta, beta):
    """
    Calculate the transmission function for a homogeneous sample.

    Parameters:
    thickness (ndarray): Thickness profile of the sample.
    x (ndarray): X-coordinates.
    y (ndarray): Y-coordinates.
    wavelength (float): Wavelength of the X-rays.
    delta (float): Real part related to refractive index decrement.
    beta (float): Imaginary part related to absorption.

    Returns:
    ndarray: Transmission function.
    """
    k = 2 * np.pi / wavelength
    return np.exp(-1j * k * delta * thickness) * np.exp(-k * beta * thickness)
