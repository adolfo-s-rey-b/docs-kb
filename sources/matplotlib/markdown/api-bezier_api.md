[Skip to main content](https://matplotlib.org/stable/api/bezier_api.html#main-content)

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
    

`matplotlib.bezier`[#](https://matplotlib.org/stable/api/bezier_api.html#module-matplotlib.bezier "Link to this heading")

==========================================================================================================================

A module providing some utility functions regarding Bézier path manipulation.

class matplotlib.bezier.BezierSegment(_control\_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L273-L402)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A d-dimensional Bézier segment.

A BezierSegment can be called with an argument, either a scalar or an array-like object, to evaluate the curve at that/those location(s).

Parameters:

**control\_points**(N, d) array

Location of the _N_ control points.

\_\_call\_\_(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L295-L311)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.__call__ "Link to this definition")

Evaluate the Bézier curve at point(s) _t_ in \[0, 1\].

Parameters:

**t**(k,) array-like

Points at which to evaluate the curve.

Returns:

(k, d) array

Value of the curve for each point in _t_.

axis\_aligned\_extrema()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L368-L402)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.axis_aligned_extrema "Link to this definition")

Return the dimension and location of the curve's interior extrema.

The extrema are the points along the curve where one of its partial derivatives is zero.

Returns:

**dims**array of int

Index \\(i\\) of the partial derivative which is zero at each interior extrema.

**dzeros**array of float

Of same size as dims. The \\(t\\) such that \\(d/dx\_i B(t) = 0\\)

property control\_points[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.control_points "Link to this definition")

The control points of the curve.

property degree[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.degree "Link to this definition")

Degree of the polynomial. One less the number of control points.

property dimension[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.dimension "Link to this definition")

The dimension of the curve.

point\_at\_t(_t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L313-L319)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.point_at_t "Link to this definition")

\[_Deprecated_\] Evaluate the curve at a single point, returning a tuple of _d_ floats.

Notes

Deprecated since version 3.11: Use Call the BezierSegment object with an argument. instead.

property polynomial\_coefficients[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment.polynomial_coefficients "Link to this definition")

The polynomial coefficients of the Bézier curve.

Warning

