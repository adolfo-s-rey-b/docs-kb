[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.autoscale.html#main-content)

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
    

matplotlib.pyplot.autoscale[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.autoscale.html#matplotlib-pyplot-autoscale "Link to this heading")

==============================================================================================================================================================

matplotlib.pyplot.autoscale(_enable\=True_, _axis\='both'_, _tight\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L3065-L3071)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.autoscale.html#matplotlib.pyplot.autoscale "Link to this definition")

Autoscale the axis view to the data (toggle).

Convenience method for simple axis view autoscaling. This:

*   Turns autoscaling on or off ([`set_autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on")
     / [`set_autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on")
    ).
    
*   Ensures that view limits will get updated when needed. - As view limits are lazy-updated, this technically marks the view limits as stale.
    

Parameters:

**enable**bool or None, default: True

True turns autoscaling on, False turns it off. None leaves the autoscaling state unchanged.

**axis**{'both', 'x', 'y'}, default: 'both'

The axis on which to operate. (For 3D Axes, _axis_ can also be set to 'z', and 'both' refers to all three Axes.)

**tight**bool or None, default: None

If True, first set the margins to zero. Then, this argument is forwarded to [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
 (regardless of its value); see the description of its behavior there.

See also

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html#autoscale)

[`matplotlib.axes.Axes.set_autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on")

[`matplotlib.axes.Axes.set_autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on")

[`matplotlib.axes.Axes.set_autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on")

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
.

On this page