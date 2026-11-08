[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#main-content)

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
    

matplotlib.pyplot.colorbar[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib-pyplot-colorbar "Link to this heading")

===========================================================================================================================================================

matplotlib.pyplot.colorbar(_mappable\=None_, _cax\=None_, _ax\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2668-L2683)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "Link to this definition")

Add a colorbar to a plot.

Parameters:

**mappable**

The [`matplotlib.colorizer.ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 (i.e., [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
, etc.) described by this colorbar. This argument is mandatory for the [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 method but optional for the [`pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 function, which sets the default to the current image.

Note that one can create a [`colorizer.ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 "on-the-fly" to generate colorbars not attached to a previously drawn artist, e.g.

cr \= colorizer.Colorizer(norm\=norm, cmap\=cmap)
fig.colorbar(colorizer.ColorizingArtist(cr), ax\=ax)

**cax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

Axes into which the colorbar will be drawn. If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, then a new Axes is created and the space for it will be stolen from the Axes(s) specified in _ax_.

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or iterable or [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of Axes, optional

The one or more parent Axes from which space for a new colorbar Axes will be stolen. This parameter is only used if _cax_ is not set.

Defaults to the Axes that contains the mappable used to create the colorbar.

**use\_gridspec**bool, optional

If _cax_ is `None`, a new _cax_ is created as an instance of Axes. If _ax_ is positioned with a subplotspec and _use\_gridspec_ is `True`, then _cax_ is also positioned with a subplotspec.

Returns:

**colorbar**[`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")

Other Parameters:

**location**None or {'left', 'right', 'top', 'bottom'}

The location, relative to the parent Axes, where the colorbar Axes is created. It also determines the _orientation_ of the colorbar (colorbars on the left and right are vertical, colorbars at the top and bottom are horizontal). If None, the location will come from the _orientation_ if it is set (vertical colorbars on the right, horizontal ones at the bottom), or default to 'right' if _orientation_ is unset.

**orientation**None or {'vertical', 'horizontal'}

The orientation of the colorbar. It is preferable to set the _location_ of the colorbar, as that also determines the _orientation_; passing incompatible values for _location_ and _orientation_ raises an exception.

**fraction**float, default: 0.15

Fraction of original Axes to use for colorbar.

**shrink**float, default: 1.0

Fraction by which to multiply the size of the colorbar.

**aspect**float, default: 20

Ratio of long to short dimensions.

**pad**float, default: 0.05 if vertical, 0.15 if horizontal

Fraction of original Axes between colorbar and new image Axes.

**anchor**(float, float), optional

The anchor point of the colorbar Axes. Defaults to (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal.

**panchor**(float, float), or _False_, optional

The anchor point of the colorbar parent Axes. If _False_, the parent axes' anchor will be unchanged. Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.

**extend**{'neither', 'both', 'min', 'max'}

Make pointed end(s) for out-of-range values (unless 'neither'). These are set for a given colormap using the colormap set\_under and set\_over methods.

**extendfrac**{_None_, 'auto', length, lengths}

If set to _None_, both the minimum and maximum triangular colorbar extensions will have a length of 5% of the interior colorbar length (this is the default setting).

If set to 'auto', makes the triangular colorbar extensions the same lengths as the interior boxes (when _spacing_ is set to 'uniform') or the same lengths as the respective adjacent interior boxes (when _spacing_ is set to 'proportional').

If a scalar, indicates the length of both the minimum and maximum triangular colorbar extensions as a fraction of the interior colorbar length. A two-element sequence of fractions may also be given, indicating the lengths of the minimum and maximum colorbar extensions respectively as a fraction of the interior colorbar length.

**extendrect**bool

If _False_ the minimum and maximum colorbar extensions will be triangular (the default). If _True_ the extensions will be rectangular.

**ticks**None or list of ticks or Locator

If None, ticks are determined automatically from the input.

**format**None or str or Formatter

If None, [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 is used. Format strings, e.g., `"%4.2e"` or `"{x:.2e}"`, are supported. An alternative [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 may be given instead.

**drawedges**bool

Whether to draw lines at color boundaries.

**label**str

The label on the colorbar's long axis.

**boundaries, values**None or a sequence

If unset, the colormap will be displayed on a 0-1 scale. If sequences, _values_ must have a length 1 less than _boundaries_. For each region delimited by adjacent entries in _boundaries_, the color mapped to the corresponding value in _values_ will be used. The size of each region is determined by the _spacing_ parameter. Normally only useful for indexed colors (i.e. `norm=NoNorm()`) or other unusual circumstances.

**spacing**{'uniform', 'proportional'}

For discrete colorbars ([`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 or contours), 'uniform' gives each color the same space; 'proportional' makes the space proportional to the data interval.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
.

If _mappable_ is a [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
, its _extend_ kwarg is included automatically.

The _shrink_ kwarg provides a simple way to scale the colorbar with respect to the Axes. Note that if _cax_ is specified, it determines the size of the colorbar, and _shrink_ and _aspect_ are ignored.

For more precise control, you can manually specify the positions of the axes objects in which the mappable and the colorbar are drawn. In this case, do not use any of the Axes properties kwargs.

It is known that some vector graphics viewers (svg and pdf) render white gaps between segments of the colorbar. This is due to bugs in the viewers, not Matplotlib. As a workaround, the colorbar can be rendered with overlapping segments:

cbar \= colorbar()
cbar.solids.set\_edgecolor("face")
draw()

However, this has negative consequences in other circumstances, e.g. with semi-transparent images (alpha < 1) and colorbar extensions; therefore, this workaround is not used by default (see issue #1188).

Examples using `matplotlib.pyplot.colorbar`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#examples-using-matplotlib-pyplot-colorbar "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_multi_image_thumb.png)

[Multiple images with one colorbar](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html)

Multiple images with one colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour_demo_thumb.png)

[Tricontour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/tricontour_demo.html)

Tricontour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_demo_thumb.png)

[Contour Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html)

Contour Demo

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)

[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)

Contourf demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_log_thumb.png)

[Contourf and log color scale](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_log.html)

Contourf and log color scale

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_hatching_thumb.png)

[Contourf hatching](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_hatching.html)

Contourf hatching

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_subplots_adjust_thumb.png)

[Subplots spacings and margins](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_adjust.html)

Subplots spacings and margins

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_tick_labelling_demo_thumb.png)

[Colorbar Tick labelling](https://matplotlib.org/stable/gallery/ticks/colorbar_tick_labelling_demo.html)

Colorbar Tick labelling

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_collection_thumb.png)

[Ellipse Collection](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html)

Ellipse Collection

![](https://matplotlib.org/stable/_images/sphx_glr_line_collection_thumb.png)

[Plot multiple lines using a LineCollection](https://matplotlib.org/stable/gallery/shapes_and_collections/line_collection.html)

Plot multiple lines using a LineCollection

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_basics_thumb.png)

[Colorbar](https://matplotlib.org/stable/gallery/color/colorbar_basics.html)

Colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_divider_thumb.png)

[Axes divider](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_divider.html)

Axes divider

![](https://matplotlib.org/stable/_images/sphx_glr_images_thumb.png)

[Image tutorial](https://matplotlib.org/stable/tutorials/images.html)

Image tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page