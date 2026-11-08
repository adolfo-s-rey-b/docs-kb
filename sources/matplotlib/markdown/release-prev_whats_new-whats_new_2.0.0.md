[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#main-content)

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
    

What's new in Matplotlib 2.0 (Jan 17, 2017)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#what-s-new-in-matplotlib-2-0-jan-17-2017 "Link to this heading")

==========================================================================================================================================================================================

Note

Matplotlib 2.0 supports Python 2.7, and 3.4+

Default style changes[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#default-style-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

The major changes in v2.0 are related to overhauling the default styles.

*   [Changes to the default style](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html)
    *   [Colors, color cycles, and colormaps](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#colors-color-cycles-and-colormaps)
        
    *   [Figure size, font size, and screen dpi](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#figure-size-font-size-and-screen-dpi)
        
    *   [Plotting functions](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#plotting-functions)
        
    *   [Hatching](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#hatching)
        
    *   [Fonts](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#fonts)
        
    *   [Legends](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#legends)
        
    *   [Image](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#image)
        
    *   [Plot layout](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#plot-layout)
        
    *   [mplot3d](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#mplot3d)
        

Improved color conversion API and RGBA support[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#improved-color-conversion-api-and-rgba-support "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
 gained a new color conversion API with full support for the alpha channel. The main public functions are [`is_color_like()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.is_color_like.html#matplotlib.colors.is_color_like "matplotlib.colors.is_color_like")
, [`matplotlib.colors.to_rgba()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#matplotlib.colors.to_rgba "matplotlib.colors.to_rgba")
, [`matplotlib.colors.to_rgba_array()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "matplotlib.colors.to_rgba_array")
 and [`to_hex()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_hex.html#matplotlib.colors.to_hex "matplotlib.colors.to_hex")
. RGBA quadruplets are encoded in hex format as "#rrggbbaa".

A side benefit is that the Qt options editor now allows setting the alpha channel of the artists as well.

New Configuration (rcParams)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#new-configuration-rcparams "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

New rcparams added

| Parameter | Description |
| --- | --- |
| `[rcParams["date.autoformatter.year"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.year#rcparam-date-autoformatter-year) ` (default: `'%Y'`) | format string for 'year' scale dates |
| `[rcParams["date.autoformatter.month"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.month#rcparam-date-autoformatter-month) ` (default: `'%Y-%m'`) | format string for 'month' scale dates |
| `[rcParams["date.autoformatter.day"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.day#rcparam-date-autoformatter-day) ` (default: `'%Y-%m-%d'`) | format string for 'day' scale dates |
| `[rcParams["date.autoformatter.hour"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.hour#rcparam-date-autoformatter-hour) ` (default: `'%m-%d %H'`) | format string for 'hour' scale times |
| `[rcParams["date.autoformatter.minute"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.minute#rcparam-date-autoformatter-minute) ` (default: `'%d %H:%M'`) | format string for 'minute' scale times |
| `[rcParams["date.autoformatter.second"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.second#rcparam-date-autoformatter-second) ` (default: `'%H:%M:%S'`) | format string for 'second' scale times |
| `[rcParams["date.autoformatter.microsecond"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.autoformatter.microsecond#rcparam-date-autoformatter-microsecond) ` (default: `'%M:%S.%f'`) | format string for 'microsecond' scale times |
| `[rcParams["scatter.marker"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=scatter.marker#rcparam-scatter-marker) ` (default: `'o'`) | default marker for scatter plot |
| `[rcParams["svg.hashsalt"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=svg.hashsalt#rcparam-svg-hashsalt) ` (default: `None`) | see note |
| `[rcParams["xtick.top"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.top#rcparam-xtick-top) ` (default: `False`), `[rcParams["xtick.major.top"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.major.top#rcparam-xtick-major-top) ` (default: `True`) `[rcParams["xtick.minor.top"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.minor.top#rcparam-xtick-minor-top) ` (default: `True`), `[rcParams["xtick.bottom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.bottom#rcparam-xtick-bottom) ` (default: `True`), `[rcParams["xtick.major.bottom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.major.bottom#rcparam-xtick-major-bottom) ` (default: `True`) `[rcParams["xtick.minor.bottom"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.minor.bottom#rcparam-xtick-minor-bottom) ` (default: `True`), `[rcParams["ytick.left"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.left#rcparam-ytick-left) ` (default: `True`), `[rcParams["ytick.minor.left"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.minor.left#rcparam-ytick-minor-left) ` (default: `True`), `[rcParams["ytick.major.left"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.major.left#rcparam-ytick-major-left) ` (default: `True`) `[rcParams["ytick.right"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.right#rcparam-ytick-right) ` (default: `False`), `[rcParams["ytick.minor.right"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.minor.right#rcparam-ytick-minor-right) ` (default: `True`), `[rcParams["ytick.major.right"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.major.right#rcparam-ytick-major-right) ` (default: `True`) | Control where major and minor ticks are drawn. The global values are `and`ed with the corresponding major/minor values. corresponding major/minor values. |
| `[rcParams["hist.bins"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=hist.bins#rcparam-hist-bins) ` (default: `10`) | The default number of bins to use in [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")<br>. This can be an [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")<br>, a list of floats, or `'auto'` if numpy >= 1.11 is installed. |
| `[rcParams["lines.scale_dashes"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.scale_dashes#rcparam-lines-scale-dashes) ` (default: `True`) | Whether the line dash patterns should scale with linewidth. |
| `[rcParams["axes.formatter.offset_threshold"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.offset_threshold#rcparam-axes-formatter-offset-threshold) ` (default: `4`) | Minimum number of digits saved in tick labels that triggers using an offset. |

### Added `svg.hashsalt` key to rcParams[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#added-svg-hashsalt-key-to-rcparams "Link to this heading")

If `svg.hashsalt` is `None` (which it is by default), the svg backend uses `uuid4` to generate the hash salt. If it is not `None`, it must be a string that is used as the hash salt instead of `uuid4`. This allows for deterministic SVG output.

### Removed the `svg.image_noscale` rcParam[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#removed-the-svg-image-noscale-rcparam "Link to this heading")

As a result of the extensive changes to image handling, the `svg.image_noscale` rcParam has been removed. The same functionality may be achieved by setting `interpolation='none'` on individual images or globally using the `image.interpolation` rcParam.

Qualitative colormaps[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#qualitative-colormaps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

ColorBrewer's "qualitative" colormaps ("Accent", "Dark2", "Paired", "Pastel1", "Pastel2", "Set1", "Set2", "Set3") were intended for discrete categorical data, with no implication of value, and therefore have been converted to `ListedColormap` instead of `LinearSegmentedColormap`, so the colors will no longer be interpolated and they can be used for choropleths, labeled image features, etc.

Axis offset label now responds to _labelcolor_[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#axis-offset-label-now-responds-to-labelcolor "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Axis offset labels are now colored the same as axis tick markers when _labelcolor_ is altered.

Improved offset text choice[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#improved-offset-text-choice "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

The default offset-text choice was changed to only use significant digits that are common to all ticks (e.g. 1231..1239 -> 1230, instead of 1231), except when they straddle a relatively large multiple of a power of ten, in which case that multiple is chosen (e.g. 1999..2001->2000).

Style parameter blacklist[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#style-parameter-blacklist "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

In order to prevent unexpected consequences from using a style, style files are no longer able to set parameters that affect things unrelated to style. These parameters include:

'interactive', 'backend', 'backend.qt4', 'webagg.port',
'webagg.port\_retries', 'webagg.open\_in\_browser', 'backend\_fallback',
'toolbar', 'timezone', 'datapath', 'figure.max\_open\_warning',
'savefig.directory', 'tk.window\_focus', 'docstring.hardcopy'

Change in default font[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#change-in-default-font "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

The default font used by matplotlib in text has been changed to DejaVu Sans and DejaVu Serif for the sans-serif and serif families, respectively. The DejaVu font family is based on the previous matplotlib default --Bitstream Vera-- but includes a much wider range of characters.

The default mathtext font has been changed from Computer Modern to the DejaVu family to maintain consistency with regular text. Two new options for the `mathtext.fontset` configuration parameter have been added: `dejavusans` (default) and `dejavuserif`. Both of these options use DejaVu glyphs whenever possible and fall back to STIX symbols when a glyph is not found in DejaVu. To return to the previous behavior, set the rcParam `mathtext.fontset` to `cm`.

Faster text rendering[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#faster-text-rendering "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Rendering text in the Agg backend is now less fuzzy and about 20% faster to draw.

Improvements for the Qt figure options editor[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#improvements-for-the-qt-figure-options-editor "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Various usability improvements were implemented for the Qt figure options editor, among which:

*   Line style entries are now sorted without duplicates.
    
*   The colormap and normalization limits can now be set for images.
    
*   Line edits for floating values now display only as many digits as necessary to avoid precision loss. An important bug was also fixed regarding input validation using Qt5 and a locale where the decimal separator is ",".
    
*   The axes selector now uses shorter, more user-friendly names for axes, and does not crash if there are no axes.
    
*   Line and image entries using the default labels ("\_lineX", "\_imageX") are now sorted numerically even when there are more than 10 entries.
    

Improved image support[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#improved-image-support "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Prior to version 2.0, matplotlib resampled images by first applying the colormap and then resizing the result. Since the resampling was performed on the colored image, this introduced colors in the output image that didn't actually exist in the colormap. Now, images are resampled first (and entirely in floating-point, if the input image is floating-point), and then the colormap is applied.

In order to make this important change, the image handling code was almost entirely rewritten. As a side effect, image resampling uses less memory and fewer datatype conversions than before.

The experimental private feature where one could "skew" an image by setting the private member `_image_skew_coordinate` has been removed. Instead, images will obey the transform of the axes on which they are drawn.

### Non-linear scales on image plots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#non-linear-scales-on-image-plots "Link to this heading")

[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 now draws data at the requested points in data space after the application of non-linear scales.

The image on the left demonstrates the new, correct behavior. The old behavior can be recreated using [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 as demonstrated on the right.

([`Source code`](https://matplotlib.org/stable/_downloads/d188ba136190f843258338e2b9feb0bd/whats_new_2-0-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/2013c6f02901554dfcca33509c62191a/whats_new_2-0-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/7c1401ca6f525c103fbdcc355c8e7934/whats_new_2-0-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-0-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-0-0-1.2x.png)

This can be understood by analogy to plotting a histogram with linearly spaced bins with a logarithmic x-axis. Equal sized bins will be displayed as wider for small _x_ and narrower for large _x_.

Support for HiDPI (Retina) displays in the NbAgg and WebAgg backends[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#support-for-hidpi-retina-displays-in-the-nbagg-and-webagg-backends "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The NbAgg and WebAgg backends will now use the full resolution of your high-pixel-density display.

Change in the default animation codec[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#change-in-the-default-animation-codec "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default animation codec has been changed from `mpeg4` to `h264`, which is more efficient. It can be set via the `animation.codec` rcParam.

Deprecated support for mencoder in animation[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#deprecated-support-for-mencoder-in-animation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The use of mencoder for writing video files with mpl is problematic; switching to ffmpeg is strongly advised. All support for mencoder will be removed in version 2.2.

Boxplot Zorder Keyword Argument[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#boxplot-zorder-keyword-argument "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The _zorder_ parameter now exists for [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
. This allows the zorder of a boxplot to be set in the plotting function call.

boxplot(np.arange(10), zorder\=10)

Filled `+` and `x` markers[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#filled-and-x-markers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

New fillable _plus_ and _x_ markers have been added. See the [`markers`](https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers "matplotlib.markers")
 module and [marker reference](https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html)
 examples.

_rcount_ and _ccount_ for [`plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#rcount-and-ccount-for-plot-surface "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As of v2.0, mplot3d's [`plot_surface`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface.html#mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface "mpl_toolkits.mplot3d.axes3d.Axes3D.plot_surface")
 now accepts _rcount_ and _ccount_ arguments for controlling the sampling of the input data for plotting. These arguments specify the maximum number of evenly spaced samples to take from the input data. These arguments are also the new default sampling method for the function, and is considered a style change.

The old _rstride_ and _cstride_ arguments, which specified the size of the evenly spaced samples, become the default when 'classic' mode is invoked, and are still available for use. There are no plans for deprecating these arguments.

Streamplot Zorder Keyword Argument Changes[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#streamplot-zorder-keyword-argument-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `zorder` parameter for [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
 now has default value of `None` instead of `2`. If `None` is given as `zorder`, [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
 has a default `zorder` of `matplotlib.lines.Line2D.zorder`.

Extension to [`matplotlib.backend_bases.GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.0.0.html#extension-to-matplotlib-backend-bases-graphicscontextbase "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To support standardizing hatch behavior across the backends we ship the [`matplotlib.backend_bases.GraphicsContextBase.get_hatch_color`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_hatch_color "matplotlib.backend_bases.GraphicsContextBase.get_hatch_color")
 method as added to [`matplotlib.backend_bases.GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
. This is only used during the render process in the backends we ship so will not break any third-party backends.

If you maintain a third-party backend which extends [`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
 this method is now available to you and should be used to color hatch patterns.

On this page