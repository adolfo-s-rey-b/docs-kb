[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_cost_sensitive_learning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_cost_sensitive_learning.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_cost_sensitive_learning.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_cost_sensitive_learning.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_cost_sensitive_learning.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_cost_sensitive_learning.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#sphx-glr-download-auto-examples-model-selection-plot-cost-sensitive-learning-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Post-tuning the decision threshold for cost-sensitive learning[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#post-tuning-the-decision-threshold-for-cost-sensitive-learning "Link to this heading")

=========================================================================================================================================================================================================================================================

Once a classifier is trained, the output of the [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 method outputs class label predictions corresponding to a thresholding of either the [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 or the [predict\_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)
 output. For a binary classifier, the default threshold is defined as a posterior probability estimate of 0.5 or a decision score of 0.0.

However, this default strategy is most likely not optimal for the task at hand. Here, we use the “Statlog” German credit dataset [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id2)
 to illustrate a use case. In this dataset, the task is to predict whether a person has a “good” or “bad” credit. In addition, a cost-matrix is provided that specifies the cost of misclassification. Specifically, misclassifying a “bad” credit as “good” is five times more costly on average than misclassifying a “good” credit as “bad”.

We use the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 to select the cut-off point of the decision function that minimizes the provided business cost.

In the second part of the example, we further extend this approach by considering the problem of fraud detection in credit card transactions: in this case, the business metric depends on the amount of each individual transaction.

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Cost-sensitive learning with constant gains and costs[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#cost-sensitive-learning-with-constant-gains-and-costs "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this first section, we illustrate the use of the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 in a setting of cost-sensitive learning when the gains and costs associated to each entry of the confusion matrix are constant. We use the problematic presented in [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id3)
 using the “Statlog” German credit dataset [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id2)
.

### “Statlog” German credit dataset[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#statlog-german-credit-dataset "Link to this heading")

We fetch the German credit dataset from OpenML.

import sklearn
from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

[sklearn.set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(transform\_output\="pandas")

german\_credit \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=31, as\_frame\=True, parser\="pandas")
X, y \= german\_credit.data, german\_credit.target

Copy to clipboard

We check the feature types available in `X`.

X.info()

Copy to clipboard

<class 'pandas.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 20 columns):
 #   Column                  Non-Null Count  Dtype
---  ------                  --------------  -----
 0   checking\_status         1000 non-null   category
 1   duration                1000 non-null   int64
 2   credit\_history          1000 non-null   category
 3   purpose                 1000 non-null   category
 4   credit\_amount           1000 non-null   int64
 5   savings\_status          1000 non-null   category
 6   employment              1000 non-null   category
 7   installment\_commitment  1000 non-null   int64
 8   personal\_status         1000 non-null   category
 9   other\_parties           1000 non-null   category
 10  residence\_since         1000 non-null   int64
 11  property\_magnitude      1000 non-null   category
 12  age                     1000 non-null   int64
 13  other\_payment\_plans     1000 non-null   category
 14  housing                 1000 non-null   category
 15  existing\_credits        1000 non-null   int64
 16  job                     1000 non-null   category
 17  num\_dependents          1000 non-null   int64
 18  own\_telephone           1000 non-null   category
 19  foreign\_worker          1000 non-null   category
dtypes: category(13), int64(7)
memory usage: 69.1 KB

Copy to clipboard

Many features are categorical and usually string-encoded. We need to encode these categories when we develop our predictive model. Let’s check the targets.

y.value\_counts()

Copy to clipboard

class
good    700
bad     300
Name: count, dtype: int64

Copy to clipboard

Another observation is that the dataset is imbalanced. We would need to be careful when evaluating our predictive model and use a family of metrics that are adapted to this setting.

In addition, we observe that the target is string-encoded. Some metrics (e.g. precision and recall) require to provide the label of interest also called the “positive label”. Here, we define that our goal is to predict whether or not a sample is a “bad” credit.

pos\_label, neg\_label \= "bad", "good"

Copy to clipboard

To carry our analysis, we split our dataset using a single stratified split.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=0)

Copy to clipboard

We are ready to design our predictive model and the associated evaluation strategy.

### Evaluation metrics[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#evaluation-metrics "Link to this heading")

In this section, we define a set of metrics that we use later. To see the effect of tuning the cut-off point, we evaluate the predictive model using the Receiver Operating Characteristic (ROC) curve and the Precision-Recall curve. The values reported on these plots are therefore the true positive rate (TPR), also known as the recall or the sensitivity, and the false positive rate (FPR), also known as the specificity, for the ROC curve and the precision and recall for the Precision-Recall curve.

From these four metrics, scikit-learn does not provide a scorer for the FPR. We therefore need to define a small custom function to compute it.

from sklearn.metrics import [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")

def fpr\_score(y, y\_pred, neg\_label, pos\_label):
    cm \= [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
(y, y\_pred, labels\=\[neg\_label, pos\_label\])
    tn, fp, \_, \_ \= cm.ravel()
    tnr \= tn / (tn + fp)
    return 1 \- tnr

Copy to clipboard

As previously stated, the “positive label” is not defined as the value “1” and calling some of the metrics with this non-standard value raise an error. We need to provide the indication of the “positive label” to the metrics.

We therefore need to define a scikit-learn scorer using [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
 where the information is passed. We store all the custom scorers in a dictionary. To use them, we need to pass the fitted model, the data and the target on which we want to evaluate the predictive model.

from sklearn.metrics import [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
, [precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
, [recall\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")

tpr\_score \= [recall\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
  \# TPR and recall are the same metric
scoring \= {
    "precision": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([precision\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")
, pos\_label\=pos\_label),
    "recall": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
([recall\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")
, pos\_label\=pos\_label),
    "fpr": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(fpr\_score, neg\_label\=neg\_label, pos\_label\=pos\_label),
    "tpr": [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(tpr\_score, pos\_label\=pos\_label),
}

Copy to clipboard

In addition, the original research [\[1\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id2)
 defines a custom business metric. We call a “business metric” any metric function that aims at quantifying how the predictions (correct or wrong) might impact the business value of deploying a given machine learning model in a specific application context. For our credit prediction task, the authors provide a custom cost-matrix which encodes that classifying a “bad” credit as “good” is 5 times more costly on average than the opposite: it is less costly for the financing institution to not grant a credit to a potential customer that will not default (and therefore miss a good customer that would have otherwise both reimbursed the credit and paid interests) than to grant a credit to a customer that will default.

We define a python function that weighs the confusion matrix and returns the overall cost. The rows of the confusion matrix hold the counts of observed classes while the columns hold counts of predicted classes. Recall that here we consider “bad” as the positive class (second row and column). Scikit-learn model selection tools expect that we follow a convention that “higher” means “better”, hence the following gain matrix assigns negative gains (costs) to the two kinds of prediction errors:

*   a gain of `-1` for each false positive (“good” credit labeled as “bad”),
    
*   a gain of `-5` for each false negative (“bad” credit labeled as “good”),
    
*   a `0` gain for true positives and true negatives.
    

Note that theoretically, given that our model is calibrated, our dataset is representative and large enough, we do not need to tune the threshold, but can safely set it to 1/5 of the cost ratio, as stated by Eq. (2) in Elkan’s paper [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id3)
.

import numpy as np

def credit\_gain\_score(y, y\_pred, neg\_label, pos\_label):
    cm \= [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
(y, y\_pred, labels\=\[neg\_label, pos\_label\])

    gain\_matrix \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
        \[\
            \[0, \-1\],  \# -1 gain for false positives\
            \[\-5, 0\],  \# -5 gain for false negatives\
        \]
    )
    return [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(cm \* gain\_matrix)

scoring\["credit\_gain"\] \= [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(
    credit\_gain\_score, neg\_label\=neg\_label, pos\_label\=pos\_label
)

Copy to clipboard

### Vanilla predictive model[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#vanilla-predictive-model "Link to this heading")

We use [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 as a predictive model that natively handles categorical features and missing values.

from sklearn.ensemble import [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")

model \= [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
(
    categorical\_features\="from\_dtype", random\_state\=0
).fit(X\_train, y\_train)
model

Copy to clipboard

HistGradientBoostingClassifier(random\_state=0)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

HistGradientBoostingClassifier

[?Documentation for HistGradientBoostingClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [loss loss: {'log\_loss'}, default='log\_loss'  <br>  <br>The loss function to use in the boosting process.  <br>  <br>For binary classification problems, 'log\_loss' is also known as logistic loss,  <br>binomial deviance or binary crossentropy. Internally, the model fits one tree  <br>per boosting iteration and uses the logistic sigmoid function (expit) as  <br>inverse link function to compute the predicted positive class probability.  <br>  <br>For multiclass classification problems, 'log\_loss' is also known as multinomial  <br>deviance or categorical crossentropy. Internally, the model fits one tree per  <br>boosting iteration and per class and uses the softmax function as inverse link  <br>function to compute the predicted probabilities of the classes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=loss,-%7B%27log_loss%27%7D%2C%20default%3D%27log_loss%27) | 'log\_loss' |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees for binary classification. For multiclass  <br>classification, \`n\_classes\` trees per iteration are built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>The constraints are only valid for binary classifications and hold  <br>over the probability of the positive class.  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: :ref:\`accuracy <accuracy\_score>\` is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores. The higher the  <br>tolerance, the more likely we are to early stop: higher tolerance  <br>means that it will be harder for subsequent iterations to be  <br>considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`{class\_label: weight}\`.  <br>If not given, all classes are supposed to have weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`n\_samples / (n\_classes \* np.bincount(y))\`.  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if \`sample\_weight\` is specified.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: array, shape = (n\_classes,)  <br>  <br>Class labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=classes_,-array%2C%20shape%20%3D%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['bad','good'\] |
| [do\_early\_stopping\_ do\_early\_stopping\_: bool  <br>  <br>Indicates whether early stopping is used during training.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=do_early_stopping_,-bool) | bool | False |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](20,) | \['checking\_status','duration','credit\_history',...,'num\_dependents', 'own\_telephone','foreign\_worker'\] |
| [is\_categorical\_ is\_categorical\_: ndarray, shape (n\_features, ) or None  <br>  <br>Boolean mask for the categorical features. \`\`None\`\` if there are no  <br>categorical features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=is_categorical_,-ndarray%2C%20shape%20%28n_features%2C%20%29%20or%20None) | ndarray\[bool\](20,) | \[ True,False, True,...,False, True, True\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_features_in_,-int) | int | 20  |
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations as selected by early stopping, depending on  <br>the \`early\_stopping\` parameter. Otherwise it corresponds to max\_iter.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_iter_,-int) | int | 100 |
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of tree that are built at each iteration. This is equal to 1  <br>for binary classification, and to \`\`n\_classes\`\` for multiclass  <br>classification.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |
| [train\_score\_ train\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the training data. The first entry  <br>is the score of the ensemble before the first iteration. Scores are  <br>computed according to the \`\`scoring\`\` parameter. If \`\`scoring\`\` is  <br>not 'loss', scores are computed on a subset of at most 10 000  <br>samples. Empty if no early stopping.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=train_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |
| [validation\_score\_ validation\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the held-out validation data. The  <br>first entry is the score of the ensemble before the first iteration.  <br>Scores are computed according to the \`\`scoring\`\` parameter. Empty if  <br>no early stopping or if \`\`validation\_fraction\`\` is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=validation_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |

  
  

We evaluate the performance of our predictive model using the ROC and Precision-Recall curves.

import matplotlib.pyplot as plt

from sklearn.metrics import PrecisionRecallDisplay, RocCurveDisplay

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(14, 6))

[PrecisionRecallDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
(
    model, X\_test, y\_test, pos\_label\=pos\_label, ax\=axs\[0\], name\="GBDT"
)
axs\[0\].plot(
    scoring\["recall"\](model, X\_test, y\_test),
    scoring\["precision"\](model, X\_test, y\_test),
    marker\="o",
    markersize\=10,
    color\="tab:blue",
    label\="Default cut-off point at a probability of 0.5",
)
axs\[0\].set\_title("Precision-Recall curve")
axs\[0\].legend()

[RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(
    model,
    X\_test,
    y\_test,
    pos\_label\=pos\_label,
    ax\=axs\[1\],
    name\="GBDT",
    plot\_chance\_level\=True,
)
axs\[1\].plot(
    scoring\["fpr"\](model, X\_test, y\_test),
    scoring\["tpr"\](model, X\_test, y\_test),
    marker\="o",
    markersize\=10,
    color\="tab:blue",
    label\="Default cut-off point at a probability of 0.5",
)
axs\[1\].set\_title("ROC curve")
axs\[1\].legend()
\_ \= fig.suptitle("Evaluation of the vanilla GBDT model")

Copy to clipboard

![Evaluation of the vanilla GBDT model, Precision-Recall curve, ROC curve](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_001.png)

We recall that these curves give insights on the statistical performance of the predictive model for different cut-off points. For the Precision-Recall curve, the reported metrics are the precision and recall and for the ROC curve, the reported metrics are the TPR (same as recall) and FPR.

Here, the different cut-off points correspond to different levels of posterior probability estimates ranging between 0 and 1. By default, `model.predict` uses a cut-off point at a probability estimate of 0.5. The metrics for such a cut-off point are reported with the blue dot on the curves: it corresponds to the statistical performance of the model when using `model.predict`.

However, we recall that the original aim was to minimize the cost (or maximize the gain) as defined by the business metric. We can compute the value of the business metric:

print(f"Business defined metric: {scoring\['credit\_gain'\](model, X\_test, y\_test)}")

Copy to clipboard

Business defined metric: -209

Copy to clipboard

At this stage we don’t know if any other cut-off can lead to a greater gain. To find the optimal one, we need to compute the cost-gain using the business metric for all possible cut-off points and choose the best. This strategy can be quite tedious to implement by hand, but the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 class is here to help us. It automatically computes the cost-gain for all possible cut-off points and optimizes for the `scoring`.

### Tuning the cut-off point[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#tuning-the-cut-off-point "Link to this heading")

We use [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 to tune the cut-off point. We need to provide the business metric to optimize as well as the positive label. Internally, the optimum cut-off point is chosen such that it maximizes the business metric via cross-validation. By default a 5-fold stratified cross-validation is used.

from sklearn.model\_selection import [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")

tuned\_model \= [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
(
    estimator\=model,
    scoring\=scoring\["credit\_gain"\],
    store\_cv\_results\=True,  \# necessary to inspect all results
)
tuned\_model.fit(X\_train, y\_train)
print(f"{tuned\_model.best\_threshold\_\=:0.2f}")

Copy to clipboard

tuned\_model.best\_threshold\_=0.03

Copy to clipboard

We plot the ROC and Precision-Recall curves for the vanilla model and the tuned model. Also we plot the cut-off points that would be used by each model. Because, we are reusing the same code later, we define a function that generates the plots.

def plot\_roc\_pr\_curves(vanilla\_model, tuned\_model, \*, title):
    fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=3, figsize\=(21, 6))

    linestyles \= ("dashed", "dotted")
    markerstyles \= ("o", ">")
    colors \= ("tab:blue", "tab:orange")
    names \= ("Vanilla GBDT", "Tuned GBDT")
    for idx, (est, linestyle, marker, color, name) in enumerate(
        zip((vanilla\_model, tuned\_model), linestyles, markerstyles, colors, names)
    ):
        decision\_threshold \= getattr(est, "best\_threshold\_", 0.5)
        [PrecisionRecallDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_estimator "sklearn.metrics.PrecisionRecallDisplay.from_estimator")
(
            est,
            X\_test,
            y\_test,
            pos\_label\=pos\_label,
            ax\=axs\[0\],
            name\=name,
            curve\_kwargs\={"linestyle": linestyle, "color": color},
        )
        axs\[0\].plot(
            scoring\["recall"\](est, X\_test, y\_test),
            scoring\["precision"\](est, X\_test, y\_test),
            marker,
            markersize\=10,
            color\=color,
            label\=f"Cut-off point at probability of {decision\_threshold:.2f}",
        )
        [RocCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_estimator "sklearn.metrics.RocCurveDisplay.from_estimator")
(
            est,
            X\_test,
            y\_test,
            pos\_label\=pos\_label,
            curve\_kwargs\={"linestyle": linestyle, "color": color},
            ax\=axs\[1\],
            name\=name,
            plot\_chance\_level\=idx \== 1,
        )
        axs\[1\].plot(
            scoring\["fpr"\](est, X\_test, y\_test),
            scoring\["tpr"\](est, X\_test, y\_test),
            marker,
            markersize\=10,
            color\=color,
            label\=f"Cut-off point at probability of {decision\_threshold:.2f}",
        )

    axs\[0\].set\_title("Precision-Recall curve")
    axs\[0\].legend()
    axs\[1\].set\_title("ROC curve")
    axs\[1\].legend()

    axs\[2\].plot(
        tuned\_model.cv\_results\_\["thresholds"\],
        tuned\_model.cv\_results\_\["scores"\],
        color\="tab:orange",
    )
    axs\[2\].plot(
        tuned\_model.best\_threshold\_,
        tuned\_model.best\_score\_,
        "o",
        markersize\=10,
        color\="tab:orange",
        label\="Optimal cut-off point for the business metric",
    )
    axs\[2\].legend()
    axs\[2\].set\_xlabel("Decision threshold (probability)")
    axs\[2\].set\_ylabel("Objective score (using cost-matrix)")
    axs\[2\].set\_title("Objective score as a function of the decision threshold")
    fig.suptitle(title)

Copy to clipboard

title \= "Comparison of the cut-off point for the vanilla and tuned GBDT model"
plot\_roc\_pr\_curves(model, tuned\_model, title\=title)

Copy to clipboard

![Comparison of the cut-off point for the vanilla and tuned GBDT model, Precision-Recall curve, ROC curve, Objective score as a function of the decision threshold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_002.png)

The first remark is that both classifiers have exactly the same ROC and Precision-Recall curves. It is expected because by default, the classifier is fitted on the same training data. In a later section, we discuss more in detail the available options regarding model refitting and cross-validation.

The second remark is that the cut-off points of the vanilla and tuned model are different. To understand why the tuned model has chosen this cut-off point, we can look at the right-hand side plot that plots the objective score that is exactly the same as our business metric. We see that the optimum threshold corresponds to the maximum of the objective score. This maximum is reached for a decision threshold much lower than 0.5: the tuned model enjoys a much higher recall at the cost of significantly lower precision: the tuned model is much more eager to predict the “bad” class label for a larger fraction of individuals.

We can now check if choosing this cut-off point leads to a better score on the testing set:

print(f"Business defined metric: {scoring\['credit\_gain'\](tuned\_model, X\_test, y\_test)}")

Copy to clipboard

Business defined metric: -143

Copy to clipboard

We observe that tuning the decision threshold improves our business gains by almost a factor of 2.

### Consideration regarding model refitting and cross-validation[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#consideration-regarding-model-refitting-and-cross-validation "Link to this heading")

In the above experiment, we used the default setting of the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
. In particular, the cut-off point is tuned using a 5-fold stratified cross-validation. Also, the underlying predictive model is refitted on the entire training data once the cut-off point is chosen.

These two strategies can be changed by providing the `refit` and `cv` parameters. For instance, one could provide a fitted `estimator` and set `cv="prefit"`, in which case the cut-off point is found on the entire dataset provided at fitting time. This also requires to set `refit=False`, so that the underlying classifier will not be refitted. Here, we can try to do such an experiment:

model.fit(X\_train, y\_train)
tuned\_model.set\_params(cv\="prefit", refit\=False).fit(X\_train, y\_train)
print(f"{tuned\_model.best\_threshold\_\=:0.2f}")

Copy to clipboard

tuned\_model.best\_threshold\_=0.25

Copy to clipboard

Then, we evaluate our model with the same approach as before:

title \= "Tuned GBDT model without refitting and using the entire dataset"
plot\_roc\_pr\_curves(model, tuned\_model, title\=title)

Copy to clipboard

![Tuned GBDT model without refitting and using the entire dataset, Precision-Recall curve, ROC curve, Objective score as a function of the decision threshold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_003.png)

We observe that the optimum cut-off point is different from the one found in the previous experiment. If we look at the right-hand side plot, we can see that the business gain has a large plateau of near-optimal 0 gain for a large span of decision thresholds. This behavior is symptomatic of overfitting. Because we disabled cross-validation, we tuned the cut-off point on the same set as the model was trained on, and this is the reason for the observed overfitting.

This option should therefore be used with caution. One needs to make sure that the data provided at fitting time to the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 is not the same as the data used to train the underlying classifier. This can be the case when the idea is just to tune the predictive model on a completely new validation set without a costly complete refit.

When cross-validation is too costly, a potential alternative is to use a single train-test split by providing a floating number in range `[0, 1]` to the `cv` parameter. It splits the data into a training and testing set. (Note that `refit=False` is still set, which means the model will not be refitted on the entire training set once the threshold has been found.) Let’s explore this option:

tuned\_model.set\_params(cv\=0.75).fit(X\_train, y\_train)

Copy to clipboard

TunedThresholdClassifierCV(cv=0.75,
                           estimator=HistGradientBoostingClassifier(random\_state=0),
                           refit=False,
                           scoring=make\_scorer(credit\_gain\_score, response\_method='predict', neg\_label=good, pos\_label=bad),
                           store\_cv\_results=True)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

TunedThresholdClassifierCV

[?Documentation for TunedThresholdClassifierCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator instance  <br>  <br>The classifier, fitted or not, for which we want to optimize  <br>the decision threshold used during \`predict\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=estimator,-estimator%20instance) | HistGradientB...andom\_state=0) |
|     | [scoring scoring: str or callable, default="balanced\_accuracy"  <br>  <br>The objective metric to be optimized. Can be one of:  <br>  <br>\- str: string associated to a scoring function for binary classification,  <br>see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=scoring,-str%20or%20callable%2C%20default%3D%22balanced_accuracy%22) | make\_scorer(c...pos\_label=bad) |
|     | [cv cv: int, float, cross-validation generator, iterable or "prefit", default=None  <br>  <br>Determines the cross-validation splitting strategy to train classifier.  <br>Possible inputs for cv are:  <br>  <br>\* \`None\`, to use the default 5-fold stratified K-fold cross validation;  <br>\* An integer number, to specify the number of folds in a stratified k-fold;  <br>\* A float number, to specify a single shuffle split. The floating number should  <br>be in (0, 1) and represent the size of the validation set;  <br>\* An object to be used as a cross-validation generator;  <br>\* An iterable yielding train, test splits;  <br>\* \`"prefit"\`, to bypass the cross-validation.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. warning::  <br>Using \`cv="prefit"\` and passing the same dataset for fitting \`estimator\`  <br>and tuning the cut-off point is subject to undesired overfitting. You can  <br>refer to :ref:\`TunedThresholdClassifierCV\_no\_cv\` for an example.  <br>  <br>This option should only be used when the set used to fit \`estimator\` is  <br>different from the one used to tune the cut-off point (by calling  <br>:meth:\`TunedThresholdClassifierCV.fit\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=cv,-int%2C%20float%2C%20cross-validation%20generator%2C%20iterable%20or%20%22prefit%22%2C%20default%3DNone) | 0.75 |
|     | [refit refit: bool, default=True  <br>  <br>Whether or not to refit the classifier on the entire training set once  <br>the decision threshold has been found.  <br>Note that forcing \`refit=False\` on cross-validation having more  <br>than a single split will raise an error. Similarly, \`refit=True\` in  <br>conjunction with \`cv="prefit"\` will raise an error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=refit,-bool%2C%20default%3DTrue) | False |
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Whether to store all scores and thresholds computed during the cross-validation  <br>process.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | True |
|     | [response\_method response\_method: {"auto", "decision\_function", "predict\_proba"}, default="auto"  <br>  <br>Methods by the classifier \`estimator\` corresponding to the  <br>decision function for which we want to find a threshold. It can be:  <br>  <br>\* if \`"auto"\`, it will try to invoke, for each classifier,  <br>\`"predict\_proba"\` or \`"decision\_function"\` in that order.  <br>\* otherwise, one of \`"predict\_proba"\` or \`"decision\_function"\`.  <br>If the method is not implemented by the classifier, it will raise an  <br>error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=response_method,-%7B%22auto%22%2C%20%22decision_function%22%2C%20%22predict_proba%22%7D%2C%20default%3D%22auto%22) | 'auto' |
|     | [thresholds thresholds: int or array-like, default=100  <br>  <br>The number of decision threshold to use when discretizing the output of the  <br>classifier \`method\`. Pass an array-like to manually specify the thresholds  <br>to use.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=thresholds,-int%20or%20array-like%2C%20default%3D100) | 100 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. When \`cv\` represents a  <br>cross-validation strategy, the fitting and scoring on each data split  <br>is done in parallel. \`\`None\`\` means 1 unless in a  <br>:obj:\`joblib.parallel\_backend\` context. \`\`-1\`\` means using all  <br>processors. See :term:\`Glossary <n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the randomness of cross-validation when \`cv\` is a float.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_score\_ best\_score\_: float or None  <br>  <br>The optimal score of the objective metric, evaluated at \`best\_threshold\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=best_score_,-float%20or%20None) | float64 | \-342 |
| [best\_threshold\_ best\_threshold\_: float  <br>  <br>The new decision threshold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=best_threshold_,-float) | float64 | 0.1092 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The class labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['bad','good'\] |
| [cv\_results\_ cv\_results\_: dict or None  <br>  <br>A dictionary containing the scores and thresholds computed during the  <br>cross-validation process. Only exist if \`store\_cv\_results=True\`. The  <br>keys are \`"thresholds"\` and \`"scores"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=cv_results_,-dict%20or%20None) | dict | {'scores': array(\[-394.,... -840.\]), 'th...ds': array(\[1.73e-...01, 9.82e-01\])} |
| [estimator\_ estimator\_: estimator instance  <br>  <br>The fitted classifier used when predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=estimator_,-estimator%20instance) | HistGradientBoostingClassifier | HistGradientB...andom\_state=0) |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](20,) | \['checking\_status','duration','credit\_history',...,'num\_dependents', 'own\_telephone','foreign\_worker'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=n_features_in_,-int) | int | 20  |

HistGradientBoostingClassifier

[?Documentation for HistGradientBoostingClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [loss loss: {'log\_loss'}, default='log\_loss'  <br>  <br>The loss function to use in the boosting process.  <br>  <br>For binary classification problems, 'log\_loss' is also known as logistic loss,  <br>binomial deviance or binary crossentropy. Internally, the model fits one tree  <br>per boosting iteration and uses the logistic sigmoid function (expit) as  <br>inverse link function to compute the predicted positive class probability.  <br>  <br>For multiclass classification problems, 'log\_loss' is also known as multinomial  <br>deviance or categorical crossentropy. Internally, the model fits one tree per  <br>boosting iteration and per class and uses the softmax function as inverse link  <br>function to compute the predicted probabilities of the classes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=loss,-%7B%27log_loss%27%7D%2C%20default%3D%27log_loss%27) | 'log\_loss' |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees for binary classification. For multiclass  <br>classification, \`n\_classes\` trees per iteration are built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>The constraints are only valid for binary classifications and hold  <br>over the probability of the positive class.  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: :ref:\`accuracy <accuracy\_score>\` is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores. The higher the  <br>tolerance, the more likely we are to early stop: higher tolerance  <br>means that it will be harder for subsequent iterations to be  <br>considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`{class\_label: weight}\`.  <br>If not given, all classes are supposed to have weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`n\_samples / (n\_classes \* np.bincount(y))\`.  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if \`sample\_weight\` is specified.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: array, shape = (n\_classes,)  <br>  <br>Class labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=classes_,-array%2C%20shape%20%3D%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['bad','good'\] |
| [do\_early\_stopping\_ do\_early\_stopping\_: bool  <br>  <br>Indicates whether early stopping is used during training.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=do_early_stopping_,-bool) | bool | False |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](20,) | \['checking\_status','duration','credit\_history',...,'num\_dependents', 'own\_telephone','foreign\_worker'\] |
| [is\_categorical\_ is\_categorical\_: ndarray, shape (n\_features, ) or None  <br>  <br>Boolean mask for the categorical features. \`\`None\`\` if there are no  <br>categorical features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=is_categorical_,-ndarray%2C%20shape%20%28n_features%2C%20%29%20or%20None) | ndarray\[bool\](20,) | \[ True,False, True,...,False, True, True\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_features_in_,-int) | int | 20  |
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations as selected by early stopping, depending on  <br>the \`early\_stopping\` parameter. Otherwise it corresponds to max\_iter.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_iter_,-int) | int | 100 |
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of tree that are built at each iteration. This is equal to 1  <br>for binary classification, and to \`\`n\_classes\`\` for multiclass  <br>classification.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |
| [train\_score\_ train\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the training data. The first entry  <br>is the score of the ensemble before the first iteration. Scores are  <br>computed according to the \`\`scoring\`\` parameter. If \`\`scoring\`\` is  <br>not 'loss', scores are computed on a subset of at most 10 000  <br>samples. Empty if no early stopping.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=train_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |
| [validation\_score\_ validation\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the held-out validation data. The  <br>first entry is the score of the ensemble before the first iteration.  <br>Scores are computed according to the \`\`scoring\`\` parameter. Empty if  <br>no early stopping or if \`\`validation\_fraction\`\` is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=validation_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |

  
  

title \= "Tuned GBDT model using a single train-test split"
plot\_roc\_pr\_curves(model, tuned\_model, title\=title)

Copy to clipboard

![Tuned GBDT model using a single train-test split, Precision-Recall curve, ROC curve, Objective score as a function of the decision threshold](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_004.png)

Regarding the cut-off point, we observe that the optimum is similar to the multiple repeated cross-validation case. However, be aware that a single split does not account for the variability of the fit/predict process and thus we are unable to know if there is any variance in the cut-off point. The repeated cross-validation averages out this effect.

Another observation concerns the ROC and Precision-Recall curves of the tuned model. As expected, these curves differ from those of the vanilla model, given that we trained the underlying classifier on a subset of the data provided during fitting and reserved a validation set for tuning the cut-off point.

Cost-sensitive learning when gains and costs are not constant[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#cost-sensitive-learning-when-gains-and-costs-are-not-constant "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As stated in [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id3)
, gains and costs are generally not constant in real-world problems. In this section, we use a similar example as in [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id3)
 for the problem of detecting fraud in credit card transaction records.

### The credit card dataset[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#the-credit-card-dataset "Link to this heading")

credit\_card \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=1597, as\_frame\=True, parser\="pandas")
credit\_card.frame.info()

Copy to clipboard

<class 'pandas.DataFrame'>
RangeIndex: 284807 entries, 0 to 284806
Data columns (total 30 columns):
 #   Column  Non-Null Count   Dtype
---  ------  --------------   -----
 0   V1      284807 non-null  float64
 1   V2      284807 non-null  float64
 2   V3      284807 non-null  float64
 3   V4      284807 non-null  float64
 4   V5      284807 non-null  float64
 5   V6      284807 non-null  float64
 6   V7      284807 non-null  float64
 7   V8      284807 non-null  float64
 8   V9      284807 non-null  float64
 9   V10     284807 non-null  float64
 10  V11     284807 non-null  float64
 11  V12     284807 non-null  float64
 12  V13     284807 non-null  float64
 13  V14     284807 non-null  float64
 14  V15     284807 non-null  float64
 15  V16     284807 non-null  float64
 16  V17     284807 non-null  float64
 17  V18     284807 non-null  float64
 18  V19     284807 non-null  float64
 19  V20     284807 non-null  float64
 20  V21     284807 non-null  float64
 21  V22     284807 non-null  float64
 22  V23     284807 non-null  float64
 23  V24     284807 non-null  float64
 24  V25     284807 non-null  float64
 25  V26     284807 non-null  float64
 26  V27     284807 non-null  float64
 27  V28     284807 non-null  float64
 28  Amount  284807 non-null  float64
 29  Class   284807 non-null  category
dtypes: category(1), float64(29)
memory usage: 63.3 MB

Copy to clipboard

The dataset contains information about credit card records from which some are fraudulent and others are legitimate. The goal is therefore to predict whether or not a credit card record is fraudulent.

data \= credit\_card.frame.drop(columns\=\["Class"\])
target \= credit\_card.frame\["Class"\].astype(int)

Copy to clipboard

First, we check the class distribution of the datasets.

target.value\_counts(normalize\=True)

Copy to clipboard

Class
0    0.998273
1    0.001727
Name: proportion, dtype: float64

Copy to clipboard

The dataset is highly imbalanced with fraudulent transaction representing only 0.17% of the data. Since we are interested in training a machine learning model, we should also make sure that we have enough samples in the minority class to train the model.

target.value\_counts()

Copy to clipboard

Class
0    284315
1       492
Name: count, dtype: int64

Copy to clipboard

We observe that we have around 500 samples that is on the low end of the number of samples required to train a machine learning model. In addition of the target distribution, we check the distribution of the amount of the fraudulent transactions.

fraud \= target \== 1
amount\_fraud \= data\["Amount"\]\[fraud\]
\_ \= amount\_fraud.plot.hist(
    bins\=30, title\="Amount of fraud transaction", xlabel\="Amount (€)"
)

Copy to clipboard

![Amount of fraud transaction](https://scikit-learn.org/stable/_images/sphx_glr_plot_cost_sensitive_learning_005.png)

### Addressing the problem with a business metric[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#addressing-the-problem-with-a-business-metric "Link to this heading")

Now, we create a business metric that depends on the amount of each transaction. We define the cost matrix similarly to [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id3)
. Accepting a legitimate transaction provides a gain of 2% of the amount of the transaction. However, accepting a fraudulent transaction results in a loss of the amount of the transaction. As stated in [\[2\]](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#id3)
, the gain and loss related to refusals (of fraudulent and legitimate transactions) are not trivial to define. Here, we define that a refusal of a legitimate transaction is estimated to a loss of 5€ while the refusal of a fraudulent transaction is estimated to a gain of 50€. Therefore, we define the following function to compute the total benefit of a given decision:

def business\_metric(y\_true, y\_pred, amount):
    mask\_true\_positive \= (y\_true \== 1) & (y\_pred \== 1)
    mask\_true\_negative \= (y\_true \== 0) & (y\_pred \== 0)
    mask\_false\_positive \= (y\_true \== 0) & (y\_pred \== 1)
    mask\_false\_negative \= (y\_true \== 1) & (y\_pred \== 0)
    fraudulent\_refuse \= mask\_true\_positive.sum() \* 50
    fraudulent\_accept \= \-amount\[mask\_false\_negative\].sum()
    legitimate\_refuse \= mask\_false\_positive.sum() \* \-5
    legitimate\_accept \= (amount\[mask\_true\_negative\] \* 0.02).sum()
    return fraudulent\_refuse + fraudulent\_accept + legitimate\_refuse + legitimate\_accept

Copy to clipboard

From this business metric, we create a scikit-learn scorer that, given a fitted classifier and a test set, computes the business metric. We use the [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
 factory again here. The variable `amount` is an additional metadata to be passed to the scorer and we need to use [metadata routing](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 to take this information into account.

[sklearn.set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(enable\_metadata\_routing\=True)
business\_scorer \= [make\_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")
(business\_metric).set\_score\_request(amount\=True)

Copy to clipboard

So at this stage, we observe that the amount of the transaction is used twice: once as a feature to train our predictive model and once as metadata to compute the the business metric and thus the statistical performance of our model. When used as a feature, we are only required to have a column in `data` that contains the amount of each transaction. To use this information as metadata, we need to have an external variable that we can pass to the scorer or the model that internally routes this metadata to the scorer. So let’s create this variable.

amount \= credit\_card.frame\["Amount"\].to\_numpy()

Copy to clipboard

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

data\_train, data\_test, target\_train, target\_test, amount\_train, amount\_test \= (
    [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
        data, target, amount, stratify\=target, test\_size\=0.5, random\_state\=42
    )
)

Copy to clipboard

We first evaluate some baseline policies to serve as reference. Recall that class “0” is the legitimate class and class “1” is the fraudulent class.

from sklearn.dummy import [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")

always\_accept\_policy \= [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
(strategy\="constant", constant\=0)
always\_accept\_policy.fit(data\_train, target\_train)
benefit \= business\_scorer(
    always\_accept\_policy, data\_test, target\_test, amount\=amount\_test
)
print(f"Benefit of the 'always accept' policy: {benefit:,.2f}€")

Copy to clipboard

Benefit of the 'always accept' policy: 221,445.07€

Copy to clipboard

A policy that considers all transactions as legitimate would create a profit of around 220,000€. We make the same evaluation for a classifier that predicts all transactions as fraudulent.

always\_reject\_policy \= [DummyClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
(strategy\="constant", constant\=1)
always\_reject\_policy.fit(data\_train, target\_train)
benefit \= business\_scorer(
    always\_reject\_policy, data\_test, target\_test, amount\=amount\_test
)
print(f"Benefit of the 'always reject' policy: {benefit:,.2f}€")

Copy to clipboard

Benefit of the 'always reject' policy: -698,490.00€

Copy to clipboard

Such a policy would entail a catastrophic loss: almost 700,000€. This is expected since the vast majority of the transactions are legitimate and the policy would refuse them at a non-trivial cost.

A predictive model that adapts the accept/reject decisions on a per transaction basis should ideally allow us to make a profit larger than the 220,000€ of the best of our constant baseline policies.

We start with a logistic regression model with the default decision threshold at 0.5. Here we tune the hyperparameter `C` of the logistic regression with a proper scoring rule (the log loss) to ensure that the model’s probabilistic predictions returned by its `predict_proba` method are as accurate as possible, irrespectively of the choice of the value of the decision threshold.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

logistic\_regression \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
())
param\_grid \= {"logisticregression\_\_C": [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-6, 6, 13)}
model \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(logistic\_regression, param\_grid, scoring\="neg\_log\_loss").fit(
    data\_train, target\_train
)
model

Copy to clipboard

GridSearchCV(estimator=Pipeline(steps=\[('standardscaler', StandardScaler()),\
                                       ('logisticregression',\
                                        LogisticRegression())\]),
             param\_grid={'logisticregression\_\_C': array(\[1.e-06, 1.e-05, 1.e-04, 1.e-03, 1.e-02, 1.e-01, 1.e+00, 1.e+01,\
       1.e+02, 1.e+03, 1.e+04, 1.e+05, 1.e+06\])},
             scoring='neg\_log\_loss')

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

GridSearchCV

[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...egression())\]) |
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | {'logisticregression\_\_C': array(\[1.e-06...e+05, 1.e+06\])} |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | 'neg\_log\_loss' |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_estimator_,-estimator) | Pipeline | Pipeline(step...t64(100.0)))\]) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(8) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_params_,-dict) | dict | {'lo...\_C': np.float64(100.0)} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the best\_estimator  <br>  <br>For multi-metric evaluation, this is present only if \`\`refit\`\` is  <br>specified.  <br>  <br>This attribute is not available if \`\`refit\`\` is a function.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=best_score_,-float) | float64 | \-0.003994 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\|param\_kernel\|param\_gamma\|param\_degree\|split0\_test\_score\|...\|rank\_t...\|  <br>+============+===========+============+=================+===+=========+  <br>\| 'poly' \| -- \| 2 \| 0.80 \|...\| 2 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'poly' \| -- \| 3 \| 0.70 \|...\| 4 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.1 \| -- \| 0.80 \|...\| 3 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>\| 'rbf' \| 0.2 \| -- \| 0.93 \|...\| 1 \|  <br>+------------+-----------+------------+-----------------+---+---------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel': masked\_array(data = \['poly', 'poly', 'rbf', 'rbf'\],  <br>mask = \[False False False False\]...)  <br>'param\_gamma': masked\_array(data = \[-- -- 0.1 0.2\],  <br>mask = \[ True True False False\]...),  <br>'param\_degree': masked\_array(data = \[2.0 3.0 -- --\],  <br>mask = \[False False True True\]...),  <br>'split0\_test\_score' : \[0.80, 0.70, 0.80, 0.93\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70, 0.78\],  <br>'mean\_test\_score' : \[0.81, 0.60, 0.75, 0.85\],  <br>'std\_test\_score' : \[0.01, 0.10, 0.05, 0.08\],  <br>'rank\_test\_score' : \[2, 4, 3, 1\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70, 0.93\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70, 0.87\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70, 0.90\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00, 0.03\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43, 0.49\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00, 0.01\],  <br>'params' : \[{'kernel': 'poly', 'degree': 2}, ...\],  <br>}  <br>  <br>For an example of visualization and interpretation of GridSearch results,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.16, ... 0.19, 0.19\]), 'me...me': array(\[0.02, ... 0.02, 0.02\]), 'me...re': array(\[-0.01,...-0. , -0. \]), 'pa...\_C': masked\_array(...l\_value=1e+20), ...} |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`feature\_names\_in\_\` when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_features_in_,-int) | int | 29  |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit_time_,-float) | float | 0.2542 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | \_Scorer | make\_scorer(l...redict\_proba') |

best\_estimator\_: Pipeline

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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](29,) | \[ 0. ,-0. ,-0.01,..., 0. , 0. ,88.35\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 29  |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1.424e+05 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](29,) | \[ 1.97, 1.66, 1.53,..., 0.41, 0.31,256.68\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](29,) | \[ 3.86, 2.75, 2.34,..., 0.17, 0.1 ,65885.14\] |

29 features

|     |
| --- |
| V1  |
| V2  |
| V3  |
| V4  |
| V5  |
| V6  |
| V7  |
| V8  |
| V9  |
| V10 |
| V11 |
| V12 |
| V13 |
| V14 |
| V15 |
| V16 |
| V17 |
| V18 |
| V19 |
| V20 |
| V21 |
| V22 |
| V23 |
| V24 |
| V25 |
| V26 |
| V27 |
| V28 |
| Amount |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | np.float64(100.0) |
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
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 29) | \[\[ 0.1 , 0.02, 0.1 ,...,-0.3 ,-0.05, 0.18\]\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-8.96\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 29  |
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[25\] |

  
  

print(
    "Benefit of logistic regression with default threshold: "
    f"{business\_scorer(model, data\_test, target\_test, amount\=amount\_test):,.2f}€"
)

Copy to clipboard

Benefit of logistic regression with default threshold: 244,919.87€

Copy to clipboard

The business metric shows that our predictive model with a default decision threshold is already winning over the baseline in terms of profit and it would be already beneficial to use it to accept or reject transactions instead of accepting all transactions.

### Tuning the decision threshold[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#tuning-the-decision-threshold "Link to this heading")

Now the question is: is our model optimal for the type of decision that we want to do? Up to now, we did not optimize the decision threshold. We use the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 to optimize the decision given our business scorer. To avoid a nested cross-validation, we will use the best estimator found during the previous grid-search.

tuned\_model \= [TunedThresholdClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
(
    estimator\=model.best\_estimator\_,
    scoring\=business\_scorer,
    thresholds\=100,
    n\_jobs\=2,
)

Copy to clipboard

Since our business scorer requires the amount of each transaction, we need to pass this information in the `fit` method. The [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 is in charge of automatically dispatching this metadata to the underlying scorer.

tuned\_model.fit(data\_train, target\_train, amount\=amount\_train)

Copy to clipboard

TunedThresholdClassifierCV(estimator=Pipeline(steps=\[('standardscaler',\
                                                      StandardScaler()),\
                                                     ('logisticregression',\
                                                      LogisticRegression(C=np.float64(100.0)))\]),
                           n\_jobs=2,
                           scoring=make\_scorer(business\_metric, response\_method='predict'))

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

TunedThresholdClassifierCV

[?Documentation for TunedThresholdClassifierCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [estimator estimator: estimator instance  <br>  <br>The classifier, fitted or not, for which we want to optimize  <br>the decision threshold used during \`predict\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=estimator,-estimator%20instance) | Pipeline(step...t64(100.0)))\]) |
|     | [scoring scoring: str or callable, default="balanced\_accuracy"  <br>  <br>The objective metric to be optimized. Can be one of:  <br>  <br>\- str: string associated to a scoring function for binary classification,  <br>see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=scoring,-str%20or%20callable%2C%20default%3D%22balanced_accuracy%22) | make\_scorer(b...hod='predict') |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. When \`cv\` represents a  <br>cross-validation strategy, the fitting and scoring on each data split  <br>is done in parallel. \`\`None\`\` means 1 unless in a  <br>:obj:\`joblib.parallel\_backend\` context. \`\`-1\`\` means using all  <br>processors. See :term:\`Glossary <n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | 2   |
|     | [response\_method response\_method: {"auto", "decision\_function", "predict\_proba"}, default="auto"  <br>  <br>Methods by the classifier \`estimator\` corresponding to the  <br>decision function for which we want to find a threshold. It can be:  <br>  <br>\* if \`"auto"\`, it will try to invoke, for each classifier,  <br>\`"predict\_proba"\` or \`"decision\_function"\` in that order.  <br>\* otherwise, one of \`"predict\_proba"\` or \`"decision\_function"\`.  <br>If the method is not implemented by the classifier, it will raise an  <br>error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=response_method,-%7B%22auto%22%2C%20%22decision_function%22%2C%20%22predict_proba%22%7D%2C%20default%3D%22auto%22) | 'auto' |
|     | [thresholds thresholds: int or array-like, default=100  <br>  <br>The number of decision threshold to use when discretizing the output of the  <br>classifier \`method\`. Pass an array-like to manually specify the thresholds  <br>to use.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=thresholds,-int%20or%20array-like%2C%20default%3D100) | 100 |
|     | [cv cv: int, float, cross-validation generator, iterable or "prefit", default=None  <br>  <br>Determines the cross-validation splitting strategy to train classifier.  <br>Possible inputs for cv are:  <br>  <br>\* \`None\`, to use the default 5-fold stratified K-fold cross validation;  <br>\* An integer number, to specify the number of folds in a stratified k-fold;  <br>\* A float number, to specify a single shuffle split. The floating number should  <br>be in (0, 1) and represent the size of the validation set;  <br>\* An object to be used as a cross-validation generator;  <br>\* An iterable yielding train, test splits;  <br>\* \`"prefit"\`, to bypass the cross-validation.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. warning::  <br>Using \`cv="prefit"\` and passing the same dataset for fitting \`estimator\`  <br>and tuning the cut-off point is subject to undesired overfitting. You can  <br>refer to :ref:\`TunedThresholdClassifierCV\_no\_cv\` for an example.  <br>  <br>This option should only be used when the set used to fit \`estimator\` is  <br>different from the one used to tune the cut-off point (by calling  <br>:meth:\`TunedThresholdClassifierCV.fit\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=cv,-int%2C%20float%2C%20cross-validation%20generator%2C%20iterable%20or%20%22prefit%22%2C%20default%3DNone) | None |
|     | [refit refit: bool, default=True  <br>  <br>Whether or not to refit the classifier on the entire training set once  <br>the decision threshold has been found.  <br>Note that forcing \`refit=False\` on cross-validation having more  <br>than a single split will raise an error. Similarly, \`refit=True\` in  <br>conjunction with \`cv="prefit"\` will raise an error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=refit,-bool%2C%20default%3DTrue) | True |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the randomness of cross-validation when \`cv\` is a float.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Whether to store all scores and thresholds computed during the cross-validation  <br>process.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_score\_ best\_score\_: float or None  <br>  <br>The optimal score of the objective metric, evaluated at \`best\_threshold\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=best_score_,-float%20or%20None) | float64 | 5.057e+04 |
| [best\_threshold\_ best\_threshold\_: float  <br>  <br>The new decision threshold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=best_threshold_,-float) | float64 | 0.0303 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The class labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [estimator\_ estimator\_: estimator instance  <br>  <br>The fitted classifier used when predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=estimator_,-estimator%20instance) | Pipeline | Pipeline(step...t64(100.0)))\]) |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#:~:text=n_features_in_,-int) | int | 29  |

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('standardscaler', ...), ('logisticregression', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 29  |

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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](29,) | \[ 0. ,-0. ,-0.01,..., 0. , 0. ,88.35\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 29  |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1.424e+05 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](29,) | \[ 1.97, 1.66, 1.53,..., 0.41, 0.31,256.68\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](29,) | \[ 3.86, 2.75, 2.34,..., 0.17, 0.1 ,65885.14\] |

29 features

|     |
| --- |
| V1  |
| V2  |
| V3  |
| V4  |
| V5  |
| V6  |
| V7  |
| V8  |
| V9  |
| V10 |
| V11 |
| V12 |
| V13 |
| V14 |
| V15 |
| V16 |
| V17 |
| V18 |
| V19 |
| V20 |
| V21 |
| V22 |
| V23 |
| V24 |
| V25 |
| V26 |
| V27 |
| V28 |
| Amount |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | np.float64(100.0) |
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
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[int64\](2,) | \[0,1\] |
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 29) | \[\[ 0.1 , 0.02, 0.1 ,...,-0.3 ,-0.05, 0.18\]\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](29,) | \['V1','V2','V3',...,'V27','V28','Amount'\] |
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-8.96\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 29  |
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[25\] |

  
  

We observe that the tuned decision threshold is far away from the default 0.5:

print(f"Tuned decision threshold: {tuned\_model.best\_threshold\_:.2f}")

Copy to clipboard

Tuned decision threshold: 0.03

Copy to clipboard

print(
    "Benefit of logistic regression with a tuned threshold: "
    f"{business\_scorer(tuned\_model, data\_test, target\_test, amount\=amount\_test):,.2f}€"
)

Copy to clipboard

Benefit of logistic regression with a tuned threshold: 249,433.39€

Copy to clipboard

We observe that tuning the decision threshold increases the expected profit when deploying our model - as indicated by the business metric. It is therefore valuable, whenever possible, to optimize the decision threshold with respect to the business metric.

### Manually setting the decision threshold instead of tuning it[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cost_sensitive_learning.html#manually-setting-the-decision-threshold-instead-of-tuning-it "Link to this heading")

In the previous example, we used the [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV")
 to find the optimal decision threshold. However, in some cases, we might have some prior knowledge about the problem at hand and we might be happy to set the decision threshold manually.

The class [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
 allows us to manually set the decision threshold. At prediction time, it behave as the previous tuned model but no search is performed during the fitting process. Note that here we use [`FrozenEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
 to wrap the predictive model to avoid any refitting.

Here, we will reuse the decision threshold found in the previous section to create a new model and check that it gives the same results.

from sklearn.frozen import [FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
from sklearn.model\_selection import [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")

model\_fixed\_threshold \= [FixedThresholdClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")
(
    estimator\=[FrozenEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.frozen.FrozenEstimator.html#sklearn.frozen.FrozenEstimator "sklearn.frozen.FrozenEstimator")
(model), threshold\=tuned\_model.best\_threshold\_
)

Copy to clipboard

business\_score \= business\_scorer(
    model\_fixed\_threshold, data\_test, target\_test, amount\=amount\_test
)
print(f"Benefit of logistic regression with a tuned threshold:  {business\_score:,.2f}€")

Copy to clipboard

Benefit of logistic regression with a tuned threshold:  249,433.39€

Copy to clipboard

We observe that we obtained the exact same results but the fitting process was much faster since we did not perform any hyper-parameter search.

Finally, the estimate of the (average) business metric itself can be unreliable, in particular when the number of data points in the minority class is very small. Any business impact estimated by cross-validation of a business metric on historical data (offline evaluation) should ideally be confirmed by A/B testing on live data (online evaluation). Note however that A/B testing models is beyond the scope of the scikit-learn library itself.

At the end, we disable the configuration flag for metadata routing:

[sklearn.set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(enable\_metadata\_routing\=False)

Copy to clipboard

**Total running time of the script:** (0 minutes 22.343 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_cost_sensitive_learning.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_cost_sensitive_learning.ipynb)

[`Download Jupyter notebook: plot_cost_sensitive_learning.ipynb`](https://scikit-learn.org/stable/_downloads/133f2198d3ab792c75b39a63b0a99872/plot_cost_sensitive_learning.ipynb)

[`Download Python source code: plot_cost_sensitive_learning.py`](https://scikit-learn.org/stable/_downloads/9ca7cbe47e4cace7242fe4c5c43dfa52/plot_cost_sensitive_learning.py)

[`Download zipped: plot_cost_sensitive_learning.zip`](https://scikit-learn.org/stable/_downloads/c75a28fb9c5813c4fe15345695d1bdcf/plot_cost_sensitive_learning.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_tuned_decision_threshold_thumb.png)

[Post-hoc tuning the cut-off point of decision function](https://scikit-learn.org/stable/auto_examples/model_selection/plot_tuned_decision_threshold.html)

Post-hoc tuning the cut-off point of decision function

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_5_0_thumb.png)

[Release Highlights for scikit-learn 1.5](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_5_0.html)

Release Highlights for scikit-learn 1.5

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_digits_thumb.png)

[Custom refit strategy of a grid search with cross-validation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html)

Custom refit strategy of a grid search with cross-validation

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/9ca7cbe47e4cace7242fe4c5c43dfa52/plot_cost_sensitive_learning.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/133f2198d3ab792c75b39a63b0a99872/plot_cost_sensitive_learning.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/c75a28fb9c5813c4fe15345695d1bdcf/plot_cost_sensitive_learning.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_cost_sensitive_learning.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_cost_sensitive_learning.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)