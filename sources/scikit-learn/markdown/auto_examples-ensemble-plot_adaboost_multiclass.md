[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_adaboost_multiclass.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_adaboost_multiclass.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_adaboost_multiclass.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_adaboost_multiclass.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_adaboost_multiclass.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_adaboost_multiclass.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#sphx-glr-download-auto-examples-ensemble-plot-adaboost-multiclass-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Multi-class AdaBoosted Decision Trees[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#multi-class-adaboosted-decision-trees "Link to this heading")

============================================================================================================================================================================================

This example shows how boosting can improve the prediction accuracy on a multi-label classification problem. It reproduces a similar experiment as depicted by Figure 1 in Zhu et al [\[1\]](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#id2)
.

The core principle of AdaBoost (Adaptive Boosting) is to fit a sequence of weak learners (e.g. Decision Trees) on repeatedly re-sampled versions of the data. Each sample carries a weight that is adjusted after each training step, such that misclassified samples will be assigned higher weights. The re-sampling process with replacement takes into account the weights assigned to each sample. Samples with higher weights have a greater chance of being selected multiple times in the new data set, while samples with lower weights are less likely to be selected. This ensures that subsequent iterations of the algorithm focus on the difficult-to-classify samples.

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Creating the dataset[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#creating-the-dataset "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

The classification dataset is constructed by taking a ten-dimensional standard normal distribution (x in R10) and defining three classes separated by nested concentric ten-dimensional spheres such that roughly equal numbers of samples are in each class (quantiles of the χ2 distribution).

from sklearn.datasets import [make\_gaussian\_quantiles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")

X, y \= [make\_gaussian\_quantiles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")
(
    n\_samples\=2\_000, n\_features\=10, n\_classes\=3, random\_state\=1
)

Copy to clipboard

We split the dataset into 2 sets: 70 percent of the samples are used for training and the remaining 30 percent for testing.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, train\_size\=0.7, random\_state\=42
)

Copy to clipboard

Training the `AdaBoostClassifier`[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#training-the-adaboostclassifier "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We train the [`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
. The estimator utilizes boosting to improve the classification accuracy. Boosting is a method designed to train weak learners (i.e. `estimator`) that learn from their predecessor’s mistakes.

Here, we define the weak learner as a [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 and set the maximum number of leaves to 8. In a real setting, this parameter should be tuned. We set it to a rather low value to limit the runtime of the example.

The `SAMME` algorithm build into the [`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
 then uses the correct or incorrect predictions made be the current weak learner to update the sample weights used for training the consecutive weak learners. Also, the weight of the weak learner itself is calculated based on its accuracy in classifying the training examples. The weight of the weak learner determines its influence on the final ensemble prediction.

from sklearn.ensemble import [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
from sklearn.tree import [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")

weak\_learner \= [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
(max\_leaf\_nodes\=8)
n\_estimators \= 300

adaboost\_clf \= [AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
(
    estimator\=weak\_learner,
    n\_estimators\=n\_estimators,
    random\_state\=42,
).fit(X\_train, y\_train)

Copy to clipboard

Analysis[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#analysis "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

### Convergence of the `AdaBoostClassifier`[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#convergence-of-the-adaboostclassifier "Link to this heading")

To demonstrate the effectiveness of boosting in improving accuracy, we evaluate the misclassification error of the boosted trees in comparison to two baseline scores. The first baseline score is the `misclassification_error` obtained from a single weak-learner (i.e. [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
), which serves as a reference point. The second baseline score is obtained from the [`DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
, which predicts the most prevalent class in a dataset.

from sklearn.dummy import [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
from sklearn.metrics import [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")

dummy\_clf \= [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
()

def misclassification\_error(y\_true, y\_pred):
    return 1 \- [accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")
(y\_true, y\_pred)

weak\_learners\_misclassification\_error \= misclassification\_error(
    y\_test, weak\_learner.fit(X\_train, y\_train).predict(X\_test)
)

dummy\_classifiers\_misclassification\_error \= misclassification\_error(
    y\_test, dummy\_clf.fit(X\_train, y\_train).predict(X\_test)
)

print(
    "DecisionTreeClassifier's misclassification\_error: "
    f"{weak\_learners\_misclassification\_error:.3f}"
)
print(
    "DummyClassifier's misclassification\_error: "
    f"{dummy\_classifiers\_misclassification\_error:.3f}"
)

Copy to clipboard

DecisionTreeClassifier's misclassification\_error: 0.475
DummyClassifier's misclassification\_error: 0.692

Copy to clipboard

After training the [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
 model, the achieved error surpasses the expected value that would have been obtained by guessing the most frequent class label, as the [`DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
 does.

Now, we calculate the `misclassification_error`, i.e. `1 - accuracy`, of the additive model ([`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
) at each boosting iteration on the test set to assess its performance.

We use [`staged_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier.staged_predict "sklearn.ensemble.AdaBoostClassifier.staged_predict")
 that makes as many iterations as the number of fitted estimator (i.e. corresponding to `n_estimators`). At iteration `n`, the predictions of AdaBoost only use the `n` first weak learners. We compare these predictions with the true predictions `y_test` and we, therefore, conclude on the benefit (or not) of adding a new weak learner into the chain.

We plot the misclassification error for the different stages:

import matplotlib.pyplot as plt
import pandas as pd

boosting\_errors \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "Number of trees": range(1, n\_estimators + 1),
        "AdaBoost": \[\
            misclassification\_error(y\_test, y\_pred)\
            for y\_pred in adaboost\_clf.staged\_predict(X\_test)\
        \],
    }
).set\_index("Number of trees")
ax \= boosting\_errors.plot()
ax.set\_ylabel("Misclassification error on test set")
ax.set\_title("Convergence of AdaBoost algorithm")

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    \[boosting\_errors.index.min(), boosting\_errors.index.max()\],
    \[weak\_learners\_misclassification\_error, weak\_learners\_misclassification\_error\],
    color\="tab:orange",
    linestyle\="dashed",
)
[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
    \[boosting\_errors.index.min(), boosting\_errors.index.max()\],
    \[\
        dummy\_classifiers\_misclassification\_error,\
        dummy\_classifiers\_misclassification\_error,\
    \],
    color\="c",
    linestyle\="dotted",
)
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(\["AdaBoost", "DecisionTreeClassifier", "DummyClassifier"\], loc\=1)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Convergence of AdaBoost algorithm](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_multiclass_001.png)

The plot shows the missclassification error on the test set after each boosting iteration. We see that the error of the boosted trees converges to an error of around 0.3 after 50 iterations, indicating a significantly higher accuracy compared to a single tree, as illustrated by the dashed line in the plot.

The misclassification error jitters because the `SAMME` algorithm uses the discrete outputs of the weak learners to train the boosted model.

The convergence of [`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
 is mainly influenced by the learning rate (i.e. `learning_rate`), the number of weak learners used (`n_estimators`), and the expressivity of the weak learners (e.g. `max_leaf_nodes`).

### Errors and weights of the Weak Learners[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#errors-and-weights-of-the-weak-learners "Link to this heading")

As previously mentioned, AdaBoost is a forward stagewise additive model. We now focus on understanding the relationship between the attributed weights of the weak learners and their statistical performance.

We use the fitted [`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")
’s attributes `estimator_errors_` and `estimator_weights_` to investigate this link.

weak\_learners\_info \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(
    {
        "Number of trees": range(1, n\_estimators + 1),
        "Errors": adaboost\_clf.estimator\_errors\_,
        "Weights": adaboost\_clf.estimator\_weights\_,
    }
).set\_index("Number of trees")

axs \= weak\_learners\_info.plot(
    subplots\=True, layout\=(1, 2), figsize\=(10, 4), legend\=False, color\="tab:blue"
)
axs\[0, 0\].set\_ylabel("Train error")
axs\[0, 0\].set\_title("Weak learner's training error")
axs\[0, 1\].set\_ylabel("Weight")
axs\[0, 1\].set\_title("Weak learner's weight")
fig \= axs\[0, 0\].get\_figure()
fig.suptitle("Weak learner's errors and weights for the AdaBoostClassifier")
fig.tight\_layout()

Copy to clipboard

![Weak learner's errors and weights for the AdaBoostClassifier, Weak learner's training error, Weak learner's weight](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_multiclass_002.png)

On the left plot, we show the weighted error of each weak learner on the reweighted training set at each boosting iteration. On the right plot, we show the weights associated with each weak learner later used to make the predictions of the final additive model.

We see that the error of the weak learner is the inverse of the weights. It means that our additive model will trust more a weak learner that makes smaller errors (on the training set) by increasing its impact on the final decision. Indeed, this exactly is the formulation of updating the base estimators’ weights after each iteration in AdaBoost.

Mathematical details[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html#mathematical-details "Link to this dropdown")

The weight associated with a weak learner trained at the stage m is inversely associated with its misclassification error such that:

α(m)\=log⁡1−err(m)err(m)+log⁡(K−1),

where α(m) and err(m) are the weight and the error of the m th weak learner, respectively, and K is the number of classes in our classification problem.

Another interesting observation boils down to the fact that the first weak learners of the model make fewer errors than later weak learners of the boosting chain.

The intuition behind this observation is the following: due to the sample reweighting, later classifiers are forced to try to classify more difficult or noisy samples and to ignore already well classified samples. Therefore, the overall error on the training set will increase. That’s why the weak learner’s weights are built to counter-balance the worse performing weak learners.

**Total running time of the script:** (0 minutes 3.550 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_adaboost_multiclass.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_adaboost_multiclass.ipynb)

[`Download Jupyter notebook: plot_adaboost_multiclass.ipynb`](https://scikit-learn.org/stable/_downloads/607c99671400a5055ef516d1aabd00c1/plot_adaboost_multiclass.ipynb)

[`Download Python source code: plot_adaboost_multiclass.py`](https://scikit-learn.org/stable/_downloads/4e46f015ab8300f262e6e8775bcdcf8a/plot_adaboost_multiclass.py)

[`Download zipped: plot_adaboost_multiclass.zip`](https://scikit-learn.org/stable/_downloads/bee6912c62835d8f46bc3fbcb465cb4b/plot_adaboost_multiclass.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_thumb.png)

[Decision Tree Regression with AdaBoost](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_regression.html)

Decision Tree Regression with AdaBoost

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_stack_predictors_thumb.png)

[Combine predictors using stacking](https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html)

Combine predictors using stacking

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)

[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Early stopping in Gradient Boosting

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/4e46f015ab8300f262e6e8775bcdcf8a/plot_adaboost_multiclass.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/607c99671400a5055ef516d1aabd00c1/plot_adaboost_multiclass.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/bee6912c62835d8f46bc3fbcb465cb4b/plot_adaboost_multiclass.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_adaboost_multiclass.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_adaboost_multiclass.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)