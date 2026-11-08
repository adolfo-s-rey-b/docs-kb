[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.get_data_home.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.get_data_home.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.get_data_home.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.get_data_home.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.get_data_home.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.get_data_home.html)

Collapse Sidebar Expand Sidebar

get\_data\_home[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#get-data-home "Link to this heading")

===============================================================================================================================================

sklearn.datasets.get\_data\_home(_data\_home\=None_) → [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L42)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#sklearn.datasets.get_data_home "Link to this definition")

Return the path of the scikit-learn data directory.

This folder is used by some large dataset loaders to avoid downloading the data several times.

By default the data directory is set to a folder named ‘scikit\_learn\_data’ in the user home folder.

Alternatively, it can be set by the ‘SCIKIT\_LEARN\_DATA’ environment variable or programmatically by giving an explicit folder path. The ‘~’ symbol is expanded to the user home folder.

If the folder does not already exist, it is automatically created.

Parameters:

**data\_home**str or path-like, default=None

The path to scikit-learn data directory. If `None`, the default path is `~/scikit_learn_data`.

Returns:

data\_home: str

The path to scikit-learn data directory.

Examples

\>>> import os
\>>> from sklearn.datasets import get\_data\_home
\>>> data\_home\_path \= get\_data\_home()
\>>> os.path.exists(data\_home\_path)
True

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_out_of_core_classification_thumb.png)

[Out-of-core classification of text documents](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html)

Out-of-core classification of text documents

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)