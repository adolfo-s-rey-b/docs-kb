[Skip to main content](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/model_selection/plot_learning_curve.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/model_selection/plot_learning_curve.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/model_selection/plot_learning_curve.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/model_selection/plot_learning_curve.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/model_selection/plot_learning_curve.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/model_selection/plot_learning_curve.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#sphx-glr-download-auto-examples-model-selection-plot-learning-curve-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plotting Learning Curves and Checking Models’ Scalability[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#plotting-learning-curves-and-checking-models-scalability "Link to this heading")

=====================================================================================================================================================================================================================================

In this example, we show how to use the class [`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")
 to easily plot learning curves. In addition, we give an interpretation to the learning curves obtained for a naive Bayes and SVM classifiers.

Then, we explore and draw some conclusions about the scalability of these predictive models by looking at their computational cost and not only at their statistical accuracy.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Learning Curve[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#learning-curve "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Learning curves show the effect of adding more samples during the training process. The effect is depicted by checking the statistical performance of the model in terms of training score and testing score.

Here, we compute the learning curve of a naive Bayes classifier and an SVM classifier with an RBF kernel using the digits dataset.

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.naive\_bayes import [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

X, y \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
naive\_bayes \= [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
()
svc \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="rbf", gamma\=0.001)

Copy to clipboard

The [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "sklearn.model_selection.LearningCurveDisplay.from_estimator")
 displays the learning curve given the dataset and the predictive model to analyze. To get an estimate of the scores uncertainty, this method uses a cross-validation procedure.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.model\_selection import LearningCurveDisplay, [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(10, 6), sharey\=True)

common\_params \= {
    "X": X,
    "y": y,
    "train\_sizes": [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.1, 1.0, 5),
    "cv": [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
(n\_splits\=50, test\_size\=0.2, random\_state\=0),
    "score\_type": "both",
    "n\_jobs": 4,
    "line\_kw": {"marker": "o"},
    "std\_display\_style": "fill\_between",
    "score\_name": "Accuracy",
}

for ax\_idx, estimator in enumerate(\[naive\_bayes, svc\]):
    [LearningCurveDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay.from_estimator "sklearn.model_selection.LearningCurveDisplay.from_estimator")
(estimator, \*\*common\_params, ax\=ax\[ax\_idx\])
    handles, label \= ax\[ax\_idx\].get\_legend\_handles\_labels()
    ax\[ax\_idx\].legend(handles\[:2\], \["Training Score", "Test Score"\])
    ax\[ax\_idx\].set\_title(f"Learning Curve for {estimator.\_\_class\_\_.\_\_name\_\_}")

Copy to clipboard

![Learning Curve for GaussianNB, Learning Curve for SVC](https://scikit-learn.org/stable/_images/sphx_glr_plot_learning_curve_001.png)

We first analyze the learning curve of the naive Bayes classifier. Its shape can be found in more complex datasets very often: the training score is very high when using few samples for training and decreases when increasing the number of samples, whereas the test score is very low at the beginning and then increases when adding samples. The training and test scores become more realistic when all the samples are used for training.

We see another typical learning curve for the SVM classifier with RBF kernel. The training score remains high regardless of the size of the training set. On the other hand, the test score increases with the size of the training dataset. Indeed, it increases up to a point where it reaches a plateau. Observing such a plateau is an indication that it might not be useful to acquire new data to train the model since the generalization performance of the model will not increase anymore.

Complexity analysis[#](https://scikit-learn.org/stable/auto_examples/model_selection/plot_learning_curve.html#complexity-analysis "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to these learning curves, it is also possible to look at the scalability of the predictive models in terms of training and scoring times.

The [`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")
 class does not provide such information. We need to resort to the [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
 function instead and make the plot manually.

from sklearn.model\_selection import [learning\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")

common\_params \= {
    "X": X,
    "y": y,
    "train\_sizes": [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.1, 1.0, 5),
    "cv": [ShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")
(n\_splits\=50, test\_size\=0.2, random\_state\=0),
    "n\_jobs": 4,
    "return\_times": True,
}

train\_sizes, \_, test\_scores\_nb, fit\_times\_nb, score\_times\_nb \= [learning\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
(
    naive\_bayes, \*\*common\_params
)
train\_sizes, \_, test\_scores\_svm, fit\_times\_svm, score\_times\_svm \= [learning\_curve](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
(
    svc, \*\*common\_params
)

Copy to clipboard

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2, figsize\=(16, 12), sharex\=True)

for ax\_idx, (fit\_times, score\_times, estimator) in enumerate(
    zip(
        \[fit\_times\_nb, fit\_times\_svm\],
        \[score\_times\_nb, score\_times\_svm\],
        \[naive\_bayes, svc\],
    )
):
    \# scalability regarding the fit time
    ax\[0, ax\_idx\].plot(train\_sizes, fit\_times.mean(axis\=1), "o-")
    ax\[0, ax\_idx\].fill\_between(
        train\_sizes,
        fit\_times.mean(axis\=1) \- fit\_times.std(axis\=1),
        fit\_times.mean(axis\=1) + fit\_times.std(axis\=1),
        alpha\=0.3,
    )
    ax\[0, ax\_idx\].set\_ylabel("Fit time (s)")
    ax\[0, ax\_idx\].set\_title(
        f"Scalability of the {estimator.\_\_class\_\_.\_\_name\_\_} classifier"
    )

    \# scalability regarding the score time
    ax\[1, ax\_idx\].plot(train\_sizes, score\_times.mean(axis\=1), "o-")
    ax\[1, ax\_idx\].fill\_between(
        train\_sizes,
        score\_times.mean(axis\=1) \- score\_times.std(axis\=1),
        score\_times.mean(axis\=1) + score\_times.std(axis\=1),
        alpha\=0.3,
    )
    ax\[1, ax\_idx\].set\_ylabel("Score time (s)")
    ax\[1, ax\_idx\].set\_xlabel("Number of training samples")

Copy to clipboard

![Scalability of the GaussianNB classifier, Scalability of the SVC classifier](https://scikit-learn.org/stable/_images/sphx_glr_plot_learning_curve_002.png)

We see that the scalability of the SVM and naive Bayes classifiers is very different. The SVM classifier complexity at fit and score time increases rapidly with the number of samples. Indeed, it is known that the fit time complexity of this classifier is more than quadratic with the number of samples which makes it hard to scale to dataset with more than a few 10,000 samples. In contrast, the naive Bayes classifier scales much better with a lower complexity at fit and score time.

Subsequently, we can check the trade-off between increased training time and the cross-validation score.

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=2, figsize\=(16, 6))

for ax\_idx, (fit\_times, test\_scores, estimator) in enumerate(
    zip(
        \[fit\_times\_nb, fit\_times\_svm\],
        \[test\_scores\_nb, test\_scores\_svm\],
        \[naive\_bayes, svc\],
    )
):
    ax\[ax\_idx\].plot(fit\_times.mean(axis\=1), test\_scores.mean(axis\=1), "o-")
    ax\[ax\_idx\].fill\_between(
        fit\_times.mean(axis\=1),
        test\_scores.mean(axis\=1) \- test\_scores.std(axis\=1),
        test\_scores.mean(axis\=1) + test\_scores.std(axis\=1),
        alpha\=0.3,
    )
    ax\[ax\_idx\].set\_ylabel("Accuracy")
    ax\[ax\_idx\].set\_xlabel("Fit time (s)")
    ax\[ax\_idx\].set\_title(
        f"Performance of the {estimator.\_\_class\_\_.\_\_name\_\_} classifier"
    )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Performance of the GaussianNB classifier, Performance of the SVC classifier](https://scikit-learn.org/stable/_images/sphx_glr_plot_learning_curve_003.png)

In these plots, we can look for the inflection point for which the cross-validation score does not increase anymore and only the training time increases.

**Total running time of the script:** (0 minutes 17.597 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_learning_curve.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_learning_curve.ipynb)

[`Download Jupyter notebook: plot_learning_curve.ipynb`](https://scikit-learn.org/stable/_downloads/ca0bfe2435d9b3fffe21c713e63d3a6f/plot_learning_curve.ipynb)

[`Download Python source code: plot_learning_curve.py`](https://scikit-learn.org/stable/_downloads/57163227aeb4c19ca4c69b87a8d1949c/plot_learning_curve.py)

[`Download zipped: plot_learning_curve.zip`](https://scikit-learn.org/stable/_downloads/83b230a9377aa30995aae41940c0d3a4/plot_learning_curve.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_roc_curve_visualization_api_thumb.png)

[ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html)

ROC Curve with Visualization API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_curve_thumb.png)

[Probability Calibration curves](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_curve.html)

Probability Calibration curves

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/57163227aeb4c19ca4c69b87a8d1949c/plot_learning_curve.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ca0bfe2435d9b3fffe21c713e63d3a6f/plot_learning_curve.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/83b230a9377aa30995aae41940c0d3a4/plot_learning_curve.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo23.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/model_selection/plot_learning_curve.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo23.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/model_selection/plot_learning_curve.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)