[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/resample.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/resample.html#sphx-glr-download-gallery-event-handling-resample-py)
 to download the full example code.

Resampling Data[#](https://matplotlib.org/stable/gallery/event_handling/resample.html#resampling-data "Link to this heading")

==============================================================================================================================

Downsampling lowers the sample rate or sample size of a signal. In this tutorial, the signal is downsampled when the plot is adjusted through dragging and zooming.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

import matplotlib.pyplot as plt
import numpy as np

\# A class that will downsample the data and recompute when zoomed.
class DataDisplayDownsampler:
    def \_\_init\_\_(self, [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
        self.origY1Data \= [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
        self.origY2Data \= [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
        self.origXData \= [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
        self.max\_points \= 50
        self.delta \= [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\] \- [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\]

    def plot(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
        x, y1, y2 \= self.\_downsample(self.origXData.min(), self.origXData.max())
        (self.line,) \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(x, y1, 'o-')
        self.poly\_collection \= [ax.fill\_between](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
(x, y1, y2, step\="pre", color\="r")

    def \_downsample(self, xstart, xend):
        \# get the points in the view range
        mask \= (self.origXData \> xstart) & (self.origXData < xend)
        \# dilate the mask by one to catch the points just outside
        \# of the view range to not truncate the line
        mask \= [np.convolve](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
(\[1, 1, 1\], mask, mode\='same').astype(bool)
        \# sort out how many points to drop
        ratio \= max([np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(mask) // self.max\_points, 1)

        \# mask data
        [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= self.origXData\[mask\]
        [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= self.origY1Data\[mask\]
        [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= self.origY2Data\[mask\]

        \# downsample data
        [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::ratio\]
        [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::ratio\]
        [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::ratio\]

        print(f"using {len([y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)} of {[np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(mask)} visible points")

        return [xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

    def update(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
):
        \# Update the artists
        lims \= [ax.viewLim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
        if abs(lims.width \- self.delta) \> 1e-8:
            self.delta \= lims.width
            xstart, xend \= lims.intervalx
            x, y1, y2 \= self.\_downsample(xstart, xend)
            self.line.set\_data(x, y1)
            self.poly\_collection.set\_data(x, y1, y2, step\="pre")
            [ax.figure.canvas.draw\_idle](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
()

\# Create a signal
[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(16, 365, (365\-16)\*4)
[y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/153) + [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/127)
[y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + .2

d \= DataDisplayDownsampler([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Hook up the line
d.plot([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)
[ax.set\_autoscale\_on](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on")
(False)  \# Otherwise, infinite loop

\# Connect for changing the view limits
[ax.callbacks.connect](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.CallbackRegistry.connect "matplotlib.cbook.CallbackRegistry.connect")
('xlim\_changed', d.update)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(16, 365)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![resample](https://matplotlib.org/stable/_images/sphx_glr_resample_001_2_00x.png)

using 52 of 1396 visible points

Tags: [interactivity: zoom](https://matplotlib.org/stable/_tags/interactivity-zoom.html)
 [interactivity: event-handling](https://matplotlib.org/stable/_tags/interactivity-event-handling.html)

[`Download Jupyter notebook: resample.ipynb`](https://matplotlib.org/stable/_downloads/95abeb9ea753e4e02ca3888ad6501f04/resample.ipynb)

[`Download Python source code: resample.py`](https://matplotlib.org/stable/_downloads/58860601ba402c68bbd750a99c1bc502/resample.py)

[`Download zipped: resample.zip`](https://matplotlib.org/stable/_downloads/44546ab760d6aa74319567c88a7cebf3/resample.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)