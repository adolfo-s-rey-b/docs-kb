[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#main-content)

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
    

matplotlib.patches.ArrowStyle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib-patches-arrowstyle "Link to this heading")

====================================================================================================================================================================

class matplotlib.patches.ArrowStyle(_stylename_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3316-L4034)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "Link to this definition")

Bases: `_Style`

[`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
 is a container class which defines several arrowstyle classes, which is used to create an arrow path along a given path. These are mainly used with [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
.

An arrowstyle object can be either created as:

ArrowStyle.Fancy(head\_length\=.4, head\_width\=.4, tail\_width\=.4)

or:

ArrowStyle("Fancy", head\_length\=.4, head\_width\=.4, tail\_width\=.4)

or:

ArrowStyle("Fancy, head\_length=.4, head\_width=.4, tail\_width=.4")

The following classes are defined

> | Class | Name | Parameters |
> | --- | --- | --- |
> | Curve | `-` | None |
> | CurveA | `<-` | head\_length=0.4, head\_width=0.2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None, scaleB=None |
> | CurveB | `->` | head\_length=0.4, head\_width=0.2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None, scaleB=None |
> | CurveAB | `<->` | head\_length=0.4, head\_width=0.2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None, scaleB=None |
> | CurveFilledA | `<\|-` | head\_length=0.4, head\_width=0.2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None, scaleB=None |
> | CurveFilledB | `-\|>` | head\_length=0.4, head\_width=0.2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None, scaleB=None |
> | CurveFilledAB | `<\|-\|>` | head\_length=0.4, head\_width=0.2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0, scaleA=None, scaleB=None |
> | BracketA | `]-` | widthA=1.0, lengthA=0.2, angleA=0 |
> | BracketB | `-[` | widthB=1.0, lengthB=0.2, angleB=0 |\
> | BracketAB | `]-[` | widthA=1.0, lengthA=0.2, angleA=0, widthB=1.0, lengthB=0.2, angleB=0 |\
> | BarAB | `\|-\|` | widthA=1.0, angleA=0, widthB=1.0, angleB=0 |\
> | BracketCurve | `]->` | widthA=1.0, lengthA=0.2, angleA=None |
> | CurveBracket | `<-[` | widthB=1.0, lengthB=0.2, angleB=None |\
> | Simple | `simple` | head\_length=0.5, head\_width=0.5, tail\_width=0.2 |\
> | Fancy | `fancy` | head\_length=0.4, head\_width=0.4, tail\_width=0.4 |\
> | Wedge | `wedge` | tail\_width=0.3, shrink\_factor=0.5 |\
\
For an overview of the visual appearance, see [Annotation arrow style reference](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html)\
.\
\
An instance of any arrow style class is a callable object, whose call signature is:\
\
\_\_call\_\_(self, path, mutation\_size, linewidth, aspect\_ratio\=1.)\
\
and it returns a tuple of a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 instance and a boolean value. _path_ is a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 instance along which the arrow will be drawn. _mutation\_size_ and _aspect\_ratio_ have the same meaning as in [`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")\
. _linewidth_ is a line width to be stroked. This is meant to be used to correct the location of the head so that it does not overshoot the destination point, but not all classes support it.\
\
Notes\
\
_angleA_ and _angleB_ specify the orientation of the bracket, as either a clockwise or counterclockwise angle depending on the arrow type. 0 degrees means perpendicular to the line connecting the arrow's head and tail.\
\
([`Source code`](https://matplotlib.org/stable/_downloads/fe9b571e8d5df922f4bd99e3d3695c43/angles_on_bracket_arrows.py)\
, [`2x.png`](https://matplotlib.org/stable/_downloads/0cb8176bea7f2d4706d4b2e14d8589b5/angles_on_bracket_arrows_00_00.2x.png)\
, [`png`](https://matplotlib.org/stable/_downloads/dce1f7d8582b44cadf498e405a520de7/angles_on_bracket_arrows_00_00.png)\
)\
\
[![](https://matplotlib.org/stable/_images/api-_as_gen-angles_on_bracket_arrows_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-angles_on_bracket_arrows_00_00.2x.png)\
\
Return the instance of the subclass with the given style name.\
\
class BarAB(_widthA\=1.0_, _angleA\=0_, _widthB\=1.0_, _angleB\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3763-L3779)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BarAB "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with vertical bars `|` at both ends.\
\
Parameters:\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**angleA, angleB**float, default: 0 degrees\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
arrow \= '|-|'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BarAB.arrow "Link to this definition")\
\
class BracketA(_widthA\=1.0_, _lengthA\=0.2_, _angleA\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3703-L3720)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketA "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with an outward square bracket at its start.\
\
Parameters:\
\
**widthA**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA**float, default: 0.2\
\
Length of the bracket.\
\
**angleA**float, default: 0 degrees\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
arrow \= '\]-'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketA.arrow "Link to this definition")

