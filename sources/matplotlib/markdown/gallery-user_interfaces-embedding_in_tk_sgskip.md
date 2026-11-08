[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html#sphx-glr-download-gallery-user-interfaces-embedding-in-tk-sgskip-py)
 to download the full example code.

Embed in Tk[#](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html#embed-in-tk "Link to this heading")

=====================================================================================================================================

import tkinter

import numpy as np

\# Implement the default Matplotlib key bindings.
from matplotlib.backend\_bases import [key\_press\_handler](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.key_press_handler "matplotlib.backend_bases.key_press_handler")
from matplotlib.backends.backend\_tkagg import [FigureCanvasTkAgg](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvasTkAgg "matplotlib.backends.backend_tkagg.FigureCanvasTkAgg")
, NavigationToolbar2Tk
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

root \= [tkinter.Tk](https://docs.python.org/3/library/tkinter.html#tkinter.Tk "tkinter.Tk")
()
root.wm\_title("Embedded in Tk")

fig \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(figsize\=(5, 4), dpi\=100)
t \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 3, .01)
ax \= fig.add\_subplot()
line, \= ax.plot(t, 2 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* t))
ax.set\_xlabel("time \[s\]")
ax.set\_ylabel("f(t)")

canvas \= [FigureCanvasTkAgg](https://matplotlib.org/stable/api/backend_tk_api.html#matplotlib.backends.backend_tkagg.FigureCanvasTkAgg "matplotlib.backends.backend_tkagg.FigureCanvasTkAgg")
(fig, master\=root)  \# A tk.DrawingArea.
canvas.draw()

\# pack\_toolbar=False will make it easier to use a layout manager later on.
toolbar \= NavigationToolbar2Tk(canvas, root, pack\_toolbar\=False)
toolbar.update()

canvas.mpl\_connect(
    "key\_press\_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl\_connect("key\_press\_event", [key\_press\_handler](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.key_press_handler "matplotlib.backend_bases.key_press_handler")
)

button\_quit \= [tkinter.Button](https://docs.python.org/3/library/tkinter.html#tkinter.Button "tkinter.Button")
(master\=root, text\="Quit", command\=root.destroy)

def update\_frequency(new\_val):
    \# retrieve frequency
    f \= float(new\_val)

    \# update data
    y \= 2 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* f \* t)
    line.set\_data(t, y)

    \# required to update canvas and attached toolbar!
    canvas.draw()

slider\_update \= [tkinter.Scale](https://docs.python.org/3/library/tkinter.html#tkinter.Scale "tkinter.Scale")
(root, from\_\=1, to\=5, orient\=[tkinter.HORIZONTAL](https://docs.python.org/3/library/tkinter.html#tkinter.HORIZONTAL "tkinter.HORIZONTAL")
,
                              command\=update\_frequency, label\="Frequency \[Hz\]")

\# Packing order is important. Widgets are processed sequentially and if there
\# is no space left, because the window is too small, they are not displayed.
\# The canvas is rather flexible in its size, so we pack it last which makes
\# sure the UI controls are displayed as long as possible.
button\_quit.pack(side\=[tkinter.BOTTOM](https://docs.python.org/3/library/tkinter.html#tkinter.BOTTOM "tkinter.BOTTOM")
)
slider\_update.pack(side\=[tkinter.BOTTOM](https://docs.python.org/3/library/tkinter.html#tkinter.BOTTOM "tkinter.BOTTOM")
)
toolbar.pack(side\=[tkinter.BOTTOM](https://docs.python.org/3/library/tkinter.html#tkinter.BOTTOM "tkinter.BOTTOM")
, fill\=[tkinter.X](https://docs.python.org/3/library/tkinter.html#tkinter.X "tkinter.X")
)
canvas.get\_tk\_widget().pack(side\=[tkinter.TOP](https://docs.python.org/3/library/tkinter.html#tkinter.TOP "tkinter.TOP")
, fill\=[tkinter.BOTH](https://docs.python.org/3/library/tkinter.html#tkinter.BOTH "tkinter.BOTH")
, expand\=True)

[tkinter.mainloop](https://docs.python.org/3/library/tkinter.html#tkinter.mainloop "tkinter.mainloop")
()

[`Download Jupyter notebook: embedding_in_tk_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/8424e14cdf5ec93eeb16aa121cf7f524/embedding_in_tk_sgskip.ipynb)

[`Download Python source code: embedding_in_tk_sgskip.py`](https://matplotlib.org/stable/_downloads/c54f37aca0e6188e16d86056e4596788/embedding_in_tk_sgskip.py)

[`Download zipped: embedding_in_tk_sgskip.zip`](https://matplotlib.org/stable/_downloads/2d334d1a5e460eaaf84f15d44f5fc885/embedding_in_tk_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)