[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_zmargin[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-zmargin "Link to this heading")

=========================================================================================================================================================================================================================

Axes3D.set\_zmargin(_m_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L566-L586)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zmargin "Link to this definition")

Set padding of Z data limits prior to autoscaling.

_m_ times the data interval will be added to each end of that interval before it is used in autoscaling. If _m_ is negative, this will clip the data range instead of expanding it.

For example, if your data is in the range \[0, 2\], a margin of 0.1 will result in a range \[-0.2, 2.2\]; a margin of -0.1 will result in a range of \[0.2, 1.8\].

Parameters:

**m**float greater than -0.5

On this page