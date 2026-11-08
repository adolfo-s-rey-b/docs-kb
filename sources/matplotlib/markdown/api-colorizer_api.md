[Skip to main content](https://matplotlib.org/stable/api/colorizer_api.html#main-content)

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
    

`matplotlib.colorizer`[#](https://matplotlib.org/stable/api/colorizer_api.html#module-matplotlib.colorizer "Link to this heading")

===================================================================================================================================

The Colorizer class which handles the data to color pipeline via a normalization and a colormap.

Provisional status of colorizer

The `colorizer` module and classes in this file are considered provisional and may change at any time without a deprecation period.

See also

[Colormap reference](https://matplotlib.org/stable/gallery/color/colormap_reference.html)
 for a list of builtin colormaps.

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
 for examples of how to make colormaps.

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
 for an in-depth discussion of choosing colormaps.

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)
 for more details about data normalization.

class matplotlib.colorizer.Colorizer(_cmap\=None_, _norm\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L38-L313)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Data to color pipeline.

This pipeline is accessible via [`Colorizer.to_rgba`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.to_rgba "matplotlib.colorizer.Colorizer.to_rgba")
 and executed via the [`Colorizer.norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.norm "matplotlib.colorizer.Colorizer.norm")
 and [`Colorizer.cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.cmap "matplotlib.colorizer.Colorizer.cmap")
 attributes.

Parameters:

**cmap: colorbar.Colorbar or str or None, default: None**

The colormap used to color data.

**norm: colors.Normalize or str or None, default: None**

The normalization used to normalize the data

autoscale(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L192-L201)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.autoscale "Link to this definition")

Autoscale the scalar limits on the norm instance using the current array

autoscale\_None(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L203-L212)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.autoscale_None "Link to this definition")

Autoscale the scalar limits on the norm instance using the current array, changing only limits that are None

changed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L283-L289)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.changed "Link to this definition")

Call this whenever the mappable is changed to notify all the callbackSM listeners to the 'changed' signal.

property clip[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.clip "Link to this definition")

property cmap[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.cmap "Link to this definition")

get\_clim()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L277-L281)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.get_clim "Link to this definition")

Return the values (min, max) that are mapped to the colormap limits.

property norm[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.norm "Link to this definition")

set\_clim(_vmin\=None_, _vmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L240-L275)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.set_clim "Link to this definition")

Set the norm limits for image scaling.

Parameters:

**vmin, vmax**float

The limits.

For scalar data, the limits may also be passed as a tuple (_vmin_, _vmax_) single positional argument.

to\_rgba(_x_, _alpha\=None_, _bytes\=False_, _norm\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L108-L147)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.to_rgba "Link to this definition")

Return a normalized RGBA array corresponding to _x_.

In the normal case, _x_ is a 1D or 2D sequence of scalars, and the corresponding [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of RGBA values will be returned, based on the norm and colormap set for this Colorizer.

There is one special case, for handling images that are already RGB or RGBA, such as might have been read from an image file. If _x_ is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 with 3 dimensions, and the last dimension is either 3 or 4, then it will be treated as an RGB or RGBA array, and no mapping will be done. The array can be [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
, or it can be floats with values in the 0-1 range; otherwise a ValueError will be raised. Any NaNs or masked elements will be set to 0 alpha. If the last dimension is 3, the _alpha_ kwarg (defaulting to 1) will be used to fill in the transparency. If the last dimension is 4, the _alpha_ kwarg is ignored; it does not replace the preexisting alpha. A ValueError will be raised if the third dimension is other than 3 or 4.

In either case, if _bytes_ is _False_ (default), the RGBA array will be floats in the 0-1 range; if it is _True_, the returned RGBA array will be [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 in the 0 to 255 range.

If norm is False, no normalization of the input data is performed, and it is assumed to be in the range (0-1).

property vmax[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.vmax "Link to this definition")

property vmin[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer.vmin "Link to this definition")

class matplotlib.colorizer.ColorizingArtist(_colorizer_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L697-L730)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "Link to this definition")

Bases: [`_ScalarMappable`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable "matplotlib.colorizer._ScalarMappable")
, [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

Base class for artists that make map data to color using a [`colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
.

The [`colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 applies data normalization before returning RGBA colors from a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
.

Parameters:

**colorizer**[`colorizer.Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")

property colorizer[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist.colorizer "Link to this definition")

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1044-L1061)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _array\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist.set "Link to this definition")

Set multiple properties at once.

a.set(a\=A, b\=B, c\=C)

is equivalent to

a.set\_a(A)
a.set\_b(B)
a.set\_c(C)

In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.

The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.

Supported properties are

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.colorizer.\_ColorizerInterface[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L316-L515)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Base class that contains the interface to [`Colorizer`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.Colorizer "matplotlib.colorizer.Colorizer")
 objects from a [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 or [`cm.ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
.

Note: This class only contain functions that interface the .colorizer attribute. Other functions that as shared between [`ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 and [`cm.ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 are not included.

autoscale()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L436-L441)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.autoscale "Link to this definition")

Autoscale the scalar limits on the norm instance using the current array

autoscale\_None()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L443-L448)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.autoscale_None "Link to this definition")

Autoscale the scalar limits on the norm instance using the current array, changing only limits that are None

property cmap[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.cmap "Link to this definition")

property colorbar[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.colorbar "Link to this definition")

The last colorbar associated with this object. May be None

get\_alpha()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L384-L388)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.get_alpha "Link to this definition")

