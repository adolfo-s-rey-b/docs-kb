[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_divider[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.html#module-mpl_toolkits.axes_grid1.axes_divider "Link to this heading")

===================================================================================================================================================================================================

Helper classes to adjust the positions of multiple axes at drawing time.

Classes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.html#classes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`AxesDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "mpl_toolkits.axes_grid1.axes_divider.AxesDivider")<br>(axes\[, xref, yref\]) | Divider based on the preexisting axes. |
| [`Divider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.axes_divider.Divider")<br>(fig, pos, horizontal, vertical\[, ...\]) | An Axes positioning class. |
| [`HBoxDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.HBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.HBoxDivider "mpl_toolkits.axes_grid1.axes_divider.HBoxDivider")<br>(fig, \*args\[, horizontal, ...\]) | A [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")<br> for laying out axes horizontally, while ensuring that they have equal heights. |
| [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")<br>(fig, \*args\[, horizontal, ...\]) | The Divider class whose rectangle area is specified as a subplot geometry. |
| [`VBoxDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.VBoxDivider.html#mpl_toolkits.axes_grid1.axes_divider.VBoxDivider "mpl_toolkits.axes_grid1.axes_divider.VBoxDivider")<br>(fig, \*args\[, horizontal, ...\]) | A [`SubplotDivider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.SubplotDivider.html#mpl_toolkits.axes_grid1.axes_divider.SubplotDivider "mpl_toolkits.axes_grid1.axes_divider.SubplotDivider")<br> for laying out axes vertically, while ensuring that they have equal widths. |

Functions[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.html#functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`make_axes_area_auto_adjustable`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable "mpl_toolkits.axes_grid1.axes_divider.make_axes_area_auto_adjustable")<br>(ax\[, ...\]) | Add auto-adjustable padding around _ax_ to take its decorations (title, labels, ticks, ticklabels) into account during layout, using [`Divider.add_auto_adjustable_area`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.add_auto_adjustable_area "mpl_toolkits.axes_grid1.axes_divider.Divider.add_auto_adjustable_area")<br>. |
| [`make_axes_locatable`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable.html#mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable "mpl_toolkits.axes_grid1.axes_divider.make_axes_locatable")<br>(axes) |     |

On this page