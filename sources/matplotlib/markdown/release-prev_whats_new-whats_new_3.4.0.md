[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#main-content)

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
    

[What's new in Matplotlib 3.4.0 (Mar 26, 2021)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#what-s-new-in-matplotlib-3-4-0-mar-26-2021 "Link to this heading")

================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Figure and Axes creation / management](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#figure-and-axes-creation-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [New subfigure functionality](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-subfigure-functionality "Link to this heading")

New [`figure.Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
 and [`figure.Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 functionalities allow creating virtual figures within figures. Similar nesting was previously done with nested gridspecs (see [Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)
). However, this did not allow localized figure artists (e.g., a colorbar or suptitle) that only pertained to each subgridspec.

The new methods [`figure.Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
 and [`figure.Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 are meant to rhyme with [`figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 and [`figure.Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 and have most of the same arguments.

See [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)
 for further details.

Note

The subfigure functionality is experimental API as of v3.4.

([`Source code`](https://matplotlib.org/stable/_downloads/9b47a4c1ff77bcdcd8f9e18566c1889f/whats_new_3-4-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/bb9a7ad4f873804e5637dd8f2ed7bea5/whats_new_3-4-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/eb55c9fce6b9170601a6376946776b4f/whats_new_3-4-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-1.2x.png)

### [Single-line string notation for `subplot_mosaic`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#single-line-string-notation-for-subplot-mosaic "Link to this heading")

[`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 and [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 now accept a single-line string, using semicolons to delimit rows. Namely,

plt.subplot\_mosaic(
    """
    AB
    CC
    """)

may be written as the shorter:

plt.subplot\_mosaic("AB;CC")

([`Source code`](https://matplotlib.org/stable/_downloads/1ab968a2b57442281c682950cd8c78b3/whats_new_3-4-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/756b068cd1a2b281fa885ea67cd1ca87/whats_new_3-4-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c2fda40361f0326ffd3f9fa4a5da18ba/whats_new_3-4-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-2.2x.png)

### [Changes to behavior of Axes creation methods (`gca`, `add_axes`, `add_subplot`)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#changes-to-behavior-of-axes-creation-methods-gca-add-axes-add-subplot "Link to this heading")

The behavior of the functions to create new Axes ([`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
, [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
, [`figure.Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
, [`figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
) has changed. In the past, these functions would detect if you were attempting to create Axes with the same keyword arguments as already-existing Axes in the current Figure, and if so, they would return the existing Axes. Now, [`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
, [`figure.Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
, and [`figure.Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 will always create new Axes. [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 will continue to reuse an existing Axes with a matching subplot spec and equal _kwargs_.

Correspondingly, the behavior of the functions to get the current Axes ([`pyplot.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
, [`figure.Figure.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "matplotlib.figure.Figure.gca")
) has changed. In the past, these functions accepted keyword arguments. If the keyword arguments matched an already-existing Axes, then that Axes would be returned, otherwise new Axes would be created with those keyword arguments. Now, the keyword arguments are only considered if there are no Axes at all in the current figure. In a future release, these functions will not accept keyword arguments at all.

### [`add_subplot`/`add_axes` gained an _axes\_class_ parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#add-subplot-add-axes-gained-an-axes-class-parameter "Link to this heading")

In particular, `mpl_toolkits` Axes subclasses can now be idiomatically used using, e.g., `fig.add_subplot(axes_class=mpl_toolkits.axislines.Axes)`

### [Subplot and subplot2grid can now work with constrained layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#subplot-and-subplot2grid-can-now-work-with-constrained-layout "Link to this heading")

`constrained_layout` depends on a single [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 for each logical layout on a figure. Previously, [`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
 and [`pyplot.subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
 added a new `GridSpec` each time they were called and were therefore incompatible with `constrained_layout`.

Now `subplot` attempts to reuse the `GridSpec` if the number of rows and columns is the same as the top level GridSpec already in the figure, i.e., `plt.subplot(2, 1, 2)` will use the same GridSpec as `plt.subplot(2, 1, 1)` and the `constrained_layout=True` option to [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 will work.

In contrast, mixing _nrows_ and _ncols_ will _not_ work with `constrained_layout`: `plt.subplot(2, 2, 1)` followed by `plt.subplots(2, 1, 2)` will still produce two GridSpecs, and `constrained_layout=True` will give bad results. In order to get the desired effect, the second call can specify the cells the second Axes is meant to cover: `plt.subplots(2, 2, (2, 4))`, or the more Pythonic `plt.subplot2grid((2, 2), (0, 1), rowspan=2)` can be used.

[Plotting methods](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#plotting-methods "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`axline` supports _transform_ parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#axline-supports-transform-parameter "Link to this heading")

[`axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
 now supports the _transform_ parameter, which applies to the points _xy1_, _xy2_. The _slope_ (if given) is always in data coordinates.

For example, this can be used with `ax.transAxes` for drawing lines with a fixed slope. In the following plot, the line appears through the same point on both Axes, even though they show different data limits.

fig, axs \= plt.subplots(1, 2)

for i, ax in enumerate(axs):
    ax.axline((0.25, 0), slope\=2, transform\=ax.transAxes)
    ax.set(xlim\=(i, i+5), ylim\=(i, i+5))

([`Source code`](https://matplotlib.org/stable/_downloads/6b0955eac721bd81641cc1438cc91c54/whats_new_3-4-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/61efabe601a8acce64875f530389092f/whats_new_3-4-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8ec3a35986a0866463dc96600ecaf554/whats_new_3-4-0-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-3.2x.png)

### [New automatic labeling for bar charts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-automatic-labeling-for-bar-charts "Link to this heading")

A new [`Axes.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
 method has been added for auto-labeling bar charts.

[![../../_images/sphx_glr_bar_label_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_bar_label_demo_001.png)](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)

Example of the new automatic labeling.[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id1 "Link to this image")

### [A list of hatches can be specified to](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id13)
 [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#a-list-of-hatches-can-be-specified-to-bar-and-barh "Link to this heading")

Similar to some other rectangle properties, it is now possible to hand a list of hatch styles to [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 in order to create bars with different hatch styles, e.g.

([`Source code`](https://matplotlib.org/stable/_downloads/bc3f0c544a8477315e6289e5731f5cda/whats_new_3-4-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ae5d4cc319626bb1183e3b4816f3bde6/whats_new_3-4-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b15b94bb27db4d8b3290ba7f00400eb7/whats_new_3-4-0-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-4.2x.png)

### [Setting `BarContainer` orientation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#setting-barcontainer-orientation "Link to this heading")

[`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 now accepts a new string argument _orientation_. It can be either `'vertical'` or `'horizontal'`, default is `None`.

### [Contour plots now default to using ScalarFormatter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#contour-plots-now-default-to-using-scalarformatter "Link to this heading")

Pass `fmt="%1.3f"` to the contouring call to restore the old default label format.

### [`Axes.errorbar` cycles non-color properties correctly](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#axes-errorbar-cycles-non-color-properties-correctly "Link to this heading")

Formerly, [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 incorrectly skipped the Axes property cycle if a color was explicitly specified, even if the property cycler was for other properties (such as line style). Now, [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 will advance the Axes property cycle as done for [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, i.e., as long as all properties in the cycler are not explicitly passed.

For example, the following will cycle through the line styles:

x \= np.arange(0.1, 4, 0.5)
y \= np.exp(\-x)
offsets \= \[0, 1\]

plt.rcParams\['axes.prop\_cycle'\] \= plt.cycler('linestyle', \['-', '--'\])

fig, ax \= plt.subplots()
for offset in offsets:
    ax.errorbar(x, y + offset, xerr\=0.1, yerr\=0.3, fmt\='tab:blue')

([`Source code`](https://matplotlib.org/stable/_downloads/5ddfc33f05e104234f237869906b2b7c/whats_new_3-4-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/81088eebd709cabd4de9d0f4ac6c93bf/whats_new_3-4-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f3c041d1deb2a1b7a27c36bd50b34fb7/whats_new_3-4-0-5.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-5.2x.png)

### [`errorbar` _errorevery_ parameter matches _markevery_](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#errorbar-errorevery-parameter-matches-markevery "Link to this heading")

Similar to the _markevery_ parameter to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
, the _errorevery_ parameter of [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 now accept slices and NumPy fancy indexes (which must match the size of _x_).

([`Source code`](https://matplotlib.org/stable/_downloads/76e12d6323677f76fdff1e0bfdd3dd33/whats_new_3-4-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e1cf4cb35340c4df28eaa4fa68f8a2d8/whats_new_3-4-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/610a8d48d5436c9e4e380b95ab187798/whats_new_3-4-0-6.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-6.2x.png)

### [`hexbin` supports data reference for _C_ parameter](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#hexbin-supports-data-reference-for-c-parameter "Link to this heading")

As with the _x_ and _y_ parameters, [`Axes.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 now supports passing the _C_ parameter using a data reference.

data \= {
    'a': np.random.rand(1000),
    'b': np.random.rand(1000),
    'c': np.random.rand(1000),
}

fig, ax \= plt.subplots()
ax.hexbin('a', 'b', C\='c', data\=data, gridsize\=10)

([`Source code`](https://matplotlib.org/stable/_downloads/1f634e6ab4fe8718f89658beef519fcc/whats_new_3-4-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9c9bf92e50a98ee1ea5ea354efd1d7ee/whats_new_3-4-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ee7bdcff117df0beba26446566f8ca12/whats_new_3-4-0-7.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-7.2x.png)

### [Support callable for formatting of Sankey labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#support-callable-for-formatting-of-sankey-labels "Link to this heading")

The [`format`](https://docs.python.org/3/library/functions.html#format "(in Python v3.14)")
 parameter of [`matplotlib.sankey.Sankey`](https://matplotlib.org/stable/api/sankey_api.html#matplotlib.sankey.Sankey "matplotlib.sankey.Sankey")
 can now accept callables.

This allows the use of an arbitrary function to label flows, for example allowing the mapping of numbers to emoji.

([`Source code`](https://matplotlib.org/stable/_downloads/3c19cc704a3fc0d82562be1a666f5d4c/whats_new_3-4-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b7b2d859c0be6d1deb9ffa69e2dceb3a/whats_new_3-4-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f78d24b41e940f2d014a395d75bd03a2/whats_new_3-4-0-8.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-8.2x.png)

### [`Axes.spines` access shortcuts](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#axes-spines-access-shortcuts "Link to this heading")

`Axes.spines` is now a dedicated container class [`Spines`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
 for a set of [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
s instead of an `OrderedDict`. On top of dict-like access, `Axes.spines` now also supports some `pandas.Series`\-like features.

Accessing single elements by item or by attribute:

ax.spines\['top'\].set\_visible(False)
ax.spines.top.set\_visible(False)

Accessing a subset of items:

ax.spines\[\['top', 'right'\]\].set\_visible(False)

Accessing all items simultaneously:

ax.spines\[:\].set\_visible(False)

### [New `stairs` method and `StepPatch` artist](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-stairs-method-and-steppatch-artist "Link to this heading")

[`pyplot.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs")
 and the underlying artist [`StepPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.StepPatch.html#matplotlib.patches.StepPatch "matplotlib.patches.StepPatch")
 provide a cleaner interface for plotting stepwise constant functions for the common case that you know the step edges. This supersedes many use cases of [`pyplot.step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html#matplotlib.pyplot.step "matplotlib.pyplot.step")
, for instance when plotting the output of [`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "(in NumPy v2.5)")
.

For both the artist and the function, the x-like edges input is one element longer than the y-like values input

([`Source code`](https://matplotlib.org/stable/_downloads/f5e7c45f25a513b651e1e4a5f5426660/whats_new_3-4-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c604437859b4b4a15fa7164bedf79af4/whats_new_3-4-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/977f056b37e412efa313de42093f64b6/whats_new_3-4-0-9.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-9.2x.png)

See [Stairs Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/stairs_demo.html)
 for examples.

### [Added _orientation_ parameter for stem plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#added-orientation-parameter-for-stem-plots "Link to this heading")

By default, stem lines are vertical. They can be changed to horizontal using the _orientation_ parameter of [`Axes.stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem")
 or [`pyplot.stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem")
:

([`Source code`](https://matplotlib.org/stable/_downloads/6f6f118ace39191755348c7140755975/whats_new_3-4-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/fe639426c692ecf3e9a6dc14dfa80fae/whats_new_3-4-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e474c1e91cd3608682dcd0a98b88823f/whats_new_3-4-0-10.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-10.2x.png)

### [Angles on Bracket arrow styles](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#angles-on-bracket-arrow-styles "Link to this heading")

Angles specified on the _Bracket_ arrow styles (`]-[`, `]-`, `-[`, or `|-|` passed to _arrowstyle_ parameter of [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")\
) are now applied. Previously, the _angleA_ and _angleB_ options were allowed, but did nothing.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/9073ebba544f03a2e7ce5d6ad7f325bb/whats_new_3-4-0-11.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/bac7f0e53c6fb5b73cc54ef056ffa930/whats_new_3-4-0-11.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/f844cbaa856780c4fc1dcf43a2c235ec/whats_new_3-4-0-11.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-11.2x.png)\
\
### [`TickedStroke` patheffect](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id24)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#tickedstroke-patheffect "Link to this heading")\
\
The new [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")\
 patheffect can be used to produce lines with a ticked style. This can be used to, e.g., distinguish the valid and invalid sides of the constraint boundaries in the solution space of optimizations.\
\
[![../../_images/sphx_glr_tickedstroke_demo_002.png](https://matplotlib.org/stable/_images/sphx_glr_tickedstroke_demo_002.png)](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)\
\
[Colors and colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id25)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#colors-and-colormaps "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Collection color specification and mapping](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id26)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#collection-color-specification-and-mapping "Link to this heading")\
\
Reworking the handling of color mapping and the keyword arguments for _facecolor_ and _edgecolor_ has resulted in three behavior changes:\
\
1.  Color mapping can be turned off by calling `Collection.set_array(None)`. Previously, this would have no effect.\
    \
2.  When a mappable array is set, with `facecolor='none'` and `edgecolor='face'`, both the faces and the edges are left uncolored. Previously the edges would be color-mapped.\
    \
3.  When a mappable array is set, with `facecolor='none'` and `edgecolor='red'`, the edges are red. This addresses Issue #1302. Previously the edges would be color-mapped.\
    \
\
### [Transparency (alpha) can be set as an array in collections](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id27)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#transparency-alpha-can-be-set-as-an-array-in-collections "Link to this heading")\
\
Previously, the alpha value controlling transparency in collections could be specified only as a scalar applied to all elements in the collection. For example, all the markers in a [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")\
 plot, or all the quadrilaterals in a [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")\
 plot, would have the same alpha value.\
\
Now it is possible to supply alpha as an array with one value for each element (marker, quadrilateral, etc.) in a collection.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/17b266a29e1dd360a307eba3ba72ba09/whats_new_3-4-0-12.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/90eb8ea167ea66e176b0d9752cdb8248/whats_new_3-4-0-12.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/0ffa199fa52e51bace8d59f9491fcc70/whats_new_3-4-0-12.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-12.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-12.2x.png)\
\
### [pcolormesh has improved transparency handling by enabling snapping](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id28)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#pcolormesh-has-improved-transparency-handling-by-enabling-snapping "Link to this heading")\
\
Due to how the snapping keyword argument was getting passed to the Agg backend, previous versions of Matplotlib would appear to show lines between the grid edges of a mesh with transparency. This version now applies snapping by default. To restore the old behavior (e.g., for test images), you may set `[rcParams["pcolormesh.snap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pcolormesh.snap#rcparam-pcolormesh-snap) ` (default: `True`) to [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")\
.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/ee4db1f7601dc72ae5649c84f83ce125/whats_new_3-4-0-13.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/fdf8ed592ae1d9db5bdf4ddb30b4e474/whats_new_3-4-0-13.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/2bf4f7abe24c3a0542a4bd123e626938/whats_new_3-4-0-13.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-13.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-13.2x.png)\
\
Note that there are lines between the grid boundaries of the main plot which are not the same transparency. The colorbar also shows these lines when a transparency is added to the colormap because internally it uses pcolormesh to draw the colorbar. With snapping on by default (below), the lines at the grid boundaries disappear.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/93bb373a79c104ffbb82f4049721303a/whats_new_3-4-0-14.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/8dc72479cd796b1d5c93c07ea0819a43/whats_new_3-4-0-14.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/3d9af8ffac87fa288dd5d1a30cf3a170/whats_new_3-4-0-14.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-14.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-14.2x.png)\
\
### [IPython representations for Colormap objects](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id29)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#ipython-representations-for-colormap-objects "Link to this heading")\
\
The [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")\
 object now has image representations for IPython / Jupyter backends. Cells returning a colormap on the last line will display an image of the colormap.\
\
In\[1\]: cmap \= plt.get\_cmap('viridis').with\_extremes(bad\='r', under\='g', over\='b')\
\
In\[2\]: cmap\
Out\[2\]:\
\
**viridis**\
\
![viridis colormap](<Base64-Image-Removed>)\
\
under\
\
bad\
\
over\
\
### [`Colormap.set_extremes` and `Colormap.with_extremes`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id30)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#colormap-set-extremes-and-colormap-with-extremes "Link to this heading")\
\
Because the [`Colormap.set_bad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_bad "matplotlib.colors.Colormap.set_bad")\
, [`Colormap.set_under`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "matplotlib.colors.Colormap.set_under")\
 and [`Colormap.set_over`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_over "matplotlib.colors.Colormap.set_over")\
 methods modify the colormap in place, the user must be careful to first make a copy of the colormap if setting the extreme colors e.g. for a builtin colormap.\
\
The new `Colormap.with_extremes(bad=..., under=..., over=...)` can be used to first copy the colormap and set the extreme colors on that copy.\
\
The new [`Colormap.set_extremes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_extremes "matplotlib.colors.Colormap.set_extremes")\
 method is provided for API symmetry with [`Colormap.with_extremes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.with_extremes "matplotlib.colors.Colormap.with_extremes")\
, but note that it suffers from the same issue as the earlier individual setters.\
\
### [Get under/over/bad colors of Colormap objects](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id31)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#get-under-over-bad-colors-of-colormap-objects "Link to this heading")\
\
[`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")\
 now has methods [`get_under`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.get_under "matplotlib.colors.Colormap.get_under")\
, [`get_over`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.get_over "matplotlib.colors.Colormap.get_over")\
, [`get_bad`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.get_bad "matplotlib.colors.Colormap.get_bad")\
 for the colors used for out-of-range and masked values.\
\
### [New `cm.unregister_cmap` function](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id32)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-cm-unregister-cmap-function "Link to this heading")\
\
`matplotlib.cm.unregister_cmap` allows users to remove a colormap that they have previously registered.\
\
### [New `CenteredNorm` for symmetrical data around a center](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id33)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-centerednorm-for-symmetrical-data-around-a-center "Link to this heading")\
\
In cases where data is symmetrical around a center, for example, positive and negative anomalies around a center zero, [`CenteredNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm "matplotlib.colors.CenteredNorm")\
 is a new norm that automatically creates a symmetrical mapping around the center. This norm is well suited to be combined with a divergent colormap which uses an unsaturated color in its center.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/8a615b076a8ba607739f167d9bc7c524/whats_new_3-4-0-15.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/3677ee4b841f55f0b4cea61a0288c71e/whats_new_3-4-0-15.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/0d6139256350647a83f7a10911a675d7/whats_new_3-4-0-15.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-15.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-15.2x.png)\
\
If the center of symmetry is different from 0, it can be set with the _vcenter_ argument. To manually set the range of [`CenteredNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm "matplotlib.colors.CenteredNorm")\
, use the _halfrange_ argument.\
\
See [Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)\
 for an example and more details about data normalization.\
\
### [New `FuncNorm` for arbitrary normalizations](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id34)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-funcnorm-for-arbitrary-normalizations "Link to this heading")\
\
The [`FuncNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.FuncNorm.html#matplotlib.colors.FuncNorm "matplotlib.colors.FuncNorm")\
 allows for arbitrary normalization using functions for the forward and inverse.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/337aaf05432305d99a9f16b959ce1b6d/whats_new_3-4-0-16.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/4e369b04dd7ecfb03e557864daa9c06c/whats_new_3-4-0-16.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/c466b7460af2b334fb7e32da4fe257ea/whats_new_3-4-0-16.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-16.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-16.2x.png)\
\
See [Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)\
 for an example and more details about data normalization.\
\
### [GridSpec-based colorbars can now be positioned above or to the left of the main axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id35)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#gridspec-based-colorbars-can-now-be-positioned-above-or-to-the-left-of-the-main-axes "Link to this heading")\
\
... by passing `location="top"` or `location="left"` to the `colorbar()` call.\
\
[Titles, ticks, and labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id36)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#titles-ticks-and-labels "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [supxlabel and supylabel](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id37)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#supxlabel-and-supylabel "Link to this heading")\
\
It is possible to add x- and y-labels to a whole figure, analogous to [`Figure.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")\
 using the new [`Figure.supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html#matplotlib.figure.Figure.supxlabel "matplotlib.figure.Figure.supxlabel")\
 and [`Figure.supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html#matplotlib.figure.Figure.supylabel "matplotlib.figure.Figure.supylabel")\
 methods.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/42da74b75f79dc2f766c5095a6c58cf9/whats_new_3-4-0-17.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/20ccd97bb48ca74db1a25675e88a2472/whats_new_3-4-0-17.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/333c6a8bb8195d7c90548530f3379437/whats_new_3-4-0-17.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-17.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-17.2x.png)\
\
### [Shared-axes `subplots` tick label visibility is now correct for top or left labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id38)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#shared-axes-subplots-tick-label-visibility-is-now-correct-for-top-or-left-labels "Link to this heading")\
\
When calling `subplots(..., sharex=True, sharey=True)`, Matplotlib automatically hides x tick labels for Axes not in the first column and y tick labels for Axes not in the last row. This behavior is incorrect if rcParams specify that Axes should be labeled on the top (`rcParams["xtick.labeltop"] = True`) or on the right (`rcParams["ytick.labelright"] = True`).\
\
Cases such as the following are now handled correctly (adjusting visibility as needed on the first row and last column of Axes):\
\
plt.rcParams\["xtick.labelbottom"\] \= False\
plt.rcParams\["xtick.labeltop"\] \= True\
plt.rcParams\["ytick.labelleft"\] \= False\
plt.rcParams\["ytick.labelright"\] \= True\
\
fig, axs \= plt.subplots(2, 2, sharex\=True, sharey\=True)\
\
([`Source code`](https://matplotlib.org/stable/_downloads/cb0833f9d337d0c455aa6d5faaa7778e/whats_new_3-4-0-18.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/c451c286d9955095e8ceaf67a41b58f9/whats_new_3-4-0-18.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/36ee507d9ddb86d6e4f4b27925004698/whats_new_3-4-0-18.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-18.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-18.2x.png)\
\
### [An iterable object with labels can be passed to](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id39)\
 [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#an-iterable-object-with-labels-can-be-passed-to-axes-plot "Link to this heading")\
\
When plotting multiple datasets by passing 2D data as _y_ value to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")\
, labels for the datasets can be passed as a list, the length matching the number of columns in _y_.\
\
x \= \[1, 2, 3\]\
\
y \= \[\[1, 2\],\
     \[2, 5\],\
     \[4, 9\]\]\
\
plt.plot(x, y, label\=\['low', 'high'\])\
plt.legend()\
\
([`Source code`](https://matplotlib.org/stable/_downloads/cc7d6736dc7685b9f864f327ec0a5333/whats_new_3-4-0-19.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/770c255f5bc2286fab6b97a4f6ca4920/whats_new_3-4-0-19.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/9ea18987ac668409b3e260f56f71c2c1/whats_new_3-4-0-19.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-19.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-19.2x.png)\
\
[Fonts and Text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id40)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#fonts-and-text "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Text transform can rotate text direction](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id41)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#text-transform-can-rotate-text-direction "Link to this heading")\
\
The new [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 parameter `transform_rotates_text` now sets whether rotations of the transform affect the text direction.\
\
[![../../_images/sphx_glr_text_rotation_relative_to_line_001.png](https://matplotlib.org/stable/_images/sphx_glr_text_rotation_relative_to_line_001.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_rotation_relative_to_line.html)\
\
Example of the new _transform\_rotates\_text_ parameter[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id2 "Link to this image")\
\
### [`matplotlib.mathtext` now supports _overset_ and _underset_ LaTeX symbols](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id42)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#matplotlib-mathtext-now-supports-overset-and-underset-latex-symbols "Link to this heading")\
\
[`mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")\
 now supports _overset_ and _underset_, called as `\overset{annotation}{body}` or `\underset{annotation}{body}`, where _annotation_ is the text "above" or "below" the _body_.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/5a91dc566a4b41ca7b50fa35a11a8786/whats_new_3-4-0-20.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/fae0b7dbe33e581722d9458560366d6b/whats_new_3-4-0-20.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/5a5befb511d51a455099cccca89584ac/whats_new_3-4-0-20.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-20.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-20.2x.png)\
\
### [_math\_fontfamily_ parameter to change `Text` font family](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id43)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#math-fontfamily-parameter-to-change-text-font-family "Link to this heading")\
\
The new _math\_fontfamily_ parameter may be used to change the family of fonts for each individual text element in a plot. If no parameter is set, the global value `[rcParams["mathtext.fontset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fontset#rcparam-mathtext-fontset) ` (default: `'dejavusans'`) will be used.\
\
[![../../_images/sphx_glr_mathtext_fontfamily_example_001.png](https://matplotlib.org/stable/_images/sphx_glr_mathtext_fontfamily_example_001.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/mathtext_fontfamily_example.html)\
\
### [`TextArea`/`AnchoredText` support _horizontalalignment_](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id44)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#textarea-anchoredtext-support-horizontalalignment "Link to this heading")\
\
The horizontal alignment of text in a [`TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")\
 or [`AnchoredText`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")\
 may now be specified, which is mostly effective for multiline text:\
\
([`Source code`](https://matplotlib.org/stable/_downloads/03d0d6adc7e8bb6091a6a210444dadbf/whats_new_3-4-0-21.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/70960e6e31fa0712692ca2a4e1914b96/whats_new_3-4-0-21.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/44dce9978f5e55aa0805869d22466a86/whats_new_3-4-0-21.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-21.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-21.2x.png)\
\
### [PDF supports URLs on `Text` artists](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id45)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#pdf-supports-urls-on-text-artists "Link to this heading")\
\
URLs on [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 artists (i.e., from [`Artist.set_url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url")\
) will now be saved in PDF files.\
\
[rcParams improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id46)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#rcparams-improvements "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [New rcParams for dates: set converter and whether to use interval\_multiples](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id47)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-rcparams-for-dates-set-converter-and-whether-to-use-interval-multiples "Link to this heading")\
\
The new `[rcParams["date.converter"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.converter#rcparam-date-converter) ` (default: `'auto'`) allows toggling between [`matplotlib.dates.DateConverter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter "matplotlib.dates.DateConverter")\
 and [`matplotlib.dates.ConciseDateConverter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateConverter "matplotlib.dates.ConciseDateConverter")\
 using the strings 'auto' and 'concise' respectively.\
\
The new `[rcParams["date.interval_multiples"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.interval_multiples#rcparam-date-interval-multiples) ` (default: `True`) allows toggling between the dates locator trying to pick ticks at set intervals (i.e., day 1 and 15 of the month), versus evenly spaced ticks that start wherever the timeseries starts:\
\
dates \= np.arange('2001-01-10', '2001-05-23', dtype\='datetime64\[D\]')\
y \= np.sin(dates.astype(float) / 10)\
fig, axs \= plt.subplots(nrows\=2, constrained\_layout\=True)\
\
plt.rcParams\['date.converter'\] \= 'concise'\
plt.rcParams\['date.interval\_multiples'\] \= True\
axs\[0\].plot(dates, y)\
\
plt.rcParams\['date.converter'\] \= 'auto'\
plt.rcParams\['date.interval\_multiples'\] \= False\
axs\[1\].plot(dates, y)\
\
([`Source code`](https://matplotlib.org/stable/_downloads/e2556d1658ef06bf21a4ffddd155e16a/whats_new_3-4-0-22.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/f588eb0501343d330bc93ce99994797a/whats_new_3-4-0-22.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/0990d1f4df3bc1dc24fa07d869968849/whats_new_3-4-0-22.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-22.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-22.2x.png)\
\
### [Date formatters now respect _usetex_ rcParam](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id48)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#date-formatters-now-respect-usetex-rcparam "Link to this heading")\
\
The [`AutoDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.AutoDateFormatter "matplotlib.dates.AutoDateFormatter")\
 and [`ConciseDateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.ConciseDateFormatter "matplotlib.dates.ConciseDateFormatter")\
 now respect `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`), and will thus use fonts consistent with TeX rendering of the default (non-date) formatter. TeX rendering may also be enabled/disabled by passing the _usetex_ parameter when creating the formatter instance.\
\
In the following plot, both the x-axis (dates) and y-axis (numbers) now use the same (TeX) font:\
\
([`Source code`](https://matplotlib.org/stable/_downloads/4c61456f4faacad80ecbf8476fda6898/whats_new_3-4-0-23.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/3aa566b38efda80cbeae38c11ae1cfe5/whats_new_3-4-0-23.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/8fe3303756ee492e627f295be2786d06/whats_new_3-4-0-23.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-23.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-23.2x.png)\
\
### [Setting _image.cmap_ to a `Colormap`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id49)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#setting-image-cmap-to-a-colormap "Link to this heading")\
\
It is now possible to set `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`) to a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")\
 instance, such as a colormap created with the new [`set_extremes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_extremes "matplotlib.colors.Colormap.set_extremes")\
 above. (This can only be done from Python code, not from the `matplotlibrc` file.)\
\
### [Tick and tick label colors can be set independently using rcParams](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id50)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#tick-and-tick-label-colors-can-be-set-independently-using-rcparams "Link to this heading")\
\
Previously, `[rcParams["xtick.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.color#rcparam-xtick-color) ` (default: `'black'`) defined both the tick color and the label color. The label color can now be set independently using `[rcParams["xtick.labelcolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.labelcolor#rcparam-xtick-labelcolor) ` (default: `'inherit'`). It defaults to `'inherit'` which will take the value from `[rcParams["xtick.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.color#rcparam-xtick-color) ` (default: `'black'`). The same holds for `ytick.[label]color`. For instance, to set the ticks to light grey and the tick labels to black, one can use the following code in a script:\
\
import matplotlib as mpl\
\
mpl.rcParams\['xtick.labelcolor'\] \= 'lightgrey'\
mpl.rcParams\['xtick.color'\] \= 'black'\
mpl.rcParams\['ytick.labelcolor'\] \= 'lightgrey'\
mpl.rcParams\['ytick.color'\] \= 'black'\
\
Or by adding the following lines to the [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)\
 file, or a Matplotlib style file:\
\
xtick.labelcolor : lightgrey\
xtick.color      : black\
ytick.labelcolor : lightgrey\
ytick.color      : black\
\
[3D Axes improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id51)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#d-axes-improvements "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Errorbar method in 3D Axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id52)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#errorbar-method-in-3d-axes "Link to this heading")\
\
The errorbar function [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")\
 is ported into the 3D Axes framework in its entirety, supporting features such as custom styling for error lines and cap marks, control over errorbar spacing, upper and lower limit marks.\
\
[![../../_images/sphx_glr_errorbar3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_errorbar3d_001.png)](https://matplotlib.org/stable/gallery/mplot3d/errorbar3d.html)\
\
### [Stem plots in 3D Axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id53)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#stem-plots-in-3d-axes "Link to this heading")\
\
Stem plots are now supported on 3D Axes. Much like 2D stems, [`stem`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html#mpl_toolkits.mplot3d.axes3d.Axes3D.stem "mpl_toolkits.mplot3d.axes3d.Axes3D.stem")\
 supports plotting the stems in various orientations:\
\
([`Source code`](https://matplotlib.org/stable/_downloads/4fd543baa74072c05c69767f6bf90952/whats_new_3-4-0-24.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/030a686372a59619125351e583b22eaf/whats_new_3-4-0-24.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/a46e151e0f0a2edd0788cf1214201a27/whats_new_3-4-0-24.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-24.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-24.2x.png)\
\
See also the [3D stem](https://matplotlib.org/stable/gallery/mplot3d/stem3d_demo.html)\
 demo.\
\
### [3D Collection properties are now modifiable](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id54)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#d-collection-properties-are-now-modifiable "Link to this heading")\
\
Previously, properties of a 3D Collection that were used for 3D effects (e.g., colors were modified to produce depth shading) could not be changed after it was created.\
\
Now it is possible to modify all properties of 3D Collections at any time.\
\
### [Panning in 3D Axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id55)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#panning-in-3d-axes "Link to this heading")\
\
Click and drag with the middle mouse button to pan 3D Axes.\
\
[Interactive tool improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id56)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#interactive-tool-improvements "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [New `RangeSlider` widget](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id57)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#new-rangeslider-widget "Link to this heading")\
\
[`widgets.RangeSlider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")\
 allows for creating a slider that defines a range rather than a single value.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/7f1572bb93aa94089ca4ef8d78c957f9/whats_new_3-4-0-25.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/7c5c8e8e5ba289229b145cd10e5301b5/whats_new_3-4-0-25.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/ceed91e10e4451a656e4886e8e321ab0/whats_new_3-4-0-25.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-25.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-4-0-25.2x.png)\
\
### [Sliders can now snap to arbitrary values](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id58)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#sliders-can-now-snap-to-arbitrary-values "Link to this heading")\
\
The [`Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")\
 UI widget now accepts arrays for _valstep_. This generalizes the previous behavior by allowing the slider to snap to arbitrary values.\
\
### [Pausing and Resuming Animations](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id59)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#pausing-and-resuming-animations "Link to this heading")\
\
The [`animation.Animation.pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.pause "matplotlib.animation.Animation.pause")\
 and [`animation.Animation.resume`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.resume "matplotlib.animation.Animation.resume")\
 methods allow you to pause and resume animations. These methods can be used as callbacks for event listeners on UI elements so that your plots can have some playback control UI.\
\
[Sphinx extensions](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id60)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#sphinx-extensions "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [`plot_directive` _caption_ option](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id61)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#plot-directive-caption-option "Link to this heading")\
\
Captions were previously supported when using the `plot_directive` directive with an external source file by specifying content:\
\
.. plot:: path/to/plot.py\
\
    This is the caption for the plot.\
\
The `:caption:` option allows specifying the caption for both external:\
\
.. plot:: path/to/plot.py\
    :caption: This is the caption for the plot.\
\
and inline plots:\
\
.. plot::\
    :caption: This is a caption for the plot.\
\
    plt.plot(\[1, 2, 3\])\
\
[Backend-specific improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id62)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#backend-specific-improvements "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Consecutive rasterized draws now merged](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id63)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#consecutive-rasterized-draws-now-merged "Link to this heading")\
\
Elements of a vector output can be individually set to rasterized, using the _rasterized_ keyword argument, or [`set_rasterized()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized")\
. This can be useful to reduce file sizes. For figures with multiple raster elements they are now automatically merged into a smaller number of bitmaps where this will not effect the visual output. For cases with many elements this can result in significantly smaller file sizes.\
\
To ensure this happens do not place vector elements between raster ones.\
\
To inhibit this merging set `Figure.suppressComposite` to True.\
\
### [Support raw/rgba frame format in `FFMpegFileWriter`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id64)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#support-raw-rgba-frame-format-in-ffmpegfilewriter "Link to this heading")\
\
When using [`FFMpegFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter "matplotlib.animation.FFMpegFileWriter")\
, the _frame\_format_ may now be set to `"raw"` or `"rgba"`, which may be slightly faster than an image format, as no encoding/decoding need take place between Matplotlib and FFmpeg.\
\
### [nbAgg/WebAgg support middle-click and double-click](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id65)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#nbagg-webagg-support-middle-click-and-double-click "Link to this heading")\
\
Double click events are now supported by the nbAgg and WebAgg backends. Formerly, WebAgg would report middle-click events as right clicks, but now reports the correct button type.\
\
### [nbAgg support binary communication](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id66)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#nbagg-support-binary-communication "Link to this heading")\
\
If the web browser and notebook support binary websockets, nbAgg will now use them for slightly improved transfer of figure display.\
\
### [Indexed color for PNG images in PDF files when possible](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id67)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#indexed-color-for-png-images-in-pdf-files-when-possible "Link to this heading")\
\
When PNG images have 256 colors or fewer, they are converted to indexed color before saving them in a PDF. This can result in a significant reduction in file size in some cases. This is particularly true for raster data that uses a colormap but no interpolation, such as Healpy mollview plots. Currently, this is only done for RGB images.\
\
### [Improved font subsettings in PDF/PS](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id68)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#improved-font-subsettings-in-pdf-ps "Link to this heading")\
\
Font subsetting in PDF and PostScript has been re-written from the embedded `ttconv` C code to Python. Some composite characters and outlines may have changed slightly. This fixes ttc subsetting in PDF, and adds support for subsetting of type 3 OTF fonts, resulting in smaller files (much smaller when using CJK fonts), and avoids running into issues with type 42 embedding and certain PDF readers such as Acrobat Reader.\
\
### [Kerning added to strings in PDFs](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id69)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#kerning-added-to-strings-in-pdfs "Link to this heading")\
\
As with text produced in the Agg backend (see [the previous what's new entry](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.2.0.html#whats-new-3-2-0-kerning)\
 for examples), PDFs now include kerning in text strings.\
\
### [Fully-fractional HiDPI in QtAgg](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id70)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#fully-fractional-hidpi-in-qtagg "Link to this heading")\
\
Fully-fractional HiDPI (that is, HiDPI ratios that are not whole integers) was added in Qt 5.14, and is now supported by the QtAgg backend when using this version of Qt or newer.\
\
### [wxAgg supports fullscreen toggle](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#id71)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.4.0.html#wxagg-supports-fullscreen-toggle "Link to this heading")\
\
The wxAgg backend supports toggling fullscreen using the f shortcut, or the manager function [`FigureManagerBase.full_screen_toggle`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureManagerBase.full_screen_toggle "matplotlib.backend_bases.FigureManagerBase.full_screen_toggle")\
.\
\
On this page