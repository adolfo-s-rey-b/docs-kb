[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#main-content)

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
    

matplotlib.axis.Axis.minorticks\_on[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#matplotlib-axis-axis-minorticks-on "Link to this heading")

====================================================================================================================================================================================

Axis.minorticks\_on()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L954-L986)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#matplotlib.axis.Axis.minorticks_on "Link to this definition")

Display default minor ticks on the Axis, depending on the scale ([`get_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_scale.html#matplotlib.axis.Axis.get_scale "matplotlib.axis.Axis.get_scale")
).

Scales use specific minor locators:

*   log: [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
    
*   symlog: [`SymmetricalLogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.SymmetricalLogLocator "matplotlib.ticker.SymmetricalLogLocator")
    
*   asinh: [`AsinhLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AsinhLocator "matplotlib.ticker.AsinhLocator")
    
*   logit: [`LogitLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogitLocator "matplotlib.ticker.LogitLocator")
    
*   default: [`AutoMinorLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoMinorLocator "matplotlib.ticker.AutoMinorLocator")
    

Displaying minor ticks may reduce performance; you may turn them off using [`minorticks_off()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_off.html#matplotlib.axis.Axis.minorticks_off "matplotlib.axis.Axis.minorticks_off")
 if drawing speed is a problem.

Examples using `matplotlib.axis.Axis.minorticks_on`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.minorticks_on.html#examples-using-matplotlib-axis-axis-minorticks-on "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multiline_thumb.png)

[Multiline text](https://matplotlib.org/stable/gallery/text_labels_and_annotations/multiline.html)

Multiline text

On this page