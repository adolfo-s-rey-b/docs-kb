[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#main-content)

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
    

matplotlib.axes.Axes.set\_prop\_cycle[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib-axes-axes-set-prop-cycle "Link to this heading")

========================================================================================================================================================================================

Axes.set\_prop\_cycle(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L1624-L1698)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "Link to this definition")

Set the property cycle of the Axes.

The property cycle controls the style properties such as color, marker and linestyle of future plot commands. The style properties of data already added to the Axes are not modified.

Call signatures:

set\_prop\_cycle(cycler)
set\_prop\_cycle(label\=values, label2\=values2, ...)
set\_prop\_cycle(label, values)

Form 1 sets given [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 object.

Form 2 creates a [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 which cycles over one or more properties simultaneously and set it as the property cycle of the Axes. If multiple properties are given, their value lists must have the same length. This is just a shortcut for explicitly creating a cycler and passing it to the function, i.e. it's short for `set_prop_cycle(cycler(label=values, label2=values2, ...))`.

Form 3 creates a [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 for a single property and set it as the property cycle of the Axes. This form exists for compatibility with the original [`cycler.cycler`](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "(in cycler v0.12)")
 interface. Its use is discouraged in favor of the kwarg form, i.e. `set_prop_cycle(label=values)`.

Parameters:

**cycler**[`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 or `None`

Set the given Cycler. _None_ resets to the cycle defined by the current style.

**label**str

The property key. Must be a valid [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 property. For example, 'color' or 'linestyle'. Aliases are allowed, such as 'c' for 'color' and 'lw' for 'linewidth'.

**values**iterable

Finite-length iterable of the property values. These values are validated and will raise a ValueError if invalid.

See also

[`matplotlib.rcsetup.cycler`](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.cycler "matplotlib.rcsetup.cycler")

Convenience function for creating validated cyclers for properties.

[`cycler.cycler`](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "(in cycler v0.12)")

The original function for creating unvalidated cyclers.

Examples

Setting the property cycle for a single property:

\>>> ax.set\_prop\_cycle(color\=\['red', 'green', 'blue'\])

Setting the property cycle for simultaneously cycling over multiple properties (e.g. red circle, green plus, blue cross):

\>>> ax.set\_prop\_cycle(color\=\['red', 'green', 'blue'\],
...                   marker\=\['o', '+', 'x'\])

Examples using `matplotlib.axes.Axes.set_prop_cycle`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#examples-using-matplotlib-axes-axes-set-prop-cycle "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_thumb.png)

[Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html)

Styling with cycler

On this page