import numpy as np
import plotly.graph_objs as go
from stl import mesh

def wind_line(stl_file):
    your_mesh = mesh.Mesh.from_file(stl_file)

    # Get the maximum and minimum z-coordinates of the mesh vertices
    z_min = your_mesh.min_[2]
    z_max = your_mesh.max_[2]
    translation_distance = (z_max - z_min) / 2
    translation_vector = np.array([-your_mesh.max_[0] / 2, 0, -translation_distance])
    your_mesh.vectors += translation_vector

    # Extract the vertex coordinates from the mesh
    x = your_mesh.x.flatten()
    y = your_mesh.y.flatten()
    z = your_mesh.z.flatten()

    # Create a scatter3d trace using the vertex coordinates
    trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=1,
            color=z,
            colorscale='Viridis',
            opacity=0.8
        )
    )

    # Create a layout for the plot
    layout = go.Layout(
        scene=dict(
            xaxis=dict(title='X (mm)'),
            yaxis=dict(title='Y (mm)'),
            zaxis=dict(title='Z (mm)')
        ),
        title='STL File Visualization'
    )

    # Create a figure and add the trace and layout
    fig = go.Figure(data=[trace], layout=layout)

    # Display the figure
    fig.show()

# Example usage
stl_file = 'example_mandrel.STL'  # Replace with your STL file
wind_line(stl_file)
