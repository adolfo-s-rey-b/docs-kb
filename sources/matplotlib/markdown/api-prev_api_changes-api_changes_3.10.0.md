[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#main-content)

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
    

API Changes for 3.10.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#api-changes-for-3-10-0 "Link to this heading")

====================================================================================================================================================

[Behavior Changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#behavior-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### onselect argument to selector widgets made optional[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#onselect-argument-to-selector-widgets-made-optional "Link to this heading")

The _onselect_ argument to [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
, [`LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")
, [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
, and [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 is no longer required.

### `NavigationToolbar2.save_figure` now returns filepath of saved figure[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#navigationtoolbar2-save-figure-now-returns-filepath-of-saved-figure "Link to this heading")

`NavigationToolbar2.save_figure` function may return the filename of the saved figure.

If a backend implements this functionality it should return [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 in the case where no figure is actually saved (because the user closed the dialog without saving).

If the backend does not or can not implement this functionality (currently the Gtk4 backends and webagg backends do not) this method will return `NavigationToolbar2.UNKNOWN_SAVED_STATUS`.

### SVG output: improved reproducibility[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#svg-output-improved-reproducibility "Link to this heading")

Some SVG-format plots [produced different output on each render](https://github.com/matplotlib/matplotlib/issues/27831)
, even with a static `svg.hashsalt` value configured.

The problem was a non-deterministic ID-generation scheme for clip paths; the fix introduces a repeatable, monotonically increasing integer ID scheme as a replacement.

Provided that plots add clip paths themselves in deterministic order, this enables repeatable (a.k.a. reproducible, deterministic) SVG output.

### ft2font classes are now final[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#ft2font-classes-are-now-final "Link to this heading")

The ft2font classes [`ft2font.FT2Font`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
, and [`ft2font.FT2Image`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image "matplotlib.ft2font.FT2Image")
 are now final and can no longer be subclassed.

### `InsetIndicator` artist[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#insetindicator-artist "Link to this heading")

[`indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset")
 and [`indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom")
 now return an instance of [`InsetIndicator`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator "matplotlib.inset.InsetIndicator")
. Use the [`rectangle`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.rectangle "matplotlib.inset.InsetIndicator.rectangle")
 and [`connectors`](https://matplotlib.org/stable/api/inset_api.html#matplotlib.inset.InsetIndicator.connectors "matplotlib.inset.InsetIndicator.connectors")
 properties of this artist to access the objects that were previously returned directly.

### `imshow` _interpolation\_stage_ default changed to 'auto'[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#imshow-interpolation-stage-default-changed-to-auto "Link to this heading")

The _interpolation\_stage_ parameter of [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 has a new default value 'auto'. For images that are up-sampled less than a factor of three or down-sampled, image interpolation will occur in 'rgba' space. For images that are up-sampled by a factor of 3 or more, then image interpolation occurs in 'data' space.

The previous default was 'data', so down-sampled images may change subtly with the new default. However, the new default also avoids floating point artifacts at sharp boundaries in a colormap when down-sampling.

The previous behavior can achieved by setting the _interpolation\_stage_ parameter or `[rcParams["image.interpolation_stage"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.interpolation_stage#rcparam-image-interpolation-stage) ` (default: `'auto'`) to 'data'.

### imshow default _interpolation_ changed to 'auto'[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#imshow-default-interpolation-changed-to-auto "Link to this heading")

The _interpolation_ parameter of [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 has a new default value 'auto', changed from 'antialiased', for consistency with _interpolation\_stage_ and because the interpolation is only anti-aliasing during down-sampling. Passing 'antialiased' still works, and behaves exactly the same as 'auto', but is discouraged.

### dark\_background and fivethirtyeight styles no longer set `savefig.facecolor` and `savefig.edgecolor`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#dark-background-and-fivethirtyeight-styles-no-longer-set-savefig-facecolor-and-savefig-edgecolor "Link to this heading")

When using these styles, `[rcParams["savefig.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.facecolor#rcparam-savefig-facecolor) ` (default: `'auto'`) and `[rcParams["savefig.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.edgecolor#rcparam-savefig-edgecolor) ` (default: `'auto'`) now inherit the global default value of "auto", which means that the actual figure colors will be used. Previously, these rcParams were set to the same values as `[rcParams["figure.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.facecolor#rcparam-figure-facecolor) ` (default: `'white'`) and `[rcParams["figure.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.edgecolor#rcparam-figure-edgecolor) ` (default: `'white'`), i.e. a saved figure would always use the theme colors even if the user manually overrode them; this is no longer the case.

This change should have no impact for users that do not manually set the figure face and edge colors.

### Add zorder option in QuiverKey[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#add-zorder-option-in-quiverkey "Link to this heading")

`zorder` can be used as a keyword argument to [`QuiverKey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.quiver.QuiverKey.html#matplotlib.quiver.QuiverKey "matplotlib.quiver.QuiverKey")
. Previously, that parameter did not have any effect because the zorder was hard coded.

### Subfigures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#subfigures "Link to this heading")

[`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 are now added in row-major order to be consistent with [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
. The return value of [`subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 is not changed, but the order of `fig.subfigs` is.

### (Sub)Figure.get\_figure[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#sub-figure-get-figure "Link to this heading")

...in future will by default return the direct parent figure, which may be a SubFigure. This will make the default behavior consistent with the [`get_figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_figure.html#matplotlib.artist.Artist.get_figure "matplotlib.artist.Artist.get_figure")
 method of other artists. To control the behavior, use the newly introduced _root_ parameter.

### `transforms.AffineDeltaTransform` updates correctly on axis limit changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#transforms-affinedeltatransform-updates-correctly-on-axis-limit-changes "Link to this heading")

Before this change, transform sub-graphs with `AffineDeltaTransform` did not update correctly. This PR ensures that changes to the child transform are passed through correctly.

### The offset string associated with ConciseDateFormatter will now invert when the axis is inverted[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#the-offset-string-associated-with-concisedateformatter-will-now-invert-when-the-axis-is-inverted "Link to this heading")

Previously, when the axis was inverted, the offset string associated with ConciseDateFormatter would not change, so the offset string indicated the axis was oriented in the wrong direction. Now, when the axis is inverted, the offset string is oriented correctly.

### `suptitle` in compressed layout[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#suptitle-in-compressed-layout "Link to this heading")

Compressed layout now automatically positions the [`suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
 just above the top row of axes. To keep this title in its previous position, either pass `in_layout=False` or explicitly set `y=0.98` in the [`suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
 call.

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Positional parameters in plotting functions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#positional-parameters-in-plotting-functions "Link to this heading")

Many plotting functions will restrict positional arguments to the first few parameters in the future. All further configuration parameters will have to be passed as keyword arguments. This is to enforce better code and and allow for future changes with reduced risk of breaking existing code.

### Changing `Figure.number`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#changing-figure-number "Link to this heading")

Changing `Figure.number` is deprecated. This value is used by [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 to identify figures. It must stay in sync with the pyplot internal state and is not intended to be modified by the user.

### `PdfFile.hatchPatterns`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#pdffile-hatchpatterns "Link to this heading")

... is deprecated.

### (Sub)Figure.set\_figure[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#sub-figure-set-figure "Link to this heading")

...is deprecated and in future will always raise an exception. The parent and root figures of a (Sub)Figure are set at instantiation and cannot be changed.

### `Poly3DCollection.get_vector`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#poly3dcollection-get-vector "Link to this heading")

... is deprecated with no replacement.

### Deprecated `register` on `matplotlib.patches._Styles` and subclasses[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#deprecated-register-on-matplotlib-patches-styles-and-subclasses "Link to this heading")

This class method is never used internally. Due to the internal check in the method it only accepts subclasses of a private baseclass embedded in the host class which makes it unlikely that it has been used externally.

### matplotlib.validate\_backend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#matplotlib-validate-backend "Link to this heading")

...is deprecated. Please use [`matplotlib.rcsetup.validate_backend`](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_backend "matplotlib.rcsetup.validate_backend")
 instead.

### matplotlib.sanitize\_sequence[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#matplotlib-sanitize-sequence "Link to this heading")

...is deprecated. Please use [`matplotlib.cbook.sanitize_sequence`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.sanitize_sequence "matplotlib.cbook.sanitize_sequence")
 instead.

### ft2font module-level constants replaced by enums[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#ft2font-module-level-constants-replaced-by-enums "Link to this heading")

The [`ft2font`](https://matplotlib.org/stable/api/ft2font.html#module-matplotlib.ft2font "matplotlib.ft2font")
\-level constants have been converted to [`enum`](https://docs.python.org/3/library/enum.html#module-enum "(in Python v3.14)")
 classes, and all API using them now take/return the new types.

The following constants are now part of [`ft2font.Kerning`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
 (without the `KERNING_` prefix):

*   `KERNING_DEFAULT`
    
*   `KERNING_UNFITTED`
    
*   `KERNING_UNSCALED`
    

The following constants are now part of [`ft2font.LoadFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.LoadFlags "matplotlib.ft2font.LoadFlags")
 (without the `LOAD_` prefix):

*   `LOAD_DEFAULT`
    
*   `LOAD_NO_SCALE`
    
*   `LOAD_NO_HINTING`
    
*   `LOAD_RENDER`
    
*   `LOAD_NO_BITMAP`
    
*   `LOAD_VERTICAL_LAYOUT`
    
*   `LOAD_FORCE_AUTOHINT`
    
*   `LOAD_CROP_BITMAP`
    
*   `LOAD_PEDANTIC`
    
*   `LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH`
    
*   `LOAD_NO_RECURSE`
    
*   `LOAD_IGNORE_TRANSFORM`
    
*   `LOAD_MONOCHROME`
    
*   `LOAD_LINEAR_DESIGN`
    
*   `LOAD_NO_AUTOHINT`
    
*   `LOAD_TARGET_NORMAL`
    
*   `LOAD_TARGET_LIGHT`
    
*   `LOAD_TARGET_MONO`
    
*   `LOAD_TARGET_LCD`
    
*   `LOAD_TARGET_LCD_V`
    

The following constants are now part of [`ft2font.FaceFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
:

*   `EXTERNAL_STREAM`
    
*   `FAST_GLYPHS`
    
*   `FIXED_SIZES`
    
*   `FIXED_WIDTH`
    
*   `GLYPH_NAMES`
    
*   `HORIZONTAL`
    
*   `KERNING`
    
*   `MULTIPLE_MASTERS`
    
*   `SCALABLE`
    
*   `SFNT`
    
*   `VERTICAL`
    

The following constants are now part of [`ft2font.StyleFlags`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags "matplotlib.ft2font.StyleFlags")
:

*   `ITALIC`
    
*   `BOLD`
    

### FontProperties initialization[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#fontproperties-initialization "Link to this heading")

[`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 initialization is limited to the two call patterns:

*   single positional parameter, interpreted as fontconfig pattern
    
*   only keyword parameters for setting individual properties
    

All other previously supported call patterns are deprecated.

### `AxLine` `xy1` and `xy2` setters[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#axline-xy1-and-xy2-setters "Link to this heading")

These setters now each take a single argument, `xy1` or `xy2` as a tuple. The old form, where `x` and `y` were passed as separate arguments, is deprecated.

### Calling `pyplot.polar()` with an existing non-polar Axes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#calling-pyplot-polar-with-an-existing-non-polar-axes "Link to this heading")

This currently plots the data into the non-polar Axes, ignoring the "polar" intention. This usage scenario is deprecated and will raise an error in the future.

### Passing floating-point values to `RendererAgg.draw_text_image`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#passing-floating-point-values-to-rendereragg-draw-text-image "Link to this heading")

Any floating-point values passed to the _x_ and _y_ parameters were truncated to integers silently. This behaviour is now deprecated, and only [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 values should be used.

### Passing floating-point values to `FT2Image`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#passing-floating-point-values-to-ft2image "Link to this heading")

Any floating-point values passed to the [`FT2Image`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image "matplotlib.ft2font.FT2Image")
 constructor, or the _x0_, _y0_, _x1_, and _y1_ parameters of [`FT2Image.draw_rect_filled`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Image.draw_rect_filled "matplotlib.ft2font.FT2Image.draw_rect_filled")
 were truncated to integers silently. This behaviour is now deprecated, and only [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
 values should be used.

### `boxplot` and `bxp` _vert_ parameter, and `rcParams["boxplot.vertical"]`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#boxplot-and-bxp-vert-parameter-and-rcparams-boxplot-vertical "Link to this heading")

The parameter _vert: bool_ has been deprecated on [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 and [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
. It is replaced by _orientation: {"vertical", "horizontal"}_ for API consistency.

`rcParams["boxplot.vertical"]`, which controlled the orientation of `boxplot`, is deprecated without replacement.

This deprecation is currently marked as pending and will be fully deprecated in Matplotlib 3.11.

### `violinplot` and `violin` _vert_ parameter[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#violinplot-and-violin-vert-parameter "Link to this heading")

The parameter _vert: bool_ has been deprecated on [`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
 and [`violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin")
. It will be replaced by _orientation: {"vertical", "horizontal"}_ for API consistency.

This deprecation is currently marked as pending and will be fully deprecated in Matplotlib 3.11.

### `proj3d.proj_transform_clip`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#proj3d-proj-transform-clip "Link to this heading")

... is deprecated with no replacement.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#removals "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### ttconv removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#ttconv-removed "Link to this heading")

The `matplotlib._ttconv` extension has been removed. Most of its functionaliy was already replaced by other code, and the only thing left was embedding TTF fonts in PostScript in Type 42 format. This is now done in the PS backend using the FontTools library.

### Remove hard reference to `lastevent` in `LocationEvent`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#remove-hard-reference-to-lastevent-in-locationevent "Link to this heading")

This was previously used to detect exiting from axes, however the hard reference would keep closed [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 objects and their children alive longer than expected.

### `ft2font.FT2Image.draw_rect` and `ft2font.FT2Font.get_xys`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#ft2font-ft2image-draw-rect-and-ft2font-ft2font-get-xys "Link to this heading")

... have been removed as they are unused.

### `Tick.set_label`, `Tick.set_label1` and `Tick.set_label2`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#tick-set-label-tick-set-label1-and-tick-set-label2 "Link to this heading")

... are removed. Calling these methods from third-party code usually had no effect, as the labels are overwritten at draw time by the tick formatter.

### Functions in `mpl_toolkits.mplot3d.proj3d`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#functions-in-mpl-toolkits-mplot3d-proj3d "Link to this heading")

The function `transform` is just an alias for `proj_transform`, use the latter instead.

The following functions were either unused (so no longer required in Matplotlib) or considered private.

*   `ortho_transformation`
    
*   `persp_transformation`
    
*   `proj_points`
    
*   `proj_trans_points`
    
*   `rot_x`
    
*   `rotation_about_vector`
    
*   `view_transformation`
    

### Arguments other than `renderer` to `get_tightbbox`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#arguments-other-than-renderer-to-get-tightbbox "Link to this heading")

... are keyword-only arguments. This is for consistency and that different classes have different additional arguments.

### Method parameters renamed to match base classes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#method-parameters-renamed-to-match-base-classes "Link to this heading")

The only parameter of `transform_affine` and `transform_non_affine` in `Transform` subclasses is renamed to _values_.

The _points_ parameter of `transforms.IdentityTransform.transform` is renamed to _values_.

The _trans_ parameter of `table.Cell.set_transform` is renamed to _t_ consistently with [`Artist.set_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform")
.

The _clippath_ parameters of `axis.Axis.set_clip_path` and `axis.Tick.set_clip_path` are renamed to _path_ consistently with [`Artist.set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
.

The _s_ parameter of `images.NonUniformImage.set_filternorm` is renamed to _filternorm_ consistently with `_ImageBase.set_filternorm`.

The _s_ parameter of `images.NonUniformImage.set_filterrad` is renamed to _filterrad_ consistently with `_ImageBase.set_filterrad`.

The only parameter of `Annotation.contains` and `Legend.contains` is renamed to _mouseevent_ consistently with [`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains")
.

### Method parameters renamed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#method-parameters-renamed "Link to this heading")

The _p_ parameter of `BboxBase.padded` is renamed to _w\_pad_, consistently with the other parameter, _h\_pad_

### _numdecs_ parameter and attribute of `LogLocator`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#numdecs-parameter-and-attribute-of-loglocator "Link to this heading")

... are removed without replacement, because they had no effect. The `PolyQuadMesh` class requires full 2D arrays of values ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously, if a masked array was input, the list of polygons within the collection would shrink to the size of valid polygons and users were required to keep track of which polygons were drawn and call `set_array()` with the smaller "compressed" array size. Passing the "compressed" and flattened array values will no longer work and the full 2D array of values (including the mask) should be passed to [`PolyQuadMesh.set_array`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyQuadMesh.set_array "matplotlib.collections.PolyQuadMesh.set_array")
. `ContourSet.collections` ~~~~~~~~~~~~~~~~~~~~~~~~~~

... has been removed. [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 is now implemented as a single [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 of paths, each path corresponding to a contour level, possibly including multiple unconnected components.

### `ContourSet.antialiased`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#contourset-antialiased "Link to this heading")

... has been removed. Use [`get_antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_antialiased "matplotlib.collections.Collection.get_antialiased")
 or [`set_antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")
 instead. Note that [`get_antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_antialiased "matplotlib.collections.Collection.get_antialiased")
 returns an array.

### `tcolors` and `tlinewidths` attributes of `ContourSet`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#tcolors-and-tlinewidths-attributes-of-contourset "Link to this heading")

... have been removed. Use [`get_facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_facecolor "matplotlib.collections.Collection.get_facecolor")
, [`get_edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_edgecolor "matplotlib.collections.Collection.get_edgecolor")
 or [`get_linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.get_linewidths "matplotlib.collections.Collection.get_linewidths")
 instead.

### `calc_label_rot_and_inline` method of `ContourLabeler`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#calc-label-rot-and-inline-method-of-contourlabeler "Link to this heading")

... has been removed without replacement.

### `add_label_clabeltext` method of `ContourLabeler`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#add-label-clabeltext-method-of-contourlabeler "Link to this heading")

... has been removed. Use [`add_label`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourLabeler.add_label "matplotlib.contour.ContourLabeler.add_label")
 instead. Passing extra positional arguments to `Figure.add_axes` ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Positional arguments passed to [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
 other than a rect or an existing `Axes` were previously ignored, and is now an error.

### Artists explicitly passed in will no longer be filtered by legend() based on their label[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#artists-explicitly-passed-in-will-no-longer-be-filtered-by-legend-based-on-their-label "Link to this heading")

Previously, artists explicitly passed to `legend(handles=[...])` are filtered out if their label starts with an underscore. This filter is no longer applied; explicitly filter out such artists (`[art for art in artists if not art.get_label().startswith('_')]`) if necessary.

Note that if no handles are specified at all, then the default still filters out labels starting with an underscore.

### The parameter of `Annotation.contains` and `Legend.contains` is renamed to _mouseevent_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#the-parameter-of-annotation-contains-and-legend-contains-is-renamed-to-mouseevent "Link to this heading")

... consistently with [`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains")
.

### Support for passing the "frac" key in `annotate(..., arrowprops={"frac": ...})`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#support-for-passing-the-frac-key-in-annotate-arrowprops-frac "Link to this heading")

... has been removed. This key has had no effect since Matplotlib 1.5.

### Passing non-int or sequence of non-int to `Table.auto_set_column_width`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#passing-non-int-or-sequence-of-non-int-to-table-auto-set-column-width "Link to this heading")

Column numbers are ints, and formerly passing any other type was effectively ignored. This has now become an error.

### Widgets[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#widgets "Link to this heading")

The _visible_ attribute getter of `*Selector` widgets has been removed; use `get_visible` instead.

### Auto-closing of figures when switching backend[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#auto-closing-of-figures-when-switching-backend "Link to this heading")

Allowable backend switches (i.e. those that do not swap a GUI event loop with another one) will not close existing figures. If necessary, call `plt.close("all")` before switching.

### `FigureCanvasBase.switch_backends`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#figurecanvasbase-switch-backends "Link to this heading")

... has been removed with no replacement.

### Accessing `event.guiEvent` after event handlers return[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#accessing-event-guievent-after-event-handlers-return "Link to this heading")

... is no longer supported, and `event.guiEvent` will be set to None once the event handlers return. For some GUI toolkits, it is unsafe to use the event, though you may separately stash the object at your own risk.

### `PdfPages(keep_empty=True)`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#pdfpages-keep-empty-true "Link to this heading")

A zero-page PDF is not valid, thus passing `keep_empty=True` to [`backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
 and [`backend_pgf.PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")
, and the `keep_empty` attribute of these classes, is no longer allowed, and empty PDF files will not be created.

Furthermore, [`backend_pdf.PdfPages`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
 no longer immediately creates the target file upon instantiation, but only when the first figure is saved. To fully control file creation, directly pass an opened file object as argument (`with open(path, "wb") as file, PdfPages(file) as pdf: ...`).

### `backend_ps.psDefs`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#backend-ps-psdefs "Link to this heading")

The `psDefs` module-level variable in `backend_ps` has been removed with no replacement.

### Automatic papersize selection in PostScript[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#automatic-papersize-selection-in-postscript "Link to this heading")

Setting `[rcParams["ps.papersize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ps.papersize#rcparam-ps-papersize) ` (default: `'letter'`) to `'auto'` or passing `papersize='auto'` to [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 is no longer supported. Either pass an explicit paper type name, or omit this parameter to use the default from the rcParam.

### `RendererAgg.tostring_rgb` and `FigureCanvasAgg.tostring_rgb`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#rendereragg-tostring-rgb-and-figurecanvasagg-tostring-rgb "Link to this heading")

... have been remove with no direct replacement. Consider using `buffer_rgba` instead, which should cover most use cases.

### `NavigationToolbar2QT.message` has been removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#navigationtoolbar2qt-message-has-been-removed "Link to this heading")

... with no replacement.

### `TexManager.texcache`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#texmanager-texcache "Link to this heading")

... is considered private and has been removed. The location of the cache directory is clarified in the doc-string.

### `cbook` API changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#cbook-api-changes "Link to this heading")

`cbook.Stack` has been removed with no replacement.

`Grouper.clean()` has been removed with no replacement. The Grouper class now cleans itself up automatically.

The _np\_load_ parameter of `cbook.get_sample_data` has been removed; [`get_sample_data`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
 now auto-loads numpy arrays. Use `get_sample_data(..., asfileobj=False)` instead to get the filename of the data file, which can then be passed to [`open`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)")
, if desired.

### Calling `paths.get_path_collection_extents` with empty _offsets_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#calling-paths-get-path-collection-extents-with-empty-offsets "Link to this heading")

Calling [`get_path_collection_extents`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.get_path_collection_extents "matplotlib.path.get_path_collection_extents")
 with an empty _offsets_ parameter has an ambiguous interpretation and is no longer allowed.

### `bbox.anchored()` with no explicit container[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#bbox-anchored-with-no-explicit-container "Link to this heading")

Not passing a _container_ argument to [`BboxBase.anchored`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.anchored "matplotlib.transforms.BboxBase.anchored")
 is no longer supported.

### `INVALID_NON_AFFINE`, `INVALID_AFFINE`, `INVALID` attributes of `TransformNode`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#invalid-non-affine-invalid-affine-invalid-attributes-of-transformnode "Link to this heading")

These attributes have been removed.

### `axes_grid1` API changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#axes-grid1-api-changes "Link to this heading")

`anchored_artists.AnchoredEllipse` has been removed. Instead, directly construct an [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")
, an [`AuxTransformBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AuxTransformBox "matplotlib.offsetbox.AuxTransformBox")
, and an [`Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
, as demonstrated in [Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)
.

The `axes_divider.AxesLocator` class has been removed. The `new_locator` method of divider instances now instead returns an opaque callable (which can still be passed to `ax.set_axes_locator`).

`axes_divider.Divider.locate` has been removed; use `Divider.new_locator(...)(ax, renderer)` instead.

`axes_grid.CbarAxesBase.toggle_label` has been removed. Instead, use standard methods for manipulating colorbar labels ([`Colorbar.set_label`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
) and tick labels ([`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
).

`inset_location.InsetPosition` has been removed; use [`inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 instead.

### `axisartist` API changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#axisartist-api-changes "Link to this heading")

The `axisartist.axes_grid` and `axisartist.axes_rgb` modules, which provide wrappers combining the functionality of [`axes_grid1`](https://matplotlib.org/stable/api/toolkits/axes_grid1.html#module-mpl_toolkits.axes_grid1 "mpl_toolkits.axes_grid1")
 and [`axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
, have been removed; directly use e.g. `AxesGrid(..., axes_class=axislines.Axes)` instead.

Calling an axisartist Axes to mean [`axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
 has been removed; explicitly call the method instead.

`floating_axes.GridHelperCurveLinear.get_data_boundary` has been removed. Use `grid_finder.extreme_finder(*[None] * 5)` to get the extremes of the grid.

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#development-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Documentation-specific custom Sphinx roles are now semi-public[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#documentation-specific-custom-sphinx-roles-are-now-semi-public "Link to this heading")

For third-party packages that derive types from Matplotlib, our use of custom roles may prevent Sphinx from building their docs. These custom Sphinx roles are now public solely for the purposes of use within projects that derive from Matplotlib types. See [`matplotlib.sphinxext.roles`](https://matplotlib.org/stable/api/sphinxext_roles.html#module-matplotlib.sphinxext.roles "matplotlib.sphinxext.roles")
 for details.

### Increase to minimum supported versions of dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.0.html#increase-to-minimum-supported-versions-of-dependencies "Link to this heading")

For Matplotlib 3.10, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 are being bumped:

| Dependency | min in mpl3.9 | min in mpl3.10 |
| --- | --- | --- |
| Python | 3.9 | 3.10 |

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [SPEC0](https://scientific-python.org/specs/spec-0000/)

On this page