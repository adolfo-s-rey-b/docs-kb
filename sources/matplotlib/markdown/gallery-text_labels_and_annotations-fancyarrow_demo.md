[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html#sphx-glr-download-gallery-text-labels-and-annotations-fancyarrow-demo-py)
 to download the full example code.

Annotation arrow style reference[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html#annotation-arrow-style-reference "Link to this heading")

====================================================================================================================================================================================

Overview of the available [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
 settings. These are used for the _arrowstyle_ parameter of [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 and [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
.

Each style can be configured with a set of parameters, which are stated along with their default values.

import inspect
import itertools
import re

import matplotlib.pyplot as plt

from matplotlib.patches import ArrowStyle

[styles](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= ArrowStyle.get\_styles()
[ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2
[nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= (len([styles](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
) + 1) // [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
[gridspec\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(wspace\=0, hspace\=0.05, left\=0, right\=1, bottom\=0, top\=1)
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1 + [nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
                        figsize\=(4 \* [ncol](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 1 + [nrow](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [gridspec\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[gridspec\_kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-0.1, 4)
    [ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :\]:
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0, 0.5, "arrowstyle", size\="large", color\="tab:blue")
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1.4, .5, "default parameters", size\="large")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, ([stylename](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [stylecls](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Wedge "matplotlib.patches.ArrowStyle.Wedge")
) in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, :\].T.flat, [styles](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items()):
    \# draw dot and annotation with arrowstyle
    [l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(1.25, 0, "o", color\="darkgrey")
    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
([stylename](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, (1.25, 0), (0, 0),
                size\="large", color\="tab:blue", va\="center", family\="monospace",
                arrowprops\=dict(
                    arrowstyle\=[stylename](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, connectionstyle\="arc3,rad=0",
                    color\="black", shrinkA\=5, shrinkB\=5, patchB\=[l](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,
                ),
                bbox\=dict(boxstyle\="square", fc\="w", ec\="darkgrey"))
    \# draw default parameters
    \# wrap at every nth comma (n = 1 or 2, depending on text length)
    [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= str([inspect.signature](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
([stylecls](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Wedge "matplotlib.patches.ArrowStyle.Wedge")
))\[1:\-1\]
    [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2 if [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.count(',') \> 3 else 1
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(1.4, 0,
            [re.sub](https://docs.python.org/3/library/re.html#re.sub "re.sub")
(', ', lambda m, c\=[itertools.count](https://docs.python.org/3/library/itertools.html#itertools.count "itertools.count")
(1): m.group()
                   if next(c) % [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 else '\\n', [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
),
            verticalalignment\="center", color\="0.3")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![fancyarrow demo](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
    
*   `matplotlib.patches.ArrowStyle.get_styles`
    
*   [`matplotlib.axes.Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
    

**Total running time of the script:** (0 minutes 2.243 seconds)

[`Download Jupyter notebook: fancyarrow_demo.ipynb`](https://matplotlib.org/stable/_downloads/0388069c25c84d6bc3a8b03a4f424035/fancyarrow_demo.ipynb)

[`Download Python source code: fancyarrow_demo.py`](https://matplotlib.org/stable/_downloads/5c12d4b66c26fc9c8cdfd42f3e8008a7/fancyarrow_demo.py)

[`Download zipped: fancyarrow_demo.zip`](https://matplotlib.org/stable/_downloads/ecbc5dc092a37a300dff91286a6f1d86/fancyarrow_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)