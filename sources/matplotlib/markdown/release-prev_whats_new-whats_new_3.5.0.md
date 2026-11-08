[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#main-content)

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
    

[What's new in Matplotlib 3.5.0 (Nov 15, 2021)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#what-s-new-in-matplotlib-3-5-0-nov-15-2021 "Link to this heading")

================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Figure and Axes creation / management](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#figure-and-axes-creation-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`subplot_mosaic` supports simple Axes sharing](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#subplot-mosaic-supports-simple-axes-sharing "Link to this heading")

[`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
, [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 support _simple_ Axes sharing (i.e., only [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
/[`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
 may be passed to _sharex_/_sharey_). When [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, tick label visibility and Axis units will be shared.

mosaic \= \[\
    \['A', \[\['B', 'C'\],\
           \['D', 'E'\]\]\],\
    \['F', 'G'\],\
\]
fig \= plt.figure(constrained\_layout\=True)
ax\_dict \= fig.subplot\_mosaic(mosaic, sharex\=True, sharey\=True)
\# All Axes use these scales after this call.
ax\_dict\['A'\].set(xscale\='log', yscale\='logit')

([`Source code`](https://matplotlib.org/stable/_downloads/2a87a4c991683f76162dfad38149e0ce/whats_new_3-5-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d1793ad06a9a93b0fd86c49f285c2eb6/whats_new_3-5-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c068a56fefb52a4d32f4c5f1a26f6443/whats_new_3-5-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-1.2x.png)

### [Figure now has `draw_without_rendering` method](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#figure-now-has-draw-without-rendering-method "Link to this heading")

Some aspects of a figure are only determined at draw-time, such as the exact position of text artists or deferred computation like automatic data limits. If you need these values, you can use `figure.canvas.draw()` to force a full draw. However, this has side effects, sometimes requires an open file, and is doing more work than is needed.

The new [`Figure.draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
 method runs all the updates that `draw()` does, but skips rendering the figure. It's thus more efficient if you need the updated values to configure further aspects of the figure.

### [Figure `__init__` passes keyword arguments through to set](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#figure-init-passes-keyword-arguments-through-to-set "Link to this heading")

Similar to many other sub-classes of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, the [`FigureBase`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "matplotlib.figure.FigureBase")
, [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, and [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 classes will now pass any additional keyword arguments to [`set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
 to allow properties of the newly created object to be set at initialization time. For example:

from matplotlib.figure import Figure
fig \= Figure(label\='my figure')

[Plotting methods](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#plotting-methods "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Add `Annulus` patch](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#add-annulus-patch "Link to this heading")

[`Annulus`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")
 is a new class for drawing elliptical annuli.

([`Source code`](https://matplotlib.org/stable/_downloads/7c29aa6fd50fa3865a0f734279e11f84/whats_new_3-5-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/7a222b39e588b8642c0bf2e398e9cb36/whats_new_3-5-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ebc7580852638a195a595e78329e7278/whats_new_3-5-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-2.2x.png)

### [`set_data` method for `FancyArrow` patch](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#set-data-method-for-fancyarrow-patch "Link to this heading")

[`FancyArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrow.html#matplotlib.patches.FancyArrow "matplotlib.patches.FancyArrow")
, the patch returned by `ax.arrow`, now has a `set_data` method that allows modifying the arrow after creation, e.g., for animation.

### [New arrow styles in `ArrowStyle` and `ConnectionPatch`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#new-arrow-styles-in-arrowstyle-and-connectionpatch "Link to this heading")

The new _arrow_ parameter to [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
 substitutes the use of the _beginarrow_ and _endarrow_ parameters in the creation of arrows. It receives arrows strings like `'<-'`, `']-[`' and `']->`' instead of individual booleans.

Two new styles `']->'` and `'<-['` are also added via this mechanism. [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
, which accepts arrow styles though its _arrowstyle_ parameter, also accepts these new styles.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/980ffd19db7dba65d48f753946645770/whats_new_3-5-0-3.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/3c40e60fa558cf8fcb64192d0bfe4b0d/whats_new_3-5-0-3.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/7f7256bc36fbe2aacb55a9b7afe36abc/whats_new_3-5-0-3.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-3.2x.png)\
\
### [Setting collection offset transform after initialization](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id11)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#setting-collection-offset-transform-after-initialization "Link to this heading")\
\
The added [`collections.Collection.set_offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")\
 may be used to set the offset transform after initialization. This can be helpful when creating a [`collections.Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")\
 outside an Axes object, and later adding it with [`Axes.add_collection()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")\
 and setting the offset transform to `Axes.transData`.\
\
[Colors and colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id12)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#colors-and-colormaps "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Colormap registry (experimental)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id13)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#colormap-registry-experimental "Link to this heading")\
\
Colormaps are now managed via [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")\
 (or [`pyplot.colormaps`](https://matplotlib.org/stable/api/pyplot_summary.html#matplotlib.pyplot.colormaps "matplotlib.pyplot.colormaps")\
), which is a [`ColormapRegistry`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")\
. While we are confident that the API is final, we formally mark it as experimental for 3.5 because we want to keep the option to still modify the API for 3.6 should the need arise.\
\
Colormaps can be obtained using item access:\
\
import matplotlib.pyplot as plt\
cmap \= plt.colormaps\['viridis'\]\
\
To register new colormaps use:\
\
plt.colormaps.register(my\_colormap)\
\
We recommend to use the new API instead of the `matplotlib.cm.get_cmap` and `matplotlib.cm.register_cmap` functions for new code. `matplotlib.cm.get_cmap` and `matplotlib.cm.register_cmap` will eventually be deprecated and removed. Within [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")\
, `plt.get_cmap()` and `plt.register_cmap()` will continue to be supported for backward compatibility.\
\
### [Image interpolation now possible at RGBA stage](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id14)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#image-interpolation-now-possible-at-rgba-stage "Link to this heading")\
\
Images in Matplotlib created via [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")\
 are resampled to match the resolution of the current canvas. It is useful to apply an auto-aliasing filter when downsampling to reduce Moiré effects. By default, interpolation is done on the data, a norm applied, and then the colormapping performed.\
\
However, it is often desirable for the anti-aliasing interpolation to happen in RGBA space, where the colors are interpolated rather than the data. This usually leads to colors outside the colormap, but visually blends adjacent colors, and is what browsers and other image processing software do.\
\
A new keyword argument _interpolation\_stage_ is provided for [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")\
 to set the stage at which the anti-aliasing interpolation happens. The default is the current behaviour of "data", with the alternative being "rgba" for the newly-available behavior.\
\
[![../../_images/sphx_glr_image_antialiasing_001.png](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)\
\
Example of the interpolation stage options.[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id1 "Link to this image")\
\
For more details see the discussion of the new keyword argument in [Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)\
.\
\
### [`imshow` supports half-float arrays](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id15)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#imshow-supports-half-float-arrays "Link to this heading")\
\
The [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")\
 method now supports half-float arrays, i.e., NumPy arrays with dtype `np.float16`.\
\
### [A callback registry has been added to Normalize objects](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id16)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#a-callback-registry-has-been-added-to-normalize-objects "Link to this heading")\
\
[`colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")\
 objects now have a callback registry, `callbacks`, that can be connected to by other objects to be notified when the norm is updated. The callback emits the key `changed` when the norm is modified. [`cm.ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")\
 is now a listener and will register a change when the norm's vmin, vmax or other attributes are changed.\
\
[Titles, ticks, and labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id17)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#titles-ticks-and-labels "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Settings tick positions and labels simultaneously in `set_ticks`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id18)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#settings-tick-positions-and-labels-simultaneously-in-set-ticks "Link to this heading")\
\
[`Axis.set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")\
 (and the corresponding [`Axes.set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")\
 / [`Axes.set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")\
) has a new parameter _labels_ allowing to set tick positions and labels simultaneously.\
\
Previously, setting tick labels was done using [`Axis.set_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels")\
 (or the corresponding [`Axes.set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")\
 / [`Axes.set_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")\
); this usually only makes sense if tick positions were previously fixed with [`set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")\
:\
\
ax.set\_xticks(\[1, 2, 3\])\
ax.set\_xticklabels(\['a', 'b', 'c'\])\
\
The combined functionality is now available in [`set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")\
:\
\
ax.set\_xticks(\[1, 2, 3\], \['a', 'b', 'c'\])\
\
The use of [`Axis.set_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "matplotlib.axis.Axis.set_ticklabels")\
 is discouraged, but it will stay available for backward compatibility.\
\
Note: This addition makes the API of [`set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")\
 also more similar to [`pyplot.xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")\
 / [`pyplot.yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")\
, which already had the additional _labels_ parameter.\
\
[Fonts and Text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id19)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#fonts-and-text "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Triple and quadruple dot mathtext accents](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id20)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#triple-and-quadruple-dot-mathtext-accents "Link to this heading")\
\
In addition to single and double dot accents, mathtext now supports triple and quadruple dot accents.\
\
fig \= plt.figure(figsize\=(3, 1))\
fig.text(0.5, 0.5, r'$\\dot{a} \\ddot{b} \\dddot{c} \\ddddot{d}$', fontsize\=40,\
         horizontalalignment\='center', verticalalignment\='center')\
\
([`Source code`](https://matplotlib.org/stable/_downloads/882dbd89d1fc1873854da5a1922854fd/whats_new_3-5-0-4.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/e8b842ce9b3f3158e6da967aba327ffa/whats_new_3-5-0-4.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/ec2c2f3dd4d9fca12beb258b9608709b/whats_new_3-5-0-4.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-4.2x.png)\
\
### [Font properties of legend title are configurable](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id21)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#font-properties-of-legend-title-are-configurable "Link to this heading")\
\
Title's font properties can be set via the _title\_fontproperties_ keyword argument, for example:\
\
([`Source code`](https://matplotlib.org/stable/_downloads/5d90f10693fb4989476a5915a4ce6b16/whats_new_3-5-0-5.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/73fec65180674671566f631472ffd1c8/whats_new_3-5-0-5.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/b69866117f3c686d703c86b89a9ac51e/whats_new_3-5-0-5.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-5.2x.png)\
\
### [`Text` and `TextBox` added _parse\_math_ option](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id22)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#text-and-textbox-added-parse-math-option "Link to this heading")\
\
[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 and [`TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")\
 objects now allow a _parse\_math_ keyword-only argument which controls whether math should be parsed from the displayed string. If _True_, the string will be parsed as a math text object. If _False_, the string will be considered a literal and no parsing will occur.\
\
### [Text can be positioned inside TextBox widget](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id23)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#text-can-be-positioned-inside-textbox-widget "Link to this heading")\
\
A new parameter called _textalignment_ can be used to control for the position of the text inside the Axes of the [`TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")\
 widget.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/68a37d28b3eea71811caa0b08c42106c/whats_new_3-5-0-6.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/f73e689f8fd7974ff8b6ad4a636abdea/whats_new_3-5-0-6.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/449bce30a7b3445cc47e05f7b21a05f9/whats_new_3-5-0-6.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-6.2x.png)\
\
### [Simplifying the font setting for usetex mode](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id24)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#simplifying-the-font-setting-for-usetex-mode "Link to this heading")\
\
Now the `[rcParams["font.family"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.family#rcparam-font-family) ` (default: `['sans-serif']`) accepts some font names as value for a more user-friendly setup.\
\
plt.rcParams.update({\
    "text.usetex": True,\
    "font.family": "Helvetica"\
})\
\
### [Type 42 subsetting is now enabled for PDF/PS backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id25)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#type-42-subsetting-is-now-enabled-for-pdf-ps-backends "Link to this heading")\
\
[`backend_pdf`](https://matplotlib.org/stable/api/backend_pdf_api.html#module-matplotlib.backends.backend_pdf "matplotlib.backends.backend_pdf")\
 and [`backend_ps`](https://matplotlib.org/stable/api/backend_ps_api.html#module-matplotlib.backends.backend_ps "matplotlib.backends.backend_ps")\
 now use a unified Type 42 font subsetting interface, with the help of [fontTools](https://fonttools.readthedocs.io/en/latest/)\
\
Set `[rcParams["pdf.fonttype"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=pdf.fonttype#rcparam-pdf-fonttype) ` (default: `3`) or `[rcParams["ps.fonttype"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.fonttype#rcparam-ps-fonttype) ` (default: `3`) to `42` to trigger this workflow:\
\
\# for PDF backend\
plt.rcParams\['pdf.fonttype'\] \= 42\
\
\# for PS backend\
plt.rcParams\['ps.fonttype'\] \= 42\
\
fig, ax \= plt.subplots()\
ax.text(0.4, 0.5, 'subsetted document is smaller in size!')\
\
fig.savefig("document.pdf")\
fig.savefig("document.ps")\
\
[rcParams improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id26)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#rcparams-improvements "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Allow setting default legend labelcolor globally](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id27)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#allow-setting-default-legend-labelcolor-globally "Link to this heading")\
\
A new `[rcParams["legend.labelcolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelcolor#rcparam-legend-labelcolor) ` (default: `'None'`) sets the default _labelcolor_ argument for [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")\
. The special values 'linecolor', 'markerfacecolor' (or 'mfc'), or 'markeredgecolor' (or 'mec') will cause the legend text to match the corresponding color of marker.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/27c466781301022dde97192d621e5a63/whats_new_3-5-0-7.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/5ab5ff99a4bee0c5639dcf94b6918a6e/whats_new_3-5-0-7.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/bdc0768abacbc3a99aa68cf19e19c73b/whats_new_3-5-0-7.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-7.2x.png)\
\
[3D Axes improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id28)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#d-axes-improvements "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Axes3D now allows manual control of draw order](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id29)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#axes3d-now-allows-manual-control-of-draw-order "Link to this heading")\
\
The [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")\
 class now has _computed\_zorder_ parameter. When set to False, Artists are drawn using their `zorder` attribute.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/cb4c26ec013e7a08aeadba7da1e70654/whats_new_3-5-0-8.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/bcb07a5045e9fe1e4e521d5d763b862b/whats_new_3-5-0-8.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/612c3371984f7c48b397ebe9e6efae66/whats_new_3-5-0-8.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-8.2x.png)\
\
### [Allow changing the vertical axis in 3d plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id30)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#allow-changing-the-vertical-axis-in-3d-plots "Link to this heading")\
\
[`view_init`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "mpl_toolkits.mplot3d.axes3d.Axes3D.view_init")\
 now has the parameter _vertical\_axis_ which allows switching which axis is aligned vertically.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/58f71ee0d2f7703291f4a215dbf65442/whats_new_3-5-0-9.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/5439e9754dc92753be652c82a927313b/whats_new_3-5-0-9.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/a72395bc7ca4471a8a02251b90c43ef5/whats_new_3-5-0-9.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-9.2x.png)\
\
### [`plot_surface` supports masked arrays and NaNs](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id31)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#plot-surface-supports-masked-arrays-and-nans "Link to this heading")\
\
[`axes3d.Axes3D.plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")\
 supports masked arrays and NaNs, and will now hide quads that contain masked or NaN points. The behaviour is similar to [`Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")\
 with `corner_mask=True`.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/b8ff8695586b447f411827787ed3008f/whats_new_3-5-0-10.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/bd28329d2b0e670016706b5928665cb6/whats_new_3-5-0-10.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/03d426e34ea0471829df70638bf5d9db/whats_new_3-5-0-10.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-10.2x.png)\
\
### [3D plotting methods support _data_ keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id32)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#d-plotting-methods-support-data-keyword-argument "Link to this heading")\
\
To match all 2D plotting methods, the 3D Axes now support the _data_ keyword argument. This allows passing arguments indirectly from a DataFrame-like structure.\
\
data \= {  \# A labelled data set, or e.g., Pandas DataFrame.\
    'x': ...,\
    'y': ...,\
    'z': ...,\
    'width': ...,\
    'depth': ...,\
    'top': ...,\
}\
\
fig, ax \= plt.subplots(subplot\_kw\={'projection': '3d')\
ax.bar3d('x', 'y', 'z', 'width', 'depth', 'top', data\=data)\
\
[Interactive tool improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id33)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#interactive-tool-improvements "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Colorbars now have pan and zoom functionality](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id34)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#colorbars-now-have-pan-and-zoom-functionality "Link to this heading")\
\
Interactive plots with colorbars can now be zoomed and panned on the colorbar axis. This adjusts the _vmin_ and _vmax_ of the `ScalarMappable` associated with the colorbar. This is currently only enabled for continuous norms. Norms used with contourf and categoricals, such as `BoundaryNorm` and `NoNorm`, have the interactive capability disabled by default. `cb.ax.set_navigate()` can be used to set whether a colorbar axes is interactive or not.\
\
### [Updated the appearance of Slider widgets](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id35)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#updated-the-appearance-of-slider-widgets "Link to this heading")\
\
The appearance of [`Slider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Slider.html#matplotlib.widgets.Slider "matplotlib.widgets.Slider")\
 and [`RangeSlider`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RangeSlider.html#matplotlib.widgets.RangeSlider "matplotlib.widgets.RangeSlider")\
 widgets were updated and given new styling parameters for the added handles.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/1fc77a320a5e3f69f8672f280e2f88df/whats_new_3-5-0-11.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/74f906718301feecf6933dec4bd84b94/whats_new_3-5-0-11.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/cbd545618473a448fa4c50513f3160c4/whats_new_3-5-0-11.png)\
)\
\
[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-5-0-11.2x.png)\
\
### [Removing points on a PolygonSelector](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id36)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#removing-points-on-a-polygonselector "Link to this heading")\
\
After completing a [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")\
, individual points can now be removed by right-clicking on them.\
\
### [Dragging selectors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id37)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#dragging-selectors "Link to this heading")\
\
The [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")\
, [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")\
 and [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")\
 have a new keyword argument, _drag\_from\_anywhere_, which when set to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")\
 allows you to click and drag from anywhere inside the selector to move it. Previously it was only possible to move it by either activating the move modifier button, or clicking on the central handle.\
\
The size of the [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")\
 can now be changed using the edge handles.\
\
### [Clearing selectors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id38)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#clearing-selectors "Link to this heading")\
\
The selectors ([`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")\
, [`LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")\
, [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")\
, [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")\
, and [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")\
) have a new method _clear_, which will clear the current selection and get the selector ready to make a new selection. This is equivalent to pressing the _escape_ key.\
\
### [Setting artist properties of selectors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id39)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#setting-artist-properties-of-selectors "Link to this heading")\
\
The artist properties of the [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")\
, [`LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")\
, [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")\
, [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")\
 and [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")\
 selectors can be changed using the `set_props` and `set_handle_props` methods.\
\
### [Ignore events outside selection](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id40)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#ignore-events-outside-selection "Link to this heading")\
\
The [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")\
, [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")\
 and [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")\
 selectors have a new keyword argument, _ignore\_event\_outside_, which when set to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")\
 will ignore events outside of the current selection. The handles or the new dragging functionality can instead be used to change the selection.\
\
### [`CallbackRegistry` objects gain a method to temporarily block signals](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id41)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#callbackregistry-objects-gain-a-method-to-temporarily-block-signals "Link to this heading")\
\
The context manager [`blocked`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.blocked "matplotlib.cbook.CallbackRegistry.blocked")\
 can be used to block callback signals from being processed by the `CallbackRegistry`. The optional keyword, _signal_, can be used to block a specific signal from being processed and let all other signals pass.\
\
import matplotlib.pyplot as plt\
\
fig, ax \= plt.subplots()\
ax.imshow(\[\[0, 1\], \[2, 3\]\])\
\
\# Block all interactivity through the canvas callbacks\
with fig.canvas.callbacks.blocked():\
    plt.show()\
\
fig, ax \= plt.subplots()\
ax.imshow(\[\[0, 1\], \[2, 3\]\])\
\
\# Only block key press events\
with fig.canvas.callbacks.blocked(signal\="key\_press\_event"):\
    plt.show()\
\
### [Directional sizing cursors](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id42)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#directional-sizing-cursors "Link to this heading")\
\
Canvases now support setting directional sizing cursors, i.e., horizontal and vertical double arrows. These are used in e.g., selector widgets. Try the [Mouse Cursor](https://matplotlib.org/stable/gallery/widgets/mouse_cursor.html)\
 example to see the cursor in your desired backend.\
\
[Sphinx extensions](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id43)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#sphinx-extensions "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [More configuration of `mathmpl` sphinx extension](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id44)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#more-configuration-of-mathmpl-sphinx-extension "Link to this heading")\
\
The [`matplotlib.sphinxext.mathmpl`](https://matplotlib.org/stable/api/sphinxext_mathmpl_api.html#module-matplotlib.sphinxext.mathmpl "matplotlib.sphinxext.mathmpl")\
 sphinx extension supports two new configuration options that may be specified in your `conf.py`:\
\
*   `mathmpl_fontsize` (float), which sets the font size of the math text in points;\
    \
*   `mathmpl_srcset` (list of str), which provides a list of sizes to support [responsive resolution images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)\
     The list should contain additional x-descriptors (`'1.5x'`, `'2x'`, etc.) to generate (1x is the default and always included.)\
    \
\
[Backend-specific improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id45)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#backend-specific-improvements "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [GTK backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id46)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#gtk-backend "Link to this heading")\
\
A backend supporting [GTK4](https://www.gtk.org/)\
 has been added. Both Agg and Cairo renderers are supported. The GTK4 backends may be selected as GTK4Agg or GTK4Cairo.\
\
### [Qt backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id47)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#qt-backends "Link to this heading")\
\
Support for Qt6 (using either [PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)\
 or [PySide6](https://doc.qt.io/qtforpython/)\
) has been added, with either the Agg or Cairo renderers. Simultaneously, support for Qt4 has been dropped. Both Qt6 and Qt5 are supported by a combined backend (QtAgg or QtCairo), and the loaded version is determined by modules already imported, the [`QT_API`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-QT_API)\
 environment variable, and available packages. See [Qt Bindings](https://matplotlib.org/stable/api/backend_qt_api.html#qt-bindings)\
 for details. The versioned Qt5 backend names (Qt5Agg or Qt5Cairo) remain supported for backwards compatibility.\
\
### [HiDPI support in Cairo-based, GTK, and Tk backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id48)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#hidpi-support-in-cairo-based-gtk-and-tk-backends "Link to this heading")\
\
The GTK3 backends now support HiDPI fully, including mixed monitor cases (on Wayland only). The newly added GTK4 backends also support HiDPI.\
\
The TkAgg backend now supports HiDPI **on Windows only**, including mixed monitor cases.\
\
All Cairo-based backends correctly support HiDPI as well as their Agg counterparts did (i.e., if the toolkit supports HiDPI, then the \*Cairo backend will now support it, but not otherwise.)\
\
### [Qt figure options editor improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id49)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#qt-figure-options-editor-improvements "Link to this heading")\
\
The figure options editor in the Qt backend now also supports editing the left and right titles (plus the existing centre title). Editing Axis limits is better supported when using a date converter. The `symlog` option is now available in Axis scaling options. All entries with the same label are now shown in the Curves tab.\
\
### [WX backends support mouse navigation buttons](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id50)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#wx-backends-support-mouse-navigation-buttons "Link to this heading")\
\
The WX backends now support navigating through view states using the mouse forward/backward buttons, as in other backends.\
\
### [WebAgg uses asyncio instead of Tornado](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id51)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#webagg-uses-asyncio-instead-of-tornado "Link to this heading")\
\
The WebAgg backend defaults to using [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "(in Python v3.14)")\
 over Tornado for timer support. This allows using the WebAgg backend in JupyterLite.\
\
[Version information](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#id52)\
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.5.0.html#version-information "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We switched to the [release-branch-semver](https://github.com/pypa/setuptools_scm#version-number-construction)\
 version scheme of setuptools-scm. This only affects the version information for development builds. Their version number now describes the targeted release, i.e. 3.5.0.dev820+g6768ef8c4c is 820 commits after the previous release and is scheduled to be officially released as 3.5.0 later.\
\
In addition to the string `__version__`, there is now a namedtuple `__version_info__` as well, which is modelled after [sys.version\_info](https://docs.python.org/3/library/sys.html#sys.version_info)\
. Its primary use is safely comparing version information, e.g. `if __version_info__ >= (3, 4, 2)`.\
\
On this page