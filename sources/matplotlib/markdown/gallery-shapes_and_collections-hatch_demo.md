[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html#sphx-glr-download-gallery-shapes-and-collections-hatch-demo-py)
 to download the full example code.

Hatch demo[#](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_demo.html#hatch-demo "Link to this heading")

==============================================================================================================================

Hatches can be added to most polygons in Matplotlib, including [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
, [`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
, [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
, and children of [`Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
. They are currently supported in the PS, PDF, SVG, macosx, and Agg backends. The WX and Cairo backends do not currently support hatching.

See also [Contourf hatching](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html)
 for an example using [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
, and [Hatch style reference](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html)
 for swatches of the existing hatches.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
, [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 5)
[y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 5)
[y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
([y1.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
) \* 4

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
(\[\['bar1', 'patches'\], \['bar2', 'patches'\]\])

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bar1'\].bar([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='black', hatch\="/")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bar1'\].bar([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bottom\=[y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='black', hatch\='//')

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bar2'\].bar([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='black', hatch\=\['--', '+', 'x', '\\\\'\])
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bar2'\].bar([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bottom\=[y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='black',
                hatch\=\['\*', 'o', 'O', '.'\])

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 40, 0.2)
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['patches'\].fill\_between([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* 4 + 30, [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0,
                            hatch\='///', zorder\=2, fc\='c')
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['patches'\].add\_patch([Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((4, 50), 10, 10, fill\=True,
                                 hatch\='\*', facecolor\='y'))
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['patches'\].add\_patch([Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
(\[(10, 20), (30, 50), (50, 10)\],
                                 hatch\=r'\\/...', facecolor\='g'))
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['patches'\].set\_xlim(0, 40)
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['patches'\].set\_ylim(10, 60)
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['patches'\].set\_aspect(1)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![hatch demo](https://matplotlib.org/stable/_images/sphx_glr_hatch_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
    
*   [`matplotlib.patches.Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`matplotlib.patches.Patch.set_hatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_hatch "matplotlib.patches.Patch.set_hatch")
    
*   [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     / [`matplotlib.pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
    

[`Download Jupyter notebook: hatch_demo.ipynb`](https://matplotlib.org/stable/_downloads/ce6efd42f86b4acf02ad01757a206da3/hatch_demo.ipynb)

[`Download Python source code: hatch_demo.py`](https://matplotlib.org/stable/_downloads/5b3124f09b7e3e5b644a2408570d7f9b/hatch_demo.py)

[`Download zipped: hatch_demo.zip`](https://matplotlib.org/stable/_downloads/a137b15f9521d9fbf98392c150460083/hatch_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)