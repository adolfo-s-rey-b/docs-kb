[Skip to main content](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#sphx-glr-download-users-explain-artists-color-cycle-py)
 to download the full example code.

Styling with cycler[#](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#styling-with-cycler "Link to this heading")

========================================================================================================================================

Demo of custom property-cycle settings to control colors and other style properties for multi-line plots.

Note

More complete documentation of the `cycler` API can be found [here](https://matplotlib.org/cycler/)
.

This example demonstrates two different APIs:

1.  Setting the rc parameter specifying the default property cycle. This affects all subsequent Axes (but not Axes already created).
    
2.  Setting the property cycle for a single pair of Axes.
    

from cycler import [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")

import matplotlib.pyplot as plt
import numpy as np

First we'll generate some sample data, in this case, four offset sine curves.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 50)
[offsets](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 4, endpoint\=False)
[yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.transpose](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")
(\[[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 + phi) for phi in [offsets](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])

Now `yy` has shape

print([yy.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

(50, 4)

So `yy[:, i]` will give you the `i`\-th offset sine curve. Let's set the default `prop_cycle` using [`matplotlib.pyplot.rc()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc "matplotlib.pyplot.rc")
. We'll combine a color cycler and a linestyle cycler by adding (`+`) two `cycler`'s together. See the bottom of this tutorial for more information about combining different cyclers.

[default\_cycler](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "cycler.Cycler")
 \= ([cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(color\=\['r', 'g', 'b', 'y'\]) +
                  [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(linestyle\=\['-', '--', ':', '-.'\]))

[plt.rc](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc "matplotlib.pyplot.rc")
('lines', linewidth\=4)
[plt.rc](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc "matplotlib.pyplot.rc")
('axes', prop\_cycle\=[default\_cycler](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "cycler.Cycler")
)

Now we'll generate a figure with two Axes, one on top of the other. On the first axes, we'll plot with the default cycler. On the second axes, we'll set the `prop_cycle` using [`matplotlib.axes.Axes.set_prop_cycle()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle")
, which will only set the `prop_cycle` for this [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance. We'll use a second `cycler` that combines a color cycler and a linewidth cycler.

[custom\_cycler](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "cycler.Cycler")
 \= ([cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(color\=\['c', 'm', 'y', 'k'\]) +
                 [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(lw\=\[1, 2, 3, 4\]))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2)
[ax0.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax0.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Set default color cycle to rgby')
[ax1.set\_prop\_cycle](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle")
([custom\_cycler](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "cycler.Cycler")
)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Set axes color cycle to cmyk')

\# Add a bit more space between the two plots.
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(hspace\=0.3)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Set default color cycle to rgby, Set axes color cycle to cmyk](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_001_2_00x.png)

Setting `prop_cycle` in the `matplotlibrc` file or style files[#](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#setting-prop-cycle-in-the-matplotlibrc-file-or-style-files "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Remember, a custom cycler can be set in your `matplotlibrc` file or a style file (`style.mplstyle`) under `axes.prop_cycle`, e.g.

axes.prop\_cycle : cycler(color=\['red', 'royalblue', 'gray'\])

For colors, a single string may be used either for one of the [Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)

axes.prop\_cycle : cycler(color='Accent')

or if each color has a single character name:

axes.prop\_cycle : cycler(color='bgrcmyk')

Cycling through multiple properties[#](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#cycling-through-multiple-properties "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can add cyclers:

from cycler import [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
cc \= ([cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(color\=list('rgb')) +
      [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(linestyle\=\['-', '--', '-.'\]))
for d in cc:
    print(d)

Results in:

{'color': 'r', 'linestyle': '-'}
{'color': 'g', 'linestyle': '--'}
{'color': 'b', 'linestyle': '-.'}

You can multiply cyclers:

from cycler import [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
cc \= ([cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(color\=list('rgb')) \*
      [cycler](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "cycler.cycler")
(linestyle\=\['-', '--', '-.'\]))
for d in cc:
    print(d)

Results in:

{'color': 'r', 'linestyle': '-'}
{'color': 'r', 'linestyle': '--'}
{'color': 'r', 'linestyle': '-.'}
{'color': 'g', 'linestyle': '-'}
{'color': 'g', 'linestyle': '--'}
{'color': 'g', 'linestyle': '-.'}
{'color': 'b', 'linestyle': '-'}
{'color': 'b', 'linestyle': '--'}
{'color': 'b', 'linestyle': '-.'}

[`Download Jupyter notebook: color_cycle.ipynb`](https://matplotlib.org/stable/_downloads/2b6269c4a1a995b895e69cc9e1ff92cf/color_cycle.ipynb)

[`Download Python source code: color_cycle.py`](https://matplotlib.org/stable/_downloads/9beda5664b175faa65a3079734e5405f/color_cycle.py)

[`Download zipped: color_cycle.zip`](https://matplotlib.org/stable/_downloads/f0ade1c2fab8fc99318dd0fbfa539ef1/color_cycle.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page