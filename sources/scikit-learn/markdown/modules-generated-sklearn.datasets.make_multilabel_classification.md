[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_multilabel_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_multilabel_classification.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_multilabel_classification.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_multilabel_classification.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_multilabel_classification.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_multilabel_classification.html)

Collapse Sidebar Expand Sidebar

make\_multilabel\_classification[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#make-multilabel-classification "Link to this heading")

==================================================================================================================================================================================================

sklearn.datasets.make\_multilabel\_classification(_n\_samples\=100_, _n\_features\=20_, _\*_, _n\_classes\=5_, _n\_labels\=2_, _length\=50_, _allow\_unlabeled\=True_, _sparse\=False_, _return\_indicator\='dense'_, _return\_distributions\=False_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L390)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "Link to this definition")

Generate a random multilabel classification problem.

For each sample, the generative process is:

*   pick the number of labels: n ~ Poisson(n\_labels)
    
*   n times, choose a class c: c ~ Multinomial(theta)
    
*   pick the document length: k ~ Poisson(length)
    
*   k times, choose a word: w ~ Multinomial(theta\_c)
    

In the above process, rejection sampling is used to make sure that n is never zero or more than `n_classes`, and that the document length is never zero. Likewise, we reject classes which have already been chosen.

For an example of usage, see [Plot randomly generated multilabel dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html#sphx-glr-auto-examples-datasets-plot-random-multilabel-dataset-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int, default=100

The number of samples.

**n\_features**int, default=20

The total number of features.

**n\_classes**int, default=5

The number of classes of the classification problem.

**n\_labels**int, default=2

The average number of labels per instance. More precisely, the number of labels per sample is drawn from a Poisson distribution with `n_labels` as its expected value, but samples are bounded (using rejection sampling) by `n_classes`, and must be nonzero if `allow_unlabeled` is False.

**length**int, default=50

The sum of the features (number of words if documents) is drawn from a Poisson distribution with this expected value.

**allow\_unlabeled**bool, default=True

If `True`, some instances might not belong to any class.

**sparse**bool, default=False

If `True`, return a sparse feature matrix.

Added in version 0.17: parameter to allow _sparse_ output.

**return\_indicator**{‘dense’, ‘sparse’} or False, default=’dense’

If `'dense'` return `Y` in the dense binary indicator format. If `'sparse'` return `Y` in the sparse binary indicator format. `False` returns a list of lists of labels.

**return\_distributions**bool, default=False

If `True`, return the prior class probability and conditional probabilities of features given classes, from which the data was drawn.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**X**ndarray of shape (n\_samples, n\_features)

The generated samples.

**Y**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

The label sets. Sparse matrix should be of CSR format.

**p\_c**ndarray of shape (n\_classes,)

The probability of each class being drawn. Only returned if `return_distributions=True`.

**p\_w\_c**ndarray of shape (n\_features, n\_classes)

The probability of each feature being drawn given each class. Only returned if `return_distributions=True`.

Examples

\>>> from sklearn.datasets import make\_multilabel\_classification
\>>> X, y \= make\_multilabel\_classification(n\_labels\=3, random\_state\=42)
\>>> X.shape
(100, 20)
\>>> y.shape
(100, 5)
\>>> list(y\[:3\])
\[array(\[1, 1, 0, 1, 0\]), array(\[0, 1, 1, 1, 0\]), array(\[0, 1, 0, 0, 0\])\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_multilabel_dataset_thumb.png)

[Plot randomly generated multilabel dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html)

Plot randomly generated multilabel dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_thumb.png)

[Multilabel classification](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)

Multilabel classification

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)