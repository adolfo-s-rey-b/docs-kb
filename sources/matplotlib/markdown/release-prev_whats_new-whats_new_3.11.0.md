[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#main-content)

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
    

[What's new in Matplotlib 3.11.0 (Jun 11, 2026)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#what-s-new-in-matplotlib-3-11-0-jun-11-2026 "Link to this heading")

====================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Figure creation / management](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#figure-creation-management "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Figures can be attached to and removed from pyplot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#figures-can-be-attached-to-and-removed-from-pyplot "Link to this heading")

Figures can now be attached to and removed from management through pyplot, which in the background also means a less strict coupling to backends.

In particular, standalone figures (created with the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 constructor) can now be registered with the [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 module by calling `plt.figure(fig)`. This allows showing them with `plt.show()` as you would do with any figure created with pyplot factory functions such as `plt.figure()` or `plt.subplots()`.

When closing a shown figure window, the related figure is reset to the standalone state, i.e., it's not visible to pyplot anymore, but if you still hold a reference to it, you can continue to work with it (e.g. do `fig.savefig()`, or re-add it to pyplot with `plt.figure(fig)` and then show it again).

The following is now possible — though the example is exaggerated to show what's possible. In practice, you'll stick with much simpler versions for better consistency

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

\# Create a standalone figure
fig \= Figure()
ax \= fig.add\_subplot()
ax.plot(\[1, 2, 3\], \[4, 5, 6\])

\# Register it with pyplot
plt.figure(fig)

\# Modify the figure through pyplot
plt.xlabel("x label")

\# Show the figure
plt.show()

\# Close the figure window through the GUI

\# Continue to work on the figure
fig.savefig("my\_figure.png")
ax.set\_ylabel("y label")

\# Re-register the figure and show it again
plt.figure(fig)
plt.show()

Technical detail

Standalone figures use [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 as canvas. This is replaced by a backend-dependent subclass when registering with pyplot, and is reset to [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 when the figure is closed. [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 uses the current canvas to save the figure (if possible). Since [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 can not render the figure, when saving the figure, it will fall back to a suitable canvas subclass, e.g., [`FigureCanvasAgg`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
 for raster outputs such as PNG.

Any Agg-based backend will create the same file output. However, there may be slight differences for non-Agg backends; e.g. if you use "GTK4Cairo" as interactive backend, `fig.savefig("file.png")` may create a slightly different image depending on whether the figure is registered with pyplot or not.

In general, you should not store a reference to the canvas, but rather always obtain it from the figure with `fig.canvas`. This will return the current canvas, which is either the original [`FigureCanvasBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
 or a backend-dependent subclass, depending on whether the figure is registered with pyplot or not.

### [Figure size units](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#figure-size-units "Link to this heading")

When creating figures, it is now possible to define figure sizes in centimetres or pixels.

Up to now the figure size is specified via `plt.figure(..., figsize=(6, 4))`, and the given numbers are interpreted as inches. It is now possible to add a unit string to the tuple, i.e. `plt.figure(..., figsize=(600, 400, "px"))`. Supported unit strings are `"in"`, `"cm"`, or `"px"`.

### [Partial `figsize` specification at figure creation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#partial-figsize-specification-at-figure-creation "Link to this heading")

Figure creation now accepts a single `None` in `figsize`. Passing `(None, h)` uses the default width from `[rcParams["figure.figsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.figsize#rcparam-figure-figsize) ` (default: `[6.4, 4.8]`), and passing `(w, None)` uses the default height. Passing `(None, None)` is invalid and raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

For example:

plt.rcParams\['figure.figsize'\] \= (14, 11)
fig \= plt.figure(figsize\=(None, 4))  \# Size will be (14, 4)

### [Subplot parameters are reset in `Figure.clear`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#subplot-parameters-are-reset-in-figure-clear "Link to this heading")

When calling [`Figure.clear()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.clear.html#matplotlib.figure.Figure.clear "matplotlib.figure.Figure.clear")
 the settings for [`gridspec.SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
 are restored to the default values.

[`SubplotParams.to_dict`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.to_dict "matplotlib.gridspec.SubplotParams.to_dict")
 is a new method to get the subplot parameters as a dict, and [`SubplotParams.reset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.reset "matplotlib.gridspec.SubplotParams.reset")
 resets the parameters to the defaults.

[Plotting methods](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#plotting-methods "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Grouped bar charts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#grouped-bar-charts "Link to this heading")

The new method [`grouped_bar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar")
 simplifies the creation of grouped bar charts significantly. It supports different input data types (lists of datasets, dicts of datasets, data in 2D arrays, pandas DataFrames), and allows for easy customization of placement via controllable distances between bars and between bar groups.

categories \= \['A', 'B'\]
datasets \= {
    'dataset 0': \[1, 11\],
    'dataset 1': \[3, 13\],
    'dataset 2': \[5, 15\],
}

fig, ax \= plt.subplots()
ax.grouped\_bar(datasets, tick\_labels\=categories)
ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/a05a6e5cce3a2bd9b232f754d0c2f467/whats_new_3-11-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/0e2bc4ed2cad2df8798099fe273f1dde/whats_new_3-11-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/24d44e0503f927320d5fdbeafd66d493/whats_new_3-11-0-1.png)
)

[![Diagram of a grouped bar chart of 3 datasets with 2 categories.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-1.2x.png)

### [`broken_barh()` vertical alignment through _align_ parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#broken-barh-vertical-alignment-through-align-parameter "Link to this heading")

[`broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh")
 now supports vertical alignment of the bars through the _align_ parameter.

fig, ax \= plt.subplots()
ax.axhline(0, color\='tab:red')
ax.broken\_barh(\[(0, 10)\], (0, 2))  \# Default is 'bottom'.
ax.axhline(10, color\='tab:red')
ax.broken\_barh(\[(0, 10)\], (10, 2), align\='center')
ax.axhline(20, color\='tab:red')
ax.broken\_barh(\[(0, 10)\], (20, 2), align\='top')

([`Source code`](https://matplotlib.org/stable/_downloads/21bef03511ca716c5c652c5488fc6bf3/whats_new_3-11-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/44ddb740f190d7cd446ea637708d503a/whats_new_3-11-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7bcc2706c0d009872f917a1d58349948/whats_new_3-11-0-2.png)
)

[![A plot with three horizontal bars at 0, 10, and 20. Each is aligned to the bottom, center, and top of those values, respectively.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-2.2x.png)

### [`hist()` supports a single color for multiple datasets](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#hist-supports-a-single-color-for-multiple-datasets "Link to this heading")

It is now possible to pass a single _color_ value to [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
. This value is applied to all datasets.

### [Stackplot styling](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#stackplot-styling "Link to this heading")

[`stackplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
 now accepts sequences for the style parameters _facecolor_, _edgecolor_, _linestyle_, and _linewidth_, similar to how the _hatch_ parameter is already handled.

x \= np.linspace(0, 10)
y1 \= x + np.sin(x)
y2 \= x + np.cos(x)

fig, ax \= plt.subplots()
ax.stackplot(x, y1, y2, facecolor\=\['tab:orange', 'tab:green'\])

([`Source code`](https://matplotlib.org/stable/_downloads/98f985f2a441f105d6884a623d8210fb/whats_new_3-11-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/87fc7cad6e968302e6c71a5d79109aba/whats_new_3-11-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3d306f674011b03cfadefcb28e6ede78/whats_new_3-11-0-3.png)
)

[![A plot of stacked datasets. The bottom area is orange and the top is green.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-3.2x.png)

### [Streamplot integration control](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#streamplot-integration-control "Link to this heading")

Two new options have been added to the [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
 method that give better control of the streamline integration:

`integration_max_step_scale`

Multiplies the default max step computed by the integrator.

`integration_max_error_scale`

Multiplies the default max error set by the integrator.

Values for these parameters between zero and one reduce (tighten) the max step or error to improve streamline accuracy by performing more computation. Values greater than one increase (loosen) the max step or error to reduce computation time at the cost of lower streamline accuracy.

The integrator defaults are both hand-tuned values and may not be applicable to all cases, so this allows customizing the behavior to specific use cases. Modifying only `integration_max_step_scale` has proved effective, but it may be useful to control the error as well.

### [Multiple arrows on a streamline](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#multiple-arrows-on-a-streamline "Link to this heading")

A new _num\_arrows_ argument has been added to [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
 that allows more than one arrow to be added to each streamline:

w \= 3
Y, X \= np.mgrid\[\-w:w:100j, \-w:w:100j\]
U \= \-1 \- X\*\*2 + Y
V \= 1 + X \- Y\*\*2

fig, ax \= plt.subplots()
ax.streamplot(X, Y, U, V, num\_arrows\=3)

([`Source code`](https://matplotlib.org/stable/_downloads/dce9d24cb8fddec8281cccfc7e358a9b/whats_new_3-11-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b928c1a515f265be823c475ef688e575/whats_new_3-11-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/6f6e412c2c8fb46caf4b1a8a5e760d02/whats_new_3-11-0-4.png)
)

[![One chart showing a streamplot. Each streamline has three arrows.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-4.2x.png)

### [`violinplot` now accepts color arguments](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#violinplot-now-accepts-color-arguments "Link to this heading")

[`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
 and [`violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin")
 now accept `facecolor` and `linecolor` as input arguments. This means that the color of violinplots can be set as they are made, rather than setting the color of individual objects afterwards. It is possible to pass a single color to be used for all violins, or pass a sequence of colors.

np.random.seed(19680801)
data \= \[sorted(np.random.normal(0, std, 100)) for std in range(1, 5)\]

fig, (ax1, ax2) \= plt.subplots(nrows\=1, ncols\=2, sharey\=True)

ax1.set\_title('Default violin plot')
ax1.set\_ylabel('Observed values')
ax1.violinplot(data)

ax2.set\_title('Set colors of violins')
ax2.set\_ylabel('Observed values')
ax2.violinplot(
    data,
    facecolor\=\[('yellow', 0.3), ('blue', 0.3), ('red', 0.3), ('green', 0.3)\],
    linecolor\='black',
)

([`Source code`](https://matplotlib.org/stable/_downloads/6af9db44c18c47b81b290c93bd50565a/whats_new_3-11-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/2e0caca91ffa33ff3f45965f23ad6ff2/whats_new_3-11-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ea7d7f6d543bf2a589d405f60a359ca2/whats_new_3-11-0-5.png)
)

[![Two violin plots. On the left, all elements are blue. On the right, each is a custom colour: a desaturated yellow, blue, red, and green for each data set, and black for the vertical bars.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-5.2x.png)

[Annotations](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#annotations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`bar_label` supports individual padding per label](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#bar-label-supports-individual-padding-per-label "Link to this heading")

[`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
 will now accept both a float value or an array-like for padding. The array-like defines the padding for each label individually.

### [Adding labels to pie chart wedges](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#adding-labels-to-pie-chart-wedges "Link to this heading")

The new [`pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
 method adds a label to each wedge in a pie chart created with [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
. It can take

*   a list of strings, similar to the existing _labels_ parameter of [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
    
*   a format string similar to the existing _autopct_ parameter of [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     except that it uses the [`str.format`](https://docs.python.org/3/library/stdtypes.html#str.format "(in Python v3.14)")
     method and it can handle absolute values as well as fractions/percentages
    

For more examples, see [Labeling pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_label.html)
.

data \= \[36, 24, 8, 12\]
labels \= \['spam', 'eggs', 'bacon', 'sausage'\]

fig, ax \= plt.subplots()
pie \= ax.pie(data)

ax.pie\_label(pie, labels, distance\=1.1)
ax.pie\_label(pie, '{frac:.1%}', distance\=0.7)
ax.pie\_label(pie, '{absval:d}', distance\=0.4)

([`Source code`](https://matplotlib.org/stable/_downloads/3d08c71e8fed7c3b6ecaa9d0674c7c5d/whats_new_3-11-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/048b90ace6fac1389cfc3ca9bcde402e/whats_new_3-11-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/fff0ffa3c05e810655bc49301df6e5cc/whats_new_3-11-0-6.png)
)

[![A pie chart with three labels on each wedge, showing a food type, number, and fraction associated with the wedge.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-6.2x.png)

### [Arrow-style sub-classes of `BoxStyle` support arrow head resizing](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#arrow-style-sub-classes-of-boxstyle-support-arrow-head-resizing "Link to this heading")

The new _head\_width_ and _head\_angle_ parameters to [`BoxStyle.LArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.LArrow "matplotlib.patches.BoxStyle.LArrow")
, [`BoxStyle.RArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.RArrow "matplotlib.patches.BoxStyle.RArrow")
 and [`BoxStyle.DArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.DArrow "matplotlib.patches.BoxStyle.DArrow")
 allow for adjustment of the size and aspect ratio of the arrow heads used.

To give a consistent appearance across all parameter values, the default head position (where the head starts relative to text) is slightly changed compared to the previous hard-coded position.

By using negative angles (or corresponding reflex angles) for _head\_angle_, arrows with 'backwards' heads may be created.

plt.text(0.2, 0.8, "LArrow", ha\='center', size\=16,
         bbox\=dict(boxstyle\="larrow, pad=0.3, head\_angle=150"))
plt.text(0.2, 0.2, "LArrow", ha\='center', size\=16,
         bbox\=dict(boxstyle\="larrow, pad=0.3, head\_width=0.5"))
plt.text(0.5, 0.8, "DArrow", ha\='center', size\=16,
         bbox\=dict(boxstyle\="darrow, pad=0.3, head\_width=3"))
plt.text(0.5, 0.2, "DArrow", ha\='center', size\=16,
         bbox\=dict(boxstyle\="darrow, pad=0.3, head\_width=1, head\_angle=60"))
plt.text(0.8, 0.8, "RArrow", ha\='center', size\=16,
         bbox\=dict(boxstyle\="rarrow, pad=0.3, head\_angle=30"))
plt.text(0.8, 0.2, "RArrow", ha\='center', size\=16,
         bbox\=dict(boxstyle\="rarrow, pad=0.3, head\_width=2, head\_angle=-90"))
plt.axis("off")

([`Source code`](https://matplotlib.org/stable/_downloads/479710f97b864af695b785687540a91d/whats_new_3-11-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/98cfec3772b224412717471516862b62/whats_new_3-11-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/39667a86bef264457ea8c01590d6aab4/whats_new_3-11-0-7.png)
)

[![Six arrow-shaped text boxes.  The arrows on the left have the shaft on their left; the arrows on the right have the shaft on the right; the arrows in the middle have shafts on both sides.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-7.2x.png)

### [_borderpad_ accepts a tuple for separate x/y padding](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#borderpad-accepts-a-tuple-for-separate-x-y-padding "Link to this heading")

The _borderpad_ parameter used for placing anchored artists (such as inset axes) now accepts a tuple of `(x_pad, y_pad)`.

This allows for specifying separate padding values for the horizontal and vertical directions, providing finer control over placement. For example, when placing an inset in a corner, one might want horizontal padding to avoid overlapping with the main plot's axis labels, but no vertical padding to keep the inset flush with the plot area edge.

Example usage with [`inset_axes()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.inset_axes.html#mpl_toolkits.axes_grid1.inset_locator.inset_axes "mpl_toolkits.axes_grid1.inset_locator.inset_axes")
:

ax\_inset \= inset\_axes(
    ax, width\="30%", height\="30%", loc\='upper left',
    borderpad\=(4, 0))

[Axes and Artists](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#axes-and-artists "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Twin Axes `delta_zorder`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#twin-axes-delta-zorder "Link to this heading")

[`twinx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx")
 and [`twiny`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twiny.html#matplotlib.axes.Axes.twiny "matplotlib.axes.Axes.twiny")
 now accept a _delta\_zorder_ keyword argument, a relative offset added to the original Axes' zorder, to control whether the twin Axes is drawn in front of, or behind, the original Axes. For example, pass `delta_zorder=-1` to draw a twin Axes behind the main Axes.

In addition, Matplotlib now automatically manages background patch visibility for each group of twinned Axes so that only the bottom-most Axes in the group has a visible background patch (respecting `frameon`).

### [`BarContainer` properties](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#barcontainer-properties "Link to this heading")

[`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 gained new properties to easily access coordinates of the bars:

*   [`bottoms`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer.bottoms "matplotlib.container.BarContainer.bottoms")
    
*   [`tops`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer.tops "matplotlib.container.BarContainer.tops")
    
*   [`position_centers`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer.position_centers "matplotlib.container.BarContainer.position_centers")
    

### [Maximum levels on log-scaled contour plots are now respected](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#maximum-levels-on-log-scaled-contour-plots-are-now-respected "Link to this heading")

When plotting contours with a log norm, passing an integer value to the `levels` argument to cap the maximum number of contour levels now works as intended.

### [`edgegapcolor` for Patches](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#edgegapcolor-for-patches "Link to this heading")

[`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 now supports an _edgegapcolor_ parameter, similar to the existing _gapcolor_ in [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
. This allows patches with dashed edges to display a secondary color in the gaps, creating a "striped" edge effect.

This is useful when drawing unfilled patches on backgrounds of unknown color, where alternating edge colors ensure the patch boundary remains visible.

from matplotlib.patches import Rectangle

fig, ax \= plt.subplots()
rect \= Rectangle((0.1, 0.1), 0.6, 0.6, fill\=False,
                  edgecolor\='orange', edgegapcolor\='blue',
                  linestyle\='--', linewidth\=3)
ax.add\_patch(rect)

([`Source code`](https://matplotlib.org/stable/_downloads/1cb156c6711c02925c4ac364876f3611/whats_new_3-11-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/37065e1aa2b5ae01e14019d3cb612b26/whats_new_3-11-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8f6beaf4eab0e06a99985575c7d5e2af/whats_new_3-11-0-8.png)
)

[![A rectangle with a dashed orange edge and blue gaps, demonstrating the edgegapcolor feature.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-8.2x.png)

### [Separated `hatchcolor` from `edgecolor`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#separated-hatchcolor-from-edgecolor "Link to this heading")

When the _hatchcolor_ parameter is specified, it will be used for the hatch. If it is not specified, it will fall back to using `[rcParams["hatch.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=hatch.color#rcparam-hatch-color) ` (default: `'edge'`). The special value 'edge' uses the patch edgecolor, with a fallback to `[rcParams["patch.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.edgecolor#rcparam-patch-edgecolor) ` (default: `'black'`) if the patch edgecolor is 'none'. Previously, hatch colors were the same as edge colors, with a fallback to `[rcParams["hatch.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=hatch.color#rcparam-hatch-color) ` (default: `'edge'`) if the patch did not have an edge color.

import matplotlib as mpl
from matplotlib.patches import Rectangle

fig, ax \= plt.subplots()

\# In this case, hatchcolor is orange
patch1 \= Rectangle((0.1, 0.1), 0.3, 0.3, edgecolor\='red', linewidth\=2,
                   hatch\='//', hatchcolor\='orange')
ax.add\_patch(patch1)

\# When hatchcolor is not specified, it matches edgecolor
\# In this case, hatchcolor is green
patch2 \= Rectangle((0.6, 0.1), 0.3, 0.3, edgecolor\='green', linewidth\=2,
                   hatch\='//', facecolor\='none')
ax.add\_patch(patch2)

\# If both hatchcolor and edgecolor are not specified
\# it will default to the 'patch.edgecolor' rcParam, which is black by default
\# In this case, hatchcolor is black
patch3 \= Rectangle((0.1, 0.6), 0.3, 0.3, hatch\='//')
ax.add\_patch(patch3)

\# When using \`hatch.color\` in the \`rcParams\`
\# edgecolor will now not overwrite hatchcolor
\# In this case, hatchcolor is black
with plt.rc\_context({'hatch.color': 'black'}):
    patch4 \= Rectangle((0.6, 0.6), 0.3, 0.3, edgecolor\='blue', linewidth\=2,
                       hatch\='//', facecolor\='none')

\# hatchcolor is black (it uses the \`hatch.color\` rcParam value)
patch4.set\_edgecolor('blue')
\# hatchcolor is still black (here, it does not update when edgecolor changes)
ax.add\_patch(patch4)

ax.annotate("hatchcolor = 'orange'",
            xy\=(.5, 1.03), xycoords\=patch1, ha\='center', va\='bottom')
ax.annotate("hatch color unspecified\\nedgecolor='green'",
            xy\=(.5, 1.03), xycoords\=patch2, ha\='center', va\='bottom')
ax.annotate("hatch color unspecified\\nusing patch.edgecolor",
            xy\=(.5, 1.03), xycoords\=patch3, ha\='center', va\='bottom')
ax.annotate("hatch.color='black'",
            xy\=(.5, 1.03), xycoords\=patch4, ha\='center', va\='bottom')

([`Source code`](https://matplotlib.org/stable/_downloads/d91e48e2e758920b0d8c911ce6d646c9/whats_new_3-11-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/643c9021fc16958a70162a91b6ef56c7/whats_new_3-11-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/74ffdeda63c7d66be867eb9b9b9f08a0/whats_new_3-11-0-9.png)
)

[![Four Rectangle patches, each displaying the color of hatches in different specifications of edgecolor and hatchcolor. Top left has hatchcolor='black' representing the default value when both hatchcolor and edgecolor are not set, top right has edgecolor='blue' and hatchcolor='black' which remains when the edgecolor is set again, bottom left has edgecolor='red' and hatchcolor='orange' on explicit specification and bottom right has edgecolor='green' and hatchcolor='green' when the hatchcolor is not set.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-9.2x.png)

For collections, a sequence of colors can be passed to the _hatchcolor_ parameter which will be cycled through for each hatch, similar to _facecolor_ and _edgecolor_.

Previously, if _edgecolor_ was not specified, the hatch color would fall back to `[rcParams["patch.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.edgecolor#rcparam-patch-edgecolor) ` (default: `'black'`), but the alpha value would default to **1.0**, regardless of the alpha value of the collection. This behavior has been changed such that, if both _hatchcolor_ and _edgecolor_ are not specified, the hatch color will fall back to 'patch.edgecolor' with the alpha value of the collection.

np.random.seed(19680801)

fig, ax \= plt.subplots()

x \= \[29, 36, 41, 25, 32, 70, 62, 58, 66, 80, 58, 68, 62, 37, 48\]
y \= \[82, 76, 48, 53, 62, 70, 84, 68, 55, 75, 29, 25, 12, 17, 20\]
colors \= \['tab:blue'\] \* 5 + \['tab:orange'\] \* 5 + \['tab:green'\] \* 5

ax.scatter(
    x,
    y,
    s\=800,
    hatch\="xxxx",
    hatchcolor\=colors,
    facecolor\="none",
    edgecolor\="black",
)

([`Source code`](https://matplotlib.org/stable/_downloads/fb5a746d36f157f45f2509ab048e8017/whats_new_3-11-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/6f9bb57b5345f3b09bad97b58f64c4cb/whats_new_3-11-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/cc4e5492027bae7333799a145da84891/whats_new_3-11-0-10.png)
)

[![A random scatter plot with hatches on the markers. The hatches are colored in blue, orange, and green, respectively. After the first three markers, the colors are cycled through again.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-10.2x.png)

[Axis and Ticks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#axis-and-ticks "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Standard getters/setters for axis inversion state](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#standard-getters-setters-for-axis-inversion-state "Link to this heading")

Whether an axis is inverted can now be queried using the [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 getters [`get_xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xinverted.html#matplotlib.axes.Axes.get_xinverted "matplotlib.axes.Axes.get_xinverted")
/[`get_yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yinverted.html#matplotlib.axes.Axes.get_yinverted "matplotlib.axes.Axes.get_yinverted")
 and set using [`set_xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted")
/[`set_yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted")
.

The previously existing methods ([`Axes.xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html#matplotlib.axes.Axes.xaxis_inverted "matplotlib.axes.Axes.xaxis_inverted")
, [`Axes.invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html#matplotlib.axes.Axes.invert_xaxis "matplotlib.axes.Axes.invert_xaxis")
) are now discouraged (but not deprecated) due to their non-standard naming and behavior.

### [`xtick` and `ytick` rotation modes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#xtick-and-ytick-rotation-modes "Link to this heading")

A new feature has been added for handling rotation of xtick and ytick labels more intuitively. The new [`rotation modes`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode")
 "xtick" and "ytick" automatically adjust the alignment of rotated tick labels, so that the text points towards their anchor point, i.e. ticks. This works for all four sides of the plot (bottom, top, left, right), reducing the need for manual adjustments when rotating labels.

fig, (ax1, ax2) \= plt.subplots(1, 2, figsize\=(7, 3.5), layout\='constrained')

pos \= range(5)
labels \= \['label'\] \* 5
ax1.set\_xticks(pos, labels, rotation\=-45, rotation\_mode\='xtick')
ax1.set\_yticks(pos, labels, rotation\=45, rotation\_mode\='ytick')
ax2.xaxis.tick\_top()
ax2.set\_xticks(pos, labels, rotation\=-45, rotation\_mode\='xtick')
ax2.yaxis.tick\_right()
ax2.set\_yticks(pos, labels, rotation\=45, rotation\_mode\='ytick')

([`Source code`](https://matplotlib.org/stable/_downloads/c9063e31db86581d99e3524a4e16f09c/whats_new_3-11-0-11.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/50d47b6e2ab5794d7a105098d7536c86/whats_new_3-11-0-11.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/744df487305d312dc6a0a9f8bd6928e0/whats_new_3-11-0-11.png)
)

[![Example of rotated xtick and ytick labels.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-11.2x.png)

### [Improved selection of log-scale ticks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id29)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#improved-selection-of-log-scale-ticks "Link to this heading")

The algorithm for selecting log-scale ticks (on powers of ten) has been improved. In particular, it will now always draw as many ticks as possible (e.g., it will not draw a single tick if it was possible to fit two ticks); if subsampling ticks, it will prefer putting ticks on integer multiples of the subsampling stride (e.g., it prefers putting ticks at 100, 103, 106 rather than 101, 104, 107) if this results in the same number of ticks at the end; and it is now more robust against floating-point calculation errors.

[Colors and colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id30)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#colors-and-colormaps "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Okabe-Ito accessible color sequence](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id31)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#okabe-ito-accessible-color-sequence "Link to this heading")

Matplotlib now includes the [Okabe-Ito color sequence](https://jfly.uni-koeln.de/color/#pallet)
. Its colors remain distinguishable for common forms of color-vision deficiency and when printed.

For example, to set it as the default colormap for your plots and image-like artists, use:

import matplotlib.pyplot as plt
from cycler import cycler

plt.rcParams\['axes.prop\_cycle'\] \= cycler(color\='okabe\_ito')
plt.rcParams\['image.cmap'\] \= 'okabe\_ito'

Or, when creating plots, you can pass it explicitly:

([`Source code`](https://matplotlib.org/stable/_downloads/71f827a740523bde09e2d761beb6e4a7/whats_new_3-11-0-12.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f6739edd33f6425bdf54e070dd413441/whats_new_3-11-0-12.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/70b37fd1a6bf87c842823775b2e06459/whats_new_3-11-0-12.png)
)

[![A plot of 8 lines, with colors of the Okabe-Ito sequence, from bottom to top: black, orange, sky blue, bluish green, yellow, blue, vermilion, and reddish purple.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-12.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-12.2x.png)

### [Six and eight color Petroff color cycles](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id32)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#six-and-eight-color-petroff-color-cycles "Link to this heading")

The six and eight color accessible Petroff color cycles are named `'petroff6'` and `'petroff8'`. They complement the existing `'petroff10'` color cycle, added in [Matplotlib 3.10.0](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.10.0.html#whats-new-3-10-0-petroff10)
.

For more details see [Petroff, M. A.: "Accessible Color Sequences for Data Visualization"](https://arxiv.org/abs/2107.02270)
. To load the `'petroff6'` color cycle in place of the default:

import matplotlib.pyplot as plt
plt.style.use('petroff6')

([`Source code`](https://matplotlib.org/stable/_downloads/d93fb99eee8ed2c8dd0b28fa8e947897/whats_new_3-11-0-13.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d07e6c8b4bb2a35eb74cc9d879b49d67/whats_new_3-11-0-13.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/4463ae677717def42e5212e795845523/whats_new_3-11-0-13.png)
)

[![A plot of 6 lines, with colors of the Petroff six-color cycle, from bottom to top: blue, orange, red, dark purple, grey, light purple.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-13.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-13.2x.png)

or to load the `'petroff8'` color cycle:

import matplotlib.pyplot as plt
plt.style.use('petroff8')

([`Source code`](https://matplotlib.org/stable/_downloads/1d338a4e4da06b1a43856e194807ae84/whats_new_3-11-0-14.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/5a530c7b63ed639578f83dec065620fd/whats_new_3-11-0-14.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3d7ea10b675b50335b73cf722fbdc242/whats_new_3-11-0-14.png)
)

[![A plot of 8 lines, with colors of the Petroff eight-color cycle, from bottom to top: blue, orange, red, purple, grey, light blue, blue, dark grey.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-14.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-14.2x.png)

### [Setting the default color cycle to a named color sequence](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id33)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#setting-the-default-color-cycle-to-a-named-color-sequence "Link to this heading")

The default color cycle may now be configured in the `matplotlibrc` file or a style file to use any of the [Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)
. For example

axes.prop\_cycle : cycler(color='Accent')

### [Colormaps support giving colors for bad, under and over values on creation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id34)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#colormaps-support-giving-colors-for-bad-under-and-over-values-on-creation "Link to this heading")

Colormaps gained keyword arguments `bad`, `under`, and `over` to specify these values on creation. Previously, these values would have to be set afterwards using one of [`set_bad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_bad "matplotlib.colors.Colormap.set_bad")
, [`set_under`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "matplotlib.colors.Colormap.set_under")
, [`set_bad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_bad "matplotlib.colors.Colormap.set_bad")
, [`set_extremes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_extremes "matplotlib.colors.Colormap.set_extremes")
, [`with_extremes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.with_extremes "matplotlib.colors.Colormap.with_extremes")
.

It is recommended to use the new functionality, e.g.:

cmap \= ListedColormap(colors, bad\="red", under\="darkblue", over\="purple")

instead of:

cmap \= ListedColormap(colors).with\_extremes(
    bad\="red", under\="darkblue", over\="purple")

or:

cmap \= ListedColormap(colors)
cmap.set\_bad("red")
cmap.set\_under("darkblue")
cmap.set\_over("purple")

### [Tuning transparency of colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id35)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#tuning-transparency-of-colormaps "Link to this heading")

The new method [`Colormap.with_alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.with_alpha "matplotlib.colors.Colormap.with_alpha")
 allows to create a new colormap with the same color values but a new uniform alpha value. This is handy if you want to modify only the transparency of mapped colors for an Artist.

[Fonts and Text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id36)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#fonts-and-text "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important

This release of Matplotlib includes a large update to text processing and rendering. Within our published wheels, the bundled version of FreeType has been updated, and the rendering pipeline itself has been overhauled to support modern features and fonts, as outlined below. It is unfortunately not possible to reproduce the exact same pixel values for a piece of rendered text as in previous versions.

If you are reliant on pixel-perfect consistency between versions, this will be broken in this release. For downstream packages that are testing plots, we recommend a few options:

1.  Update your test images directly; if you are comfortable with requiring 3.11 and above only, then this is the simplest option. However, it does mean dropping support for many users with older Matplotlib versions. Alternatively, provide two sets of test images, one before and one after. This would increase compatibility at the cost of disk space.
    
2.  Increase tolerances on tests with text. Note that this might obscure unintended differences, so be careful with increasing tolerances too high. If you are using Matplotlib's [`image_comparison`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.image_comparison "matplotlib.testing.decorators.image_comparison")
     decorator, you can pass the _tol_ argument:
    
    @image\_comparison(\['plot.png'\], tol\=5, style\='mpl20')
    def test\_plot():
        ...
    
    If you are using [pytest-mpl](https://pytest-mpl.readthedocs.io/)
    , then you can pass the _tolerance_ argument:
    
    @pytest.mark.mpl\_image\_compare(tolerance\=5)
    def test\_plot():
        ...
    
3.  Remove non-essential text elements. The easiest way to avoid this problem is to not have any text to worry about. For both the [`image_comparison`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.decorators.image_comparison "matplotlib.testing.decorators.image_comparison")
     decorator and [pytest-mpl](https://pytest-mpl.readthedocs.io/)
    , you can pass the _remove\_text_ argument:
    
    @image\_comparison(\['plot.png'\], remove\_text\=True, style\='mpl20')
    def test\_plot():
        ...
    
    @pytest.mark.mpl\_image\_compare(remove\_text\=True)
    def test\_plot():
        ...
    
    to remove the title and tick texts; note other deliberate texts are not removed.
    
4.  Replace text with placeholders. If you do need text to exist, but don't intend to check the exact pixels (for example, to confirm layout is correct), then you can replace the text with a placeholder of a fixed size. If you are using [pytest](http://doc.pytest.org/en/latest/)
    , the [`text_placeholders`](https://matplotlib.org/stable/api/testing_api.html#matplotlib.testing.conftest.text_placeholders "matplotlib.testing.conftest.text_placeholders")
     fixture may be used to replace text with a fixed-size box. Consider vendoring a similar fixture in your own tests if necessary.
    
5.  Use a different image comparison algorithm. While not available in Matplotlib's testing framework, a [perceptual hashing algorithm](https://en.wikipedia.org/wiki/Perceptual_hashing)
     may be more appropriate if you wish to avoid depending on exact pixel values.
    

### [Complex text layout with libraqm](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id37)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#complex-text-layout-with-libraqm "Link to this heading")

Text support has been extended to include complex text layout. This support includes:

1.  Languages that require advanced layout, such as Arabic or Hebrew.
    
2.  Text that mixes left-to-right and right-to-left languages.
    
    ([`2x.png`](https://matplotlib.org/stable/_downloads/927522cf261ce3c4b3c6e2be95fd4728/whats_new_3-11-0-15.2x.png)
    , [`png`](https://matplotlib.org/stable/_downloads/23ecd83eb0ac2c71dfc4ffe79b88eac8/whats_new_3-11-0-15.png)
    )
    
    [![The mixed-language text 'Here is some رَقْم in اَلْعَرَبِيَّةُ'.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-15.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-15.2x.png)
    
3.  Ligatures that combine several adjacent characters for improved legibility.
    
    ([`2x.png`](https://matplotlib.org/stable/_downloads/4d47caed9acc9cf5383164c2a24b6638/whats_new_3-11-0-16.2x.png)
    , [`png`](https://matplotlib.org/stable/_downloads/bb07109516964799c9c0d3f336562ea2/whats_new_3-11-0-16.png)
    )
    
    [![A rightwards arrow pointing from the individual letters 'f', 'f', and 'i', to the 'ffi' ligature.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-16.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-16.2x.png)
    
4.  Combining multiple or double-width diacritics.
    
    ([`2x.png`](https://matplotlib.org/stable/_downloads/0e692105ff1ef071c5a4723ea61fb90b/whats_new_3-11-0-17.2x.png)
    , [`png`](https://matplotlib.org/stable/_downloads/95e6124d2260b65c4a92ed92837448c4/whats_new_3-11-0-17.png)
    )
    
    [![An "equation" showing the letter 'a' plus a circumflex accent plus a tilde plus the letter 'c' plus a diaeresis, producing a single glyph of all of them.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-17.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-17.2x.png)
    

Note, all advanced features require corresponding font support, and may require additional fonts over the builtin DejaVu Sans.

Remove any pre-shaping workaround

Because Matplotlib did not previously reorder text, the usual workaround for Arabic, Persian, Urdu and Hebrew was to reorder the string before passing it in, typically with `arabic_reshaper` and `python-bidi`:

preprocessed \= get\_display(arabic\_reshaper.reshape(text))
ax.set\_title(preprocessed)

Matplotlib now reorders the string itself, so a string that arrives already in visual order is reordered a second time and is drawn backwards. Nothing is raised, and to a reader who does not read the script the result still looks like correct text, so this is easy to ship without noticing.

*   If you can require Matplotlib 3.11, pass the logical string and delete the pre-processing.
    
*   If you support older versions as well, branch on the Matplotlib version and pre-process only on the older one.
    
*   If you cannot change the call at all, because the text is handed to a third-party library that calls Matplotlib for you, wrap the pre-processed string in `LEFT-TO-RIGHT OVERRIDE` and `POP DIRECTIONAL FORMATTING`:
    
    text \= ('\\N{LEFT-TO-RIGHT OVERRIDE}' + preprocessed +
            '\\N{POP DIRECTIONAL FORMATTING}')
    
    That reads correctly on every version. It does not always render identically, because it draws the font's presentation-form glyphs rather than the font's own shaping, and some fonts space those differently.
    

### [Specifying font feature tags](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id38)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#specifying-font-feature-tags "Link to this heading")

OpenType fonts may support feature tags that specify alternate glyph shapes or substitutions to be made optionally. The text API now supports setting a list of feature tags to be used with the associated font. Feature tags can be set/get with:

*   [`matplotlib.text.Text.set_fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "matplotlib.text.Text.set_fontfeatures")
     / [`matplotlib.text.Text.get_fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_fontfeatures "matplotlib.text.Text.get_fontfeatures")
    
*   Any API that creates a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
     object by passing the _fontfeatures_ argument (e.g., `plt.xlabel(..., fontfeatures=...)`)
    

Font feature strings are eventually passed to HarfBuzz, and so all [string formats supported by hb\_feature\_from\_string()](https://harfbuzz.github.io/harfbuzz-hb-common.html#hb-feature-from-string)
 are supported. Note though that subranges are not explicitly supported and behaviour may change in the future.

For example, the default font `DejaVu Sans` enables Standard Ligatures (the `'liga'` tag) by default, and also provides optional Discretionary Ligatures (the `dlig` tag.) These may be toggled with `+` or `-`.

fig \= plt.figure(figsize\=(7, 3))

fig.text(0.5, 0.85, 'Ligatures', fontsize\=40, horizontalalignment\='center')

\# Default has Standard Ligatures (liga).
fig.text(0, 0.6, 'Default: fi ffi fl st', fontsize\=40)

\# Disable Standard Ligatures with -liga.
fig.text(0, 0.35, 'Disabled: fi ffi fl st', fontsize\=40,
         fontfeatures\=\['-liga'\])

\# Enable Discretionary Ligatures with dlig.
fig.text(0, 0.1, 'Discretionary: fi ffi fl st', fontsize\=40,
         fontfeatures\=\['dlig'\])

([`Source code`](https://matplotlib.org/stable/_downloads/414007d34f884c05f71beb0b467c2f93/whats_new_3-11-0-18.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1e629892edf3ef3da0dd9755a145515e/whats_new_3-11-0-18.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3c406de1044500dd19a6d03324b36681/whats_new_3-11-0-18.png)
)

[![An example of ligatures affecting text, in four lines. The first line is the title "Ligatures". Each subsequent line shows the style, followed by the examples "fi", "ffi", "fl", and "st". The second line is the default, where all but "st" use ligatures. The third line has disabled ligatures and all examples are drawn as individual glyphs. The fourth line has enabled discretionary ligatures and all examples, including the "st", use ligatures.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-18.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-18.2x.png)

Available font feature tags may be found at [https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist)

### [Specifying text language](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id39)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#specifying-text-language "Link to this heading")

OpenType fonts may support language systems which can be used to select different typographic conventions, e.g., localized variants of letters that share a single Unicode code point, or different default font features. The text API now supports setting a language to be used and may be set/get with:

*   [`matplotlib.text.Text.set_language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "matplotlib.text.Text.set_language")
     / [`matplotlib.text.Text.get_language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_language "matplotlib.text.Text.get_language")
    
*   Any API that creates a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
     object by passing the _language_ argument (e.g., `plt.xlabel(..., language=...)`)
    

The language of the text must be in a format accepted by libraqm, namely [a BCP47 language code](https://www.w3.org/International/articles/language-tags/)
. If None or unset, then no particular language will be implied, and default font settings will be used.

For example, Matplotlib's default font `DejaVu Sans` supports language-specific glyphs in the Serbian and Macedonian languages in the Cyrillic alphabet (vs Russian), or the Sámi family of languages in the Latin alphabet (vs English).

fig \= plt.figure(figsize\=(7, 3))

char \= '\\U00000431'
fig.text(0.5, 0.8, f'\\\\U{ord(char):08x}', fontsize\=40, horizontalalignment\='center')
fig.text(0, 0.6, f'Serbian: {char}', fontsize\=40, language\='sr')
fig.text(1, 0.6, f'Russian: {char}', fontsize\=40, language\='ru',
         horizontalalignment\='right')

char \= '\\U0000014a'
fig.text(0.5, 0.3, f'\\\\U{ord(char):08x}', fontsize\=40, horizontalalignment\='center')
fig.text(0, 0.1, f'Inari Sámi: {char}', fontsize\=40, language\='smn')
fig.text(1, 0.1, f'English: {char}', fontsize\=40, language\='en',
         horizontalalignment\='right')

([`Source code`](https://matplotlib.org/stable/_downloads/ece546963424441aa277e5e6e0f54091/whats_new_3-11-0-19.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/bed19ee5ce9fca850563acf7b130cc4d/whats_new_3-11-0-19.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/87e55d9b302e354d1cced630edde43fb/whats_new_3-11-0-19.png)
)

[![An example of how text language affects rendering, in four lines. The first line lists the Unicode code point '\U00000431`, which is the Cyrillic small letter BE. The second line then shows the rendering when the language is set to Serbian vs set to Russian. The third line lists the Unicode code point '\U0000014a`, which is the Latin capital letter ENG. The fourth line then shows the rendering when the language is set to Inari Sámi vs set to English.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-19.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-19.2x.png)

### [Missing glyphs use Last Resort font](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id40)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#missing-glyphs-use-last-resort-font "Link to this heading")

Most fonts do not have 100% character coverage, and will fall back to a "not found" glyph for characters that are not provided. Often, this glyph will be minimal (e.g., the default DejaVu Sans "not found" glyph is just a rectangle.) Such minimal glyphs provide no context as to the characters that are missing.

Now, missing glyphs will fall back to the [Last Resort font](https://github.com/unicode-org/last-resort-font)
 produced by the Unicode Consortium. This special-purpose font provides glyphs that represent types of Unicode characters. These glyphs show a representative character from the missing Unicode block, and at larger sizes, more context to help determine which character and font are needed.

To disable this fallback behaviour, set `[rcParams["font.enable_last_resort"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.enable_last_resort#rcparam-font-enable-last-resort) ` (default: `True`) to `False`.

([`Source code`](https://matplotlib.org/stable/_downloads/11e33c3c131cb40b78497e07c2c9e9de/whats_new_3-11-0-20.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/89ae120a8e3bb55a20689fb822cac455/whats_new_3-11-0-20.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7613b895893639da9bb8f52674362079/whats_new_3-11-0-20.png)
)

[![An example of missing glyph behaviour, the first glyph from Bengali script, second glyph from Hiragana, and the last glyph from the Unicode Private Use Area. Multiple lines repeat the text with increasing font size from top to bottom.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-20.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-20.2x.png)

### [Fonts addressable by all their SFNT family names](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id41)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#fonts-addressable-by-all-their-sfnt-family-names "Link to this heading")

Fonts can now be selected by any of the family names they advertise in the OpenType name table, not just the one FreeType reports as the primary family name.

Some fonts store different family names on different platforms or in different name-table entries. For example, Ubuntu Light stores `"Ubuntu"` in the Macintosh-platform Name ID 1 slot (which FreeType uses as the primary name) and `"Ubuntu Light"` in the Microsoft-platform Name ID 1 slot. Previously only the FreeType-derived name was registered, requiring an obscure weight-based workaround:

\# Previously required
matplotlib.rcParams\['font.family'\] \= 'Ubuntu'
matplotlib.rcParams\['font.weight'\] \= 300

All name-table entries that describe a family — Name ID 1 on both platforms, the Typographic Family (Name ID 16), and the WWS Family (Name ID 21) — are now registered as separate entries in the [`FontManager`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager "matplotlib.font_manager.FontManager")
, so any of those names can be used directly:

matplotlib.rcParams\['font.family'\] \= 'Ubuntu Light'

### [Support for loading TrueType Collection fonts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id42)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#support-for-loading-truetype-collection-fonts "Link to this heading")

TrueType Collection fonts (commonly found as files with a `.ttc` extension) are now supported. Namely, Matplotlib will include these file extensions in its scan for system fonts, and will add all sub-fonts to its list of available fonts (i.e., the list from [`get_font_names`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.get_font_names "matplotlib.font_manager.get_font_names")
).

From most high-level API, this means you should be able to specify the name of any sub-font in a collection just as you would any other font. Note that at this time, there is no way to specify the entire collection with any sort of automated selection of the internal sub-fonts.

In the low-level API, to ensure backwards-compatibility while facilitating this new support, a [`FontPath`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontPath "matplotlib.font_manager.FontPath")
 instance (comprised of a font path and a sub-font index, with behaviour similar to a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
) may be passed to the font management API in place of a simple [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")
 path. Any font management API that previously returned a string path now returns a [`FontPath`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontPath "matplotlib.font_manager.FontPath")
 instance instead.

### [New environment variable to ignore system fonts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id43)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#new-environment-variable-to-ignore-system-fonts "Link to this heading")

System fonts may be ignored by setting the [`MPL_IGNORE_SYSTEM_FONTS`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPL_IGNORE_SYSTEM_FONTS)
; this suppresses searching for system fonts (in known directories or via some platform-specific subprocess) as well as limiting the results from [`FontManager.findfont`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontManager.findfont "matplotlib.font_manager.FontManager.findfont")
.

### [Mathtext distinguishes _italic_ and _normal_ font](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id44)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#mathtext-distinguishes-italic-and-normal-font "Link to this heading")

Matplotlib's lightweight TeX expression parser (`usetex=False`) now distinguishes between _italic_ and _normal_ math fonts to closer replicate the behaviour of LaTeX. The normal math font is selected by default in math environment (unless the rcParam `mathtext.default` is overwritten) but can be explicitly set with the new `\mathnormal` command. Italic font is selected with `\mathit`. The main difference is that _italic_ produces italic digits, whereas _normal_ produces upright digits. Previously, it was not possible to typeset italic digits. Note that `normal` now corresponds to what used to be `it`, whereas `it` now renders all characters italic. **Important**: In case the default mathematics font is overwritten by setting `mathtext.default: it` in `matplotlibrc`, it must be either commented out or changed to `mathtext.default: normal` to preserve its behaviour. Otherwise, all alphanumeric characters, including digits, are rendered italic.

One difference to traditional LaTeX is that LaTeX further distinguishes between _normal_ (`\mathnormal`) and _default math_, where the default uses roman digits and normal uses oldstyle digits. This distinction is no longer present with modern LaTeX engines and unicode-math nor in Matplotlib.

### [mathtext support for `\phantom`, `\llap`, `\rlap`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id45)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#mathtext-support-for-phantom-llap-rlap "Link to this heading")

mathtext gained support for the TeX macros `\phantom`, `\llap`, and `\rlap`. `\phantom` allows to occupy some space on the canvas as if some text was being rendered, without actually rendering that text, whereas `\llap` and `\rlap` allows to render some text on the canvas while pretending that it occupies no space. Altogether these macros allow some finer control of text alignments.

See [https://www.tug.org/TUGboat/tb22-4/tb72perlS.pdf](https://www.tug.org/TUGboat/tb22-4/tb72perlS.pdf)
 for a detailed description of these macros.

For example, using these macros in the first legend below allows reserving space so that it is the same size as the second legend with longer text:

fig \= plt.figure(layout\="constrained")
sfs \= fig.subfigures(2)

ax0 \= sfs\[0\].add\_subplot()
ax0.plot(\[1, 2\], label\=r"$\\rlap{\\text{foo}}\\phantom{\\text{a longer label}}$")
sfs\[0\].legend(loc\="outside right upper")

ax1 \= sfs\[1\].add\_subplot()
ax1.plot(\[1, 2\], label\="foo")
ax1.plot(\[2, 1\], label\="a longer label")
sfs\[1\].legend(loc\="outside right upper")

([`Source code`](https://matplotlib.org/stable/_downloads/319ce10d1292a086bbe9a0e9c023637c/whats_new_3-11-0-21.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/da559a4f880d5eaf885ce6b9667f1da8/whats_new_3-11-0-21.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3fe81152345269c0af45d75f5ddf2d8d/whats_new_3-11-0-21.png)
)

[![Two plots of diagonal lines. The first Axes has a legend with a single entry labelled "foo". The second Axes has a legend with two entries labelled "foo" and "a longer label". Both legends are the same width despite the former containing a shorter label.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-21.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-21.2x.png)

### [Underlining text while using Mathtext](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id46)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#underlining-text-while-using-mathtext "Link to this heading")

Mathtext now supports the `\underline` command.

plt.figure(figsize\=(6, 2))
plt.text(0.05, 0.7, r'This is $\\underline{underlined}$ text.', fontsize\=24)
plt.text(0.05, 0.2, r'So is $\\underline{\\mathrm{this}}$.', fontsize\=24)
plt.axis('off')

([`Source code`](https://matplotlib.org/stable/_downloads/45ca6aab97e930bca03c2489a740ac92/whats_new_3-11-0-22.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/14323c9de643f1982d92d1c3cfe1ad0f/whats_new_3-11-0-22.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/11689071c18e1bb726090e578599d6af/whats_new_3-11-0-22.png)
)

[![Two lines of text. The first says "This is underlined text." and the word "underlined" is italic and has a line under it. The second line says "So us this." and the word "this" has a line under it.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-22.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-22.2x.png)

### [Improved font embedding in PDF](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id47)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#improved-font-embedding-in-pdf "Link to this heading")

Both Type 3 and Type 42 fonts (see [Fonts in Matplotlib](https://matplotlib.org/stable/users/explain/text/fonts.html#fonts)
 for more details) are now embedded into PDFs without limitation. Fonts may be split into multiple embedded subsets in order to satisfy format limits. Additionally, a corrected Unicode mapping is added for each.

This means that _all_ text should now be selectable and copyable in PDF viewers that support doing so.

When using the `usetex` feature, Matplotlib calls TeX to render the text and formulas in the figure. The fonts that get used are usually "Type 1" fonts. They used to be embedded in full but are now limited to the glyphs that are actually used in the figure. This reduces the size of the resulting PDF files.

[rcParams improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id48)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#rcparams-improvements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Separate styling options for major/minor grid line in rcParams](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id49)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#separate-styling-options-for-major-minor-grid-line-in-rcparams "Link to this heading")

Using `[rcParams["grid.major.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=grid.major.*#rcparam-grid-major-color) ` or `[rcParams["grid.minor.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=grid.minor.*#rcparam-grid-minor-color) ` will overwrite the value in `[rcParams["grid.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=grid.*#rcparam-grid-color) ` for the major and minor gridlines, respectively.

import matplotlib as mpl

\# Set visibility for major and minor gridlines
mpl.rcParams\["axes.grid"\] \= True
mpl.rcParams\["ytick.minor.visible"\] \= True
mpl.rcParams\["xtick.minor.visible"\] \= True
mpl.rcParams\["axes.grid.which"\] \= "both"

\# Using grid.\* to set both major and minor properties
mpl.rcParams\["grid.color"\] \= "lightgrey"

\# Overwrite some values for major and minor separately
mpl.rcParams\["grid.major.linewidth"\] \= 1.2
mpl.rcParams\["grid.minor.color"\] \= "tab:blue"
mpl.rcParams\["grid.minor.linestyle"\] \= ":"

plt.plot(\[0, 1\], \[0, 1\])

([`Source code`](https://matplotlib.org/stable/_downloads/5bb3ea6f08c34fd29a6ed771988c6999/whats_new_3-11-0-23.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/de83b001b66d722bf8dda73beb25a4ba/whats_new_3-11-0-23.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7512f4c8580ec3b4c6bd0606a78fe019/whats_new_3-11-0-23.png)
)

[![Modifying the gridlines using the new options `rcParams`](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-23.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-23.2x.png)

### [`axes.prop_cycle` rcParam security improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id50)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#axes-prop-cycle-rcparam-security-improvements "Link to this heading")

The `axes.prop_cycle` rcParam is now parsed in a safer and more restricted manner. Only literals, `cycler()` and `concat()` calls, the operators `+` and `*`, and slicing are allowed. All previously valid cycler strings documented at [https://matplotlib.org/cycler/](https://matplotlib.org/cycler/)
 are still supported, for example:

axes.prop\_cycle : cycler('color', \['r', 'g', 'b'\]) + cycler('linewidth', \[1, 2, 3\])
axes.prop\_cycle : 2 \* cycler('color', 'rgb')
axes.prop\_cycle : concat(cycler('color', 'rgb'), cycler('color', 'cmk'))
axes.prop\_cycle : cycler('color', 'rgbcmk')\[:3\]

[Legends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id51)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#legends "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`legend.linewidth` rcParam and parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id52)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#legend-linewidth-rcparam-and-parameter "Link to this heading")

A new rcParam `legend.linewidth` has been added to control the line width of the legend's box edges. When set to `None` (the default), it inherits the value from `patch.linewidth`. This allows for independent control of the legend frame line width without affecting other elements.

The [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 constructor also accepts a new _linewidth_ parameter to set the legend frame line width directly, overriding the rcParam value.

fig, ax \= plt.subplots()
ax.plot(\[1, 2, 3\], label\='data')
ax.legend(linewidth\=2.0)  \# Thick legend box edge

([`Source code`](https://matplotlib.org/stable/_downloads/7af05aee55df8910b0874b19176af8f7/whats_new_3-11-0-24.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d31fca77d537ac199b8203b416cbffb0/whats_new_3-11-0-24.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/97828937b0a0ef7263b7ebac01847b49/whats_new_3-11-0-24.png)
)

[![A line plot with a legend showing a thick border around the legend box.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-24.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-24.2x.png)

### [`PatchCollection` legends now supported](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id53)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#patchcollection-legends-now-supported "Link to this heading")

[`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 instances now properly display in legends when given a label. Previously, labels on [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 objects were ignored by the legend system, requiring users to create manual legend entries.

import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

fig, ax \= plt.subplots()
patches \= \[mpatches.Circle((0, 0.5), 0.1), mpatches.Rectangle((0.5, 0), 0.2, 0.3)\]
pc \= PatchCollection(patches, facecolor\='blue', edgecolor\='black', label\='My patches')
ax.add\_collection(pc)
ax.legend()  \# Now displays the label "My patches"

([`Source code`](https://matplotlib.org/stable/_downloads/834544887b53e8ec63102ce9337448f4/whats_new_3-11-0-25.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/02823a7c9c64abba3f79cbe9c79a1c49/whats_new_3-11-0-25.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/869bf98d94df82875b3f0bca4fe25790/whats_new_3-11-0-25.png)
)

[![The legend entry displays a rectangle matching the visual properties (colors, line styles, line widths) of the first patch in the collection.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-25.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-25.2x.png)

[Widgets and Interactivity](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id54)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#widgets-and-interactivity "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Zooming using mouse wheel](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id55)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#zooming-using-mouse-wheel "Link to this heading")

Control+MouseWheel can be used to zoom in the plot windows. Additionally, x+MouseWheel zooms only the x-axis and y+MouseWheel zooms only the y-axis.

The zoom focusses on the mouse pointer. With Control, the axes aspect ratio is kept; with x or y, only the respective axis is scaled.

Zooming is currently only supported on rectilinear Axes.

### [Consistent zoom boxes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id56)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#consistent-zoom-boxes "Link to this heading")

Zooming now has a consistent dashed box style across all backends.

### [RadioButtons and CheckButtons widgets support flexible layouts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id57)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#radiobuttons-and-checkbuttons-widgets-support-flexible-layouts "Link to this heading")

The [`widgets.RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 and [`widgets.CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
 widgets now support arranging buttons in different layouts via the new _layout_ parameter. You can arrange buttons vertically (default), horizontally, or in a 2D grid by passing a `(rows, cols)` tuple.

See [Radio Buttons Grid](https://matplotlib.org/stable/gallery/widgets/radio_buttons_grid.html)
 for a `(rows, cols)` example.

from matplotlib.widgets import CheckButtons

t \= np.arange(0.0, 2.0, 0.01)
s0 \= np.sin(2\*np.pi\*t)
s1 \= np.sin(4\*np.pi\*t)
s2 \= np.sin(6\*np.pi\*t)
s3 \= np.sin(8\*np.pi\*t)

fig, axes \= plt.subplot\_mosaic(
    \[\['main'\], \['buttons'\]\],
    height\_ratios\=\[8, 1\],
    layout\="constrained",
)

l0, \= axes\['main'\].plot(t, s0, lw\=2, label\='2 Hz')
l1, \= axes\['main'\].plot(t, s1, lw\=2, label\='4 Hz')
l2, \= axes\['main'\].plot(t, s2, lw\=2, label\='6 Hz')
l3, \= axes\['main'\].plot(t, s3, lw\=2, label\='8 Hz')
axes\['main'\].set\_xlabel('Time (s)')
axes\['main'\].set\_ylabel('Amplitude')

lines\_by\_label \= {l.get\_label(): l for l in \[l0, l1, l2, l3\]}

axes\['buttons'\].set\_facecolor('0.95')
check \= CheckButtons(
    axes\['buttons'\],
    labels\=lines\_by\_label.keys(),
    actives\=\[l.get\_visible() for l in lines\_by\_label.values()\],
    layout\='horizontal'
)

def callback(label):
    ln \= lines\_by\_label\[label\]
    ln.set\_visible(not ln.get\_visible())
    fig.canvas.draw\_idle()

check.on\_clicked(callback)

([`Source code`](https://matplotlib.org/stable/_downloads/f1a8af311946c9a808291fed56469c07/whats_new_3-11-0-26.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/eb9f925da64708d41e63f01d94156a35/whats_new_3-11-0-26.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/96bebfc449dfa1e7d644e2019294266a/whats_new_3-11-0-26.png)
)

[![Multiple sine waves with checkboxes to toggle their visibility.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-26.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-26.2x.png)

### [Callable _valfmt_ for `Slider` and `RangeSlider`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id58)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#callable-valfmt-for-slider-and-rangeslider "Link to this heading")

In addition to the existing %-format string, the _valfmt_ parameter of [`Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")
 and [`RangeSlider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")
 now also accepts a callable of the form `valfmt(val: float) -> str`.

### [WebAgg scroll capture control](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id59)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#webagg-scroll-capture-control "Link to this heading")

The WebAgg backend now provides the ability to capture scroll events to prevent page scrolling when interacting with plots. This can be enabled or disabled via the new [`FigureCanvasWebAggCore.set_capture_scroll`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.set_capture_scroll "matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.set_capture_scroll")
 and [`FigureCanvasWebAggCore.get_capture_scroll`](https://matplotlib.org/stable/api/backend_webagg_core_api.html#matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.get_capture_scroll "matplotlib.backends.backend_webagg_core.FigureCanvasWebAggCore.get_capture_scroll")
 methods.

[3D plotting improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id60)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#d-plotting-improvements "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Non-linear scales on 3D axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id61)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#non-linear-scales-on-3d-axes "Link to this heading")

Resolving a long-standing issue, 3D axes now support non-linear axis scales such as `'log'`, `'symlog'`, `'logit'`, `'asinh'`, and custom `'function'` scales, just like 2D axes. Use [`set_xscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale")
, [`set_yscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_yscale")
, and [`set_zscale`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zscale")
 to set the scale for each axis independently.

\# A sine chirp with increasing frequency and amplitude
x \= np.linspace(0, 1, 400)  \# time
y \= 10 \*\* (2 \* x)  \# frequency, growing exponentially from 1 to 100 Hz
phase \= 2 \* np.pi \* (10 \*\* (2 \* x) \- 1) / (2 \* np.log(10))
z \= np.sin(phase) \* x \*\* 2 \* 10  \# amplitude, growing quadratically

fig \= plt.figure()
ax \= fig.add\_subplot(projection\='3d')
ax.plot(x, y, z)

ax.set\_xlabel('Time (linear)')
ax.set\_ylabel('Frequency, Hz (log)')
ax.set\_zlabel('Amplitude (symlog)')

ax.set\_yscale('log')
ax.set\_zscale('symlog')

([`Source code`](https://matplotlib.org/stable/_downloads/ac41f117595b9491fe2d3a545d33f51e/whats_new_3-11-0-27.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9ef322808c644abad610b4717725aab1/whats_new_3-11-0-27.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7f5b5aefbea1971b1ebbd528a34e8bac/whats_new_3-11-0-27.png)
)

[![A 3D plot with a linear x-axis, logarithmic y-axis, and symlog z-axis.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-27.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-27.2x.png)

See [`matplotlib.scale`](https://matplotlib.org/stable/api/scale_api.html#module-matplotlib.scale "matplotlib.scale")
 for details on all available scales and their parameters.

### [Snapping 3D rotation angles with Control key](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id62)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#snapping-3d-rotation-angles-with-control-key "Link to this heading")

Rotation of 3D axes now supports snapping to fixed angular increments when holding the Control key during mouse rotation.

The snap step size is controlled by the new `[rcParams["axes3d.snap_rotation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.snap_rotation#rcparam-axes3d-snap-rotation) ` (default: `5.0`) rcParam. Setting it to 0 disables snapping.

For example:

mpl.rcParams\["axes3d.snap\_rotation"\] \= 10

will snap elevation, azimuth, and roll angles to multiples of 10 degrees while rotating with the mouse.

### [3D depth-shading fix](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id63)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#d-depth-shading-fix "Link to this heading")

Previously, a slightly buggy method of estimating the visual "depth" of 3D items could lead to sudden and unexpected changes in transparency as the plot orientation changed.

Now, the behavior has been made smooth and predictable. A new parameter _depthshade\_minalpha_ has also been added to allow users to set the minimum transparency level. Depth-shading is an option for [`Patch3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3DCollection.html#mpl_toolkits.mplot3d.art3d.Patch3DCollection "mpl_toolkits.mplot3d.art3d.Patch3DCollection")
 and [`Path3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection "mpl_toolkits.mplot3d.art3d.Path3DCollection")
, including 3D scatter plots.

The default values for `depthshade` and `depthshade_minalpha` are now controlled by `[rcParams["axes3d.depthshade"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.depthshade#rcparam-axes3d-depthshade) ` (default: `True`) and `[rcParams["axes3d.depthshade_minalpha"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.depthshade_minalpha#rcparam-axes3d-depthshade-minalpha) ` (default: `0.3`), respectively.

A simple example:

fig \= plt.figure()
ax \= fig.add\_subplot(projection\="3d")

X \= \[i for i in range(10)\]
Y \= \[i for i in range(10)\]
Z \= \[i for i in range(10)\]
S \= \[(i + 1) \* 400 for i in range(10)\]

ax.scatter(
    xs\=X, ys\=Y, zs\=Z, s\=S,
    depthshade\=True,
    depthshade\_minalpha\=0.3,
)
ax.view\_init(elev\=10, azim\=-150, roll\=0)

([`Source code`](https://matplotlib.org/stable/_downloads/3ef4cf17676c3692924c97eabece35ab/whats_new_3-11-0-28.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/5a60a2c0426cb75544ce348014ca6810/whats_new_3-11-0-28.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7a6f3276a0cb340ae275da8da769936a/whats_new_3-11-0-28.png)
)

[![A 3D scatter plot with depth-shading enabled.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-28.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-28.2x.png)

### [3D performance improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id64)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#d-performance-improvements "Link to this heading")

Draw time for 3D plots has been improved, especially for surface and wireframe plots. Users should see up to a 10× speedup in some cases. This should make interacting with 3D plots much more responsive.

[Other improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id65)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#other-improvements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Saving figures as GIF works again](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id66)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#saving-figures-as-gif-works-again "Link to this heading")

According to the figure documentation, the `savefig` method supports the GIF format with the file extension `.gif`. However, GIF support had been broken since Matplotlib 2.0.0. It works again.

### [`CallbackRegistry.disconnect` allows directly callbacks by function](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id67)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#callbackregistry-disconnect-allows-directly-callbacks-by-function "Link to this heading")

[`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
 now allows directly passing a function and optionally signal to [`disconnect`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.disconnect "matplotlib.cbook.CallbackRegistry.disconnect")
 instead of needing to track the callback ID returned by [`connect`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
.

from matplotlib.cbook import CallbackRegistry

def my\_callback(event):
    print(event)

callbacks \= CallbackRegistry()
callbacks.connect('my\_signal', my\_callback)

\# Disconnect by function reference instead of callback ID
callbacks.disconnect('my\_signal', my\_callback)

### [`violin_stats` simpler _method_ parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#id68)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.11.0.html#violin-stats-simpler-method-parameter "Link to this heading")

The _method_ parameter of [`violin_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")
 may now be specified as tuple of strings, and has a new default `("GaussianKDE", "scott")`. Calling [`violin_stats`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")
 followed by [`violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin")
 is therefore now equivalent to calling [`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
.

from matplotlib.cbook import violin\_stats

rng \= np.random.default\_rng(19680801)
data \= rng.normal(size\=(10, 3))

fig, (ax1, ax2) \= plt.subplots(ncols\=2, layout\='constrained', figsize\=(6.4, 3.5))

\# Create the violin plot in one step
ax1.violinplot(data)
ax1.set\_title('One Step')

\# Process the data and then create the violin plot
vstats \= violin\_stats(data)
ax2.violin(vstats)
ax2.set\_title('Two Steps')

([`Source code`](https://matplotlib.org/stable/_downloads/2b84cca655500b93e3c47341f53fcc9d/whats_new_3-11-0-29.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/fc1de2917038b65977eb317697f5ec77/whats_new_3-11-0-29.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/38f7583bf640ef27be74e746e01bedbb/whats_new_3-11-0-29.png)
)

[![Example showing violin_stats followed by violin gives the same result as violinplot.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-29.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-11-0-29.2x.png)

On this page