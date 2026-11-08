[Skip to main content](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/feature_selection/plot_rfe_digits.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/feature_selection/plot_rfe_digits.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/feature_selection/plot_rfe_digits.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/feature_selection/plot_rfe_digits.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/feature_selection/plot_rfe_digits.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/feature_selection/plot_rfe_digits.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html#sphx-glr-download-auto-examples-feature-selection-plot-rfe-digits-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Recursive feature elimination[#](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_digits.html#recursive-feature-elimination "Link to this heading")

============================================================================================================================================================================

This example demonstrates how Recursive Feature Elimination ([`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
) can be used to determine the importance of individual pixels for classifying handwritten digits. [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
 recursively removes the least significant features, assigning ranks based on their importance, where higher `ranking_` values denote lower importance. The ranking is visualized using both shades of blue and pixel annotations for clarity. As expected, pixels positioned at the center of the image tend to be more predictive than those near the edges.

Note

See also [Recursive feature elimination with cross-validation](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_rfe_with_cross_validation.html#sphx-glr-auto-examples-feature-selection-plot-rfe-with-cross-validation-py)

![Ranking of pixels with RFE (Logistic Regression)](https://scikit-learn.org/stable/_images/sphx_glr_plot_rfe_digits_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn.datasets import [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
from sklearn.feature\_selection import [RFE](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")

\# Load the digits dataset
digits \= [load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
()
X \= digits.images.reshape((len(digits.images), \-1))
y \= digits.target

pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("scaler", [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
()),\
        ("rfe", [RFE](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")\
(estimator\=[LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(), n\_features\_to\_select\=1, step\=1)),\
    \]
)

pipe.fit(X, y)
ranking \= pipe.named\_steps\["rfe"\].ranking\_.reshape(digits.images\[0\].shape)

\# Plot pixel ranking
[plt.matshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow")
(ranking, cmap\=plt.cm.Blues)

\# Add annotations for pixel numbers
for i in range(ranking.shape\[0\]):
    for j in range(ranking.shape\[1\]):
        [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(j, i, str(ranking\[i, j\]), ha\="center", va\="center", color\="black")

[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Ranking of pixels with RFE\\n(Logistic Regression)")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.291 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_rfe_digits.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_rfe_digits.ipynb)

[`Download Jupyter notebook: plot_rfe_digits.ipynb`](https://scikit-learn.org/stable/_downloads/89b02c3e866d0979d0024f34b90877de/plot_rfe_digits.ipynb)

[`Download Python source code: plot_rfe_digits.py`](https://scikit-learn.org/stable/_downloads/f03a2a04a75f73f183e0407e663d121d/plot_rfe_digits.py)

[`Download zipped: plot_rfe_digits.zip`](https://scikit-learn.org/stable/_downloads/0b569e153dc27fb6eeb5063e271e8921/plot_rfe_digits.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_thumb.png)

[Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)

Kernel Density Estimation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/f03a2a04a75f73f183e0407e663d121d/plot_rfe_digits.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/89b02c3e866d0979d0024f34b90877de/plot_rfe_digits.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0b569e153dc27fb6eeb5063e271e8921/plot_rfe_digits.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo13.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/feature_selection/plot_rfe_digits.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo13.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/feature_selection/plot_rfe_digits.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)