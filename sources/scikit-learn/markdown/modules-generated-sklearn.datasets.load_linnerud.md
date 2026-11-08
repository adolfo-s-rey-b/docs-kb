[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_linnerud.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_linnerud.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_linnerud.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_linnerud.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_linnerud.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_linnerud.html)

Collapse Sidebar Expand Sidebar

load\_linnerud[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#load-linnerud "Link to this heading")

==============================================================================================================================================

sklearn.datasets.load\_linnerud(_\*_, _return\_X\_y\=False_, _as\_frame\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L1168)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud "Link to this definition")

Load and return the physical exercise Linnerud dataset.

This dataset is suitable for multi-output regression tasks.

|     |     |
| --- | --- |
| Samples total | 20  |
| Dimensionality | 3 (for both data and target) |
| Features | integer |
| Targets | integer |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset)
.

Parameters:

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a Bunch object. See below for more information about the `data` and `target` objects.

Added in version 0.18.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric, string or categorical). The target is a pandas DataFrame or Series depending on the number of target columns. If `return_X_y` is True, then (`data`, `target`) will be pandas DataFrames or Series as described below.

Added in version 0.23.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data{ndarray, dataframe} of shape (20, 3)

The data matrix. If `as_frame=True`, `data` will be a pandas DataFrame.

target: {ndarray, dataframe} of shape (20, 3)

The regression targets. If `as_frame=True`, `target` will be a pandas DataFrame.

feature\_names: list

The names of the dataset columns.

target\_names: list

The names of the target columns.

frame: DataFrame of shape (20, 6)

Only present when `as_frame=True`. DataFrame with `data` and `target`.

Added in version 0.23.

DESCR: str

The full description of the dataset.

data\_filename: str

The path to the location of the data.

target\_filename: str

The path to the location of the target.

Added in version 0.20.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarrays. The first contains a 2D ndarray of shape `(20, 3)` with each row representing one sample and the columns representing the features. The second ndarray of shape `(20, 3)` contains the multi target samples. If `as_frame=True`, both arrays are pandas dataframes.

Added in version 0.18.

Examples

\>>> from sklearn.datasets import load\_linnerud
\>>> linnerud \= load\_linnerud()
\>>> linnerud.data.shape
(20, 3)
\>>> linnerud.target.shape
(20, 3)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)