[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.config_context.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.config_context.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.config_context.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.config_context.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.config_context.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.config_context.html)

Collapse Sidebar Expand Sidebar

config\_context[#](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#config-context "Link to this heading")

========================================================================================================================================

sklearn.config\_context(_\*_, _assume\_finite\=None_, _working\_memory\=None_, _print\_changed\_only\=None_, _display\=None_, _pairwise\_dist\_chunk\_size\=None_, _enable\_cython\_pairwise\_dist\=None_, _array\_api\_dispatch\=None_, _transform\_output\=None_, _enable\_metadata\_routing\=None_, _skip\_parameter\_validation\=None_, _sparse\_interface\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/_config.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "Link to this definition")

Context manager to temporarily change the global scikit-learn configuration.

This context manager can be used to apply scikit-learn configuration changes within the scope of the with statement. Once the context exits, the global configuration is restored again.

The default global configurations (which take effect when scikit-learn is imported) are defined below in the parameter list.

Parameters:

**assume\_finite**bool, default=None

If True, validation for finiteness will be skipped, saving time, but leading to potential crashes. If False, validation for finiteness will be performed, avoiding error. If None, the existing configuration won’t change. Global default: False.

**working\_memory**int, default=None

If set, scikit-learn will attempt to limit the size of temporary arrays to this number of MiB (per job when parallelised), often saving both computation time and memory on expensive operations that can be performed in chunks. If None, the existing configuration won’t change. Global default: 1024.

**print\_changed\_only**bool, default=None

If True, only the parameters that were set to non-default values will be printed when printing an estimator. For example, `print(SVC())` while True will only print ‘SVC()’, but would print ‘SVC(C=1.0, cache\_size=200, …)’ with all the non-changed parameters when False. If None, the existing configuration won’t change. Global default: True.

Changed in version 0.23: Global default configuration changed from False to True.

**display**{‘text’, ‘diagram’}, default=None

If ‘diagram’, estimators will be displayed as a diagram in a Jupyter lab or notebook context. If ‘text’, estimators will be displayed as text. If None, the existing configuration won’t change. Global default: ‘diagram’.

Added in version 0.23.

**pairwise\_dist\_chunk\_size**int, default=None

The number of row vectors per chunk for the accelerated pairwise- distances reduction backend. Global default: 256 (suitable for most of modern laptops’ caches and architectures).

Intended for easier benchmarking and testing of scikit-learn internals. End users are not expected to benefit from customizing this configuration setting.

Added in version 1.1.

**enable\_cython\_pairwise\_dist**bool, default=None

Use the accelerated pairwise-distances reduction backend when possible. Global default: True.

Intended for easier benchmarking and testing of scikit-learn internals. End users are not expected to benefit from customizing this configuration setting.

Added in version 1.1.

**array\_api\_dispatch**bool, default=None

Use Array API dispatching when inputs follow the Array API standard. Global default: False.

See the [User Guide](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

Added in version 1.2.

**transform\_output**str, default=None

Configure output of `transform` and `fit_transform`.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Global default: “default”.

Added in version 1.2.

Added in version 1.4: `"polars"` option was added.

**enable\_metadata\_routing**bool, default=None

Enable metadata routing. By default this feature is disabled.

Refer to [metadata routing user guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   `True`: Metadata routing is enabled
    
*   `False`: Metadata routing is disabled, use the old syntax.
    
*   `None`: Configuration is unchanged
    

Global default: False.

Added in version 1.3.

**skip\_parameter\_validation**bool, default=None

If `True`, disable the validation of the hyper-parameters’ types and values in the fit method of estimators and for arguments passed to public helper functions. It can save time in some situations but can lead to low level crashes and exceptions with confusing error messages. Global default: False.

Note that for data parameters, such as `X` and `y`, only type validation is skipped but validation with `check_array` will continue to run.

Added in version 1.3.

**sparse\_interface**str, default=”spmatrix”

The sparse interface used for every sparse object that scikit-learn produces, e.g., function returns, estimator attributes, estimator properties, etc.

*   `"sparray"`: Return sparse as SciPy sparse array
    
*   `"spmatrix"`: Return sparse as SciPy sparse matrix
    

Added in version 1.8.

Yields:

None.

See also

[`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")

Set global scikit-learn configuration.

[`get_config`](https://scikit-learn.org/stable/modules/generated/sklearn.get_config.html#sklearn.get_config "sklearn.get_config")

Retrieve current values of the global configuration.

Notes

All settings, not just those presently modified, will be returned to their previous values when the context manager is exited.

Examples

\>>> import sklearn
\>>> from sklearn.utils.validation import assert\_all\_finite
\>>> with sklearn.config\_context(assume\_finite\=True):
...     assert\_all\_finite(\[float('nan')\])
\>>> with sklearn.config\_context(assume\_finite\=True):
...     with sklearn.config\_context(assume\_finite\=False):
...         assert\_all\_finite(\[float('nan')\])
Traceback (most recent call last):
...
ValueError: Input contains NaN...

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)

[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)

Introducing the set\_output API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)