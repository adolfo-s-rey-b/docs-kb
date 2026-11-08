[Skip to main content](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/semi_supervised/plot_label_propagation_digits.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/semi_supervised/plot_label_propagation_digits.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/semi_supervised/plot_label_propagation_digits.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/semi_supervised/plot_label_propagation_digits.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/semi_supervised/plot_label_propagation_digits.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#sphx-glr-download-auto-examples-semi-supervised-plot-label-propagation-digits-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Label Propagation digits: Demonstrating performance[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#label-propagation-digits-demonstrating-performance "Link to this heading")

===================================================================================================================================================================================================================================

This example demonstrates the power of semisupervised learning by training a Label Spreading model to classify handwritten digits with sets of very few labels.

The handwritten digit dataset has 1797 total points. The model will be trained using all points, but only 30 will be labeled. Results in the form of a confusion matrix and a series of metrics over each class will be very good.

At the end, the top 10 most uncertain predictions will be shown.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data generation[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#data-generation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

We use the digits dataset. We only use a subset of randomly selected samples.

import numpy as np

from sklearn import datasets

digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(2)
indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(digits.data))
rng.shuffle(indices)

Copy to clipboard

We selected 340 samples of which only 40 will be associated with a known label. Therefore, we store the indices of the 300 other samples for which we are not supposed to know their labels.

X \= digits.data\[indices\[:340\]\]
y \= digits.target\[indices\[:340\]\]
images \= digits.images\[indices\[:340\]\]

n\_total\_samples \= len(y)
n\_labeled\_points \= 40

indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_total\_samples)

unlabeled\_set \= indices\[n\_labeled\_points:\]

Copy to clipboard

Shuffle everything around

y\_train \= [np.copy](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
(y)
y\_train\[unlabeled\_set\] \= \-1

Copy to clipboard

Semi-supervised learning[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#semi-supervised-learning "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We fit a [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
 and use it to predict the unknown labels.

from sklearn.metrics import [classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
from sklearn.semi\_supervised import [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")

lp\_model \= [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
(gamma\=0.25, max\_iter\=20)
lp\_model.fit(X, y\_train)
predicted\_labels \= lp\_model.transduction\_\[unlabeled\_set\]
true\_labels \= y\[unlabeled\_set\]

print(
    "Label Spreading model: %d labeled & %d unlabeled points (%d total)"
    % (n\_labeled\_points, n\_total\_samples \- n\_labeled\_points, n\_total\_samples)
)

Copy to clipboard

Label Spreading model: 40 labeled & 300 unlabeled points (340 total)

Copy to clipboard

Classification report

print([classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(true\_labels, predicted\_labels))

Copy to clipboard

              precision    recall  f1-score   support

           0       1.00      1.00      1.00        27
           1       0.82      1.00      0.90        37
           2       1.00      0.86      0.92        28
           3       1.00      0.80      0.89        35
           4       0.92      1.00      0.96        24
           5       0.74      0.94      0.83        34
           6       0.89      0.96      0.92        25
           7       0.94      0.89      0.91        35
           8       1.00      0.68      0.81        31
           9       0.81      0.88      0.84        24

    accuracy                           0.90       300
   macro avg       0.91      0.90      0.90       300
weighted avg       0.91      0.90      0.90       300

Copy to clipboard

Confusion matrix

from sklearn.metrics import ConfusionMatrixDisplay

[ConfusionMatrixDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
(
    true\_labels, predicted\_labels, labels\=lp\_model.classes\_
)

Copy to clipboard

![plot label propagation digits](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_001.png)

<sklearn.metrics.\_plot.confusion\_matrix.ConfusionMatrixDisplay object at 0x7e1d3ccf1370>

Copy to clipboard

Plot the most uncertain predictions[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html#plot-the-most-uncertain-predictions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here, we will pick and show the 10 most uncertain predictions.

from scipy import stats

pred\_entropies \= [stats.distributions.entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html#scipy.stats.entropy "scipy.stats.entropy")
(lp\_model.label\_distributions\_.T)

Copy to clipboard

Pick the top 10 most uncertain labels

uncertainty\_index \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(pred\_entropies)\[\-10:\]

Copy to clipboard

Plot

import matplotlib.pyplot as plt

f \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 5))
for index, image\_index in enumerate(uncertainty\_index):
    image \= images\[image\_index\]

    sub \= f.add\_subplot(2, 5, index + 1)
    sub.imshow(image, cmap\=plt.cm.gray\_r)
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(\[\])
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(\[\])
    sub.set\_title(
        "predict: %i\\ntrue: %i" % (lp\_model.transduction\_\[image\_index\], y\[image\_index\])
    )

f.suptitle("Learning with small amount of labeled data")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Learning with small amount of labeled data, predict: 1 true: 2, predict: 2 true: 2, predict: 8 true: 8, predict: 1 true: 8, predict: 1 true: 8, predict: 1 true: 8, predict: 3 true: 3, predict: 8 true: 8, predict: 2 true: 2, predict: 7 true: 2](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_002.png)

**Total running time of the script:** (0 minutes 0.321 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_label_propagation_digits.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_label_propagation_digits.ipynb)

[`Download Jupyter notebook: plot_label_propagation_digits.ipynb`](https://scikit-learn.org/stable/_downloads/22bab9f5303a6f1be42d14efb0f90b40/plot_label_propagation_digits.ipynb)

[`Download Python source code: plot_label_propagation_digits.py`](https://scikit-learn.org/stable/_downloads/fb13b4879e1cc9657e76544444ca7197/plot_label_propagation_digits.py)

[`Download zipped: plot_label_propagation_digits.zip`](https://scikit-learn.org/stable/_downloads/388f5c580f2084392fb899ca1bc53867/plot_label_propagation_digits.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_active_learning_thumb.png)

[Label Propagation digits: Active learning](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)

Label Propagation digits: Active learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/fb13b4879e1cc9657e76544444ca7197/plot_label_propagation_digits.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/22bab9f5303a6f1be42d14efb0f90b40/plot_label_propagation_digits.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/388f5c580f2084392fb899ca1bc53867/plot_label_propagation_digits.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_label_propagation_digits.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_label_propagation_digits.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)