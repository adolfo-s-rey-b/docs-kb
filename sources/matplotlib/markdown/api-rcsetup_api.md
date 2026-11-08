[Skip to main content](https://matplotlib.org/stable/api/rcsetup_api.html#main-content)

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
    

`matplotlib.rcsetup`[#](https://matplotlib.org/stable/api/rcsetup_api.html#module-matplotlib.rcsetup "Link to this heading")

=============================================================================================================================

The rcsetup module contains the validation code for customization using Matplotlib's rc settings.

Each rc setting is assigned a function used to validate any attempted changes to that setting. The validation functions are defined in the rcsetup module, and are used to construct the rcParams global object which stores the settings and is referenced throughout Matplotlib.

The default values of the rc settings are set in the default matplotlibrc file. Any additions or deletions to the parameter set listed here should also be propagated to the `lib/matplotlib/mpl-data/matplotlibrc` in Matplotlib's root source directory. New rcparams also need to be added to the RcKeyType enum in `lib/matplotlib/typing.py`.

class matplotlib.rcsetup.ValidateInStrings(_key_, _valid_, _ignorecase\=False_, _\*_, _\_deprecated\_since\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L42-L103)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.ValidateInStrings "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

_valid_ is a list of legal strings.

matplotlib.rcsetup.cycler(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L733-L815)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.cycler "Link to this definition")

Create a [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 object much like [`cycler.cycler()`](https://matplotlib.org/cycler/generated/cycler.cycler.html#cycler.cycler "(in cycler v0.12)")
, but includes input validation.

Call signatures:

cycler(cycler)
cycler(label\=values, label2\=values2, ...)
cycler(label, values)

Form 1 copies a given [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 object.

Form 2 creates a [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 which cycles over one or more properties simultaneously. If multiple properties are given, their value lists must have the same length.

Form 3 creates a [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 for a single property. This form exists for compatibility with the original cycler. Its use is discouraged in favor of the kwarg form, i.e. `cycler(label=values)`.

Parameters:

**cycler**Cycler

Copy constructor for Cycler.

**label**str

The property key. Must be a valid [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 property. For example, 'color' or 'linestyle'. Aliases are allowed, such as 'c' for 'color' and 'lw' for 'linewidth'.

**values**iterable

Finite-length iterable of the property values. These values are validated and will raise a ValueError if invalid.

Returns:

Cycler

A new [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)")
 for the given properties.

Examples

Creating a cycler for a single property:

\>>> c \= cycler(color\=\['red', 'green', 'blue'\])

Creating a cycler for simultaneously cycling over multiple properties (e.g. red circle, green plus, blue cross):

\>>> c \= cycler(color\=\['red', 'green', 'blue'\],
...            marker\=\['o', '+', 'x'\])

matplotlib.rcsetup.validate\_any(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L165-L166)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_any "Link to this definition")

matplotlib.rcsetup.validate\_anylist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_anylist "Link to this definition")

matplotlib.rcsetup.validate\_aspect(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L415-L421)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_aspect "Link to this definition")

matplotlib.rcsetup.validate\_axisbelow(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L191-L199)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_axisbelow "Link to this definition")

matplotlib.rcsetup.validate\_backend(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L309-L315)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_backend "Link to this definition")

matplotlib.rcsetup.validate\_bbox(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L611-L622)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_bbox "Link to this definition")

matplotlib.rcsetup.validate\_bool(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L179-L188)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_bool "Link to this definition")

Convert b to `bool` or raise.

matplotlib.rcsetup.validate\_color(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L375-L397)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_color "Link to this definition")

Return a valid color arg.

matplotlib.rcsetup.validate\_color\_for\_prop\_cycle(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L347-L351)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_color_for_prop_cycle "Link to this definition")

matplotlib.rcsetup.validate\_color\_or\_auto(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L335-L338)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_color_or_auto "Link to this definition")

matplotlib.rcsetup.validate\_color\_or\_inherit(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L328-L332)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_color_or_inherit "Link to this definition")

Return a valid color arg.

