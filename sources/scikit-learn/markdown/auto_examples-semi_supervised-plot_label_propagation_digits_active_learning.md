[Skip to main content](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html#sphx-glr-download-auto-examples-semi-supervised-plot-label-propagation-digits-active-learning-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Label Propagation digits: Active learning[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html#label-propagation-digits-active-learning "Link to this heading")

===============================================================================================================================================================================================================================

Demonstrates an active learning technique to learn handwritten digits using label propagation.

We start by training a label propagation model with only 10 labeled points, then we select the top five most uncertain points to label. Next, we train with 15 labeled points (original 10 + 5 new ones). We repeat this process four times to have a model trained with 30 labeled examples. Note you can increase this to label more than 30 by changing `max_iterations`. Labeling more than 30 can be useful to get a sense for the speed of convergence of this active learning technique.

A plot will appear showing the top 5 most uncertain digits for each iteration of training. These may or may not contain mistakes, but we will train the next model with their true labels.

![Active learning with Label Propagation. Rows show 5 most uncertain labels to learn with the next model., predict: 1 true: 1, predict: 2 true: 1, predict: 1 true: 1, predict: 1 true: 1, predict: 3 true: 3, predict: 4 true: 4, predict: 4 true: 4, predict: 4 true: 4, predict: 8 true: 2, predict: 8 true: 7, predict: 2 true: 2, predict: 9 true: 5, predict: 9 true: 5, predict: 5 true: 9, predict: 7 true: 7, predict: 8 true: 8, predict: 1 true: 8, predict: 3 true: 3, predict: 4 true: 4, predict: 8 true: 8, predict: 1 true: 1, predict: 1 true: 1, predict: 7 true: 7, predict: 7 true: 7, predict: 1 true: 1](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_active_learning_001.png)

Iteration 0 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Label Spreading model: 40 labeled & 290 unlabeled (330 total)
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        22
           1       0.78      0.69      0.73        26
           2       0.93      0.93      0.93        29
           3       1.00      0.89      0.94        27
           4       0.92      0.96      0.94        23
           5       0.96      0.70      0.81        33
           6       0.97      0.97      0.97        35
           7       0.94      0.91      0.92        33
           8       0.62      0.89      0.74        28
           9       0.73      0.79      0.76        34

    accuracy                           0.87       290
   macro avg       0.89      0.87      0.87       290
weighted avg       0.88      0.87      0.87       290

Confusion matrix
\[\[22  0  0  0  0  0  0  0  0  0\]\
 \[ 0 18  2  0  0  0  1  0  5  0\]\
 \[ 0  0 27  0  0  0  0  0  2  0\]\
 \[ 0  0  0 24  0  0  0  0  3  0\]\
 \[ 0  1  0  0 22  0  0  0  0  0\]\
 \[ 0  0  0  0  0 23  0  0  0 10\]\
 \[ 0  1  0  0  0  0 34  0  0  0\]\
 \[ 0  0  0  0  0  0  0 30  3  0\]\
 \[ 0  3  0  0  0  0  0  0 25  0\]\
 \[ 0  0  0  0  2  1  0  2  2 27\]\]
Iteration 1 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Label Spreading model: 45 labeled & 285 unlabeled (330 total)
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        22
           1       0.79      1.00      0.88        22
           2       1.00      0.93      0.96        29
           3       1.00      1.00      1.00        26
           4       0.92      0.96      0.94        23
           5       0.96      0.70      0.81        33
           6       1.00      0.97      0.99        35
           7       0.94      0.91      0.92        33
           8       0.77      0.86      0.81        28
           9       0.73      0.79      0.76        34

    accuracy                           0.90       285
   macro avg       0.91      0.91      0.91       285
weighted avg       0.91      0.90      0.90       285

Confusion matrix
\[\[22  0  0  0  0  0  0  0  0  0\]\
 \[ 0 22  0  0  0  0  0  0  0  0\]\
 \[ 0  0 27  0  0  0  0  0  2  0\]\
 \[ 0  0  0 26  0  0  0  0  0  0\]\
 \[ 0  1  0  0 22  0  0  0  0  0\]\
 \[ 0  0  0  0  0 23  0  0  0 10\]\
 \[ 0  1  0  0  0  0 34  0  0  0\]\
 \[ 0  0  0  0  0  0  0 30  3  0\]\
 \[ 0  4  0  0  0  0  0  0 24  0\]\
 \[ 0  0  0  0  2  1  0  2  2 27\]\]
Iteration 2 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Label Spreading model: 50 labeled & 280 unlabeled (330 total)
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        22
           1       0.85      1.00      0.92        22
           2       1.00      1.00      1.00        28
           3       1.00      1.00      1.00        26
           4       0.87      1.00      0.93        20
           5       0.96      0.70      0.81        33
           6       1.00      0.97      0.99        35
           7       0.94      1.00      0.97        32
           8       0.92      0.86      0.89        28
           9       0.73      0.79      0.76        34

    accuracy                           0.92       280
   macro avg       0.93      0.93      0.93       280
weighted avg       0.93      0.92      0.92       280

Confusion matrix
\[\[22  0  0  0  0  0  0  0  0  0\]\
 \[ 0 22  0  0  0  0  0  0  0  0\]\
 \[ 0  0 28  0  0  0  0  0  0  0\]\
 \[ 0  0  0 26  0  0  0  0  0  0\]\
 \[ 0  0  0  0 20  0  0  0  0  0\]\
 \[ 0  0  0  0  0 23  0  0  0 10\]\
 \[ 0  1  0  0  0  0 34  0  0  0\]\
 \[ 0  0  0  0  0  0  0 32  0  0\]\
 \[ 0  3  0  0  1  0  0  0 24  0\]\
 \[ 0  0  0  0  2  1  0  2  2 27\]\]
Iteration 3 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Label Spreading model: 55 labeled & 275 unlabeled (330 total)
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        22
           1       0.85      1.00      0.92        22
           2       1.00      1.00      1.00        27
           3       1.00      1.00      1.00        26
           4       0.87      1.00      0.93        20
           5       0.96      0.87      0.92        31
           6       1.00      0.97      0.99        35
           7       1.00      1.00      1.00        31
           8       0.92      0.86      0.89        28
           9       0.88      0.85      0.86        33

    accuracy                           0.95       275
   macro avg       0.95      0.95      0.95       275
weighted avg       0.95      0.95      0.95       275

Confusion matrix
\[\[22  0  0  0  0  0  0  0  0  0\]\
 \[ 0 22  0  0  0  0  0  0  0  0\]\
 \[ 0  0 27  0  0  0  0  0  0  0\]\
 \[ 0  0  0 26  0  0  0  0  0  0\]\
 \[ 0  0  0  0 20  0  0  0  0  0\]\
 \[ 0  0  0  0  0 27  0  0  0  4\]\
 \[ 0  1  0  0  0  0 34  0  0  0\]\
 \[ 0  0  0  0  0  0  0 31  0  0\]\
 \[ 0  3  0  0  1  0  0  0 24  0\]\
 \[ 0  0  0  0  2  1  0  0  2 28\]\]
Iteration 4 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Label Spreading model: 60 labeled & 270 unlabeled (330 total)
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        22
           1       0.96      1.00      0.98        22
           2       1.00      0.96      0.98        27
           3       0.96      1.00      0.98        25
           4       0.86      1.00      0.93        19
           5       0.96      0.87      0.92        31
           6       1.00      0.97      0.99        35
           7       1.00      1.00      1.00        31
           8       0.92      0.96      0.94        25
           9       0.88      0.85      0.86        33

    accuracy                           0.96       270
   macro avg       0.95      0.96      0.96       270
weighted avg       0.96      0.96      0.96       270

Confusion matrix
\[\[22  0  0  0  0  0  0  0  0  0\]\
 \[ 0 22  0  0  0  0  0  0  0  0\]\
 \[ 0  0 26  1  0  0  0  0  0  0\]\
 \[ 0  0  0 25  0  0  0  0  0  0\]\
 \[ 0  0  0  0 19  0  0  0  0  0\]\
 \[ 0  0  0  0  0 27  0  0  0  4\]\
 \[ 0  1  0  0  0  0 34  0  0  0\]\
 \[ 0  0  0  0  0  0  0 31  0  0\]\
 \[ 0  0  0  0  1  0  0  0 24  0\]\
 \[ 0  0  0  0  2  1  0  0  2 28\]\]

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from sklearn import datasets
from sklearn.metrics import [classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
, [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
from sklearn.semi\_supervised import [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")

digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(digits.data))
rng.shuffle(indices)

X \= digits.data\[indices\[:330\]\]
y \= digits.target\[indices\[:330\]\]
images \= digits.images\[indices\[:330\]\]

n\_total\_samples \= len(y)
n\_labeled\_points \= 40
max\_iterations \= 5

unlabeled\_indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(n\_total\_samples)\[n\_labeled\_points:\]
f \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()

for i in range(max\_iterations):
    if len(unlabeled\_indices) \== 0:
        print("No unlabeled items left to label.")
        break
    y\_train \= [np.copy](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
(y)
    y\_train\[unlabeled\_indices\] \= \-1

    lp\_model \= [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
(gamma\=0.25, max\_iter\=20)
    lp\_model.fit(X, y\_train)

    predicted\_labels \= lp\_model.transduction\_\[unlabeled\_indices\]
    true\_labels \= y\[unlabeled\_indices\]

    cm \= [confusion\_matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
(true\_labels, predicted\_labels, labels\=lp\_model.classes\_)

    print("Iteration %i %s" % (i, 70 \* "\_"))
    print(
        "Label Spreading model: %d labeled & %d unlabeled (%d total)"
        % (n\_labeled\_points, n\_total\_samples \- n\_labeled\_points, n\_total\_samples)
    )

    print([classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(true\_labels, predicted\_labels))

    print("Confusion matrix")
    print(cm)

    \# compute the entropies of transduced label distributions
    pred\_entropies \= [stats.distributions.entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html#scipy.stats.entropy "scipy.stats.entropy")
(lp\_model.label\_distributions\_.T)

    \# select up to 5 digit examples that the classifier is most uncertain about
    uncertainty\_index \= [np.argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")
(pred\_entropies)\[::\-1\]
    uncertainty\_index \= uncertainty\_index\[\
        [np.isin](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "numpy.isin")\
(uncertainty\_index, unlabeled\_indices)\
    \]\[:5\]

    \# keep track of indices that we get labels for
    delete\_indices \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\], dtype\=int)

    \# for more than 5 iterations, visualize the gain only on the first 5
    if i < 5:
        f.text(
            0.05,
            (1 \- (i + 1) \* 0.183),
            "model %d\\n\\nfit with\\n%d labels" % ((i + 1), i \* 5 + 10),
            size\=10,
        )
    for index, image\_index in enumerate(uncertainty\_index):
        image \= images\[image\_index\]

        \# for more than 5 iterations, visualize the gain only on the first 5
        if i < 5:
            sub \= f.add\_subplot(5, 5, index + 1 + (5 \* i))
            sub.imshow(image, cmap\=plt.cm.gray\_r, interpolation\="none")
            sub.set\_title(
                "predict: %i\\ntrue: %i"
                % (lp\_model.transduction\_\[image\_index\], y\[image\_index\]),
                size\=10,
            )
            sub.axis("off")

        \# labeling 5 points, remote from labeled set
        (delete\_index,) \= (unlabeled\_indices \== image\_index).nonzero()
        delete\_indices \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((delete\_indices, delete\_index))

    unlabeled\_indices \= [np.delete](https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy.delete "numpy.delete")
(unlabeled\_indices, delete\_indices)
    n\_labeled\_points += len(uncertainty\_index)

f.suptitle(
    (
        "Active learning with Label Propagation.\\nRows show 5 most "
        "uncertain labels to learn with the next model."
    ),
    y\=1.15,
)
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(left\=0.2, bottom\=0.03, right\=0.9, top\=0.9, wspace\=0.2, hspace\=0.85)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.485 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.ipynb)

[`Download Jupyter notebook: plot_label_propagation_digits_active_learning.ipynb`](https://scikit-learn.org/stable/_downloads/a72c1f35af8f7695645ce87422b177bf/plot_label_propagation_digits_active_learning.ipynb)

[`Download Python source code: plot_label_propagation_digits_active_learning.py`](https://scikit-learn.org/stable/_downloads/0dd5e0a7942f1446accf7dffd47aed28/plot_label_propagation_digits_active_learning.py)

[`Download zipped: plot_label_propagation_digits_active_learning.zip`](https://scikit-learn.org/stable/_downloads/4dcec41c6039a7291948a1846cd34240/plot_label_propagation_digits_active_learning.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/0dd5e0a7942f1446accf7dffd47aed28/plot_label_propagation_digits_active_learning.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a72c1f35af8f7695645ce87422b177bf/plot_label_propagation_digits_active_learning.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4dcec41c6039a7291948a1846cd34240/plot_label_propagation_digits_active_learning.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)