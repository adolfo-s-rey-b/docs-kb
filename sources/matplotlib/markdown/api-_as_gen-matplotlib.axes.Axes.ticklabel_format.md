[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#main-content)

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
    

matplotlib.axes.Axes.ticklabel\_format[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib-axes-axes-ticklabel-format "Link to this heading")

=============================================================================================================================================================================================

Axes.ticklabel\_format(_\*_, _axis\='both'_, _style\=None_, _scilimits\=None_, _useOffset\=None_, _useLocale\=None_, _useMathText\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L3508-L3584)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "Link to this definition")

Configure the [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 used by default for linear Axes.

If a parameter is not set, the corresponding property of the formatter is left unchanged.

Parameters:

**axis**{'x', 'y', 'both'}, default: 'both'

The axis to configure. Only major ticks are affected.

**style**{'sci', 'scientific', 'plain'}

Whether to use scientific notation. The formatter default is to use scientific notation. 'sci' is equivalent to 'scientific'.

**scilimits**pair of ints (m, n)

Scientific notation is used only for numbers outside the range 10m to 10n (and only if the formatter is configured to use scientific notation at all). Use (0, 0) to include all numbers. Use (m, m) where m != 0 to fix the order of magnitude to 10m. The formatter default is `[rcParams["axes.formatter.limits"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.limits#rcparam-axes-formatter-limits) ` (default: `[-5, 6]`).

**useOffset**bool or float

If True, the offset is calculated as needed. If False, no offset is used. If a numeric value, it sets the offset. The formatter default is `[rcParams["axes.formatter.useoffset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.useoffset#rcparam-axes-formatter-useoffset) ` (default: `True`).

**useLocale**bool

Whether to format the number using the current locale or using the C (English) locale. This affects e.g. the decimal separator. The formatter default is `[rcParams["axes.formatter.use_locale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_locale#rcparam-axes-formatter-use-locale) ` (default: `False`).

**useMathText**bool

Render the offset and scientific notation in mathtext. The formatter default is `[rcParams["axes.formatter.use_mathtext"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.use_mathtext#rcparam-axes-formatter-use-mathtext) ` (default: `False`).

Raises:

AttributeError

If the current formatter is not a [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
.

Examples using `matplotlib.axes.Axes.ticklabel_format`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#examples-using-matplotlib-axes-axes-ticklabel-format "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scalarformatter_thumb.png)

[The default tick formatter](https://matplotlib.org/stable/gallery/ticks/scalarformatter.html)

The default tick formatter

On this page