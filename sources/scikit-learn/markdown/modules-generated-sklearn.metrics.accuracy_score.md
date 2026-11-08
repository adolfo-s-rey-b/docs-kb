[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.accuracy_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.accuracy_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.accuracy_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.accuracy_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.accuracy_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.accuracy_score.html)

Collapse Sidebar Expand Sidebar

accuracy\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#accuracy-score "Link to this heading")

================================================================================================================================================

sklearn.metrics.accuracy\_score(_y\_true_, _y\_pred_, _\*_, _normalize\=True_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_classification.py#L331)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "Link to this definition")

Accuracy classification score.

In multilabel classification, this function computes subset accuracy: the set of labels predicted for a sample must _exactly_ match the corresponding set of labels in y\_true.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)
.

Parameters:

**y\_true**1d array-like, or label indicator array / sparse matrix

Ground truth (correct) labels. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**y\_pred**1d array-like, or label indicator array / sparse matrix

Predicted labels, as returned by a classifier. Sparse matrix is only supported when labels are of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 type.

**normalize**bool, default=True

If `False`, return the number of correctly classified samples. Otherwise, return the fraction of correctly classified samples.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights.

Returns:

**score**float

If `normalize == True`, returns the fraction of correctly classified samples, else returns the number of correctly classified samples.

The best performance is 1.0 with `normalize == True` and the number of samples with `normalize == False`.

See also

[`balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score")

Compute the balanced accuracy to deal with imbalanced datasets.

[`jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")

Compute the Jaccard similarity coefficient score.

[`hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")

Compute the average Hamming loss or Hamming distance between two sets of samples.

[`zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")

Compute the Zero-one classification loss. By default, the function will return the percentage of imperfectly predicted subsets.

Examples

\>>> from sklearn.metrics import accuracy\_score
\>>> y\_pred \= \[0, 2, 1, 3\]
\>>> y\_true \= \[0, 1, 2, 3\]
\>>> accuracy\_score(y\_true, y\_pred)
0.5
\>>> accuracy\_score(y\_true, y\_pred, normalize\=False)
2.0

Copy to clipboard

In the multilabel case with binary label indicators:

\>>> import numpy as np
\>>> accuracy\_score(np.array(\[\[0, 1\], \[1, 1\]\]), np.ones((2, 2)))
0.5

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_multiclass_thumb.png)

[Multi-class AdaBoosted Decision Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_adaboost_multiclass.html)

Multi-class AdaBoosted Decision Trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_thumb.png)

[Probabilistic predictions with Gaussian process classification (GPC)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc.html)

Probabilistic predictions with Gaussian process classification (GPC)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_metric_evaluation_thumb.png)

[Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html)

Demonstration of multi-metric evaluation on cross\_val\_score and GridSearchCV

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_9_0_thumb.png)

[Release Highlights for scikit-learn 1.9](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_9_0.html)

Release Highlights for scikit-learn 1.9

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)