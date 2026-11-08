[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-stairs-demo-py)
 to download the full example code.

Stairs Demo[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html#stairs-demo "Link to this heading")

=================================================================================================================================

This example demonstrates the use of [`stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
 for stepwise constant functions. A common use case is histogram and histogram-like data visualization.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [StepPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
[h](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
([np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(5, 3, 5000),
                        [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 20))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 1, figsize\=(7, 15))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].stairs([h](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='Simple histogram')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].stairs([h](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 5, baseline\=50, label\='Modified baseline')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].stairs([h](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 10, baseline\=None, label\='No edges')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title("Step Histograms")

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].stairs([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 6, 1), fill\=True,
              label\='Filled histogram\\nw/ automatic edges')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].stairs([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 6, 1)\*0.3, [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(2, 8, 1),
              orientation\='horizontal', hatch\='//',
              label\='Hatched histogram\\nw/ horizontal orientation')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title("Filled histogram")

[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
 \= [StepPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
(values\=\[1, 2, 3, 2, 1\],
                  [edges](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=range(1, 7),
                  label\=('Patch derived underlying object\\n'
                         'with default edge/facecolor behaviour'))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].add\_patch([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_xlim(0, 7)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_ylim(\-1, 5)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].set\_title("StepPatch artist")

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
    [ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Step Histograms, Filled histogram, StepPatch artist](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_001_2_00x.png)

_baseline_ can take an array to allow for stacked histogram plots

[A](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[0, 0, 0\],\
     \[1, 2, 3\],\
     \[2, 4, 6\],\
     \[3, 6, 9\]\]

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(len([A](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) \- 1):
    [plt.stairs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
([A](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
+1\], baseline\=[A](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], fill\=True)

![stairs demo](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_002_2_00x.png)

Comparison of [`pyplot.step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html#matplotlib.pyplot.step "matplotlib.pyplot.step")
 and [`pyplot.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html#comparison-of-pyplot-step-and-pyplot-stairs "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`pyplot.step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html#matplotlib.pyplot.step "matplotlib.pyplot.step")
 defines the positions of the steps as single values. The steps extend left/right/both ways from these reference values depending on the parameter _where_. The number of _x_ and _y_ values is the same.

In contrast, [`pyplot.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
 defines the positions of the steps via their bounds _edges_, which is one element longer than the step values.

[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(14)
[centers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\] + [np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
([bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) / 2
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([centers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 2)

[plt.step](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html#matplotlib.pyplot.step "matplotlib.pyplot.step")
([bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, where\='post', label\='step(where="post")')
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o--', color\='grey', alpha\=0.3)

[plt.stairs](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, baseline\=None, label\='stairs()')
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([centers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1, 'o--', color\='grey', alpha\=0.3)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
([bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 2), [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(\[[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[0\], [np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")\
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, 2), [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[\-1\]\]) \- 1,
         'o', color\='red', alpha\=0.2)

[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('step() vs. stairs()')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![step() vs. stairs()](https://matplotlib.org/stable/_images/sphx_glr_stairs_demo_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs")
     / [`matplotlib.pyplot.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
    
*   [`matplotlib.patches.StepPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
    

Tags: [plot-type: stairs](https://matplotlib.org/stable/_tags/plot-type-stairs.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 2.246 seconds)

[`Download Jupyter notebook: stairs_demo.ipynb`](https://matplotlib.org/stable/_downloads/c451a463d09263d1eb52792106c96266/stairs_demo.ipynb)

[`Download Python source code: stairs_demo.py`](https://matplotlib.org/stable/_downloads/99b2228ef8ead5b15771558e042ee4f3/stairs_demo.py)

[`Download zipped: stairs_demo.zip`](https://matplotlib.org/stable/_downloads/6c9ac4dc8e6375af8789e1fe62b3f6e7/stairs_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page