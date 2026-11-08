[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#main-content)

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
    

matplotlib.pyplot.pause[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib-pyplot-pause "Link to this heading")

==================================================================================================================================================

matplotlib.pyplot.pause(_interval_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L767-L792)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "Link to this definition")

Run the GUI event loop for _interval_ seconds.

If there is an active figure, it will be updated and displayed before the pause, and the GUI event loop (if any) will run during the pause.

This can be used for crude animation. For more complex animation use [`matplotlib.animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")
.

If there is no active figure, sleep for _interval_ seconds instead.

See also

[`matplotlib.animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")

Proper animations

[`show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")

Show all figures and optional block until all figures are closed.

Examples using `matplotlib.pyplot.pause`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#examples-using-matplotlib-pyplot-pause "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_animation_demo_thumb.png)

[pyplot animation](https://matplotlib.org/stable/gallery/animation/animation_demo.html)

pyplot animation

![](https://matplotlib.org/stable/_images/sphx_glr_blitting_thumb.png)

[Faster rendering by using blitting](https://matplotlib.org/stable/users/explain/animations/blitting.html)

Faster rendering by using blitting

On this page