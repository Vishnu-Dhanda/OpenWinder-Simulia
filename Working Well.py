import plotly.graph_objects as go
import trimesh
import numpy as np


def plot_stl_mesh(stl_file, winding_angle):
    # Load the STL file
    mesh = trimesh.load_mesh(stl_file)

    # Get the vertices and faces from the mesh
    vertices = mesh.vertices
    faces = mesh.faces
    
    # Calculate the center of the mesh
    center = np.mean(vertices, axis=0)

    # Shift the vertices to place x and z axis at the center
    vertices[:, 0] -= center[0]
    vertices[:, 2] -= center[2]

    lighting_effects = dict(ambient=0.8, diffuse=0.2, specular=0.4, fresnel=0.2)
    
    # Create a plotly mesh object
    mesh_plot = go.Mesh3d(
        x=vertices[:, 0],
        y=vertices[:, 1],
        z=vertices[:, 2],
        i=faces[:, 0],
        j=faces[:, 1],
        k=faces[:, 2],
        color='#d9d9d9',
        opacity=1,
        lighting=lighting_effects,
        flatshading=True
    )
    
    # Calculate the winding vectors based on the specified angle
    theta = np.radians(winding_angle)
    wind_vectors = np.tile(np.array([np.cos(theta), np.sin(theta), 0]), (len(vertices), 1))
    
    # Add the winding vectors to the vertices
    vertices += wind_vectors

    # Create the figure and add the mesh trace
    fig = go.Figure(data=[mesh_plot])
    
    # Find the maximum values in each direction
    max_x = np.max(vertices[:, 0])
    max_y = np.max(vertices[:, 1])
    max_z = np.max(vertices[:, 2])
    fig.update_scenes(aspectmode='data', xaxis_showgrid=True, yaxis_showgrid=True, zaxis_showgrid=True)
    fig.update_scenes(xaxis_gridwidth=0.7, yaxis_gridwidth=0.7, zaxis_gridwidth=0.7)

    # Add the following lines to set the gridline and background colors
    fig.update_layout(scene=dict(
        xaxis=dict(gridcolor='black'),
        yaxis=dict(gridcolor='black'),
        zaxis=dict(gridcolor='black'),
        bgcolor='white'
    ))

    # Set camera parameters to zoom and fit the entire graph
    camera = dict(
        eye=dict(x=2, y=2, z=2)  # Adjust the values to change the zoom level
    )
    fig.update_layout(scene_camera=camera)
    
    # Show the figure
    fig.show()


# Example usage
stl_file_path = "Part1.stl"
winding_angle_degrees = 45
plot_stl_mesh(stl_file_path, winding_angle_degrees)
