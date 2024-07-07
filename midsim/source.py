from phenom.source import SASE_Source

import numpy as np
import scipy.constants

h = scipy.constants.physical_constants['Planck constant in eV s'][0]

def analytical_pulse_energy(q, photon_energy):
    """
    Estimate of analytical_pulse_energy from electron bunch charge and radiation energy

    :param q: electron bunch charge [nC]
    :param photon_energy: radiation energy [eV]

    :return P: pulse energy [J]
    """

    P = 19*q/photon_energy
    return P

def analytical_pulse_duration(q):
    """
    Estimate analytical_pulse_duration from electron bunch charge

    :param q: electron bunch charge [nC]

    :return t: Duration of pulse [s]
    """

    t = (q*1e3)/9.8
    return t*1e-15


def analytical_pulse_width(photon_energy):
    """
    Estimate analytical_pulse_width (FWHM) from radiation energy (assumes symmetrical beam)

    :param photon_energy: radiation energy [eV]

    :return sig: Radiation pulse width [m]
    """

    sig = np.log((7.4e03/(photon_energy/1e03)))*6
    return sig/1e6


def analytical_pulse_divergence(photon_energy):

    """
    Estimate of analytical_pulse_divergence (half-angle) from electron bunch charge and radiation energy

    :param q: electron bunch charge [nC]
    :param photon_energy: radiation energy [eV]

    :return dtheta: pulse divergence [rad]
    """
    return ((14.1)/((photon_energy/1e03)**0.75)) / 1e06

## wrap sase
def SA1_Source(photon_energy,
               beam_charge,
               nr = 512,
               nt = 512,
               bandwidth = 1e-12,
               x0 = 0.0,
               y0 = 0.0,
               t0 = 0.0,
               theta_x = 0.0,
               theta_y = 0.0):

    duration = analytical_pulse_duration(q = beam_charge)
    pulse_energy = analytical_pulse_energy(q = beam_charge, photon_energy = photon_energy)
    pulse_width = analytical_pulse_width(photon_energy = photon_energy)
    pulse_div = analytical_pulse_divergence(photon_energy = photon_energy)

    x = y = np.linspace(-pulse_width*4, pulse_width*4, nr)
    t = np.linspace(-duration*1.5, duration*1.5, nt)

    if type(pulse_width) == np.float64:
        pulse_width = float(pulse_width)

    ## define the pulse
    src = SASE_Source(x = x,
                      y = y,
                      t = t,
                      photon_energy = photon_energy,
                      pulse_energy = pulse_energy,
                      pulse_duration = duration,
                      bandwidth = bandwidth,
                      sigma = pulse_width,
                      div = pulse_div,
                      x0 = x0,
                      y0 = y0,
                      t0 = t0,
                      theta_x = theta_x,
                      theta_y = theta_y
                      )

    return src