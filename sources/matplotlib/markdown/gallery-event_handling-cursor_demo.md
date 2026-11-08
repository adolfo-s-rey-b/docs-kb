[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html#sphx-glr-download-gallery-event-handling-cursor-demo-py)
 to download the full example code.

Cross-hair cursor[#](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html#cross-hair-cursor "Link to this heading")

=====================================================================================================================================

This example adds a cross-hair as a data cursor. The cross-hair is implemented as regular line objects that are updated on mouse move.

We show three implementations:

1.  A simple cursor implementation that redraws the figure on every mouse move. This is a bit slow, and you may notice some lag of the cross-hair movement.
    
2.  A cursor that uses blitting for speedup of the rendering.
    
3.  A cursor that snaps to data points.
    

Faster cursoring is possible using native GUI drawing, as in [Add a cursor in WX](https://matplotlib.org/stable/gallery/user_interfaces/wxcursor_demo_sgskip.html)
.

The [mpldatacursor](https://github.com/joferkington/mpldatacursor)
 and [mplcursors](https://github.com/anntzer/mplcursors)
 third-party packages can be used to achieve a similar effect.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backend\_bases import [MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")

class Cursor:
    """
    A cross hair cursor.
    """
    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
        self.horizontal\_line \= [ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(color\='k', lw\=0.8, ls\='--')
        self.vertical\_line \= [ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(color\='k', lw\=0.8, ls\='--')
        \# text location in axes coordinates
        self.text \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.72, 0.9, '', transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

    def set\_cross\_hair\_visible(self, visible):
        need\_redraw \= self.horizontal\_line.get\_visible() != visible
        self.horizontal\_line.set\_visible(visible)
        self.vertical\_line.set\_visible(visible)
        self.text.set\_visible(visible)
        return need\_redraw

    def on\_mouse\_move(self, event):
        if not event.inaxes:
            need\_redraw \= self.set\_cross\_hair\_visible(False)
            if need\_redraw:
                self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.draw()
        else:
            self.set\_cross\_hair\_visible(True)
            [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= event.xdata, event.ydata
            \# update the line positions
            self.horizontal\_line.set\_ydata(\[[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
            self.vertical\_line.set\_xdata(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
            self.text.set\_text(f'x={[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:1.2f}, y={[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:1.2f}')
            self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.draw()

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 0.01)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Simple cursor')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o')
cursor \= Cursor([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('motion\_notify\_event', cursor.on\_mouse\_move)

\# Simulate a mouse move to (0.5, 0.5), needed for online docs
[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
[MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
(
    "motion\_notify\_event", [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
, \*[t.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((0.5, 0.5))
).\_process()

![Simple cursor](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_001_2_00x.png)

Faster redrawing using blitting[#](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html#faster-redrawing-using-blitting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

This technique stores the rendered plot as a background image. Only the changed artists (cross-hair lines and text) are rendered anew. They are combined with the background using blitting.

This technique is significantly faster. It requires a bit more setup because the background has to be stored without the cross-hair lines (see `create_new_background()`). Additionally, a new background has to be created whenever the figure changes. This is achieved by connecting to the `'draw_event'`.

class BlittedCursor:
    """
    A cross-hair cursor using blitting for faster redraw.
    """
    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
        self.background \= None
        self.horizontal\_line \= [ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(color\='k', lw\=0.8, ls\='--')
        self.vertical\_line \= [ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(color\='k', lw\=0.8, ls\='--')
        \# text location in axes coordinates
        self.text \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.72, 0.9, '', transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)
        self.\_creating\_background \= False
        [ax.figure.canvas.mpl\_connect](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
('draw\_event', self.on\_draw)

    def on\_draw(self, event):
        self.create\_new\_background()

    def set\_cross\_hair\_visible(self, visible):
        need\_redraw \= self.horizontal\_line.get\_visible() != visible
        self.horizontal\_line.set\_visible(visible)
        self.vertical\_line.set\_visible(visible)
        self.text.set\_visible(visible)
        return need\_redraw

    def create\_new\_background(self):
        if self.\_creating\_background:
            \# discard calls triggered from within this function
            return
        self.\_creating\_background \= True
        self.set\_cross\_hair\_visible(False)
        self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.draw()
        self.background \= self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.copy\_from\_bbox(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)
        self.set\_cross\_hair\_visible(True)
        self.\_creating\_background \= False

    def on\_mouse\_move(self, event):
        if self.background is None:
            self.create\_new\_background()
        if not event.inaxes:
            need\_redraw \= self.set\_cross\_hair\_visible(False)
            if need\_redraw:
                self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.restore\_region(self.background)
                self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.blit(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)
        else:
            self.set\_cross\_hair\_visible(True)
            \# update the line positions
            [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= event.xdata, event.ydata
            self.horizontal\_line.set\_ydata(\[[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
            self.vertical\_line.set\_xdata(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
            self.text.set\_text(f'x={[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:1.2f}, y={[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:1.2f}')

            self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.restore\_region(self.background)
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.horizontal\_line)
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.vertical\_line)
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.draw\_artist(self.text)
            self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.blit(self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.bbox)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 0.01)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Blitted cursor')
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o')
blitted\_cursor \= BlittedCursor([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('motion\_notify\_event', blitted\_cursor.on\_mouse\_move)

\# Simulate a mouse move to (0.5, 0.5), needed for online docs
[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
[MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
(
    "motion\_notify\_event", [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
, \*[t.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((0.5, 0.5))
).\_process()

![Blitted cursor](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_002_2_00x.png)

Snapping to data points[#](https://matplotlib.org/stable/gallery/event_handling/cursor_demo.html#snapping-to-data-points "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

The following cursor snaps its position to the data points of a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 object.

To save unnecessary redraws, the index of the last indicated data point is saved in `self._last_index`. A redraw is only triggered when the mouse moves far enough so that another data point must be selected. This reduces the lag due to many redraws. Of course, blitting could still be added on top for additional speedup.

class SnappingCursor:
    """
    A cross-hair cursor that snaps to the data point of a line, which is
    closest to the \*x\* position of the cursor.

    For simplicity, this assumes that \*x\* values of the data are sorted.
    """
    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
):
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
        self.horizontal\_line \= [ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(color\='k', lw\=0.8, ls\='--')
        self.vertical\_line \= [ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(color\='k', lw\=0.8, ls\='--')
        self.[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, self.[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [line.get\_data](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.get_data "matplotlib.lines.Line2D.get_data")
()
        self.\_last\_index \= None
        \# text location in axes coords
        self.text \= [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.72, 0.9, '', transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

    def set\_cross\_hair\_visible(self, visible):
        need\_redraw \= self.horizontal\_line.get\_visible() != visible
        self.horizontal\_line.set\_visible(visible)
        self.vertical\_line.set\_visible(visible)
        self.text.set\_visible(visible)
        return need\_redraw

    def on\_mouse\_move(self, event):
        if not event.inaxes:
            self.\_last\_index \= None
            need\_redraw \= self.set\_cross\_hair\_visible(False)
            if need\_redraw:
                self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.draw()
        else:
            self.set\_cross\_hair\_visible(True)
            [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= event.xdata, event.ydata
            index \= min([np.searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
(self.[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), len(self.[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \- 1)
            if index \== self.\_last\_index:
                return  \# still on the same data point. Nothing to do.
            self.\_last\_index \= index
            [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= self.[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[index\]
            [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= self.[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[index\]
            \# update the line positions
            self.horizontal\_line.set\_ydata(\[[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
            self.vertical\_line.set\_xdata(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])
            self.text.set\_text(f'x={[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:1.2f}, y={[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:1.2f}')
            self.[ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
.draw()

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 1, 0.01)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Snapping cursor')
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o')
snap\_cursor \= SnappingCursor([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)
[fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('motion\_notify\_event', snap\_cursor.on\_mouse\_move)

\# Simulate a mouse move to (0.5, 0.5), needed for online docs
[t](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
[MouseEvent](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseEvent "matplotlib.backend_bases.MouseEvent")
(
    "motion\_notify\_event", [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
, \*[t.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((0.5, 0.5))
).\_process()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Snapping cursor](https://matplotlib.org/stable/_images/sphx_glr_cursor_demo_003_2_00x.png)

**Total running time of the script:** (0 minutes 1.992 seconds)

[`Download Jupyter notebook: cursor_demo.ipynb`](https://matplotlib.org/stable/_downloads/ee41a49a2bbf8c6e50f1fc7031a35680/cursor_demo.ipynb)

[`Download Python source code: cursor_demo.py`](https://matplotlib.org/stable/_downloads/b50d37f9b82e9455a7917dd5929c697f/cursor_demo.py)

[`Download zipped: cursor_demo.zip`](https://matplotlib.org/stable/_downloads/a101be84574b27468c652e147c013d83/cursor_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page