[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx3_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx3_sgskip.html#sphx-glr-download-gallery-user-interfaces-embedding-in-wx3-sgskip-py)
 to download the full example code.

Embed in wx #3[#](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx3_sgskip.html#embed-in-wx-3 "Link to this heading")

===========================================================================================================================================

Copyright (C) 2003-2004 Andrew Straw, Jeremy O'Donoghue and others

License: This work is licensed under the PSF. A copy should be included with this source code, and is also available at [https://docs.python.org/3/license.html](https://docs.python.org/3/license.html)

This is yet another example of using matplotlib with wx. Hopefully this is pretty full-featured:

*   both matplotlib toolbar and WX buttons manipulate plot
    
*   full wxApp framework, including widget interaction
    
*   XRC (XML wxWidgets resource) file to create GUI (made with XRCed)
    

This was derived from embedding\_in\_wx and dynamic\_image\_wxagg.

Thanks to matplotlib and wx teams for creating such great software!

import wx
import wx.xrc as xrc

import numpy as np

from matplotlib.backends.backend\_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend\_wxagg import \\
    NavigationToolbar2WxAgg as NavigationToolbar
import matplotlib.cbook as cbook
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

ERR\_TOL \= 1e-5  \# floating point slop for peak-detection

class PlotPanel([wx.Panel](https://docs.wxpython.org/wx.Panel.html#wx.Panel "wx.Panel")
):
    def \_\_init\_\_(self, parent):
        super().\_\_init\_\_(parent, \-1)

        self.fig \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
((5, 4), 75)
        self.canvas \= FigureCanvas(self, \-1, self.fig)
        self.toolbar \= NavigationToolbar(self.canvas)  \# matplotlib toolbar
        self.toolbar.Realize()

        \# Now put all into a sizer
        sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.VERTICAL)
        \# This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        \# Best to allow the toolbar to resize!
        sizer.Add(self.toolbar, 0, wx.GROW)
        self.SetSizer(sizer)
        self.Fit()

    def init\_plot\_data(self):
        ax \= self.fig.add\_subplot()

        x \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(120.0) \* 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 60.0
        y \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(100.0) \* 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 50.0
        self.x, self.y \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(x, y)
        z \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(self.x) + [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(self.y)
        self.im \= ax.imshow(z, cmap\="RdBu", origin\='lower')

        zmax \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(z) \- ERR\_TOL
        ymax\_i, xmax\_i \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
(z \>= zmax)
        if self.im.origin \== 'upper':
            ymax\_i \= z.shape\[0\] \- ymax\_i
        self.lines \= ax.plot(xmax\_i, ymax\_i, 'ko')

        self.toolbar.update()  \# Not sure why this is needed - ADS

    def GetToolBar(self):
        \# You will need to override GetToolBar if you are using an
        \# unmanaged toolbar in your frame
        return self.toolbar

    def OnWhiz(self, event):
        self.x += [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 15
        self.y += [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 / 20
        z \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(self.x) + [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(self.y)
        self.im.set\_array(z)

        zmax \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(z) \- ERR\_TOL
        ymax\_i, xmax\_i \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
(z \>= zmax)
        if self.im.origin \== 'upper':
            ymax\_i \= z.shape\[0\] \- ymax\_i
        self.lines\[0\].set\_data(xmax\_i, ymax\_i)

        self.canvas.draw()

class MyApp([wx.App](https://docs.wxpython.org/wx.App.html#wx.App "wx.App")
):
    def OnInit(self):
        xrcfile \= [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('embedding\_in\_wx3.xrc',
                                        asfileobj\=False)
        print('loading', xrcfile)

        self.res \= [xrc.XmlResource](https://docs.wxpython.org/wx.xrc.XmlResource.html#wx.xrc.XmlResource "wx.xrc.XmlResource")
(xrcfile)

        \# main frame and panel ---------

        self.frame \= self.res.LoadFrame(None, "MainFrame")
        self.panel \= [xrc.XRCCTRL](https://docs.wxpython.org/wx.xrc.functions.html#wx.xrc.XRCCTRL "wx.xrc.XRCCTRL")
(self.frame, "MainPanel")

        \# matplotlib panel -------------

        \# container for matplotlib panel (I like to make a container
        \# panel for our panel so I know where it'll go when in XRCed.)
        plot\_container \= [xrc.XRCCTRL](https://docs.wxpython.org/wx.xrc.functions.html#wx.xrc.XRCCTRL "wx.xrc.XRCCTRL")
(self.frame, "plot\_container\_panel")
        sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.VERTICAL)

        \# matplotlib panel itself
        self.plotpanel \= PlotPanel(plot\_container)
        self.plotpanel.init\_plot\_data()

        \# wx boilerplate
        sizer.Add(self.plotpanel, 1, wx.EXPAND)
        plot\_container.SetSizer(sizer)

        \# whiz button ------------------
        whiz\_button \= [xrc.XRCCTRL](https://docs.wxpython.org/wx.xrc.functions.html#wx.xrc.XRCCTRL "wx.xrc.XRCCTRL")
(self.frame, "whiz\_button")
        whiz\_button.Bind(wx.EVT\_BUTTON, self.plotpanel.OnWhiz)

        \# bang button ------------------
        bang\_button \= [xrc.XRCCTRL](https://docs.wxpython.org/wx.xrc.functions.html#wx.xrc.XRCCTRL "wx.xrc.XRCCTRL")
(self.frame, "bang\_button")
        bang\_button.Bind(wx.EVT\_BUTTON, self.OnBang)

        \# final setup ------------------
        self.frame.Show()

        self.SetTopWindow(self.frame)

        return True

    def OnBang(self, event):
        bang\_count \= [xrc.XRCCTRL](https://docs.wxpython.org/wx.xrc.functions.html#wx.xrc.XRCCTRL "wx.xrc.XRCCTRL")
(self.frame, "bang\_count")
        bangs \= bang\_count.GetValue()
        bangs \= int(bangs) + 1
        bang\_count.SetValue(str(bangs))

if \_\_name\_\_ \== '\_\_main\_\_':
    app \= MyApp()
    app.MainLoop()

[`Download Jupyter notebook: embedding_in_wx3_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/7672645272cb1863dfa347ba46b7be4e/embedding_in_wx3_sgskip.ipynb)

[`Download Python source code: embedding_in_wx3_sgskip.py`](https://matplotlib.org/stable/_downloads/07e64378616d93d4fa17eaf626e5d9e8/embedding_in_wx3_sgskip.py)

[`Download zipped: embedding_in_wx3_sgskip.zip`](https://matplotlib.org/stable/_downloads/c75cd9ff3fe6ee0de921bcb0d9161caf/embedding_in_wx3_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)