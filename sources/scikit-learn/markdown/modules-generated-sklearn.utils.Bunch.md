[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.Bunch.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.Bunch.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.Bunch.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.Bunch.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.Bunch.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.Bunch.html)

Collapse Sidebar Expand Sidebar

Bunch[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#bunch "Link to this heading")

==================================================================================================================

class sklearn.utils.Bunch(_\*\*kwargs_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_bunch.py#L7)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "Link to this definition")

Container object exposing keys as attributes.

Bunch objects are sometimes used as an output for functions and methods. They extend dictionaries by enabling values to be accessed by key, `bunch["value_key"]`, or by an attribute, `bunch.value_key`.

Examples

\>>> from sklearn.utils import Bunch
\>>> b \= Bunch(a\=1, b\=2)
\>>> b\['b'\]
2
\>>> b.b
2
\>>> b.a \= 3
\>>> b\['a'\]
3
\>>> b.c \= 6
\>>> b\['c'\]
6

Copy to clipboard

clear(_/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.clear "Link to this definition")

Remove all items from the dict.

copy(_/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.copy "Link to this definition")

Return a shallow copy of the dict.

classmethod fromkeys(_iterable_, _value\=None_, _/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.fromkeys "Link to this definition")

Create a new dictionary with keys from iterable and values set to value.

get(_key_, _default\=None_, _/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.get "Link to this definition")

Return the value for key if key is in the dictionary, else default.

items(_/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.items "Link to this definition")

Return a set-like object providing a view on the dict’s items.

keys(_/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.keys "Link to this definition")

Return a set-like object providing a view on the dict’s keys.

pop(_key_, _default\=<unrepresentable>_, _/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.pop "Link to this definition")

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem(_/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.popitem "Link to this definition")

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault(_key_, _default\=None_, _/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.setdefault "Link to this definition")

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update(\[_E_, \]_\*\*F_) → None.  Update D from mapping/iterable E and F.[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.update "Link to this definition")

If E is present and has a .keys() method, then does: for k in E.keys(): D\[k\] = E\[k\] If E is present and lacks a .keys() method, then does: for k, v in E: D\[k\] = v In either case, this is followed by: for k in F: D\[k\] = F\[k\]

values(_/_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch.values "Link to this definition")

Return an object providing a view on the dict’s values.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_distribution_modeling_thumb.png)

[Species distribution modeling](https://scikit-learn.org/stable/auto_examples/applications/plot_species_distribution_modeling.html)

Species distribution modeling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)