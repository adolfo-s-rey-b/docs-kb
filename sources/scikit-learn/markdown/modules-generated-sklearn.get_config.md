[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.get_config.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

get\_config[#](https://scikit-learn.org/stable/modules/generated/sklearn.get_config.html#get-config "Link to this heading")

============================================================================================================================

sklearn.get\_config()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/_config.py#L36)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.get_config.html#sklearn.get_config "Link to this definition")

Retrieve the current scikit-learn configuration.

This reflects the effective global configurations as established by default upon library import, or modified via [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
 or [`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
.

Returns:

**config**dict

Keys are parameter names that can be passed to [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
.

See also

[`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")

Context manager for global scikit-learn configuration.

[`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")

Set global scikit-learn configuration.

Examples

\>>> import sklearn
\>>> config \= sklearn.get\_config()
\>>> config.keys()
dict\_keys(\[...\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)