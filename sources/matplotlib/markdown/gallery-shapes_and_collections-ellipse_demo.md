[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html#sphx-glr-download-gallery-shapes-and-collections-ellipse-demo-py)
 to download the full example code.

Ellipse Demo[#](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html#ellipse-demo "Link to this heading")

====================================================================================================================================

Draw many ellipses. Here individual ellipses are drawn. Compare this to the [Ellipse collection example](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html)
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[NUM](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 250

[ells](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
(xy\=[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
(2) \* 10,\
                width\=[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
(), height\=[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
(),\
                [angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")\
\=[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
() \* 360)\
        for i in range([NUM](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 10), ylim\=(0, 10), aspect\="equal")

for [e](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
 in [ells](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([e](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
)
    [e.set\_clip\_box](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box")
([ax.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
)
    [e.set\_alpha](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_alpha "matplotlib.patches.Patch.set_alpha")
([np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
())
    [e.set\_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
([np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(3))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ellipse demo](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_001_2_00x.png)

Ellipse Rotated[#](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html#ellipse-rotated "Link to this heading")

==========================================================================================================================================

Draw many ellipses with different angles.

[angle\_step](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 45  \# degrees
[angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 180, [angle\_step](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-2.2, 2.2), ylim\=(\-2.2, 2.2), aspect\="equal")

for [angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
 in [angles](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((0, 0), 4, 2, [angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
\=[angle](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
, alpha\=0.1)
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ellipse demo](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
    
*   [`matplotlib.axes.Axes.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
    
*   [`matplotlib.artist.Artist.set_clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box")
    
*   [`matplotlib.artist.Artist.set_alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha")
    
*   [`matplotlib.patches.Patch.set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
    

[`Download Jupyter notebook: ellipse_demo.ipynb`](https://matplotlib.org/stable/_downloads/a3de40e57ef69c154a4856d1f21f1a53/ellipse_demo.ipynb)

[`Download Python source code: ellipse_demo.py`](https://matplotlib.org/stable/_downloads/31fa58ec8d6c8fd749693c492182e91e/ellipse_demo.py)

[`Download zipped: ellipse_demo.zip`](https://matplotlib.org/stable/_downloads/14a795d49aab094d4b83174f17418bf2/ellipse_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page