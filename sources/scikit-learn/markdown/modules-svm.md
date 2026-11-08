[Skip to main content](https://scikit-learn.org/stable/modules/svm.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/svm.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/svm.html)
[1.8.0](https://scikit-learn.org/1.8/modules/svm.html)
[1.7.2](https://scikit-learn.org/1.7/modules/svm.html)
[1.6.1](https://scikit-learn.org/1.6/modules/svm.html)
[1.5.2](https://scikit-learn.org/1.5/modules/svm.html)
[1.4.2](https://scikit-learn.org/1.4/modules/svm.html)

Collapse Sidebar Expand Sidebar

1.4. Support Vector Machines[#](https://scikit-learn.org/stable/modules/svm.html#support-vector-machines "Link to this heading")

=================================================================================================================================

**Support vector machines (SVMs)** are a set of supervised learning methods used for [classification](https://scikit-learn.org/stable/modules/svm.html#svm-classification)
, [regression](https://scikit-learn.org/stable/modules/svm.html#svm-regression)
 and [outliers detection](https://scikit-learn.org/stable/modules/svm.html#svm-outlier-detection)
.

The advantages of support vector machines are:

*   Effective in high dimensional spaces.
    
*   Still effective in cases where number of dimensions is greater than the number of samples.
    
*   Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
    
*   Versatile: different [Kernel functions](https://scikit-learn.org/stable/modules/svm.html#svm-kernels)
     can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
    

The disadvantages of support vector machines include:

*   If the number of features is much greater than the number of samples, avoid over-fitting in choosing [Kernel functions](https://scikit-learn.org/stable/modules/svm.html#svm-kernels)
     and regularization term is crucial.
    
*   SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see [Scores and probabilities](https://scikit-learn.org/stable/modules/svm.html#scores-probabilities)
    , below).
    

The support vector machines in scikit-learn support both dense (`numpy.ndarray` and convertible to that by `numpy.asarray`) and sparse (any `scipy.sparse`) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered `numpy.ndarray` (dense) or `scipy.sparse.csr_matrix` (sparse) with `dtype=float64`.

1.4.1. Classification[#](https://scikit-learn.org/stable/modules/svm.html#classification "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
, [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
 and [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 are classes capable of performing binary and multi-class classification on a dataset.

[![../_images/sphx_glr_plot_iris_svc_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_001.png)](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
 are similar methods, but accept slightly different sets of parameters and have different mathematical formulations (see section [Mathematical formulation](https://scikit-learn.org/stable/modules/svm.html#svm-mathematical-formulation)
). On the other hand, [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 is another (faster) implementation of Support Vector Classification for the case of a linear kernel. It also lacks some of the attributes of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
, like `support_`. [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 uses `squared_hinge` loss and due to its implementation in `liblinear` it also regularizes the intercept, if considered. This effect can however be reduced by carefully fine tuning its `intercept_scaling` parameter, which allows the intercept term to have a different regularization behavior compared to the other features. The classification results and score can therefore differ from the other two classifiers.

As other classifiers, [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
, [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
 and [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 take as input two arrays: an array `X` of shape `(n_samples, n_features)` holding the training samples, and an array `y` of class labels (strings or integers), of shape `(n_samples)`:

\>>> from sklearn import svm
\>>> X \= \[\[0, 0\], \[1, 1\]\]
\>>> y \= \[0, 1\]
\>>> clf \= svm.SVC()
\>>> clf.fit(X, y)
SVC()

Copy to clipboard

After being fitted, the model can then be used to predict new values:

\>>> clf.predict(\[\[2., 2.\]\])
array(\[1\])

Copy to clipboard

SVMs decision function (detailed in the [Mathematical formulation](https://scikit-learn.org/stable/modules/svm.html#svm-mathematical-formulation)
) depends on some subset of the training data, called the support vectors. Some properties of these support vectors can be found in attributes `support_vectors_`, `support_` and `n_support_`:

\>>> \# get support vectors
\>>> clf.support\_vectors\_
array(\[\[0., 0.\],\
       \[1., 1.\]\])
\>>> \# get indices of support vectors
\>>> clf.support\_
array(\[0, 1\]...)
\>>> \# get number of support vectors for each class
\>>> clf.n\_support\_
array(\[1, 1\]...)

Copy to clipboard

Examples

*   [SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html#sphx-glr-auto-examples-svm-plot-separating-hyperplane-py)
    
*   [SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#sphx-glr-auto-examples-svm-plot-svm-anova-py)
    
*   [Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-auto-examples-classification-plot-classification-probability-py)
    

### 1.4.1.1. Multi-class classification[#](https://scikit-learn.org/stable/modules/svm.html#multi-class-classification "Link to this heading")

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
 implement the “one-versus-one” (“ovo”) approach for multi-class classification, which constructs `n_classes * (n_classes - 1) / 2` classifiers, each trained on data from two classes. Internally, the solver always uses this “ovo” strategy to train the models. However, by default, the `decision_function_shape` parameter is set to `"ovr"` (“one-vs-rest”), to have a consistent interface with other classifiers by monotonically transforming the “ovo” decision function into an “ovr” decision function of shape `(n_samples, n_classes)`.

\>>> X \= \[\[0\], \[1\], \[2\], \[3\]\]
\>>> Y \= \[0, 1, 2, 3\]
\>>> clf \= svm.SVC(decision\_function\_shape\='ovo')
\>>> clf.fit(X, Y)
SVC(decision\_function\_shape='ovo')
\>>> dec \= clf.decision\_function(\[\[1\]\])
\>>> dec.shape\[1\] \# 6 classes: 4\*3/2 = 6
6
\>>> clf.decision\_function\_shape \= "ovr"
\>>> dec \= clf.decision\_function(\[\[1\]\])
\>>> dec.shape\[1\] \# 4 classes
4

Copy to clipboard

On the other hand, [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 implements a “one-vs-rest” (“ovr”) multi-class strategy, thus training `n_classes` models.

\>>> lin\_clf \= svm.LinearSVC()
\>>> lin\_clf.fit(X, Y)
LinearSVC()
\>>> dec \= lin\_clf.decision\_function(\[\[1\]\])
\>>> dec.shape\[1\]
4

Copy to clipboard

See [Mathematical formulation](https://scikit-learn.org/stable/modules/svm.html#svm-mathematical-formulation)
 for a complete description of the decision function.

Details on multi-class strategies[#](https://scikit-learn.org/stable/modules/svm.html#details-on-multi-class-strategies "Link to this dropdown")

Note that the [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 also implements an alternative multi-class strategy, the so-called multi-class SVM formulated by Crammer and Singer [\[16\]](https://scikit-learn.org/stable/modules/svm.html#id18)
, by using the option `multi_class='crammer_singer'`. In practice, one-vs-rest classification is usually preferred, since the results are mostly similar, but the runtime is significantly less.

For “one-vs-rest” [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 the attributes `coef_` and `intercept_` have the shape `(n_classes, n_features)` and `(n_classes,)` respectively. Each row of the coefficients corresponds to one of the `n_classes` “one-vs-rest” classifiers and similar for the intercepts, in the order of the “one” class.

In the case of “one-vs-one” [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
, the layout of the attributes is a little more involved. In the case of a linear kernel, the attributes `coef_` and `intercept_` have the shape `(n_classes * (n_classes - 1) / 2, n_features)` and `(n_classes * (n_classes - 1) / 2)` respectively. This is similar to the layout for [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 described above, with each row now corresponding to a binary classifier. The order for classes 0 to n is “0 vs 1”, “0 vs 2” , … “0 vs n”, “1 vs 2”, “1 vs 3”, “1 vs n”, . . . “n-1 vs n”.

The shape of `dual_coef_` is `(n_classes-1, n_SV)` with a somewhat hard to grasp layout. The columns correspond to the support vectors involved in any of the `n_classes * (n_classes - 1) / 2` “one-vs-one” classifiers. Each support vector `v` has a dual coefficient in each of the `n_classes - 1` classifiers comparing the class of `v` against another class. Note that some, but not all, of these dual coefficients, may be zero. The `n_classes - 1` entries in each column are these dual coefficients, ordered by the opposing class.

This might be clearer with an example: consider a three class problem with class 0 having three support vectors v00,v01,v02 and class 1 and 2 having two support vectors v10,v11 and v20,v21 respectively. For each support vector vij, there are two dual coefficients. Let’s call the coefficient of support vector vij in the classifier between classes i and k αi,kj. Then `dual_coef_` looks like this:

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| α0,10 | α0,11 | α0,12 | α1,00 | α1,01 | α2,00 | α2,01 |
| α0,20 | α0,21 | α0,22 | α1,20 | α1,21 | α2,10 | α2,11 |
| Coefficients for SVs of class 0 |     |     | Coefficients for SVs of class 1 |     | Coefficients for SVs of class 2 |     |

Examples

*   [Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html#sphx-glr-auto-examples-svm-plot-iris-svc-py)
    

### 1.4.1.2. Scores and probabilities[#](https://scikit-learn.org/stable/modules/svm.html#scores-and-probabilities "Link to this heading")

The `decision_function` method of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
 gives per-class scores for each sample (or a single score per sample in the binary case). When the constructor option `probability` is set to `True`, class membership probability estimates (from the methods `predict_proba` and `predict_log_proba`) are enabled. In the binary case, the probabilities are calibrated using Platt scaling [\[9\]](https://scikit-learn.org/stable/modules/svm.html#id11)
: logistic regression on the SVM’s scores, fit by an additional cross-validation on the training data. In the multiclass case, this is extended as per [\[10\]](https://scikit-learn.org/stable/modules/svm.html#id12)
.

Note

The same probability calibration procedure is available for all estimators via the [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
 (see [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html#calibration)
). In the case of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
, this procedure is builtin to [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
 which is used under the hood, so it does not rely on scikit-learn’s [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
.

The cross-validation involved in Platt scaling is an expensive operation for large datasets. In addition, the probability estimates may be inconsistent with the scores:

*   the “argmax” of the scores may not be the argmax of the probabilities
    
*   in binary classification, a sample may be labeled by `predict` as belonging to the positive class even if the output of `predict_proba` is less than 0.5; and similarly, it could be labeled as negative even if the output of `predict_proba` is more than 0.5.
    

Platt’s method is also known to have theoretical issues. If confidence scores are required, but these do not have to be probabilities, then it is advisable to set `probability=False` and use `decision_function` instead of `predict_proba`.

Please note that when `decision_function_shape='ovr'` and `n_classes > 2`, unlike `decision_function`, the `predict` method does not try to break ties by default. You can set `break_ties=True` for the output of `predict` to be the same as `np.argmax(clf.decision_function(...), axis=1)`, otherwise the first class among the tied classes will always be returned; but have in mind that it comes with a computational cost. See [SVM Tie Breaking Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html#sphx-glr-auto-examples-svm-plot-svm-tie-breaking-py)
 for an example on tie breaking.

### 1.4.1.3. Unbalanced problems[#](https://scikit-learn.org/stable/modules/svm.html#unbalanced-problems "Link to this heading")

In problems where it is desired to give more importance to certain classes or certain individual samples, the parameters `class_weight` and `sample_weight` can be used.

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 (but not [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
) implements the parameter `class_weight` in the `fit` method. It’s a dictionary of the form `{class_label : value}`, where value is a floating point number > 0 that sets the parameter `C` of class `class_label` to `C * value`. The figure below illustrates the decision boundary of an unbalanced problem, with and without weight correction.

[![../_images/sphx_glr_plot_separating_hyperplane_unbalanced_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_001.png)](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

[`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
, [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
, [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
, [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
, [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
, [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
 and [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 implement also weights for individual samples in the `fit` method through the `sample_weight` parameter. Similar to `class_weight`, this sets the parameter `C` for the i-th example to `C * sample_weight[i]`, which will encourage the classifier to get these samples right. The figure below illustrates the effect of sample weighting on the decision boundary. The size of the circles is proportional to the sample weights:

[![../_images/sphx_glr_plot_weighted_samples_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_001.png)](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)

Examples

*   [SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#sphx-glr-auto-examples-svm-plot-separating-hyperplane-unbalanced-py)
    
*   [SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html#sphx-glr-auto-examples-svm-plot-weighted-samples-py)
    

1.4.2. Regression[#](https://scikit-learn.org/stable/modules/svm.html#regression "Link to this heading")

---------------------------------------------------------------------------------------------------------

The method of Support Vector Classification can be extended to solve regression problems. This method is called Support Vector Regression.

The model produced by support vector classification (as described above) depends only on a subset of the training data, because the cost function for building the model does not care about training points that lie beyond the margin. Analogously, the model produced by Support Vector Regression depends only on a subset of the training data, because the cost function ignores samples whose prediction is close to their target.

There are three different implementations of Support Vector Regression: [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
, [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
 and [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
. [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
 provides a faster implementation than [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 but only considers the linear kernel, while [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
 implements a slightly different formulation than [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
 and [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
. Due to its implementation in `liblinear` [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
 also regularizes the intercept, if considered. This effect can however be reduced by carefully fine tuning its `intercept_scaling` parameter, which allows the intercept term to have a different regularization behavior compared to the other features. The classification results and score can therefore differ from the other two classifiers. See [Implementation details](https://scikit-learn.org/stable/modules/svm.html#svm-implementation-details)
 for further details.

As with classification classes, the fit method will take as argument vectors X, y, only that in this case y is expected to have floating point values instead of integer values:

\>>> from sklearn import svm
\>>> X \= \[\[0, 0\], \[2, 2\]\]
\>>> y \= \[0.5, 2.5\]
\>>> regr \= svm.SVR()
\>>> regr.fit(X, y)
SVR()
\>>> regr.predict(\[\[1, 1\]\])
array(\[1.5\])

Copy to clipboard

Examples

*   [Support Vector Regression (SVR) using linear and non-linear kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#sphx-glr-auto-examples-svm-plot-svm-regression-py)
    

1.4.3. Density estimation, novelty detection[#](https://scikit-learn.org/stable/modules/svm.html#density-estimation-novelty-detection "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

The class [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
 implements a One-Class SVM which is used in outlier detection.

See [Novelty and Outlier Detection](https://scikit-learn.org/stable/modules/outlier_detection.html#outlier-detection)
 for the description and usage of OneClassSVM.

1.4.4. Complexity[#](https://scikit-learn.org/stable/modules/svm.html#complexity "Link to this heading")

---------------------------------------------------------------------------------------------------------

Support Vector Machines are powerful tools, but their compute and storage requirements increase rapidly with the number of training vectors. The core of an SVM is a quadratic programming problem (QP), separating support vectors from the rest of the training data. The QP solver used by the [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
\-based implementation scales between O(nfeatures×nsamples2) and O(nfeatures×nsamples3) depending on how efficiently the [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
 cache is used in practice (dataset dependent). If the data is very sparse nfeatures should be replaced by the average number of non-zero features in a sample vector.

For the linear case, the algorithm used in [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 by the [liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
 implementation is much more efficient than its [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
\-based [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 counterpart and can scale almost linearly to millions of samples and/or features.

1.4.5. Tips on Practical Use[#](https://scikit-learn.org/stable/modules/svm.html#tips-on-practical-use "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   **Avoiding data copy**: For [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     and [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , if the data passed to certain methods is not C-ordered contiguous and double precision, it will be copied before calling the underlying C implementation. You can check whether a given numpy array is C-contiguous by inspecting its `flags` attribute.
    
    For [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     (and [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
    ) any input passed as a numpy array will be copied and converted to the [liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
     internal sparse data representation (double precision floats and int32 indices of non-zero components). If you want to fit a large-scale linear classifier without copying a dense numpy C-contiguous double precision array as input, we suggest to use the [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     class instead. The objective function can be configured to be almost the same as the [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     model.
    
*   **Kernel cache size**: For [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     and [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , the size of the kernel cache has a strong impact on run times for larger problems. If you have enough RAM available, it is recommended to set `cache_size` to a higher value than the default of 200(MB), such as 500(MB) or 1000(MB).
    
*   **Setting C**: `C` is `1` by default and it’s a reasonable default choice. If you have a lot of noisy observations you should decrease it: decreasing C corresponds to more regularization.
    
    [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     and [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
     are less sensitive to `C` when it becomes large, and prediction results stop improving after a certain threshold. Meanwhile, larger `C` values will take more time to train, sometimes up to 10 times longer, as shown in [\[11\]](https://scikit-learn.org/stable/modules/svm.html#id13)
    .
    
*   Support Vector Machine algorithms are not scale invariant, so **it is highly recommended to scale your data**. For example, scale each attribute on the input vector X to \[0,1\] or \[-1,+1\], or standardize it to have mean 0 and variance 1. Note that the _same_ scaling must be applied to the test vector to obtain meaningful results. This can be done easily by using a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
    :
    
    \>>> from sklearn.pipeline import make\_pipeline
    \>>> from sklearn.preprocessing import StandardScaler
    \>>> from sklearn.svm import SVC
    
    \>>> clf \= make\_pipeline(StandardScaler(), SVC())
    
    Copy to clipboard
    
    See section [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
     for more details on scaling and normalization.
    

*   Regarding the `shrinking` parameter, quoting [\[12\]](https://scikit-learn.org/stable/modules/svm.html#id14)
    : _We found that if the number of iterations is large, then shrinking can shorten the training time. However, if we loosely solve the optimization problem (e.g., by using a large stopping tolerance), the code without using shrinking may be much faster_
    
*   Parameter `nu` in [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    /[`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    /[`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
     approximates the fraction of training errors and support vectors.
    
*   In [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , if the data is unbalanced (e.g. many positive and few negative), set `class_weight='balanced'` and/or try different penalty parameters `C`.
    
*   **Randomness of the underlying implementations**: The underlying implementations of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
     use a random number generator only to shuffle the data for probability estimation (when `probability` is set to `True`). This randomness can be controlled with the `random_state` parameter. If `probability` is set to `False` these estimators are not random and `random_state` has no effect on the results. The underlying [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     implementation is similar to the ones of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     and [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    . As no probability estimation is provided for [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , it is not random.
    
    The underlying [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     implementation uses a random number generator to select features when fitting the model with a dual coordinate descent (i.e. when `dual` is set to `True`). It is thus not uncommon to have slightly different results for the same input data. If that happens, try with a smaller `tol` parameter. This randomness can also be controlled with the `random_state` parameter. When `dual` is set to `False` the underlying implementation of [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     is not random and `random_state` has no effect on the results.
    
*   Using L1 penalization as provided by `LinearSVC(penalty='l1', dual=False)` yields a sparse solution, i.e. only a subset of feature weights is different from zero and contribute to the decision function. Increasing `C` yields a more complex model (more features are selected). The `C` value that yields a “null” model (all weights equal to zero) can be calculated using [`l1_min_c`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#sklearn.svm.l1_min_c "sklearn.svm.l1_min_c")
    .
    

1.4.6. Kernel functions[#](https://scikit-learn.org/stable/modules/svm.html#kernel-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

The _kernel function_ can be any of the following:

*   linear: ⟨x,x′⟩.
    
*   polynomial: (γ⟨x,x′⟩+r)d, where d is specified by parameter `degree`, r by `coef0`.
    
*   rbf: exp⁡(−γ‖x−x′‖2), where γ is specified by parameter `gamma`, must be greater than 0.
    
*   sigmoid tanh⁡(γ⟨x,x′⟩+r), where r is specified by `coef0`.
    

Different kernels are specified by the `kernel` parameter:

\>>> linear\_svc \= svm.SVC(kernel\='linear')
\>>> linear\_svc.kernel
'linear'
\>>> rbf\_svc \= svm.SVC(kernel\='rbf')
\>>> rbf\_svc.kernel
'rbf'

Copy to clipboard

See also [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)
 for a solution to use RBF kernels that is much faster and more scalable.

### 1.4.6.1. Parameters of the RBF Kernel[#](https://scikit-learn.org/stable/modules/svm.html#parameters-of-the-rbf-kernel "Link to this heading")

When training an SVM with the _Radial Basis Function_ (RBF) kernel, two parameters must be considered: `C` and `gamma`. The parameter `C`, common to all SVM kernels, trades off misclassification of training examples against simplicity of the decision surface. A low `C` makes the decision surface smooth, while a high `C` aims at classifying all training examples correctly. `gamma` defines how much influence a single training example has. The larger `gamma` is, the closer other examples must be to be affected.

Proper choice of `C` and `gamma` is critical to the SVM’s performance. One is advised to use [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 with `C` and `gamma` spaced exponentially far apart to choose good values.

Examples

*   [RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#sphx-glr-auto-examples-svm-plot-rbf-parameters-py)
    
*   [Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html#sphx-glr-auto-examples-svm-plot-svm-scale-c-py)
    

### 1.4.6.2. Custom Kernels[#](https://scikit-learn.org/stable/modules/svm.html#custom-kernels "Link to this heading")

You can define your own kernels by either giving the kernel as a python function or by precomputing the Gram matrix.

Classifiers with custom kernels behave the same way as any other classifiers, except that:

*   Field `support_vectors_` is now empty, only indices of support vectors are stored in `support_`
    
*   A reference (and not a copy) of the first argument in the `fit()` method is stored for future reference. If that array changes between the use of `fit()` and `predict()` you will have unexpected results.
    

Using Python functions as kernels[#](https://scikit-learn.org/stable/modules/svm.html#using-python-functions-as-kernels "Link to this dropdown")

You can use your own defined kernels by passing a function to the `kernel` parameter.

Your kernel must take as arguments two matrices of shape `(n_samples_1, n_features)`, `(n_samples_2, n_features)` and return a kernel matrix of shape `(n_samples_1, n_samples_2)`.

The following code defines a linear kernel and creates a classifier instance that will use that kernel:

\>>> import numpy as np
\>>> from sklearn import svm
\>>> def my\_kernel(X, Y):
...     return np.dot(X, Y.T)
...
\>>> clf \= svm.SVC(kernel\=my\_kernel)

Copy to clipboard

Using the Gram matrix[#](https://scikit-learn.org/stable/modules/svm.html#using-the-gram-matrix "Link to this dropdown")

You can pass pre-computed kernels by using the `kernel='precomputed'` option. You should then pass Gram matrix instead of X to the `fit` and `predict` methods. The kernel values between _all_ training vectors and the test vectors must be provided:

\>>> import numpy as np
\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn import svm
\>>> X, y \= make\_classification(n\_samples\=10, random\_state\=0)
\>>> X\_train , X\_test , y\_train, y\_test \= train\_test\_split(X, y, random\_state\=0)
\>>> clf \= svm.SVC(kernel\='precomputed')
\>>> \# linear kernel computation
\>>> gram\_train \= np.dot(X\_train, X\_train.T)
\>>> clf.fit(gram\_train, y\_train)
SVC(kernel='precomputed')
\>>> \# predict on training examples
\>>> gram\_test \= np.dot(X\_test, X\_train.T)
\>>> clf.predict(gram\_test)
array(\[0, 1, 0\])

Copy to clipboard

Examples

*   [SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html#sphx-glr-auto-examples-svm-plot-custom-kernel-py)
    

1.4.7. Mathematical formulation[#](https://scikit-learn.org/stable/modules/svm.html#mathematical-formulation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

A support vector machine constructs a hyper-plane or set of hyper-planes in a high or infinite dimensional space, which can be used for classification, regression or other tasks. Intuitively, a good separation is achieved by the hyper-plane that has the largest distance to the nearest training data points of any class (so-called functional margin), since in general the larger the margin the lower the generalization error of the classifier. The figure below shows the decision function for a linearly separable problem, with three samples on the margin boundaries, called “support vectors”:

[![../_images/sphx_glr_plot_separating_hyperplane_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_001.png)](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_001.png)

In general, when the problem isn’t linearly separable, the support vectors are the samples _within_ the margin boundaries.

We recommend [\[13\]](https://scikit-learn.org/stable/modules/svm.html#id15)
 and [\[14\]](https://scikit-learn.org/stable/modules/svm.html#id16)
 as good references for the theory and practicalities of SVMs.

### 1.4.7.1. SVC[#](https://scikit-learn.org/stable/modules/svm.html#svc "Link to this heading")

Given training vectors xi∈Rp, i=1,…, n, in two classes, and a vector y∈{1,−1}n, our goal is to find w∈Rp and b∈R such that the prediction given by sign(wTϕ(x)+b) is correct for most samples.

SVC solves the following primal problem:

minw,b,ζ12wTw+C∑i\=1nζisubject to yi(wTϕ(xi)+b)≥1−ζi,ζi≥0,i\=1,...,n

Intuitively, we’re trying to maximize the margin (by minimizing ||w||2\=wTw), while incurring a penalty when a sample is misclassified or within the margin boundary. Ideally, the value yi(wTϕ(xi)+b) would be ≥1 for all samples, which indicates a perfect prediction. But problems are usually not always perfectly separable with a hyperplane, so we allow some samples to be at a distance ζi from their correct margin boundary. The penalty term `C` controls the strength of this penalty, and as a result, acts as an inverse regularization parameter (see note below).

The dual problem to the primal is

minα12αTQα−eTαsubject to yTα\=00≤αi≤C,i\=1,...,n

where e is the vector of all ones, and Q is an n by n positive semidefinite matrix, Qij≡yiyjK(xi,xj), where K(xi,xj)\=ϕ(xi)Tϕ(xj) is the kernel. The terms αi are called the dual coefficients, and they are upper-bounded by C. This dual representation highlights the fact that training vectors are implicitly mapped into a higher (maybe infinite) dimensional space by the function ϕ: see [kernel trick](https://en.wikipedia.org/wiki/Kernel_method)
.

Once the optimization problem is solved, the output of [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 for a given sample x becomes:

∑i∈SVyiαiK(xi,x)+b,

and the predicted class corresponds to its sign. We only need to sum over the support vectors (i.e. the samples that lie within the margin) because the dual coefficients αi are zero for the other samples.

These parameters can be accessed through the attributes `dual_coef_` which holds the product yiαi, `support_vectors_` which holds the support vectors, and `intercept_` which holds the independent term b.

Note

While SVM models derived from [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
 and [liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
 use `C` as regularization parameter, most other estimators use `alpha`. The exact equivalence between the amount of regularization of two models depends on the exact objective function optimized by the model. For example, when the estimator used is [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 regression, the relation between them is given as C\=1α.

LinearSVC[#](https://scikit-learn.org/stable/modules/svm.html#linearsvc "Link to this dropdown")

The primal problem can be equivalently formulated as

minw,b12wTw+C∑i\=1nmax(0,1−yi(wTϕ(xi)+b)),

where we make use of the [hinge loss](https://en.wikipedia.org/wiki/Hinge_loss)
. This is the form that is directly optimized by [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
, but unlike the dual form, this one does not involve inner products between samples, so the famous kernel trick cannot be applied. This is why only the linear kernel is supported by [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
 (ϕ is the identity function).

NuSVC[#](https://scikit-learn.org/stable/modules/svm.html#nusvc "Link to this dropdown")

The ν\-SVC formulation [\[15\]](https://scikit-learn.org/stable/modules/svm.html#id17)
 is a reparameterization of the C\-SVC and therefore mathematically equivalent.

We introduce a new parameter ν (instead of C) which controls the number of support vectors and _margin errors_: ν∈(0,1\] is an upper bound on the fraction of margin errors and a lower bound of the fraction of support vectors. A margin error corresponds to a sample that lies on the wrong side of its margin boundary: it is either misclassified, or it is correctly classified but does not lie beyond the margin.

### 1.4.7.2. SVR[#](https://scikit-learn.org/stable/modules/svm.html#svr "Link to this heading")

Given training vectors xi∈Rp, i=1,…, n, and a vector y∈Rn ε\-SVR solves the following primal problem:

minw,b,ζ,ζ∗12wTw+C∑i\=1n(ζi+ζi∗)subject to yi−wTϕ(xi)−b≤ε+ζi,wTϕ(xi)+b−yi≤ε+ζi∗,ζi,ζi∗≥0,i\=1,...,n

Here, we are penalizing samples whose prediction is at least ε away from their true target. These samples penalize the objective by ζi or ζi∗, depending on whether their predictions lie above or below the ε tube.

The dual problem is

minα,α∗12(α−α∗)TQ(α−α∗)+εeT(α+α∗)−yT(α−α∗)subject to eT(α−α∗)\=00≤αi,αi∗≤C,i\=1,...,n

where e is the vector of all ones, Q is an n by n positive semidefinite matrix, Qij≡K(xi,xj)\=ϕ(xi)Tϕ(xj) is the kernel. Here training vectors are implicitly mapped into a higher (maybe infinite) dimensional space by the function ϕ.

The prediction is:

∑i∈SV(αi−αi∗)K(xi,x)+b

These parameters can be accessed through the attributes `dual_coef_` which holds the difference αi−αi∗, `support_vectors_` which holds the support vectors, and `intercept_` which holds the independent term b

LinearSVR[#](https://scikit-learn.org/stable/modules/svm.html#linearsvr "Link to this dropdown")

The primal problem can be equivalently formulated as

minw,b12wTw+C∑i\=1nmax(0,|yi−(wTϕ(xi)+b)|−ε),

where we make use of the epsilon-insensitive loss, i.e. errors of less than ε are ignored. This is the form that is directly optimized by [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")
.

1.4.8. Implementation details[#](https://scikit-learn.org/stable/modules/svm.html#implementation-details "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Internally, we use [libsvm](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
 [\[12\]](https://scikit-learn.org/stable/modules/svm.html#id14)
 and [liblinear](https://www.csie.ntu.edu.tw/~cjlin/liblinear/)
 [\[11\]](https://scikit-learn.org/stable/modules/svm.html#id13)
 to handle all computations. These libraries are wrapped using C and Cython. For a description of the implementation and details of the algorithms used, please refer to their respective papers.

References

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)