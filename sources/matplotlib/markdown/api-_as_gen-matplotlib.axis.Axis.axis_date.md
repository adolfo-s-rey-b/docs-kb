[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#main-content)

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
    

matplotlib.axis.Axis.axis\_date[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#matplotlib-axis-axis-axis-date "Link to this heading")

========================================================================================================================================================================

Axis.axis\_date(_tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2422-L2437)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#matplotlib.axis.Axis.axis_date "Link to this definition")

Set up axis ticks and labels to treat data along this Axis as dates.

Parameters:

**tz**str or [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

The timezone used to create date labels.

On this page