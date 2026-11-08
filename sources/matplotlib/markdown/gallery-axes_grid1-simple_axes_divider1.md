[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider1.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider1.html#sphx-glr-download-gallery-axes-grid1-simple-axes-divider1-py)
 to download the full example code.

Simple Axes Divider 1[#](https://matplotlib.org/stable/gallery/axes_grid1/simple_axes_divider1.html#simple-axes-divider-1 "Link to this heading")

==================================================================================================================================================

See also [The axes\_grid1 toolkit](https://matplotlib.org/stable/users/explain/toolkits/axes_grid.html#axes-grid)
.

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1 import [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
, Size

def label\_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5, .5, text, transform\=ax.transAxes,
            horizontalalignment\="center", verticalalignment\="center")
    ax.tick\_params(bottom\=False, labelbottom\=False,
                   left\=False, labelleft\=False)

Fixed Axes sizes; fixed paddings.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Fixed axes sizes, fixed paddings")

\# Sizes are in inches.
[horiz](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(1.), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(1.5), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5)\]
[vert](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(1.5), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(1.)\]

[rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.1, 0.1, 0.8, 0.8)
\# Divide the Axes rectangle into a grid with sizes specified by horiz \* vert.
[div](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
 \= [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [horiz](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [vert](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, aspect\=False)

\# The rect parameter will actually be ignored and overridden by axes\_locator.
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=0, ny\=0))
label\_axes([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=0, ny=0")
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=0, ny\=2))
label\_axes([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=0, ny=2")
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=2, ny\=2))
label\_axes([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=2, ny=2")
[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=2, nx1\=4, ny\=0))
label\_axes([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=2, nx1=4, ny=0")

![Fixed axes sizes, fixed paddings](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider1_001_2_00x.png)

Axes sizes that scale with the figure size; fixed paddings.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Scalable axes sizes, fixed paddings")

[horiz](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1.5), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1.), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(.5)\]
[vert](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1.), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1.5)\]

[rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.1, 0.1, 0.8, 0.8)
\# Divide the Axes rectangle into a grid with sizes specified by horiz \* vert.
[div](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
 \= [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [horiz](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [vert](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, aspect\=False)

\# The rect parameter will actually be ignored and overridden by axes\_locator.
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=0, ny\=0))
label\_axes([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=0, ny=0")
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=0, ny\=2))
label\_axes([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=0, ny=2")
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=2, ny\=2))
label\_axes([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=2, ny=2")
[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([rect](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, axes\_locator\=[div.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=2, nx1\=4, ny\=0))
label\_axes([ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, "nx=2, nx1=4, ny=0")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Scalable axes sizes, fixed paddings](https://matplotlib.org/stable/_images/sphx_glr_simple_axes_divider1_002_2_00x.png)

[`Download Jupyter notebook: simple_axes_divider1.ipynb`](https://matplotlib.org/stable/_downloads/c0effe5b6480bde8e7380adda1adce3a/simple_axes_divider1.ipynb)

[`Download Python source code: simple_axes_divider1.py`](https://matplotlib.org/stable/_downloads/43ee01b4b62cb46e1521f86c6de1a0a4/simple_axes_divider1.py)

[`Download zipped: simple_axes_divider1.zip`](https://matplotlib.org/stable/_downloads/a2632b9289477775b3c280e95d12d190/simple_axes_divider1.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)