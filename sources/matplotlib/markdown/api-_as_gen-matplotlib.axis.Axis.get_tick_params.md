[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#main-content)

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
    

matplotlib.axis.Axis.get\_tick\_params[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib-axis-axis-get-tick-params "Link to this heading")

===========================================================================================================================================================================================

Axis.get\_tick\_params(_which\='major'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L1037-L1089)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_tick_params.html#matplotlib.axis.Axis.get_tick_params "Link to this definition")

Get appearance parameters for ticks, ticklabels, and gridlines.

Added in version 3.7.

Parameters:

**which**{'major', 'minor'}, default: 'major'

The group of ticks for which the parameters are retrieved.

Returns:

dict

Properties for styling tick elements added to the axis.

Notes

This method returns the appearance parameters for styling _new_ elements added to this axis and may be different from the values on current elements if they were modified directly by the user (e.g., via `set_*` methods on individual tick objects).

Examples

\>>> ax.yaxis.set\_tick\_params(labelsize\=30, labelcolor\='red',
...                          direction\='out', which\='major')
\>>> ax.yaxis.get\_tick\_params(which\='major')
{'direction': 'out',
'left': True,
'right': False,
'labelleft': True,
'labelright': False,
'gridOn': False,
'labelsize': 30,
'labelcolor': 'red'}
\>>> ax.yaxis.get\_tick\_params(which\='minor')
{'left': True,
'right': False,
'labelleft': True,
'labelright': False,
'gridOn': False}

On this page