[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html#sphx-glr-download-gallery-shapes-and-collections-ellipse-arrow-py)
 to download the full example code.

Ellipse with orientation arrow demo[#](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_arrow.html#ellipse-with-orientation-arrow-demo "Link to this heading")

===================================================================================================================================================================================

This demo shows how to draw an ellipse with an orientation arrow (clockwise or counterclockwise). Compare this to the [Ellipse collection example](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html)
.

import matplotlib.pyplot as plt

from matplotlib.markers import [MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

\# Create a figure and axis
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\={"aspect": "equal"})

[ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(
    xy\=(2, 4),
    width\=30,
    height\=20,
    angle\=35,
    facecolor\="none",
    edgecolor\="b"
)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
)

\# Plot an arrow marker at the end point of minor axis
[vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [ellipse.get\_co\_vertices](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.get_co_vertices "matplotlib.patches.Ellipse.get_co_vertices")
()
[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg([ellipse.angle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.angle "matplotlib.patches.Ellipse.angle")
)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(
    [vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\]\[0\],
    [vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\]\[1\],
    color\="b",
    marker\=[MarkerStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
(">", "full", [t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
),
    markersize\=10
)
\# Note: To reverse the orientation arrow, switch the marker type from > to <.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ellipse arrow](https://matplotlib.org/stable/_images/sphx_glr_ellipse_arrow_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
    

[`Download Jupyter notebook: ellipse_arrow.ipynb`](https://matplotlib.org/stable/_downloads/a3262b8c2b73257ec928a41efbf2c3ec/ellipse_arrow.ipynb)

[`Download Python source code: ellipse_arrow.py`](https://matplotlib.org/stable/_downloads/fb232f1d61103dbdcc09a95b875bcce7/ellipse_arrow.py)

[`Download zipped: ellipse_arrow.zip`](https://matplotlib.org/stable/_downloads/8ea200449280481d5dccca21ba7506d1/ellipse_arrow.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)