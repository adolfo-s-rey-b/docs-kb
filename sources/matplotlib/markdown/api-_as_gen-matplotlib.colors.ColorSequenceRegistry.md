[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#main-content)

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
    

matplotlib.colors.ColorSequenceRegistry[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib-colors-colorsequenceregistry "Link to this heading")

==================================================================================================================================================================================================

class matplotlib.colors.ColorSequenceRegistry[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L99-L203)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "Link to this definition")

Bases: [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")

Container for sequences of colors that are known to Matplotlib by name.

The universal registry instance is [`matplotlib.color_sequences`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.color_sequences "matplotlib.color_sequences")
. There should be no need for users to instantiate [`ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
 themselves.

Read access uses a dict-like interface mapping names to lists of colors:

import matplotlib as mpl
colors \= mpl.color\_sequences\['tab10'\]

For a list of built in color sequences, see [Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)
. The returned lists are copies, so that their modification does not change the global definition of the color sequence.

Additional color sequences can be added via [`ColorSequenceRegistry.register`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry.register "matplotlib.colors.ColorSequenceRegistry.register")
:

mpl.color\_sequences.register('rgb', \['r', 'g', 'b'\])

register(_name_, _color\_list_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L158-L190)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry.register "Link to this definition")

Register a new color sequence.

The color sequence registry stores a copy of the given _color\_list_, so that future changes to the original list do not affect the registered color sequence. Think of this as the registry taking a snapshot of _color\_list_ at registration.

Parameters:

**name**str

The name for the color sequence.

**color\_list**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

An iterable returning valid Matplotlib colors when iterating over. Note however that the returned color sequence will always be a list regardless of the input type.

unregister(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L192-L203)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry.unregister "Link to this definition")

Remove a sequence from the registry.

You cannot remove built-in color sequences.

If the name is not registered, returns with no error.

Examples using `matplotlib.colors.ColorSequenceRegistry`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#examples-using-matplotlib-colors-colorsequenceregistry "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_thumb.png)

[Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)

Nested pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_color_sequences_thumb.png)

[Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)

Named color sequences

On this page