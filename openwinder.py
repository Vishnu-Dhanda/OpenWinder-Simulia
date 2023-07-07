import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.patches as mpatches

def create_cylinder(radius, height):
    return radius, height

def wind_line(cylinder_radius, cylinder_height, winding_angle):

    circumference = 2 * math.pi * cylinder_radius
    winding_length = circumference / math.tan(math.radians(winding_angle))
    num_windings = math.ceil(cylinder_height / winding_length)

    # Plotting the cylinder
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')  # 3D plot

    # Rotate the cylinder by 90 degrees around the z-axis
    ax1.view_init(elev=23, azim=45)

    # Cylinder surface
    theta = np.linspace(0, 2 * np.pi, 100)
    y = np.linspace(0, cylinder_height, 100)
    Y, Theta = np.meshgrid(y, theta)
    X = (cylinder_radius-2) * np.cos(Theta)
    Z = (cylinder_radius-2) * np.sin(Theta)
    mandrel = ax1.plot_surface(X, Y, Z, color='#d9d9d9', edgecolor='none')

    # Line winding
    num_points = int(num_windings * 100)
    theta_line = np.linspace(0, num_windings * 2 * np.pi, num_points)
    x_line = (cylinder_radius + 1) * np.cos(theta_line)  
    z_line = (cylinder_radius + 1) * np.sin(theta_line)  
    y_line = np.linspace(0, cylinder_height, num_points)
    tow = ax1.plot(x_line, y_line, z_line, color='#333333', linewidth=4, zorder=10)
    ax1.grid(False)

    # Set plot limits and labels for the 3D plot
    ax1.set_xlim(-cylinder_radius, cylinder_radius)
    ax1.set_ylim(0, cylinder_height)
    ax1.set_zlim(-cylinder_radius, cylinder_radius)
    ax1.set_xlabel('X (mm)')
    ax1.set_ylabel('Y (mm)')
    ax1.set_zlabel('Z (mm)')
    ax1.set_title('First Pass On Cylinder')

    # Create legend
    legend_labels = ['Mandrel', 'Tow']
    legend_handles = [
        mpatches.Patch(color='#d9d9d9', alpha=1),
        Line3DCollection([tow[0].get_data()], colors='#333333', linewidths=3)
    ]
    ax1.legend(legend_handles, legend_labels)

    # Adjust the aspect ratio of the plot
    ax1.set_box_aspect([1, cylinder_height / (cylinder_height - (cylinder_height / 2)), 1])

    plt.show()


radius = 150
height = 3000
angle = 70

cylinder = create_cylinder(radius, height)
wind_line(cylinder[0], cylinder[1], angle)
