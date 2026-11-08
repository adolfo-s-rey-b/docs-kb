[Skip to main content](https://matplotlib.org/stable/api/hatch_api.html#main-content)

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
    

`matplotlib.hatch`[#](https://matplotlib.org/stable/api/hatch_api.html#module-matplotlib.hatch "Link to this heading")

=======================================================================================================================

Module for generating hatch patterns.

For examples of using the hatch API, see [Hatch style reference](https://matplotlib.org/stable/gallery/shapes_and_collections/hatch_style_reference.html#sphx-glr-gallery-shapes-and-collections-hatch-style-reference-py)
.

The following hatching patterns are available, shown here at level 2 density:

([`Source code`](https://matplotlib.org/stable/_downloads/69200257c0deeea8b15ccdeead409e3c/hatch_classes.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/342b781cd3947e280f3496bd9d6ef14c/hatch_classes.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5ac6dd752af9a2f4e35d15f662d85754/hatch_classes.png)
)

[![8 squares, each showing the pattern corresponding to the hatch symbol: symbol '/' makes right leaning diagonals, '\' makes left leaning diagonals, '|' makes vertical lines, '-' makes horizontal lines, '+' makes a grid, 'X' makes a grid rotated 90 degrees, 'o' makes small unfilled circles, 'O' makes large unfilled circles, '.' makes small filled circles, and '*' makes a star with 5 points](https://matplotlib.org/stable/_images/api-hatch_classes.2x.png)](https://matplotlib.org/stable/_images/api-hatch_classes.2x.png)

class matplotlib.hatch.Circles(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L141-L146)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Circles "Link to this definition")

Bases: [`Shapes`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Shapes "matplotlib.hatch.Shapes")

class matplotlib.hatch.HatchPatternBase[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L26-L28)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HatchPatternBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

The base class for a hatch pattern.

class matplotlib.hatch.HorizontalHatch(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L31-L45)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HorizontalHatch "Link to this definition")

Bases: [`HatchPatternBase`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HatchPatternBase "matplotlib.hatch.HatchPatternBase")

set\_vertices\_and\_codes(_vertices_, _codes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L36-L45)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HorizontalHatch.set_vertices_and_codes "Link to this definition")

class matplotlib.hatch.LargeCircles(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L157-L162)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.LargeCircles "Link to this definition")

Bases: [`Circles`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Circles "matplotlib.hatch.Circles")

size \= 0.35[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.LargeCircles.size "Link to this definition")

class matplotlib.hatch.NorthEastHatch(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L65-L81)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.NorthEastHatch "Link to this definition")

Bases: [`HatchPatternBase`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HatchPatternBase "matplotlib.hatch.HatchPatternBase")

set\_vertices\_and\_codes(_vertices_, _codes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L74-L81)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.NorthEastHatch.set_vertices_and_codes "Link to this definition")

class matplotlib.hatch.Shapes(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L104-L138)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Shapes "Link to this definition")

Bases: [`HatchPatternBase`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HatchPatternBase "matplotlib.hatch.HatchPatternBase")

filled \= False[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Shapes.filled "Link to this definition")

set\_vertices\_and\_codes(_vertices_, _codes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L118-L138)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Shapes.set_vertices_and_codes "Link to this definition")

class matplotlib.hatch.SmallCircles(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L149-L154)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallCircles "Link to this definition")

Bases: [`Circles`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Circles "matplotlib.hatch.Circles")

size \= 0.2[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallCircles.size "Link to this definition")

class matplotlib.hatch.SmallFilledCircles(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L165-L171)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallFilledCircles "Link to this definition")

Bases: [`Circles`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Circles "matplotlib.hatch.Circles")

filled \= True[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallFilledCircles.filled "Link to this definition")

size \= 0.1[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallFilledCircles.size "Link to this definition")

class matplotlib.hatch.SouthEastHatch(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L84-L101)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SouthEastHatch "Link to this definition")

Bases: [`HatchPatternBase`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HatchPatternBase "matplotlib.hatch.HatchPatternBase")

set\_vertices\_and\_codes(_vertices_, _codes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L94-L101)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SouthEastHatch.set_vertices_and_codes "Link to this definition")

class matplotlib.hatch.Stars(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L174-L186)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Stars "Link to this definition")

Bases: [`Shapes`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Shapes "matplotlib.hatch.Shapes")

filled \= True[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Stars.filled "Link to this definition")

size \= 0.3333333333333333[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Stars.size "Link to this definition")

class matplotlib.hatch.VerticalHatch(_hatch_, _density_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L48-L62)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.VerticalHatch "Link to this definition")

Bases: [`HatchPatternBase`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.HatchPatternBase "matplotlib.hatch.HatchPatternBase")

set\_vertices\_and\_codes(_vertices_, _codes_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L53-L62)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.VerticalHatch.set_vertices_and_codes "Link to this definition")

matplotlib.hatch.get\_path(_hatchpattern_, _density\=6_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/hatch.py#L217-L243)
[#](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.get_path "Link to this definition")

Given a hatch specifier, _hatchpattern_, generates Path to render the hatch in a unit square. _density_ is the number of lines per unit square.

On this page