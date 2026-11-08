[Skip to main content](https://matplotlib.org/stable/api/artist_api.html#main-content)

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
    

`matplotlib.artist`[#](https://matplotlib.org/stable/api/artist_api.html#module-matplotlib.artist "Link to this heading")

==========================================================================================================================

Inheritance Diagrams[#](https://matplotlib.org/stable/api/artist_api.html#inheritance-diagrams "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Inheritance diagram of matplotlib.axes.\_axes.Axes, matplotlib.axes.\_base.\_AxesBase, matplotlib.axis.Axis, matplotlib.axis.Tick, matplotlib.axis.XAxis, matplotlib.axis.XTick, matplotlib.axis.YAxis, matplotlib.axis.YTick, matplotlib.collections.AsteriskPolygonCollection, matplotlib.collections.CircleCollection, matplotlib.collections.Collection, matplotlib.collections.EllipseCollection, matplotlib.collections.EventCollection, matplotlib.collections.LineCollection, matplotlib.collections.PatchCollection, matplotlib.collections.PathCollection, matplotlib.collections.PolyCollection, matplotlib.collections.QuadMesh, matplotlib.collections.RegularPolyCollection, matplotlib.collections.StarPolygonCollection, matplotlib.collections.TriMesh, matplotlib.collections.\_CollectionWithSizes, matplotlib.contour.ContourSet, matplotlib.contour.QuadContourSet, matplotlib.figure.FigureBase, matplotlib.figure.Figure, matplotlib.figure.SubFigure, matplotlib.image.AxesImage, matplotlib.image.BboxImage, matplotlib.image.FigureImage, matplotlib.image.NonUniformImage, matplotlib.image.PcolorImage, matplotlib.image.\_ImageBase, matplotlib.legend.Legend, matplotlib.lines.Line2D, matplotlib.offsetbox.AnchoredOffsetbox, matplotlib.offsetbox.AnchoredText, matplotlib.offsetbox.AnnotationBbox, matplotlib.offsetbox.AuxTransformBox, matplotlib.offsetbox.DrawingArea, matplotlib.offsetbox.HPacker, matplotlib.offsetbox.OffsetBox, matplotlib.offsetbox.OffsetImage, matplotlib.offsetbox.PackerBase, matplotlib.offsetbox.PaddedBox, matplotlib.offsetbox.TextArea, matplotlib.offsetbox.VPacker, matplotlib.patches.Annulus, matplotlib.patches.Arc, matplotlib.patches.Arrow, matplotlib.patches.Circle, matplotlib.patches.CirclePolygon, matplotlib.patches.ConnectionPatch, matplotlib.patches.Ellipse, matplotlib.patches.FancyArrow, matplotlib.patches.FancyArrowPatch, matplotlib.patches.FancyBboxPatch, matplotlib.patches.Patch, matplotlib.patches.PathPatch, matplotlib.patches.Polygon, matplotlib.patches.Rectangle, matplotlib.patches.RegularPolygon, matplotlib.patches.Shadow, matplotlib.patches.StepPatch, matplotlib.patches.Wedge, matplotlib.projections.geo.AitoffAxes, matplotlib.projections.geo.GeoAxes, matplotlib.projections.geo.HammerAxes, matplotlib.projections.geo.LambertAxes, matplotlib.projections.geo.MollweideAxes, matplotlib.projections.polar.PolarAxes, matplotlib.projections.polar.RadialAxis, matplotlib.projections.polar.RadialTick, matplotlib.projections.polar.ThetaAxis, matplotlib.projections.polar.ThetaTick, matplotlib.quiver.Barbs, matplotlib.quiver.Quiver, matplotlib.quiver.QuiverKey, matplotlib.spines.Spine, matplotlib.table.Cell, matplotlib.table.Table, matplotlib.text.Annotation, matplotlib.text.Text, matplotlib.tri.TriContourSet

`Artist` class[#](https://matplotlib.org/stable/api/artist_api.html#artist-class "Link to this heading")

---------------------------------------------------------------------------------------------------------

class matplotlib.artist.Artist[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L110-L1475)
[#](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "Link to this definition")

Abstract base class for objects that render into a FigureCanvas.

Typically, all visible elements in a figure are subclasses of Artist.

### Interactive[#](https://matplotlib.org/stable/api/artist_api.html#interactive "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.add_callback`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.add_callback.html#matplotlib.artist.Artist.add_callback "matplotlib.artist.Artist.add_callback") | Add a callback function that will be called whenever one of the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>'s properties changes. |
| [`Artist.remove_callback`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove_callback.html#matplotlib.artist.Artist.remove_callback "matplotlib.artist.Artist.remove_callback") | Remove a callback based on its observer id. |
| [`Artist.pchanged`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.pchanged.html#matplotlib.artist.Artist.pchanged "matplotlib.artist.Artist.pchanged") | Call all of the registered callbacks. |
| [`Artist.get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib.artist.Artist.get_cursor_data "matplotlib.artist.Artist.get_cursor_data") | Return the cursor data for a given event. |
| [`Artist.format_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.format_cursor_data.html#matplotlib.artist.Artist.format_cursor_data "matplotlib.artist.Artist.format_cursor_data") | Return a string representation of _data_. |
| [`Artist.set_mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | Set whether this artist is queried for custom context information when the mouse cursor moves over it. |
| [`Artist.get_mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_mouseover.html#matplotlib.artist.Artist.get_mouseover "matplotlib.artist.Artist.get_mouseover") | Return whether this artist is queried for custom context information when the mouse cursor moves over it. |
| [`Artist.mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.mouseover.html#matplotlib.artist.Artist.mouseover "matplotlib.artist.Artist.mouseover") | Return whether this artist is queried for custom context information when the mouse cursor moves over it. |
| [`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains") | Test whether the artist contains the mouse event. |
| [`Artist.pick`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.pick.html#matplotlib.artist.Artist.pick "matplotlib.artist.Artist.pick") | Process a pick event. |
| [`Artist.pickable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.pickable.html#matplotlib.artist.Artist.pickable "matplotlib.artist.Artist.pickable") | Return whether the artist is pickable. |
| [`Artist.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | Define the picking behavior of the artist. |
| [`Artist.get_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_picker.html#matplotlib.artist.Artist.get_picker "matplotlib.artist.Artist.get_picker") | Return the picking behavior of the artist. |

### Clipping[#](https://matplotlib.org/stable/api/artist_api.html#clipping "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.set_clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | Set whether the artist uses clipping. |
| [`Artist.get_clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_clip_on.html#matplotlib.artist.Artist.get_clip_on "matplotlib.artist.Artist.get_clip_on") | Return whether the artist uses clipping. |
| [`Artist.set_clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | Set the artist's clip [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")<br>. |
| [`Artist.get_clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_clip_box.html#matplotlib.artist.Artist.get_clip_box "matplotlib.artist.Artist.get_clip_box") | Return the clipbox. |
| [`Artist.set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Set the artist's clip path. |
| [`Artist.get_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_clip_path.html#matplotlib.artist.Artist.get_clip_path "matplotlib.artist.Artist.get_clip_path") | Return the clip path. |

### Bulk Properties[#](https://matplotlib.org/stable/api/artist_api.html#bulk-properties "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update") | \[_Discouraged_\] Update this artist's properties from the dictionary _props_. |
| [`Artist.update_from`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update_from.html#matplotlib.artist.Artist.update_from "matplotlib.artist.Artist.update_from") | Copy properties from _other_ to _self_. |
| [`Artist.properties`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.properties.html#matplotlib.artist.Artist.properties "matplotlib.artist.Artist.properties") | Return a dictionary of all the properties of the artist. |
| [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set") | Set multiple properties at once. |

### Drawing[#](https://matplotlib.org/stable/api/artist_api.html#drawing "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib.artist.Artist.draw "matplotlib.artist.Artist.draw") | Draw the Artist (and its children) using the given renderer. |
| [`Artist.set_animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | Set whether the artist is intended to be used in an animation. |
| [`Artist.get_animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_animated.html#matplotlib.artist.Artist.get_animated "matplotlib.artist.Artist.get_animated") | Return whether the artist is animated. |
| [`Artist.set_alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | Set the alpha value used for blending - not supported on all backends. |
| [`Artist.get_alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_alpha.html#matplotlib.artist.Artist.get_alpha "matplotlib.artist.Artist.get_alpha") | Return the alpha value used for blending - not supported on all backends. |
| [`Artist.set_snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | Set the snapping behavior. |
| [`Artist.get_snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_snap.html#matplotlib.artist.Artist.get_snap "matplotlib.artist.Artist.get_snap") | Return the snap setting. |
| [`Artist.set_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | Set the artist's visibility. |
| [`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible") | Return the visibility. |
| [`Artist.zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.zorder.html#matplotlib.artist.Artist.zorder "matplotlib.artist.Artist.zorder") |     |
| [`Artist.set_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | Set the zorder for the artist. |
| [`Artist.get_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_zorder.html#matplotlib.artist.Artist.get_zorder "matplotlib.artist.Artist.get_zorder") | Return the artist's zorder. |
| [`Artist.set_agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | Set the agg filter. |
| [`Artist.set_sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | Set the sketch parameters. |
| [`Artist.get_sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_sketch_params.html#matplotlib.artist.Artist.get_sketch_params "matplotlib.artist.Artist.get_sketch_params") | Return the sketch parameters for the artist. |
| [`Artist.set_rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | Force rasterized (bitmap) drawing for vector graphics output. |
| [`Artist.get_rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_rasterized.html#matplotlib.artist.Artist.get_rasterized "matplotlib.artist.Artist.get_rasterized") | Return whether the artist is to be rasterized. |
| [`Artist.set_path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | Set the path effects. |
| [`Artist.get_path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_path_effects.html#matplotlib.artist.Artist.get_path_effects "matplotlib.artist.Artist.get_path_effects") |     |
| [`Artist.get_agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_agg_filter.html#matplotlib.artist.Artist.get_agg_filter "matplotlib.artist.Artist.get_agg_filter") | Return filter function to be used for agg filter. |
| [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent") | Get the artist's bounding box in display space, ignoring clipping. |
| [`Artist.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "matplotlib.artist.Artist.get_tightbbox") | Get the artist's bounding box in display space, taking clipping into account. |
| [`Artist.get_transformed_clip_path_and_affine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_transformed_clip_path_and_affine.html#matplotlib.artist.Artist.get_transformed_clip_path_and_affine "matplotlib.artist.Artist.get_transformed_clip_path_and_affine") | Return the clip path with the non-affine part of its transformation applied, and the remaining affine part of its transformation. |

### Figure and Axes[#](https://matplotlib.org/stable/api/artist_api.html#figure-and-axes "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove") | Remove the artist from the figure if possible. |
| [`Artist.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.axes.html#matplotlib.artist.Artist.axes "matplotlib.artist.Artist.axes") | The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> instance the artist resides in, or _None_. |
| [`Artist.set_figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | Set the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")<br> instance the artist belongs to. |
| [`Artist.get_figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_figure.html#matplotlib.artist.Artist.get_figure "matplotlib.artist.Artist.get_figure") | Return the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")<br> instance the artist belongs to. |
| [`Artist.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.figure.html#matplotlib.artist.Artist.figure "matplotlib.artist.Artist.figure") | The (Sub)Figure that the artist is on. |

### Children[#](https://matplotlib.org/stable/api/artist_api.html#children "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.get_children`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_children.html#matplotlib.artist.Artist.get_children "matplotlib.artist.Artist.get_children") | Return a list of the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>s of this [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>. |
| [`Artist.findobj`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.findobj.html#matplotlib.artist.Artist.findobj "matplotlib.artist.Artist.findobj") | Find artist objects. |

### Transform[#](https://matplotlib.org/stable/api/artist_api.html#transform "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.set_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | Set the artist transform. |
| [`Artist.get_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_transform.html#matplotlib.artist.Artist.get_transform "matplotlib.artist.Artist.get_transform") | Return the [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")<br> instance used by this artist. |
| [`Artist.is_transform_set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.is_transform_set.html#matplotlib.artist.Artist.is_transform_set "matplotlib.artist.Artist.is_transform_set") | Return whether the Artist has an explicitly set transform. |

### Units[#](https://matplotlib.org/stable/api/artist_api.html#units "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.convert_xunits`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.convert_xunits.html#matplotlib.artist.Artist.convert_xunits "matplotlib.artist.Artist.convert_xunits") | Convert _x_ using the unit type of the xaxis. |
| [`Artist.convert_yunits`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.convert_yunits.html#matplotlib.artist.Artist.convert_yunits "matplotlib.artist.Artist.convert_yunits") | Convert _y_ using the unit type of the yaxis. |
| [`Artist.have_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.have_units.html#matplotlib.artist.Artist.have_units "matplotlib.artist.Artist.have_units") | Return whether units are set on any axis. |

### Metadata[#](https://matplotlib.org/stable/api/artist_api.html#metadata "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.set_gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | Set the (group) id for the artist. |
| [`Artist.get_gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_gid.html#matplotlib.artist.Artist.get_gid "matplotlib.artist.Artist.get_gid") | Return the group id. |
| [`Artist.set_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | Set a label that will be displayed in the legend. |
| [`Artist.get_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_label.html#matplotlib.artist.Artist.get_label "matplotlib.artist.Artist.get_label") | Return the label used for this artist in the legend. |
| [`Artist.set_url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | Set the url for the artist. |
| [`Artist.get_url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_url.html#matplotlib.artist.Artist.get_url "matplotlib.artist.Artist.get_url") | Return the url. |

### Miscellaneous[#](https://matplotlib.org/stable/api/artist_api.html#miscellaneous "Link to this heading")

|     |     |
| --- | --- |
| [`Artist.sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges") | `x` and `y` sticky edge lists for autoscaling. |
| [`Artist.set_in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | Set if artist is to be included in layout calculations, E.g. |
| [`Artist.get_in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_in_layout.html#matplotlib.artist.Artist.get_in_layout "matplotlib.artist.Artist.get_in_layout") | Return boolean flag, `True` if artist is included in layout calculations. |
| [`Artist.stale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.stale.html#matplotlib.artist.Artist.stale "matplotlib.artist.Artist.stale") | Whether the artist is 'stale' and needs to be re-drawn for the output to match the internal state of the artist. |

Functions[#](https://matplotlib.org/stable/api/artist_api.html#functions "Link to this heading")

-------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`allow_rasterization`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.allow_rasterization.html#matplotlib.artist.allow_rasterization "matplotlib.artist.allow_rasterization") | Decorator for Artist.draw method. |
| [`get`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.get.html#matplotlib.artist.get "matplotlib.artist.get") | Return the value of an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>'s _property_, or print all of them. |
| [`getp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.getp.html#matplotlib.artist.getp "matplotlib.artist.getp") | Return the value of an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>'s _property_, or print all of them. |
| [`setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp") | Set one or more properties on an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>, or list allowed values. |
| [`kwdoc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.kwdoc.html#matplotlib.artist.kwdoc "matplotlib.artist.kwdoc") | Inspect an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> class (using [`ArtistInspector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector "matplotlib.artist.ArtistInspector")<br>) and return information about its settable properties and their current values. |
| [`ArtistInspector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.ArtistInspector.html#matplotlib.artist.ArtistInspector "matplotlib.artist.ArtistInspector") | A helper class to inspect an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> and return information about its settable properties and their current values. |

On this page