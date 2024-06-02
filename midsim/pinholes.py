import numpy as np
import matplotlib.pyplot as plt



def rotate_coordinates(x, y, angle):
    """
    Rotate coordinates by a given angle.

    Parameters:
    x (ndarray): X-coordinates.
    y (ndarray): Y-coordinates.
    angle (float): Angle in degrees to rotate the coordinates.

    Returns:
    ndarray, ndarray: Rotated X and Y coordinates.
    """
    radians = np.radians(angle)
    cos_angle = np.cos(radians)
    sin_angle = np.sin(radians)
    x_rot = cos_angle * x - sin_angle * y
    y_rot = sin_angle * x + cos_angle * y
    return x_rot, y_rot

def polygon(x, y, pinhole_radius, n, pinhole_separation, rotation=0, inverse=False):
    """
    Create a polygon pattern with pinholes.

    Parameters:
    x (ndarray): X-coordinates.
    y (ndarray): Y-coordinates.
    pinhole_radius (float): Radius of each pinhole.
    n (int): Number of sides (or pinholes) of the polygon.
    pinhole_separation (float): Distance of the pinholes from the center of the polygon.
    rotation (float): Rotation angle of the polygon in degrees (default is 0).
    inverse (bool): If True, the pattern is inverted (default is False).

    Returns:
    ndarray: Array representing the thickness pattern of the polygon.
    """
    x_rot, y_rot = rotate_coordinates(x, y, rotation)
    
    if n == 1:
        # Special case for a single pinhole at the central position specified by pinhole_separation
        x_pinhole = pinhole_separation
        y_pinhole = 0
        pinhole = (x_rot - x_pinhole)**2 + (y_rot - y_pinhole)**2 <= pinhole_radius**2
        polygon = pinhole
    else:
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
        polygon = np.zeros_like(x, dtype=bool)
        for angle in angles:
            x_pinhole = pinhole_separation * np.cos(angle)
            y_pinhole = pinhole_separation * np.sin(angle)
            pinhole = (x_rot - x_pinhole)**2 + (y_rot - y_pinhole)**2 <= pinhole_radius**2
            polygon = polygon | pinhole

    thickness = np.where(polygon, 1.0, 0.0) if inverse else np.where(polygon, 0.0, 1.0)
    return thickness


if __name__ == '__main__':
    # Example usage
    x = np.linspace(-0.0002, 0.0002, 1000)
    y = np.linspace(-0.0002, 0.0002, 1000)
    X, Y = np.meshgrid(x, y)

    # Create a 3x3 grid of shapes with increasing n
    fig, axs = plt.subplots(3, 3, figsize=(6, 6))
    for i in range(3):
        for j in range(3):
            n = i * 3 + j + 1
            thickness = polygon(X, Y, pinhole_radius=1e-5, n=n, pinhole_separation=5e-5, rotation=0, inverse=True)
            axs[i, j].imshow(thickness, extent=(-0.0002, 0.0002, -0.0002, 0.0002))
            axs[i, j].set_title(f'n={n}')
            axs[i, j].axis('off')

    plt.tight_layout()
    plt.show()
