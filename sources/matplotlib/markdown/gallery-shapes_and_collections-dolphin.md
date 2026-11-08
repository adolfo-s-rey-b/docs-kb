[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html#sphx-glr-download-gallery-shapes-and-collections-dolphin-py)
 to download the full example code.

Dolphins[#](https://matplotlib.org/stable/gallery/shapes_and_collections/dolphin.html#dolphins "Link to this heading")

=======================================================================================================================

This example shows how to draw, and manipulate shapes given vertices and nodes using the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 and [`transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
 classes.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
, [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.transforms import [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(50)
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(50) \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 2.0
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
[circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((0, 0), 1, facecolor\='none',
                edgecolor\=(0, 0.8, 0.8), linewidth\=3, alpha\=0.5)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)

[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
((100, 100)),
                origin\='lower', cmap\="winter",
                interpolation\='spline36',
                extent\=(\-1, 1, \-1, 1))
[im.set\_clip\_path](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
([circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o', color\=(0.9, 0.9, 1.0), alpha\=0.8)

\# Dolphin from OpenClipart library by Andy Fitzsimon (Public Domain).

[dolphin](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= """
M -0.59739425,160.18173 C -0.62740401,160.18885 -0.57867129,160.11183
\-0.57867129,160.11183 C -0.57867129,160.11183 -0.5438361,159.89315
\-0.39514638,159.81496 C -0.24645668,159.73678 -0.18316813,159.71981
\-0.18316813,159.71981 C -0.18316813,159.71981 -0.10322971,159.58124
\-0.057804323,159.58725 C -0.029723983,159.58913 -0.061841603,159.60356
\-0.071265813,159.62815 C -0.080250183,159.65325 -0.082918513,159.70554
\-0.061841203,159.71248 C -0.040763903,159.7194 -0.0066711426,159.71091
0.077336307,159.73612 C 0.16879567,159.76377 0.28380306,159.86448
0.31516668,159.91533 C 0.3465303,159.96618 0.5011127,160.1771
0.5011127,160.1771 C 0.63668998,160.19238 0.67763022,160.31259
0.66556395,160.32668 C 0.65339985,160.34212 0.66350443,160.33642
0.64907098,160.33088 C 0.63463742,160.32533 0.61309688,160.297
0.5789627,160.29339 C 0.54348657,160.28968 0.52329693,160.27674
0.50728856,160.27737 C 0.49060916,160.27795 0.48965803,160.31565
0.46114204,160.33673 C 0.43329696,160.35786 0.4570711,160.39871
0.43309565,160.40685 C 0.4105108,160.41442 0.39416631,160.33027
0.3954995,160.2935 C 0.39683269,160.25672 0.43807996,160.21522
0.44567915,160.19734 C 0.45327833,160.17946 0.27946869,159.9424
\-0.061852613,159.99845 C -0.083965233,160.0427 -0.26176109,160.06683
\-0.26176109,160.06683 C -0.30127962,160.07028 -0.21167141,160.09731
\-0.24649368,160.1011 C -0.32642366,160.11569 -0.34521187,160.06895
\-0.40622293,160.0819 C -0.467234,160.09485 -0.56738444,160.17461
\-0.59739425,160.18173
"""

[vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[\]
[codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
[parts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [dolphin](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.split()
[i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 0
[code\_map](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'M': [Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
,
    'C': [Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
,
    'L': [Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
,
}

while [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 < len([parts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [path\_code](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
 \= [code\_map](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[parts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]\]
    [npoints](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [Path.NUM\_VERTICES\_FOR\_CODE](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[path\_code](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]
    [codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.extend(\[[path\_code](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\] \* [npoints](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [vertices.extend](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
(\[\[\*map(float, [y.split](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
(','))\]\
                     for [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 in [parts](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 + 1:\]\[:[npoints](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]\])
    [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 += [npoints](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1
[vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
([vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\] \-= 160

[dolphin\_path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[dolphin\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([dolphin\_path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, facecolor\=(0.6, 0.6, 0.6),
                          edgecolor\=(0.0, 0.0, 0.0))
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([dolphin\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)

[vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().rotate\_deg(60).transform([vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[dolphin\_path2](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[dolphin\_patch2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([dolphin\_path2](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, facecolor\=(0.5, 0.5, 0.5),
                           edgecolor\=(0.0, 0.0, 0.0))
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([dolphin\_patch2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![dolphin](https://matplotlib.org/stable/_images/sphx_glr_dolphin_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
    
*   [`matplotlib.patches.Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
    
*   [`matplotlib.transforms.Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
    
*   [`matplotlib.transforms.Affine2D.rotate_deg`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.rotate_deg "matplotlib.transforms.Affine2D.rotate_deg")
    

Tags: [component: patch](https://matplotlib.org/stable/_tags/component-patch.html)
 [styling: shape](https://matplotlib.org/stable/_tags/styling-shape.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

**Total running time of the script:** (0 minutes 1.281 seconds)

[`Download Jupyter notebook: dolphin.ipynb`](https://matplotlib.org/stable/_downloads/b4f7b74609121e23ec259b94a685c667/dolphin.ipynb)

[`Download Python source code: dolphin.py`](https://matplotlib.org/stable/_downloads/10d104944eed9df046d0a9efa3257590/dolphin.py)

[`Download zipped: dolphin.zip`](https://matplotlib.org/stable/_downloads/4e5c1b1e8a08c87d76685bf2f094a03f/dolphin.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)