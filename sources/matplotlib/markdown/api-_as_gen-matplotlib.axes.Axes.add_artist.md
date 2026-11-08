[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#main-content)

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
    

matplotlib.axes.Axes.add\_artist[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib-axes-axes-add-artist "Link to this heading")

===========================================================================================================================================================================

Axes.add\_artist(_a_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L2354-L2374)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "Link to this definition")

Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 to the Axes; return the artist.

Use [`add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
 only for artists for which there is no dedicated "add" method; and if necessary, use a method such as [`update_datalim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html#matplotlib.axes.Axes.update_datalim "matplotlib.axes.Axes.update_datalim")
 to manually update the [`dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
 if the artist is to be included in autoscaling.

If no `transform` has been specified when creating the artist (e.g. `artist.get_transform() == None`) then the transform is set to `ax.transData`.

Examples using `matplotlib.axes.Axes.add_artist`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#examples-using-matplotlib-axes-axes-add-artist "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_with_legend_thumb.png)

[Scatter plot with a legend](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html)

Scatter plot with a legend

![](https://matplotlib.org/stable/_images/sphx_glr_demo_bboximage_thumb.png)

[BboxImage Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/demo_bboximage.html)

BboxImage Demo

![](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_thumb.png)

[Bar of pie](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html)

Bar of pie

![](https://matplotlib.org/stable/_images/sphx_glr_demo_text_path_thumb.png)

[Using a text as a Path](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_path.html)

Using a text as a Path

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_demo_annotation_box_thumb.png)

[Artists as annotations](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_annotation_box.html)

Artists as annotations

![](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_thumb.png)

[Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)

Reference for Matplotlib artists

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_thumb.png)

[Ellipse Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html)

Ellipse Demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_anchored_direction_arrows_thumb.png)

[Anchored Direction Arrow](https://matplotlib.org/stable/gallery/axes_grid1/demo_anchored_direction_arrows.html)

Anchored Direction Arrow

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_grid2_thumb.png)

[Axes Grid2](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_grid2.html)

Axes Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_inset_locator_demo2_thumb.png)

[Inset locator demo 2](https://matplotlib.org/stable/gallery/axes_grid1/inset_locator_demo2.html)

Inset locator demo 2

![](https://matplotlib.org/stable/_images/sphx_glr_simple_anchored_artists_thumb.png)

[Simple Anchored Artists](https://matplotlib.org/stable/gallery/axes_grid1/simple_anchored_artists.html)

Simple Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_artist_tests_thumb.png)

[Artist tests](https://matplotlib.org/stable/gallery/units/artist_tests.html)

Artist tests

![](https://matplotlib.org/stable/_images/sphx_glr_anchored_artists_thumb.png)

[Anchored Artists](https://matplotlib.org/stable/gallery/misc/anchored_artists.html)

Anchored Artists

![](https://matplotlib.org/stable/_images/sphx_glr_anatomy_thumb.png)

[Anatomy of a figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

Anatomy of a figure

![](https://matplotlib.org/stable/_images/sphx_glr_legend_guide_thumb.png)

[Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)

Legend guide

![](https://matplotlib.org/stable/_images/sphx_glr_annotations_thumb.png)

[Annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

Annotations

On this page