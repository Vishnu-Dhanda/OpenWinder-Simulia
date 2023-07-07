import plotly.graph_objects as go
import numpy as np
from stl import mesh
# Download data set from plotly repo


fig = go.Figure(data=[go.Mesh3d(x=[1], y=[1], z=[1], color='lightpink', opacity=1, showpoints=True,)])
fig.show()