[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html#sphx-glr-download-gallery-images-contours-and-fields-quiver-simple-demo-py)
 to download the full example code.

Quiver Simple Demo[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_simple_demo.html#quiver-simple-demo "Link to this heading")

==========================================================================================================================================================

A simple example of a [`quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
 plot with a [`quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey")
.

For more advanced options refer to [Advanced quiver and quiverkey functions](https://matplotlib.org/stable/gallery/images_contours_and_fields/quiver_demo.html)
.

import matplotlib.pyplot as plt
import numpy as np

[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-10, 10, 1)
[Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-10, 10, 1)
[U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[q](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
 \= [ax.quiver](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.quiverkey](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey")
([q](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.Quiver.html#matplotlib.quiver.Quiver "matplotlib.quiver.Quiver")
, [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0.3, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=1.1, [U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=10,
             label\='Quiver key, length = 10', labelpos\='E')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![quiver simple demo](https://matplotlib.org/stable/_images/sphx_glr_quiver_simple_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
     / [`matplotlib.pyplot.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver")
    
*   [`matplotlib.axes.Axes.quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey")
     / [`matplotlib.pyplot.quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html#matplotlib.pyplot.quiverkey "matplotlib.pyplot.quiverkey")
    

[`Download Jupyter notebook: quiver_simple_demo.ipynb`](https://matplotlib.org/stable/_downloads/d0141c97ca8c36319384c707e7c5c3d7/quiver_simple_demo.ipynb)

[`Download Python source code: quiver_simple_demo.py`](https://matplotlib.org/stable/_downloads/5a48ca1008ec889cb849275558b036a9/quiver_simple_demo.py)

[`Download zipped: quiver_simple_demo.zip`](https://matplotlib.org/stable/_downloads/627f04740610855df8fa8e92e887cb1a/quiver_simple_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)