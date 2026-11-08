[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html#main-content)

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
    

matplotlib.pyplot.polar[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html#matplotlib-pyplot-polar "Link to this heading")

==================================================================================================================================================

matplotlib.pyplot.polar(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2834-L2868)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html#matplotlib.pyplot.polar "Link to this definition")

Make a polar plot.

call signature:

polar(theta, r, \[fmt\], \*\*kwargs)

This is a convenience wrapper around [`pyplot.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
. It ensures that the current Axes is polar (or creates one if needed) and then passes all parameters to `.pyplot.plot`.

Note

When making polar plots using the [pyplot API](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
, `polar()` should typically be the first command because that makes sure a polar Axes is created. Using other commands such as `plt.title()` before this can lead to the implicit creation of a rectangular Axes, in which case a subsequent `polar()` call will fail.

Examples using `matplotlib.pyplot.polar`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html#examples-using-matplotlib-pyplot-polar "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_transoffset_thumb.png)

[transforms.offset\_copy](https://matplotlib.org/stable/gallery/misc/transoffset.html)

transforms.offset\_copy

On this page