Follows opposite convention from [`numpy.polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "(in NumPy v2.5)")
.

Returns:

(n+1, d) array

Coefficients after expanding in polynomial basis, where \\(n\\) is the degree of the Bézier curve and \\(d\\) its dimension. These are the numbers (\\(C\_j\\)) such that the curve can be written \\(\\sum\_{j=0}^n C\_j t^j\\).

Notes

The coefficients are calculated as

\\\[{n \\choose j} \\sum\_{i=0}^j (-1)^{i+j} {j \\choose i} P\_i\\\]

where \\(P\_i\\) are the control points of the curve.

exception matplotlib.bezier.NonIntersectingPathException[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L109-L110)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.NonIntersectingPathException "Link to this definition")

Bases: [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")

matplotlib.bezier.check\_if\_parallel(_dx1_, _dy1_, _dx2_, _dy2_, _tolerance\=1e-05_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L528-L555)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.check_if_parallel "Link to this definition")

Check if two lines are parallel.

Parameters:

**dx1, dy1, dx2, dy2**float

The gradients _dy_/_dx_ of the two lines.

**tolerance**float

The angular tolerance in radians up to which the lines are considered parallel.

Returns:

is\_parallel

*   1 if two lines are parallel in same direction.
    
*   \-1 if two lines are parallel in opposite direction.
    
*   False otherwise.
    

matplotlib.bezier.find\_bezier\_t\_intersecting\_with\_closedpath(_bezier\_point\_at\_t_, _inside\_closedpath_, _t0\=0.0_, _t1\=1.0_, _tolerance\=0.01_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L197-L270)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.find_bezier_t_intersecting_with_closedpath "Link to this definition")

Find the intersection of the Bézier curve with a closed path.

The intersection point _t_ is approximated by two parameters _t0_, _t1_ such that _t0_ <= _t_ <= _t1_.

Search starts from _t0_ and _t1_ and uses a simple bisecting algorithm therefore one of the end points must be inside the path while the other doesn't. The search stops when the distance of the points parametrized by _t0_ and _t1_ gets smaller than the given _tolerance_.

Parameters:

**bezier\_point\_at\_t**callable

A function returning x, y coordinates of the Bézier at parameter _t_. It must have the signature:

bezier\_point\_at\_t(t: float) \-> tuple\[float, float\]

**inside\_closedpath**callable

A function returning True if a given point (x, y) is inside the closed path. It must have the signature:

inside\_closedpath(point: tuple\[float, float\]) \-> bool

**t0, t1**float

Start parameters for the search.

**tolerance**float

Maximal allowed distance between the final points.

Returns:

**t0, t1**float

The Bézier path parameters.

matplotlib.bezier.find\_control\_points(_c1x_, _c1y_, _mmx_, _mmy_, _c2x_, _c2y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L632-L639)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.find_control_points "Link to this definition")

Find control points of the Bézier curve passing through (_c1x_, _c1y_), (_mmx_, _mmy_), and (_c2x_, _c2y_), at parametric values 0, 0.5, and 1.

matplotlib.bezier.get\_cos\_sin(_x0_, _y0_, _x1_, _y1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L519-L525)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.get_cos_sin "Link to this definition")

matplotlib.bezier.get\_intersection(_cx1_, _cy1_, _cos\_t1_, _sin\_t1_, _cx2_, _cy2_, _cos\_t2_, _sin\_t2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L116-L146)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.get_intersection "Link to this definition")

Return the intersection between the line through (_cx1_, _cy1_) at angle _t1_ and the line through (_cx2_, _cy2_) at angle _t2_.

matplotlib.bezier.get\_normal\_points(_cx_, _cy_, _cos\_t_, _sin\_t_, _length_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L149-L165)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.get_normal_points "Link to this definition")

For a line passing through (_cx_, _cy_) and having an angle _t_, return locations of the two points located along its perpendicular line at the distance of _length_.

matplotlib.bezier.get\_parallels(_bezier2_, _width_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L558-L629)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.get_parallels "Link to this definition")

Given the quadratic Bézier control points _bezier2_, returns control points of quadratic Bézier lines roughly parallel to given one separated by _width_.

matplotlib.bezier.inside\_circle(_cx_, _cy_, _r_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L500-L514)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.inside_circle "Link to this definition")

Return a function that checks whether a point is in a circle with center (_cx_, _cy_) and radius _r_.

The returned function has the signature:

f(xy: tuple\[float, float\]) \-> bool

matplotlib.bezier.make\_wedged\_bezier2(_bezier2_, _width_, _w1\=1.0_, _wm\=0.5_, _w2\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L642-L690)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.make_wedged_bezier2 "Link to this definition")

Being similar to [`get_parallels`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.get_parallels "matplotlib.bezier.get_parallels")
, returns control points of two quadratic Bézier lines having a width roughly parallel to given one separated by _width_.

matplotlib.bezier.split\_bezier\_intersecting\_with\_closedpath(_bezier_, _inside\_closedpath_, _tolerance\=0.01_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L405-L433)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.split_bezier_intersecting_with_closedpath "Link to this definition")

Split a Bézier curve into two at the intersection with a closed path.

Parameters:

**bezier**(N, 2) array-like

Control points of the Bézier segment. See [`BezierSegment`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.BezierSegment "matplotlib.bezier.BezierSegment")
.

**inside\_closedpath**callable

A function returning True if a given point (x, y) is inside the closed path. See also [`find_bezier_t_intersecting_with_closedpath`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.find_bezier_t_intersecting_with_closedpath "matplotlib.bezier.find_bezier_t_intersecting_with_closedpath")
.

**tolerance**float

The tolerance for the intersection. See also [`find_bezier_t_intersecting_with_closedpath`](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.find_bezier_t_intersecting_with_closedpath "matplotlib.bezier.find_bezier_t_intersecting_with_closedpath")
.

Returns:

left, right

Lists of control points for the two Bézier segments.

matplotlib.bezier.split\_de\_casteljau(_beta_, _t_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L179-L194)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.split_de_casteljau "Link to this definition")

Split a Bézier segment defined by its control points _beta_ into two separate segments divided at _t_ and return their control points.

matplotlib.bezier.split\_path\_inout(_path_, _inside_, _tolerance\=0.01_, _reorder\_inout\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/bezier.py#L439-L497)
[#](https://matplotlib.org/stable/api/bezier_api.html#matplotlib.bezier.split_path_inout "Link to this definition")

Divide a path into two segments at the point where `inside(x, y)` becomes False.

On this page