matplotlib.rcsetup.validate\_colorlist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_colorlist "Link to this definition")

return a list of colorspecs

matplotlib.rcsetup.validate\_cycler(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L921-L963)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_cycler "Link to this definition")

Return a Cycler object from a string repr or the object itself.

matplotlib.rcsetup.validate\_dashlist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_dashlist "Link to this definition")

matplotlib.rcsetup.validate\_dpi(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L202-L210)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_dpi "Link to this definition")

Confirm s is string 'figure' or convert s to float or raise.

matplotlib.rcsetup.validate\_fillstylelist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fillstylelist "Link to this definition")

matplotlib.rcsetup.validate\_float(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L219-L237)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_float "Link to this definition")

matplotlib.rcsetup.validate\_float\_or\_None(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L219-L237)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_float_or_None "Link to this definition")

matplotlib.rcsetup.validate\_floatlist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_floatlist "Link to this definition")

matplotlib.rcsetup.validate\_font\_properties(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L475-L477)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_font_properties "Link to this definition")

matplotlib.rcsetup.validate\_fontsize(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L431-L442)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fontsize "Link to this definition")

matplotlib.rcsetup.validate\_fontsize\_None(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L424-L428)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fontsize_None "Link to this definition")

matplotlib.rcsetup.validate\_fontsizelist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fontsizelist "Link to this definition")

matplotlib.rcsetup.validate\_fontstretch(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L461-L472)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fontstretch "Link to this definition")

matplotlib.rcsetup.validate\_fonttype(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L283-L303)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fonttype "Link to this definition")

Confirm that this is a Postscript or PDF font type that we know how to convert to.

matplotlib.rcsetup.validate\_fontweight(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L448-L458)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_fontweight "Link to this definition")

matplotlib.rcsetup.validate\_hatch(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L663-L675)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_hatch "Link to this definition")

Validate a hatch pattern. A hatch pattern string can have any sequence of the following characters: `\ / | - + * . x o O`.

matplotlib.rcsetup.validate\_hatchlist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_hatchlist "Link to this definition")

Validate a hatch pattern. A hatch pattern string can have any sequence of the following characters: `\ / | - + * . x o O`.

matplotlib.rcsetup.validate\_hist\_bins(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L966-L979)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_hist_bins "Link to this definition")

matplotlib.rcsetup.validate\_int(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L219-L237)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_int "Link to this definition")

matplotlib.rcsetup.validate\_int\_or\_None(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L219-L237)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_int_or_None "Link to this definition")

matplotlib.rcsetup.validate\_intlist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_intlist "Link to this definition")

matplotlib.rcsetup.validate\_markevery(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L574-L605)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_markevery "Link to this definition")

Validate the markevery property of a Line2D object.

Parameters:

**s**None, int, (int, int), slice, float, (float, float), or list\[int\]

Returns:

None, int, (int, int), slice, float, (float, float), or list\[int\]

matplotlib.rcsetup.validate\_markeverylist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_markeverylist "Link to this definition")

Validate the markevery property of a Line2D object.

Parameters:

**s**None, int, (int, int), slice, float, (float, float), or list\[int\]

Returns:

None, int, (int, int), slice, float, (float, float), or list\[int\]

matplotlib.rcsetup.validate\_ps\_distiller(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L506-L512)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_ps_distiller "Link to this definition")

matplotlib.rcsetup.validate\_sketch(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L625-L636)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_sketch "Link to this definition")

matplotlib.rcsetup.validate\_string(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L219-L237)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_string "Link to this definition")

matplotlib.rcsetup.validate\_string\_or\_None(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L219-L237)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_string_or_None "Link to this definition")

matplotlib.rcsetup.validate\_stringlist(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L128-L154)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_stringlist "Link to this definition")

return a list of strings

matplotlib.rcsetup.validate\_whiskers(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/rcsetup.py#L495-L503)
[#](https://matplotlib.org/stable/api/rcsetup_api.html#matplotlib.rcsetup.validate_whiskers "Link to this definition")

On this page