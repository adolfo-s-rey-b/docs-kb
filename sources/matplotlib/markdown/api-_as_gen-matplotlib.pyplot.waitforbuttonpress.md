[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#main-content)

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
    

matplotlib.pyplot.waitforbuttonpress[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib-pyplot-waitforbuttonpress "Link to this heading")

=========================================================================================================================================================================================

matplotlib.pyplot.waitforbuttonpress(_timeout\=\-1_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2996-L2998)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib.pyplot.waitforbuttonpress "Link to this definition")

Blocking call to interact with the figure.

Wait for user input and return True if a key was pressed, False if a mouse button was pressed and None if no input was given within _timeout_ seconds. Negative values deactivate _timeout_.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`Figure.waitforbuttonpress`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.waitforbuttonpress.html#matplotlib.figure.Figure.waitforbuttonpress "matplotlib.figure.Figure.waitforbuttonpress")
.

Examples using `matplotlib.pyplot.waitforbuttonpress`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#examples-using-matplotlib-pyplot-waitforbuttonpress "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_ginput_manual_clabel_sgskip_thumb.png)

[Interactive functions](https://matplotlib.org/stable/gallery/event_handling/ginput_manual_clabel_sgskip.html)

Interactive functions

On this page