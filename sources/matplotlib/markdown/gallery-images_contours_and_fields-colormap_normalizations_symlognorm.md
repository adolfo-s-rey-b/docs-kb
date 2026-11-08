[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations_symlognorm.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations_symlognorm.html#sphx-glr-download-gallery-images-contours-and-fields-colormap-normalizations-symlognorm-py)
 to download the full example code.

Colormap normalizations SymLogNorm[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations_symlognorm.html#colormap-normalizations-symlognorm "Link to this heading")

==========================================================================================================================================================================================================

Demonstration of using norm to map colormaps onto data in non-linear ways.

Synthetic dataset consisting of two humps, one negative and one positive, the positive with 8-times the amplitude. Linearly, the negative hump is almost invisible, and it is very difficult to see any detail of its profile. With the logarithmic scaling applied to both positive and negative values, it is much easier to see the shape of each hump.

See [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.colors as colors

def rbf(x, y):
    return 1.0 / (1 + 5 \* ((x \*\* 2) + (y \*\* 2)))

[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 200
[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[\-3:3:complex(0, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
), \-2:2:complex(0, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\]
[Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= rbf([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 0.5, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 0.5)
[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= rbf([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 0.5, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 0.5)
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[shadeopts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'cmap': 'PRGn', 'shading': 'gouraud'}
[colormap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'PRGn'
[lnrwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.5

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, sharex\=True, sharey\=True)

[pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].pcolormesh([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                       norm\=[colors.SymLogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
(linthresh\=[lnrwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
, linscale\=1,
                                              vmin\=-[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
, vmax\=[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
, base\=10),
                       \*\*[shadeopts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], extend\='both')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].text(\-2.5, 1.5, 'symlog')

[pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].pcolormesh([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vmin\=-[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
, vmax\=[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
                       \*\*[shadeopts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], extend\='both')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].text(\-2.5, 1.5, 'linear')

![colormap normalizations symlognorm](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_symlognorm_001_2_00x.png)

In order to find the best visualization for any particular dataset, it may be necessary to experiment with multiple different color scales. As well as the [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
 scaling, there is also the option of using [`AsinhNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.AsinhNorm.html#matplotlib.colors.AsinhNorm "matplotlib.colors.AsinhNorm")
 (experimental), which has a smoother transition between the linear and logarithmic regions of the transformation applied to the data values, "Z". In the plots below, it may be possible to see contour-like artifacts around each hump despite there being no sharp features in the dataset itself. The `asinh` scaling shows a smoother shading of each hump.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, sharex\=True, sharey\=True)

[pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].pcolormesh([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                       norm\=[colors.SymLogNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")
(linthresh\=[lnrwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
, linscale\=1,
                                              vmin\=-[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
, vmax\=[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
, base\=10),
                       \*\*[shadeopts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], extend\='both')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].text(\-2.5, 1.5, 'symlog')

[pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 \= [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].pcolormesh([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                       norm\=[colors.AsinhNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.AsinhNorm.html#matplotlib.colors.AsinhNorm "matplotlib.colors.AsinhNorm")
(linear\_width\=[lnrwidth](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
                                             vmin\=-[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
, vmax\=[gain](https://docs.python.org/3/library/functions.html#int "builtins.int")
),
                       \*\*[shadeopts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([pcm](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
, [ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], extend\='both')
[ax](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].text(\-2.5, 1.5, 'asinh')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![colormap normalizations symlognorm](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_symlognorm_002_2_00x.png)

**Total running time of the script:** (0 minutes 4.262 seconds)

[`Download Jupyter notebook: colormap_normalizations_symlognorm.ipynb`](https://matplotlib.org/stable/_downloads/6a3af30cb526b0f1e2e1af8980d24001/colormap_normalizations_symlognorm.ipynb)

[`Download Python source code: colormap_normalizations_symlognorm.py`](https://matplotlib.org/stable/_downloads/add263170379d71b432151cf853a3c0d/colormap_normalizations_symlognorm.py)

[`Download zipped: colormap_normalizations_symlognorm.zip`](https://matplotlib.org/stable/_downloads/582fd6a005d74740345e497249240d9a/colormap_normalizations_symlognorm.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)