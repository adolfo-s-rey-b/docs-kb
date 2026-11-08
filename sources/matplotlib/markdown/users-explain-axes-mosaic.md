[Skip to main content](https://matplotlib.org/stable/users/explain/axes/mosaic.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/axes/mosaic.html#sphx-glr-download-users-explain-axes-mosaic-py)
 to download the full example code.

Complex and semantic figure composition (subplot\_mosaic)[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#complex-and-semantic-figure-composition-subplot-mosaic "Link to this heading")

=========================================================================================================================================================================================================

Laying out Axes in a Figure in a non-uniform grid can be both tedious and verbose. For dense, even grids we have [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 but for more complex layouts, such as Axes that span multiple columns / rows of the layout or leave some areas of the Figure blank, you can use [`gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 (see [Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#arranging-axes)
) or manually place your Axes. [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 aims to provide an interface to visually lay out your Axes (as either ASCII art or nested lists) to streamline this process.

This interface naturally supports naming your Axes. [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 returns a dictionary keyed on the labels used to lay out the Figure. By returning data structures with names, it is easier to write plotting code that is independent of the Figure layout.

This is inspired by a [proposed MEP](https://github.com/matplotlib/matplotlib/pull/4384)
 and the [patchwork](https://github.com/thomasp85/patchwork)
 library for R. While we do not implement the operator overloading style, we do provide a Pythonic API for specifying (nested) Axes layouts.

import matplotlib.pyplot as plt
import numpy as np

\# Helper function used for visualization in the following examples
def identify\_axes([ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, fontsize\=48):
    """
    Helper to identify the Axes in the examples below.

    Draws the label in a large font in the center of the Axes.

    Parameters
    ----------
    ax\_dict : dict\[str, Axes\]
        Mapping between the title / label and the Axes.
    fontsize : int, optional
        How big the label should be.
    """
    kw \= dict(ha\="center", va\="center", fontsize\=fontsize, color\="darkgrey")
    for k, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.5, 0.5, k, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, \*\*kw)

If we want a 2x2 grid we can use [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 which returns a 2D array of [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 which we can index into to do our plotting.

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[hist\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1\_500)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[ax\_array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(2, 2, squeeze\=False)

[ax\_array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].bar(\["a", "b", "c"\], \[5, 7, 9\])
[ax\_array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].plot(\[1, 2, 3\])
[ax\_array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].hist([hist\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\="auto")
[ax\_array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].imshow(\[\[1, 2\], \[2, 1\]\])

identify\_axes(
    {([j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, k): a for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, r in enumerate([ax\_array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) for k, a in enumerate(r)},
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_001_2_00x.png)

Using [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 we can produce the same mosaic but give the Axes semantic names

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
(
    \[\
        \["bar", "plot"\],\
        \["hist", "image"\],\
    \],
)
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["bar"\].bar(\["a", "b", "c"\], \[5, 7, 9\])
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["plot"\].plot(\[1, 2, 3\])
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["hist"\].hist([hist\_data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["image"\].imshow(\[\[1, 2\], \[2, 1\]\])
identify\_axes([ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_002_2_00x.png)

A key difference between [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 and [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 is the return value. While the former returns an array for index access, the latter returns a dictionary mapping the labels to the [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instances created

print([ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

{'bar': <Axes: label='bar'>, 'plot': <Axes: label='plot'>, 'hist': <Axes: label='hist'>, 'image': <Axes: label='image'>}

String short-hand[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#string-short-hand "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

By restricting our Axes labels to single characters we can "draw" the Axes we want as "ASCII art". The following

[mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= """
    AB
    CD
    """

will give us 4 Axes laid out in a 2x2 grid and generates the same figure mosaic as above (but now labeled with `{"A", "B", "C", "D"}` rather than `{"bar", "plot", "hist", "image"}`).

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
([mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
identify\_axes([ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_003_2_00x.png)

Alternatively, you can use the more compact string notation

[mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= "AB;CD"

will give you the same composition, where the `";"` is used as the row separator instead of newline.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
([mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
identify\_axes([ax\_dict](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_004_2_00x.png)

Axes spanning multiple rows/columns[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#axes-spanning-multiple-rows-columns "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Something we can do with [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
, that we cannot do with [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
, is to specify that an Axes should span several rows or columns.

If we want to re-arrange our four Axes to have `"C"` be a horizontal span on the bottom and `"D"` be a vertical span on the right we would do

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    """
    ABD
    CCD
    """
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_005_2_00x.png)

If we do not want to fill in all the spaces in the Figure with Axes, we can specify some spaces in the grid to be blank

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    """
    A.C
    BBB
    .D.
    """
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_006_2_00x.png)

If we prefer to use another character (rather than a period `"."`) to mark the empty space, we can use _empty\_sentinel_ to specify the character to use.

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    """
    aX
    Xb
    """,
    empty\_sentinel\="X",
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_007_2_00x.png)

Internally there is no meaning attached to the letters we use, any Unicode code point is valid!

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    """αб
       ℝ☢"""
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_008_2_00x.png)

It is not recommended to use white space as either a label or an empty sentinel with the string shorthand because it may be stripped while processing the input.

Controlling mosaic creation[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#controlling-mosaic-creation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

This feature is built on top of [`gridspec`](https://matplotlib.org/stable/api/gridspec_api.html#module-matplotlib.gridspec "matplotlib.gridspec")
 and you can pass the keyword arguments through to the underlying [`gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 (the same as [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
).

In this case we want to use the input to specify the arrangement, but set the relative widths of the rows / columns. For convenience, [`gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
's _height\_ratios_ and _width\_ratios_ are exposed in the [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 calling sequence.

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    """
    .a.
    bAc
    .d.
    """,
    \# set the height ratios between the rows
    height\_ratios\=\[1, 3.5, 1\],
    \# set the width ratios between the columns
    width\_ratios\=\[1, 3.5, 1\],
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_009_2_00x.png)

Other [`gridspec.GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 keywords can be passed via _gridspec\_kw_. For example, use the {_left_, _right_, _bottom_, _top_} keyword arguments to position the overall mosaic to put multiple versions of the same mosaic in a figure.

[mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= """AA
            BC"""
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
(
    [mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
    gridspec\_kw\={
        "bottom": 0.25,
        "top": 0.95,
        "left": 0.1,
        "right": 0.5,
        "wspace": 0.5,
        "hspace": 0.5,
    },
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
(
    [mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
    gridspec\_kw\={
        "bottom": 0.05,
        "top": 0.75,
        "left": 0.6,
        "right": 0.95,
        "wspace": 0.5,
        "hspace": 0.5,
    },
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_010_2_00x.png)

Alternatively, you can use the sub-Figure functionality:

[mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= """AA
            BC"""
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[left](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, [right](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(nrows\=1, ncols\=2)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [left.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#matplotlib.figure.SubFigure.subplot_mosaic "matplotlib.figure.SubFigure.subplot_mosaic")
([mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [right.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#matplotlib.figure.SubFigure.subplot_mosaic "matplotlib.figure.SubFigure.subplot_mosaic")
([mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_011_2_00x.png)

Controlling subplot creation[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#controlling-subplot-creation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

We can also pass through arguments used to create the subplots (again, the same as [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
) which will apply to all of the Axes created.

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    "AB", subplot\_kw\={"projection": "polar"}
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_012_2_00x.png)

### Per-Axes subplot keyword arguments[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#per-axes-subplot-keyword-arguments "Link to this heading")

If you need to control the parameters passed to each subplot individually use _per\_subplot\_kw_ to pass a mapping between the Axes identifiers (or tuples of Axes identifiers) to dictionaries of keywords to be passed.

Added in version 3.7.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(
    "AB;CD",
    per\_subplot\_kw\={
        "A": {"projection": "polar"},
        ("C", "D"): {"xscale": "log"}
    },
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_013_2_00x.png)

If the layout is specified with the string short-hand, then we know the Axes labels will be one character and can unambiguously interpret longer strings in _per\_subplot\_kw_ to specify a set of Axes to apply the keywords to:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(
    "AB;CD",
    per\_subplot\_kw\={
        "AD": {"projection": "polar"},
        "BC": {"facecolor": ".9"}
    },
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_014_2_00x.png)

If _subplot\_kw_ and _per\_subplot\_kw_ are used together, then they are merged with _per\_subplot\_kw_ taking priority:

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    "AB;CD",
    subplot\_kw\={"facecolor": "xkcd:tangerine"},
    per\_subplot\_kw\={
        "B": {"facecolor": "xkcd:water blue"},
        "D": {"projection": "polar", "facecolor": "w"},
    }
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_015_2_00x.png)

Nested list input[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#nested-list-input "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Everything we can do with the string shorthand we can also do when passing in a list (internally we convert the string shorthand to a nested list), for example using spans, blanks, and _gridspec\_kw_:

[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    \[\
        \["main", "zoom"\],\
        \["main", "BLANK"\],\
    \],
    empty\_sentinel\="BLANK",
    width\_ratios\=\[2, 1\],
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_016_2_00x.png)

In addition, using the list input we can specify nested mosaics. Any element of the inner list can be another set of nested lists:

[inner](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    \["inner A"\],\
    \["inner B"\],\
\]

[outer\_nested\_mosaic](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    \["main", [inner](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\],\
    \["bottom", "bottom"\],\
\]
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    [outer\_nested\_mosaic](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, empty\_sentinel\=None
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, fontsize\=36)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_017_2_00x.png)

We can also pass in a 2D NumPy array to do things like

[mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((4, 4), dtype\=int)
for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(4):
    [mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
, [j](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\] \= [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 + 1
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained").subplot\_mosaic(
    [mosaic](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
    empty\_sentinel\=0,
)
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_018_2_00x.png)

Axis sharing[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#axis-sharing "Link to this heading")

------------------------------------------------------------------------------------------------------------------

[`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 supports _sharex_ and _sharey_ as does [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
. When `True`, all Axes in the mosaic share the same x-axis or y-axis, which is useful for directly comparing data across panels.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(layout\="constrained")
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
("AC;BC", sharex\=True)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["A"\].set\_title("Axes A")
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["B"\].set\_title("Axes B")
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["C"\].set\_title("Axes C")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values():
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3, 4\], \[1, 4, 2, 3\])
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![Axes A, Axes C, Axes B](https://matplotlib.org/stable/_images/sphx_glr_mosaic_019_2_00x.png)

Note that when using `sharex=True` only the bottom row of Axes shows x-axis tick labels, and when using `sharey=True` only the left column shows y-axis tick labels. This is identical to the behavior of [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
.

### Interaction with empty sentinels[#](https://matplotlib.org/stable/users/explain/axes/mosaic.html#interaction-with-empty-sentinels "Link to this heading")

When the mosaic layout has blank spaces (empty sentinels), axis sharing can produce inintended results. In the following example, there are no tick labels in the top row:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(".A;BC", sharey\=True, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values():
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3, 4\], \[1, 4, 2, 3\])
identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_020_2_00x.png)

The reason for this behavior is that sharing removes tick labels from all but the most-left / most-bottom grid positions.

The fix is to manually re-enable tick labels on the Axes that should display them using [`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(".A;BC", sharey\=True, layout\="constrained")
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.values():
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[1, 2, 3, 4\], \[1, 4, 2, 3\])

\# Re-enable y-axis tick labels on Axes "A"
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["A"\].tick\_params(labelleft\=True)

identify\_axes([axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

![mosaic](https://matplotlib.org/stable/_images/sphx_glr_mosaic_021_2_00x.png)

**Total running time of the script:** (0 minutes 20.183 seconds)

[`Download Jupyter notebook: mosaic.ipynb`](https://matplotlib.org/stable/_downloads/c845cd1b7e5d796333d92f240787aaae/mosaic.ipynb)

[`Download Python source code: mosaic.py`](https://matplotlib.org/stable/_downloads/af8c3c8cd4b98795b4f4562826726e37/mosaic.py)

[`Download zipped: mosaic.zip`](https://matplotlib.org/stable/_downloads/f512dde983169fb7bc52414b27a73f66/mosaic.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page