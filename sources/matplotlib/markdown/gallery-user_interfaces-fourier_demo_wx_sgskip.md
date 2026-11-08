[Skip to main content](https://matplotlib.org/stable/gallery/user_interfaces/fourier_demo_wx_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/user_interfaces/fourier_demo_wx_sgskip.html#sphx-glr-download-gallery-user-interfaces-fourier-demo-wx-sgskip-py)
 to download the full example code.

Fourier Demo WX[#](https://matplotlib.org/stable/gallery/user_interfaces/fourier_demo_wx_sgskip.html#fourier-demo-wx "Link to this heading")

=============================================================================================================================================

import wx

import numpy as np

from matplotlib.backends.backend\_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

class Knob:
    """
    Knob - simple class with a "setKnob" method.
    A Knob instance is attached to a Param instance, e.g., param.attach(knob)
    Base class is for documentation purposes.
    """

    def setKnob(self, value):
        pass

class Param:
    """
    The idea of the "Param" class is that some parameter in the GUI may have
    several knobs that both control it and reflect the parameter's state, e.g.
    a slider, text, and dragging can all change the value of the frequency in
    the waveform of this example.
    The class allows a cleaner way to update/"feedback" to the other knobs when
    one is being changed.  Also, this class handles min/max constraints for all
    the knobs.
    Idea - knob list - in "set" method, knob object is passed as well
      - the other knobs in the knob list have a "set" method which gets
        called for the others.
    """

    def \_\_init\_\_(self, initialValue\=None, minimum\=0., maximum\=1.):
        self.minimum \= minimum
        self.maximum \= maximum
        if initialValue != self.constrain(initialValue):
            raise ValueError('illegal initial value')
        self.value \= initialValue
        self.knobs \= \[\]

    def attach(self, knob):
        self.knobs += \[knob\]

    def set(self, value, knob\=None):
        self.value \= value
        self.value \= self.constrain(value)
        for feedbackKnob in self.knobs:
            if feedbackKnob != knob:
                feedbackKnob.setKnob(self.value)
        return self.value

    def constrain(self, value):
        if value <= self.minimum:
            value \= self.minimum
        if value \>= self.maximum:
            value \= self.maximum
        return value

class SliderGroup(Knob):
    def \_\_init\_\_(self, parent, label, param):
        self.sliderLabel \= [wx.StaticText](https://docs.wxpython.org/wx.StaticText.html#wx.StaticText "wx.StaticText")
(parent, label\=label)
        self.sliderText \= [wx.TextCtrl](https://docs.wxpython.org/wx.TextCtrl.html#wx.TextCtrl "wx.TextCtrl")
(parent, \-1, style\=wx.TE\_PROCESS\_ENTER)
        self.slider \= [wx.Slider](https://docs.wxpython.org/wx.Slider.html#wx.Slider "wx.Slider")
(parent, \-1)
        \# self.slider.SetMax(param.maximum\*1000)
        self.slider.SetRange(0, int(param.maximum \* 1000))
        self.setKnob(param.value)

        sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.HORIZONTAL)
        sizer.Add(self.sliderLabel, 0,
                  wx.EXPAND | wx.ALL,
                  border\=2)
        sizer.Add(self.sliderText, 0,
                  wx.EXPAND | wx.ALL,
                  border\=2)
        sizer.Add(self.slider, 1, wx.EXPAND)
        self.sizer \= sizer

        self.slider.Bind(wx.EVT\_SLIDER, self.sliderHandler)
        self.sliderText.Bind(wx.EVT\_TEXT\_ENTER, self.sliderTextHandler)

        self.param \= param
        self.param.attach(self)

    def sliderHandler(self, event):
        value \= event.GetInt() / 1000.
        self.param.set(value)

    def sliderTextHandler(self, event):
        value \= float(self.sliderText.GetValue())
        self.param.set(value)

    def setKnob(self, value):
        self.sliderText.SetValue(f'{value:g}')
        self.slider.SetValue(int(value \* 1000))

class FourierDemoFrame([wx.Frame](https://docs.wxpython.org/wx.Frame.html#wx.Frame "wx.Frame")
):
    def \_\_init\_\_(self, \*args, \*\*kwargs):
        super().\_\_init\_\_(\*args, \*\*kwargs)
        panel \= [wx.Panel](https://docs.wxpython.org/wx.Panel.html#wx.Panel "wx.Panel")
(self)

        \# create the GUI elements
        self.createCanvas(panel)
        self.createSliders(panel)

        \# place them in a sizer for the Layout
        sizer \= [wx.BoxSizer](https://docs.wxpython.org/wx.BoxSizer.html#wx.BoxSizer "wx.BoxSizer")
(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.frequencySliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, border\=5)
        sizer.Add(self.amplitudeSliderGroup.sizer, 0,
                  wx.EXPAND | wx.ALL, border\=5)
        panel.SetSizer(sizer)

    def createCanvas(self, parent):
        self.lines \= \[\]
        self.figure \= [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
()
        self.canvas \= FigureCanvas(parent, \-1, self.figure)
        self.canvas.callbacks.connect('button\_press\_event', self.mouseDown)
        self.canvas.callbacks.connect('motion\_notify\_event', self.mouseMotion)
        self.canvas.callbacks.connect('button\_release\_event', self.mouseUp)
        self.state \= ''
        self.mouseInfo \= (None, None, None, None)
        self.f0 \= Param(2., minimum\=0., maximum\=6.)
        self.A \= Param(1., minimum\=0.01, maximum\=2.)
        self.createPlots()

        \# Not sure I like having two params attached to the same Knob,
        \# but that is what we have here... it works but feels kludgy -
        \# although maybe it's not too bad since the knob changes both params
        \# at the same time (both f0 and A are affected during a drag)
        self.f0.attach(self)
        self.A.attach(self)

    def createSliders(self, panel):
        self.frequencySliderGroup \= SliderGroup(
            panel,
            label\='Frequency f0:',
            param\=self.f0)
        self.amplitudeSliderGroup \= SliderGroup(panel, label\=' Amplitude a:',
                                                param\=self.A)

    def mouseDown(self, event):
        if self.lines\[0\].contains(event)\[0\]:
            self.state \= 'frequency'
        elif self.lines\[1\].contains(event)\[0\]:
            self.state \= 'time'
        else:
            self.state \= ''
        self.mouseInfo \= (event.xdata, event.ydata,
                          max(self.f0.value, .1),
                          self.A.value)

    def mouseMotion(self, event):
        if self.state \== '':
            return
        x, y \= event.xdata, event.ydata
        if x is None:  \# outside the Axes
            return
        x0, y0, f0Init, AInit \= self.mouseInfo
        self.A.set(AInit + (AInit \* (y \- y0) / y0), self)
        if self.state \== 'frequency':
            self.f0.set(f0Init + (f0Init \* (x \- x0) / x0))
        elif self.state \== 'time':
            if (x \- x0) / x0 != \-1.:
                self.f0.set(1. / (1. / f0Init + (1. / f0Init \* (x \- x0) / x0)))

    def mouseUp(self, event):
        self.state \= ''

    def createPlots(self):
        \# This method creates the subplots, waveforms and labels.
        \# Later, when the waveforms or sliders are dragged, only the
        \# waveform data will be updated (not here, but below in setKnob).
        self.subplot1, self.subplot2 \= self.figure.subplots(2)
        x1, y1, x2, y2 \= self.compute(self.f0.value, self.A.value)
        color \= (1., 0., 0.)
        self.lines += self.subplot1.plot(x1, y1, color\=color, linewidth\=2)
        self.lines += self.subplot2.plot(x2, y2, color\=color, linewidth\=2)
        \# Set some plot attributes
        self.subplot1.set\_title(
            "Click and drag waveforms to change frequency and amplitude",
            fontsize\=12)
        self.subplot1.set\_ylabel("Frequency Domain Waveform X(f)", fontsize\=8)
        self.subplot1.set\_xlabel("frequency f", fontsize\=8)
        self.subplot2.set\_ylabel("Time Domain Waveform x(t)", fontsize\=8)
        self.subplot2.set\_xlabel("time t", fontsize\=8)
        self.subplot1.set\_xlim(\-6, 6)
        self.subplot1.set\_ylim(0, 1)
        self.subplot2.set\_xlim(\-2, 2)
        self.subplot2.set\_ylim(\-2, 2)
        self.subplot1.text(0.05, .95,
                           r'$X(f) = \\mathcal{F}\\{x(t)\\}$',
                           verticalalignment\='top',
                           transform\=self.subplot1.transAxes)
        self.subplot2.text(0.05, .95,
                           r'$x(t) = a \\cdot \\cos(2\\pi f\_0 t) e^{-\\pi t^2}$',
                           verticalalignment\='top',
                           transform\=self.subplot2.transAxes)

    def compute(self, f0, A):
        f \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-6., 6., 0.02)
        t \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-2., 2., 0.01)
        x \= A \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* f0 \* t) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* t \*\* 2)
        X \= A / 2 \* \\
            ([np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* (f \- f0) \*\* 2) + [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
 \* (f + f0) \*\* 2))
        return f, X, t, x

    def setKnob(self, value):
        \# Note, we ignore value arg here and just go by state of the params
        x1, y1, x2, y2 \= self.compute(self.f0.value, self.A.value)
        \# update the data of the two waveforms
        self.lines\[0\].set(xdata\=x1, ydata\=y1)
        self.lines\[1\].set(xdata\=x2, ydata\=y2)
        \# make the canvas draw its contents again with the new data
        self.canvas.draw()

class App([wx.App](https://docs.wxpython.org/wx.App.html#wx.App "wx.App")
):
    def OnInit(self):
        self.frame1 \= FourierDemoFrame(parent\=None, title\="Fourier Demo",
                                       size\=(640, 480))
        self.frame1.Show()
        return True

if \_\_name\_\_ \== "\_\_main\_\_":
    app \= App()
    app.MainLoop()

[`Download Jupyter notebook: fourier_demo_wx_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/5990feb78f8d1c9c4522f857da4a26ee/fourier_demo_wx_sgskip.ipynb)

[`Download Python source code: fourier_demo_wx_sgskip.py`](https://matplotlib.org/stable/_downloads/91f22990514946c3765a84044904bb84/fourier_demo_wx_sgskip.py)

[`Download zipped: fourier_demo_wx_sgskip.zip`](https://matplotlib.org/stable/_downloads/9fe7e2432d0d85d7d93b6cbdf48e57b8/fourier_demo_wx_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)