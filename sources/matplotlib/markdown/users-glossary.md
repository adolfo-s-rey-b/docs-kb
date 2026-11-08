[Skip to main content](https://matplotlib.org/stable/users/glossary.html#main-content)

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
    

Glossary[#](https://matplotlib.org/stable/users/glossary.html#glossary "Link to this heading")

===============================================================================================

This glossary defines concepts and terminology specific to Matplotlib.

Figure[#](https://matplotlib.org/stable/users/glossary.html#term-Figure "Link to this term")

The outermost container for a Matplotlib graphic. Think of this as the canvas to draw on.

This is implemented in the class [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. For more details see [Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-intro)
.

Axes[#](https://matplotlib.org/stable/users/glossary.html#term-Axes "Link to this term")

This is a container for what is often colloquially called a plot/chart/graph. It's a data area with [Axis](https://matplotlib.org/stable/users/glossary.html#term-Axis)
es, i.e. coordinate directions, and includes data artists like lines, bars etc. as well as decorations like title, axis labels, legend.

Since most "plotting operations" are realized as methods on [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 this is the object users will mostly interact with.

Note: The term _Axes_ was taken over from MATLAB. Think of this as a container spanned by the _x_\- and _y_\-axis, including decoration and data.

Axis[#](https://matplotlib.org/stable/users/glossary.html#term-Axis "Link to this term")

A direction with a scale. The scale defines the mapping from data coordinates to screen coordinates. The Axis also includes the ticks and axis label.

Artist[#](https://matplotlib.org/stable/users/glossary.html#term-Artist "Link to this term")

The base class for all graphical element that can be drawn. Examples are Lines, Rectangles, Text, Ticks, Legend, Axes, ...