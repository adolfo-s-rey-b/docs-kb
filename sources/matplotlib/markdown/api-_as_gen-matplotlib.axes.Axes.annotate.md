[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#main-content)

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
    

matplotlib.axes.Axes.annotate[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib-axes-axes-annotate "Link to this heading")

====================================================================================================================================================================

Axes.annotate(_text_, _xy_, _xytext\=None_, _xycoords\='data'_, _textcoords\=None_, _arrowprops\=None_, _annotation\_clip\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L731-L743)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "Link to this definition")

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

Examples using `matplotlib.axes.Axes.annotate`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#examples-using-matplotlib-axes-axes-annotate "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_timeline_thumb.png)

[Timeline with lines, dates, and text](https://matplotlib.org/stable/gallery/lines_bars_and_markers/timeline.html)

Timeline with lines, dates, and text

![](https://matplotlib.org/stable/_images/sphx_glr_pie_and_donut_labels_thumb.png)

[A pie and a donut with labels](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html)

A pie and a donut with labels

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_and_subplots_thumb.png)

[Combine two subplots using subplots and GridSpec](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_and_subplots.html)

Combine two subplots using subplots and GridSpec

![](https://matplotlib.org/stable/_images/sphx_glr_text_commands_thumb.png)

[Text properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html)

Text properties

![](https://matplotlib.org/stable/_images/sphx_glr_rainbow_text_thumb.png)

[Concatenate text objects with different properties](https://matplotlib.org/stable/gallery/text_labels_and_annotations/rainbow_text.html)

Concatenate text objects with different properties

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_basic_thumb.png)

[Annotating a plot](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_basic.html)

Annotating a plot

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_polar_thumb.png)

[Annotate polar plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_polar.html)

Annotate polar plots

![](https://matplotlib.org/stable/_images/sphx_glr_fancyarrow_demo_thumb.png)

[Annotation arrow style reference](https://matplotlib.org/stable/gallery/text_labels_and_annotations/fancyarrow_demo.html)

Annotation arrow style reference

![](https://matplotlib.org/stable/_images/sphx_glr_label_subplots_thumb.png)

[Labelling subplots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html)

Labelling subplots

![](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_thumb.png)

[Scale invariant angle label](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html)

Scale invariant angle label

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_donut_thumb.png)

[Mmh Donuts!!!](https://matplotlib.org/stable/gallery/shapes_and_collections/donut.html)

Mmh Donuts!!!

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

![](https://matplotlib.org/stable/_images/sphx_glr_annotate_with_units_thumb.png)

[Annotation with units](https://matplotlib.org/stable/gallery/units/annotate_with_units.html)

Annotation with units

![](https://matplotlib.org/stable/_images/sphx_glr_patheffect_demo_thumb.png)

[Patheffect Demo](https://matplotlib.org/stable/gallery/misc/patheffect_demo.html)

Patheffect Demo

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

![](https://matplotlib.org/stable/_images/sphx_glr_ishikawa_diagram_thumb.png)

[Ishikawa Diagram](https://matplotlib.org/stable/gallery/specialty_plots/ishikawa_diagram.html)

Ishikawa Diagram

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_blitting_thumb.png)

[Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html)

Faster rendering by using blitting

![](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_thumb.png)

[Transformations Tutorial](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html)

Transformations Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

![](https://matplotlib.org/stable/_images/sphx_glr_text_intro_thumb.png)

[Text in Matplotlib](https://matplotlib.org/stable/users/explain/text/text_intro.html)

Text in Matplotlib

On this page