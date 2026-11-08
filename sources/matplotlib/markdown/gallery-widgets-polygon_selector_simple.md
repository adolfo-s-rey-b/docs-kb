[Skip to main content](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html#sphx-glr-download-gallery-widgets-polygon-selector-simple-py)
 to download the full example code.

Polygon Selector[#](https://matplotlib.org/stable/gallery/widgets/polygon_selector_simple.html#polygon-selector "Link to this heading")

========================================================================================================================================

Shows how to create a polygon programmatically or interactively

import matplotlib.pyplot as plt

from matplotlib.widgets import [PolygonSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")

To create the polygon programmatically

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
()

[selector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
 \= [PolygonSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, lambda \*args: None)

\# Add three vertices
[selector.verts](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector.verts "matplotlib.widgets.PolygonSelector.verts")
 \= \[(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)\]

![polygon selector simple](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_001_2_00x.png)

To create the polygon interactively

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig2.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show")
()

[selector2](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
 \= [PolygonSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, lambda \*args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

![polygon selector simple](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_simple_002_2_00x.png)

Click on the figure to create a polygon.
Press the 'esc' key to start a new polygon.
Try holding the 'shift' key to move all of the vertices.
Try holding the 'ctrl' key to move a single vertex.

Tags: [component: axes](https://matplotlib.org/stable/_tags/component-axes.html)
 [styling: position](https://matplotlib.org/stable/_tags/styling-position.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)
 [domain: cartography](https://matplotlib.org/stable/_tags/domain-cartography.html)
 [domain: geometry](https://matplotlib.org/stable/_tags/domain-geometry.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
    

[`Download Jupyter notebook: polygon_selector_simple.ipynb`](https://matplotlib.org/stable/_downloads/b73d7c2c6fb019ca38593385ad8e9d02/polygon_selector_simple.ipynb)

[`Download Python source code: polygon_selector_simple.py`](https://matplotlib.org/stable/_downloads/82a3b4570f59acc5a372cb7be136c952/polygon_selector_simple.py)

[`Download zipped: polygon_selector_simple.zip`](https://matplotlib.org/stable/_downloads/563c98a8d4e5d6c739f25f1752fe106c/polygon_selector_simple.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)