### Incident Wavefield

Assume an incident wavefield \(\psi_i(x,y)\), which can have any form, not restricted to plane waves:

\[ \psi_i(x,y) \]

### Sample Transmission Function

The sample is characterized by a transmission function \(T(x,y)\), which may include both amplitude and phase modifications:

\[ T(x,y) = A_T(x,y) e^{i \phi(x,y)} \]

where:

- \(A_T(x,y)\) is the amplitude modulation by the sample.
- \(\phi(x,y)\) is the phase shift introduced by the sample.

### Modified Wavefield After Interaction with the Sample

When the incident wavefield \(\psi_i(x,y)\) interacts with the sample, the transmitted wavefield \(\psi_t(x,y)\) is:

\[ \psi_t(x,y) = \psi_i(x,y) T(x,y) = \psi_i(x,y) A_T(x,y) e^{i \phi(x,y)} \]

### Scattered Wavefield

To describe the scattered wavefield \(\psi_s\) resulting from this interaction, we use the Huygens-Fresnel principle, which states that every point on a wavefront can be considered a source of secondary spherical wavelets. The resultant wavefield is the superposition of these secondary wavelets.

### General Scattering Equation

The scattered wavefield \(\psi_s(x',y')\) at a point \((x',y')\) can be expressed as an integral over the contributions from each point \((x,y)\) in the sample:

\[ \psi_s(x',y') = \iint \frac{\psi_t(x,y)}{r} e^{ikr} dx dy \]

where:

- \(k\) is the wavenumber.
- \(r\) is the distance between the point \((x,y)\) in the sample and the observation point \((x',y')\).

The distance \(r\) can be approximated in the far-field (Fraunhofer approximation) or near-field (Fresnel approximation) regimes. For a general treatment, we use the exact expression:

\[ r = \sqrt{(x' - x)^2 + (y' - y)^2 + z^2} \]

where \(z\) is the distance along the propagation direction.

### Integral Form of the Scattered Field

Using the exact form of \(r\), the scattered wavefield is:

\[ \psi_s(x',y') = \iint \frac{\psi_i(x,y) A_T(x,y) e^{i \phi(x,y)}}{\sqrt{(x' - x)^2 + (y' - y)^2 + z^2}} e^{ik \sqrt{(x' - x)^2 + (y' - y)^2 + z^2}} dx dy \]

### Simplifying Assumptions

For practical purposes, the exact expression can often be simplified using approximations. If we assume the far-field (Fraunhofer approximation), the phase factor can be linearized, and the distance \(r\) can be approximated as:

\[ r \approx z \left(1 + \frac{(x' - x)^2 + (y' - y)^2}{2z^2}\right) \]

leading to a simplified expression for the scattered wavefield:

\[ \psi_s(x',y') \approx \frac{e^{ikz}}{z} \iint \psi_i(x,y) A_T(x,y) e^{i \phi(x,y)} e^{ik \left( \frac{(x' - x)^2 + (y' - y)^2}{2z} \right)} dx dy \]

### Intensity of the Scattered Wavefield

The intensity of the scattered wavefield is given by:

\[ I_s(x',y') = \left| \psi_s(x',y') \right|^2 \]

### Summary

The scattering of a general wavefield \(\psi(x,y)\) from a sample \(T(x,y)\) can be described b

