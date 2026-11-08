[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_pca_iris.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_pca_iris.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_pca_iris.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_pca_iris.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_pca_iris.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_pca_iris.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-download-auto-examples-decomposition-plot-pca-iris-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Principal Component Analysis (PCA) on Iris Dataset[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#principal-component-analysis-pca-on-iris-dataset "Link to this heading")

==============================================================================================================================================================================================================

This example shows a well known decomposition technique known as Principal Component Analysis (PCA) on the [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set)
.

This dataset is made of 4 features: sepal length, sepal width, petal length, petal width. We use PCA to project this 4 feature space into a 3-dimensional space.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading the Iris dataset[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#loading-the-iris-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

The Iris dataset is directly available as part of scikit-learn. It can be loaded using the [`load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
 function. With the default parameters, a [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 object is returned, containing the data, the target values, the feature names, and the target names.

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
(as\_frame\=True)
print(iris.keys())

Copy to clipboard

dict\_keys(\['data', 'target', 'frame', 'target\_names', 'DESCR', 'feature\_names', 'filename', 'data\_module'\])

Copy to clipboard

Plot of pairs of features of the Iris dataset[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#plot-of-pairs-of-features-of-the-iris-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s first plot the pairs of features of the Iris dataset.

import seaborn as sns

\# Rename classes using the iris target names
iris.frame\["target"\] \= iris.target\_names\[iris.target\]
\_ \= [sns.pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot")
(iris.frame, hue\="target")

Copy to clipboard

![plot pca iris](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_001.png)

Each data point on each scatter plot refers to one of the 150 iris flowers in the dataset, with the color indicating their respective type (Setosa, Versicolor, and Virginica).

You can already see a pattern regarding the Setosa type, which is easily identifiable based on its short and wide sepal. Only considering these two dimensions, sepal width and length, there’s still overlap between the Versicolor and Virginica types.

The diagonal of the plot shows the distribution of each feature. We observe that the petal width and the petal length are the most discriminant features for the three types.

Plot a PCA representation[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#plot-a-pca-representation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s apply a Principal Component Analysis (PCA) to the iris dataset and then plot the irises across the first three principal components. This will allow us to better differentiate among the three types!

import matplotlib.pyplot as plt

\# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl\_toolkits.mplot3d  \# noqa: F401

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(1, figsize\=(8, 6))
ax \= fig.add\_subplot(111, projection\="3d", elev\=-150, azim\=110)

X\_reduced \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=3).fit\_transform(iris.data)
scatter \= ax.scatter(
    X\_reduced\[:, 0\],
    X\_reduced\[:, 1\],
    X\_reduced\[:, 2\],
    c\=iris.target,
    s\=40,
)

ax.set(
    title\="First three principal components",
    xlabel\="1st Principal Component",
    ylabel\="2nd Principal Component",
    zlabel\="3rd Principal Component",
)
ax.xaxis.set\_ticklabels(\[\])
ax.yaxis.set\_ticklabels(\[\])
ax.zaxis.set\_ticklabels(\[\])

\# Add a legend
legend1 \= ax.legend(
    scatter.legend\_elements()\[0\],
    iris.target\_names.tolist(),
    loc\="upper right",
    title\="Classes",
)
ax.add\_artist(legend1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![First three principal components](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_002.png)

PCA will create 3 new features that are a linear combination of the 4 original features. In addition, this transformation maximizes the variance. With this transformation, we can identify each species using only the first principal component.

**Total running time of the script:** (0 minutes 1.663 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_pca_iris.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_pca_iris.ipynb)

[`Download Jupyter notebook: plot_pca_iris.ipynb`](https://scikit-learn.org/stable/_downloads/46b6a23d83637bf0f381ce9d8c528aa2/plot_pca_iris.ipynb)

[`Download Python source code: plot_pca_iris.py`](https://scikit-learn.org/stable/_downloads/1168f82083b3e70f31672e7c33738f8d/plot_pca_iris.py)

[`Download zipped: plot_pca_iris.zip`](https://scikit-learn.org/stable/_downloads/99402c7ce7a6ab7fafcb48caa3c9447b/plot_pca_iris.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_vs_lda_thumb.png)

[Comparison of LDA and PCA 2D projection of Iris dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html)

Comparison of LDA and PCA 2D projection of Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_dtc_thumb.png)

[Plot the decision surface of decision trees trained on the iris dataset](https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html)

Plot the decision surface of decision trees trained on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/1168f82083b3e70f31672e7c33738f8d/plot_pca_iris.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/46b6a23d83637bf0f381ce9d8c528aa2/plot_pca_iris.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/99402c7ce7a6ab7fafcb48caa3c9447b/plot_pca_iris.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_pca_iris.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_pca_iris.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)