[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html#sphx-glr-download-gallery-shapes-and-collections-quad-bezier-py)
 to download the full example code.

Bezier curve[#](https://matplotlib.org/stable/gallery/shapes_and_collections/quad_bezier.html#bezier-curve "Link to this heading")

===================================================================================================================================

This example showcases the [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 object to create a Bezier polycurve path patch.

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches
import matplotlib.path as mpath

[Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pp1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [mpatches.PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(
    [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(\[(0, 0), (1, 0), (1, 1), (0, 0)\],
         \[[Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [Path.CURVE3](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [Path.CURVE3](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]),
    fc\="none", transform\=[ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)

[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([pp1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0.75\], \[0.25\], "ro")
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('The red point should be on the path')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![The red point should be on the path](https://matplotlib.org/stable/_images/sphx_glr_quad_bezier_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    

[`Download Jupyter notebook: quad_bezier.ipynb`](https://matplotlib.org/stable/_downloads/d66c3af865863890580b2d3a7257664d/quad_bezier.ipynb)

[`Download Python source code: quad_bezier.py`](https://matplotlib.org/stable/_downloads/64b72931ba7d2523dcf12bc573b095f0/quad_bezier.py)

[`Download zipped: quad_bezier.zip`](https://matplotlib.org/stable/_downloads/d13c768f09fad23dfab5aa7cce2c0268/quad_bezier.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)