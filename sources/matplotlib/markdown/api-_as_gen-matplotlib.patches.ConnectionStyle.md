[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#main-content)

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
    

matplotlib.patches.ConnectionStyle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib-patches-connectionstyle "Link to this heading")

===================================================================================================================================================================================

class matplotlib.patches.ConnectionStyle(_stylename_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2894-L3301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle "Link to this definition")

Bases: `_Style`

[`ConnectionStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle "matplotlib.patches.ConnectionStyle")
 is a container class which defines several connectionstyle classes, which is used to create a path between two points. These are mainly used with [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
.

A connectionstyle object can be either created as:

ConnectionStyle.Arc3(rad\=0.2)

or:

ConnectionStyle("Arc3", rad\=0.2)

or:

ConnectionStyle("Arc3, rad=0.2")

The following classes are defined

> | Class | Name | Parameters |
> | --- | --- | --- |
> | Arc3 | `arc3` | rad=0.0 |
> | Angle3 | `angle3` | angleA=90, angleB=0 |
> | Angle | `angle` | angleA=90, angleB=0, rad=0.0 |
> | Arc | `arc` | angleA=0, angleB=0, armA=None, armB=None, rad=0.0 |
> | Bar | `bar` | armA=0.0, armB=0.0, fraction=0.3, angle=None |

An instance of any connection style class is a callable object, whose call signature is:

\_\_call\_\_(self, posA, posB,
         patchA\=None, patchB\=None,
         shrinkA\=2., shrinkB\=2.)

and it returns a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance. _posA_ and _posB_ are tuples of (x, y) coordinates of the two points to be connected. _patchA_ (or _patchB_) is given, the returned path is clipped so that it start (or end) from the boundary of the patch. The path is further shrunk by _shrinkA_ (or _shrinkB_) which is given in points.

Return the instance of the subclass with the given style name.

class Angle(_angleA\=90_, _angleB\=0_, _rad\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3071-L3133)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Angle "Link to this definition")

Bases: `_Base`

Creates a piecewise continuous quadratic Bézier path between two points. The path has a one passing-through point placed at the intersecting point of two lines which cross the start and end point, and have a slope of _angleA_ and _angleB_, respectively. The connecting edges are rounded with _rad_.

Parameters:

**angleA**float

Starting angle of the path.

**angleB**float

Ending angle of the path.

**rad**float

Rounding radius of the edge.

connect(_posA_, _posB_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3100-L3133)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Angle.connect "Link to this definition")

class Angle3(_angleA\=90_, _angleB\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3031-L3069)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Angle3 "Link to this definition")

Bases: `_Base`

Creates a simple quadratic Bézier curve between two points. The middle control point is placed at the intersecting point of two lines which cross the start and end point, and have a slope of _angleA_ and _angleB_, respectively.

Parameters:

**angleA**float

Starting angle of the path.

**angleB**float

Ending angle of the path.

connect(_posA_, _posB_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3054-L3069)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Angle3.connect "Link to this definition")

class Arc(_angleA\=0_, _angleB\=0_, _armA\=None_, _armB\=None_, _rad\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3135-L3229)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Arc "Link to this definition")

Bases: `_Base`

Creates a piecewise continuous quadratic Bézier path between two points. The path can have two passing-through points, a point placed at the distance of _armA_ and angle of _angleA_ from point A, another point with respect to point B. The edges are rounded with _rad_.

Parameters:

**angleA**float

Starting angle of the path.

**angleB**float

Ending angle of the path.

**armA**float or None

Length of the starting arm.

**armB**float or None

Length of the ending arm.

**rad**float

Rounding radius of the edges.

connect(_posA_, _posB_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3172-L3229)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Arc.connect "Link to this definition")

class Arc3(_rad\=0.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2993-L3029)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Arc3 "Link to this definition")

Bases: `_Base`

Creates a simple quadratic Bézier curve between two points. The curve is created so that the middle control point (C1) is located at the same distance from the start (C0) and end points(C2) and the distance of the C1 to the line connecting C0-C2 is _rad_ times the distance of C0-C2.

Parameters:

**rad**float

Curvature of the curve.

connect(_posA_, _posB_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3012-L3029)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Arc3.connect "Link to this definition")

class Bar(_armA\=0.0_, _armB\=0.0_, _fraction\=0.3_, _angle\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3231-L3301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Bar "Link to this definition")

Bases: `_Base`

A line with _angle_ between A and B with _armA_ and _armB_. One of the arms is extended so that they are connected in a right angle. The length of _armA_ is determined by (_armA_ + _fraction_ x AB distance). Same for _armB_.

Parameters:

**armA**float

Minimum length of armA.

**armB**float

Minimum length of armB.

**fraction**float

A fraction of the distance between two points that will be added to armA and armB.

**angle**float or None

Angle of the connecting line (if None, parallel to A and B).

connect(_posA_, _posB_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3262-L3301)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle.Bar.connect "Link to this definition")

On this page