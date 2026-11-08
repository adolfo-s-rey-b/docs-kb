[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#main-content)

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
    

matplotlib.pyplot.xlim[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib-pyplot-xlim "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.xlim(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2222-L2256)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "Link to this definition")

Get or set the x limits of the current Axes.

Call signatures:

left, right \= xlim()  \# return the current xlim
xlim((left, right))   \# set the xlim to left, right
xlim(left, right)     \# set the xlim to left, right

If you do not specify args, you can pass _left_ or _right_ as kwargs, i.e.:

xlim(right\=3)  \# adjust the right leaving left unchanged
xlim(left\=1)  \# adjust the left leaving right unchanged

Setting limits turns autoscaling off for the x-axis.

Returns:

left, right

A tuple of the new x-axis limits.

Notes

Calling this function with no arguments (e.g. `xlim()`) is the pyplot equivalent of calling [`get_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib.axes.Axes.get_xlim "matplotlib.axes.Axes.get_xlim")
 on the current Axes. Calling this function with arguments is the pyplot equivalent of calling [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 on the current Axes. All arguments are passed though.

Examples using `matplotlib.pyplot.xlim`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#examples-using-matplotlib-pyplot-xlim "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_frame_grabbing_sgskip_thumb.png)

[Frame grabbing](https://matplotlib.org/stable/gallery/animation/frame_grabbing_sgskip.html)

Frame grabbing

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

On this page