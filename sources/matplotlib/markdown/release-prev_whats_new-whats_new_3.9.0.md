[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#main-content)

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
    

[What's new in Matplotlib 3.9.0 (May 15, 2024)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#what-s-new-in-matplotlib-3-9-0-may-15-2024 "Link to this heading")

================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.9.0 (May 15, 2024)](https://matplotlib.org/stable/release/prev_whats_new/github_stats_3.9.0.html#github-stats-3-9-0)
.

[Plotting and Annotation improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#plotting-and-annotation-improvements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`Axes.inset_axes` is no longer experimental](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#axes-inset-axes-is-no-longer-experimental "Link to this heading")

[`Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 is considered stable for use.

### [Legend support for Boxplot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#legend-support-for-boxplot "Link to this heading")

Boxplots now support a _label_ parameter to create legend entries. Legend labels can be passed as a list of strings to label multiple boxes in a single [`Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 call:

np.random.seed(19680801)
fruit\_weights \= \[\
    np.random.normal(130, 10, size\=100),\
    np.random.normal(125, 20, size\=100),\
    np.random.normal(120, 30, size\=100),\
\]
labels \= \['peaches', 'oranges', 'tomatoes'\]
colors \= \['peachpuff', 'orange', 'tomato'\]

fig, ax \= plt.subplots()
ax.set\_ylabel('fruit weight (g)')

bplot \= ax.boxplot(fruit\_weights,
                   patch\_artist\=True,  \# fill with color
                   label\=labels)

\# fill with colors
for patch, color in zip(bplot\['boxes'\], colors):
    patch.set\_facecolor(color)

ax.set\_xticks(\[\])
ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/d61aae4cd75184ba2f55a0e5676da548/whats_new_3-9-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/67b0cf8585f02fe445591044475505e8/whats_new_3-9-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7c4e0a53b89affd107b1cb01a83786e0/whats_new_3-9-0-1.png)
)

[![Example of creating 3 boxplots and assigning legend labels as a sequence.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-1.2x.png)

Or as a single string to each individual [`Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
:

fig, ax \= plt.subplots()

data\_A \= np.random.random((100, 3))
data\_B \= np.random.random((100, 3)) + 0.2
pos \= np.arange(3)

ax.boxplot(data\_A, positions\=pos \- 0.2, patch\_artist\=True, label\='Box A',
           boxprops\={'facecolor': 'steelblue'})
ax.boxplot(data\_B, positions\=pos + 0.2, patch\_artist\=True, label\='Box B',
           boxprops\={'facecolor': 'lightblue'})

ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/bf7e28f23d1467dfca72675d30ec5394/whats_new_3-9-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/5d16cd9c6396b0bd7ce7d74613f61e99/whats_new_3-9-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7844f4fe968e64262c91cf915e0b2505/whats_new_3-9-0-2.png)
)

[![Example of creating 2 boxplots and assigning each legend label as a string.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-2.2x.png)

### [Percent sign in pie labels auto-escaped with `usetex=True`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#percent-sign-in-pie-labels-auto-escaped-with-usetex-true "Link to this heading")

It is common, with [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
, to specify labels that include a percent sign (`%`), which denotes a comment for LaTeX. When enabling LaTeX with `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) or passing `textprops={"usetex": True}`, this used to cause the percent sign to disappear.

Now, the percent sign is automatically escaped (by adding a preceding backslash) so that it appears regardless of the `usetex` setting. If you have pre-escaped the percent sign, this will be detected, and remain as is.

### [`hatch` parameter for stackplot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#hatch-parameter-for-stackplot "Link to this heading")

The [`stackplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
 _hatch_ parameter now accepts a list of strings describing hatching styles that will be applied sequentially to the layers in the stack:

fig, (ax1, ax2) \= plt.subplots(ncols\=2, figsize\=(10,5))

cols \= 10
rows \= 4
data \= (
np.reshape(np.arange(0, cols, 1), (1, \-1)) \*\* 2
+ np.reshape(np.arange(0, rows), (\-1, 1))
+ np.random.random((rows, cols))\*5
)
x \= range(data.shape\[1\])
ax1.stackplot(x, data, hatch\="x")
ax2.stackplot(x, data, hatch\=\["//","\\\\","x","o"\])

ax1.set\_title("hatch='x'")
ax2.set\_title("hatch=\['//','\\\\\\\\','x','o'\]")

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/0fde302d8a0289399c0d0b070fdf4aa3/whats_new_3-9-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/92095c7d445c48859dc805cd426c1fdb/whats_new_3-9-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/2e98a2beb68e362bcf0853ce515dcfc5/whats_new_3-9-0-3.png)
)

[![Two charts, identified as ax1 and ax2, showing "stackplots", i.e. one-dimensional distributions of data stacked on top of one another. The first plot, ax1 has cross-hatching on all slices, having been given a single string as the "hatch" argument. The second plot, ax2 has different styles of hatching on each slice - diagonal hatching in opposite directions on the first two slices, cross-hatching on the third slice, and open circles on the fourth.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-3.2x.png)

### [Add option to plot only one half of violin plot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#add-option-to-plot-only-one-half-of-violin-plot "Link to this heading")

Setting the parameter _side_ to 'low' or 'high' allows to only plot one half of the [`Axes.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
.

\# Fake data with reproducible random state.
np.random.seed(19680801)
data \= np.random.normal(0, 8, size\=100)

fig, ax \= plt.subplots()

ax.violinplot(data, \[0\], showmeans\=True, showextrema\=True)
ax.violinplot(data, \[1\], showmeans\=True, showextrema\=True, side\='low')
ax.violinplot(data, \[2\], showmeans\=True, showextrema\=True, side\='high')

ax.set\_title('Violin Sides Example')
ax.set\_xticks(\[0, 1, 2\], \['Default', 'side="low"', 'side="high"'\])
ax.set\_yticklabels(\[\])

([`Source code`](https://matplotlib.org/stable/_downloads/e9421baf199fd6f7a09f67bfb4958abf/whats_new_3-9-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/fd96d60d87ed0ea40e05341870ec30c9/whats_new_3-9-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/53cfb082eddbed25e95f4e12f7d023e0/whats_new_3-9-0-4.png)
)

[![Three copies of a vertical violin plot; first in blue showing the default of both sides, followed by an orange copy that only shows the "low" (or left, in this case) side, and finally a green copy that only shows the "high" (or right) side.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-4.2x.png)

### [`axhline` and `axhspan` on polar axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#axhline-and-axhspan-on-polar-axes "Link to this heading")

... now draw circles and circular arcs ([`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
) or annuli and wedges ([`axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
).

fig \= plt.figure()
ax \= fig.add\_subplot(projection\="polar")
ax.set\_rlim(0, 1.2)

ax.axhline(1, c\="C0", alpha\=.5)
ax.axhspan(.8, .9, fc\="C1", alpha\=.5)
ax.axhspan(.6, .7, .8, .9, fc\="C2", alpha\=.5)

([`Source code`](https://matplotlib.org/stable/_downloads/41ebe1e215ffed863629b9d4a3647956/whats_new_3-9-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c5841e7ea8bf478d3d9db739de717dde/whats_new_3-9-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/2ddfdce9eeca3a0b685d0095f96c2467/whats_new_3-9-0-5.png)
)

[![A sample polar plot, that contains an axhline at radius 1, an axhspan annulus between radius 0.8 and 0.9, and an axhspan wedge between radius 0.6 and 0.7 and 288° and 324°.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-5.2x.png)

### [Subplot titles can now be automatically aligned](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#subplot-titles-can-now-be-automatically-aligned "Link to this heading")

Subplot axes titles can be misaligned vertically if tick labels or xlabels are placed at the top of one subplot. The new [`align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")
 method on the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class will now align the titles vertically.

fig, axs \= plt.subplots(1, 2, layout\='constrained')

axs\[0\].plot(np.arange(0, 1e6, 1000))
axs\[0\].set\_title('Title 0')
axs\[0\].set\_xlabel('XLabel 0')

axs\[1\].plot(np.arange(1, 0, \-0.1) \* 2000, np.arange(1, 0, \-0.1))
axs\[1\].set\_title('Title 1')
axs\[1\].set\_xlabel('XLabel 1')
axs\[1\].xaxis.tick\_top()
axs\[1\].tick\_params(axis\='x', rotation\=55)

([`Source code`](https://matplotlib.org/stable/_downloads/f59bc8849d8744a5304651aff7d69e35/whats_new_3-9-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/12d3801ffc8a5c16fae5c1fc1f30f635/whats_new_3-9-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7566f27d9f6277bc2c1806e00bb40f7a/whats_new_3-9-0-6.png)
)

[![A figure with two Axes side-by-side, the second of which with ticks on top. The Axes titles and x-labels appear unaligned with each other due to these ticks.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-6.2x.png)

fig, axs \= plt.subplots(1, 2, layout\='constrained')

axs\[0\].plot(np.arange(0, 1e6, 1000))
axs\[0\].set\_title('Title 0')
axs\[0\].set\_xlabel('XLabel 0')

axs\[1\].plot(np.arange(1, 0, \-0.1) \* 2000, np.arange(1, 0, \-0.1))
axs\[1\].set\_title('Title 1')
axs\[1\].set\_xlabel('XLabel 1')
axs\[1\].xaxis.tick\_top()
axs\[1\].tick\_params(axis\='x', rotation\=55)

fig.align\_labels()
fig.align\_titles()

([`Source code`](https://matplotlib.org/stable/_downloads/71df738a67f85f175e88b7ba6b5d0bde/whats_new_3-9-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/4b618f156c58576b7a940058a35bde70/whats_new_3-9-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/9e6ed51feab825b310c2a83b29f88df5/whats_new_3-9-0-7.png)
)

[![A figure with two Axes side-by-side, the second of which with ticks on top. Unlike the previous figure, the Axes titles and x-labels appear aligned.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-7.2x.png)

### [`axisartist` can now be used together with standard `Formatters`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#axisartist-can-now-be-used-together-with-standard-formatters "Link to this heading")

... instead of being limited to axisartist-specific ones.

### [Toggle minorticks on Axis](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#toggle-minorticks-on-axis "Link to this heading")

Minor ticks on an [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 can be displayed or removed using [`minorticks_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#matplotlib.axis.Axis.minorticks_on "matplotlib.axis.Axis.minorticks_on")
 and [`minorticks_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_off.html#matplotlib.axis.Axis.minorticks_off "matplotlib.axis.Axis.minorticks_off")
; e.g., `ax.xaxis.minorticks_on()`. See also [`minorticks_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_on.html#matplotlib.axes.Axes.minorticks_on "matplotlib.axes.Axes.minorticks_on")
.

### [`StrMethodFormatter` now respects `axes.unicode_minus`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#strmethodformatter-now-respects-axes-unicode-minus "Link to this heading")

When formatting negative values, [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 will now use unicode minus signs if `[rcParams["axes.unicode_minus"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.unicode_minus#rcparam-axes-unicode-minus) ` (default: `True`) is set.

\>>> from matplotlib.ticker import StrMethodFormatter
\>>> with plt.rc\_context({'axes.unicode\_minus': False}):
...     formatter \= StrMethodFormatter('{x}')
...     print(formatter.format\_data(\-10))
\-10

\>>> with plt.rc\_context({'axes.unicode\_minus': True}):
...     formatter \= StrMethodFormatter('{x}')
...     print(formatter.format\_data(\-10))
−10

[Figure, Axes, and Legend Layout](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#figure-axes-and-legend-layout "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Subfigures now have controllable zorders](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#subfigures-now-have-controllable-zorders "Link to this heading")

Previously, setting the zorder of a subfigure had no effect, and those were plotted on top of any figure-level artists (i.e for example on top of fig-level legends). Now, subfigures behave like any other artists, and their zorder can be controlled, with default a zorder of 0.

x \= np.linspace(1, 10, 10)
y1, y2 \= x, \-x
fig \= plt.figure(constrained\_layout\=True)
subfigs \= fig.subfigures(nrows\=1, ncols\=2)
for subfig in subfigs:
    axarr \= subfig.subplots(2, 1)
    for ax in axarr.flatten():
        (l1,) \= ax.plot(x, y1, label\="line1")
        (l2,) \= ax.plot(x, y2, label\="line2")
subfigs\[0\].set\_zorder(6)
l \= fig.legend(handles\=\[l1, l2\], loc\="upper center", ncol\=2)

([`Source code`](https://matplotlib.org/stable/_downloads/b0393128f2b28a0b602644d89f409ba8/whats_new_3-9-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f057445c4ccd3feeff92b5357b02dc92/whats_new_3-9-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3d7743c34c37f102ebbec7ec9522c6a9/whats_new_3-9-0-8.png)
)

[![Example on controlling the zorder of a subfigure](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-8.2x.png)

### [Getters for xmargin, ymargin and zmargin](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#getters-for-xmargin-ymargin-and-zmargin "Link to this heading")

[`Axes.get_xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xmargin.html#matplotlib.axes.Axes.get_xmargin "matplotlib.axes.Axes.get_xmargin")
, [`Axes.get_ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymargin.html#matplotlib.axes.Axes.get_ymargin "matplotlib.axes.Axes.get_ymargin")
 and [`Axes3D.get_zmargin`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmargin.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmargin "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zmargin")
 methods have been added to return the margin values set by [`Axes.set_xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin")
, [`Axes.set_ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin")
 and [`Axes3D.set_zmargin`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin")
, respectively.

[Mathtext improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#mathtext-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`mathtext` documentation improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#mathtext-documentation-improvements "Link to this heading")

The documentation is updated to take information directly from the parser. This means that (almost) all supported symbols, operators, etc. are shown at [Writing mathematical expressions](https://matplotlib.org/stable/users/explain/text/mathtext.html#mathtext)
.

### [`mathtext` spacing corrections](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#mathtext-spacing-corrections "Link to this heading")

As consequence of the updated documentation, the spacing on a number of relational and operator symbols were correctly classified and therefore will be spaced properly.

[Widget Improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#widget-improvements "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Check and Radio Button widgets support clearing](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#check-and-radio-button-widgets-support-clearing "Link to this heading")

The [`CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
 and [`RadioButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RadioButtons.html#matplotlib.widgets.RadioButtons "matplotlib.widgets.RadioButtons")
 widgets now support clearing their state by calling their `.clear` method. Note that it is not possible to have no selected radio buttons, so the selected option at construction time is selected.

[3D plotting improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#d-plotting-improvements "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Setting 3D axis limits now set the limits exactly](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#setting-3d-axis-limits-now-set-the-limits-exactly "Link to this heading")

Previously, setting the limits of a 3D axis would always add a small margin to the limits. Limits are now set exactly by default. The newly introduced rcparam `axes3d.automargin` can be used to revert to the old behavior where margin is automatically added.

fig, axs \= plt.subplots(1, 2, subplot\_kw\={'projection': '3d'})

plt.rcParams\['axes3d.automargin'\] \= True
axs\[0\].set(xlim\=(0, 1), ylim\=(0, 1), zlim\=(0, 1), title\='Old Behavior')

plt.rcParams\['axes3d.automargin'\] \= False  \# the default in 3.9.0
axs\[1\].set(xlim\=(0, 1), ylim\=(0, 1), zlim\=(0, 1), title\='New Behavior')

([`Source code`](https://matplotlib.org/stable/_downloads/45ed6bf250574b6acdab99ddeaca7004/whats_new_3-9-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/db8490db259287d106d450730e290630/whats_new_3-9-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/44018b18edb187a9b91ac668ab04c681/whats_new_3-9-0-9.png)
)

[![Example of the new behavior of 3D axis limits, and how setting the rcParam reverts to the old behavior.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-9.2x.png)

[Other improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#other-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [BackendRegistry](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#backendregistry "Link to this heading")

New [`BackendRegistry`](https://matplotlib.org/stable/api/backend_registry_api.html#matplotlib.backends.registry.BackendRegistry "matplotlib.backends.registry.BackendRegistry")
 class is the single source of truth for available backends. The singleton instance is `matplotlib.backends.backend_registry`. It is used internally by Matplotlib, and also IPython (and therefore Jupyter) starting with IPython 8.24.0.

There are three sources of backends: built-in (source code is within the Matplotlib repository), explicit `module://some.backend` syntax (backend is obtained by loading the module), or via an entry point (self-registering backend in an external package).

To obtain a list of all registered backends use:

\>>> from matplotlib.backends import backend\_registry
\>>> backend\_registry.list\_all()

### [Add `widths`, `heights` and `angles` setter to `EllipseCollection`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#add-widths-heights-and-angles-setter-to-ellipsecollection "Link to this heading")

The `widths`, `heights` and `angles` values of the [`EllipseCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
 can now be changed after the collection has been created.

from matplotlib.collections import EllipseCollection

rng \= np.random.default\_rng(0)

widths \= (2, )
heights \= (3, )
angles \= (45, )
offsets \= rng.random((10, 2)) \* 10

fig, ax \= plt.subplots()

ec \= EllipseCollection(
    widths\=widths,
    heights\=heights,
    angles\=angles,
    offsets\=offsets,
    units\='x',
    offset\_transform\=ax.transData,
    )

ax.add\_collection(ec)
ax.set\_xlim(\-2, 12)
ax.set\_ylim(\-2, 12)

new\_widths \= rng.random((10, 2)) \* 2
new\_heights \= rng.random((10, 2)) \* 3
new\_angles \= rng.random((10, 2)) \* 180

ec.set(widths\=new\_widths, heights\=new\_heights, angles\=new\_angles)

([`Source code`](https://matplotlib.org/stable/_downloads/f66d62891f28a48bf43925b2a52453bb/whats_new_3-9-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/10521f7cbd2cb73b8d05b2f9fb7cdb01/whats_new_3-9-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/17df022b49aea8606ca778d5cf62abae/whats_new_3-9-0-10.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-10.2x.png)

### [`image.interpolation_stage` rcParam](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#image-interpolation-stage-rcparam "Link to this heading")

This new rcParam controls whether image interpolation occurs in "data" space or in "rgba" space.

### [Arrow patch position is now modifiable](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#arrow-patch-position-is-now-modifiable "Link to this heading")

A setter method has been added that allows updating the position of the [`patches.Arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")
 object without requiring a full re-draw.

from matplotlib import animation
from matplotlib.patches import Arrow

fig, ax \= plt.subplots()
ax.set\_xlim(0, 10)
ax.set\_ylim(0, 10)

a \= Arrow(2, 0, 0, 10)
ax.add\_patch(a)

\# code for modifying the arrow
def update(i):
    a.set\_data(x\=.5, dx\=i, dy\=6, width\=2)

ani \= animation.FuncAnimation(fig, update, frames\=15, interval\=90, blit\=False)

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/01a283d9e4c21901612bdec6d5ed3ba7/whats_new_3-9-0-11.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/964a1ebc89d1de2f003a8e9d7bca044f/whats_new_3-9-0-11.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/19de4770b81c213060e19adbf5efb10b/whats_new_3-9-0-11.png)
)

[![Example of changing the position of the arrow with the new ``set_data`` method.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-9-0-11.2x.png)

### [NonUniformImage now has mouseover support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.9.0.html#nonuniformimage-now-has-mouseover-support "Link to this heading")

When mousing over a [`NonUniformImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
, the data values are now displayed.

On this page