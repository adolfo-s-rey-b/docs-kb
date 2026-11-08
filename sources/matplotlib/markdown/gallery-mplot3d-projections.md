[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/projections.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/projections.html#sphx-glr-download-gallery-mplot3d-projections-py)
 to download the full example code.

3D plot projection types[#](https://matplotlib.org/stable/gallery/mplot3d/projections.html#d-plot-projection-types "Link to this heading")

===========================================================================================================================================

Demonstrates the different camera projections for 3D plots, and the effects of changing the focal length for a perspective projection. Note that Matplotlib corrects for the 'zoom' effect of changing the focal length.

The default focal length of 1 corresponds to a Field of View (FOV) of 90 deg. An increased focal length between 1 and infinity "flattens" the image, while a decreased focal length between 1 and 0 exaggerates the perspective and gives the image more apparent depth. In the limiting case, a focal length of infinity corresponds to an orthographic projection after correction of the zoom effect.

You can calculate focal length from a FOV via the equation:

\\\[1 / \\tan (\\mathrm{FOV} / 2)\\\]

Or vice versa:

\\\[\\mathrm{FOV} = 2 \\arctan (1 / \\mathrm{focal length})\\\]

import matplotlib.pyplot as plt

from mpl\_toolkits.mplot3d import axes3d

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, subplot\_kw\={'projection': '3d'})

\# Get the test data
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [axes3d.get\_test\_data](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.get_test_data.html#mpl_toolkits.mplot3d.axes3d.get_test_data "mpl_toolkits.mplot3d.axes3d.get_test_data")
(0.05)

\# Plot the data
for [ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [ax.plot\_wireframe](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_wireframe "mpl_toolkits.mplot3d.Axes3D.plot_wireframe")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, rstride\=10, cstride\=10)

\# Set the orthographic projection.
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_proj\_type('ortho')  \# FOV = 0 deg
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title("'ortho'\\nfocal\_length = ∞", fontsize\=10)

\# Set the perspective projections
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_proj\_type('persp')  \# FOV = 90 deg
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title("'persp'\\nfocal\_length = 1 (default)", fontsize\=10)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_proj\_type('persp', focal\_length\=0.2)  \# FOV = 157.4 deg
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_title("'persp'\\nfocal\_length = 0.2", fontsize\=10)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

!['ortho' focal_length = ∞, 'persp' focal_length = 1 (default), 'persp' focal_length = 0.2](https://matplotlib.org/stable/_images/sphx_glr_projections_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [styling: small-multiples](https://matplotlib.org/stable/_tags/styling-small-multiples.html)
 [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

[`Download Jupyter notebook: projections.ipynb`](https://matplotlib.org/stable/_downloads/6b6882ebe6f002faff15ebbc7324ba3c/projections.ipynb)

[`Download Python source code: projections.py`](https://matplotlib.org/stable/_downloads/9b22f16328066c6a0d023743cb5c6241/projections.py)

[`Download zipped: projections.zip`](https://matplotlib.org/stable/_downloads/31fa809eeea470f92f24f3c93e9ed9d2/projections.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)