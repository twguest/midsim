import numpy as np

def fresnel_diffraction(psi, x, y, z, wavelength):
    """
    Calculate the Fresnel diffraction of a wavefield.

    Parameters:
    psi (ndarray): Incident wavefield.
    x (ndarray): X-coordinates.
    y (ndarray): Y-coordinates.
    z (float): Propagation distance.
    wavelength (float): Wavelength of the X-rays.

    Returns:
    ndarray: Scattered wavefield.
    """
    fx = np.fft.fftfreq(x.shape[1], d=(x[0,1] - x[0,0]))
    fy = np.fft.fftfreq(y.shape[0], d=(y[1,0] - y[0,0]))
    FX, FY = np.meshgrid(fx, fy)
    H = np.exp(-1j * np.pi * wavelength * z * (FX**2 + FY**2))
    psi_ft = np.fft.fft2(psi)
    psi_s = np.fft.ifft2(psi_ft * H)
    return psi_s
