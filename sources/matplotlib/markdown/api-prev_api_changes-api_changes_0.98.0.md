[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#main-content)

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
    

Changes for 0.98.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#changes-for-0-98-0 "Link to this heading")

============================================================================================================================================

*   [`matplotlib.image.imread()`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imread "matplotlib.image.imread")
     now no longer always returns RGBA data---if the image is luminance or RGB, it will return a MxN or MxNx3 array if possible. Also uint8 is no longer always forced to float.
    
*   Rewrote the [`matplotlib.cm.ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
     callback infrastructure to use [`matplotlib.cbook.CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
     rather than custom callback handling. Any users of `matplotlib.cm.ScalarMappable.add_observer` of the [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
     should use the `matplotlib.cm.ScalarMappable.callbacksSM` [`CallbackRegistry`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry "matplotlib.cbook.CallbackRegistry")
     instead.
    
*   New axes function and Axes method provide control over the plot color cycle: `matplotlib.axes.set_default_color_cycle` and `matplotlib.axes.Axes.set_color_cycle`.
    
*   Matplotlib now requires Python 2.4, so [`matplotlib.cbook`](https://matplotlib.org/stable/api/cbook_api.html#module-matplotlib.cbook "matplotlib.cbook")
     will no longer provide [`set`](https://docs.python.org/3/library/stdtypes.html#set "(in Python v3.14)")
    , [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "(in Python v3.14)")
    , [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "(in Python v3.14)")
     or `izip` compatibility functions.
    
*   In Numpy 1.0, bins are specified by the left edges only. The axes method [`matplotlib.axes.Axes.hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     now uses future Numpy 1.3 semantics for histograms. Providing `binedges`, the last value gives the upper-right edge now, which was implicitly set to +infinity in Numpy 1.0. This also means that the last bin doesn't contain upper outliers any more by default.
    
*   New axes method and pyplot function, [`hexbin()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin "matplotlib.pyplot.hexbin")
    , is an alternative to [`scatter()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
     for large datasets. It makes something like a [`pcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor")
     of a 2-D histogram, but uses hexagonal bins.
    
*   New kwarg, `symmetric`, in [`matplotlib.ticker.MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
     allows one require an axis to be centered around zero.
    
*   Toolkits must now be imported from `mpl_toolkits` (not `matplotlib.toolkits`)
    

Notes about the transforms refactoring[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#notes-about-the-transforms-refactoring "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A major new feature of the 0.98 series is a more flexible and extensible transformation infrastructure, written in Python/Numpy rather than a custom C extension.

The primary goal of this refactoring was to make it easier to extend matplotlib to support new kinds of projections. This is mostly an internal improvement, and the possible user-visible changes it allows are yet to come.

See [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
 for a description of the design of the new transformation framework.

For efficiency, many of these functions return views into Numpy arrays. This means that if you hold on to a reference to them, their contents may change. If you want to store a snapshot of their current values, use the Numpy array method copy().

The view intervals are now stored only in one place -- in the [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance, not in the locator instances as well. This means locators must get their limits from their [`matplotlib.axis.Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
, which in turn looks up its limits from the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. If a locator is used temporarily and not assigned to an Axis or Axes, (e.g., in [`matplotlib.contour`](https://matplotlib.org/stable/api/contour_api.html#module-matplotlib.contour "matplotlib.contour")
), a dummy axis must be created to store its bounds. Call [`matplotlib.ticker.TickHelper.create_dummy_axis()`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper.create_dummy_axis "matplotlib.ticker.TickHelper.create_dummy_axis")
 to do so.

The functionality of `Pbox` has been merged with [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
. Its methods now all return copies rather than modifying in place.

The following lists many of the simple changes necessary to update code from the old transformation framework to the new one. In particular, methods that return a copy are named with a verb in the past tense, whereas methods that alter an object in place are named with a verb in the present tense.

### [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-transforms "Link to this heading")

| Old method | New method |
| --- | --- |
| `Bbox.get_bounds` | [`transforms.Bbox.bounds`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.bounds "matplotlib.transforms.Bbox.bounds") |
| `Bbox.width` | [`transforms.Bbox.width`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.width "matplotlib.transforms.BboxBase.width") |
| `Bbox.height` | [`transforms.Bbox.height`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.height "matplotlib.transforms.BboxBase.height") |
| `Bbox.intervalx().get_bounds()` `Bbox.intervalx().set_bounds()` | [`transforms.Bbox.intervalx`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.intervalx "matplotlib.transforms.Bbox.intervalx")<br> \[It is now a property.\] |
| `Bbox.intervaly().get_bounds()` `Bbox.intervaly().set_bounds()` | [`transforms.Bbox.intervaly`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.intervaly "matplotlib.transforms.Bbox.intervaly")<br> \[It is now a property.\] |
| `Bbox.xmin` | [`transforms.Bbox.x0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x0 "matplotlib.transforms.Bbox.x0")<br> or [`transforms.Bbox.xmin`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmin "matplotlib.transforms.BboxBase.xmin")<br> [\[1\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id5) |
| `Bbox.ymin` | [`transforms.Bbox.y0`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y0 "matplotlib.transforms.Bbox.y0")<br> or [`transforms.Bbox.ymin`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymin "matplotlib.transforms.BboxBase.ymin")<br> [\[1\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id5) |
| `Bbox.xmax` | [`transforms.Bbox.x1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x1 "matplotlib.transforms.Bbox.x1")<br> or [`transforms.Bbox.xmax`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.xmax "matplotlib.transforms.BboxBase.xmax")<br> [\[1\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id5) |
| `Bbox.ymax` | [`transforms.Bbox.y1`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y1 "matplotlib.transforms.Bbox.y1")<br> or [`transforms.Bbox.ymax`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.ymax "matplotlib.transforms.BboxBase.ymax")<br> [\[1\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id5) |
| `Bbox.overlaps(bboxes)` | [`Bbox.count_overlaps(bboxes)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.count_overlaps "matplotlib.transforms.BboxBase.count_overlaps") |
| `bbox_all(bboxes)` | [`Bbox.union(bboxes)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.union "matplotlib.transforms.BboxBase.union")<br> \[It is a staticmethod.\] |
| `lbwh_to_bbox(l, b, w, h)` | [`Bbox.from_bounds(x0, y0, w, h)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_bounds "matplotlib.transforms.Bbox.from_bounds")<br> \[It is a staticmethod.\] |
| `inverse_transform_bbox(trans, bbox)` | `bbox.inverse_transformed(trans)` |
| `Interval.contains_open(v)` | [`interval_contains_open(tuple, v)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.interval_contains_open "matplotlib.transforms.interval_contains_open") |
| `Interval.contains(v)` | [`interval_contains(tuple, v)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.interval_contains "matplotlib.transforms.interval_contains") |
| `identity_transform()` | [`transforms.IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform") |
| `blend_xy_sep_transform(xtrans, ytrans)` | [`blended_transform_factory(xtrans, ytrans)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory") |
| `scale_transform(xs, ys)` | [`Affine2D().scale(xs[, ys])`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale") |
| `get_bbox_transform(boxin, boxout)` | [`BboxTransform(boxin, boxout)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransform "matplotlib.transforms.BboxTransform")<br> or [`BboxTransformFrom(boxin)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformFrom "matplotlib.transforms.BboxTransformFrom")<br> or [`BboxTransformTo(boxout)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo") |
| `Transform.seq_xy_tup(points)` | [`Transform.transform(points)`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform") |
| `Transform.inverse_xy_tup(points)` | [`Transform.inverted()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")<br>.transform(points) |

### [`matplotlib.axes`](https://matplotlib.org/stable/api/axes_api.html#module-matplotlib.axes "matplotlib.axes")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-axes "Link to this heading")

| Old method | New method |
| --- | --- |
| `Axes.get_position()` | [`matplotlib.axes.Axes.get_position()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html#matplotlib.axes.Axes.get_position "matplotlib.axes.Axes.get_position")<br> [\[2\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id9) |
| `Axes.set_position()` | [`matplotlib.axes.Axes.set_position()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position")<br> [\[3\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id10) |
| `Axes.toggle_log_lineary()` | [`matplotlib.axes.Axes.set_yscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")<br> [\[4\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id11) |
| `Subplot` class | removed |

The `Polar` class has moved to [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
.

### [`matplotlib.artist`](https://matplotlib.org/stable/api/artist_api.html#module-matplotlib.artist "matplotlib.artist")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-artist "Link to this heading")

| Old method | New method |
| --- | --- |
| `Artist.set_clip_path(path)` | `Artist.set_clip_path(path, transform)` [\[5\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id13) |

### [`matplotlib.collections`](https://matplotlib.org/stable/api/collections_api.html#module-matplotlib.collections "matplotlib.collections")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-collections "Link to this heading")

| Old method | New method |
| --- | --- |
| _linestyle_ | _linestyles_ [\[6\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id15) |

### [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-colors "Link to this heading")

| Old method | New method |
| --- | --- |
| `ColorConvertor.to_rgba_list(c)` | `colors.to_rgba_array(c)` \[[`matplotlib.colors.to_rgba_array()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "matplotlib.colors.to_rgba_array")<br> returns an Nx4 NumPy array of RGBA color quadruples.\] |

### [`matplotlib.contour`](https://matplotlib.org/stable/api/contour_api.html#module-matplotlib.contour "matplotlib.contour")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-contour "Link to this heading")

| Old method | New method |
| --- | --- |
| `Contour._segments` | `matplotlib.contour.Contour.get_paths` \[Returns a list of [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> instances.\] |

### [`matplotlib.figure`](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure "matplotlib.figure")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-figure "Link to this heading")

| Old method | New method |
| --- | --- |
| `Figure.dpi.get()` `Figure.dpi.set()` | [`matplotlib.figure.Figure.dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.dpi.html#matplotlib.figure.Figure.dpi "matplotlib.figure.Figure.dpi")<br> _(a property)_ |

### [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-patches "Link to this heading")

| Old method | New method |
| --- | --- |
| `Patch.get_verts()` | [`matplotlib.patches.Patch.get_path()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.get_path "matplotlib.patches.Patch.get_path")<br> \[Returns a [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")<br> instance\] |

### [`matplotlib.backend_bases`](https://matplotlib.org/stable/api/backend_bases_api.html#module-matplotlib.backend_bases "matplotlib.backend_bases")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#matplotlib-backend-bases "Link to this heading")

| Old method | New method |
| --- | --- |
| `GraphicsContext.set_clip_rectangle(tuple)` | [`GraphicsContext.set_clip_rectangle(bbox)`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_clip_rectangle "matplotlib.backend_bases.GraphicsContextBase.set_clip_rectangle") |
| `GraphicsContext.get_clip_path()` | [`GraphicsContext.get_clip_path()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.get_clip_path "matplotlib.backend_bases.GraphicsContextBase.get_clip_path")<br> [\[7\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id18) |
| `GraphicsContext.set_clip_path()` | [`GraphicsContext.set_clip_path()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase.set_clip_path "matplotlib.backend_bases.GraphicsContextBase.set_clip_path")<br> [\[8\]](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#id19) |

### [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_0.98.0.html#rendererbase "Link to this heading")

New methods:

*   [`draw_path(self, gc, path, transform, rgbFace)`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
    
*   [`draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace)`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_markers "matplotlib.backend_bases.RendererBase.draw_markers")
    
*   [`draw_path_collection(self, master_transform, cliprect, clippath, clippath_trans, paths, all_transforms, offsets, offsetTrans, facecolors, edgecolors, linewidths, linestyles, antialiaseds)`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path_collection "matplotlib.backend_bases.RendererBase.draw_path_collection")
     _\[optional\]_
    

Changed methods:

*   `draw_image(self, x, y, im, bbox)` is now [`draw_image(self, x, y, im, bbox, clippath, clippath_trans)`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_image "matplotlib.backend_bases.RendererBase.draw_image")
    

Removed methods:

*   `draw_arc`
    
*   `draw_line_collection`
    
*   `draw_line`
    
*   `draw_lines`
    
*   `draw_point`
    
*   `draw_quad_mesh`
    
*   `draw_poly_collection`
    
*   `draw_polygon`
    
*   `draw_rectangle`
    
*   `draw_regpoly_collection`
    

On this page