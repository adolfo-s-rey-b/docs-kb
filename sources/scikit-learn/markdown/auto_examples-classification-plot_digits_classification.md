[Skip to main content](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/classification/plot_digits_classification.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/classification/plot_digits_classification.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/classification/plot_digits_classification.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/classification/plot_digits_classification.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/classification/plot_digits_classification.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/classification/plot_digits_classification.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#sphx-glr-download-auto-examples-classification-plot-digits-classification-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Recognizing hand-written digits[#](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#recognizing-hand-written-digits "Link to this heading")

========================================================================================================================================================================================

This example shows how scikit-learn can be used to recognize images of hand-written digits, from 0-9.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

\# Standard scientific Python imports
import matplotlib.pyplot as plt

\# Import datasets, classifiers and performance metrics
from sklearn import datasets, metrics, svm
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

Copy to clipboard

Digits dataset[#](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#digits-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

The digits dataset consists of 8x8 pixel images of digits. The `images` attribute of the dataset stores 8x8 arrays of grayscale values for each image. We will use these arrays to visualize the first 4 images. The `target` attribute of the dataset stores the digit each image represents and this is included in the title of the 4 plots below.

Note: if we were working from image files (e.g., ‘png’ files), we would load them using [`matplotlib.pyplot.imread`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "(in Matplotlib v3.11.1)")
.

digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()

\_, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=4, figsize\=(10, 3))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set\_axis\_off()
    ax.imshow(image, cmap\=plt.cm.gray\_r, interpolation\="nearest")
    ax.set\_title("Training: %i" % label)

Copy to clipboard

![Training: 0, Training: 1, Training: 2, Training: 3](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_001.png)

Classification[#](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html#classification "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

To apply a classifier on this data, we need to flatten the images, turning each 2-D array of grayscale values from shape `(8, 8)` into shape `(64,)`. Subsequently, the entire dataset will be of shape `(n_samples, n_features)`, where `n_samples` is the number of images and `n_features` is the total number of pixels in each image.

We can then split the data into train and test subsets and fit a support vector classifier on the train samples. The fitted classifier can subsequently be used to predict the value of the digit for the samples in the test subset.

\# flatten the images
n\_samples \= len(digits.images)
data \= digits.images.reshape((n\_samples, \-1))

\# Create a classifier: a support vector classifier
clf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(gamma\=0.001)

\# Split data into 50% train and 50% test subsets
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    data, digits.target, test\_size\=0.5, shuffle\=False
)

\# Learn the digits on the train subset
clf.fit(X\_train, y\_train)

\# Predict the value of the digit on the test subset
predicted \= clf.predict(X\_test)

Copy to clipboard

Below we visualize the first 4 test samples and show their predicted digit value in the title.

\_, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=4, figsize\=(10, 3))
for ax, image, prediction in zip(axes, X\_test, predicted):
    ax.set\_axis\_off()
    image \= image.reshape(8, 8)
    ax.imshow(image, cmap\=plt.cm.gray\_r, interpolation\="nearest")
    ax.set\_title(f"Prediction: {prediction}")

Copy to clipboard

![Prediction: 8, Prediction: 8, Prediction: 4, Prediction: 9](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_002.png)

