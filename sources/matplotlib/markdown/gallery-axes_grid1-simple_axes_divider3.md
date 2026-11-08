[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider3.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider3.html#sphx-glr-download-gallery-axes-grid1-simple-axes-divider3-py)
 to download the full example code.

Simple axes divider 3[#](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider3.html#simple-axes-divider-3 "Link to this heading")

==================================================================================================================================================

See also [The axes\_grid1 toolkit](https://matplotlib.org/stable/users/explain/toolkits/axes_grid.html#axes-grid)
.

![simple axes divider3](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider3_001_2_00x.png)

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1 import [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
import mpl\_toolkits.axes\_grid1.axes\_size as Size

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5.5, 4))

\# the rect parameter will be ignored as we will set axes\_locator
[rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.1, 0.1, 0.8, 0.8)
[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")\
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, label\="%d" % i) for i in range(4)\]

[horiz](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.AxesX](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")\
([ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[0\]), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5), [Size.AxesX](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesX.html#mpl_toolkits.axes_grid1.axes_size.AxesX "mpl_toolkits.axes_grid1.axes_size.AxesX")\
([ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[1\])\]
[vert](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.AxesY](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")\
([ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[0\]), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5), [Size.AxesY](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.AxesY.html#mpl_toolkits.axes_grid1.axes_size.AxesY "mpl_toolkits.axes_grid1.axes_size.AxesY")\
([ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[2\])\]

\# divide the Axes rectangle into grid whose size is specified by horiz \* vert
[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
 \= [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [horiz](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [vert](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, aspect\=False)

[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].set\_axes\_locator([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=0, ny\=0))
[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\].set\_axes\_locator([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=2, ny\=0))
[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[2\].set\_axes\_locator([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=0, ny\=2))
[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[3\].set\_axes\_locator([divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=2, ny\=2))

[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].set\_xlim(0, 2)
[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\].set\_xlim(0, 1)

[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].set\_ylim(0, 1)
[ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[2\].set\_ylim(0, 2)

[divider.set\_aspect](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.set_aspect "mpl_toolkits.axes_grid1.Divider.set_aspect")
(1.)

for [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [ax](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
:
    [ax1.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(labelbottom\=False, labelleft\=False)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: simple_axes_divider3.ipynb`](https://matplotlib.org/stable/_downloads/a5b07b02cbcb6a67ca2c623a32262d00/simple_axes_divider3.ipynb)

[`Download Python source code: simple_axes_divider3.py`](https://matplotlib.org/stable/_downloads/bb0580289006b321b47cf070fd5c1bfb/simple_axes_divider3.py)

[`Download zipped: simple_axes_divider3.zip`](https://matplotlib.org/stable/_downloads/71c874b5e7b315eced3bacfde651bd71/simple_axes_divider3.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)