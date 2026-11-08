[Skip to main content](https://matplotlib.org/stable/users/explain/animations/blitting.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/animations/blitting.html#sphx-glr-download-users-explain-animations-blitting-py)
 to download the full example code.

Faster rendering by using blitting[#](https://matplotlib.org/stable/users/explain/animations/blitting.html#faster-rendering-by-using-blitting "Link to this heading")

======================================================================================================================================================================

_Blitting_ is a [standard technique](https://en.wikipedia.org/wiki/Bit_blit)
 in raster graphics that, in the context of Matplotlib, can be used to (drastically) improve performance of interactive figures. For example, the [`animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")
 and [`widgets`](https://matplotlib.org/stable/api/widgets_api.html#module-matplotlib.widgets "matplotlib.widgets")
 modules use blitting internally. Here, we demonstrate how to implement your own blitting, outside of these classes.

Blitting speeds up repetitive drawing by rendering all non-changing graphic elements into a background image once. Then, for every draw, only the changing elements need to be drawn onto this background. For example, if the limits of an Axes have not changed, we can render the empty Axes including all ticks and labels once, and only draw the changing data later.

The strategy is

*   Prepare the constant background:
    
    *   Draw the figure, but exclude all artists that you want to animate by marking them as _animated_ (see [`Artist.set_animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated")
        ).
        
    *   Save a copy of the RBGA buffer.
        
*   Render the individual images:
    
    *   Restore the copy of the RGBA buffer.
        
    *   Redraw the animated artists using [`Axes.draw_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw_artist.html#matplotlib.axes.Axes.draw_artist "matplotlib.axes.Axes.draw_artist")
         / [`Figure.draw_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_artist.html#matplotlib.figure.Figure.draw_artist "matplotlib.figure.Figure.draw_artist")
        .
        
    *   Show the resulting image on the screen.
        

One consequence of this procedure is that your animated artists are always drawn on top of the static artists.

Not all backends support blitting. You can check if a given canvas does via the [`FigureCanvasBase.supports_blit`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.supports_blit "matplotlib.backend_bases.FigureCanvasBase.supports_blit")
 property.

Minimal example[#](https://matplotlib.org/stable/users/explain/animations/blitting.html#minimal-example "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

We can use the [`FigureCanvasAgg`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg "matplotlib.backends.backend_agg.FigureCanvasAgg")
 methods [`copy_from_bbox`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.copy_from_bbox "matplotlib.backends.backend_agg.FigureCanvasAgg.copy_from_bbox")
 and [`restore_region`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.FigureCanvasAgg.restore_region "matplotlib.backends.backend_agg.FigureCanvasAgg.restore_region")
 in conjunction with setting `animated=True` on our artist to implement a minimal example that uses blitting to accelerate rendering

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 100)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# animated=True tells matplotlib to only draw the artist when we
\# explicitly request it
([ln](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,) \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), animated\=True)

\# make sure the window is raised, but the script keeps going
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
(block\=False)

\# stop to admire our empty window axes and ensure it is rendered at
\# least once.
#
\# We need to fully draw the figure at its final size on the screen
\# before we continue on so that :
\#  a) we have the correctly sized and drawn background to grab
\#  b) we have a cached renderer so that \`\`ax.draw\_artist\`\` works
\# so we spin the event loop to let the backend process any pending operations
[plt.pause](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
(0.1)

\# get copy of entire figure (everything inside fig.bbox) sans animated artist
bg \= [fig.canvas.copy\_from\_bbox](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
([fig.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
)
\# draw the animated artist, this uses a cached renderer
[ax.draw\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw_artist.html#matplotlib.axes.Axes.draw_artist "matplotlib.axes.Axes.draw_artist")
([ln](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)
\# show the result to the screen, this pushes the updated RGBA buffer from the
\# renderer to the GUI framework so you can see it
[fig.canvas.blit](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.blit "matplotlib.backend_bases.FigureCanvasBase.blit")
([fig.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
)

for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(100):
    \# reset the background back in the canvas state, screen unchanged
    [fig.canvas.restore\_region](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
(bg)
    \# update the artist, neither the canvas state nor the screen have changed
    [ln.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + ([j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / 100) \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
    \# re-render the artist, updating the canvas state, but not the screen
    [ax.draw\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw_artist.html#matplotlib.axes.Axes.draw_artist "matplotlib.axes.Axes.draw_artist")
([ln](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)
    \# copy the image to the GUI state, but screen might not be changed yet
    [fig.canvas.blit](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.blit "matplotlib.backend_bases.FigureCanvasBase.blit")
([fig.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
)
    \# flush any pending GUI events, re-painting the screen if needed
    [fig.canvas.flush\_events](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.flush_events "matplotlib.backend_bases.FigureCanvasBase.flush_events")
()
    \# you can put a pause in if you want to slow things down
    \# plt.pause(.1)

![blitting](https://matplotlib.org/stable/_images/sphx_glr_blitting_001_2_00x.png)

This example works and shows a simple animation, however because we are only grabbing the background once, if the size of the figure in pixels changes (due to either the size or dpi of the figure changing) , the background will be invalid and result in incorrect (but sometimes cool looking!) images. There is also a global variable and a fair amount of boilerplate which suggests we should wrap this in a class.

Class-based example[#](https://matplotlib.org/stable/users/explain/animations/blitting.html#class-based-example "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

We can use a class to encapsulate the boilerplate logic and state of restoring the background, drawing the artists, and then blitting the result to the screen. Additionally, we can use the `'draw_event'` callback to capture a new background whenever a full re-draw happens to handle resizes correctly.

class BlitManager:
    def \_\_init\_\_(self, canvas, animated\_artists\=()):
        """
        Parameters
        ----------
        canvas : FigureCanvasAgg
            The canvas to work with, this only works for subclasses of the Agg
            canvas which have the \`~FigureCanvasAgg.copy\_from\_bbox\` and
            \`~FigureCanvasAgg.restore\_region\` methods.

        animated\_artists : Iterable\[Artist\]
            List of the artists to manage
        """
        self.canvas \= canvas
        self.\_bg \= None
        self.\_artists \= \[\]

        for a in animated\_artists:
            self.add\_artist(a)
        \# grab the background on every draw
        self.cid \= canvas.mpl\_connect("draw\_event", self.on\_draw)

    def on\_draw(self, event):
        """Callback to register with 'draw\_event'."""
        cv \= self.canvas
        if event is not None:
            if event.canvas != cv:
                raise RuntimeError
        self.\_bg \= cv.copy\_from\_bbox(cv.figure.bbox)
        self.\_draw\_animated()

    def add\_artist(self, art):
        """
        Add an artist to be managed.

        Parameters
        ----------
        art : Artist

            The artist to be added.  Will be set to 'animated' (just
            to be safe).  \*art\* must be in the figure associated with
            the canvas this class is managing.

        """
        if art.figure != self.canvas.figure:
            raise RuntimeError
        art.set\_animated(True)
        self.\_artists.append(art)

    def \_draw\_animated(self):
        """Draw all of the animated artists."""
        [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= self.canvas.figure
        for a in self.\_artists:
            [fig.draw\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_artist.html#matplotlib.figure.Figure.draw_artist "matplotlib.figure.Figure.draw_artist")
(a)

    def update(self):
        """Update the screen with animated artists."""
        cv \= self.canvas
        [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= cv.figure
        \# paranoia in case we missed the draw event,
        if self.\_bg is None:
            self.on\_draw(None)
        else:
            \# restore the background
            cv.restore\_region(self.\_bg)
            \# draw all of the animated artists
            self.\_draw\_animated()
            \# update the GUI state
            cv.blit([fig.bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
)
        \# let the GUI event loop process anything it has to do
        cv.flush\_events()

Here is how we would use our class. This is a slightly more complicated example than the first case as we add a text frame counter as well.

\# make a new figure
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
\# add a line
([ln](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
,) \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), animated\=True)
\# add a frame number
[fr\_number](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
    "0",
    (0, 1),
    xycoords\="axes fraction",
    xytext\=(10, \-10),
    textcoords\="offset points",
    ha\="left",
    va\="top",
    animated\=True,
)
bm \= BlitManager([fig.canvas](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase "matplotlib.backend_bases.FigureCanvasBase")
, \[[ln](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
, [fr\_number](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")\
\])
\# make sure our window is on the screen and drawn
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
(block\=False)
[plt.pause](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause")
(.1)

for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(100):
    \# update the artists
    [ln.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + ([j](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / 100) \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
))
    [fr\_number.set\_text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text")
(f"frame: {[j](https://docs.python.org/3/library/functions.html#int "builtins.int")
}")
    \# tell the blitting manager to do its thing
    bm.update()

![blitting](https://matplotlib.org/stable/_images/sphx_glr_blitting_002_2_00x.png)

This class does not depend on [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 and is suitable to embed into larger GUI application.

**Total running time of the script:** (0 minutes 2.427 seconds)

[`Download Jupyter notebook: blitting.ipynb`](https://matplotlib.org/stable/_downloads/4474e5053d9334b09fc7fcf56bb27cd0/blitting.ipynb)

[`Download Python source code: blitting.py`](https://matplotlib.org/stable/_downloads/45aa008579ef6857fc6688e29efa25be/blitting.py)

[`Download zipped: blitting.zip`](https://matplotlib.org/stable/_downloads/a1385b4dae9d7363a88dbd0c341e1610/blitting.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page