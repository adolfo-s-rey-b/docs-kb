[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html#sphx-glr-download-gallery-mplot3d-pathpatch3d-py)
 to download the full example code.

Draw flat objects in 3D plot[#](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html#draw-flat-objects-in-3d-plot "Link to this heading")

====================================================================================================================================================

Demonstrate using [`pathpatch_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d "mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d")
 to 'draw' shapes and text on a 3D plot.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
, [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
from matplotlib.text import [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
import mpl\_toolkits.mplot3d.art3d as art3d

def text3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, xyz, s, zdir\="z", size\=None, angle\=0, usetex\=False, \*\*kwargs):
    """
    Plots the string \*s\* on the Axes \*ax\*, with position \*xyz\*, size \*size\*,
    and rotation angle \*angle\*. \*zdir\* gives the axis which is to be treated as
    the third dimension. \*usetex\* is a boolean indicating whether the string
    should be run through a LaTeX subprocess or not.  Any additional keyword
    arguments are forwarded to \`.transform\_path\`.

    Note: zdir affects the interpretation of xyz.
    """
    x, y, z \= xyz
    if zdir \== "y":
        xy1, z1 \= (x, z), y
    elif zdir \== "x":
        xy1, z1 \= (y, z), x
    else:
        xy1, z1 \= (x, y), z

    text\_path \= [TextPath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
((0, 0), s, size\=size, usetex\=usetex)
    trans \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate(angle).translate(xy1\[0\], xy1\[1\])

    p1 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(trans.transform\_path(text\_path), \*\*kwargs)
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
(p1)
    [art3d.pathpatch\_2d\_to\_3d](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d "mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d")
(p1, z\=z1, zdir\=zdir)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='3d')

\# Draw a circle on the x=0 'wall'
[p](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.PathPatch3D.html#mpl_toolkits.mplot3d.art3d.PathPatch3D "mpl_toolkits.mplot3d.art3d.PathPatch3D")
 \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((5, 5), 3)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([p](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.PathPatch3D.html#mpl_toolkits.mplot3d.art3d.PathPatch3D "mpl_toolkits.mplot3d.art3d.PathPatch3D")
)
[art3d.pathpatch\_2d\_to\_3d](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d "mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d")
([p](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.PathPatch3D.html#mpl_toolkits.mplot3d.art3d.PathPatch3D "mpl_toolkits.mplot3d.art3d.PathPatch3D")
, z\=0, zdir\="x")

\# Manually label the axes
text3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, (4, \-2, 0), "X-axis", zdir\="z", size\=.5, usetex\=False,
       ec\="none", fc\="k")
text3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, (12, 4, 0), "Y-axis", zdir\="z", size\=.5, usetex\=False,
       angle\=[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2, ec\="none", fc\="k")
text3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, (12, 10, 4), "Z-axis", zdir\="y", size\=.5, usetex\=False,
       angle\=[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2, ec\="none", fc\="k")

\# Write a Latex formula on the z=0 'floor'
text3d([ax](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.Axes3D")
, (1, 5, 0),
       r"$\\displaystyle G\_{\\mu\\nu} + \\Lambda g\_{\\mu\\nu} = "
       r"\\frac{8\\pi G}{c^4} T\_{\\mu\\nu}  $",
       zdir\="z", size\=1, usetex\=True,
       ec\="none", fc\="k")

[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xlim "mpl_toolkits.mplot3d.Axes3D.set_xlim")
(0, 10)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_ylim "mpl_toolkits.mplot3d.Axes3D.set_ylim")
(0, 10)
[ax.set\_zlim](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.Axes3D.set_zlim")
(0, 10)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![pathpatch3d](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [component: label](https://matplotlib.org/stable/_tags/component-label.html)
 [level: advanced](https://matplotlib.org/stable/_tags/level-advanced.html)

[`Download Jupyter notebook: pathpatch3d.ipynb`](https://matplotlib.org/stable/_downloads/cafceb37c9397d60bd1f04da0c92c497/pathpatch3d.ipynb)

[`Download Python source code: pathpatch3d.py`](https://matplotlib.org/stable/_downloads/ab0fba45e231f940e29a0a3aacac8776/pathpatch3d.py)

[`Download zipped: pathpatch3d.zip`](https://matplotlib.org/stable/_downloads/c6376b9ad1559a0cd02d8152bb522a02/pathpatch3d.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)