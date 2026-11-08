[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_voting_decision_regions.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_voting_decision_regions.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_voting_decision_regions.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_voting_decision_regions.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_voting_decision_regions.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_voting_decision_regions.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html#sphx-glr-download-auto-examples-ensemble-plot-voting-decision-regions-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Visualizing the probabilistic predictions of a VotingClassifier[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html#visualizing-the-probabilistic-predictions-of-a-votingclassifier "Link to this heading")

====================================================================================================================================================================================================================================================

Plot the predicted class probabilities in a toy dataset predicted by three different classifiers and averaged by the [`VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
.

First, three linear classifiers are initialized. Two are spline models with interaction terms, one using constant extrapolation and the other using periodic extrapolation. The third classifier is a [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 with the default “rbf” kernel.

In the first part of this example, these three classifiers are used to demonstrate soft-voting using [`VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
 with weighted average. We set `weights=[2, 1, 3]`, meaning the constant extrapolation spline model’s predictions are weighted twice as much as the periodic spline model’s, and the Nystroem model’s predictions are weighted three times as much as the periodic spline.

The second part demonstrates how soft predictions can be converted into hard predictions.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

We first generate a noisy XOR dataset, which is a binary classification task.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import [ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")

n\_samples \= 500
rng \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(0)
feature\_names \= \["Feature #0", "Feature #1"\]
common\_scatter\_plot\_params \= dict(
    cmap\=[ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["tab:red", "tab:blue"\]),
    edgecolor\="white",
    linewidth\=1,
)

xor \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0).uniform(low\=-1, high\=1, size\=(n\_samples, 2)),
    columns\=feature\_names,
)
noise \= rng.normal(loc\=0, scale\=0.1, size\=(n\_samples, 2))
target\_xor \= [np.logical\_xor](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")
(
    xor\["Feature #0"\] + noise\[:, 0\] \> 0, xor\["Feature #1"\] + noise\[:, 1\] \> 0
)

X \= xor\[feature\_names\]
y \= target\_xor.astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.scatter(X\["Feature #0"\], X\["Feature #1"\], c\=y, \*\*common\_scatter\_plot\_params)
ax.set\_title("The XOR dataset")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![The XOR dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_001.png)

Due to the inherent non-linear separability of the XOR dataset, tree-based models would often be preferred. However, appropriate feature engineering combined with a linear model can yield effective results, with the added benefit of producing better-calibrated probabilities for samples located in the transition regions affected by noise.

We define and fit the models on the whole dataset.

from sklearn.ensemble import [VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
, [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

clf1 \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(degree\=2, n\_knots\=2),
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(interaction\_only\=True),
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=10),
)
clf2 \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(
        degree\=2,
        n\_knots\=4,
        extrapolation\="periodic",
        include\_bias\=True,
    ),
    [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(interaction\_only\=True),
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=10),
)
clf3 \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
(gamma\=2, random\_state\=0),
    [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=10),
)
weights \= \[2, 1, 3\]
eclf \= [VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
(
    estimators\=\[\
        ("constant splines model", clf1),\
        ("periodic splines model", clf2),\
        ("nystroem model", clf3),\
    \],
    voting\="soft",
    weights\=weights,
)

clf1.fit(X, y)
clf2.fit(X, y)
clf3.fit(X, y)
eclf.fit(X, y)

Copy to clipboard

VotingClassifier(estimators=\[('constant splines model',\
                              Pipeline(steps=\[('splinetransformer',\
                                               SplineTransformer(degree=2,\
                                                                 n\_knots=2)),\
                                              ('polynomialfeatures',\
                                               PolynomialFeatures(interaction\_only=True)),\
                                              ('logisticregression',\
                                               LogisticRegression(C=10))\])),\
                             ('periodic splines model',\
                              Pipeline(steps=\[('splinetransformer',\
                                               SplineTransformer(degree=2,\
                                                                 extrapolation='periodic',\
                                                                 n\_knots=4)),\
                                              ('polynomialfeatures',\
                                               PolynomialFeatures(interaction\_only=True)),\
                                              ('logisticregression',\
                                               LogisticRegression(C=10))\])),\
                             ('nystroem model',\
                              Pipeline(steps=\[('standardscaler',\
                                               StandardScaler()),\
                                              ('nystroem',\
                                               Nystroem(gamma=2,\
                                                        random\_state=0)),\
                                              ('logisticregression',\
                                               LogisticRegression(C=10))\]))\],
                 voting='soft', weights=\[2, 1, 3\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

VotingClassifier

[?Documentation for VotingClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimators estimators: list of (str, estimator) tuples  <br>  <br>Invoking the \`\`fit\`\` method on the \`\`VotingClassifier\`\` will fit clones  <br>of those original estimators that will be stored in the class attribute  <br>\`\`self.estimators\_\`\`. An estimator can be set to \`\`'drop'\`\` using  <br>:meth:\`set\_params\`.  <br>  <br>.. versionchanged:: 0.21  <br>\`\`'drop'\`\` is accepted. Using None was deprecated in 0.22 and  <br>support was removed in 0.24.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=estimators,-list%20of%20%28str%2C%20estimator%29%20tuples) | \[('constant splines model', ...), ('periodic splines model', ...), ...\] |
|     | [voting voting: {'hard', 'soft'}, default='hard'  <br>  <br>If 'hard', uses predicted class labels for majority rule voting.  <br>Else if 'soft', predicts the class label based on the argmax of  <br>the sums of the predicted probabilities, which is recommended for  <br>an ensemble of well-calibrated classifiers.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=voting,-%7B%27hard%27%2C%20%27soft%27%7D%2C%20default%3D%27hard%27) | 'soft' |
|     | [weights weights: array-like of shape (n\_classifiers,), default=None  <br>  <br>Sequence of weights (\`float\` or \`int\`) to weight the occurrences of  <br>predicted class labels (\`hard\` voting) or class probabilities  <br>before averaging (\`soft\` voting). Uses uniform weights if \`None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=weights,-array-like%20of%20shape%20%28n_classifiers%2C%29%2C%20default%3DNone) | \[2, 1, ...\] |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel for \`\`fit\`\`.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [flatten\_transform flatten\_transform: bool, default=True  <br>  <br>Affects shape of transform output only when voting='soft'  <br>If voting='soft' and flatten\_transform=True, transform method returns  <br>matrix with shape (n\_samples, n\_classifiers \* n\_classes). If  <br>flatten\_transform=False, it returns  <br>(n\_classifiers, n\_samples, n\_classes).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=flatten_transform,-bool%2C%20default%3DTrue) | True |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting will be printed as it  <br>is completed.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int32\](2,) | \[0,1\] |
| [estimators\_ estimators\_: list of classifiers  <br>  <br>The collection of fitted sub-estimators as defined in \`\`estimators\`\`  <br>that are not 'drop'. Note that sub-estimators are always fitted on  <br>integer-encoded labels (see \`\`le\_\`\` attribute). When \`\`y\`\` contains  <br>non-integer class labels (e.g. strings), use \`\`le\_.inverse\_transform\`\`  <br>to map predictions back to the original label space.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=estimators_,-list%20of%20classifiers) | list | \[Pipeline(step...ssion(C=10))\]), Pipeline(step...ssion(C=10))\]), Pipeline(step...ssion(C=10))\])\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimators expose such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['Feature #0','Feature #1'\] |
| [le\_ le\_: :class:\`~sklearn.preprocessing.LabelEncoder\`  <br>  <br>Transformer used to encode the labels during fit and decode during  <br>prediction. Sub-estimators in \`\`estimators\_\`\` are fitted on the  <br>integer-encoded labels produced by this encoder.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=le_,-%3Aclass%3A~sklearn.preprocessing.LabelEncoder) | LabelEncoder | LabelEncoder() |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying classifier exposes such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=n_features_in_,-int) | int | 2   |
| [named\_estimators\_ named\_estimators\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Attribute to access any fitted sub-estimators by name.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.VotingClassifier.html#:~:text=named_estimators_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'constant sp...sion(C=10))\])} |

constant splines model

SplineTransformer

[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 2   |
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 2   |
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | 'uniform' |
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'constant' |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1d94d3da30>, <scipy.interp...x7e1d94d3c3b0>\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['Feature #0','Feature #1'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 6   |

6 features

|     |
| --- |
| Feature #0\_sp\_0 |
| Feature #0\_sp\_1 |
| Feature #0\_sp\_2 |
| Feature #1\_sp\_0 |
| Feature #1\_sp\_1 |
| Feature #1\_sp\_2 |

PolynomialFeatures

[?Documentation for PolynomialFeatures](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [interaction\_only interaction\_only: bool, default=False  <br>  <br>If \`True\`, only interaction features are produced: features that are  <br>products of at most \`degree\` \*distinct\* input features, i.e. terms with  <br>power of 2 or higher of the same input feature are excluded:  <br>  <br>\- included: \`x\[0\]\`, \`x\[1\]\`, \`x\[0\] \* x\[1\]\`, etc.  <br>\- excluded: \`x\[0\] \*\* 2\`, \`x\[0\] \*\* 2 \* x\[1\]\`, etc.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=interaction_only,-bool%2C%20default%3DFalse) | True |
|     | [degree degree: int or tuple (min\_degree, max\_degree), default=2  <br>  <br>If a single int is given, it specifies the maximal degree of the  <br>polynomial features. If a tuple \`(min\_degree, max\_degree)\` is passed,  <br>then \`min\_degree\` is the minimum and \`max\_degree\` is the maximum  <br>polynomial degree of the generated features. Note that \`min\_degree=0\`  <br>and \`min\_degree=1\` are equivalent as outputting the degree zero term is  <br>determined by \`include\_bias\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=degree,-int%20or%20tuple%20%28min_degree%2C%20max_degree%29%2C%20default%3D2) | 2   |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If \`True\` (default), then include a bias column, the feature in which  <br>all polynomial powers are zero (i.e. a column of ones - acts as an  <br>intercept term in a linear model).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to  <br>compute, but may slow down subsequent estimators.  <br>  <br>.. versionadded:: 0.21](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=n_features_in_,-int) | int | 6   |
| [n\_output\_features\_ n\_output\_features\_: int  <br>  <br>The total number of polynomial output features. The number of output  <br>features is computed by iterating over all suitably sized combinations  <br>of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=n_output_features_,-int) | int | 22  |
| [powers\_ powers\_: ndarray of shape (\`n\_output\_features\_\`, \`n\_features\_in\_\`)  <br>  <br>\`powers\_\[i, j\]\` is the exponent of the jth input in the ith output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=powers_,-ndarray%20of%20shape%20%28n_output_features_%2C%20n_features_in_%29) | ndarray\[int64\](22, 6) | \[\[0,0,0,0,0,0\], \[1,0,0,0,0,0\], \[0,1,0,0,0,0\], ..., \[0,0,0,1,1,0\], \[0,0,0,1,0,1\], \[0,0,0,0,1,1\]\] |

22 features

|     |
| --- |
| 1   |
| x0  |
| x1  |
| x2  |
| x3  |
| x4  |
| x5  |
| x0 x1 |
| x0 x2 |
| x0 x3 |
| x0 x4 |
| x0 x5 |
| x1 x2 |
| x1 x3 |
| x1 x4 |
| x1 x5 |
| x2 x3 |
| x2 x4 |
| x2 x5 |
| x3 x4 |
| x3 x5 |
| x4 x5 |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 10  |
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int32\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 22) | \[\[ 0.07,-0.36, 0.71,...,-0.73, 0.03, 0.64\]\] |
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[0.12\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 22  |
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[16\] |

periodic splines model

SplineTransformer

[?Documentation for SplineTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_knots n\_knots: int, default=5  <br>  <br>Number of knots of the splines if \`knots\` equals one of  <br>{'uniform', 'quantile'}. Must be larger or equal 2. Ignored if \`knots\`  <br>is array-like.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_knots,-int%2C%20default%3D5) | 4   |
|     | [degree degree: int, default=3  <br>  <br>The polynomial degree of the spline basis. Must be a non-negative  <br>integer.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=degree,-int%2C%20default%3D3) | 2   |
|     | [extrapolation extrapolation: {'error', 'constant', 'linear', 'continue', 'periodic'}, default='constant'  <br>  <br>If 'error', values outside the min and max values of the training  <br>features raises a \`ValueError\`. If 'constant', the value of the  <br>splines at minimum and maximum value of the features is used as  <br>constant extrapolation. If 'linear', a linear extrapolation is used.  <br>If 'continue', the splines are extrapolated as is, i.e. option  <br>\`extrapolate=True\` in :class:\`scipy.interpolate.BSpline\`. If  <br>'periodic', periodic splines with a periodicity equal to the distance  <br>between the first and last knot are used. Periodic splines enforce  <br>equal function values and derivatives at the first and last knot.  <br>For example, this makes it possible to avoid introducing an arbitrary  <br>jump between Dec 31st and Jan 1st in spline features derived from a  <br>naturally periodic "day-of-year" input feature. In this case it is  <br>recommended to manually set the knot values to control the period.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=extrapolation,-%7B%27error%27%2C%20%27constant%27%2C%20%27linear%27%2C%20%27continue%27%2C%20%27periodic%27%7D%2C%20%20%20%20%20%20%20%20%20default%3D%27constant%27) | 'periodic' |
|     | [knots knots: {'uniform', 'quantile'} or array-like of shape (n\_knots, n\_features), default='uniform'  <br>  <br>Set knot positions such that first knot <= features <= last knot.  <br>  <br>\- If 'uniform', \`n\_knots\` number of knots are distributed uniformly  <br>from min to max values of the features.  <br>\- If 'quantile', they are distributed uniformly along the quantiles of  <br>the features.  <br>\- If an array-like is given, it directly specifies the sorted knot  <br>positions including the boundary knots. Note that, internally,  <br>\`degree\` number of knots are added before the first knot, the same  <br>after the last knot.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=knots,-int%2C%20default%3D5) | 'uniform' |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If False, then the last spline element inside the data range  <br>of a feature is dropped. As B-splines sum to one over the spline basis  <br>functions for each data point, they implicitly include a bias term,  <br>i.e. a column of ones. It acts as an intercept term in a linear models.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to compute, but  <br>may slow down subsequent estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |
|     | [handle\_missing handle\_missing: {'error', 'zeros'}, default='error'  <br>  <br>Specifies the way missing values are handled.  <br>  <br>\- 'error' : Raise an error if \`np.nan\` values are present during :meth:\`fit\`.  <br>\- 'zeros' : Encode splines of missing values with values \`0\`.  <br>  <br>Note that \`handle\_missing='zeros'\` differs from first imputing missing values  <br>with zeros and then creating the spline basis. The latter creates spline basis  <br>functions which have non-zero values at the missing values  <br>whereas this option simply sets all spline basis function values to zero at the  <br>missing values.  <br>  <br>.. versionadded:: 1.8](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=handle_missing,-%7B%27error%27%2C%20%27zeros%27%7D%2C%20default%3D%27error%27) | 'error' |
|     | [sparse\_output sparse\_output: bool, default=False  <br>  <br>Will return sparse CSR matrix if set True else will return an array.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=sparse_output,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [bsplines\_ bsplines\_: list of shape (n\_features,)  <br>  <br>List of BSplines objects, one for each feature.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=bsplines_,-list%20of%20shape%20%28n_features%2C%29) | list | \[<scipy.interp...x7e1d94d3c230>, <scipy.interp...x7e1d94d3dbb0>\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['Feature #0','Feature #1'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>The total number of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_features\_out\_ n\_features\_out\_: int  <br>  <br>The total number of output features, which is computed as  <br>\`n\_features \* n\_splines\`, where \`n\_splines\` is  <br>the number of bases elements of the B-splines,  <br>\`n\_knots + degree - 1\` for non-periodic splines and  <br>\`n\_knots - 1\` for periodic ones.  <br>If \`include\_bias=False\`, then it is only  <br>\`n\_features \* (n\_splines - 1)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.SplineTransformer.html#:~:text=n_features_out_,-int) | int | 6   |

6 features

|     |
| --- |
| Feature #0\_sp\_0 |
| Feature #0\_sp\_1 |
| Feature #0\_sp\_2 |
| Feature #1\_sp\_0 |
| Feature #1\_sp\_1 |
| Feature #1\_sp\_2 |

PolynomialFeatures

[?Documentation for PolynomialFeatures](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [interaction\_only interaction\_only: bool, default=False  <br>  <br>If \`True\`, only interaction features are produced: features that are  <br>products of at most \`degree\` \*distinct\* input features, i.e. terms with  <br>power of 2 or higher of the same input feature are excluded:  <br>  <br>\- included: \`x\[0\]\`, \`x\[1\]\`, \`x\[0\] \* x\[1\]\`, etc.  <br>\- excluded: \`x\[0\] \*\* 2\`, \`x\[0\] \*\* 2 \* x\[1\]\`, etc.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=interaction_only,-bool%2C%20default%3DFalse) | True |
|     | [degree degree: int or tuple (min\_degree, max\_degree), default=2  <br>  <br>If a single int is given, it specifies the maximal degree of the  <br>polynomial features. If a tuple \`(min\_degree, max\_degree)\` is passed,  <br>then \`min\_degree\` is the minimum and \`max\_degree\` is the maximum  <br>polynomial degree of the generated features. Note that \`min\_degree=0\`  <br>and \`min\_degree=1\` are equivalent as outputting the degree zero term is  <br>determined by \`include\_bias\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=degree,-int%20or%20tuple%20%28min_degree%2C%20max_degree%29%2C%20default%3D2) | 2   |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If \`True\` (default), then include a bias column, the feature in which  <br>all polynomial powers are zero (i.e. a column of ones - acts as an  <br>intercept term in a linear model).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to  <br>compute, but may slow down subsequent estimators.  <br>  <br>.. versionadded:: 0.21](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=n_features_in_,-int) | int | 6   |
| [n\_output\_features\_ n\_output\_features\_: int  <br>  <br>The total number of polynomial output features. The number of output  <br>features is computed by iterating over all suitably sized combinations  <br>of input features.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=n_output_features_,-int) | int | 22  |
| [powers\_ powers\_: ndarray of shape (\`n\_output\_features\_\`, \`n\_features\_in\_\`)  <br>  <br>\`powers\_\[i, j\]\` is the exponent of the jth input in the ith output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=powers_,-ndarray%20of%20shape%20%28n_output_features_%2C%20n_features_in_%29) | ndarray\[int64\](22, 6) | \[\[0,0,0,0,0,0\], \[1,0,0,0,0,0\], \[0,1,0,0,0,0\], ..., \[0,0,0,1,1,0\], \[0,0,0,1,0,1\], \[0,0,0,0,1,1\]\] |

22 features

|     |
| --- |
| 1   |
| x0  |
| x1  |
| x2  |
| x3  |
| x4  |
| x5  |
| x0 x1 |
| x0 x2 |
| x0 x3 |
| x0 x4 |
| x0 x5 |
| x1 x2 |
| x1 x3 |
| x1 x4 |
| x1 x5 |
| x2 x3 |
| x2 x4 |
| x2 x5 |
| x3 x4 |
| x3 x5 |
| x4 x5 |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 10  |
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int32\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 22) | \[\[-0.01,-0.2 ,-0.54,..., 0.91, 2.07,-2.42\]\] |
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 22  |
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[22\] |

nystroem model

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['Feature #0','Feature #1'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[ 0.01,-0.02\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 500 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[0.57,0.59\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[0.33,0.35\] |

2 features

|     |
| --- |
| Feature #0 |
| Feature #1 |

Nystroem

[?Documentation for Nystroem](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [gamma gamma: float, default=None  <br>  <br>Gamma parameter for the RBF, laplacian, polynomial, exponential chi2  <br>and sigmoid kernels. Interpretation of the default value is left to  <br>the kernel; see the documentation for sklearn.metrics.pairwise.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=gamma,-float%2C%20default%3DNone) | 2   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the uniform sampling without  <br>replacement of \`n\_components\` of the training data to construct the  <br>basis kernel.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [kernel kernel: str or callable, default='rbf'  <br>  <br>Kernel map to be approximated. A callable should accept two arguments  <br>and the keyword arguments passed to this object as \`kernel\_params\`, and  <br>should return a floating point number.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel,-str%20or%20callable%2C%20default%3D%27rbf%27) | 'rbf' |
|     | [coef0 coef0: float, default=None  <br>  <br>Zero coefficient for polynomial and sigmoid kernels.  <br>Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=coef0,-float%2C%20default%3DNone) | None |
|     | [degree degree: float, default=None  <br>  <br>Degree of the polynomial kernel. Ignored by other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=degree,-float%2C%20default%3DNone) | None |
|     | [kernel\_params kernel\_params: dict, default=None  <br>  <br>Additional parameters (keyword arguments) for kernel function passed  <br>as callable object.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=kernel_params,-dict%2C%20default%3DNone) | None |
|     | [n\_components n\_components: int, default=100  <br>  <br>Number of features to construct.  <br>How many data points will be used to construct the mapping.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_components,-int%2C%20default%3D100) | 100 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to use for the computation. This works by breaking  <br>down the kernel matrix into \`n\_jobs\` even slices and computing them in  <br>parallel.  <br>  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [component\_indices\_ component\_indices\_: ndarray of shape (n\_components)  <br>  <br>Indices of \`\`components\_\`\` in the training set.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=component_indices_,-ndarray%20of%20shape%20%28n_components%29) | ndarray\[int64\](100,) | \[ 90,254,283,...,440, 60,208\] |
| [components\_ components\_: ndarray of shape (n\_components, n\_features)  <br>  <br>Subset of training points used to construct the feature map.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=components_,-ndarray%20of%20shape%20%28n_components%2C%20n_features%29) | ndarray\[float64\](100, 2) | \[\[-1.18, 0.45\], \[-0.87,-0.15\], \[ 0.13, 1.48\], ..., \[ 0.78,-0.68\], \[ 0.77, 0.04\], \[-1.3 ,-1.62\]\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=n_features_in_,-int) | int | 2   |
| [normalization\_ normalization\_: ndarray of shape (n\_components, n\_components)  <br>  <br>Normalization matrix needed for embedding.  <br>Square root of the kernel matrix on \`\`components\_\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.kernel_approximation.Nystroem.html#:~:text=normalization_,-ndarray%20of%20shape%20%28n_components%2C%20n_components%29) | ndarray\[float64\](100, 100) | \[\[1179.99, 29.85, 6.59,..., 2.13, -0.24, -0.02\], \[ 29.85, 31.15, -0.73,..., 0.64, -1.17, 0.04\], \[ 6.59, -0.73, 31.71,..., 0.49, -2.09, 0.02\], ..., \[ 2.13, 0.64, 0.49,..., 12.36, -3.56, 0.02\], \[ -0.24, -1.17, -2.09,..., -3.56, 31.67, 0. \], \[ -0.02, 0.04, 0.02,..., 0.02, 0. , 8.87\]\] |

100 features

|     |
| --- |
| nystroem0 |
| nystroem1 |
| nystroem2 |
| nystroem3 |
| nystroem4 |
| nystroem5 |
| nystroem6 |
| nystroem7 |
| nystroem8 |
| nystroem9 |
| nystroem10 |
| nystroem11 |
| nystroem12 |
| nystroem13 |
| nystroem14 |
| nystroem15 |
| nystroem16 |
| nystroem17 |
| nystroem18 |
| nystroem19 |
| nystroem20 |
| nystroem21 |
| nystroem22 |
| nystroem23 |
| nystroem24 |
| nystroem25 |
| nystroem26 |
| nystroem27 |
| nystroem28 |
| nystroem29 |
| nystroem30 |
| nystroem31 |
| nystroem32 |
| nystroem33 |
| nystroem34 |
| nystroem35 |
| nystroem36 |
| nystroem37 |
| nystroem38 |
| nystroem39 |
| nystroem40 |
| nystroem41 |
| nystroem42 |
| nystroem43 |
| nystroem44 |
| nystroem45 |
| nystroem46 |
| nystroem47 |
| nystroem48 |
| nystroem49 |
| nystroem50 |
| nystroem51 |
| nystroem52 |
| nystroem53 |
| nystroem54 |
| nystroem55 |
| nystroem56 |
| nystroem57 |
| nystroem58 |
| nystroem59 |
| nystroem60 |
| nystroem61 |
| nystroem62 |
| nystroem63 |
| nystroem64 |
| nystroem65 |
| nystroem66 |
| nystroem67 |
| nystroem68 |
| nystroem69 |
| nystroem70 |
| nystroem71 |
| nystroem72 |
| nystroem73 |
| nystroem74 |
| nystroem75 |
| nystroem76 |
| nystroem77 |
| nystroem78 |
| nystroem79 |
| nystroem80 |
| nystroem81 |
| nystroem82 |
| nystroem83 |
| nystroem84 |
| nystroem85 |
| nystroem86 |
| nystroem87 |
| nystroem88 |
| nystroem89 |
| nystroem90 |
| nystroem91 |
| nystroem92 |
| nystroem93 |
| nystroem94 |
| nystroem95 |
| nystroem96 |
| nystroem97 |
| nystroem98 |
| nystroem99 |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 10  |
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int32\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 100) | \[\[ 1.09,-1.54,-0.87,..., 1.69,-0.69,-1.07\]\] |
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[0.23\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 100 |
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[17\] |

6 features

|     |
| --- |
| votingclassifier\_constant splines model0 |
| votingclassifier\_constant splines model1 |
| votingclassifier\_periodic splines model0 |
| votingclassifier\_periodic splines model1 |
| votingclassifier\_nystroem model0 |
| votingclassifier\_nystroem model1 |

  
  

Finally we use [`DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
 to plot the predicted probabilities. By using a diverging colormap (such as `"RdBu"`), we can ensure that darker colors correspond to `predict_proba` close to either 0 or 1, and white corresponds to `predict_proba` of 0.5.

from itertools import [product](https://docs.python.org/3/library/itertools.html#itertools.product "itertools.product")

from sklearn.inspection import DecisionBoundaryDisplay

fig, axarr \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, sharex\="col", sharey\="row", figsize\=(10, 8))
for idx, clf, title in zip(
    [product](https://docs.python.org/3/library/itertools.html#itertools.product "itertools.product")
(\[0, 1\], \[0, 1\]),
    \[clf1, clf2, clf3, eclf\],
    \[\
        "Splines with\\nconstant extrapolation",\
        "Splines with\\nperiodic extrapolation",\
        "RBF Nystroem",\
        "Soft Voting",\
    \],
):
    disp \= [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X,
        response\_method\="predict\_proba",
        plot\_method\="pcolormesh",
        cmap\="RdBu",
        alpha\=0.8,
        ax\=axarr\[idx\[0\], idx\[1\]\],
    )
    axarr\[idx\[0\], idx\[1\]\].scatter(
        X\["Feature #0"\],
        X\["Feature #1"\],
        c\=y,
        \*\*common\_scatter\_plot\_params,
    )
    axarr\[idx\[0\], idx\[1\]\].set\_title(title)
    fig.colorbar(disp.surface\_, ax\=axarr\[idx\[0\], idx\[1\]\], label\="Probability estimate")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Splines with constant extrapolation, Splines with periodic extrapolation, RBF Nystroem, Soft Voting](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_002.png)

As a sanity check, we can verify for a given sample that the probability predicted by the [`VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
 is indeed the weighted average of the individual classifiers’ soft-predictions.

In the case of binary classification such as in the present example, the [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 arrays contain the probability of belonging to class 0 (here in red) as the first entry, and the probability of belonging to class 1 (here in blue) as the second entry.

test\_sample \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
({"Feature #0": \[\-0.5\], "Feature #1": \[1.5\]})
predict\_probas \= \[est.predict\_proba(test\_sample).ravel() for est in eclf.estimators\_\]
for (est\_name, \_), est\_probas in zip(eclf.estimators, predict\_probas):
    print(f"{est\_name}'s predicted probabilities: {est\_probas}")

Copy to clipboard

constant splines model's predicted probabilities: \[0.11272662 0.88727338\]
periodic splines model's predicted probabilities: \[0.99726573 0.00273427\]
nystroem model's predicted probabilities: \[0.3185838 0.6814162\]

Copy to clipboard

print(
    "Weighted average of soft-predictions: "
    f"{[np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(weights, predict\_probas) / [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(weights)}"
)

Copy to clipboard

Weighted average of soft-predictions: \[0.3630784 0.6369216\]

Copy to clipboard

We can see that manual calculation of predicted probabilities above is equivalent to that produced by the `VotingClassifier`:

print(
    "Predicted probability of VotingClassifier: "
    f"{eclf.predict\_proba(test\_sample).ravel()}"
)

Copy to clipboard

Predicted probability of VotingClassifier: \[0.3630784 0.6369216\]

Copy to clipboard

To convert soft predictions into hard predictions when weights are provided, the weighted average predicted probabilities are computed for each class. Then, the final class label is then derived from the class label with the highest average probability, which corresponds to the default threshold at `predict_proba=0.5` in the case of binary classification.

print(
    "Class with the highest weighted average of soft-predictions: "
    f"{[np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax")
([np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(weights, predict\_probas) / [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(weights))}"
)

Copy to clipboard

Class with the highest weighted average of soft-predictions: 1

Copy to clipboard

This is equivalent to the output of `VotingClassifier`’s `predict` method:

print(f"Predicted class of VotingClassifier: {eclf.predict(test\_sample).ravel()}")

Copy to clipboard

Predicted class of VotingClassifier: \[1\]

Copy to clipboard

Soft votes can be thresholded as for any other probabilistic classifier. This allows you to set a threshold probability at which the positive class will be predicted, instead of simply selecting the class with the highest predicted probability.

from sklearn.model\_selection import [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")

eclf\_other\_threshold \= [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
(
    eclf, threshold\=0.7, response\_method\="predict\_proba"
).fit(X, y)
print(
    "Predicted class of thresholded VotingClassifier: "
    f"{eclf\_other\_threshold.predict(test\_sample)}"
)

Copy to clipboard

Predicted class of thresholded VotingClassifier: \[0\]

Copy to clipboard

**Total running time of the script:** (0 minutes 0.755 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_voting_decision_regions.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_voting_decision_regions.ipynb)

[`Download Jupyter notebook: plot_voting_decision_regions.ipynb`](https://scikit-learn.org/stable/_downloads/905bd7d135e7fe5fdec55e4f0aa77420/plot_voting_decision_regions.ipynb)

[`Download Python source code: plot_voting_decision_regions.py`](https://scikit-learn.org/stable/_downloads/12b6dbb270865986bd1c9bbf7ce24cb0/plot_voting_decision_regions.py)

[`Download zipped: plot_voting_decision_regions.zip`](https://scikit-learn.org/stable/_downloads/04b9a7769df5b331f4d94e1d065b4311/plot_voting_decision_regions.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_thumb.png)

[Polynomial and Spline interpolation](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)

Polynomial and Spline interpolation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_calibration_thumb.png)

[Comparison of Calibration of Classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_compare_calibration.html)

Comparison of Calibration of Classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_frozen_examples_thumb.png)

[Examples of Using FrozenEstimator](https://scikit-learn.org/stable/auto_examples/frozen/plot_frozen_examples.html)

Examples of Using FrozenEstimator

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/12b6dbb270865986bd1c9bbf7ce24cb0/plot_voting_decision_regions.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/905bd7d135e7fe5fdec55e4f0aa77420/plot_voting_decision_regions.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/04b9a7769df5b331f4d94e1d065b4311/plot_voting_decision_regions.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_voting_decision_regions.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_voting_decision_regions.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)