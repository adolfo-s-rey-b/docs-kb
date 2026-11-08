[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.calibration.calibration_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.calibration.calibration_curve.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.calibration.calibration_curve.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.calibration.calibration_curve.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.calibration.calibration_curve.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.calibration.calibration_curve.html)

Collapse Sidebar Expand Sidebar

calibration\_curve[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#calibration-curve "Link to this heading")

=============================================================================================================================================================

sklearn.calibration.calibration\_curve(_y\_true_, _y\_prob_, _\*_, _pos\_label\=None_, _n\_bins\=5_, _strategy\='uniform'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/calibration.py#L1217)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "Link to this definition")

Compute true and predicted probabilities for a calibration curve.

The method assumes the inputs come from a binary classifier, and discretize the \[0, 1\] interval into bins.

Calibration curves may also be referred to as reliability diagrams.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/calibration.html#calibration)
.

Parameters:

**y\_true**array-like of shape (n\_samples,)

True targets.

**y\_prob**array-like of shape (n\_samples,)

Probabilities of the positive class.

**pos\_label**int, float, bool or str, default=None

The label of the positive class.

Added in version 1.1.

**n\_bins**int, default=5

Number of bins to discretize the \[0, 1\] interval. A bigger number requires more data. Bins with no samples (i.e. without corresponding values in `y_prob`) will not be returned, thus the returned arrays may have less than `n_bins` values.

**strategy**{‘uniform’, ‘quantile’}, default=’uniform’

Strategy used to define the widths of the bins.

uniform

The bins have identical widths.

quantile

The bins have the same number of samples and depend on `y_prob`.

Returns:

**prob\_true**ndarray of shape (n\_bins,) or smaller

The proportion of samples whose class is the positive class, in each bin (fraction of positives).

**prob\_pred**ndarray of shape (n\_bins,) or smaller

The mean predicted probability in each bin.

See also

[`CalibrationDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")

Plot calibration curve using true and predicted labels.

[`CalibrationDisplay.from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_estimator "sklearn.calibration.CalibrationDisplay.from_estimator")

Plot calibration curve using an estimator and data.

References

Alexandru Niculescu-Mizil and Rich Caruana (2005) Predicting Good Probabilities With Supervised Learning, in Proceedings of the 22nd International Conference on Machine Learning (ICML). See section 4 (Qualitative Analysis of Predictions).

Examples

\>>> import numpy as np
\>>> from sklearn.calibration import calibration\_curve
\>>> y\_true \= np.array(\[0, 0, 0, 0, 1, 1, 1, 1, 1\])
\>>> y\_pred \= np.array(\[0.1, 0.2, 0.3, 0.4, 0.65, 0.7, 0.8, 0.9,  1.\])
\>>> prob\_true, prob\_pred \= calibration\_curve(y\_true, y\_pred, n\_bins\=3)
\>>> prob\_true
array(\[0. , 0.5, 1. \])
\>>> prob\_pred
array(\[0.2  , 0.525, 0.85 \])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)