class BracketAB(_widthA\=1.0_, _lengthA\=0.2_, _angleA\=0_, _widthB\=1.0_, _lengthB\=0.2_, _angleB\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3741-L3761)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketAB "Link to this definition")

Bases: `_Curve`

An arrow with outward square brackets at both ends.

Parameters:

**widthA, widthB**float, default: 1.0

Width of the bracket.

**lengthA, lengthB**float, default: 0.2

Length of the bracket.

**angleA, angleB**float, default: 0 degrees

Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.

arrow \= '\]-\['[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketAB.arrow "Link to this definition")\
\
class BracketB(_widthB\=1.0_, _lengthB\=0.2_, _angleB\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3722-L3739)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketB "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with an outward square bracket at its end.\
\
Parameters:\
\
**widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleB**float, default: 0 degrees\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
arrow \= '-\['[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketB.arrow "Link to this definition")\
\
class BracketCurve(_widthA\=1.0_, _lengthA\=0.2_, _angleA\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3781-L3801)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketCurve "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with an outward square bracket at its start and a head at the end.\
\
Parameters:\
\
**widthA**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA**float, default: 0.2\
\
Length of the bracket.\
\
**angleA**float, default: 0 degrees\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
arrow \= '\]->'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.BracketCurve.arrow "Link to this definition")\
\
class Curve[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3664-L3671)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Curve "Link to this definition")\
\
Bases: `_Curve`\
\
A simple curve without any arrow head.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
class CurveA(_head\_length\=0.4_, _head\_width\=0.2_, _widthA\=1.0_, _widthB\=1.0_, _lengthA\=0.2_, _lengthB\=0.2_, _angleA\=0_, _angleB\=0_, _scaleA\=None_, _scaleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3673-L3676)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveA "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with a head at its start point.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
arrow \= '<-'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveA.arrow "Link to this definition")\
\
class CurveAB(_head\_length\=0.4_, _head\_width\=0.2_, _widthA\=1.0_, _widthB\=1.0_, _lengthA\=0.2_, _lengthB\=0.2_, _angleA\=0_, _angleB\=0_, _scaleA\=None_, _scaleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3683-L3686)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveAB "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with heads both at the start and the end point.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
arrow \= '<->'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveAB.arrow "Link to this definition")\
\
class CurveB(_head\_length\=0.4_, _head\_width\=0.2_, _widthA\=1.0_, _widthB\=1.0_, _lengthA\=0.2_, _lengthB\=0.2_, _angleA\=0_, _angleB\=0_, _scaleA\=None_, _scaleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3678-L3681)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveB "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with a head at its end point.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
arrow \= '->'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveB.arrow "Link to this definition")\
\
class CurveBracket(_widthB\=1.0_, _lengthB\=0.2_, _angleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3803-L3823)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveBracket "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with an outward square bracket at its end and a head at the start.\
\
Parameters:\
\
**widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleB**float, default: 0 degrees\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
arrow \= '<-\['[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveBracket.arrow "Link to this definition")\
\
class CurveFilledA(_head\_length\=0.4_, _head\_width\=0.2_, _widthA\=1.0_, _widthB\=1.0_, _lengthA\=0.2_, _lengthB\=0.2_, _angleA\=0_, _angleB\=0_, _scaleA\=None_, _scaleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3688-L3691)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveFilledA "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with filled triangle head at the start.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
arrow \= '<|-'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveFilledA.arrow "Link to this definition")\
\
class CurveFilledAB(_head\_length\=0.4_, _head\_width\=0.2_, _widthA\=1.0_, _widthB\=1.0_, _lengthA\=0.2_, _lengthB\=0.2_, _angleA\=0_, _angleB\=0_, _scaleA\=None_, _scaleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3698-L3701)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveFilledAB "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with filled triangle heads at both ends.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
arrow \= '<|-|>'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveFilledAB.arrow "Link to this definition")\
\
class CurveFilledB(_head\_length\=0.4_, _head\_width\=0.2_, _widthA\=1.0_, _widthB\=1.0_, _lengthA\=0.2_, _lengthB\=0.2_, _angleA\=0_, _angleB\=0_, _scaleA\=None_, _scaleB\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3693-L3696)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveFilledB "Link to this definition")\
\
Bases: `_Curve`\
\
An arrow with filled triangle head at the end.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head, relative to _mutation\_size_.\
\
**head\_width**float, default: 0.2\
\
Width of the arrow head, relative to _mutation\_size_.\
\
**widthA, widthB**float, default: 1.0\
\
Width of the bracket.\
\
**lengthA, lengthB**float, default: 0.2\
\
Length of the bracket.\
\
**angleA, angleB**float, default: 0\
\
Orientation of the bracket, as a counterclockwise angle. 0 degrees means perpendicular to the line.\
\
**scaleA, scaleB**float, default: _mutation\_size_\
\
The scale of the brackets.\
\
arrow \= '-|>'[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.CurveFilledB.arrow "Link to this definition")\
\
class Fancy(_head\_length\=0.4_, _head\_width\=0.4_, _tail\_width\=0.4_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3904-L3990)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Fancy "Link to this definition")\
\
Bases: `_Base`\
\
A fancy arrow. Only works with a quadratic Bézier curve.\
\
Parameters:\
\
**head\_length**float, default: 0.4\
\
Length of the arrow head.\
\
**head\_width**float, default: 0.4\
\
Width of the arrow head.\
\
**tail\_width**float, default: 0.4\
\
Width of the arrow tail.\
\
transmute(_path_, _mutation\_size_, _linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3925-L3990)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Fancy.transmute "Link to this definition")\
\
The transmute method is the very core of the ArrowStyle class and must be overridden in the subclasses. It receives the _path_ object along which the arrow will be drawn, and the _mutation\_size_, with which the arrow head etc. will be scaled. The _linewidth_ may be used to adjust the path so that it does not pass beyond the given points. It returns a tuple of a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 instance and a boolean. The boolean value indicate whether the path can be filled or not. The return value can also be a list of paths and list of booleans of the same length.\
\
class Simple(_head\_length\=0.5_, _head\_width\=0.5_, _tail\_width\=0.2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3825-L3902)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Simple "Link to this definition")\
\
Bases: `_Base`\
\
A simple arrow. Only works with a quadratic Bézier curve.\
\
Parameters:\
\
**head\_length**float, default: 0.5\
\
Length of the arrow head.\
\
**head\_width**float, default: 0.5\
\
Width of the arrow head.\
\
**tail\_width**float, default: 0.2\
\
Width of the arrow tail.\
\
transmute(_path_, _mutation\_size_, _linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3846-L3902)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Simple.transmute "Link to this definition")\
\
The transmute method is the very core of the ArrowStyle class and must be overridden in the subclasses. It receives the _path_ object along which the arrow will be drawn, and the _mutation\_size_, with which the arrow head etc. will be scaled. The _linewidth_ may be used to adjust the path so that it does not pass beyond the given points. It returns a tuple of a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 instance and a boolean. The boolean value indicate whether the path can be filled or not. The return value can also be a list of paths and list of booleans of the same length.\
\
class Wedge(_tail\_width\=0.3_, _shrink\_factor\=0.5_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L3992-L4034)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Wedge "Link to this definition")\
\
Bases: `_Base`\
\
Wedge(?) shape. Only works with a quadratic Bézier curve. The start point has a width of the _tail\_width_ and the end point has a width of 0. At the middle, the width is _shrink\_factor\*x\*tail\_width_.\
\
Parameters:\
\
**tail\_width**float, default: 0.3\
\
Width of the tail.\
\
**shrink\_factor**float, default: 0.5\
\
Fraction of the arrow width at the middle point.\
\
transmute(_path_, _mutation\_size_, _linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L4014-L4034)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle.Wedge.transmute "Link to this definition")\
\
The transmute method is the very core of the ArrowStyle class and must be overridden in the subclasses. It receives the _path_ object along which the arrow will be drawn, and the _mutation\_size_, with which the arrow head etc. will be scaled. The _linewidth_ may be used to adjust the path so that it does not pass beyond the given points. It returns a tuple of a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
 instance and a boolean. The boolean value indicate whether the path can be filled or not. The return value can also be a list of paths and list of booleans of the same length.\
\
Examples using `matplotlib.patches.ArrowStyle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#examples-using-matplotlib-patches-arrowstyle "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://matplotlib.org/stable/_images/sphx_glr_angles_on_bracket_arrows_thumb.png)\
\
[Angle annotations on bracket arrows](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angles_on_bracket_arrows.html)\
\
Angle annotations on bracket arrows\
\
![](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_thumb.png)\
\
[Annotation arrow style reference](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html)\
\
Annotation arrow style reference\
\
On this page