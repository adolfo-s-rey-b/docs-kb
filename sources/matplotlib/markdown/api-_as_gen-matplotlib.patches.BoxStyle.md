[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#main-content)

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
    

matplotlib.patches.BoxStyle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib-patches-boxstyle "Link to this heading")

==============================================================================================================================================================

class matplotlib.patches.BoxStyle(_stylename_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2488-L2891)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "Link to this definition")

Bases: `_Style`

[`BoxStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")
 is a container class which defines several boxstyle classes, which are used for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
.

A style object can be created as:

BoxStyle.Round(pad\=0.2)

or:

BoxStyle("Round", pad\=0.2)

or:

BoxStyle("Round, pad=0.2")

The following boxstyle classes are defined.

> | Class | Name | Parameters |
> | --- | --- | --- |
> | Square | `square` | pad=0.3 |
> | Circle | `circle` | pad=0.3 |
> | Ellipse | `ellipse` | pad=0.3 |
> | RArrow | `rarrow` | pad=0.3, head\_width=1.5, head\_angle=90 |
> | LArrow | `larrow` | pad=0.3, head\_width=1.5, head\_angle=90 |
> | DArrow | `darrow` | pad=0.3, head\_width=1.5, head\_angle=90 |
> | Round | `round` | pad=0.3, rounding\_size=None |
> | Round4 | `round4` | pad=0.3, rounding\_size=None |
> | Sawtooth | `sawtooth` | pad=0.3, tooth\_size=None |
> | Roundtooth | `roundtooth` | pad=0.3, tooth\_size=None |

An instance of a boxstyle class is a callable object, with the signature

\_\_call\_\_(self, x0, y0, width, height, mutation\_size) \-> Path

_x0_, _y0_, _width_ and _height_ specify the location and size of the box to be drawn; _mutation\_size_ scales the outline properties such as padding.

Return the instance of the subclass with the given style name.

class Circle(_pad\=0.3_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2543-L2562)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Circle "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A circular box.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2556-L2562)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Circle.__call__ "Link to this definition")

Call self as a function.

class DArrow(_pad\=0.3_, _head\_width\=1.5_, _head\_angle\=90_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2668-L2710)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.DArrow "Link to this definition")

Bases: [`RArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.RArrow "matplotlib.patches.BoxStyle.RArrow")

A box in the shape of a two-way arrow.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**head\_width**float, default: 1.5

The head width, relative to the arrow shaft width; must be nonnegative.

**head\_angle**float, default: 90

The angle at the tip of the arrow, in degrees; must be nonzero (modulo 360). Negative angles result in arrow heads pointing backwards.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2673-L2710)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.DArrow.__call__ "Link to this definition")

Call self as a function.

class Ellipse(_pad\=0.3_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2564-L2590)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Ellipse "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

An elliptical box.

Added in version 3.7.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2581-L2590)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Ellipse.__call__ "Link to this definition")

Call self as a function.

class LArrow(_pad\=0.3_, _head\_width\=1.5_, _head\_angle\=90_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2659-L2666)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.LArrow "Link to this definition")

Bases: [`RArrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.RArrow "matplotlib.patches.BoxStyle.RArrow")

A box in the shape of a left-pointing arrow.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**head\_width**float, default: 1.5

The head width, relative to the arrow shaft width; must be nonnegative.

**head\_angle**float, default: 90

The angle at the tip of the arrow, in degrees; must be nonzero (modulo 360). Negative angles result in arrow heads pointing backwards.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2663-L2666)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.LArrow.__call__ "Link to this definition")

Call self as a function.

class RArrow(_pad\=0.3_, _head\_width\=1.5_, _head\_angle\=90_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2592-L2657)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.RArrow "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A box in the shape of a right-pointing arrow.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**head\_width**float, default: 1.5

The head width, relative to the arrow shaft width; must be nonnegative.

**head\_angle**float, default: 90

The angle at the tip of the arrow, in degrees; must be nonzero (modulo 360). Negative angles result in arrow heads pointing backwards.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2618-L2657)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.RArrow.__call__ "Link to this definition")

Call self as a function.

class Round(_pad\=0.3_, _rounding\_size\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2712-L2768)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Round "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A box with round corners.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**rounding\_size**float, default: _pad_

Radius of the corners.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2728-L2768)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Round.__call__ "Link to this definition")

Call self as a function.

class Round4(_pad\=0.3_, _rounding\_size\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2770-L2817)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Round4 "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A box with rounded edges.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**rounding\_size**float, default: _pad_/2

Rounding of edges.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2786-L2817)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Round4.__call__ "Link to this definition")

Call self as a function.

class Roundtooth(_pad\=0.3_, _tooth\_size\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2878-L2891)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Roundtooth "Link to this definition")

Bases: [`Sawtooth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Sawtooth "matplotlib.patches.BoxStyle.Sawtooth")

A box with a rounded sawtooth outline.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**tooth\_size**float, default: _pad_/2

Size of the sawtooth.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2882-L2891)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Roundtooth.__call__ "Link to this definition")

Call self as a function.

class Sawtooth(_pad\=0.3_, _tooth\_size\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2819-L2876)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Sawtooth "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A box with a sawtooth outline.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

**tooth\_size**float, default: _pad_/2

Size of the sawtooth.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2873-L2876)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Sawtooth.__call__ "Link to this definition")

Call self as a function.

class Square(_pad\=0.3_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2520-L2541)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Square "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A square box.

Parameters:

**pad**float, default: 0.3

The amount of padding around the original box.

\_\_call\_\_(_x0_, _y0_, _width_, _height_, _mutation\_size_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patches.py#L2533-L2541)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle.Square.__call__ "Link to this definition")

Call self as a function.

Examples using `matplotlib.patches.BoxStyle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#examples-using-matplotlib-patches-boxstyle "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_thumb.png)

[Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)

Reference for Matplotlib artists

![](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_thumb.png)

[Drawing fancy boxes](https://matplotlib.org/stable/gallery/shapes_and_collections/fancybox_demo.html)

Drawing fancy boxes

On this page