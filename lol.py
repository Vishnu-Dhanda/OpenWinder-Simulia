import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_cylinder(radius, height):
    return radius, height


def wind_line(cylinder_radius, cylinder_height, winding_angle):
    circumference = 2 * math.pi * cylinder_radius
    winding_length = circumference / math.tan(math.radians(winding_angle))
    num_windings = math.ceil(cylinder_height / winding_length)

    # Set seaborn style
    sns.set(style='whitegrid')

    # Plotting the cylinder
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection='3d')  # 3D plot
    ax2 = fig.add_subplot(122)  # 2D plot

    # Cylinder surface
    z = np.linspace(0, cylinder_height, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    Z, Theta = np.meshgrid(z, theta)
    X = cylinder_radius * np.cos(Theta)
    Y = cylinder_radius * np.sin(Theta)
    ax1.plot_surface(X, Y, Z, color='gray', edgecolors='k', linewidth=0.5, rcount=100, ccount=100, alpha=1)

    # Line winding
    num_points = int(num_windings * 100)
    theta_line = np.linspace(0, num_windings * 2 * np.pi, num_points)
    x_line = cylinder_radius * np.cos(theta_line)
    y_line = cylinder_radius * np.sin(theta_line)
    z_line = np.linspace(0, cylinder_height, num_points)
    ax1.plot(x_line, y_line, z_line, 'r-', linewidth=2)

    # 2D plot of the winding line
    ax2.plot(z_line, x_line, 'r-', linewidth=2)
    ax2.set_xlim(0, cylinder_height)
    ax2.set_ylim(-cylinder_radius, cylinder_radius)
    ax2.set_xlabel('Z')
    ax2.set_ylabel('X')
    ax2.set_title('Winding Line Projection')

    # Remove gridlines from the 2D plot
    ax2.grid(False)
    ax1.grid(False)

    # Set plot limits and labels for the 3D plot
    ax1.set_xlim(-cylinder_radius, cylinder_radius)
    ax1.set_ylim(-cylinder_radius, cylinder_radius)
    ax1.set_zlim(0, cylinder_height)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('Winding Line on Cylinder')

    # Add face lighting to the cylinder
    ax1.light_sources = [(1, 1, 1)]

    # Add cam lights
    ax1.view_init(elev=30, azim=0)
    plt.gcf().canvas.draw()
    ax1.view_init(elev=30, azim=210)
    plt.gcf().canvas.draw()
    ax1.view_init(elev=30, azim=330)
    plt.gcf().canvas.draw()

    plt.show()


# Example usage
radius = 5
height = 600
angle = 2

cylinder = create_cylinder(radius, height)
wind_line(cylinder[0], cylinder[1], angle)
