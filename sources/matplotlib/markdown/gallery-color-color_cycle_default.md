[Skip to main content](https://matplotlib.org/stable/gallery/color/color_cycle_default.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/color_cycle_default.html#sphx-glr-download-gallery-color-color-cycle-default-py)
 to download the full example code.

Colors in the default property cycle[#](https://matplotlib.org/stable/gallery/color/color_cycle_default.html#colors-in-the-default-property-cycle "Link to this heading")

==========================================================================================================================================================================

Display the colors from the default prop\_cycle, which is obtained from the [rc parameters](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import [TABLEAU\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [same\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.same_color.html#matplotlib.colors.same_color "matplotlib.colors.same_color")

def f([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, a):
    """A nice sigmoid-like parametrized curve, ending approximately at \*a\*."""
    return 0.85 \* a \* (1 / (1 + [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)) + 0.2)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Colors in the default property cycle")

[prop\_cycle](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "cycler.Cycler")
 \= [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\]
[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [prop\_cycle.by\_key](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler.by_key "cycler.Cycler.by_key")
()\['color'\]
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4, 4, 200)

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, ([color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
) in enumerate(zip([colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [TABLEAU\_COLORS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)):
    assert [same\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.same_color.html#matplotlib.colors.same_color "matplotlib.colors.same_color")
([color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)
    [pos](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 4.5 \- [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, f([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pos](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(4.2, [pos](https://docs.python.org/3/library/functions.html#float "builtins.float")
, f"'C{[i](https://docs.python.org/3/library/functions.html#int "builtins.int")
}': '{[color\_name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'", [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, va\="center")
    [ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(9, 1, width\=1.5, bottom\=[pos](https://docs.python.org/3/library/functions.html#float "builtins.float")
\-0.5)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Colors in the default property cycle](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_default_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
    
*   [`matplotlib.colors.same_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.same_color.html#matplotlib.colors.same_color "matplotlib.colors.same_color")
    
*   [`cycler.Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
    

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [purpose: reference](https://matplotlib.org/stable/_tags/purpose-reference.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: color_cycle_default.ipynb`](https://matplotlib.org/stable/_downloads/12f988776a8f665343bd3a3e57058a9b/color_cycle_default.ipynb)

[`Download Python source code: color_cycle_default.py`](https://matplotlib.org/stable/_downloads/233af54bee28814ae4bb34817226f0ea/color_cycle_default.py)

[`Download zipped: color_cycle_default.zip`](https://matplotlib.org/stable/_downloads/0bec4b6ae179a8ba06f521bc1d4a5b4e/color_cycle_default.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)