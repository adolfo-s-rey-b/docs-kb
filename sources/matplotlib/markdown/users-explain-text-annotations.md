[Skip to main content](https://matplotlib.org/stable/users/explain/text/annotations.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/users/explain/text/annotations.html#sphx-glr-download-users-explain-text-annotations-py)
 to download the full example code.

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#id3)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations "Link to this heading")

===============================================================================================================================================================================================

Annotations are graphical elements, often pieces of text, that explain, add context to, or otherwise highlight some portion of the visualized data. [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 supports a number of coordinate systems for flexibly positioning data and annotations relative to each other and a variety of options of for styling the text. Axes.annotate also provides an optional arrow from the text to the data and this arrow can be styled in various ways. [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
 can also be used for simple text annotation, but does not provide as much flexibility in positioning and styling as [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
.

[Basic annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#id4)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#basic-annotation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In an annotation, there are two points to consider: the location of the data being annotated _xy_ and the location of the annotation text _xytext_. Both of these arguments are `(x, y)` tuples:

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))

[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 5.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2)

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('local max', [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=(2, 1), xytext\=(3, 1.5),
            arrowprops\=dict(facecolor\='black', shrink\=0.05))
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-2, 2)

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_001_2_00x.png)

In this example, both the _xy_ (arrow tip) and _xytext_ locations (text location) are in data coordinates. There are a variety of other coordinate systems one can choose -- you can specify the coordinate system of _xy_ and _xytext_ with one of the following strings for _xycoords_ and _textcoords_ (default is 'data')

| argument | coordinate system |
| --- | --- |
| 'figure points' | points from the lower left corner of the figure |
| 'figure pixels' | pixels from the lower left corner of the figure |
| 'figure fraction' | (0, 0) is lower left of figure and (1, 1) is upper right |
| 'axes points' | points from lower left corner of the Axes |
| 'axes pixels' | pixels from lower left corner of the Axes |
| 'axes fraction' | (0, 0) is lower left of Axes and (1, 1) is upper right |
| 'data' | use the axes data coordinate system |

The following strings are also valid arguments for _textcoords_

| argument | coordinate system |
| --- | --- |
| 'offset points' | offset (in points) from the xy value |
| 'offset pixels' | offset (in pixels) from the xy value |

For physical coordinate systems (points or pixels) the origin is the bottom-left of the figure or Axes. Points are [typographic points](https://en.wikipedia.org/wiki/Point_(typography))
 meaning that they are a physical unit measuring 1/72 of an inch. Points and pixels are discussed in further detail in [Plotting in physical coordinates](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-fig-scale-dpi)
.

### [Annotating data](https://matplotlib.org/stable/users/explain/text/annotations.html#id5)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-data "Link to this heading")

This example places the text coordinates in fractional axes coordinates:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))

[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 5.0, 0.01)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=2)

[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('local max', [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=(2, 1), xycoords\='data',
            xytext\=(0.01, .99), textcoords\='axes fraction',
            va\='top', ha\='left',
            arrowprops\=dict(facecolor\='black', shrink\=0.05))
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-2, 2)

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_002_2_00x.png)

### [Annotating an Artist](https://matplotlib.org/stable/users/explain/text/annotations.html#id6)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-an-artist "Link to this heading")

Annotations can be positioned relative to an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 instance by passing that Artist in as _xycoords_. Then _xy_ is interpreted as a fraction of the Artist's bounding box.

