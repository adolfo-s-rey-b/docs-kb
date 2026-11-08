[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html#sphx-glr-download-gallery-lines-bars-and-markers-multivariate-marker-plot-py)
 to download the full example code.

Mapping marker properties to multivariate data[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html#mapping-marker-properties-to-multivariate-data "Link to this heading")

====================================================================================================================================================================================================================

This example shows how to use different properties of markers to plot multivariate datasets. Here we represent a successful baseball throw as a smiley face with marker size mapped to the skill of thrower, marker rotation to the take-off angle, and thrust to the marker color.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
from matplotlib.markers import [MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
from matplotlib.text import [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

[SUCCESS\_SYMBOLS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
((0, 0), "☹"),\
    [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
((0, 0), "😒"),\
    [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
((0, 0), "☺"),\
\]

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 25
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(42)
[skills](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(5, 80, size\=[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
) \* 0.1 + 5
[takeoff\_angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 90, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[thrusts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.uniform](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html#numpy.random.uniform "numpy.random.uniform")
(size\=[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[successful](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(0, 3, size\=[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[positions](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(size\=([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2)) \* 5
[data](https://docs.python.org/3/library/functions.html#zip "builtins.zip")
 \= zip([skills](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [takeoff\_angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [thrusts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [successful](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [positions](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["plasma"\]
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Throwing success", size\=14)
for [skill](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [takeoff](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [thrust](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [mood](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, [pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in [data](https://docs.python.org/3/library/functions.html#zip "builtins.zip")
:
    [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([skill](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
).rotate\_deg([takeoff](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
    [m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
 \= [MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
([SUCCESS\_SYMBOLS](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[mood](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\], transform\=[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], [pos](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], marker\=[m](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
, color\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([thrust](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
))
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([plt.cm.ScalarMappable](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable "matplotlib.colorizer._ScalarMappable")
(norm\=[Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(0, 1), [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
\="plasma"),
             [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, label\="Normalized Thrust \[a.u.\]")
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("X position \[m\]")
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Y position \[m\]")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Throwing success](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_001_2_00x.png)

Tags: [component: marker](https://matplotlib.org/stable/_tags/component-marker.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [styling: shape](https://matplotlib.org/stable/_tags/styling-shape.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

[`Download Jupyter notebook: multivariate_marker_plot.ipynb`](https://matplotlib.org/stable/_downloads/9f1f6b65b7e6be19a8d13e1b628d7044/multivariate_marker_plot.ipynb)

[`Download Python source code: multivariate_marker_plot.py`](https://matplotlib.org/stable/_downloads/0c9f82be1ea4cded0763a4430f4a0e83/multivariate_marker_plot.py)

[`Download zipped: multivariate_marker_plot.zip`](https://matplotlib.org/stable/_downloads/7f20d86781b3c2cd5011a465bf7ad97b/multivariate_marker_plot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)