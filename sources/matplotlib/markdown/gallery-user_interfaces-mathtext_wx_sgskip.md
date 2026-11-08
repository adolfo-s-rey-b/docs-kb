[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/mathtext_wx_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/mathtext_wx_sgskip.html#sphx-glr-download-gallery-user-interfaces-mathtext-wx-sgskip-py)
 to download the full example code.

Display mathtext in WX[#](https://matplotlib.org/stable/gallery/user_interfaces/mathtext_wx_sgskip.html#display-mathtext-in-wx "Link to this heading")

=======================================================================================================================================================

Demonstrates how to convert (math)text to a wx.Bitmap for display in various controls on wxPython.

from io import [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")

import wx

import numpy as np

from matplotlib.backends.backend\_wx import NavigationToolbar2Wx
from matplotlib.backends.backend\_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

IS\_WIN \= 'wxMSW' in wx.PlatformInfo

def mathtext\_to\_wxbitmap(s):
    \# We draw the text at position (0, 0) but then rely on
    \# \`\`facecolor="none"\`\` and \`\`bbox\_inches="tight", pad\_inches=0\`\` to get a
    \# transparent mask that is then loaded into a wx.Bitmap.
    fig \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
(facecolor\="none")
    text\_color \= (
        [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
([wx.SystemSettings.GetColour](https://docs.wxpython.org/wx.SystemSettings.html#wx.SystemSettings.GetColour "wx.SystemSettings.GetColour")
(wx.SYS\_COLOUR\_WINDOWTEXT)) / 255)
    fig.text(0, 0, s, fontsize\=10, color\=text\_color)
    buf \= [BytesIO](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO")
()
    fig.savefig(buf, format\="png", dpi\=150, bbox\_inches\="tight", pad\_inches\=0)
    s \= buf.getvalue()
    return [wx.Bitmap.NewFromPNGData](https://docs.wxpython.org/wx.Bitmap.html#wx.Bitmap.NewFromPNGData "wx.Bitmap.NewFromPNGData")
(s, len(s))

functions \= \[\
    (r'$\\sin(2 \\pi x)$', lambda x: [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")\
(2\*[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
\*x)),\
    (r'$\\frac{4}{3}\\pi x^3$', lambda x: (4/3)\*[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
\*x\*\*3),\
    (r'$\\cos(2 \\pi x)$', lambda x: [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")\
(2\*[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
\*x)),\
    (r'$\\log(x)$', lambda x: [np.log](https://numpy.org/doc/stable/reference/generated/numpy.log.html#numpy.log "numpy.log")\
(x))\
\]

class CanvasFrame([wx.Frame](https://docs.wxpython.org/wx.Frame.html#wx.Frame "wx.Frame")
):
    def \_\_init\_\_(self, parent, title):
        super().\_\_init\_\_(parent, \-1, title, size\=(550, 350))

        self.figure \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
()
        self.axes \= self.figure.add\_subplot()

        self.canvas \= FigureCanvas(self, \-1, self.figure)

        self.change\_plot(0)

        self.sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.VERTICAL)
        self.add\_buttonbar()
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.add\_toolbar()  \# comment this out for no toolbar

        menuBar \= [wx.MenuBar](https://docs.wxpython.org/wx.MenuBar.html#wx.MenuBar "wx.MenuBar")
()

        \# File Menu
        menu \= [wx.Menu](https://docs.wxpython.org/wx.Menu.html#wx.Menu "wx.Menu")
()
        m\_exit \= menu.Append(
            wx.ID\_EXIT, "E&xit\\tAlt-X", "Exit this simple sample")
        menuBar.Append(menu, "&File")
        self.Bind(wx.EVT\_MENU, self.OnClose, m\_exit)

        if IS\_WIN:
            \# Equation Menu
            menu \= [wx.Menu](https://docs.wxpython.org/wx.Menu.html#wx.Menu "wx.Menu")
()
            for i, (mt, func) in enumerate(functions):
                bm \= mathtext\_to\_wxbitmap(mt)
                item \= [wx.MenuItem](https://docs.wxpython.org/wx.MenuItem.html#wx.MenuItem "wx.MenuItem")
(menu, 1000 + i, " ")
                item.SetBitmap(bm)
                menu.Append(item)
                self.Bind(wx.EVT\_MENU, self.OnChangePlot, item)
            menuBar.Append(menu, "&Functions")

        self.SetMenuBar(menuBar)

        self.SetSizer(self.sizer)
        self.Fit()

    def add\_buttonbar(self):
        self.button\_bar \= [wx.Panel](https://docs.wxpython.org/wx.Panel.html#wx.Panel "wx.Panel")
(self)
        self.button\_bar\_sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.HORIZONTAL)
        self.sizer.Add(self.button\_bar, 0, wx.LEFT | wx.TOP | wx.GROW)

        for i, (mt, func) in enumerate(functions):
            bm \= mathtext\_to\_wxbitmap(mt)
            button \= [wx.BitmapButton](https://docs.wxpython.org/wx.BitmapButton.html#wx.BitmapButton "wx.BitmapButton")
(self.button\_bar, 1000 + i, bm)
            self.button\_bar\_sizer.Add(button, 1, wx.GROW)
            self.Bind(wx.EVT\_BUTTON, self.OnChangePlot, button)

        self.button\_bar.SetSizer(self.button\_bar\_sizer)

    def add\_toolbar(self):
        """Copied verbatim from embedding\_wx2.py"""
        self.toolbar \= NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        \# By adding toolbar in sizer, we are able to put it at the bottom
        \# of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        \# update the axes menu on the toolbar
        self.toolbar.update()

    def OnChangePlot(self, event):
        self.change\_plot(event.GetId() \- 1000)

    def change\_plot(self, plot\_number):
        t \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1.0, 3.0, 0.01)
        s \= functions\[plot\_number\]\[1\](t)
        self.axes.clear()
        self.axes.plot(t, s)
        self.canvas.draw()

    def OnClose(self, event):
        self.Destroy()

class MyApp([wx.App](https://docs.wxpython.org/wx.App.html#wx.App "wx.App")
):
    def OnInit(self):
        frame \= CanvasFrame(None, "wxPython mathtext demo app")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if \_\_name\_\_ \== "\_\_main\_\_":
    app \= MyApp()
    app.MainLoop()

[`Download Jupyter notebook: mathtext_wx_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/dd6d6b83319e6c1d1306414dcb009091/mathtext_wx_sgskip.ipynb)

[`Download Python source code: mathtext_wx_sgskip.py`](https://matplotlib.org/stable/_downloads/79d41c98ca5c56ba3cd899653b27d324/mathtext_wx_sgskip.py)

[`Download zipped: mathtext_wx_sgskip.zip`](https://matplotlib.org/stable/_downloads/935528d82d53f470f00159c510130201/mathtext_wx_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)