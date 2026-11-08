[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html#sphx-glr-download-gallery-mplot3d-custom-shaded-3d-surface-py)
 to download the full example code.

Custom hillshading in a 3D surface plot[#](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html#custom-hillshading-in-a-3d-surface-plot "Link to this heading")

=======================================================================================================================================================================================

Demonstrates using custom hillshading in a 3D surface plot.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook
from matplotlib.colors import [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")

\# Load and format data
[dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
 \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('jacksboro\_fault\_dem.npz')
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['elevation'\]
[nrows](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ncols](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [z.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['xmin'\], [dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['xmax'\], [ncols](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
([dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['ymin'\], [dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['ymax'\], [nrows](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[region](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [np.s\_](https://numpy.org/doc/stable/reference/generated/numpy.s_.html#numpy.s_ "numpy.s_")
\[5:50, 5:50\]
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[region](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[region](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\], [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[region](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\]

\# Set up plot
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(projection\='3d'))

[ls](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
 \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(270, 45)
\# To use a custom hillshading mode, override the built-in shading and pass
\# in the rgb colors of the shaded surface calculated from "shade".
[rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [ls.shade](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade "matplotlib.colors.LightSource.shade")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\=[plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["gist\_earth"\], vert\_exag\=0.1, blend\_mode\='soft')
[surf](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
 \= [ax.plot\_surface](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.Axes3D.plot_surface")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, rstride\=1, cstride\=1, facecolors\=[rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                       linewidth\=0, antialiased\=False, shade\=False)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![custom shaded 3d surface](https://matplotlib.org/stable/_images/sphx_glr_custom_shaded_3d_surface_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)
 [domain: cartography](https://matplotlib.org/stable/_tags/domain-cartography.html)

[`Download Jupyter notebook: custom_shaded_3d_surface.ipynb`](https://matplotlib.org/stable/_downloads/726191cdda9655ec6240e01a94b66a85/custom_shaded_3d_surface.ipynb)

[`Download Python source code: custom_shaded_3d_surface.py`](https://matplotlib.org/stable/_downloads/3b9ac21ecf6a0b30550b0fb236dcec5a/custom_shaded_3d_surface.py)

[`Download zipped: custom_shaded_3d_surface.zip`](https://matplotlib.org/stable/_downloads/4bc61410a2af3b415d1db7c3ae186fee/custom_shaded_3d_surface.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)