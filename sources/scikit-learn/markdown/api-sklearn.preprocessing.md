[Skip to main content](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.preprocessing.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.preprocessing.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.preprocessing.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.preprocessing.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.preprocessing.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.preprocessing.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.preprocessing.html)

Collapse Sidebar Expand Sidebar

sklearn.preprocessing[#](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "Link to this heading")

=============================================================================================================================================

Methods for scaling, centering, normalization, binarization, and more.

**User guide.** See the [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
 section for further details.

|     |     |
| --- | --- |
| [`Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer") | Binarize data (set feature values to 0 or 1) according to a threshold. |
| [`FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer") | Constructs a transformer from an arbitrary callable. |
| [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer") | Bin continuous data into intervals. |
| [`KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer") | Center an arbitrary kernel matrix K. |
| [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer") | Binarize labels in a one-vs-all fashion. |
| [`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder") | Encode target labels with value between 0 and n\_classes-1. |
| [`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler") | Scale each feature by its maximum absolute value. |
| [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler") | Transform features by scaling each feature to a given range. |
| [`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer") | Transform between iterable of iterables and a multilabel format. |
| [`Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer") | Normalize samples individually to unit norm. |
| [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder") | Encode categorical features as a one-hot numeric array. |
| [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder") | Encode categorical features as an integer array. |
| [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures") | Generate polynomial and interaction features. |
| [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer") | Apply a power transform featurewise to make data more Gaussian-like. |
| [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer") | Transform features using quantiles information. |
| [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler") | Scale features using statistics that are robust to outliers. |
| [`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer") | Generate univariate B-spline bases for features. |
| [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler") | Standardize features by removing the mean and scaling to unit variance. |
| [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder") | Target Encoder for regression and classification targets. |
| [`add_dummy_feature`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.add_dummy_feature.html#sklearn.preprocessing.add_dummy_feature "sklearn.preprocessing.add_dummy_feature") | Augment dataset with an additional dummy feature. |
| [`binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html#sklearn.preprocessing.binarize "sklearn.preprocessing.binarize") | Boolean thresholding of array-like or scipy.sparse matrix. |
| [`label_binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize") | Binarize labels in a one-vs-all fashion. |
| [`maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale") | Scale each feature to the \[-1, 1\] range without breaking the sparsity. |
| [`minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale") | Transform features by scaling each feature to a given range. |
| [`normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize") | Scale input vectors individually to unit norm (vector length). |
| [`power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform") | Parametric, monotonic transformation to make data more Gaussian-like. |
| [`quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform") | Transform features using quantiles information. |
| [`robust_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "sklearn.preprocessing.robust_scale") | Standardize a dataset along any axis. |
| [`scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale") | Standardize a dataset along any axis. |