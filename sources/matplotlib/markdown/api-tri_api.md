[Skip to main content](https://matplotlib.org/stable/api/tri_api.html#main-content)

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
    

`matplotlib.tri`[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib-tri "Link to this heading")

==========================================================================================================

Unstructured triangular grid functions.

class matplotlib.tri.Triangulation(_x_, _y_, _triangles\=None_, _mask\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L8-L247)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "Link to this definition")

An unstructured triangular grid consisting of npoints points and ntri triangles. The triangles can either be specified by the user or automatically generated using a Delaunay triangulation.

Parameters:

**x, y**(npoints,) array-like

Coordinates of grid points.

**triangles**(ntri, 3) array-like of int, optional

For each triangle, the indices of the three points that make up the triangle, ordered in an anticlockwise manner. If not specified, the Delaunay triangulation is calculated.

**mask**(ntri,) array-like of bool, optional

Which triangles are masked out.

Attributes:

**triangles**(ntri, 3) array of int

For each triangle, the indices of the three points that make up the triangle, ordered in an anticlockwise manner. If you want to take the _mask_ into account, use [`get_masked_triangles`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_masked_triangles "matplotlib.tri.Triangulation.get_masked_triangles")
 instead.

**mask**(ntri, 3) array of bool or None

Masked out triangles.

**is\_delaunay**bool

Whether the Triangulation is a calculated Delaunay triangulation (where _triangles_ was not specified) or not.

Notes

For a Triangulation to be valid it must not have duplicate points, triangles formed from colinear points, or overlapping triangles.

calculate\_plane\_coefficients(_z_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L93-L101)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.calculate_plane_coefficients "Link to this definition")

Calculate plane equation coefficients for all unmasked triangles from the point (x, y) coordinates and specified z-array of shape (npoints). The returned array has shape (npoints, 3) and allows z-value at (x, y) position in triangle tri to be calculated using `z = array[tri, 0] * x  + array[tri, 1] * y + array[tri, 2]`.

property edges[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.edges "Link to this definition")

Return integer array of shape (nedges, 2) containing all edges of non-masked triangles.

Each row defines an edge by its start point index and end point index. Each edge appears only once, i.e. for an edge between points _i_ and _j_, there will only be either _(i, j)_ or _(j, i)_.

get\_cpp\_triangulation()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L117-L131)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_cpp_triangulation "Link to this definition")

Return the underlying C++ Triangulation object, creating it if necessary.

static get\_from\_args\_and\_kwargs(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L142-L168)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_from_args_and_kwargs "Link to this definition")

Return a Triangulation object from the args and kwargs, and the remaining args and kwargs with the consumed values removed.

There are two alternatives: either the first argument is a Triangulation object, in which case it is returned, or the args and kwargs are sufficient to create a new Triangulation to return. In the latter case, see Triangulation.\_\_init\_\_ for the possible args and kwargs.

get\_masked\_triangles()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L133-L140)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_masked_triangles "Link to this definition")

Return an array of triangles taking the mask into account.

get\_trifinder()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L193-L203)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_trifinder "Link to this definition")

