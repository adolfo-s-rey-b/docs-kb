[Skip to main content](https://matplotlib.org/stable/api/_tight_bbox_api.html#main-content)

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
    

`matplotlib._tight_bbox`[#](https://matplotlib.org/stable/api/_tight_bbox_api.html#module-matplotlib._tight_bbox "Link to this heading")

=========================================================================================================================================

Helper module for the _bbox\_inches_ parameter in [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
.

matplotlib.\_tight\_bbox.adjust\_bbox(_fig_, _bbox\_inches_, _renderer_, _fixed\_dpi\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_tight_bbox.py#L8-L70)
[#](https://matplotlib.org/stable/api/_tight_bbox_api.html#matplotlib._tight_bbox.adjust_bbox "Link to this definition")

Temporarily adjust the figure so that only the specified area (bbox\_inches) is saved.

It modifies fig.bbox, fig.bbox\_inches, fig.transFigure.\_boxout, and fig.patch. While the figure size changes, the scale of the original figure is conserved. A function which restores the original values are returned.

matplotlib.\_tight\_bbox.process\_figure\_for\_rasterizing(_fig_, _bbox\_inches\_restore_, _renderer_, _fixed\_dpi\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_tight_bbox.py#L73-L84)
[#](https://matplotlib.org/stable/api/_tight_bbox_api.html#matplotlib._tight_bbox.process_figure_for_rasterizing "Link to this definition")

A function that needs to be called when figure dpi changes during the drawing (e.g., rasterizing). It recovers the bbox and re-adjust it with the new dpi.

On this page