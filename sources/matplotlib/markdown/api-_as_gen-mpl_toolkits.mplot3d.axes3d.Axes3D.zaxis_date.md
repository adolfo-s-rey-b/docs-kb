[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.zaxis\_date[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date.html#mpl-toolkits-mplot3d-axes3d-axes3d-zaxis-date "Link to this heading")

======================================================================================================================================================================================================================

Axes3D.zaxis\_date(_tz\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L74-L75)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date.html#mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_date "Link to this definition")

Set up axis ticks and labels to treat data along the zaxis as dates.

Parameters:

**tz**str or [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "(in Python v3.14)")
, default: `[rcParams["timezone"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=timezone#rcparam-timezone) ` (default: `'UTC'`)

The timezone used to create date labels.

Notes

This function is merely provided for completeness, but 3D Axes do not support dates for ticks, and so this may not work as expected.

On this page