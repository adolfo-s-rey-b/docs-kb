[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#main-content)

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
    

matplotlib.pyplot.xkcd[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib-pyplot-xkcd "Link to this heading")

===============================================================================================================================================

matplotlib.pyplot.xkcd(_scale\=1_, _length\=100_, _randomness\=2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L833-L898)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd "Link to this definition")

Turn on [xkcd](https://xkcd.com/)
 sketch-style drawing mode.

This will only have an effect on things drawn after this function is called.

For best results, install the [xkcd script](https://github.com/ipython/xkcd-font/)
 font; xkcd fonts are not packaged with Matplotlib.

Parameters:

**scale**float, optional

The amplitude of the wiggle perpendicular to the source line.

**length**float, optional

The length of the wiggle along the line.

**randomness**float, optional

The scale factor by which the length is shrunken or expanded.

Notes

This function works by a number of rcParams, overriding those set before.

If you want the effects of this function to be temporary, it can be used as a context manager, for example:

with plt.xkcd():
    \# This figure will be in XKCD-style
    fig1 \= plt.figure()
    \# ...

\# This figure will be in regular style
fig2 \= plt.figure()

Examples using `matplotlib.pyplot.xkcd`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#examples-using-matplotlib-pyplot-xkcd "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_xkcd_thumb.png)

[XKCD](https://matplotlib.org/stable/gallery/showcase/xkcd.html)

XKCD

On this page