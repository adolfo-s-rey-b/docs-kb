[Skip to main content](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/ensemble/plot_ensemble_oob.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/ensemble/plot_ensemble_oob.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/ensemble/plot_ensemble_oob.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/ensemble/plot_ensemble_oob.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/ensemble/plot_ensemble_oob.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/ensemble/plot_ensemble_oob.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html#sphx-glr-download-auto-examples-ensemble-plot-ensemble-oob-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

OOB Errors for Random Forests[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html#oob-errors-for-random-forests "Link to this heading")

=====================================================================================================================================================================

The `RandomForestClassifier` is trained using _bootstrap aggregation_, where each new tree is fit from a bootstrap sample of the training observations zi\=(xi,yi). The _out-of-bag_ (OOB) error is the average error for each zi calculated using predictions from the trees that do not contain zi in their respective bootstrap sample. This allows the `RandomForestClassifier` to be fit and validated whilst being trained [\[1\]](https://scikit-learn.org/stable/auto_examples/ensemble/plot_ensemble_oob.html#id2)
.

The example below demonstrates how the OOB error can be measured at the addition of each new tree during training. The resulting plot allows a practitioner to approximate a suitable value of `n_estimators` at which the error stabilizes.

![plot ensemble oob](https://scikit-learn.org/stable/_images/sphx_glr_plot_ensemble_oob_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from collections import [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")

import matplotlib.pyplot as plt

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

RANDOM\_STATE \= 123

\# Generate a binary classification dataset.
X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(
    n\_samples\=500,
    n\_features\=25,
    n\_clusters\_per\_class\=1,
    n\_informative\=15,
    random\_state\=RANDOM\_STATE,
)

\# NOTE: Setting the \`warm\_start\` construction parameter to \`True\` disables
\# support for parallelized ensembles but is necessary for tracking the OOB
\# error trajectory during training.
ensemble\_clfs \= \[\
    (\
        "RandomForestClassifier, max\_features='sqrt'",\
        [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(\
            warm\_start\=True,\
            oob\_score\=True,\
            max\_features\="sqrt",\
            random\_state\=RANDOM\_STATE,\
        ),\
    ),\
    (\
        "RandomForestClassifier, max\_features='log2'",\
        [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(\
            warm\_start\=True,\
            max\_features\="log2",\
            oob\_score\=True,\
            random\_state\=RANDOM\_STATE,\
        ),\
    ),\
    (\
        "RandomForestClassifier, max\_features=None",\
        [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(\
            warm\_start\=True,\
            max\_features\=None,\
            oob\_score\=True,\
            random\_state\=RANDOM\_STATE,\
        ),\
    ),\
\]

\# Map a classifier name to a list of (<n\_estimators>, <error rate>) pairs.
error\_rate \= [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
((label, \[\]) for label, \_ in ensemble\_clfs)

\# Range of \`n\_estimators\` values to explore.
min\_estimators \= 15
max\_estimators \= 150

for label, clf in ensemble\_clfs:
    for i in range(min\_estimators, max\_estimators + 1, 5):
        clf.set\_params(n\_estimators\=i)
        clf.fit(X, y)

        \# Record the OOB error for each \`n\_estimators=i\` setting.
        oob\_error \= 1 \- clf.oob\_score\_
        error\_rate\[label\].append((i, oob\_error))

\# Generate the "OOB error rate" vs. "n\_estimators" plot.
for label, clf\_err in error\_rate.items():
    xs, ys \= zip(\*clf\_err)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(xs, ys, label\=label)

[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(min\_estimators, max\_estimators)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("n\_estimators")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("OOB error rate")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(loc\="upper right")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.529 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_ensemble_oob.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_ensemble_oob.ipynb)

[`Download Jupyter notebook: plot_ensemble_oob.ipynb`](https://scikit-learn.org/stable/_downloads/6c50dbd9c6dc52f3da913f8d8f82274d/plot_ensemble_oob.ipynb)

[`Download Python source code: plot_ensemble_oob.py`](https://scikit-learn.org/stable/_downloads/75191b2eb3b4aa13066927321dd3fdcf/plot_ensemble_oob.py)

[`Download zipped: plot_ensemble_oob.zip`](https://scikit-learn.org/stable/_downloads/a3fe1b9a65568eb1b8610be42fd84cbb/plot_ensemble_oob.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_oob_thumb.png)

[Gradient Boosting Out-of-Bag estimates](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_oob.html)

Gradient Boosting Out-of-Bag estimates

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/75191b2eb3b4aa13066927321dd3fdcf/plot_ensemble_oob.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6c50dbd9c6dc52f3da913f8d8f82274d/plot_ensemble_oob.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a3fe1b9a65568eb1b8610be42fd84cbb/plot_ensemble_oob.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo12.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_ensemble_oob.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo12.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/ensemble/plot_ensemble_oob.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)