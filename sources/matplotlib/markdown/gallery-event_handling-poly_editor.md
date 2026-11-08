[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html#sphx-glr-download-gallery-event-handling-poly-editor-py)
 to download the full example code.

Polygon editor[#](https://matplotlib.org/stable/gallery/event_handling/poly_editor.html#polygon-editor "Link to this heading")

===============================================================================================================================

This is an example to show how to build cross-GUI applications using Matplotlib event handling to interact with objects on the canvas.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

![Click and drag a point to move it](https://matplotlib.org/stable/_images/sphx_glr_poly_editor_001_2_00x.png)

import numpy as np

from matplotlib.artist import Artist
from matplotlib.lines import [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

def dist\_point\_to\_segment(p, s0, s1):
    """
    Get the distance from the point \*p\* to the segment (\*s0\*, \*s1\*), where
    \*p\*, \*s0\*, \*s1\* are \`\`\[x, y\]\`\` arrays.
    """
    s01 \= s1 \- s0
    s0p \= p \- s0
    if (s01 \== 0).all():
        return [np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\*s0p)
    \# Project onto segment, without going past segment ends.
    p1 \= s0 + [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
((s0p @ s01) / (s01 @ s01), 0, 1) \* s01
    return [np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\*(p \- p1))

class PolygonInteractor:
    """
    A polygon editor.

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """

    showverts \= True
    epsilon \= 5  \# max pixel distance to count as a vertex hit

    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
):
        if [poly.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.figure.html#matplotlib.artist.Artist.figure "matplotlib.artist.Artist.figure")
 is None:
            raise RuntimeError('You must first add the polygon to a figure '
                               'or canvas before defining the interactor')
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
        canvas \= [poly.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.figure.html#matplotlib.artist.Artist.figure "matplotlib.artist.Artist.figure")
        self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 \= [poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")

        x, y \= zip(\*self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy)
        self.line \= [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
(x, y,
                           marker\='o', markerfacecolor\='r',
                           animated\=True)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.add\_line(self.line)

        self.cid \= self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.add\_callback(self.poly\_changed)
        self.\_ind \= None  \# the active vert

        canvas.mpl\_connect('draw\_event', self.on\_draw)
        canvas.mpl\_connect('button\_press\_event', self.on\_button\_press)
        canvas.mpl\_connect('key\_press\_event', self.on\_key\_press)
        canvas.mpl\_connect('button\_release\_event', self.on\_button\_release)
        canvas.mpl\_connect('motion\_notify\_event', self.on\_mouse\_move)
        self.canvas \= canvas

    def on\_draw(self, event):
        self.background \= self.canvas.copy\_from\_bbox(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.line)
        \# do not need to blit here, this will fire before the screen is
        \# updated

    def poly\_changed(self, [poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
):
        """This method is called whenever the pathpatch object is called."""
        \# only copy the artist props to the line (except visibility)
        vis \= self.line.get\_visible()
        [Artist.update\_from](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update_from.html#matplotlib.artist.Artist.update_from "matplotlib.artist.Artist.update_from")
(self.line, [poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)
        self.line.set\_visible(vis)  \# don't use the poly visibility state

    def get\_ind\_under\_point(self, event):
        """
        Return the index of the point closest to the event position or \*None\*
        if no point is within \`\`self.epsilon\`\` to the event position.
        """
        \# display coords
        xy \= [np.asarray](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")
(self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy)
        xyt \= self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.get\_transform().transform(xy)
        xt, yt \= xyt\[:, 0\], xyt\[:, 1\]
        d \= [np.hypot](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(xt \- event.x, yt \- event.y)
        indseq, \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
(d \== d.min())
        ind \= indseq\[0\]

        if d\[ind\] \>= self.epsilon:
            ind \= None

        return ind

    def on\_button\_press(self, event):
        """Callback for mouse button presses."""
        if not self.showverts:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        self.\_ind \= self.get\_ind\_under\_point(event)

    def on\_button\_release(self, event):
        """Callback for mouse button releases."""
        if not self.showverts:
            return
        if event.button != 1:
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
        elif event.key \== 'd':
            ind \= self.get\_ind\_under\_point(event)
            if ind is not None:
                self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy \= [np.delete](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")
(self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy,
                                         ind, axis\=0)
                self.line.set\_data(zip(\*self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy))
        elif event.key \== 'i':
            xys \= self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.get\_transform().transform(self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy)
            p \= event.x, event.y  \# display coords
            for i in range(len(xys) \- 1):
                s0 \= xys\[i\]
                s1 \= xys\[i + 1\]
                d \= dist\_point\_to\_segment(p, s0, s1)
                if d <= self.epsilon:
                    self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy \= [np.insert](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert "numpy.insert")
(
                        self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy, i+1,
                        \[event.xdata, event.ydata\],
                        axis\=0)
                    self.line.set\_data(zip(\*self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy))
                    break
        if self.line.stale:
            self.canvas.draw\_idle()

    def on\_mouse\_move(self, event):
        """Callback for mouse movements."""
        if not self.showverts:
            return
        if self.\_ind is None:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return
        x, y \= event.xdata, event.ydata

        self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy\[self.\_ind\] \= x, y
        if self.\_ind \== 0:
            self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy\[\-1\] \= x, y
        elif self.\_ind \== len(self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy) \- 1:
            self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy\[0\] \= x, y
        self.line.set\_data(zip(\*self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
.xy))

        self.canvas.restore\_region(self.background)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.[poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.line)
        self.canvas.blit(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)

if \_\_name\_\_ \== '\_\_main\_\_':
    import matplotlib.pyplot as plt

    from matplotlib.patches import [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")

    [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.1)
    [r](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1.5

    [xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    [poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 \= [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
([np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[[xs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [ys](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]), animated\=True)

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)
    p \= PolygonInteractor([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [poly](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)

    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Click and drag a point to move it')
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-2, 2)
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-2, 2)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: poly_editor.ipynb`](https://matplotlib.org/stable/_downloads/9c786f31bd2914ddbf409193d50a6767/poly_editor.ipynb)

[`Download Python source code: poly_editor.py`](https://matplotlib.org/stable/_downloads/c45649bbf5126722bd95da5362a4fddc/poly_editor.py)

[`Download zipped: poly_editor.zip`](https://matplotlib.org/stable/_downloads/8c18e2dc2a69af23a64628354309d1c6/poly_editor.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)