[`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
 builds a text report showing the main classification metrics.

print(
    f"Classification report for classifier {clf}:\\n"
    f"{[metrics.classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(y\_test, predicted)}\\n"
)

Copy to clipboard

Classification report for classifier SVC(gamma=0.001):
              precision    recall  f1-score   support

           0       1.00      0.99      0.99        88
           1       0.99      0.97      0.98        91
           2       0.99      0.99      0.99        86
           3       0.98      0.87      0.92        91
           4       0.99      0.96      0.97        92
           5       0.95      0.97      0.96        91
           6       0.99      0.99      0.99        91
           7       0.96      0.99      0.97        89
           8       0.94      1.00      0.97        88
           9       0.93      0.98      0.95        92

    accuracy                           0.97       899
   macro avg       0.97      0.97      0.97       899
weighted avg       0.97      0.97      0.97       899

Copy to clipboard

We can also plot a [confusion matrix](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
 of the true digit values and the predicted digit values.

disp \= [metrics.ConfusionMatrixDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay.from_predictions "sklearn.metrics.ConfusionMatrixDisplay.from_predictions")
(y\_test, predicted)
disp.figure\_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\\n{disp.confusion\_matrix}")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Confusion Matrix](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_003.png)

Confusion matrix:
\[\[87  0  0  0  1  0  0  0  0  0\]\
 \[ 0 88  1  0  0  0  0  0  1  1\]\
 \[ 0  0 85  1  0  0  0  0  0  0\]\
 \[ 0  0  0 79  0  3  0  4  5  0\]\
 \[ 0  0  0  0 88  0  0  0  0  4\]\
 \[ 0  0  0  0  0 88  1  0  0  2\]\
 \[ 0  1  0  0  0  0 90  0  0  0\]\
 \[ 0  0  0  0  0  1  0 88  0  0\]\
 \[ 0  0  0  0  0  0  0  0 88  0\]\
 \[ 0  0  0  1  0  1  0  0  0 90\]\]

Copy to clipboard

If the results from evaluating a classifier are stored in the form of a [confusion matrix](https://scikit-learn.org/stable/modules/model_evaluation.html#confusion-matrix)
 and not in terms of `y_true` and `y_pred`, one can still build a [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
 as follows:

\# The ground truth and predicted lists
y\_true \= \[\]
y\_pred \= \[\]
cm \= disp.confusion\_matrix

\# For each cell in the confusion matrix, add the corresponding ground truths
\# and predictions to the lists
for gt in range(len(cm)):
    for pred in range(len(cm)):
        y\_true += \[gt\] \* cm\[gt\]\[pred\]
        y\_pred += \[pred\] \* cm\[gt\]\[pred\]

print(
    "Classification report rebuilt from confusion matrix:\\n"
    f"{[metrics.classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(y\_true, y\_pred)}\\n"
)

Copy to clipboard

Classification report rebuilt from confusion matrix:
              precision    recall  f1-score   support

           0       1.00      0.99      0.99        88
           1       0.99      0.97      0.98        91
           2       0.99      0.99      0.99        86
           3       0.98      0.87      0.92        91
           4       0.99      0.96      0.97        92
           5       0.95      0.97      0.96        91
           6       0.99      0.99      0.99        91
           7       0.96      0.99      0.97        89
           8       0.94      1.00      0.97        88
           9       0.93      0.98      0.95        92

    accuracy                           0.97       899
   macro avg       0.97      0.97      0.97       899
weighted avg       0.97      0.97      0.97       899

Copy to clipboard

**Total running time of the script:** (0 minutes 0.431 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_digits_classification.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_digits_classification.ipynb)

[`Download Jupyter notebook: plot_digits_classification.ipynb`](https://scikit-learn.org/stable/_downloads/eb87d6211b2c0a7c2dc460a9e28b1f6a/plot_digits_classification.ipynb)

[`Download Python source code: plot_digits_classification.py`](https://scikit-learn.org/stable/_downloads/1a55101a8e49ab5d3213dadb31332045/plot_digits_classification.py)

[`Download zipped: plot_digits_classification.zip`](https://scikit-learn.org/stable/_downloads/3749b413371f6991d683ca525228e765/plot_digits_classification.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_active_learning_thumb.png)

[Label Propagation digits: Active learning](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)

Label Propagation digits: Active learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/1a55101a8e49ab5d3213dadb31332045/plot_digits_classification.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/eb87d6211b2c0a7c2dc460a9e28b1f6a/plot_digits_classification.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/3749b413371f6991d683ca525228e765/plot_digits_classification.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo4.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/classification/plot_digits_classification.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo4.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/classification/plot_digits_classification.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)