import matplotlib.patches as mpatches

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))
[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [mpatches.FancyArrowPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
((1.25, 1.5), (1.75, 1.5),
                               arrowstyle\='->,head\_width=.15', mutation\_scale\=20)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
("label", (.5, .5), xycoords\=[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, ha\='center', va\='bottom')
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(1, 2), ylim\=(1, 2))

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_003_2_00x.png)

Here the annotation is placed at position (.5,.5) relative to the arrow's lower left corner and is vertically and horizontally at that position. Vertically, the bottom aligns to that reference point so that the label is above the line. For an example of chaining annotation Artists, see the [Artist section](https://matplotlib.org/stable/users/explain/text/annotations.html#artist-annotation-coord)
 of [Coordinate systems for annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-coordinate-systems)
.

### [Annotating with arrows](https://matplotlib.org/stable/users/explain/text/annotations.html#id7)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-with-arrows "Link to this heading")

You can enable drawing of an arrow from the text to the annotated point by giving a dictionary of arrow properties in the optional keyword argument _arrowprops_.

| _arrowprops_ key | description |
| --- | --- |
| width | the width of the arrow in points |
| frac | the fraction of the arrow length occupied by the head |
| headwidth | the width of the base of the arrow head in points |
| shrink | move the tip and base some percent away from the annotated point and text |
| \*\*kwargs | any key for [`matplotlib.patches.Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")<br>, e.g., `facecolor` |

In the example below, the _xy_ point is in the data coordinate system since _xycoords_ defaults to 'data'. For a polar Axes, this is in (theta, radius) space. The text in this example is placed in the fractional figure coordinate system. [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 keyword arguments like _horizontalalignment_, _verticalalignment_ and _fontsize_ are passed from [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
 to the `Text` instance.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='polar')
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 0.001)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='#ee8d18', lw\=3)

[ind](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 800
[thisr](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [thistheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[ind](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[ind](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[[thistheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
\], \[[thisr](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
\], 'o')
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
('a polar annotation',
            [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=([thistheta](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [thisr](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
),  \# theta, radius
            xytext\=(0.05, 0.05),    \# fraction, fraction
            textcoords\='figure fraction',
            arrowprops\=dict(facecolor\='black', shrink\=0.05),
            horizontalalignment\='left',
            verticalalignment\='bottom')

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_004_2_00x.png)

For more on plotting with arrows, see [Customizing annotation arrows](https://matplotlib.org/stable/users/explain/text/annotations.html#annotation-with-custom-arrow)

### [Placing text annotations relative to data](https://matplotlib.org/stable/users/explain/text/annotations.html#id8)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#placing-text-annotations-relative-to-data "Link to this heading")

Annotations can be positioned at a relative offset to the _xy_ input to annotation by setting the _textcoords_ keyword argument to `'offset points'` or `'offset pixels'`.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[1, 3, 5, 7, 9\]
[y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[2, 4, 6, 8, 10\]
[annotations](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["A", "B", "C", "D", "E"\]
[ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=20)

for [xi](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [yi](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 in zip([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [annotations](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
([text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
,
                [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=([xi](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [yi](https://docs.python.org/3/library/functions.html#int "builtins.int")
), xycoords\='data',
                xytext\=(1.5, 1.5), textcoords\='offset points')

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_005_2_00x.png)

The annotations are offset 1.5 points (1.5\*1/72 inches) from the _xy_ values.

[Advanced annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#id9)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#advanced-annotation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We recommend reading [Basic annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations-tutorial)
, [`text()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
 and [`annotate()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")
 before reading this section.

### [Annotating with boxed text](https://matplotlib.org/stable/users/explain/text/annotations.html#id10)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#annotating-with-boxed-text "Link to this heading")

[`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
 takes a _bbox_ keyword argument, which draws a box around the text:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5, 5))
[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, "Direction",
            ha\="center", va\="center", rotation\=45, size\=15,
            bbox\=dict(boxstyle\="rarrow,pad=0.3",
                      fc\="lightblue", ec\="steelblue", lw\=2))

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_006_2_00x.png)

The arguments are the name of the box style with its attributes as keyword arguments. Currently, following box styles are implemented:

| Class | Name | Attrs |
| --- | --- | --- |
| Circle | `circle` | pad=0.3 |
| DArrow | `darrow` | pad=0.3,head\_width=1.5,head\_angle=90 |
| Ellipse | `ellipse` | pad=0.3 |
| LArrow | `larrow` | pad=0.3,head\_width=1.5,head\_angle=90 |
| RArrow | `rarrow` | pad=0.3,head\_width=1.5,head\_angle=90 |
| Round | `round` | pad=0.3,rounding\_size=None |
| Round4 | `round4` | pad=0.3,rounding\_size=None |
| Roundtooth | `roundtooth` | pad=0.3,tooth\_size=None |
| Sawtooth | `sawtooth` | pad=0.3,tooth\_size=None |
| Square | `square` | pad=0.3 |

