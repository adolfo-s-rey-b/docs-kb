[Skip to main content](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html#sphx-glr-download-gallery-spines-spine-placement-demo-py)
 to download the full example code.

Spine placement[#](https://matplotlib.org/stable/gallery/spines/spine_placement_demo.html#spine-placement "Link to this heading")

==================================================================================================================================

The position of the axis spines can be influenced using [`set_position`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
.

Note: If you want to obtain arrow heads at the ends of the axes, also check out the [Centered spines with arrows](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html)
 example.

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 100)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(
    \[\['center', 'zero'\],\
     \['axes', 'data'\]\]
)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Spine positions')

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['center'\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("'center'")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['left', 'bottom'\]\].set\_position('center')
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['zero'\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("'zero'")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['left', 'bottom'\]\].set\_position('zero')
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['axes'\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("'axes' (0.2, 0.2)")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.spines.left.set\_position](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
(('axes', 0.2))
[ax.spines.bottom.set\_position](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
(('axes', 0.2))
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['data'\]
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("'data' (1, 2)")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.spines.left.set\_position](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
(('data', 1))
[ax.spines.bottom.set\_position](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine.set_position "matplotlib.spines.Spine.set_position")
(('data', 2))
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Spine positions, 'center', 'zero', 'axes' (0.2, 0.2), 'data' (1, 2)](https://matplotlib.org/stable/_images/sphx_glr_spine_placement_demo_001_2_00x.png)

[`Download Jupyter notebook: spine_placement_demo.ipynb`](https://matplotlib.org/stable/_downloads/750e49b415bb813567e321e425418e63/spine_placement_demo.ipynb)

[`Download Python source code: spine_placement_demo.py`](https://matplotlib.org/stable/_downloads/bf9ef8b51aeea6553751ee8060c5e19e/spine_placement_demo.py)

[`Download zipped: spine_placement_demo.zip`](https://matplotlib.org/stable/_downloads/c07d1027ccdcd1aa472cdcbce85a60a1/spine_placement_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)