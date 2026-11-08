[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#main-content)

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
    

What's new in Matplotlib 3.0 (Sep 18, 2018)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#what-s-new-in-matplotlib-3-0-sep-18-2018 "Link to this heading")

========================================================================================================================================================================================

Improved default backend selection[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#improved-default-backend-selection "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default backend no longer must be set as part of the build process. Instead, at run time, the builtin backends are tried in sequence until one of them imports.

Headless Linux servers (identified by the DISPLAY environment variable not being defined) will not select a GUI backend.

Cyclic colormaps[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#cyclic-colormaps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Two new colormaps named 'twilight' and 'twilight\_shifted' have been added. These colormaps start and end on the same color, and have two symmetric halves with equal lightness, but diverging color. Since they wrap around, they are a good choice for cyclic data such as phase angles, compass directions, or time of day. Like _viridis_ and _cividis_, _twilight_ is perceptually uniform and colorblind friendly.

Ability to scale axis by a fixed order of magnitude[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#ability-to-scale-axis-by-a-fixed-order-of-magnitude "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To scale an axis by a fixed order of magnitude, set the _scilimits_ argument of [`Axes.ticklabel_format`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format")
 to the same (non-zero) lower and upper limits. Say to scale the y axis by a million (1e6), use

ax.ticklabel\_format(style\='sci', scilimits\=(6, 6), axis\='y')

The behavior of `scilimits=(0, 0)` is unchanged. With this setting, Matplotlib will adjust the order of magnitude depending on the axis values, rather than keeping it fixed. Previously, setting `scilimits=(m, m)` was equivalent to setting `scilimits=(0, 0)`.

Add `AnchoredDirectionArrows` feature to mpl\_toolkits[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#add-anchoreddirectionarrows-feature-to-mpl-toolkits "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A new mpl\_toolkits class [`AnchoredDirectionArrows`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDirectionArrows")
 draws a pair of orthogonal arrows to indicate directions on a 2D plot. A minimal working example takes in the transformation object for the coordinate system (typically ax.transAxes), and arrow labels. There are several optional parameters that can be used to alter layout. For example, the arrow pairs can be rotated and the color can be changed. By default the labels and arrows have the same color, but the class may also pass arguments for customizing arrow and text layout, these are passed to [`matplotlib.textpath.TextPath`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.TextPath "matplotlib.textpath.TextPath")
 and [`matplotlib.patches.FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
. Location, length and width for both arrow tail and head can be adjusted, the direction arrows and labels can have a frame. Padding and separation parameters can be adjusted.

Add `minorticks_on()/off()` methods for colorbar[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#add-minorticks-on-off-methods-for-colorbar "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A new method `ColorbarBase.minorticks_on` has been added to correctly display minor ticks on a colorbar. This method doesn't allow the minor ticks to extend into the regions beyond vmin and vmax when the _extend_ keyword argument (used while creating the colorbar) is set to 'both', 'max' or 'min'. A complementary method `ColorbarBase.minorticks_off` has also been added to remove the minor ticks on the colorbar.

Colorbar ticks can now be automatic[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#colorbar-ticks-can-now-be-automatic "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The number of ticks placed on colorbars was previously appropriate for a large colorbar, but looked bad if the colorbar was made smaller (i.e. via the _shrink_ keyword argument). This has been changed so that the number of ticks is now responsive to how large the colorbar is.

Don't automatically rename duplicate file names[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#don-t-automatically-rename-duplicate-file-names "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously, when saving a figure to a file using the GUI's save dialog box, if the default filename (based on the figure window title) already existed on disk, Matplotlib would append a suffix (e.g. `Figure_1-1.png`), preventing the dialog from prompting to overwrite the file. This behaviour has been removed. Now if the file name exists on disk, the user is prompted whether or not to overwrite it. This eliminates guesswork, and allows intentional overwriting, especially when the figure name has been manually set using `figure.canvas.set_window_title()`.

Legend now has a _title\_fontsize_ keyword argument (and rcParam)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#legend-now-has-a-title-fontsize-keyword-argument-and-rcparam "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The title for a [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 and [`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 can now have its font size set via the _title\_fontsize_ keyword argument. There is also a new `[rcParams["legend.title_fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.title_fontsize#rcparam-legend-title-fontsize) ` (default: `None`). Both default to `None`, which means the legend title will have the same font size as the axes default font size (_not_ the legend font size, set by the _fontsize_ keyword argument or `[rcParams["legend.fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.fontsize#rcparam-legend-fontsize) ` (default: `'medium'`)).

Support for axes.prop\_cycle property _markevery_ in rcParams[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#support-for-axes-prop-cycle-property-markevery-in-rcparams "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Matplotlib `rcParams` settings object now supports configuration of the attribute `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`) with cyclers using the _markevery_ Line2D object property.

Multi-page PDF support for pgf backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#multi-page-pdf-support-for-pgf-backend "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The pgf backend now also supports multi-page PDF files.

from matplotlib.backends.backend\_pgf import PdfPages
import matplotlib.pyplot as plt

with PdfPages('multipage.pdf') as pdf:
    \# page 1
    plt.plot(\[2, 1, 3\])
    pdf.savefig()

    \# page 2
    plt.cla()
    plt.plot(\[3, 1, 2\])
    pdf.savefig()

Pie charts are now circular by default[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#pie-charts-are-now-circular-by-default "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We acknowledge that the majority of people do not like egg-shaped pies. Therefore, an axes to which a pie chart is plotted will be set to have equal aspect ratio by default. This ensures that the pie appears circular independent on the axes size or units. To revert to the previous behaviour set the axes' aspect ratio to automatic by using `ax.set_aspect("auto")` or `plt.axis("auto")`.

Add `ax.get_gridspec` to `SubplotBase`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#add-ax-get-gridspec-to-subplotbase "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

New method `SubplotBase.get_gridspec` is added so that users can easily get the gridspec that went into making an axes:

import matplotlib.pyplot as plt

fig, axs \= plt.subplots(3, 2)
gs \= axs\[0, \-1\].get\_gridspec()

\# remove the last column
for ax in axs\[:,\-1\].flatten():
  ax.remove()

\# make a subplot in last column that spans rows.
ax \= fig.add\_subplot(gs\[:, \-1\])
plt.show()

Axes titles will no longer overlap xaxis[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#axes-titles-will-no-longer-overlap-xaxis "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously an axes title had to be moved manually if an xaxis overlapped (usually when the xaxis was put on the top of the axes). Now, the title will be automatically moved above the xaxis and its decorators (including the xlabel) if they are at the top.

If desired, the title can still be placed manually. There is a slight kludge; the algorithm checks if the y-position of the title is 1.0 (the default), and moves if it is. If the user places the title in the default location (i.e. `ax.title.set_position(0.5, 1.0)`), the title will still be moved above the xaxis. If the user wants to avoid this, they can specify a number that is close (i.e. `ax.title.set_position(0.5, 1.01)`) and the title will not be moved via this algorithm.

New convenience methods for GridSpec[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#new-convenience-methods-for-gridspec "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are new convenience methods for [`gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 and [`gridspec.GridSpecFromSubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "matplotlib.gridspec.GridSpecFromSubplotSpec")
. Instead of the former we can now call [`Figure.add_gridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
 and for the latter [`SubplotSpec.subgridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec.subgridspec "matplotlib.gridspec.SubplotSpec.subgridspec")
.

import matplotlib.pyplot as plt

fig \= plt.figure()
gs0 \= fig.add\_gridspec(3, 1)
ax1 \= fig.add\_subplot(gs0\[0\])
ax2 \= fig.add\_subplot(gs0\[1\])
gssub \= gs0\[2\].subgridspec(1, 3)
for i in range(3):
    fig.add\_subplot(gssub\[0, i\])

Figure has an [`add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
 method[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#figure-has-an-add-artist-method "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A method [`add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")
 has been added to the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class, which allows artists to be added directly to a figure. E.g.

circ \= plt.Circle((.7, .5), .05)
fig.add\_artist(circ)

In case the added artist has no transform set previously, it will be set to the figure transform (`fig.transFigure`). This new method may be useful for adding artists to figures without axes or to easily position static elements in figure coordinates.

`:math:` directive renamed to `:mathmpl:`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.0.html#math-directive-renamed-to-mathmpl "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `:math:` rst role provided by [`matplotlib.sphinxext.mathmpl`](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#module-matplotlib.sphinxext.mathmpl "matplotlib.sphinxext.mathmpl")
 has been renamed to `:mathmpl:` to avoid conflicting with the `:math:` role that Sphinx 1.8 provides by default. (`:mathmpl:` uses Matplotlib to render math expressions to images embedded in html, whereas Sphinx uses MathJax.)

When using Sphinx<1.8, both names (`:math:` and `:mathmpl:`) remain available for backwards-compatibility.

On this page