[![../../../_images/sphx_glr_fancybox_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_fancybox_demo_001.png)](https://matplotlib.org/gallery/shapes_and_collections/fancybox_demo.html)

The patch object (box) associated with the text can be accessed using:

bb \= [t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.get\_bbox\_patch()

The return value is a [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
; patch properties (facecolor, edgewidth, etc.) can be accessed and modified as usual. [`FancyBboxPatch.set_boxstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch.set_boxstyle "matplotlib.patches.FancyBboxPatch.set_boxstyle")
 sets the box shape:

bb.set\_boxstyle("rarrow", pad\=0.6)

The attribute arguments can also be specified within the style name with separating comma:

bb.set\_boxstyle("rarrow, pad=0.6")

### [Defining custom box styles](https://matplotlib.org/stable/users/explain/text/annotations.html#id11)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#defining-custom-box-styles "Link to this heading")

Custom box styles can be implemented as a function that takes arguments specifying both a rectangular box and the amount of "mutation", and returns the "mutated" path. The specific signature is the one of `custom_box_style` below.

Here, we return a new path which adds an "arrow" shape on the left of the box.

The custom box style can then be used by passing `bbox=dict(boxstyle=custom_box_style, ...)` to [`Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
.

from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

def custom\_box\_style(x0, y0, width, height, mutation\_size):
    """
    Given the location and size of the box, return the path of the box around it.

    Rotation is automatically taken care of.

    Parameters
    ----------
    x0, y0, width, height : float
       Box location and size.
    mutation\_size : float
        Mutation reference scale, typically the text font size.
    """
    \# padding
    mypad \= 0.3
    pad \= mutation\_size \* mypad
    \# width and height with padding added.
    width \= width + 2 \* pad
    height \= height + 2 \* pad
    \# boundary of the padded box
    x0, y0 \= x0 \- pad, y0 \- pad
    x1, y1 \= x0 + width, y0 + height
    \# return the new path
    return [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(\[(x0, y0), (x1, y0), (x1, y1), (x0, y1),\
                 (x0\-pad, (y0+y1)/2), (x0, y0), (x0, y0)\],
                closed\=True)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, "Test", size\=30, va\="center", ha\="center", rotation\=30,
        bbox\=dict(boxstyle\=custom\_box\_style, alpha\=0.2))

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_007_2_00x.png)

Likewise, custom box styles can be implemented as classes that implement `__call__`.

The classes can then be registered into the `BoxStyle._style_list` dict, which allows specifying the box style as a string, `bbox=dict(boxstyle="registered_name,param=value,...", ...)`. Note that this registration relies on internal APIs and is therefore not officially supported.

from matplotlib.patches import BoxStyle

class MyStyle:
    """A simple box."""

    def \_\_init\_\_(self, pad\=0.3):
        """
        The arguments must be floats and have default values.

        Parameters
        ----------
        pad : float
            amount of padding
        """
        self.pad \= pad
        super().\_\_init\_\_()

    def \_\_call\_\_(self, x0, y0, width, height, mutation\_size):
        """
        Given the location and size of the box, return the path of the box around it.

        Rotation is automatically taken care of.

        Parameters
        ----------
        x0, y0, width, height : float
            Box location and size.
        mutation\_size : float
            Reference scale for the mutation, typically the text font size.
        """
        \# padding
        pad \= mutation\_size \* self.pad
        \# width and height with padding added
        width \= width + 2 \* pad
        height \= height + 2 \* pad
        \# boundary of the padded box
        x0, y0 \= x0 \- pad, y0 \- pad
        x1, y1 \= x0 + width, y0 + height
        \# return the new path
        return [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(\[(x0, y0), (x1, y0), (x1, y1), (x0, y1),\
                     (x0\-pad, (y0+y1)/2), (x0, y0), (x0, y0)\],
                    closed\=True)

[BoxStyle.\_style\_list](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["angled"\] \= MyStyle  \# Register the custom style.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))
[ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, "Test", size\=30, va\="center", ha\="center", rotation\=30,
        bbox\=dict(boxstyle\="angled,pad=0.5", alpha\=0.2))

del [BoxStyle.\_style\_list](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["angled"\]  \# Unregister it.

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_008_2_00x.png)

Similarly, you can define a custom [`ConnectionStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionStyle.html#matplotlib.patches.ConnectionStyle "matplotlib.patches.ConnectionStyle")
 and a custom [`ArrowStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ArrowStyle.html#matplotlib.patches.ArrowStyle "matplotlib.patches.ArrowStyle")
. View the source code at [`patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
 to learn how each class is defined.

### [Customizing annotation arrows](https://matplotlib.org/stable/users/explain/text/annotations.html#id12)
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#customizing-annotation-arrows "Link to this heading")

An arrow connecting _xy_ to _xytext_ can be optionally drawn by specifying the _arrowprops_ argument. To draw only an arrow, use empty string as the first argument:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(3, 3))
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
("",
            [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=(0.2, 0.2), xycoords\='data',
            xytext\=(0.8, 0.8), textcoords\='data',
            arrowprops\=dict(arrowstyle\="->", connectionstyle\="arc3"))

![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_009_2_00x.png)

The arrow is drawn as follows:

1.  A path connecting the two points is created, as specified by the _connectionstyle_ parameter.
    
2.  The path is clipped to avoid patches _patchA_ and _patchB_, if these are set.
    
3.  The path is further shrunk by _shrinkA_ and _shrinkB_ (in pixels).
    
4.  The path is transmuted to an arrow patch, as specified by the _arrowstyle_ parameter.
    

([`2x.png`](https://matplotlib.org/stable/_downloads/4dca774e0ef5239d7c4308501dbcf705/annotations-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/04ef7105644b726ea0a286a27578b233/annotations-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-text-annotations-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-text-annotations-1.2x.png)

The creation of the connecting path between two points is controlled by `connectionstyle` key and the following styles are available:

| Name | Attrs |
| --- | --- |
| `angle` | angleA=90,angleB=0,rad=0.0 |
| `angle3` | angleA=90,angleB=0 |
| `arc` | angleA=0,angleB=0,armA=None,armB=None,rad=0.0 |
| `arc3` | rad=0.0 |
| `bar` | armA=0.0,armB=0.0,fraction=0.3,angle=None |

Note that "3" in `angle3` and `arc3` is meant to indicate that the resulting path is a quadratic spline segment (three control points). As will be discussed below, some arrow style options can only be used when the connecting path is a quadratic spline.

The behavior of each connection style is (limitedly) demonstrated in the example below. (Warning: The behavior of the `bar` style is currently not well-defined and may be changed in the future).

([`Source code`](https://matplotlib.org/stable/_downloads/45760bc4b11f4b37b071b779830f1b03/annotations-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d73f23abb4fd9e024c93f0d6415a7a1e/annotations-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/23cad79f0441c86a82903c1ae30be4d9/annotations-2.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-text-annotations-2.2x.png)](https://matplotlib.org/stable/_images/users-explain-text-annotations-2.2x.png)

Connection styles for annotations

The connecting path (after clipping and shrinking) is then mutated to an arrow patch, according to the given `arrowstyle`:

| Name | Attrs |
| --- | --- |
| `-` | None |
| `->` | head\_length=0.4,head\_width=0.2 |
| `-[` | widthB=1.0,lengthB=0.2,angleB=None |\
| `\|-\|` | widthA=1.0,widthB=1.0 |\
| `-\|>` | head\_length=0.4,head\_width=0.2 |\
| `<-` | head\_length=0.4,head\_width=0.2 |\
| `<->` | head\_length=0.4,head\_width=0.2 |\
| `<\|-` | head\_length=0.4,head\_width=0.2 |\
| `<\|-\|>` | head\_length=0.4,head\_width=0.2 |\
| `fancy` | head\_length=0.4,head\_width=0.4,tail\_width=0.4 |\
| `simple` | head\_length=0.5,head\_width=0.5,tail\_width=0.2 |\
| `wedge` | tail\_width=0.3,shrink\_factor=0.5 |\
\
[![../../../_images/sphx_glr_fancyarrow_demo_001.png](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_001.png)](https://matplotlib.org/gallery/text_labels_and_annotations/fancyarrow_demo.html)\
\
Some arrowstyles only work with connection styles that generate a quadratic-spline segment. They are `fancy`, `simple`, and `wedge`. For these arrow styles, you must use the "angle3" or "arc3" connection style.\
\
If the annotation string is given, the patch is set to the bbox patch of the text by default.\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
\
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test",\
            [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.2, 0.2), xycoords\='data',\
            xytext\=(0.8, 0.8), textcoords\='data',\
            size\=20, va\="center", ha\="center",\
            arrowprops\=dict(arrowstyle\="simple",\
                            connectionstyle\="arc3,rad=-0.2"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_010_2_00x.png)\
\
As with [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")\
, a box around the text can be drawn using the _bbox_ argument.\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
\
[ann](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.2, 0.2), xycoords\='data',\
                  xytext\=(0.8, 0.8), textcoords\='data',\
                  size\=20, va\="center", ha\="center",\
                  bbox\=dict(boxstyle\="round4", fc\="w"),\
                  arrowprops\=dict(arrowstyle\="-|>",\
                                  connectionstyle\="arc3,rad=-0.2",\
                                  fc\="w"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_011_2_00x.png)\
\
By default, the starting point is set to the center of the text extent. This can be adjusted with `relpos` key value. The values are normalized to the extent of the text. For example, (0, 0) means lower-left corner and (1, 1) means top-right.\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
\
[ann](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.2, 0.2), xycoords\='data',\
                  xytext\=(0.8, 0.8), textcoords\='data',\
                  size\=20, va\="center", ha\="center",\
                  bbox\=dict(boxstyle\="round4", fc\="w"),\
                  arrowprops\=dict(arrowstyle\="-|>",\
                                  connectionstyle\="arc3,rad=0.2",\
                                  relpos\=(0., 0.),\
                                  fc\="w"))\
\
[ann](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.2, 0.2), xycoords\='data',\
                  xytext\=(0.8, 0.8), textcoords\='data',\
                  size\=20, va\="center", ha\="center",\
                  bbox\=dict(boxstyle\="round4", fc\="w"),\
                  arrowprops\=dict(arrowstyle\="-|>",\
                                  connectionstyle\="arc3,rad=-0.2",\
                                  relpos\=(1., 0.),\
                                  fc\="w"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_012_2_00x.png)\
\
### [Placing Artist at anchored Axes locations](https://matplotlib.org/stable/users/explain/text/annotations.html#id13)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#placing-artist-at-anchored-axes-locations "Link to this heading")\
\
There are classes of artists that can be placed at an anchored location in the Axes. A common example is the legend. This type of artist can be created by using the [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")\
 class. A few predefined classes are available in [`matplotlib.offsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#module-matplotlib.offsetbox "matplotlib.offsetbox")\
 and in [`mpl_toolkits.axes_grid1.anchored_artists`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.html#module-mpl_toolkits.axes_grid1.anchored_artists "mpl_toolkits.axes_grid1.anchored_artists")\
.\
\
from matplotlib.offsetbox import [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
[at](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")\
 \= [AnchoredText](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")\
("Figure 1a",\
                  prop\=dict(size\=15), frameon\=True, loc\='upper left')\
[at.patch.set\_boxstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch.set_boxstyle "matplotlib.patches.FancyBboxPatch.set_boxstyle")\
("round,pad=0.,rounding\_size=0.2")\
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
([at](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredText "matplotlib.offsetbox.AnchoredText")\
)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_013_2_00x.png)\
\
The _loc_ keyword has same meaning as in the legend command.\
\
A simple application is when the size of the artist (or collection of artists) is known in pixel size during the time of creation. For example, If you want to draw a circle with fixed size of 20 pixel x 20 pixel (radius = 10 pixel), you can utilize [`AnchoredDrawingArea`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")\
. The instance is created with a size of the drawing area (in pixels), and arbitrary artists can be added to the drawing area. Note that the extents of the artists that are added to the drawing area are not related to the placement of the drawing area itself. Only the initial size matters.\
\
The artists that are added to the drawing area should not have a transform set (it will be overridden) and the dimensions of those artists are interpreted as a pixel coordinate, i.e., the radius of the circles in above example are 10 pixels and 5 pixels, respectively.\
\
from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
from mpl\_toolkits.axes\_grid1.anchored\_artists import [AnchoredDrawingArea](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
[ada](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")\
 \= [AnchoredDrawingArea](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")\
(40, 20, 0, 0,\
                          loc\='upper right', pad\=0., frameon\=False)\
[p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
 \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
((10, 10), 10)\
[ada.drawing\_area.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")\
([p1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
)\
[p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
 \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
((30, 10), 5, fc\="r")\
[ada.drawing\_area.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")\
([p2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
)\
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
([ada](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")\
)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_014_2_00x.png)\
\
Sometimes, you want your artists to scale with the data coordinate (or coordinates other than canvas pixels). You can use [`AnchoredAuxTransformBox`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox "mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox")\
 class. This is similar to [`AnchoredDrawingArea`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea "mpl_toolkits.axes_grid1.anchored_artists.AnchoredDrawingArea")\
 except that the extent of the artist is determined during the drawing time respecting the specified transform.\
\
The ellipse in the example below will have width and height corresponding to 0.1 and 0.4 in data coordinates and will be automatically scaled when the view limits of the Axes change.\
\
from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
from mpl\_toolkits.axes\_grid1.anchored\_artists import [AnchoredAuxTransformBox](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox "mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox")\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
[box](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
 \= [AnchoredAuxTransformBox](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox "mpl_toolkits.axes_grid1.anchored_artists.AnchoredAuxTransformBox")\
([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")\
, loc\='upper left')\
[el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
((0, 0), width\=0.1, height\=0.4, angle\=30)  \# in data coordinates!\
[box.drawing\_area.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
([el](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
)\
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
([box](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_015_2_00x.png)\
\
Another method of anchoring an artist relative to a parent Axes or anchor point is via the _bbox\_to\_anchor_ argument of [`AnchoredOffsetbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")\
. This artist can then be automatically positioned relative to another artist using [`HPacker`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
 and [`VPacker`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.VPacker "matplotlib.offsetbox.VPacker")\
:\
\
from matplotlib.offsetbox import ([AnchoredOffsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")\
, [DrawingArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
, [HPacker](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
,\
                                  [TextArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")\
)\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
\
[box1](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")\
 \= [TextArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")\
(" Test: ", textprops\=dict(color\="k"))\
[box2](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
 \= [DrawingArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
(60, 20, 0, 0)\
\
[el1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
((10, 10), width\=16, height\=5, angle\=30, fc\="r")\
[el2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
((30, 10), width\=16, height\=5, angle\=170, fc\="g")\
[el3](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
 \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
((50, 10), width\=16, height\=5, angle\=230, fc\="b")\
[box2.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")\
([el1](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
)\
[box2.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")\
([el2](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
)\
[box2.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")\
([el3](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
)\
\
[box](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
 \= [HPacker](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
(children\=\[[box1](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")\
, [box2](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
\],\
              align\="center",\
              pad\=0, sep\=5)\
\
[anchored\_box](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")\
 \= [AnchoredOffsetbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")\
(loc\='lower left',\
                                 child\=[box](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.HPacker "matplotlib.offsetbox.HPacker")\
, pad\=0.,\
                                 frameon\=True,\
                                 bbox\_to\_anchor\=(0., 1.02),\
                                 bbox\_transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")\
,\
                                 borderpad\=0.,)\
\
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
([anchored\_box](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnchoredOffsetbox "matplotlib.offsetbox.AnchoredOffsetbox")\
)\
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")\
(top\=0.8)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_016_2_00x.png)\
\
Note that, unlike in [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")\
, the `bbox_transform` is set to [`IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")\
 by default\
\
### [Using an Artist as an annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#id14)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#using-an-artist-as-an-annotation "Link to this heading")\
\
[`AnnotationBbox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
 uses artists in [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")\
 container artists as the annotations and supports positioning these annotations using the same coordinate systems as the other annotation methods. For more examples, see [Artists as annotations](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html)\
\
from matplotlib.offsetbox import [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
, [DrawingArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
, [OffsetImage](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")\
from matplotlib.patches import [Annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
\
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")\
(.2, .8, "Green!", color\='green')\
\
[da](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
 \= [DrawingArea](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
(20, 20)\
[annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")\
 \= [Annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")\
((10, 10), 10, 5, color\='tab:green')\
[da.add\_artist](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea.add_artist "matplotlib.offsetbox.DrawingArea.add_artist")\
([annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")\
)\
\
\# position annulus relative to text\
[ab1](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
([da](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")\
, [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(.5, 0),\
                     xybox\=(.5, .25),\
                     xycoords\=[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
,\
                     boxcoords\=([text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
, "data"),\
                     arrowprops\=dict(arrowstyle\="->"),\
                     bboxprops\=dict(alpha\=0.5))\
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
([ab1](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
)\
\
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 \= 25\
[arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \= [np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")\
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 1, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
), [N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
).reshape([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
)\
[im](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")\
 \= [OffsetImage](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")\
([arr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, cmap\='Greens')\
[im.image.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.axes.html#matplotlib.artist.Artist.axes "matplotlib.artist.Artist.axes")\
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\
\# position gradient relative to text and annulus\
[ab2](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
 \= [AnnotationBbox](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
([im](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetImage "matplotlib.offsetbox.OffsetImage")\
, [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(.5, 0),\
                     xybox\=(.75, 0),\
                     xycoords\=[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
,\
                     boxcoords\=('data', [annulus](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Annulus.html#matplotlib.patches.Annulus "matplotlib.patches.Annulus")\
),\
                     arrowprops\=dict(arrowstyle\="->"),\
                     bboxprops\=dict(alpha\=0.5))\
[ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")\
([ab2](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox "matplotlib.offsetbox.AnnotationBbox")\
)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_017_2_00x.png)\
\
[Coordinate systems for annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#id15)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#coordinate-systems-for-annotations "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Matplotlib Annotations support several types of coordinate systems. The examples in [Basic annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations-tutorial)\
 used the `data` coordinate system; Some others more advanced options are:\
\
### [](https://matplotlib.org/stable/users/explain/text/annotations.html#id16)\
[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
 instance[#](https://matplotlib.org/stable/users/explain/text/annotations.html#transform-instance "Link to this heading")\
\
Transforms map coordinates into different coordinate systems, usually the display coordinate system. See [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)\
 for a detailed explanation. Here Transform objects are used to identify the coordinate system of the corresponding points. For example, the `Axes.transAxes` transform positions the annotation relative to the Axes coordinates; therefore using it is identical to setting the coordinate system to "axes fraction":\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=1, ncols\=2, figsize\=(6, 3))\
[ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.2, 0.2), xycoords\=[ax1.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")\
)\
[ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.2, 0.2), xycoords\="axes fraction")\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_018_2_00x.png)\
\
Another commonly used [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
 instance is `Axes.transData`. This transform is the coordinate system of the data plotted in the Axes. In this example, it is used to draw an arrow between related data points in two Axes. We have passed an empty text because in this case, the annotation connects data points.\
\
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(\-1, 1)\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=1, ncols\=2, figsize\=(6, 3))\
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")\
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, \-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\*\*3)\
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")\
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, \-3\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\*\*2)\
[ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("",\
             [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0, 0), xycoords\=[ax1.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")\
,\
             xytext\=(0, 0), textcoords\=[ax2.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")\
,\
             arrowprops\=dict(arrowstyle\="<->"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_019_2_00x.png)\
\
### [](https://matplotlib.org/stable/users/explain/text/annotations.html#id17)\
[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")\
 instance[#](https://matplotlib.org/stable/users/explain/text/annotations.html#artist-instance "Link to this heading")\
\
The _xy_ value (or _xytext_) is interpreted as a fractional coordinate of the bounding box (bbox) of the artist:\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=1, ncols\=1, figsize\=(3, 3))\
[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 1",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.5, 0.5), xycoords\="data",\
                  va\="center", ha\="center",\
                  bbox\=dict(boxstyle\="round", fc\="w"))\
\
[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 2",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(1, 0.5), xycoords\=[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
,  \# (1, 0.5) of an1's bbox\
                  xytext\=(30, 0), textcoords\="offset points",\
                  va\="center", ha\="left",\
                  bbox\=dict(boxstyle\="round", fc\="w"),\
                  arrowprops\=dict(arrowstyle\="->"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_020_2_00x.png)\
\
Note that you must ensure that the extent of the coordinate artist (_an1_ in this example) is determined before _an2_ gets drawn. Usually, this means that _an2_ needs to be drawn after _an1_. The base class for all bounding boxes is [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")\
\
### [Callable that returns](https://matplotlib.org/stable/users/explain/text/annotations.html#id18)\
 [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
 of [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#callable-that-returns-transform-of-bboxbase "Link to this heading")\
\
A callable object that takes the renderer instance as single argument, and returns either a [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")\
 or a [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")\
. For example, the return value of [`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")\
 is a bbox, so this method is identical to (2) passing in the artist:\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=1, ncols\=1, figsize\=(3, 3))\
[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 1",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.5, 0.5), xycoords\="data",\
                  va\="center", ha\="center",\
                  bbox\=dict(boxstyle\="round", fc\="w"))\
\
[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 2",\
                  [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(1, 0.5), xycoords\=[an1.get\_window\_extent](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.get_window_extent "matplotlib.text.Annotation.get_window_extent")\
,\
                  xytext\=(30, 0), textcoords\="offset points",\
                  va\="center", ha\="left",\
                  bbox\=dict(boxstyle\="round", fc\="w"),\
                  arrowprops\=dict(arrowstyle\="->"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_021_2_00x.png)\
\
[`Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")\
 is the bounding box of the Axes object and is therefore identical to setting the coordinate system to axes fraction:\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=1, ncols\=2, figsize\=(6, 3))\
\
[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test1", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.5, 0.5), xycoords\="axes fraction")\
[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 2", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.5, 0.5), xycoords\=[ax2.get\_window\_extent](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_window_extent.html#matplotlib.axes.Axes.get_window_extent "matplotlib.axes.Axes.get_window_extent")\
)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_022_2_00x.png)\
\
### [Blended coordinate specification](https://matplotlib.org/stable/users/explain/text/annotations.html#id19)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#blended-coordinate-specification "Link to this heading")\
\
A blended pair of coordinate specifications -- the first for the x-coordinate, and the second is for the y-coordinate. For example, x=0.5 is in data coordinates, and y=1 is in normalized axes coordinates:\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.5, 1), xycoords\=("data", "axes fraction"))\
[ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")\
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\=.5, color\='lightgray')\
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")\
(xlim\=(0, 2), ylim\=(1, 2))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_023_2_00x.png)\
\
Any of the supported coordinate systems can be used in a blended specification. For example, the text "Anchored to 1 & 2" is positioned relative to the two [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 Artists:\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
\
[t1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")\
(0.05, .05, "Text 1", va\='bottom', ha\='left')\
[t2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
 \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")\
(0.90, .90, "Text 2", ha\='right')\
[t3](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Anchored to 1 & 2", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0, 0), xycoords\=([t1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
, [t2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")\
),\
                 va\='bottom', color\='tab:orange',)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_024_2_00x.png)\
\
### [](https://matplotlib.org/stable/users/explain/text/annotations.html#id20)\
[`text.OffsetFrom`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#text-offsetfrom "Link to this heading")\
\
Sometimes, you want your annotation with some "offset points", not from the annotated point but from some other point or artist. [`text.OffsetFrom`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")\
 is a helper for such cases.\
\
from matplotlib.text import [OffsetFrom](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(3, 3))\
[an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 1", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.5, 0.5), xycoords\="data",\
                  va\="center", ha\="center",\
                  bbox\=dict(boxstyle\="round", fc\="w"))\
\
[offset\_from](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")\
 \= [OffsetFrom](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")\
([an1](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
, (0.5, 0))\
[an2](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
("Test 2", [xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
\=(0.1, 0.1), xycoords\="data",\
                  xytext\=(0, \-10), textcoords\=[offset\_from](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.OffsetFrom "matplotlib.text.OffsetFrom")\
,\
                  \# xytext is offset points from "xy=(0.5, 0), xycoords=an1"\
                  va\="top", ha\="center",\
                  bbox\=dict(boxstyle\="round", fc\="w"),\
                  arrowprops\=dict(arrowstyle\="->"))\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_025_2_00x.png)\
\
[Non-text annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#id21)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#non-text-annotations "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### [Using ConnectionPatch](https://matplotlib.org/stable/users/explain/text/annotations.html#id22)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#using-connectionpatch "Link to this heading")\
\
[`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
 is like an annotation without text. While [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")\
 is sufficient in most situations, [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
 is useful when you want to connect points in different Axes. For example, here we connect the point _xy_ in the data coordinates of `ax1` to point _xy_ in the data coordinates of `ax2`:\
\
from matplotlib.patches import [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(nrows\=1, ncols\=2, figsize\=(6, 3))\
[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
 \= (0.3, 0.2)\
[con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
 \= [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
(xyA\=[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, coordsA\=[ax1.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")\
,\
                      xyB\=[xy](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, coordsB\=[ax2.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")\
)\
\
[fig.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")\
([con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
)\
\
![annotations](https://matplotlib.org/stable/_images/sphx_glr_annotations_026_2_00x.png)\
\
Here, we added the [`ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")\
 to the _figure_ (with [`add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist")\
) rather than to either Axes. This ensures that the ConnectionPatch artist is drawn on top of both Axes, and is also necessary when using [constrained\_layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)\
 for positioning the Axes.\
\
### [Zoom effect between Axes](https://matplotlib.org/stable/users/explain/text/annotations.html#id23)\
[#](https://matplotlib.org/stable/users/explain/text/annotations.html#zoom-effect-between-axes "Link to this heading")\
\
[`mpl_toolkits.axes_grid1.inset_locator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.inset_locator.html#module-mpl_toolkits.axes_grid1.inset_locator "mpl_toolkits.axes_grid1.inset_locator")\
 defines some patch classes useful for interconnecting two Axes.\
\
[![../../../_images/sphx_glr_axes_zoom_effect_001.png](https://matplotlib.org/stable/_images/sphx_glr_axes_zoom_effect_001.png)](https://matplotlib.org/gallery/subplots_axes_and_figures/axes_zoom_effect.html)\
\
The code for this figure is at [Axes zoom effect](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axes_zoom_effect.html)\
 and familiarity with [Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)\
 is recommended.\
\
**Total running time of the script:** (0 minutes 6.873 seconds)\
\
[`Download Jupyter notebook: annotations.ipynb`](https://matplotlib.org/stable/_downloads/34b71ff3911c646d75af535140c8fb6e/annotations.ipynb)\
\
[`Download Python source code: annotations.py`](https://matplotlib.org/stable/_downloads/d4f5244fb548ebe6e67e43884bdbc4d4/annotations.py)\
\
[`Download zipped: annotations.zip`](https://matplotlib.org/stable/_downloads/4eeee63c8489a7cd7ea0d4b9877fd27e/annotations.zip)\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page