[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html#sphx-glr-download-gallery-subplots-axes-and-figures-auto-subplots-adjust-py)
 to download the full example code.

Programmatically control subplot adjustment[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html#programmatically-control-subplot-adjustment "Link to this heading")

=============================================================================================================================================================================================================

Note

This example is primarily intended to show some advanced concepts in Matplotlib.

If you are only looking for having enough space for your labels, it is almost always simpler and good enough to either set the subplot parameters manually using [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
, or use one of the automatic layout mechanisms ([Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
 or [Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
).

This example describes a user-defined way to read out Artist sizes and set the subplot parameters accordingly. Its main purpose is to illustrate some advanced concepts like reading out text positions, working with bounding boxes and transforms and using [events](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling)
. But it can also serve as a starting point if you want to automate the layouting and need more flexibility than tight layout and constrained layout.

Below, we collect the bounding boxes of all y-labels and move the left border of the subplot to the right so that it leaves enough room for the union of all the bounding boxes.

There's one catch with calculating text bounding boxes: Querying the text bounding boxes ([`Text.get_window_extent`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.get_window_extent "matplotlib.text.Text.get_window_extent")
) needs a renderer ([`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 instance), to calculate the text size. This renderer is only available after the figure has been drawn ([`Figure.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw.html#matplotlib.figure.Figure.draw "matplotlib.figure.Figure.draw")
).

A solution to this is putting the adjustment logic in a draw callback. This function is executed after the figure has been drawn. It can now check if the subplot leaves enough room for the text. If not, the subplot parameters are updated and second draw is triggered.

import matplotlib.pyplot as plt

import matplotlib.transforms as mtransforms

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(range(10))
[ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[2, 5, 7\], labels\=\['really, really, really', 'long', 'labels'\])

def on\_draw(event):
    bboxes \= \[\]
    for label in [ax.get\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html#matplotlib.axes.Axes.get_yticklabels "matplotlib.axes.Axes.get_yticklabels")
():
        \# Bounding box in pixels
        bbox\_px \= label.get\_window\_extent()
        \# Transform to relative figure coordinates. This is the inverse of
        \# transFigure.
        bbox\_fig \= bbox\_px.transformed([fig.transFigure.inverted](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2DBase.inverted "matplotlib.transforms.Affine2DBase.inverted")
())
        bboxes.append(bbox\_fig)
    \# the bbox that bounds all the bboxes, again in relative figure coords
    bbox \= mtransforms.Bbox.union(bboxes)
    if [fig.subplotpars.left](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 < bbox.width:
        \# Move the subplot left edge more to the right
        [fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(left\=1.1\*bbox.width)  \# pad a little
        [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()

[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('draw\_event', on\_draw)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![auto subplots adjust](https://matplotlib.org/stable/_images/sphx_glr_auto_subplots_adjust_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.artist.Artist.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_window_extent.html#matplotlib.artist.Artist.get_window_extent "matplotlib.artist.Artist.get_window_extent")
    
*   [`matplotlib.transforms.Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    
*   [`matplotlib.transforms.BboxBase.transformed`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.transformed "matplotlib.transforms.BboxBase.transformed")
    
*   [`matplotlib.transforms.BboxBase.union`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.union "matplotlib.transforms.BboxBase.union")
    
*   [`matplotlib.transforms.Transform.inverted`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
    
*   [`matplotlib.figure.Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
    
*   [`matplotlib.gridspec.SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
    
*   [`matplotlib.backend_bases.FigureCanvasBase.mpl_connect`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
    

Tags: [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [styling: position](https://matplotlib.org/stable/_tags/styling-position.html)
 [level: advanced](https://matplotlib.org/stable/_tags/level-advanced.html)

[`Download Jupyter notebook: auto_subplots_adjust.ipynb`](https://matplotlib.org/stable/_downloads/66808b7e152335729a1eadf1d1ff336c/auto_subplots_adjust.ipynb)

[`Download Python source code: auto_subplots_adjust.py`](https://matplotlib.org/stable/_downloads/a54f19823bde998a456571636498aa98/auto_subplots_adjust.py)

[`Download zipped: auto_subplots_adjust.zip`](https://matplotlib.org/stable/_downloads/8dbb07953cd3c2fba9242bd168fc55d4/auto_subplots_adjust.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)