[Skip to main content](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/feature_selection/plot_feature_selection_pipeline.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/feature_selection/plot_feature_selection_pipeline.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/feature_selection/plot_feature_selection_pipeline.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/feature_selection/plot_feature_selection_pipeline.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/feature_selection/plot_feature_selection_pipeline.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/feature_selection/plot_feature_selection_pipeline.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html#sphx-glr-download-auto-examples-feature-selection-plot-feature-selection-pipeline-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Pipeline ANOVA SVM[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html#pipeline-anova-svm "Link to this heading")

======================================================================================================================================================================

This example shows how a feature selection can be easily integrated within a machine learning pipeline.

We also show that you can easily inspect part of the pipeline.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

We will start by generating a binary classification dataset. Subsequently, we will divide the dataset into two subsets.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_features\=20,
    n\_informative\=3,
    n\_redundant\=0,
    n\_classes\=2,
    n\_clusters\_per\_class\=2,
    random\_state\=42,
)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=42)

Copy to clipboard

A common mistake done with feature selection is to search a subset of discriminative features on the full dataset, instead of only using the training set. The usage of scikit-learn [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 prevents to make such mistake.

Here, we will demonstrate how to build a pipeline where the first step will be the feature selection.

When calling `fit` on the training data, a subset of feature will be selected and the index of these selected features will be stored. The feature selector will subsequently reduce the number of features, and pass this subset to the classifier which will be trained.

from sklearn.feature\_selection import [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
, [f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

anova\_filter \= [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
([f\_classif](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")
, k\=3)
clf \= [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
()
anova\_svm \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(anova\_filter, clf)
anova\_svm.fit(X\_train, y\_train)

Copy to clipboard

Pipeline(steps=\[('selectkbest', SelectKBest(k=3)), ('linearsvc', LinearSVC())\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('selectkbest', ...), ('linearsvc', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 20  |

SelectKBest

[?Documentation for SelectKBest](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [k k: int or "all", default=10  <br>  <br>Number of top features to select.  <br>The "all" option bypasses selection, for use in a parameter search.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=k,-int%20or%20%22all%22%2C%20default%3D10) | 3   |
|     | [score\_func score\_func: callable, default=f\_classif  <br>  <br>Function taking two arrays X and y, and returning a pair of arrays  <br>(scores, pvalues) or a single array with scores.  <br>Default is f\_classif (see below "See Also"). The default function only  <br>works with classification tasks.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=score_func,-callable%2C%20default%3Df_classif) | <function f\_c...x7e1df6819170> |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=n_features_in_,-int) | int | 20  |
| [pvalues\_ pvalues\_: array-like of shape (n\_features,)  <br>  <br>p-values of feature scores, None if \`score\_func\` returned only scores.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=pvalues_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](20,) | \[0.71,0.36,0. ,...,0.64,0.4 ,0.02\] |
| [scores\_ scores\_: array-like of shape (n\_features,)  <br>  <br>Scores of features.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=scores_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](20,) | \[ 0.14, 0.86,104.06,..., 0.22, 0.73, 6.08\] |

3 features

|     |
| --- |
| x2  |
| x9  |
| x19 |

LinearSVC

[?Documentation for LinearSVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [penalty penalty: {'l1', 'l2'}, default='l2'  <br>  <br>Specifies the norm used in the penalization. The 'l2'  <br>penalty is the standard used in SVC. The 'l1' leads to \`\`coef\_\`\`  <br>vectors that are sparse.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%7D%2C%20default%3D%27l2%27) | 'l2' |
|     | [loss loss: {'hinge', 'squared\_hinge'}, default='squared\_hinge'  <br>  <br>Specifies the loss function. 'hinge' is the standard SVM loss  <br>(used e.g. by the SVC class) while 'squared\_hinge' is the  <br>square of the hinge loss. The combination of \`\`penalty='l1'\`\`  <br>and \`\`loss='hinge'\`\` is not supported.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=loss,-%7B%27hinge%27%2C%20%27squared_hinge%27%7D%2C%20default%3D%27squared_hinge%27) | 'squared\_hinge' |
|     | [dual dual: "auto" or bool, default="auto"  <br>  <br>Select the algorithm to either solve the dual or primal  <br>optimization problem. Prefer dual=False when n\_samples > n\_features.  <br>\`dual="auto"\` will choose the value of the parameter automatically,  <br>based on the values of \`n\_samples\`, \`n\_features\`, \`loss\`, \`multi\_class\`  <br>and \`penalty\`. If \`n\_samples\` < \`n\_features\` and optimizer supports  <br>chosen \`loss\`, \`multi\_class\` and \`penalty\`, then dual will be set to True,  <br>otherwise it will be set to False.  <br>  <br>.. versionchanged:: 1.3  <br>The \`"auto"\` option is added in version 1.3 and will be the default  <br>in version 1.5.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=dual,-%22auto%22%20or%20bool%2C%20default%3D%22auto%22) | 'auto' |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive.  <br>For an intuitive visualization of the effects of scaling  <br>the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |
|     | [multi\_class multi\_class: {'ovr', 'crammer\_singer'}, default='ovr'  <br>  <br>Determines the multi-class strategy if \`y\` contains more than  <br>two classes.  <br>\`\`"ovr"\`\` trains n\_classes one-vs-rest classifiers, while  <br>\`\`"crammer\_singer"\`\` optimizes a joint objective over all classes.  <br>While \`crammer\_singer\` is interesting from a theoretical perspective  <br>as it is consistent, it is seldom used in practice as it rarely leads  <br>to better accuracy and is more expensive to compute.  <br>If \`\`"crammer\_singer"\`\` is chosen, the options loss, penalty and dual  <br>will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=multi_class,-%7B%27ovr%27%2C%20%27crammer_singer%27%7D%2C%20default%3D%27ovr%27) | 'ovr' |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether or not to fit an intercept. If set to True, the feature vector  <br>is extended to include an intercept term: \`\[x\_1, ..., x\_n, 1\]\`, where  <br>1 corresponds to the intercept. If set to False, no intercept will be  <br>used in calculations (i.e. data is expected to be already centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1.0  <br>  <br>When \`fit\_intercept\` is True, the instance vector x becomes \`\`\[x\_1,  <br>..., x\_n, intercept\_scaling\]\`\`, i.e. a "synthetic" feature with a  <br>constant value equal to \`intercept\_scaling\` is appended to the instance  <br>vector. The intercept becomes intercept\_scaling \* synthetic feature  <br>weight. Note that liblinear internally penalizes the intercept,  <br>treating it like any other term in the feature vector. To reduce the  <br>impact of the regularization on the intercept, the \`intercept\_scaling\`  <br>parameter can be set to a value greater than 1; the higher the value of  <br>\`intercept\_scaling\`, the lower the impact of regularization on it.  <br>Then, the weights become \`\[w\_x\_1, ..., w\_x\_n,  <br>w\_intercept\*intercept\_scaling\]\`, where \`w\_x\_1, ..., w\_x\_n\` represent  <br>the feature weights and the intercept weight is scaled by  <br>\`intercept\_scaling\`. This scaling allows the intercept term to have a  <br>different regularization behavior compared to the other features.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=intercept_scaling,-float%2C%20default%3D1.0) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Set the parameter C of class i to \`\`class\_weight\[i\]\*C\`\` for  <br>SVC. If not given, all classes are supposed to have  <br>weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Enable verbose output. Note that this setting takes advantage of a  <br>per-process runtime setting in liblinear that, if enabled, may not work  <br>properly in a multithreaded context.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>the dual coordinate descent (if \`\`dual=True\`\`). When \`\`dual=False\`\` the  <br>underlying implementation of :class:\`LinearSVC\` is not random and  <br>\`\`random\_state\`\` has no effect on the results.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [max\_iter max\_iter: int, default=1000  <br>  <br>The maximum number of iterations to be run.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=max_iter,-int%2C%20default%3D1000) | 1000 |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The unique classes labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray of shape (1, n\_features) if n\_classes == 2 else (n\_classes, n\_features)  <br>  <br>Weights assigned to the features (coefficients in the primal  <br>problem).  <br>  <br>\`\`coef\_\`\` is a readonly property derived from \`\`raw\_coef\_\`\` that  <br>follows the internal memory layout of liblinear.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=coef_,-ndarray%20of%20shape%20%281%2C%20n_features%29%20if%20n_classes%20%3D%3D%202%20%20%20%20%20%20%20%20%20%20%20%20%20else%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 3) | \[\[0.76,0.27,0.26\]\] |
| [intercept\_ intercept\_: ndarray of shape (1,) if n\_classes == 2 else (n\_classes,)  <br>  <br>Constants in decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20if%20n_classes%20%3D%3D%202%20else%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.06\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=n_features_in_,-int) | int | 3   |
| [n\_iter\_ n\_iter\_: int  <br>  <br>Maximum number of iterations run across all classes.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.LinearSVC.html#:~:text=n_iter_,-int) | int | 5   |

  
  

Once the training is complete, we can predict on new unseen samples. In this case, the feature selector will only select the most discriminative features based on the information stored during training. Then, the data will be passed to the classifier which will make the prediction.

Here, we show the final metrics via a classification report.

from sklearn.metrics import [classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")

y\_pred \= anova\_svm.predict(X\_test)
print([classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(y\_test, y\_pred))

Copy to clipboard

              precision    recall  f1-score   support

           0       0.92      0.80      0.86        15
           1       0.75      0.90      0.82        10

    accuracy                           0.84        25
   macro avg       0.84      0.85      0.84        25
weighted avg       0.85      0.84      0.84        25

Copy to clipboard

Be aware that you can inspect a step in the pipeline. For instance, we might be interested about the parameters of the classifier. Since we selected three features, we expect to have three coefficients.

anova\_svm\[\-1\].coef\_

Copy to clipboard

array(\[\[0.75788833, 0.27161955, 0.26113448\]\])

Copy to clipboard

However, we do not know which features were selected from the original dataset. We could proceed by several manners. Here, we will invert the transformation of these coefficients to get information about the original space.

anova\_svm\[:\-1\].inverse\_transform(anova\_svm\[\-1\].coef\_)

Copy to clipboard

array(\[\[0.        , 0.        , 0.75788833, 0.        , 0.        ,\
        0.        , 0.        , 0.        , 0.        , 0.27161955,\
        0.        , 0.        , 0.        , 0.        , 0.        ,\
        0.        , 0.        , 0.        , 0.        , 0.26113448\]\])

Copy to clipboard

We can see that the features with non-zero coefficients are the selected features by the first step.

**Total running time of the script:** (0 minutes 0.029 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_feature_selection_pipeline.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_feature_selection_pipeline.ipynb)

[`Download Jupyter notebook: plot_feature_selection_pipeline.ipynb`](https://scikit-learn.org/stable/_downloads/51e6f272e94e3b63cfd48c4b41fbaa10/plot_feature_selection_pipeline.ipynb)

[`Download Python source code: plot_feature_selection_pipeline.py`](https://scikit-learn.org/stable/_downloads/5a7e586367163444711012a4c5214817/plot_feature_selection_pipeline.py)

[`Download zipped: plot_feature_selection_pipeline.zip`](https://scikit-learn.org/stable/_downloads/64040a7010774aea8b93dc426b3edcae/plot_feature_selection_pipeline.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_with_cross_validation_thumb.png)

[Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html)

Recursive feature elimination with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_select_from_model_diabetes_thumb.png)

[Model-based and sequential feature selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html)

Model-based and sequential feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/5a7e586367163444711012a4c5214817/plot_feature_selection_pipeline.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/51e6f272e94e3b63cfd48c4b41fbaa10/plot_feature_selection_pipeline.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/64040a7010774aea8b93dc426b3edcae/plot_feature_selection_pipeline.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_feature_selection_pipeline.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_feature_selection_pipeline.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)