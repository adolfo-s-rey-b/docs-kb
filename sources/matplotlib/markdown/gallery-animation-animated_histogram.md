[Skip to main content](https://matplotlib.org/stable/gallery/animation/animated_histogram.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/animation/animated_histogram.html#sphx-glr-download-gallery-animation-animated-histogram-py)
 to download the full example code.

Animated histogram[#](https://matplotlib.org/stable/gallery/animation/animated_histogram.html#animated-histogram "Link to this heading")

=========================================================================================================================================

Use histogram's [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 to draw a bunch of rectangles for an animated histogram.

import functools

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

\# Setting up a random number generator with a fixed state for reproducibility.
[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(seed\=19680801)
\# Fixing bin edges.
[HIST\_BINS](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-4, 4, 100)

\# Histogram our data with numpy.
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
(1000)
[n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [HIST\_BINS](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

To animate the histogram, we need an `animate` function, which generates a random set of numbers and updates the heights of rectangles. The `animate` function updates the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 patches on an instance of [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
.

def animate(frame\_number, [bar\_container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
):
    \# Simulate new data coming in.
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.standard\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_normal.html#numpy.random.Generator.standard_normal "numpy.random.Generator.standard_normal")
(1000)
    [n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [HIST\_BINS](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    for count, rect in zip([n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bar\_container.patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        rect.set\_height(count)

    return [bar\_container.patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

Using [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
 allows us to get an instance of [`BarContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
, which is a collection of [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 instances. Since [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 will only pass the frame number parameter to the animation function, we use [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.14)")
 to fix the `bar_container` parameter.

\# Output generated via \`matplotlib.animation.Animation.to\_jshtml\`.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bar\_container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [HIST\_BINS](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=1,
                              ec\="yellow", fc\="green", alpha\=0.5)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(top\=55)  \# set safe limit to ensure that all data is visible.

[anim](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 \= [functools.partial](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
(animate, [bar\_container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
\=[bar\_container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
)
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [anim](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
, 50, repeat\=False, blit\=True)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [component: animation](https://matplotlib.org/stable/_tags/component-animation.html)

**Total running time of the script:** (0 minutes 16.824 seconds)

[`Download Jupyter notebook: animated_histogram.ipynb`](https://matplotlib.org/stable/_downloads/5dbe235f5ce060079b6f2f2cc97499de/animated_histogram.ipynb)

[`Download Python source code: animated_histogram.py`](https://matplotlib.org/stable/_downloads/0609ba7da6aff274c9d51ded96d741f0/animated_histogram.py)

[`Download zipped: animated_histogram.zip`](https://matplotlib.org/stable/_downloads/fe900e88f3412932cf56f4d2d51a26f2/animated_histogram.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)