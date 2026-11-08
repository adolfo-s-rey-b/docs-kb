[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.clear_data_home.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.clear_data_home.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.clear_data_home.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.clear_data_home.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.clear_data_home.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.clear_data_home.html)

Collapse Sidebar Expand Sidebar

clear\_data\_home[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html#clear-data-home "Link to this heading")

=====================================================================================================================================================

sklearn.datasets.clear\_data\_home(_data\_home\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L89)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html#sklearn.datasets.clear_data_home "Link to this definition")

Delete all the content of the data home cache.

Parameters:

**data\_home**str or path-like, default=None

The path to scikit-learn data directory. If `None`, the default path is `~/scikit_learn_data`.

Examples

\>>> from sklearn.datasets import clear\_data\_home
\>>> clear\_data\_home()

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)