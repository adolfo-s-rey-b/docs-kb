[Skip to main content](https://matplotlib.org/stable/users/explain/figure/index.html#main-content)

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
    

Figures and backends[#](https://matplotlib.org/stable/users/explain/figure/index.html#figures-and-backends "Link to this heading")

===================================================================================================================================

When looking at Matplotlib visualization, you are almost always looking at Artists placed on a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. In the example below, the figure is the blue region and [`add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 has added an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 artist to the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 (see [Parts of a Figure](https://matplotlib.org/stable/users/explain/quick_start.html#figure-parts)
). A more complicated visualization can add multiple Axes to the Figure, colorbars, legends, annotations, and the Axes themselves can have multiple Artists added to them (e.g. `ax.plot` or `ax.imshow`).

fig \= plt.figure(figsize\=(4, 2), facecolor\='lightskyblue',
                 layout\='constrained')
fig.suptitle('A nice Matplotlib Figure')
ax \= fig.add\_subplot()
ax.set\_title('Axes', loc\='left', fontstyle\='oblique', fontsize\='medium')

([`Source code`](https://matplotlib.org/stable/_downloads/4afa6aaf1de4ec5296b1734d37b5d152/index-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e4d818affa557fb20cd3e0abcf72b844/index-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/dc2d3618602be4c40b4fe879ea73b6e5/index-1.png)
)

[![](https://matplotlib.org/stable/_images/users-explain-figure-index-1.2x.png)](https://matplotlib.org/stable/_images/users-explain-figure-index-1.2x.png)

*   [Introduction to figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html)
    *   [Viewing Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#viewing-figures)
        
    *   [Creating Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#creating-figures)
        
    *   [Saving Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#saving-figures)
        

*   [Output backends](https://matplotlib.org/stable/users/explain/figure/backends.html)
    
*   [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html)
    
*   [Interacting with figures](https://matplotlib.org/stable/users/explain/figure/interactive.html)
    
*   [Interactive figures and asynchronous programming](https://matplotlib.org/stable/users/explain/figure/interactive_guide.html)
    
*   [Event handling](https://matplotlib.org/stable/users/explain/figure/event_handling.html)
    
*   [Writing a backend -- the pyplot interface](https://matplotlib.org/stable/users/explain/figure/writing_a_backend_pyplot_interface.html)