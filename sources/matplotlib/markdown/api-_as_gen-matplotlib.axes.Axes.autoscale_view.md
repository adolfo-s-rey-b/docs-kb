[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#main-content)

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
    

matplotlib.axes.Axes.autoscale\_view[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib-axes-axes-autoscale-view "Link to this heading")

=======================================================================================================================================================================================

Axes.autoscale\_view(_tight\=None_, _scalex\=True_, _scaley\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3092-L3229)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "Link to this definition")

Autoscale the view limits using the data limits.

Parameters:

**tight**bool or None

If _True_, only expand the axis limits using the margins. Note that unlike for [`autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
, `tight=True` does _not_ set the margins to zero.

If _False_ and `[rcParams["axes.autolimit_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.autolimit_mode#rcparam-axes-autolimit-mode) ` (default: `'data'`) is 'round\_numbers', then after expansion by the margins, further expand the axis limits using the axis major locator.

If None (the default), reuse the value set in the previous call to [`autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
 (the initial value is False, but the default style sets `[rcParams["axes.autolimit_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.autolimit_mode#rcparam-axes-autolimit-mode) ` (default: `'data'`) to 'data', in which case this behaves like True).

**scalex**bool, default: True

Whether to autoscale the x-axis.

**scaley**bool, default: True

Whether to autoscale the y-axis.

Notes

The autoscaling preserves any preexisting axis direction reversal.

The data limits are not updated automatically when artist data are changed after the artist has been added to an Axes instance. In that case, use [`matplotlib.axes.Axes.relim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
 prior to calling autoscale\_view.

If the views of the Axes are fixed, e.g. via [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
, they will not be changed by autoscale\_view(). See [`matplotlib.axes.Axes.autoscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
 for an alternative.

Examples using `matplotlib.axes.Axes.autoscale_view`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#examples-using-matplotlib-axes-axes-autoscale-view "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_compound_path_thumb.png)

[Compound path](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html)

Compound path

![](https://matplotlib.org/stable/_images/sphx_glr_textbox_thumb.png)

[Textbox](https://matplotlib.org/stable/gallery/widgets/textbox.html)

Textbox

![](https://matplotlib.org/stable/_images/sphx_glr_bar_unit_demo_thumb.png)

[Group barchart with units](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html)

Group barchart with units

![](https://matplotlib.org/stable/_images/sphx_glr_histogram_path_thumb.png)

[Building histograms using Rectangles and PolyCollections](https://matplotlib.org/stable/gallery/misc/histogram_path.html)

Building histograms using Rectangles and PolyCollections

![](https://matplotlib.org/stable/_images/sphx_glr_packed_bubbles_thumb.png)

[Packed-bubble chart](https://matplotlib.org/stable/gallery/misc/packed_bubbles.html)

Packed-bubble chart

![](https://matplotlib.org/stable/_images/sphx_glr_autoscale_thumb.png)

[Axis autoscaling](https://matplotlib.org/stable/users/explain/axes/autoscale.html)

Axis autoscaling

On this page