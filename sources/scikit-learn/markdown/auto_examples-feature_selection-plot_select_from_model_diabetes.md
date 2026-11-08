[Skip to main content](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/feature_selection/plot_select_from_model_diabetes.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/feature_selection/plot_select_from_model_diabetes.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/feature_selection/plot_select_from_model_diabetes.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/feature_selection/plot_select_from_model_diabetes.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/feature_selection/plot_select_from_model_diabetes.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#sphx-glr-download-auto-examples-feature-selection-plot-select-from-model-diabetes-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Model-based and sequential feature selection[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#model-based-and-sequential-feature-selection "Link to this heading")

==========================================================================================================================================================================================================================

This example illustrates and compares two approaches for feature selection: [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 which is based on feature importance, and [`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
 which relies on a greedy approach.

We use the Diabetes dataset, which consists of 10 features collected from 442 diabetes patients.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading the data[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#loading-the-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

We first load the diabetes dataset which is available from within scikit-learn, and print its description:

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")

diabetes \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
()
X, y \= diabetes.data, diabetes.target
print(diabetes.DESCR)

Copy to clipboard

.. \_diabetes\_dataset:

Diabetes dataset
----------------

Ten baseline variables, age, sex, body mass index, average blood
pressure, and six blood serum measurements were obtained for each of n =
442 diabetes patients, as well as the response of interest, a
quantitative measure of disease progression one year after baseline.

\*\*Data Set Characteristics:\*\*

:Number of Instances: 442

:Number of Attributes: First 10 columns are numeric predictive values

:Target: Column 11 is a quantitative measure of disease progression one year after baseline

:Attribute Information:
    - age     age in years
    - sex
    - bmi     body mass index
    - bp      average blood pressure
    - s1      tc, total serum cholesterol
    - s2      ldl, low-density lipoproteins
    - s3      hdl, high-density lipoproteins
    - s4      tch, total cholesterol / HDL
    - s5      ltg, possibly log of serum triglycerides level
    - s6      glu, blood sugar level

Note: Each of these 10 feature variables have been mean centered and scaled by the standard deviation times the square root of \`n\_samples\` (i.e. the sum of squares of each column totals 1).

Source URL:
https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html

For more information see:
Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani (2004) "Least Angle Regression," Annals of Statistics (with discussion), 407-499.
(https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle\_2002.pdf)

Copy to clipboard

Feature importance from coefficients[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#feature-importance-from-coefficients "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To get an idea of the importance of the features, we are going to use the [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
 estimator. The features with the highest absolute `coef_` value are considered the most important. We can observe the coefficients directly without needing to scale them (or scale the data) because from the description above, we know that the features were already standardized. For a more complete example on the interpretations of the coefficients of linear models, you may refer to [Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#sphx-glr-auto-examples-inspection-plot-linear-model-coefficient-interpretation-py)
.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear\_model import [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")

ridge \= [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
(alphas\=[np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-6, 6, num\=5)).fit(X, y)
importance \= np.abs(ridge.coef\_)
feature\_names \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(diabetes.feature\_names)
[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(height\=importance, x\=feature\_names)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Feature importances via coefficients")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Feature importances via coefficients](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_001.png)

Selecting features based on importance[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#selecting-features-based-on-importance "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now we want to select the two features which are the most important according to the coefficients. The [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 is meant just for that. [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 accepts a `threshold` parameter and will select the features whose importance (defined by the coefficients) are above this threshold.

Since we want to select only 2 features, we will set this threshold slightly above the coefficient of third most important feature.

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn.feature\_selection import [SelectFromModel](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")

threshold \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(importance)\[\-3\] + 0.01

tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
sfm \= [SelectFromModel](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
(ridge, threshold\=threshold).fit(X, y)
toc \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
print(f"Features selected by SelectFromModel: {feature\_names\[sfm.get\_support()\]}")
print(f"Done in {toc \- tic:.3f}s")

Copy to clipboard

Features selected by SelectFromModel: \['s1' 's5'\]
Done in 0.002s

Copy to clipboard

Selecting features with Sequential Feature Selection[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#selecting-features-with-sequential-feature-selection "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another way of selecting features is to use [`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
 (SFS). SFS is a greedy procedure where, at each iteration, we choose the best new feature to add to our selected features based a cross-validation score. That is, we start with 0 features and choose the best single feature with the highest score. The procedure is repeated until we reach the desired number of selected features.

We can also go in the reverse direction (backward SFS), _i.e._ start with all the features and greedily choose features to remove one by one. We illustrate both approaches here.

from sklearn.feature\_selection import [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")

tic\_fwd \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
sfs\_forward \= [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
(
    ridge, n\_features\_to\_select\=2, direction\="forward"
).fit(X, y)
toc\_fwd \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

tic\_bwd \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
sfs\_backward \= [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
(
    ridge, n\_features\_to\_select\=2, direction\="backward"
).fit(X, y)
toc\_bwd \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

print(
    "Features selected by forward sequential selection: "
    f"{feature\_names\[sfs\_forward.get\_support()\]}"
)
print(f"Done in {toc\_fwd \- tic\_fwd:.3f}s")
print(
    "Features selected by backward sequential selection: "
    f"{feature\_names\[sfs\_backward.get\_support()\]}"
)
print(f"Done in {toc\_bwd \- tic\_bwd:.3f}s")

Copy to clipboard

Features selected by forward sequential selection: \['bmi' 's5'\]
Done in 0.244s
Features selected by backward sequential selection: \['bmi' 's5'\]
Done in 0.688s

Copy to clipboard

Interestingly, forward and backward selection have selected the same set of features. In general, this isn’t the case and the two methods would lead to different results.

We also note that the features selected by SFS differ from those selected by feature importance: SFS selects `bmi` instead of `s1`. This does sound reasonable though, since `bmi` corresponds to the third most important feature according to the coefficients. It is quite remarkable considering that SFS makes no use of the coefficients at all.

To finish with, we should note that [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 is significantly faster than SFS. Indeed, [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 only needs to fit a model once, while SFS needs to cross-validate many different models for each of the iterations. SFS however works with any model, while [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
 requires the underlying estimator to expose a `coef_` attribute or a `feature_importances_` attribute. The forward SFS is faster than the backward SFS because it only needs to perform `n_features_to_select = 2` iterations, while the backward SFS needs to perform `n_features - n_features_to_select = 8` iterations.

Using negative tolerance values[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#using-negative-tolerance-values "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
 can be used to remove features present in the dataset and return a smaller subset of the original features with `direction="backward"` and a negative value of `tol`.

We begin by loading the Breast Cancer dataset, consisting of 30 different features and 569 samples.

import numpy as np

from sklearn.datasets import [load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")

breast\_cancer\_data \= [load\_breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")
()
X, y \= breast\_cancer\_data.data, breast\_cancer\_data.target
feature\_names \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(breast\_cancer\_data.feature\_names)
print(breast\_cancer\_data.DESCR)

Copy to clipboard

.. \_breast\_cancer\_dataset:

Breast cancer Wisconsin (diagnostic) dataset
--------------------------------------------

\*\*Data Set Characteristics:\*\*

:Number of Instances: 569

:Number of Attributes: 30 numeric, predictive attributes and the class

:Attribute Information:
    - radius (mean of distances from center to points on the perimeter)
    - texture (standard deviation of gray-scale values)
    - perimeter
    - area
    - smoothness (local variation in radius lengths)
    - compactness (perimeter^2 / area - 1.0)
    - concavity (severity of concave portions of the contour)
    - concave points (number of concave portions of the contour)
    - symmetry
    - fractal dimension ("coastline approximation" - 1)

    The mean, standard error, and "worst" or largest (mean of the three
    worst/largest values) of these features were computed for each image,
    resulting in 30 features.  For instance, field 0 is Mean Radius, field
    10 is Radius SE, field 20 is Worst Radius.

    - class:
            - WDBC-Malignant
            - WDBC-Benign

:Summary Statistics:

===================================== ====== ======
                                        Min    Max
===================================== ====== ======
radius (mean):                        6.981  28.11
texture (mean):                       9.71   39.28
perimeter (mean):                     43.79  188.5
area (mean):                          143.5  2501.0
smoothness (mean):                    0.053  0.163
compactness (mean):                   0.019  0.345
concavity (mean):                     0.0    0.427
concave points (mean):                0.0    0.201
symmetry (mean):                      0.106  0.304
fractal dimension (mean):             0.05   0.097
radius (standard error):              0.112  2.873
texture (standard error):             0.36   4.885
perimeter (standard error):           0.757  21.98
area (standard error):                6.802  542.2
smoothness (standard error):          0.002  0.031
compactness (standard error):         0.002  0.135
concavity (standard error):           0.0    0.396
concave points (standard error):      0.0    0.053
symmetry (standard error):            0.008  0.079
fractal dimension (standard error):   0.001  0.03
radius (worst):                       7.93   36.04
texture (worst):                      12.02  49.54
perimeter (worst):                    50.41  251.2
area (worst):                         185.2  4254.0
smoothness (worst):                   0.071  0.223
compactness (worst):                  0.027  1.058
concavity (worst):                    0.0    1.252
concave points (worst):               0.0    0.291
symmetry (worst):                     0.156  0.664
fractal dimension (worst):            0.055  0.208
===================================== ====== ======

:Missing Attribute Values: None

:Class Distribution: 212 - Malignant, 357 - Benign

:Creator:  Dr. William H. Wolberg, W. Nick Street, Olvi L. Mangasarian

:Donor: Nick Street

:Date: November, 1995

This is a copy of UCI ML Breast Cancer Wisconsin (Diagnostic) datasets.
https://goo.gl/U2Uwz2

Features are computed from a digitized image of a fine needle
aspirate (FNA) of a breast mass.  They describe
characteristics of the cell nuclei present in the image.

Separating plane described above was obtained using
Multisurface Method-Tree (MSM-T) \[K. P. Bennett, "Decision Tree\
Construction Via Linear Programming." Proceedings of the 4th\
Midwest Artificial Intelligence and Cognitive Science Society,\
pp. 97-101, 1992\], a classification method which uses linear
programming to construct a decision tree.  Relevant features
were selected using an exhaustive search in the space of 1-4
features and 1-3 separating planes.

The actual linear program used to obtain the separating plane
in the 3-dimensional space is that described in:
\[K. P. Bennett and O. L. Mangasarian: "Robust Linear\
Programming Discrimination of Two Linearly Inseparable Sets",\
Optimization Methods and Software 1, 1992, 23-34\].

This database is also available through the UW CS ftp server:

ftp ftp.cs.wisc.edu
cd math-prog/cpo-dataset/machine-learn/WDBC/

.. dropdown:: References

  - W.N. Street, W.H. Wolberg and O.L. Mangasarian. Nuclear feature extraction
    for breast tumor diagnosis. IS&T/SPIE 1993 International Symposium on
    Electronic Imaging: Science and Technology, volume 1905, pages 861-870,
    San Jose, CA, 1993.
  - O.L. Mangasarian, W.N. Street and W.H. Wolberg. Breast cancer diagnosis and
    prognosis via linear programming. Operations Research, 43(4), pages 570-577,
    July-August 1995.
  - W.H. Wolberg, W.N. Street, and O.L. Mangasarian. Machine learning techniques
    to diagnose breast cancer from fine-needle aspirates. Cancer Letters 77 (1994)
    163-171.

Copy to clipboard

We will make use of the [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 estimator with [`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
 to perform the feature selection.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import [roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

for tol in \[\-1e-2, \-1e-3, \-1e-4\]:
    start \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    feature\_selector \= [SequentialFeatureSelector](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector")
(
        [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(),
        n\_features\_to\_select\="auto",
        direction\="backward",
        scoring\="roc\_auc",
        tol\=tol,
        n\_jobs\=2,
    )
    model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), feature\_selector, [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
())
    model.fit(X, y)
    end \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    print(f"\\ntol: {tol}")
    print(f"Features selected: {feature\_names\[model\[1\].get\_support()\]}")
    print(f"ROC AUC score: {[roc\_auc\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
(y, model.predict\_proba(X)\[:, 1\]):.3f}")
    print(f"Done in {end \- start:.3f}s")

Copy to clipboard

tol: -0.01
Features selected: \['worst perimeter'\]
ROC AUC score: 0.975
Done in 18.929s

tol: -0.001
Features selected: \['radius error' 'fractal dimension error' 'worst texture'\
 'worst perimeter' 'worst concave points'\]
ROC AUC score: 0.997
Done in 18.597s

tol: -0.0001
Features selected: \['mean compactness' 'mean concavity' 'mean concave points' 'radius error'\
 'area error' 'concave points error' 'symmetry error'\
 'fractal dimension error' 'worst texture' 'worst perimeter' 'worst area'\
 'worst concave points' 'worst symmetry'\]
ROC AUC score: 0.998
Done in 15.243s

Copy to clipboard

We can see that the number of features selected tend to increase as negative values of `tol` approach to zero. The time taken for feature selection also decreases as the values of `tol` come closer to zero.

**Total running time of the script:** (0 minutes 53.819 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_select_from_model_diabetes.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_select_from_model_diabetes.ipynb)

[`Download Jupyter notebook: plot_select_from_model_diabetes.ipynb`](https://scikit-learn.org/stable/_downloads/f1e887db7b101f4c858db7db12e9c7e2/plot_select_from_model_diabetes.ipynb)

[`Download Python source code: plot_select_from_model_diabetes.py`](https://scikit-learn.org/stable/_downloads/53e76f761ef04e8d06fa5757554513b0/plot_select_from_model_diabetes.py)

[`Download zipped: plot_select_from_model_diabetes.zip`](https://scikit-learn.org/stable/_downloads/cde909454db5f1c683f557f051f7934e/plot_select_from_model_diabetes.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_pipeline_thumb.png)

[Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Pipeline ANOVA SVM

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)

[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Recursive feature elimination with cross-validation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/53e76f761ef04e8d06fa5757554513b0/plot_select_from_model_diabetes.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f1e887db7b101f4c858db7db12e9c7e2/plot_select_from_model_diabetes.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/cde909454db5f1c683f557f051f7934e/plot_select_from_model_diabetes.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_select_from_model_diabetes.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_select_from_model_diabetes.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)