[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#main-content)

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
    

matplotlib.pyplot.rc[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib-pyplot-rc "Link to this heading")

=========================================================================================================================================

matplotlib.pyplot.rc(_group_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L795-L797)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc "Link to this definition")

Set the current [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
. _group_ is the grouping for the rc, e.g., for `lines.linewidth` the group is `lines`, for `axes.facecolor`, the group is `axes`, and so on. Group may also be a list or tuple of group names, e.g., (_xtick_, _ytick_). _kwargs_ is a dictionary attribute name/value pairs, e.g.,:

rc('lines', linewidth\=2, color\='r')

sets the current [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 and is equivalent to:

rcParams\['lines.linewidth'\] \= 2
rcParams\['lines.color'\] \= 'r'

The following aliases are available to save typing for interactive users:

| Alias | Property |
| --- | --- |
| 'lw' | 'linewidth' |
| 'ls' | 'linestyle' |
| 'c' | 'color' |
| 'fc' | 'facecolor' |
| 'ec' | 'edgecolor' |
| 'mew' | 'markeredgewidth' |
| 'aa' | 'antialiased' |
| 'sans' | 'sans-serif' |

Thus you could abbreviate the above call as:

rc('lines', lw\=2, c\='r')

Note you can use python's kwargs dictionary facility to store dictionaries of default parameters. e.g., you can customize the font rc as follows:

font \= {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 'large'}
rc('font', \*\*font)  \# pass in the font dict as kwargs

This enables you to easily switch between several configurations. Use `matplotlib.style.use('default')` or [`rcdefaults()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcdefaults "matplotlib.rcdefaults")
 to restore the default [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 after changes.

Notes

Note

This is equivalent to [`matplotlib.rc`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc "matplotlib.rc")
.

Similar functionality is available by using the normal dict interface, i.e. `rcParams.update({"lines.linewidth": 2, ...})` (but `rcParams.update` does not support abbreviations or grouping).

Examples using `matplotlib.pyplot.rc`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#examples-using-matplotlib-pyplot-rc "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_line_demo_dash_control_thumb.png)

[Dashed line style configuration](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html)

Dashed line style configuration

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_thumb.png)

[Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html)

Styling with cycler

On this page