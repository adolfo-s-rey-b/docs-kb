[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#main-content)

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
    

matplotlib.pyplot.ginput[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib-pyplot-ginput "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.ginput(_n\=1_, _timeout\=30_, _show\_clicks\=True_, _mouse\_add\=MouseButton.LEFT_, _mouse\_pop\=MouseButton.RIGHT_, _mouse\_stop\=MouseButton.MIDDLE_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2943-L2959)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib.pyplot.ginput "Link to this definition")

Blocking call to interact with a figure.

Wait until the user clicks _n_ times on the figure, and return the coordinates of each click in a list.

There are three possible interactions:

*   Add a point.
    
*   Remove the most recently added point.
    
*   Stop the interaction and return the points added so far.
    

The actions are assigned to mouse buttons via the arguments _mouse\_add_, _mouse\_pop_ and _mouse\_stop_.

Parameters:

**n**int, default: 1

Number of mouse clicks to accumulate. If negative, accumulate clicks until the input is terminated manually.

**timeout**float, default: 30 seconds

Number of seconds to wait before timing out. If zero or negative will never time out.

**show\_clicks**bool, default: True

If True, show a red cross at the location of each click.

**mouse\_add**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
 or None, default: [`MouseButton.LEFT`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.LEFT "matplotlib.backend_bases.MouseButton.LEFT")

Mouse button used to add points.

**mouse\_pop**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
 or None, default: [`MouseButton.RIGHT`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.RIGHT "matplotlib.backend_bases.MouseButton.RIGHT")

Mouse button used to remove the most recently added point.

**mouse\_stop**[`MouseButton`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton "matplotlib.backend_bases.MouseButton")
 or None, default: [`MouseButton.MIDDLE`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton.MIDDLE "matplotlib.backend_bases.MouseButton.MIDDLE")

Mouse button used to stop input.

Returns:

list of tuples

A list of the clicked (x, y) coordinates.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.ginput.html#matplotlib.figure.Figure.ginput "matplotlib.figure.Figure.ginput")
.

The keyboard can also be used to select points in case your mouse does not have one or more of the buttons. The delete and backspace keys act like right-clicking (i.e., remove last point), the enter key terminates input and any other key (not already used by the window manager) selects a point.

Examples using `matplotlib.pyplot.ginput`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#examples-using-matplotlib-pyplot-ginput "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

On this page