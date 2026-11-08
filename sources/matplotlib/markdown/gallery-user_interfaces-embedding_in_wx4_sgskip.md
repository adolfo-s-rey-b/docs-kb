[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx4_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx4_sgskip.html#sphx-glr-download-gallery-user-interfaces-embedding-in-wx4-sgskip-py)
 to download the full example code.

Embed in wx #4[#](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx4_sgskip.html#embed-in-wx-4 "Link to this heading")

===========================================================================================================================================

An example of how to use wxagg in a wx application with a custom toolbar.

import wx

import numpy as np

from matplotlib.backends.backend\_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend\_wxagg import \\
    NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

class MyNavigationToolbar(NavigationToolbar):
    """Extend the default wx toolbar with your own event handlers."""

    def \_\_init\_\_(self, canvas):
        super().\_\_init\_\_(canvas)
        \# We use a stock wx bitmap, but you could also use your own image file.
        bmp \= [wx.ArtProvider.GetBitmap](https://docs.wxpython.org/wx.ArtProvider.html#wx.ArtProvider.GetBitmap "wx.ArtProvider.GetBitmap")
(wx.ART\_CROSS\_MARK, wx.ART\_TOOLBAR)
        tool \= self.AddTool(wx.ID\_ANY, 'Click me', bmp,
                            'Activate custom control')
        self.Bind(wx.EVT\_TOOL, self.\_on\_custom, id\=tool.GetId())

    def \_on\_custom(self, event):
        \# add some text to the Axes in a random location in axes coords with a
        \# random color
        ax \= self.canvas.figure.axes\[0\]
        x, y \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2)  \# generate a random location
        rgb \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(3)  \# generate a random color
        ax.text(x, y, 'You clicked me', transform\=ax.transAxes, color\=rgb)
        self.canvas.draw()
        event.Skip()

class CanvasFrame([wx.Frame](https://docs.wxpython.org/wx.Frame.html#wx.Frame "wx.Frame")
):
    def \_\_init\_\_(self):
        super().\_\_init\_\_(None, \-1, 'CanvasFrame', size\=(550, 350))

        self.figure \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(figsize\=(5, 4), dpi\=100)
        self.axes \= self.figure.add\_subplot()
        t \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 3.0, 0.01)
        s \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* t)

        self.axes.plot(t, s)

        self.canvas \= FigureCanvas(self, \-1, self.figure)

        self.sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        self.toolbar \= MyNavigationToolbar(self.canvas)
        self.toolbar.Realize()
        \# By adding toolbar in sizer, we are able to put it at the bottom
        \# of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)

        \# update the axes menu on the toolbar
        self.toolbar.update()
        self.SetSizer(self.sizer)
        self.Fit()

class App([wx.App](https://docs.wxpython.org/wx.App.html#wx.App "wx.App")
):
    def OnInit(self):
        """Create the main window and insert the custom frame."""
        frame \= CanvasFrame()
        frame.Show(True)
        return True

if \_\_name\_\_ \== "\_\_main\_\_":
    app \= App()
    app.MainLoop()

[`Download Jupyter notebook: embedding_in_wx4_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/49c25b5a16ffdf716d9e7a25c2bac2f3/embedding_in_wx4_sgskip.ipynb)

[`Download Python source code: embedding_in_wx4_sgskip.py`](https://matplotlib.org/stable/_downloads/380985f6602f4e14b013028d8c1ad7b2/embedding_in_wx4_sgskip.py)

[`Download zipped: embedding_in_wx4_sgskip.zip`](https://matplotlib.org/stable/_downloads/4e52e3cf9f6c936de2a53daa54d3d38c/embedding_in_wx4_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)