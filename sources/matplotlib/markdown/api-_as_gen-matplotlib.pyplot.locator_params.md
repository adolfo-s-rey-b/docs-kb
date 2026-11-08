[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.locator_params.html#main-content)

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
    

matplotlib.pyplot.locator\_params[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.locator_params.html#matplotlib-pyplot-locator-params "Link to this heading")

==============================================================================================================================================================================

matplotlib.pyplot.locator\_params(_axis\='both'_, _tight\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3815-L3819)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.locator_params.html#matplotlib.pyplot.locator_params "Link to this definition")

Control behavior of major tick locators.

Because the locator is involved in autoscaling, [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
 is called automatically after the parameters are changed.

Parameters:

**axis**{'both', 'x', 'y'}, default: 'both'

The axis on which to operate. (For 3D Axes, _axis_ can also be set to 'z', and 'both' refers to all three axes.)

**tight**bool or None, optional

Parameter passed to [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
. Default is None, for no change.

Other Parameters:

**\*\*kwargs**

Remaining keyword arguments are passed to directly to the `set_params()` method of the locator. Supported keywords depend on the type of the locator. See for example [`set_params`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator.set_params "matplotlib.ticker.MaxNLocator.set_params")
 for the [`ticker.MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
 used by default for linear.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.locator_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html#matplotlib.axes.Axes.locator_params "matplotlib.axes.Axes.locator_params")
.

Examples

When plotting small subplots, one might want to reduce the maximum number of ticks and use tight bounds, for example:

ax.locator\_params(tight\=True, nbins\=4)

On this page