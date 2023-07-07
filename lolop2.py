import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patches as mpatches
from stl import mesh
from mpl_toolkits import mplot3d

def wind_line(stl_file):
    your_mesh = mesh.Mesh.from_file(stl_file)

    # Get the maximum and minimum z-coordinates of the mesh vertices
    z_min = your_mesh.min_[2]
    z_max = your_mesh.max_[2]
    translation_distance = (z_max - z_min) / 2
    translation_vector = np.array([-your_mesh.max_[0] / 2, 0, -translation_distance])
    your_mesh.vectors += translation_vector

    # Plotting the cylinder
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')  # 3D plot

    # Rotate the cylinder by 90 degrees around the z-axis
    ax1.view_init(elev=23, azim=45)

    # Add the mesh to the plot with black edge color
    ax1.add_collection3d(Poly3DCollection(your_mesh.vectors, facecolors='#d9d9d9', edgecolors='k'))

    # Set auto scaling of the plot
    ax1.auto_scale_xyz([-your_mesh.max_[0], your_mesh.max_[0]], [0, your_mesh.max_[1]], [-z_max, z_max])

    # Set plot limits and labels for the 3D plot
    ax1.set_xlim(-your_mesh.max_[0], your_mesh.max_[0])
    ax1.set_ylim(0, your_mesh.max_[1])
    ax1.set_zlim(-z_max, z_max)
    ax1.set_xlabel('X (mm)')
    ax1.set_ylabel('Y (mm)')
    ax1.set_zlabel('Z (mm)')
    ax1.set_title('First Pass On Cylinder')

    plt.show()

# Example usage
stl_file = 'unix.stl'  # Replace with your STL file
wind_line(stl_file)
