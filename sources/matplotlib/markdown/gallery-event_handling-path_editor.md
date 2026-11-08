[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/path_editor.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/path_editor.html#sphx-glr-download-gallery-event-handling-path-editor-py)
 to download the full example code.

Path editor[#](https://matplotlib.org/stable/gallery/event_handling/path_editor.html#path-editor "Link to this heading")

=========================================================================================================================

Sharing events across GUIs.

This example demonstrates a cross-GUI application using Matplotlib event handling to interact with and modify objects on the canvas.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

![drag vertices to update path](https://matplotlib.org/stable/_images/sphx_glr_path_editor_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backend\_bases import MouseButton
from matplotlib.patches import [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[pathdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    ([Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (1.58, \-2.57)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (0.35, \-1.1)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (\-1.75, 2.0)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (0.375, 2.0)),\
    ([Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (0.85, 1.15)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (2.2, 3.2)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (3, 0.05)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (2.0, \-0.5)),\
    ([Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (1.58, \-2.57)),\
\]

[codes](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [verts](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= zip(\*[pathdata](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([verts](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [codes](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
(
    [path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, facecolor\='green', edgecolor\='yellow', alpha\=0.5)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)

class PathInteractor:
    """
    A path editor.

    Press 't' to toggle vertex markers on and off.  When vertex markers are on,
    they can be dragged with the mouse.
    """

    showverts \= True
    epsilon \= 5  \# max pixel distance to count as a vertex hit

    def \_\_init\_\_(self, pathpatch):

        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= pathpatch.axes
        canvas \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.figure.canvas
        self.pathpatch \= pathpatch
        self.pathpatch.set\_animated(True)

        x, y \= zip(\*self.pathpatch.get\_path().vertices)

        self.line, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(
            x, y, marker\='o', markerfacecolor\='r', animated\=True)

        self.\_ind \= None  \# the active vertex

        canvas.mpl\_connect('draw\_event', self.on\_draw)
        canvas.mpl\_connect('button\_press\_event', self.on\_button\_press)
        canvas.mpl\_connect('key\_press\_event', self.on\_key\_press)
        canvas.mpl\_connect('button\_release\_event', self.on\_button\_release)
        canvas.mpl\_connect('motion\_notify\_event', self.on\_mouse\_move)
        self.canvas \= canvas

    def get\_ind\_under\_point(self, event):
        """
        Return the index of the point closest to the event position or \*None\*
        if no point is within \`\`self.epsilon\`\` to the event position.
        """
        xy \= self.pathpatch.get\_path().vertices
        xyt \= self.pathpatch.get\_transform().transform(xy)  \# to display coords
        xt, yt \= xyt\[:, 0\], xyt\[:, 1\]
        d \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((xt \- event.x)\*\*2 + (yt \- event.y)\*\*2)
        ind \= d.argmin()
        return ind if d\[ind\] < self.epsilon else None

    def on\_draw(self, event):
        """Callback for draws."""
        self.background \= self.canvas.copy\_from\_bbox(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.pathpatch)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.line)

    def on\_button\_press(self, event):
        """Callback for mouse button presses."""
        if (event.inaxes is None
                or event.button != [MouseButton.LEFT](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
                or not self.showverts):
            return
        self.\_ind \= self.get\_ind\_under\_point(event)

    def on\_button\_release(self, event):
        """Callback for mouse button releases."""
        if (event.button != [MouseButton.LEFT](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
                or not self.showverts):
            return
        self.\_ind \= None

    def on\_key\_press(self, event):
        """Callback for key presses."""
        if not event.inaxes:
            return
        if event.key \== 't':
            self.showverts \= not self.showverts
            self.line.set\_visible(self.showverts)
            if not self.showverts:
                self.\_ind \= None
        self.canvas.draw()

    def on\_mouse\_move(self, event):
        """Callback for mouse movements."""
        if (self.\_ind is None
                or event.inaxes is None
                or event.button != [MouseButton.LEFT](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
                or not self.showverts):
            return

        vertices \= self.pathpatch.get\_path().vertices

        vertices\[self.\_ind\] \= event.xdata, event.ydata
        self.line.set\_data(zip(\*vertices))

        self.canvas.restore\_region(self.background)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.pathpatch)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.line)
        self.canvas.blit(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)

interactor \= PathInteractor([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('drag vertices to update path')
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-3, 4)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-3, 4)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: path_editor.ipynb`](https://matplotlib.org/stable/_downloads/f5e7a628b5567339938d9d0e5c4f062f/path_editor.ipynb)

[`Download Python source code: path_editor.py`](https://matplotlib.org/stable/_downloads/2b072ea346f552f1d4e4cab8f3eeef72/path_editor.py)

[`Download zipped: path_editor.zip`](https://matplotlib.org/stable/_downloads/1b1aa200cda7f6befb7d4c5db15c9564/path_editor.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)