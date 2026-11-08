[Skip to main content](https://matplotlib.org/stable/gallery/axes_grid1/demo_fixed_size_axes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axes_grid1/demo_fixed_size_axes.html#sphx-glr-download-gallery-axes-grid1-demo-fixed-size-axes-py)
 to download the full example code.

Axes with a fixed physical size[#](https://matplotlib.org/stable/gallery/axes_grid1/demo_fixed_size_axes.html#axes-with-a-fixed-physical-size "Link to this heading")

======================================================================================================================================================================

Note that this can be accomplished with the main library for Axes on Figures that do not change size: [Adding single Axes at a time](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#fixed-size-axes)

import matplotlib.pyplot as plt

from mpl\_toolkits.axes\_grid1 import [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
, Size

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))

\# The first items are for padding and the second items are for the Axes.
\# sizes are in inch.
[h](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(1.0), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(4.5)\]
[v](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(0.7), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(5.)\]

[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
 \= [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (0, 0, 1, 1), [h](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [v](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, aspect\=False)
\# The width and height of the rectangle are ignored.

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([divider.get\_position](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_position "mpl_toolkits.axes_grid1.Divider.get_position")
(),
                  axes\_locator\=[divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=1, ny\=1))

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\])

![demo fixed size axes](https://matplotlib.org/stable/_images/sphx_glr_demo_fixed_size_axes_001_2_00x.png)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6))

\# The first & third items are for padding and the second items are for the
\# Axes. Sizes are in inches.
[h](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(1.0), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1.), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.2)\]
[v](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(0.7), [Size.Scaled](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Scaled.html#mpl_toolkits.axes_grid1.axes_size.Scaled "mpl_toolkits.axes_grid1.axes_size.Scaled")\
(1.), [Size.Fixed](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.Fixed.html#mpl_toolkits.axes_grid1.axes_size.Fixed "mpl_toolkits.axes_grid1.axes_size.Fixed")\
(.5)\]

[divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
 \= [Divider](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.Divider")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (0, 0, 1, 1), [h](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [v](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, aspect\=False)
\# The width and height of the rectangle are ignored.

[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
([divider.get\_position](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.get_position "mpl_toolkits.axes_grid1.Divider.get_position")
(),
                  axes\_locator\=[divider.new\_locator](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.Divider.new_locator")
(nx\=1, ny\=1))

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![demo fixed size axes](https://matplotlib.org/stable/_images/sphx_glr_demo_fixed_size_axes_002_2_00x.png)

[`Download Jupyter notebook: demo_fixed_size_axes.ipynb`](https://matplotlib.org/stable/_downloads/168e63cc0650bc4cb6a1765cbd2de991/demo_fixed_size_axes.ipynb)

[`Download Python source code: demo_fixed_size_axes.py`](https://matplotlib.org/stable/_downloads/88a68d33e6dc95f3756002ca22961251/demo_fixed_size_axes.py)

[`Download zipped: demo_fixed_size_axes.zip`](https://matplotlib.org/stable/_downloads/18af70ae5d06cb39562a637f75056b3b/demo_fixed_size_axes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)