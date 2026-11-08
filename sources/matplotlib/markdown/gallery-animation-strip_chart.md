[Skip to main content](https://matplotlib.org/stable/gallery/animation/strip_chart.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/strip_chart.html#sphx-glr-download-gallery-animation-strip-chart-py)
 to download the full example code.

Oscilloscope[#](https://matplotlib.org/stable/gallery/animation/strip_chart.html#oscilloscope "Link to this heading")

======================================================================================================================

Emulates an oscilloscope.

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation
from matplotlib.lines import [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

class Scope:
    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, maxt\=2, dt\=0.02):
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
        self.dt \= dt
        self.maxt \= maxt
        self.tdata \= \[0\]
        self.ydata \= \[0\]
        self.line \= [Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
(self.tdata, self.ydata)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.add\_line(self.line)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.set\_ylim(\-.1, 1.1)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.set\_xlim(0, self.maxt)

    def update(self, y):
        lastt \= self.tdata\[\-1\]
        if lastt \>= self.tdata\[0\] + self.maxt:  \# reset the arrays
            self.tdata \= \[self.tdata\[\-1\]\]
            self.ydata \= \[self.ydata\[\-1\]\]
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.set\_xlim(self.tdata\[0\], self.tdata\[0\] + self.maxt)
            self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.figure.canvas.draw()

        \# This slightly more complex calculation avoids floating-point issues
        \# from just repeatedly adding \`self.dt\` to the previous value.
        t \= self.tdata\[0\] + len(self.tdata) \* self.dt

        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set\_data(self.tdata, self.ydata)
        return self.line,

def emitter(p\=0.1):
    """Return a random value in \[0, 1) with probability p, else 0."""\
    while True:\
        v \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
()\
        if v \> p:\
            yield 0.\
        else:\
            yield [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")\
()\
\
\# Fixing random state for reproducibility\
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")\
(19680801 // 10)\
\
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
scope \= Scope([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
)\
\
\# pass a generator in "emitter" to produce data for the update func\
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")\
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")\
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")\
, scope.update, emitter, interval\=50,\
                              blit\=True, save\_count\=100)\
\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
\# ..tags:: animation, plot-type: line\
\
**Total running time of the script:** (0 minutes 25.817 seconds)\
\
[`Download Jupyter notebook: strip_chart.ipynb`](https://matplotlib.org/stable/_downloads/0d37310d80373fee3923c5ba3d646f75/strip_chart.ipynb)\
\
[`Download Python source code: strip_chart.py`](https://matplotlib.org/stable/_downloads/bf6d0a45f5a6dec6f679c42b579ead7a/strip_chart.py)\
\
[`Download zipped: strip_chart.zip`](https://matplotlib.org/stable/_downloads/a7d2fe376018f521bc8f44e9c32cd344/strip_chart.zip)\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)