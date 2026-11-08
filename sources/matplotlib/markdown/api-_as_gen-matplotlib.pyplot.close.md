[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#main-content)

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
    

matplotlib.pyplot.close[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib-pyplot-close "Link to this heading")

==================================================================================================================================================

matplotlib.pyplot.close(_fig\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L1268-L1313)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "Link to this definition")

Close a figure window, and unregister it from pyplot.

Parameters:

**fig**None or int or str or [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure to close. There are a number of ways to specify this:

*   _None_: the current figure
    
*   [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
    : the given [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
     instance
    
*   `int`: a figure number
    
*   `str`: a figure name
    
*   'all': all figures
    

Notes

pyplot maintains a reference to figures created with [`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
. When work on the figure is completed, it should be closed, i.e. deregistered from pyplot, to free its memory (see also `[rcParams["figure.max_open_warning"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.max_open_warning#rcparam-figure-max-open-warning) ` (default: `20`)). Closing a figure window created by [`show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
 automatically deregisters the figure. For all other use cases, most prominently [`savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
 without [`show()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
, the figure must be deregistered explicitly using [`close()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
.

Examples using `matplotlib.pyplot.close`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#examples-using-matplotlib-pyplot-close "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_pong_sgskip_thumb.png)

[Pong](https://matplotlib.org/stable/gallery/event_handling/pong_sgskip.html)

Pong

![](https://matplotlib.org/stable/_images/sphx_glr_multipage_pdf_thumb.svg)

[Multipage PDF](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html)

Multipage PDF

![](https://matplotlib.org/stable/_images/sphx_glr_multiprocess_sgskip_thumb.png)

[Multiprocessing](https://matplotlib.org/stable/gallery/misc/multiprocess_sgskip.html)

Multiprocessing

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page