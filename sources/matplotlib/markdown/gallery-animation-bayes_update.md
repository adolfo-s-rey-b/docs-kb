[Skip to main content](https://matplotlib.org/stable/gallery/animation/bayes_update.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/bayes_update.html#sphx-glr-download-gallery-animation-bayes-update-py)
 to download the full example code.

The Bayes update[#](https://matplotlib.org/stable/gallery/animation/bayes_update.html#the-bayes-update "Link to this heading")

===============================================================================================================================

This animation displays the posterior estimate updates as it is refitted when new data arrives. The vertical line represents the theoretical value to which the plotted distribution should converge.

Output generated via [`matplotlib.animation.Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

import math

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import [FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")

def beta\_pdf(x, a, b):
    return (x\*\*(a\-1) \* (1\-x)\*\*(b\-1) \* [math.gamma](https://docs.python.org/3/library/math.html#math.gamma "math.gamma")
(a + b)
            / ([math.gamma](https://docs.python.org/3/library/math.html#math.gamma "math.gamma")
(a) \* [math.gamma](https://docs.python.org/3/library/math.html#math.gamma "math.gamma")
(b)))

class UpdateDist:
    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, prob\=0.5):
        self.success \= 0
        self.prob \= prob
        self.line, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[\], \[\], 'k-')
        self.x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 200)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

        \# Set up plot parameters
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.set\_xlim(0, 1)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.set\_ylim(0, 10)
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.grid(True)

        \# This vertical line represents the theoretical value, to
        \# which the plotted distribution should converge.
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.axvline(prob, linestyle\='--', color\='black')

    def start(self):
        \# Used for the \*init\_func\* parameter of FuncAnimation; this is called when
        \# initializing the animation, and also after resizing the figure.
        return self.line,

    def \_\_call\_\_(self, i):
        \# This way the plot can continuously run and we just keep
        \# watching new realizations of the process
        if i \== 0:
            self.success \= 0
            self.line.set\_data(\[\], \[\])
            return self.line,

        \# Choose success based on exceed a threshold with a uniform pick
        if [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
() < self.prob:
            self.success += 1
        y \= beta\_pdf(self.x, self.success + 1, (i \- self.success) + 1)
        self.line.set\_data(self.x, y)
        return self.line,

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ud \= UpdateDist([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, prob\=0.7)
[anim](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ud, init\_func\=ud.start, frames\=100, interval\=100, blit\=True)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)

**Total running time of the script:** (0 minutes 24.366 seconds)

[`Download Jupyter notebook: bayes_update.ipynb`](https://matplotlib.org/stable/_downloads/1031069b233d778873c178931f9832df/bayes_update.ipynb)

[`Download Python source code: bayes_update.py`](https://matplotlib.org/stable/_downloads/9c47d872942711ff6f2d83120a1ed2b5/bayes_update.py)

[`Download zipped: bayes_update.zip`](https://matplotlib.org/stable/_downloads/84fc9ff0c3872d8dd39cbb78967cfc8e/bayes_update.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)