[Skip to main content](https://matplotlib.org/stable/api/lines_api.html#main-content)

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
    

`matplotlib.lines`[#](https://matplotlib.org/stable/api/lines_api.html#module-matplotlib.lines "Link to this heading")

=======================================================================================================================

2D lines with support for a variety of line styles, markers, colors, etc.

Classes[#](https://matplotlib.org/stable/api/lines_api.html#classes "Link to this heading")

--------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>(xdata, ydata, \*\[, linewidth, ...\]) | A line - the line can have both a solid linestyle connecting all the vertices, and a marker at each vertex. |
| [`VertexSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector "matplotlib.lines.VertexSelector")<br>(line) | Manage the callbacks to maintain a list of selected vertices for [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`AxLine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.AxLine.html#matplotlib.lines.AxLine "matplotlib.lines.AxLine")<br>(xy1, xy2, slope, \*\*kwargs) | A helper class that implements [`axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")<br>, by recomputing the artist transform at draw time. |

Functions[#](https://matplotlib.org/stable/api/lines_api.html#functions "Link to this heading")

------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`segment_hits`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.segment_hits.html#matplotlib.lines.segment_hits "matplotlib.lines.segment_hits")<br>(cx, cy, x, y, radius) | Return the indices of the segments in the polyline with coordinates (_cx_, _cy_) that are within a distance _radius_ of the point (_x_, _y_). |

On this page