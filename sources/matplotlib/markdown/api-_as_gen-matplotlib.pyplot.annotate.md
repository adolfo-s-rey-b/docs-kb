[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#main-content)

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
    

matplotlib.pyplot.annotate[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib-pyplot-annotate "Link to this heading")

===========================================================================================================================================================

matplotlib.pyplot.annotate(_text_, _xy_, _xytext\=None_, _xycoords\='data'_, _textcoords\=None_, _arrowprops\=None_, _annotation\_clip\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3035-L3055)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "Link to this definition")

Annotate the point _xy_ with text _text_.

In the simplest form, the text is placed at _xy_.

Optionally, the text can be displayed in another position _xytext_. An arrow pointing from the text to the annotated point _xy_ can then be added by defining _arrowprops_.

Parameters:

**text**str

The text of the annotation.

**xy**(float, float)

The point _(x, y)_ to annotate. The coordinate system is determined by _xycoords_.

**xytext**(float, float), default: _xy_

The position _(x, y)_ to place the text at. The coordinate system is determined by _textcoords_.

**xycoords**single or two-tuple of str or [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 or callable, default: 'data'

The coordinate system that _xy_ is given in. The following types of values are supported:

*   One of the following strings:
    
    | Value | Description |
    | --- | --- |
    | 'figure points' | Points from the lower left of the figure |
    | 'figure pixels' | Pixels from the lower left of the figure |
    | 'figure fraction' | Fraction of figure from lower left |
    | 'subfigure points' | Points from the lower left of the subfigure |
    | 'subfigure pixels' | Pixels from the lower left of the subfigure |
    | 'subfigure fraction' | Fraction of subfigure from lower left |
    | 'axes points' | Points from lower left corner of the Axes |
    | 'axes pixels' | Pixels from lower left corner of the Axes |
    | 'axes fraction' | Fraction of Axes from lower left |
    | 'data' | Use the coordinate system of the object being annotated (default) |
    | 'polar' | _(theta, r)_ if not native 'data' coordinates |
    
    Note that 'subfigure pixels' and 'figure pixels' are the same for the parent figure, so users who want code that is usable in a subfigure can use 'subfigure pixels'.
    
*   An [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
    : _xy_ is interpreted as a fraction of the artist's [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    . E.g. _(0, 0)_ would be the lower left corner of the bounding box and _(0.5, 1)_ would be the center top of the bounding box.
    
*   A [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
     to transform _xy_ to screen coordinates.
    
*   A function with one of the following signatures:
    
    def transform(renderer) \-> Bbox
    def transform(renderer) \-> Transform
    
    where _renderer_ is a [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
     subclass.
    
    The result of the function is interpreted like the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
     and [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
     cases above.
    
*   A tuple _(xcoords, ycoords)_ specifying separate coordinate systems for _x_ and _y_. _xcoords_ and _ycoords_ must each be of one of the above described types.
    

See [Advanced annotation](https://matplotlib.org/stable/users/explain/text/annotations.html#plotting-guide-annotation)
 for more details.

**textcoords**single or two-tuple of str or [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 or callable, default: value of _xycoords_

The coordinate system that _xytext_ is given in.

All _xycoords_ values are valid as well as the following strings:

| Value | Description |
| --- | --- |
| 'offset points' | Offset, in points, from the _xy_ value |
| 'offset pixels' | Offset, in pixels, from the _xy_ value |
| 'offset fontsize' | Offset, relative to fontsize, from the _xy_ value |

**arrowprops**dict, optional

The properties used to draw a [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
 arrow between the positions _xy_ and _xytext_. Defaults to None, i.e. no arrow is drawn.

For historical reasons there are two different ways to specify arrows, "simple" and "fancy":

**Simple arrow:**

If _arrowprops_ does not contain the key 'arrowstyle' the allowed keys are:

| Key | Description |
| --- | --- |
| width | The width of the arrow in points |
| headwidth | The width of the base of the arrow head in points |
| headlength | The length of the arrow head in points |
| shrink | Fraction of total length to shrink from both ends |
| ?   | Any [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")<br> property |

The arrow is attached to the edge of the text box, the exact position (corners or centers) depending on where it's pointing to.

**Fancy arrow:**

This is used if 'arrowstyle' is provided in the _arrowprops_.

Valid keys are the following [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")
 parameters:

| Key | Description |
| --- | --- |
| arrowstyle | The arrow style |
| connectionstyle | The connection style |
| relpos | See below; default is (0.5, 0.5) |
| patchA | Default is bounding box of the text |
| patchB | Default is None |
| shrinkA | In points. Default is 2 points |
| shrinkB | In points. Default is 2 points |
| mutation\_scale | Default is text size (in points) |
| mutation\_aspect | Default is 1 |
| ?   | Any [`FancyArrowPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyArrowPatch.html#matplotlib.patches.FancyArrowPatch "matplotlib.patches.FancyArrowPatch")<br> property |

The exact starting point position of the arrow is defined by _relpos_. It's a tuple of relative coordinates of the text box, where (0, 0) is the lower left corner and (1, 1) is the upper right corner. Values <0 and >1 are supported and specify points outside the text box. By default (0.5, 0.5), so the starting point is centered in the text box.

**annotation\_clip**bool or None, default: None

Whether to clip (i.e. not draw) the annotation when the annotation point _xy_ is outside the Axes area.

*   If _True_, the annotation will be clipped when _xy_ is outside the Axes.
    
*   If _False_, the annotation will always be drawn.
    
*   If _None_, the annotation will be clipped when _xy_ is outside the Axes and _xycoords_ is 'data'.
    

**\*\*kwargs**

Additional kwargs are passed to [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
.

Returns:

[`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")

See also

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html#annotations)

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
.

Examples using `matplotlib.pyplot.annotate`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#examples-using-matplotlib-pyplot-annotate "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_basic_thumb.png)

[Annotating a plot](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_basic.html)

Annotating a plot

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_polar_thumb.png)

[Annotate polar plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_polar.html)

Annotate polar plots

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

On this page