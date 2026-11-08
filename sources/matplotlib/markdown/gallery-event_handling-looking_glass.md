[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html#sphx-glr-download-gallery-event-handling-looking-glass-py)
 to download the full example code.

Looking glass[#](https://matplotlib.org/stable/gallery/event_handling/looking_glass.html#looking-glass "Link to this heading")

===============================================================================================================================

Example using mouse events to simulate a looking glass for inspecting data.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

![Left click and drag to move looking glass](https://matplotlib.org/stable/_images/sphx_glr_looking_glass_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.patches as patches

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, 200)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [patches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((0.5, 0.5), 0.25, alpha\=0.8, fc\='yellow')
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)

[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=0.2)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, alpha\=1.0, clip\_path\=[circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Left click and drag to move looking glass")

class EventHandler:
    def \_\_init\_\_(self):
        [fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('button\_press\_event', self.on\_press)
        [fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('button\_release\_event', self.on\_release)
        [fig.canvas.mpl\_connect](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect "matplotlib.backend_bases.FigureCanvasBase.mpl_connect")
('motion\_notify\_event', self.on\_move)
        self.x0, self.y0 \= [circ.center](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.center "matplotlib.patches.Ellipse.center")
        self.pressevent \= None

    def on\_press(self, event):
        if event.inaxes != [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
:
            return

        if not [circ.contains](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.contains "matplotlib.patches.Patch.contains")
(event)\[0\]:
            return

        self.pressevent \= event

    def on\_release(self, event):
        self.pressevent \= None
        self.x0, self.y0 \= [circ.center](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.center "matplotlib.patches.Ellipse.center")

    def on\_move(self, event):
        if self.pressevent is None or event.inaxes != self.pressevent.inaxes:
            return

        dx \= event.xdata \- self.pressevent.xdata
        dy \= event.ydata \- self.pressevent.ydata
        [circ.center](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.center "matplotlib.patches.Ellipse.center")
 \= self.x0 + dx, self.y0 + dy
        [line.set\_clip\_path](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
([circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
        [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()

handler \= EventHandler()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: looking_glass.ipynb`](https://matplotlib.org/stable/_downloads/eceaf4545b944fe5ab14312e9d93c864/looking_glass.ipynb)

[`Download Python source code: looking_glass.py`](https://matplotlib.org/stable/_downloads/3f1ecbb039cffe24c51d1499214bb495/looking_glass.py)

[`Download zipped: looking_glass.zip`](https://matplotlib.org/stable/_downloads/67a8d8fb8bcc5da7145398864b8419cb/looking_glass.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)