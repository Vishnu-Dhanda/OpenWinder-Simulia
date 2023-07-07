import plotly.graph_objects as go
import numpy as np
import trimesh
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Load STL file using trimesh
stl_file = "path/to/your/stl/file.stl"
mesh = trimesh.load(stl_file)

# Filament winding parameters
radius = 1.0  # Radius of the winding path
angle_step = 5  # Angle step size between each winding revolution

# Calculate winding path
winding_path = []
angle = 0
while angle < 360:
    # Compute x and y coordinates for the winding path
    x = radius * np.cos(np.deg2rad(angle))
    y = radius * np.sin(np.deg2rad(angle))
    z = angle  # Use angle as z-coordinate for visualization purposes
    winding_path.append((x, y, z))
    angle += angle_step

# Generate filament windings by extruding the winding path along the mesh surface
filament_winding = []
for point in winding_path:
    direction = np.array([point[0], point[1], 0])  # Set z-component of the direction to 0
    transformed_points, _, _, _ = mesh.ray.intersects_location([np.array(point)], direction)
    filament_winding.append(transformed_points[0])

# Plot the mesh and filament winding using Plotly
fig = go.Figure(data=[
    go.Mesh3d(
        x=mesh.vertices[:, 0],
        y=mesh.vertices[:, 1],
        z=mesh.vertices[:, 2],
        i=mesh.faces[:, 0],
        j=mesh.faces[:, 1],
        k=mesh.faces[:, 2],
        color='lightblue',
        opacity=0.8,
        lighting=dict(ambient=0.7)
    ),
    go.Scatter3d(
        x=[point[0] for point in filament_winding],
        y=[point[1] for point in filament_winding],
        z=[point[2] for point in filament_winding],
        mode='lines',
        line=dict(color='red', width=2),
        name='Filament Winding'
    )
])

# Set layout properties
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False)
    ),
    showlegend=False
)

# Show the Plotly figure
fig.show()