get\_clim()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L360-L364)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.get_clim "Link to this definition")

Return the values (min, max) that are mapped to the colormap limits.

get\_cmap()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L398-L400)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.get_cmap "Link to this definition")

Return the [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 instance.

property norm[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.norm "Link to this definition")

set\_clim(_vmin\=None_, _vmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L366-L382)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "Link to this definition")

Set the norm limits for image scaling.

Parameters:

**vmin, vmax**float

The limits.

For scalar data, the limits may also be passed as a tuple (_vmin_, _vmax_) as a single positional argument.

set\_cmap(_cmap_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L402-L410)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "Link to this definition")

Set the colormap for luminance data.

Parameters:

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 or str or None

set\_norm(_norm_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L420-L434)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "Link to this definition")

Set the normalization instance.

Parameters:

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 or str or None

Notes

If there are any colorbars using the mappable for this norm, setting the norm of the mappable will reset the norm, locator, and formatters on the colorbar to default.

to\_rgba(_x_, _alpha\=None_, _bytes\=False_, _norm\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L328-L358)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.to_rgba "Link to this definition")

Return a normalized RGBA array corresponding to _x_.

In the normal case, _x_ is a 1D or 2D sequence of scalars, and the corresponding [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of RGBA values will be returned, based on the norm and colormap set for this Colorizer.

There is one special case, for handling images that are already RGB or RGBA, such as might have been read from an image file. If _x_ is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 with 3 dimensions, and the last dimension is either 3 or 4, then it will be treated as an RGB or RGBA array, and no mapping will be done. The array can be [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
, or it can be floats with values in the 0-1 range; otherwise a ValueError will be raised. Any NaNs or masked elements will be set to 0 alpha. If the last dimension is 3, the _alpha_ kwarg (defaulting to 1) will be used to fill in the transparency. If the last dimension is 4, the _alpha_ kwarg is ignored; it does not replace the preexisting alpha. A ValueError will be raised if the third dimension is other than 3 or 4.

In either case, if _bytes_ is _False_ (default), the RGBA array will be floats in the 0-1 range; if it is _True_, the returned RGBA array will be [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
 in the 0 to 255 range.

If norm is False, no normalization of the input data is performed, and it is assumed to be in the range (0-1).

class matplotlib.colorizer.\_ScalarMappable(_norm\=None_, _cmap\=None_, _\*_, _colorizer\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L518-L630)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable "Link to this definition")

Bases: [`_ColorizerInterface`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface "matplotlib.colorizer._ColorizerInterface")

A mixin class to map one or multiple sets of scalar data to RGBA.

The ScalarMappable applies data normalization before returning RGBA colors from the given [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
.

Parameters:

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 (or subclass thereof) or str or None

The normalizing object which scales data, typically into the interval `[0, 1]`. If a [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
, a [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 subclass is dynamically generated based on the scale with the corresponding name. If _None_, _norm_ defaults to a _colors.Normalize_ object which initializes its scaling based on the first data processed.

**cmap**str or [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")

The colormap used to map normalized data values to RGBA colors.

changed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L604-L610)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.changed "Link to this definition")

Call this whenever the mappable is changed to notify all the callbackSM listeners to the 'changed' signal.

get\_array()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L595-L602)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.get_array "Link to this definition")

Return the array of values, that are mapped to colors.

The base class [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 does not make any assumptions on the dimensionality and shape of the array.

set\_array(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colorizer.py#L562-L593)
[#](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "Link to this definition")

Set the value array from array-like _A_.

Parameters:

**A**array-like or None

The values that are mapped to colors.

The base class [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 does not make any assumptions on the dimensionality and shape of the value array _A_.

On this page