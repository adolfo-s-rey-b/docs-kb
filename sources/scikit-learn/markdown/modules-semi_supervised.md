[Skip to main content](https://scikit-learn.org/stable/modules/semi_supervised.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/semi_supervised.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/semi_supervised.html)
[1.8.0](https://scikit-learn.org/1.8/modules/semi_supervised.html)
[1.7.2](https://scikit-learn.org/1.7/modules/semi_supervised.html)
[1.6.1](https://scikit-learn.org/1.6/modules/semi_supervised.html)
[1.5.2](https://scikit-learn.org/1.5/modules/semi_supervised.html)
[1.4.2](https://scikit-learn.org/1.4/modules/semi_supervised.html)

Collapse Sidebar Expand Sidebar

1.14. Semi-supervised learning[#](https://scikit-learn.org/stable/modules/semi_supervised.html#semi-supervised-learning "Link to this heading")

================================================================================================================================================

[Semi-supervised learning](https://en.wikipedia.org/wiki/Semi-supervised_learning)
 is a situation in which in your training data some of the samples are not labeled. The semi-supervised estimators in [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")
 are able to make use of this additional unlabeled data to better capture the shape of the underlying data distribution and generalize better to new samples. These algorithms can perform well when we have a very small amount of labeled points and a large amount of unlabeled points.

Note

Semi-supervised algorithms need to make assumptions about the distribution of the dataset in order to achieve performance gains. See [here](https://en.wikipedia.org/wiki/Semi-supervised_learning#Assumptions)
 for more details.

Examples

*   [Semi-supervised Classification on a Text Dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html#sphx-glr-auto-examples-semi-supervised-plot-semi-supervised-newsgroups-py)
    

1.14.1. Self Training[#](https://scikit-learn.org/stable/modules/semi_supervised.html#self-training "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

This self-training implementation is based on Yarowsky’s [\[1\]](https://scikit-learn.org/stable/modules/semi_supervised.html#id4)
 algorithm. Using this algorithm, a given supervised classifier can function as a semi-supervised classifier, allowing it to learn from unlabeled data.

[`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
 can be called with any classifier that implements `predict_proba`, passed as the parameter `estimator`. In each iteration, the `estimator` predicts labels for the unlabeled samples and adds a subset of these labels to the labeled dataset.

The choice of this subset is determined by the selection criterion. This selection can be done using a `threshold` on the prediction probabilities, or by choosing the `k_best` samples according to the prediction probabilities.

The labels used for the final fit as well as the iteration in which each sample was labeled are available as attributes. The optional `max_iter` parameter specifies how many times the loop is executed at most.

The `max_iter` parameter may be set to `None`, causing the algorithm to iterate until all samples have labels or no new samples are selected in that iteration.

Note

When using the self-training classifier, the [calibration](https://scikit-learn.org/stable/modules/calibration.html#calibration)
 of the classifier is important.

Examples

*   [Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html#sphx-glr-auto-examples-semi-supervised-plot-self-training-varying-threshold-py)
    
*   [Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#sphx-glr-auto-examples-semi-supervised-plot-semi-supervised-versus-svm-iris-py)
    

References

1.14.2. Label Propagation[#](https://scikit-learn.org/stable/modules/semi_supervised.html#label-propagation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Label propagation denotes a few variations of semi-supervised graph inference algorithms.

A few features available in this model:

*   Used for classification tasks
    
*   Kernel methods to project data into alternate dimensional spaces
    

`scikit-learn` provides two label propagation models: [`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
 and [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
. Both work by constructing a similarity graph over all items in the input dataset.

[![../_images/sphx_glr_plot_label_propagation_structure_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_structure_001.png)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_structure.html)

**An illustration of label-propagation:** _the structure of unlabeled observations is consistent with the class structure, and thus the class label can be propagated to the unlabeled observations of the training set._[#](https://scikit-learn.org/stable/modules/semi_supervised.html#id6 "Link to this image")

[`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
 and [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 differ in modifications to the similarity matrix that graph and the clamping effect on the label distributions. Clamping allows the algorithm to change the weight of the true ground labeled data to some degree. The [`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
 algorithm performs hard clamping of input labels, which means α\=0. This clamping factor can be relaxed, to say α\=0.2, which means that we will always retain 80 percent of our original label distribution, but the algorithm gets to change its confidence of the distribution within 20 percent.

[`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
 uses the raw similarity matrix constructed from the data with no modifications. In contrast, [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 minimizes a loss function that has regularization properties, as such it is often more robust to noise. The algorithm iterates on a modified version of the original graph and normalizes the edge weights by computing the normalized graph Laplacian matrix. This procedure is also used in [Spectral clustering](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering)
.

Label propagation models have two built-in kernel methods. Choice of kernel affects both scalability and performance of the algorithms. The following are available:

*   rbf (exp⁡(−γ|x−y|2),γ\>0). γ is specified by keyword gamma.
    
*   knn (1\[x′∈kNN(x)\]). k is specified by keyword n\_neighbors.
    

The RBF kernel will produce a fully connected graph which is represented in memory by a dense matrix. This matrix may be very large and combined with the cost of performing a full matrix multiplication calculation for each iteration of the algorithm can lead to prohibitively long running times. On the other hand, the KNN kernel will produce a much more memory-friendly sparse matrix which can drastically reduce running times.

Examples

*   [Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html#sphx-glr-auto-examples-semi-supervised-plot-semi-supervised-versus-svm-iris-py)
    
*   [Label Propagation circles: Learning a complex structure](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_structure.html#sphx-glr-auto-examples-semi-supervised-plot-label-propagation-structure-py)
    
*   [Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#sphx-glr-auto-examples-semi-supervised-plot-label-propagation-digits-py)
    
*   [Label Propagation digits: Active learning](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html#sphx-glr-auto-examples-semi-supervised-plot-label-propagation-digits-active-learning-py)
    

References

\[2\] Yoshua Bengio, Olivier Delalleau, Nicolas Le Roux. In Semi-Supervised Learning (2006), pp. 193-216

\[3\] Olivier Delalleau, Yoshua Bengio, Nicolas Le Roux. Efficient Non-Parametric Function Induction in Semi-Supervised Learning. AISTAT 2005 [https://www.gatsby.ucl.ac.uk/aistats/fullpapers/204.pdf](https://www.gatsby.ucl.ac.uk/aistats/fullpapers/204.pdf)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)