[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_wine.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_wine.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_wine.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_wine.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_wine.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_wine.html)

Collapse Sidebar Expand Sidebar

load\_wine[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#load-wine "Link to this heading")

==================================================================================================================================

sklearn.datasets.load\_wine(_\*_, _return\_X\_y\=False_, _as\_frame\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L492)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "Link to this definition")

Load and return the wine dataset (classification).

Added in version 0.18.

The wine dataset is a classic and very easy multi-class classification dataset.

|     |     |
| --- | --- |
| Classes | 3   |
| Samples per class | \[59,71,48\] |
| Samples total | 178 |
| Dimensionality | 13  |
| Features | real, positive |

The copy of UCI ML Wine Data Set dataset is downloaded and modified to fit standard format from: [https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-dataset)
.

Parameters:

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a Bunch object. See below for more information about the `data` and `target` objects.

**as\_frame**bool, default=False

If True, the data is a pandas DataFrame including columns with appropriate dtypes (numeric). The target is a pandas DataFrame or Series depending on the number of target columns. If `return_X_y` is True, then (`data`, `target`) will be pandas DataFrames or Series as described below.

Added in version 0.23.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data{ndarray, dataframe} of shape (178, 13)

The data matrix. If `as_frame=True`, `data` will be a pandas DataFrame.

target: {ndarray, Series} of shape (178,)

The classification target. If `as_frame=True`, `target` will be a pandas Series.

feature\_names: list

The names of the dataset columns.

target\_names: list

The names of target classes.

frame: DataFrame of shape (178, 14)

Only present when `as_frame=True`. DataFrame with `data` and `target`.

Added in version 0.23.

DESCR: str

The full description of the dataset.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarrays. The first contains a 2D array of shape (178, 13) with each row representing one sample and the columns representing the features. The second array of shape (178,) contains the target samples. If `as_frame=True`, both arrays are pandas objects, i.e. `X` a dataframe and `y` a series.

Examples

Let’s say you are interested in the samples 10, 80, and 140, and want to know their class name.

\>>> from sklearn.datasets import load\_wine
\>>> data \= load\_wine()
\>>> data.target\[\[10, 80, 140\]\]
array(\[0, 1, 2\])
\>>> list(data.target\_names)
\[np.str\_('class\_0'), np.str\_('class\_1'), np.str\_('class\_2')\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_wine_thumb.png)

[Outlier detection on a real data set](https://scikit-learn.org/stable/auto_examples/applications/plot_outlier_detection_wine.html)

Outlier detection on a real data set

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_thumb.png)

[ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

ROC Curve with Visualization API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)