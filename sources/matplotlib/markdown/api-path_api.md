[Skip to main content](https://matplotlib.org/stable/api/path_api.html#main-content)

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
    

`matplotlib.path`[#](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "Link to this heading")

====================================================================================================================

A module for dealing with the polylines used throughout Matplotlib.

The primary class for polyline handling in Matplotlib is [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
. Almost all vector drawing makes use of [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
s somewhere in the drawing pipeline.

Whilst a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance itself cannot be drawn, some [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 subclasses, such as [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 and [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
, can be used for convenient [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 visualisation.

class matplotlib.path.Path(_vertices_, _codes\=None_, _\_interpolation\_steps\=1_, _closed\=False_, _readonly\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L24-L1105)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A series of possibly disconnected, possibly closed, line and curve segments.

The underlying storage is made up of two parallel numpy arrays:

*   _vertices_: an (N, 2) float array of vertices
    
*   _codes_: an N-length [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")
     array of path codes, or None
    

These two arrays always have the same length in the first dimension. For example, to represent a cubic curve, you must provide three vertices and three [`CURVE4`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE4 "matplotlib.path.Path.CURVE4")
 codes.

The code types are:

*   [`STOP`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.STOP "matplotlib.path.Path.STOP")
    1 vertex (ignored)
    
    A marker for the end of the entire path (currently not required and ignored)
    
*   [`MOVETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "matplotlib.path.Path.MOVETO")
    1 vertex
    
    Pick up the pen and move to the given vertex.
    
*   [`LINETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "matplotlib.path.Path.LINETO")
    1 vertex
    
    Draw a line from the current position to the given vertex.
    
*   [`CURVE3`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE3 "matplotlib.path.Path.CURVE3")
    1 control point, 1 endpoint
    
    Draw a quadratic Bézier curve from the current position, with the given control point, to the given end point.
    
*   [`CURVE4`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE4 "matplotlib.path.Path.CURVE4")
    2 control points, 1 endpoint
    
    Draw a cubic Bézier curve from the current position, with the given control points, to the given end point.
    
*   [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
    1 vertex (ignored)
    
    Draw a line segment to the start point of the current polyline.
    

If _codes_ is None, it is interpreted as a [`MOVETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "matplotlib.path.Path.MOVETO")
 followed by a series of [`LINETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "matplotlib.path.Path.LINETO")
.

Users of Path objects should not access the vertices and codes arrays directly. Instead, they should use [`iter_segments`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_segments "matplotlib.path.Path.iter_segments")
 or [`cleaned`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.cleaned "matplotlib.path.Path.cleaned")
 to get the vertex/code pairs. This helps, in particular, to consistently handle the case of _codes_ being None.

Some behavior of Path objects can be controlled by rcParams. See the rcParams whose keys start with 'path.'.

Note

The vertices and codes arrays should be treated as immutable -- there are a number of optimizations and assumptions made up front in the constructor that will not change when the data changes.

Create a new path with the given vertices and codes.

Parameters:

**vertices**(N, 2) array-like

The path vertices, as an array, masked array or sequence of pairs. Masked values, if any, will be converted to NaNs, which are then handled correctly by the Agg PathIterator and other consumers of path data, such as [`iter_segments()`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_segments "matplotlib.path.Path.iter_segments")
.

**codes**array-like or None, optional

N-length array of integers representing the codes of the path. If not None, codes must be the same length as vertices. If None, _vertices_ will be treated as a series of line segments.

**\_interpolation\_steps**int, optional

Used as a hint to certain projections, such as Polar, that this path should be linearly interpolated immediately before drawing. This attribute is primarily an implementation detail and is not intended for public use.

**closed**bool, optional

If _codes_ is None and closed is True, vertices will be treated as line segments of a closed polygon. Note that the last vertex will then be ignored (as the corresponding code will be set to [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
).

**readonly**bool, optional

Makes the path behave in an immutable way and sets the vertices and codes as read-only arrays.

CLOSEPOLY \= np.uint8(79)[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "Link to this definition")

CURVE3 \= np.uint8(3)[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE3 "Link to this definition")

CURVE4 \= np.uint8(4)[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE4 "Link to this definition")

LINETO \= np.uint8(2)[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "Link to this definition")

MOVETO \= np.uint8(1)[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "Link to this definition")

NUM\_VERTICES\_FOR\_CODE \= {np.uint8(0): 1, np.uint8(1): 1, np.uint8(2): 1, np.uint8(3): 2, np.uint8(4): 3, np.uint8(79): 1}[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.NUM_VERTICES_FOR_CODE "Link to this definition")

A dictionary mapping Path codes to the number of vertices that the code expects.

STOP \= np.uint8(0)[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.STOP "Link to this definition")

classmethod arc(_theta1_, _theta2_, _n\=None_, _is\_wedge\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L971-L1061)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.arc "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for the unit circle arc from angles _theta1_ to _theta2_ (in degrees).

_theta2_ is unwrapped to produce the shortest arc within 360 degrees. That is, if _theta2_ > _theta1_ + 360, the arc will be from _theta1_ to _theta2_ - 360 and not a full circle plus some extra overlap.

As a special case, if the span _theta2_ - _theta1_ is within floating-point tolerance of a whole number of turns, a complete circle is drawn.

If _n_ is provided, it is the number of spline segments to make. If _n_ is not provided, the number of spline segments is determined based on the delta between _theta1_ and _theta2_.

> Masionobe, L. 2003. [Drawing an elliptical arc using polylines, quadratic or cubic Bezier curves](https://web.archive.org/web/20190318044212/http://www.spaceroots.org/documents/ellipse/index.html)
> .

classmethod circle(_center\=(0.0, 0.0)_, _radius\=1.0_, _readonly\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L859-L925)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.circle "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 representing a circle of a given radius and center.

Parameters:

**center**(float, float), default: (0, 0)

The center of the circle.

**radius**float, default: 1

The radius of the circle.

**readonly**bool

Whether the created path should have the "readonly" argument set when creating the Path instance.

Notes

The circle is approximated using 8 cubic Bézier curves, as described in

> Lancaster, Don. [Approximating a Circle or an Ellipse Using Four Bezier Cubic Splines](https://www.tinaja.com/glib/ellipse4.pdf)
> .

cleaned(_transform\=None_, _remove\_nans\=False_, _clip\=None_, _\*_, _simplify\=False_, _curves\=False_, _stroke\_width\=1.0_, _snap\=False_, _sketch\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L489-L506)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.cleaned "Link to this definition")

Return a new [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 with vertices and codes cleaned according to the parameters.

See also

[`Path.iter_segments`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_segments "matplotlib.path.Path.iter_segments")

for details of the keyword arguments.

clip\_to\_bbox(_bbox_, _inside\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L1093-L1105)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.clip_to_bbox "Link to this definition")

Clip the path to the given bounding box.

The path must be made up of one or more closed polygons. This algorithm will not behave correctly for unclosed paths.

If _inside_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
, clip to the inside of the box, otherwise to the outside of the box.

code\_type[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.code_type "Link to this definition")

alias of `uint8`

property codes[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.codes "Link to this definition")

The list of codes in the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 as a 1D array.

Each code is one of [`STOP`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.STOP "matplotlib.path.Path.STOP")
, [`MOVETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "matplotlib.path.Path.MOVETO")
, [`LINETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "matplotlib.path.Path.LINETO")
, [`CURVE3`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE3 "matplotlib.path.Path.CURVE3")
, [`CURVE4`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE4 "matplotlib.path.Path.CURVE4")
 or [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
. For codes that correspond to more than one vertex ([`CURVE3`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE3 "matplotlib.path.Path.CURVE3")
 and [`CURVE4`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE4 "matplotlib.path.Path.CURVE4")
), that code will be repeated so that the length of [`vertices`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.vertices "matplotlib.path.Path.vertices")
 and [`codes`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.codes "matplotlib.path.Path.codes")
 is always the same.

contains\_path(_path_, _transform\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L615-L624)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_path "Link to this definition")

Return whether this (closed) path completely contains the given path.

If _transform_ is not `None`, the path will be transformed before checking for containment.

contains\_point(_point_, _transform\=None_, _radius\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L521-L569)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_point "Link to this definition")

Return whether the area enclosed by the path contains the given point.

The path is always treated as closed; i.e. if the last code is not [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
 an implicit segment connecting the last vertex to the first vertex is assumed.

Parameters:

**point**(float, float)

The point (x, y) to check.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

If not `None`, _point_ will be compared to `self` transformed by _transform_; i.e. for a correct check, _transform_ should transform the path into the coordinate system of _point_.

**radius**float, default: 0

Additional margin on the path in coordinates of _point_. The path is extended tangentially by _radius/2_; i.e. if you would draw the path with a linewidth of _radius_, all points on the line would still be considered to be contained in the area. Conversely, negative values shrink the area: Points on the imaginary line will be considered outside the area.

Returns:

bool

Notes

The current algorithm has some limitations:

*   The result is undefined for points exactly at the boundary (i.e. at the path shifted by _radius/2_).
    
*   The result is undefined if there is no enclosed area, i.e. all vertices are on a straight line.
    
*   If bounding lines start to cross each other due to _radius_ shift, the result is not guaranteed to be correct.
    

contains\_points(_points_, _transform\=None_, _radius\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L571-L613)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.contains_points "Link to this definition")

Return whether the area enclosed by the path contains the given points.

The path is always treated as closed; i.e. if the last code is not [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
 an implicit segment connecting the last vertex to the first vertex is assumed.

Parameters:

**points**(N, 2) array

The points to check. Columns contain x and y values.

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

If not `None`, _points_ will be compared to `self` transformed by _transform_; i.e. for a correct check, _transform_ should transform the path into the coordinate system of _points_.

**radius**float, default: 0

Additional margin on the path in coordinates of _points_. The path is extended tangentially by _radius/2_; i.e. if you would draw the path with a linewidth of _radius_, all points on the line would still be considered to be contained in the area. Conversely, negative values shrink the area: Points on the imaginary line will be considered outside the area.

Returns:

length-N bool array

Notes

The current algorithm has some limitations:

*   The result is undefined for points exactly at the boundary (i.e. at the path shifted by _radius/2_).
    
*   The result is undefined if there is no enclosed area, i.e. all vertices are on a straight line.
    
*   If bounding lines start to cross each other due to _radius_ shift, the result is not guaranteed to be correct.
    

copy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L271-L276)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.copy "Link to this definition")

Return a shallow copy of the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, which will share the vertices and codes with the source [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

deepcopy(_memo\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L293-L308)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.deepcopy "Link to this definition")

Return a deep copy of the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
. The [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 will not be readonly, even if the source [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 is.

Parameters:

**memo**dict, optional

A dictionary to use for memoizing, passed to [`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.14)")
.

Returns:

Path

A deep copy of the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, but not readonly.

get\_extents(_transform\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L626-L665)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.get_extents "Link to this definition")

Get Bbox of the path.

Parameters:

**transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
, optional

Transform to apply to path before computing extents, if any.

**\*\*kwargs**

Forwarded to [`iter_bezier`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_bezier "matplotlib.path.Path.iter_bezier")
.

Returns:

matplotlib.transforms.Bbox

The extents of the path Bbox(\[\[xmin, ymin\], \[xmax, ymax\]\])

static hatch(_hatchpattern_, _density\=6_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L1081-L1091)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.hatch "Link to this definition")

Given a hatch specifier, _hatchpattern_, generates a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 that can be used in a repeated hatching pattern. _density_ is the number of lines per unit square.

interpolated(_steps_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L688-L726)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.interpolated "Link to this definition")

Return a new path with each segment divided into _steps_ parts.

Codes other than [`LINETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "matplotlib.path.Path.LINETO")
, [`MOVETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "matplotlib.path.Path.MOVETO")
, and [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
 are not handled correctly.

Parameters:

**steps**int

The number of segments in the new path for each in the original.

Returns:

Path

The interpolated path.

intersects\_bbox(_bbox_, _filled\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L676-L686)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.intersects_bbox "Link to this definition")

Return whether this path intersects a given [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
.

If _filled_ is True, then this also returns True if the path completely encloses the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 (i.e., the path is treated as filled).

The bounding box is always considered filled.

intersects\_path(_other_, _filled\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L667-L674)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.intersects_path "Link to this definition")

Return whether if this path intersects another given path.

If _filled_ is True, then this also returns True if one path completely encloses the other (i.e., the paths are treated as filled).

iter\_bezier(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L432-L477)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_bezier "Link to this definition")

Iterate over each Bézier curve (lines included) in a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

Parameters:

**\*\*kwargs**

Forwarded to [`iter_segments`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_segments "matplotlib.path.Path.iter_segments")
.

Yields:

**B**[`BezierSegment`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment "matplotlib.bezier.BezierSegment")

The Bézier curves that make up the current path. Note in particular that freestanding points are Bézier curves of order 0, and lines are Bézier curves of order 1 (with two control points).

**code**[`code_type`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.code_type "matplotlib.path.Path.code_type")

The code describing what kind of curve is being returned. [`MOVETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "matplotlib.path.Path.MOVETO")
, [`LINETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "matplotlib.path.Path.LINETO")
, [`CURVE3`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE3 "matplotlib.path.Path.CURVE3")
, and [`CURVE4`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CURVE4 "matplotlib.path.Path.CURVE4")
 correspond to Bézier curves with 1, 2, 3, and 4 control points (respectively). [`CLOSEPOLY`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.CLOSEPOLY "matplotlib.path.Path.CLOSEPOLY")
 is a [`LINETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.LINETO "matplotlib.path.Path.LINETO")
 with the control points correctly chosen based on the start/end points of the current stroke.

iter\_segments(_transform\=None_, _remove\_nans\=True_, _clip\=None_, _snap\=False_, _stroke\_width\=1.0_, _simplify\=None_, _curves\=True_, _sketch\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L366-L430)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.iter_segments "Link to this definition")

Iterate over all curve segments in the path.

Each iteration returns a pair `(vertices, code)`, where `vertices` is a sequence of 1-3 coordinate pairs, and `code` is a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 code.

Additionally, this method can provide a number of standard cleanups and conversions to the path.

Parameters:

**transform**None or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

If not None, the given affine transformation will be applied to the path.

**remove\_nans**bool, optional

Whether to remove all NaNs from the path and skip over them using MOVETO commands.

**clip**None or (float, float, float, float), optional

If not None, must be a four-tuple (x1, y1, x2, y2) defining a rectangle in which to clip the path.

**snap**None or bool, optional

If True, snap all nodes to pixels; if False, don't snap them. If None, snap if the path contains only segments parallel to the x or y axes, and no more than 1024 of them.

**stroke\_width**float, optional

The width of the stroke being drawn (used for path snapping).

**simplify**None or bool, optional

Whether to simplify the path by removing vertices that do not affect its appearance. If None, use the [`should_simplify`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.should_simplify "matplotlib.path.Path.should_simplify")
 attribute. See also `[rcParams["path.simplify"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=path.simplify#rcparam-path-simplify) ` (default: `True`) and `[rcParams["path.simplify_threshold"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=path.simplify_threshold#rcparam-path-simplify-threshold) ` (default: `0.111111111111`).

**curves**bool, optional

If True, curve segments will be returned as curve segments. If False, all curves will be converted to line segments.

**sketch**None or sequence, optional

If not None, must be a 3-tuple of the form (scale, length, randomness), representing the sketch parameters.

classmethod make\_compound\_path(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L338-L358)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.make_compound_path "Link to this definition")

Concatenate a list of [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
s into a single [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, removing all [`STOP`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.STOP "matplotlib.path.Path.STOP")
s.

classmethod make\_compound\_path\_from\_polys(_XY_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L310-L336)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.make_compound_path_from_polys "Link to this definition")

Make a compound [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 object to draw a number of polygons with equal numbers of sides.

([`Source code`](https://matplotlib.org/stable/_downloads/e44134d2fdd50b66bb9fe932e3555cdd/histogram_path.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/565ca4a614dae2e46ffe1a6ec5da6995/histogram_path_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/9d2e557c43c766afe81e0c6cddfcc4ae/histogram_path_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-histogram_path_00_00.2x.png)](https://matplotlib.org/stable/_images/api-histogram_path_00_00.2x.png)

([`2x.png`](https://matplotlib.org/stable/_downloads/ecb8b8d4285460444dddba3ea2d09adf/histogram_path_01_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/57b9136d1f264f9e72f99c71a47f00b7/histogram_path_01_00.png)
)

[![](https://matplotlib.org/stable/_images/api-histogram_path_01_00.2x.png)](https://matplotlib.org/stable/_images/api-histogram_path_01_00.2x.png)

Parameters:

**XY**(numpolys, numsides, 2) array

property readonly[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.readonly "Link to this definition")

[`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 if the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 is read-only.

property should\_simplify[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.should_simplify "Link to this definition")

[`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 if the vertices array should be simplified.

property simplify\_threshold[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.simplify_threshold "Link to this definition")

The fraction of a pixel difference below which vertices will be simplified out.

to\_polygons(_transform\=None_, _width\=0_, _height\=0_, _closed\_only\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L728-L773)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.to_polygons "Link to this definition")

Convert this path to a list of polygons or polylines. Each polygon/polyline is an (N, 2) array of vertices. In other words, each polygon has no [`MOVETO`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.MOVETO "matplotlib.path.Path.MOVETO")
 instructions or curves. This is useful for displaying in backends that do not support compound paths or Bézier curves.

If _width_ and _height_ are both non-zero then the lines will be simplified so that vertices outside of (0, 0), (width, height) will be clipped.

The resulting polygons will be simplified if the [`Path.should_simplify`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.should_simplify "matplotlib.path.Path.should_simplify")
 attribute of the path is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
.

If _closed\_only_ is [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 (default), only closed polygons, with the last point being the same as the first point, will be returned. Any unclosed polylines in the path will be explicitly closed. If _closed\_only_ is [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
, any unclosed polygons in the path will be returned as unclosed polygons, and the closed polygons will be returned explicitly closed by setting the last point to the same as the first point.

transformed(_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L508-L519)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.transformed "Link to this definition")

Return a transformed copy of the path.

See also

[`matplotlib.transforms.TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")

A specialized path class that will cache the transformed result and automatically update when the transform changes.

classmethod unit\_circle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L847-L857)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_circle "Link to this definition")

Return the readonly [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 of the unit circle.

For most cases, [`Path.circle()`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.circle "matplotlib.path.Path.circle")
 will be what you want.

classmethod unit\_circle\_righthalf()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L929-L969)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_circle_righthalf "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 of the right half of a unit circle.

See [`Path.circle`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.circle "matplotlib.path.Path.circle")
 for the reference on the approximation used.

classmethod unit\_rectangle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L777-L785)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_rectangle "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance of the unit rectangle from (0, 0) to (1, 1).

classmethod unit\_regular\_asterisk(_numVertices_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L837-L843)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_regular_asterisk "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for a unit regular asterisk with the given numVertices and radius of 1.0, centered at (0, 0).

classmethod unit\_regular\_polygon(_numVertices_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L789-L809)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_regular_polygon "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance for a unit regular polygon with the given _numVertices_ such that the circumscribing circle has radius 1.0, centered at (0, 0).

classmethod unit\_regular\_star(_numVertices_, _innerCircle\=0.5_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L813-L835)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.unit_regular_star "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for a unit regular star with the given numVertices and radius of 1.0, centered at (0, 0).

property vertices[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.vertices "Link to this definition")

The vertices of the [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 as an (N, 2) array.

classmethod wedge(_theta1_, _theta2_, _n\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L1063-L1079)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.wedge "Link to this definition")

Return a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 for the unit circle wedge from angles _theta1_ to _theta2_ (in degrees).

_theta2_ is unwrapped to produce the shortest wedge within 360 degrees. That is, if _theta2_ > _theta1_ + 360, the wedge will be from _theta1_ to _theta2_ - 360 and not a full circle plus some extra overlap.

If _n_ is provided, it is the number of spline segments to make. If _n_ is not provided, the number of spline segments is determined based on the delta between _theta1_ and _theta2_.

See [`Path.arc`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.arc "matplotlib.path.Path.arc")
 for the reference on the approximation used.

matplotlib.path.get\_path\_collection\_extents(_master\_transform_, _paths_, _transforms_, _offsets_, _offset\_transform_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/path.py#L1108-L1146)
[#](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.get_path_collection_extents "Link to this definition")

Get bounding box of a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
s internal objects.

That is, given a sequence of [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
s, [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
s objects, and offsets, as found in a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
, return the bounding box that encapsulates all of them.

Parameters:

**master\_transform**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

Global transformation applied to all paths.

**paths**list of [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

**transforms**list of [`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

If non-empty, this overrides _master\_transform_.

**offsets**(N, 2) array-like

**offset\_transform**[`Affine2DBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase "matplotlib.transforms.Affine2DBase")

Transform applied to the offsets before offsetting the path.

Notes

The way that _paths_, _transforms_ and _offsets_ are combined follows the same method as for collections: each is iterated over independently, so if you have 3 paths (A, B, C), 2 transforms (α, β) and 1 offset (O), their combinations are as follows:

*   (A, α, O)
    
*   (B, β, O)
    
*   (C, α, O)
    

On this page