Return the default [`matplotlib.tri.TriFinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriFinder "matplotlib.tri.TriFinder")
 of this triangulation, creating it if necessary. This allows the same TriFinder object to be easily shared.

property neighbors[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.neighbors "Link to this definition")

Return integer array of shape (ntri, 3) containing neighbor triangles.

For each triangle, the indices of the three triangles that share the same edges, or -1 if there is no such neighboring triangle. `neighbors[i, j]` is the triangle that is the neighbor to the edge from point index `triangles[i, j]` to point index `triangles[i, (j+1)%3]`.

set\_mask(_mask_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triangulation.py#L220-L247)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "Link to this definition")

Set or clear the mask array.

Parameters:

**mask**None or bool array of length ntri

class matplotlib.tri.TriContourSet(_ax_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_tricontour.py#L8-L79)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "Link to this definition")

Bases: [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")

Create and store a set of contour lines or filled regions for a triangular grid.

This class is typically not instantiated directly by the user but by [`tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
 and [`tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf")
.

Attributes:

**levels**array

The values of the contour levels.

**layers**array

Same as levels for line contours; half-way between levels for filled contours. See `ContourSet._process_colors`.

Draw triangular grid contour lines or filled regions, depending on whether keyword arg _filled_ is False (default) or True.

The first argument of the initializer must be an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object. The remaining arguments and keyword arguments are described in the docstring of [`tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _antialiased\=<UNSET>_, _array\=<UNSET>_, _capstyle\=<UNSET>_, _clim\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _cmap\=<UNSET>_, _color\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _gid\=<UNSET>_, _hatch\=<UNSET>_, _hatch\_linewidth\=<UNSET>_, _hatchcolor\=<UNSET>_, _in\_layout\=<UNSET>_, _joinstyle\=<UNSET>_, _label\=<UNSET>_, _linestyle\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _norm\=<UNSET>_, _offset\_transform\=<UNSET>_, _offsets\=<UNSET>_, _path\_effects\=<UNSET>_, _paths\=<UNSET>_, _picker\=<UNSET>_, _pickradius\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _urls\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet.set "Link to this definition")

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
> | [`alpha`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_alpha "matplotlib.collections.Collection.set_alpha") | array-like or float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`antialiased`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`aa`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased")<br> or [`antialiaseds`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_antialiased "matplotlib.collections.Collection.set_antialiased") | bool or list of bools |
> | [`array`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ScalarMappable.set_array "matplotlib.colorizer._ScalarMappable.set_array") | array-like or None |
> | [`capstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_capstyle "matplotlib.collections.Collection.set_capstyle") | [`CapStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.CapStyle "matplotlib._enums.CapStyle")<br> or {'butt', 'projecting', 'round'} |
> | [`clim`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_clim "matplotlib.colorizer._ColorizerInterface.set_clim") | (vmin: float, vmax: float) |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`cmap`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_cmap "matplotlib.colorizer._ColorizerInterface.set_cmap") | [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br> or str or None |
> | [`color`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_color "matplotlib.collections.Collection.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of RGBA tuples |
> | [`edgecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`ec`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor")<br> or [`edgecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_edgecolor "matplotlib.collections.Collection.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'face' |
> | [`facecolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`facecolors`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_facecolor "matplotlib.collections.Collection.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`hatch`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch "matplotlib.collections.Collection.set_hatch") | {'/', '\\', '\|', '-', '+', 'x', 'o', 'O', '.', '\*'} |
> | [`hatch_linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatch_linewidth "matplotlib.collections.Collection.set_hatch_linewidth") | unknown |
> | [`hatchcolor`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_hatchcolor "matplotlib.collections.Collection.set_hatchcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> or 'edge' |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`joinstyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_joinstyle "matplotlib.collections.Collection.set_joinstyle") | [`JoinStyle`](https://matplotlib.org/stable/api/_enums_api.html#matplotlib._enums.JoinStyle "matplotlib._enums.JoinStyle")<br> or {'miter', 'round', 'bevel'} |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linestyle`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`dashes`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`linestyles`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle")<br> or [`ls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linestyle "matplotlib.collections.Collection.set_linestyle") | {'-', '--', '-.', ':', '', ...} or (offset, on-off-seq) or list thereof |
> | [`linewidth`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`linewidths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth")<br> or [`lw`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_linewidth "matplotlib.collections.Collection.set_linewidth") | float or list of floats |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`norm`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer._ColorizerInterface.set_norm "matplotlib.colorizer._ColorizerInterface.set_norm") | [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> or str or None |
> | [`offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")<br> or [`transOffset`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offsets "matplotlib.collections.Collection.set_offsets") | (N, 2) or (2,) array-like |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`paths`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_paths "matplotlib.collections.Collection.set_paths") | unknown |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`pickradius`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_pickradius "matplotlib.collections.Collection.set_pickradius") | float |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`urls`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_urls "matplotlib.collections.Collection.set_urls") | list of str or None |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

class matplotlib.tri.TriFinder(_triangulation_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_trifinder.py#L7-L24)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriFinder "Link to this definition")

Abstract base class for classes used to find the triangles of a Triangulation in which (x, y) points lie.

Rather than instantiate an object of a class derived from TriFinder, it is usually better to use the function [`Triangulation.get_trifinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_trifinder "matplotlib.tri.Triangulation.get_trifinder")
.

Derived classes implement \_\_call\_\_(x, y) where x and y are array-like point coordinates of the same shape.

class matplotlib.tri.TrapezoidMapTriFinder(_triangulation_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_trifinder.py#L27-L96)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TrapezoidMapTriFinder "Link to this definition")

Bases: [`TriFinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriFinder "matplotlib.tri._trifinder.TriFinder")

[`TriFinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriFinder "matplotlib.tri.TriFinder")
 class implemented using the trapezoid map algorithm from the book "Computational Geometry, Algorithms and Applications", second edition, by M. de Berg, M. van Kreveld, M. Overmars and O. Schwarzkopf.

The triangulation must be valid, i.e. it must not have duplicate points, triangles formed from colinear points, or overlapping triangles. The algorithm has some tolerance to triangles formed from colinear points, but this should not be relied upon.

class matplotlib.tri.TriInterpolator(_triangulation_, _z_, _trifinder\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triinterpolate.py#L15-L229)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriInterpolator "Link to this definition")

Abstract base class for classes used to interpolate on a triangular grid.

Derived classes implement the following methods:

*   `__call__(x, y)`, where x, y are array-like point coordinates of the same shape, and that returns a masked array of the same shape containing the interpolated z-values.
    
*   `gradient(x, y)`, where x, y are array-like point coordinates of the same shape, and that returns a list of 2 masked arrays of the same shape containing the 2 derivatives of the interpolator (derivatives of interpolated z values with respect to x and y).
    

class matplotlib.tri.LinearTriInterpolator(_triangulation_, _z_, _trifinder\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triinterpolate.py#L232-L283)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator "Link to this definition")

Bases: [`TriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriInterpolator "matplotlib.tri._triinterpolate.TriInterpolator")

Linear interpolator on a triangular grid.

Each triangle is represented by a plane so that an interpolated value at point (x, y) lies on the plane of the triangle containing (x, y). Interpolated values are therefore continuous across the triangulation, but their first derivatives are discontinuous at edges between triangles.

Parameters:

**triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

The triangulation to interpolate over.

**z**(npoints,) array-like

Array of values, defined at grid points, to interpolate between.

**trifinder**[`TriFinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriFinder "matplotlib.tri.TriFinder")
, optional

If this is not specified, the Triangulation's default TriFinder will be used by calling [`Triangulation.get_trifinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_trifinder "matplotlib.tri.Triangulation.get_trifinder")
.

Methods

|     |     |
| --- | --- |
| **\`\_\_call\_\_\` (x, y)** | (Returns interpolated values at (x, y) points.) |
| **\`gradient\` (x, y)** | (Returns interpolated derivatives at (x, y) points.) |

gradient(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triinterpolate.py#L269-L271)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.LinearTriInterpolator.gradient "Link to this definition")

Returns a list of 2 masked arrays containing interpolated derivatives at the specified (x, y) points.

Parameters:

**x, y**array-like

x and y coordinates of the same shape and any number of dimensions.

Returns:

**dzdx, dzdy**np.ma.array

2 masked arrays of the same shape as _x_ and _y_; values corresponding to (x, y) points outside of the triangulation are masked out. The first returned array contains the values of \\(\\frac{\\partial z}{\\partial x}\\) and the second those of \\(\\frac{\\partial z}{\\partial y}\\).

class matplotlib.tri.CubicTriInterpolator(_triangulation_, _z_, _kind\='min\_E'_, _trifinder\=None_, _dz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triinterpolate.py#L286-L573)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "Link to this definition")

Bases: [`TriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriInterpolator "matplotlib.tri._triinterpolate.TriInterpolator")

Cubic interpolator on a triangular grid.

In one-dimension - on a segment - a cubic interpolating function is defined by the values of the function and its derivative at both ends. This is almost the same in 2D inside a triangle, except that the values of the function and its 2 derivatives have to be defined at each triangle node.

The CubicTriInterpolator takes the value of the function at each node - provided by the user - and internally computes the value of the derivatives, resulting in a smooth interpolation. (As a special feature, the user can also impose the value of the derivatives at each node, but this is not supposed to be the common usage.)

Parameters:

**triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

The triangulation to interpolate over.

**z**(npoints,) array-like

Array of values, defined at grid points, to interpolate between.

**kind**{'min\_E', 'geom', 'user'}, optional

Choice of the smoothing algorithm, in order to compute the interpolant derivatives (defaults to 'min\_E'):

*   if 'min\_E': (default) The derivatives at each node is computed to minimize a bending energy.
    
*   if 'geom': The derivatives at each node is computed as a weighted average of relevant triangle normals. To be used for speed optimization (large grids).
    
*   if 'user': The user provides the argument _dz_, no computation is hence needed.
    

**trifinder**[`TriFinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriFinder "matplotlib.tri.TriFinder")
, optional

If not specified, the Triangulation's default TriFinder will be used by calling [`Triangulation.get_trifinder`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.get_trifinder "matplotlib.tri.Triangulation.get_trifinder")
.

**dz**tuple of array-likes (dzdx, dzdy), optional

Used only if _kind_ ='user'. In this case _dz_ must be provided as (dzdx, dzdy) where dzdx, dzdy are arrays of the same shape as _z_ and are the interpolant first derivatives at the _triangulation_ points.

Methods

|     |     |
| --- | --- |
| **\`\_\_call\_\_\` (x, y)** | (Returns interpolated values at (x, y) points.) |
| **\`gradient\` (x, y)** | (Returns interpolated derivatives at (x, y) points.) |

Notes

This note is a bit technical and details how the cubic interpolation is computed.

The interpolation is based on a Clough-Tocher subdivision scheme of the _triangulation_ mesh (to make it clearer, each triangle of the grid will be divided in 3 child-triangles, and on each child triangle the interpolated function is a cubic polynomial of the 2 coordinates). This technique originates from FEM (Finite Element Method) analysis; the element used is a reduced Hsieh-Clough-Tocher (HCT) element. Its shape functions are described in [\[1\]](https://matplotlib.org/stable/api/tri_api.html#r0be0c58fd53f-1)
. The assembled function is guaranteed to be C1-smooth, i.e. it is continuous and its first derivatives are also continuous (this is easy to show inside the triangles but is also true when crossing the edges).

In the default case (_kind_ ='min\_E'), the interpolant minimizes a curvature energy on the functional space generated by the HCT element shape functions - with imposed values but arbitrary derivatives at each node. The minimized functional is the integral of the so-called total curvature (implementation based on an algorithm from [\[2\]](https://matplotlib.org/stable/api/tri_api.html#r0be0c58fd53f-2)
 - PCG sparse solver):

\\\[E(z) = \\frac{1}{2} \\int\_{\\Omega} \\left( \\left( \\frac{\\partial^2{z}}{\\partial{x}^2} \\right)^2 + \\left( \\frac{\\partial^2{z}}{\\partial{y}^2} \\right)^2 + 2\\left( \\frac{\\partial^2{z}}{\\partial{y}\\partial{x}} \\right)^2 \\right) dx\\,dy\\\]

If the case _kind_ ='geom' is chosen by the user, a simple geometric approximation is used (weighted average of the triangle normal vectors), which could improve speed on very large grids.

References

\[[1](https://matplotlib.org/stable/api/tri_api.html#id1)\
\]

Michel Bernadou, Kamal Hassan, "Basis functions for general Hsieh-Clough-Tocher triangles, complete or reduced.", International Journal for Numerical Methods in Engineering, 17(5):784 - 789. 2.01.

\[[2](https://matplotlib.org/stable/api/tri_api.html#id2)\
\]

C.T. Kelley, "Iterative Methods for Optimization".

gradient(_x_, _y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_triinterpolate.py#L425-L427)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator.gradient "Link to this definition")

Returns a list of 2 masked arrays containing interpolated derivatives at the specified (x, y) points.

Parameters:

**x, y**array-like

x and y coordinates of the same shape and any number of dimensions.

Returns:

**dzdx, dzdy**np.ma.array

2 masked arrays of the same shape as _x_ and _y_; values corresponding to (x, y) points outside of the triangulation are masked out. The first returned array contains the values of \\(\\frac{\\partial z}{\\partial x}\\) and the second those of \\(\\frac{\\partial z}{\\partial y}\\).

class matplotlib.tri.TriRefiner(_triangulation_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_trirefine.py#L12-L44)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriRefiner "Link to this definition")

Abstract base class for classes implementing mesh refinement.

A TriRefiner encapsulates a Triangulation object and provides tools for mesh refinement and interpolation.

Derived classes must implement:

*   `refine_triangulation(return_tri_index=False, **kwargs)` , where the optional keyword arguments _kwargs_ are defined in each TriRefiner concrete implementation, and which returns:
    
    *   a refined triangulation,
        
    *   optionally (depending on _return\_tri\_index_), for each point of the refined triangulation: the index of the initial triangulation triangle to which it belongs.
        
*   `refine_field(z, triinterpolator=None, **kwargs)`, where:
    
    *   _z_ array of field values (to refine) defined at the base triangulation nodes,
        
    *   _triinterpolator_ is an optional [`TriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriInterpolator "matplotlib.tri.TriInterpolator")
        ,
        
    *   the other optional keyword arguments _kwargs_ are defined in each TriRefiner concrete implementation;
        
    
    and which returns (as a tuple) a refined triangular mesh and the interpolated values of the field at the refined triangulation nodes.
    

class matplotlib.tri.UniformTriRefiner(_triangulation_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_trirefine.py#L47-L307)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner "Link to this definition")

Bases: [`TriRefiner`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriRefiner "matplotlib.tri._trirefine.TriRefiner")

Uniform mesh refinement by recursive subdivisions.

Parameters:

**triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

The encapsulated triangulation (to be refined)

refine\_field(_z_, _triinterpolator\=None_, _subdiv\=3_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_trirefine.py#L133-L169)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner.refine_field "Link to this definition")

Refine a field defined on the encapsulated triangulation.

Parameters:

**z**(npoints,) array-like

Values of the field to refine, defined at the nodes of the encapsulated triangulation. (`n_points` is the number of points in the initial triangulation)

**triinterpolator**[`TriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriInterpolator "matplotlib.tri.TriInterpolator")
, optional

Interpolator used for field interpolation. If not specified, a [`CubicTriInterpolator`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.CubicTriInterpolator "matplotlib.tri.CubicTriInterpolator")
 will be used.

**subdiv**int, default: 3

Recursion level for the subdivision. Each triangle is divided into `4**subdiv` child triangles.

Returns:

**refi\_tri**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

The returned refined triangulation.

**refi\_z**1D array of length: _refi\_tri_ node count.

The returned interpolated field (at _refi\_tri_ nodes).

refine\_triangulation(_return\_tri\_index\=False_, _subdiv\=3_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_trirefine.py#L64-L131)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.UniformTriRefiner.refine_triangulation "Link to this definition")

Compute a uniformly refined triangulation _refi\_triangulation_ of the encapsulated `triangulation`.

This function refines the encapsulated triangulation by splitting each father triangle into 4 child sub-triangles built on the edges midside nodes, recursing _subdiv_ times. In the end, each triangle is hence divided into `4**subdiv` child triangles.

Parameters:

**return\_tri\_index**bool, default: False

Whether an index table indicating the father triangle index of each point is returned.

**subdiv**int, default: 3

Recursion level for the subdivision. Each triangle is divided into `4**subdiv` child triangles; hence, the default results in 64 refined subtriangles for each triangle of the initial triangulation.

Returns:

**refi\_triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

The refined triangulation.

**found\_index**int array

Index of the initial triangulation containing triangle, for each point of _refi\_triangulation_. Returned only if _return\_tri\_index_ is set to True.

class matplotlib.tri.TriAnalyzer(_triangulation_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_tritools.py#L11-L263)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer "Link to this definition")

Define basic tools for triangular mesh analysis and improvement.

A TriAnalyzer encapsulates a [`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")
 object and provides basic tools for mesh analysis and mesh improvement.

Parameters:

**triangulation**[`Triangulation`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation "matplotlib.tri.Triangulation")

The encapsulated triangulation to analyze.

Attributes:

[`scale_factors`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.scale_factors "matplotlib.tri.TriAnalyzer.scale_factors")

Factors to rescale the triangulation into a unit square.

circle\_ratios(_rescale\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_tritools.py#L50-L115)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.circle_ratios "Link to this definition")

Return a measure of the triangulation triangles flatness.

The ratio of the incircle radius over the circumcircle radius is a widely used indicator of a triangle flatness. It is always `<= 0.5` and `== 0.5` only for equilateral triangles. Circle ratios below 0.01 denote very flat triangles.

To avoid unduly low values due to a difference of scale between the 2 axis, the triangular mesh can first be rescaled to fit inside a unit square with [`scale_factors`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.scale_factors "matplotlib.tri.TriAnalyzer.scale_factors")
 (Only if _rescale_ is True, which is its default value).

Parameters:

**rescale**bool, default: True

If True, internally rescale (based on [`scale_factors`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.scale_factors "matplotlib.tri.TriAnalyzer.scale_factors")
), so that the (unmasked) triangles fit exactly inside a unit square mesh.

Returns:

masked array

Ratio of the incircle radius over the circumcircle radius, for each 'rescaled' triangle of the encapsulated triangulation. Values corresponding to masked triangles are masked out.

get\_flat\_tri\_mask(_min\_circle\_ratio\=0.01_, _rescale\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/tri/_tritools.py#L117-L190)
[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.get_flat_tri_mask "Link to this definition")

Eliminate excessively flat border triangles from the triangulation.

Returns a mask _new\_mask_ which allows to clean the encapsulated triangulation from its border-located flat triangles (according to their [`circle_ratios()`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.circle_ratios "matplotlib.tri.TriAnalyzer.circle_ratios")
). This mask is meant to be subsequently applied to the triangulation using [`Triangulation.set_mask`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.Triangulation.set_mask "matplotlib.tri.Triangulation.set_mask")
. _new\_mask_ is an extension of the initial triangulation mask in the sense that an initially masked triangle will remain masked.

The _new\_mask_ array is computed recursively; at each step flat triangles are removed only if they share a side with the current mesh border. Thus, no new holes in the triangulated domain will be created.

Parameters:

**min\_circle\_ratio**float, default: 0.01

Border triangles with incircle/circumcircle radii ratio r/R will be removed if r/R < _min\_circle\_ratio_.

**rescale**bool, default: True

If True, first, internally rescale (based on [`scale_factors`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.scale_factors "matplotlib.tri.TriAnalyzer.scale_factors")
) so that the (unmasked) triangles fit exactly inside a unit square mesh. This rescaling accounts for the difference of scale which might exist between the 2 axis.

Returns:

array of bool

Mask to apply to encapsulated triangulation. All the initially masked triangles remain masked in the _new\_mask_.

Notes

The rationale behind this function is that a Delaunay triangulation - of an unstructured set of points - sometimes contains almost flat triangles at its border, leading to artifacts in plots (especially for high-resolution contouring). Masked with computed _new\_mask_, the encapsulated triangulation would contain no more unmasked border triangles with a circle ratio below _min\_circle\_ratio_, thus improving the mesh quality for subsequent plots or interpolation.

property scale\_factors[#](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriAnalyzer.scale_factors "Link to this definition")

Factors to rescale the triangulation into a unit square.

Returns:

(float, float)

Scaling factors (kx, ky) so that the triangulation `[triangulation.x * kx, triangulation.y * ky]` fits exactly inside a unit square.

On this page