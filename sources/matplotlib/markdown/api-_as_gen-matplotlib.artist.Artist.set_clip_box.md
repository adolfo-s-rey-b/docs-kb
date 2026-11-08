[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#main-content)

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
    

matplotlib.artist.Artist.set\_clip\_box[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib-artist-artist-set-clip-box "Link to this heading")

==============================================================================================================================================================================================

Artist.set\_clip\_box(_clipbox_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L808-L824)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "Link to this definition")

Set the artist's clip [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
.

Parameters:

**clipbox**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
 or None

Will typically be created from a [`TransformedBbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
. For instance, `TransformedBbox(Bbox([[0, 0], [1, 1]]), ax.transAxes)` is the default clipping for an artist added to an Axes.

Examples using `matplotlib.artist.Artist.set_clip_box`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#examples-using-matplotlib-artist-artist-set-clip-box "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_annotation_demo_thumb.png)

[Annotate plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html)

Annotate plots

![](https://matplotlib.org/stable/_images/sphx_glr_ellipse_demo_thumb.png)

[Ellipse Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_demo.html)

Ellipse Demo

On this page