[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#main-content)

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
    

matplotlib.pyplot.ylim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib-pyplot-ylim "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.ylim(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2277-L2311)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "Link to this definition")

Get or set the y-limits of the current Axes.

Call signatures:

bottom, top \= ylim()  \# return the current ylim
ylim((bottom, top))   \# set the ylim to bottom, top
ylim(bottom, top)     \# set the ylim to bottom, top

If you do not specify args, you can alternatively pass _bottom_ or _top_ as kwargs, i.e.:

ylim(top\=3)  \# adjust the top leaving bottom unchanged
ylim(bottom\=1)  \# adjust the bottom leaving top unchanged

Setting limits turns autoscaling off for the y-axis.

Returns:

bottom, top

A tuple of the new y-axis limits.

Notes

Calling this function with no arguments (e.g. `ylim()`) is the pyplot equivalent of calling [`get_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#matplotlib.axes.Axes.get_ylim "matplotlib.axes.Axes.get_ylim")
 on the current Axes. Calling this function with arguments is the pyplot equivalent of calling [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
 on the current Axes. All arguments are passed though.

Examples using `matplotlib.pyplot.ylim`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#examples-using-matplotlib-pyplot-ylim "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_frame_grabbing_sgskip_thumb.png)

[Frame grabbing](https://matplotlib.org/stable/gallery/animation/frame_grabbing_sgskip.html)

Frame grabbing

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

![](https://matplotlib.org/stable/_images/sphx_glr_findobj_demo_thumb.png)

[Findobj Demo](https://matplotlib.org/stable/gallery/misc/findobj_demo.html)

Findobj Demo

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

On this page