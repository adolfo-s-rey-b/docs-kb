[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#main-content)

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
    

mpl\_toolkits.axisartist.grid\_finder.DictFormatter[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#mpl-toolkits-axisartist-grid-finder-dictformatter "Link to this heading")

==================================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.grid\_finder.DictFormatter(_format\_dict_, _formatter\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L308-L328)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#mpl_toolkits.axisartist.grid_finder.DictFormatter "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

format\_dict : dictionary for format strings to be used. formatter : fall-back formatter

\_\_call\_\_(_direction_, _factor_, _values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L318-L328)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#mpl_toolkits.axisartist.grid_finder.DictFormatter.__call__ "Link to this definition")

factor is ignored if value is found in the dictionary

Examples using `mpl_toolkits.axisartist.grid_finder.DictFormatter`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.DictFormatter.html#examples-using-mpl-toolkits-axisartist-grid-finder-dictformatter "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

On this page