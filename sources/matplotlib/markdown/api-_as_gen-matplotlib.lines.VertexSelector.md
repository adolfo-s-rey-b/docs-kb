[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#main-content)

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
    

matplotlib.lines.VertexSelector[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib-lines-vertexselector "Link to this heading")

==========================================================================================================================================================================

class matplotlib.lines.VertexSelector(_line_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1676-L1746)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Manage the callbacks to maintain a list of selected vertices for [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
. Derived classes should override the [`process_selected`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector.process_selected "matplotlib.lines.VertexSelector.process_selected")
 method to do something with the picks.

Here is an example which highlights the selected verts with red circles:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

class HighlightSelected(lines.VertexSelector):
    def \_\_init\_\_(self, line, fmt\='ro', \*\*kwargs):
        super().\_\_init\_\_(line)
        self.markers, \= self.axes.plot(\[\], \[\], fmt, \*\*kwargs)

    def process\_selected(self, ind, xs, ys):
        self.markers.set\_data(xs, ys)
        self.canvas.draw()

fig, ax \= plt.subplots()
x, y \= np.random.rand(2, 30)
line, \= ax.plot(x, y, 'bs-', picker\=5)

selector \= HighlightSelected(line)
plt.show()

Parameters:

**line**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The line must already have been added to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 and must have its picker property set.

property canvas[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector.canvas "Link to this definition")

onpick(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1739-L1746)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector.onpick "Link to this definition")

When the line is picked, update the set of selected indices.

process\_selected(_ind_, _xs_, _ys_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/lines.py#L1726-L1737)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector.process_selected "Link to this definition")

Default "do nothing" implementation of the [`process_selected`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.VertexSelector.html#matplotlib.lines.VertexSelector.process_selected "matplotlib.lines.VertexSelector.process_selected")
 method.

Parameters:

**ind**list of int

The indices of the selected vertices.

**xs, ys**array-like

The coordinates of the selected vertices.

On this page