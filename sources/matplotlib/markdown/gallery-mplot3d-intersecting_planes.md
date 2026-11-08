[Skip to main content](https://matplotlib.org/stable/gallery/mplot3d/intersecting_planes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/mplot3d/intersecting_planes.html#sphx-glr-download-gallery-mplot3d-intersecting-planes-py)
 to download the full example code.

Intersecting planes[#](https://matplotlib.org/stable/gallery/mplot3d/intersecting_planes.html#intersecting-planes "Link to this heading")

==========================================================================================================================================

This examples demonstrates drawing intersecting planes in 3D. It is a generalization of [2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)
.

Drawing intersecting planes in [`mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d "mpl_toolkits.mplot3d")
 is complicated, because [`mplot3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d "mpl_toolkits.mplot3d")
 is not a real 3D renderer, but only projects the Artists into 3D and draws them in the right order. This does not work correctly if Artists overlap each other mutually. In this example, we lift the problem of mutual overlap by segmenting the planes at their intersections, making four parts out of each plane.

This examples only works correctly for planes that cut each other in halves. This limitation is intentional to keep the code more readable. Cutting at arbitrary positions would of course be possible but makes the code even more complex. Thus, this example is more a demonstration of the concept how to work around limitations of the 3D visualization, it's not a refined solution for drawing arbitrary intersecting planes, which you can copy-and-paste as is.

import matplotlib.pyplot as plt
import numpy as np

def plot\_quadrants(ax, array, fixed\_coord, cmap):
    """For a given 3d \*array\* plot a plane with \*fixed\_coord\*, using four quadrants."""
    [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= array.shape
    index \= {
        'x': ([nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2, slice(None), slice(None)),
        'y': (slice(None), [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2, slice(None)),
        'z': (slice(None), slice(None), [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2),
    }\[fixed\_coord\]
    plane\_data \= array\[index\]

    n0, n1 \= plane\_data.shape
    quadrants \= \[\
        plane\_data\[:n0 // 2, :n1 // 2\],\
        plane\_data\[:n0 // 2, n1 // 2:\],\
        plane\_data\[n0 // 2:, :n1 // 2\],\
        plane\_data\[n0 // 2:, n1 // 2:\]\
    \]

    min\_val \= array.min()
    max\_val \= array.max()

    cmap \= [plt.get\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
(cmap)

    for i, quadrant in enumerate(quadrants):
        facecolors \= cmap((quadrant \- min\_val) / (max\_val \- min\_val))
        if fixed\_coord \== 'x':
            Y, Z \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 // 2, 0:[nz](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 // 2\]
            X \= [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2 \* [np.ones\_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")
(Y)
            Y\_offset \= (i // 2) \* [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2
            Z\_offset \= (i % 2) \* [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2
            ax.plot\_surface(X, Y + Y\_offset, Z + Z\_offset, rstride\=1, cstride\=1,
                            facecolors\=facecolors, shade\=False)
        elif fixed\_coord \== 'y':
            X, Z \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 // 2, 0:[nz](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 // 2\]
            Y \= [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2 \* [np.ones\_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")
(X)
            X\_offset \= (i // 2) \* [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2
            Z\_offset \= (i % 2) \* [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2
            ax.plot\_surface(X + X\_offset, Y, Z + Z\_offset, rstride\=1, cstride\=1,
                            facecolors\=facecolors, shade\=False)
        elif fixed\_coord \== 'z':
            X, Y \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[0:[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 // 2, 0:[ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 // 2\]
            Z \= [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2 \* [np.ones\_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")
(X)
            X\_offset \= (i // 2) \* [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2
            Y\_offset \= (i % 2) \* [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
 // 2
            ax.plot\_surface(X + X\_offset, Y + Y\_offset, Z, rstride\=1, cstride\=1,
                            facecolors\=facecolors, shade\=False)

def figure\_3D\_array\_slices(array, cmap\=None):
    """Plot a 3d array using three intersecting centered planes."""
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    ax \= fig.add\_subplot(projection\='3d')
    ax.set\_box\_aspect(array.shape)
    plot\_quadrants(ax, array, 'x', cmap\=cmap)
    plot\_quadrants(ax, array, 'y', cmap\=cmap)
    plot\_quadrants(ax, array, 'z', cmap\=cmap)
    return fig, ax

[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 70, 100, 50
[r\_square](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[\-1:1:1j \* [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, \-1:1:1j \* [ny](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, \-1:1:1j \* [nz](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \*\* 2).sum(0)

figure\_3D\_array\_slices([r\_square](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\='viridis\_r')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![intersecting planes](https://matplotlib.org/stable/_images/sphx_glr_intersecting_planes_001_2_00x.png)

Tags: [plot-type: 3D](https://matplotlib.org/stable/_tags/plot-type-3d.html)
 [level: advanced](https://matplotlib.org/stable/_tags/level-advanced.html)

**Total running time of the script:** (0 minutes 2.094 seconds)

[`Download Jupyter notebook: intersecting_planes.ipynb`](https://matplotlib.org/stable/_downloads/da157336c39ca520002bfcc2a119f975/intersecting_planes.ipynb)

[`Download Python source code: intersecting_planes.py`](https://matplotlib.org/stable/_downloads/68e888ee31fb17abb06115e5c35bf104/intersecting_planes.py)

[`Download zipped: intersecting_planes.zip`](https://matplotlib.org/stable/_downloads/48f1d3bb6700bfe30a80e0129f424861/intersecting_planes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)