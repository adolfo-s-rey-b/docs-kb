[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_outlier_detection_bench.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_outlier_detection_bench.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_outlier_detection_bench.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_outlier_detection_bench.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_outlier_detection_bench.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#sphx-glr-download-auto-examples-miscellaneous-plot-outlier-detection-bench-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Evaluation of outlier detection estimators[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#evaluation-of-outlier-detection-estimators "Link to this heading")

===============================================================================================================================================================================================================

This example compares two outlier detection algorithms, namely [Local Outlier Factor](https://scikit-learn.org/stable/modules/outlier_detection.html#local-outlier-factor)
 (LOF) and [Isolation Forest](https://scikit-learn.org/stable/modules/outlier_detection.html#isolation-forest)
 (IForest), on real-world datasets available in [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
. The goal is to show that different algorithms perform well on different datasets and contrast their training speed and sensitivity to hyperparameters.

The algorithms are trained (without labels) on the whole dataset assumed to contain outliers.

1.  The ROC curves are computed using knowledge of the ground-truth labels and displayed using [`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
    .
    
2.  The performance is assessed in terms of the ROC-AUC.
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset preprocessing and model training[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#dataset-preprocessing-and-model-training "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Different outlier detection models require different preprocessing. In the presence of categorical variables, [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
 is often a good strategy for tree-based models such as [`IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
, whereas neighbors-based models such as [`LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
 would be impacted by the ordering induced by ordinal encoding. To avoid inducing an ordering, on should rather use [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
.

Neighbors-based models may also require scaling of the numerical features (see for instance [Effect of rescaling on a k-neighbors models](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html#neighbors-scaling)
). In the presence of outliers, a good option is to use a [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
.

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.ensemble import [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
from sklearn.neighbors import [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import (
    [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
,
    [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
,
    [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
,
)

def make\_estimator(name, categorical\_columns\=None, iforest\_kw\=None, lof\_kw\=None):
    """Create an outlier detection estimator based on its name."""
    if name \== "LOF":
        outlier\_detector \= [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
(\*\*(lof\_kw or {}))
        if categorical\_columns is None:
            preprocessor \= [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
()
        else:
            preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
                transformers\=\[("categorical", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(), categorical\_columns)\],
                remainder\=[RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
(),
            )
    else:  \# name == "IForest"
        outlier\_detector \= [IsolationForest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
(\*\*(iforest\_kw or {}))
        if categorical\_columns is None:
            preprocessor \= None
        else:
            ordinal\_encoder \= [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
(
                handle\_unknown\="use\_encoded\_value", unknown\_value\=-1
            )
            preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
                transformers\=\[\
                    ("categorical", ordinal\_encoder, categorical\_columns),\
                \],
                remainder\="passthrough",
            )

    return [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(preprocessor, outlier\_detector)

Copy to clipboard

The following `fit_predict` function returns the average outlier score of X.

from time import [perf\_counter](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")

def fit\_predict(estimator, X):
    tic \= [perf\_counter](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
()
    if estimator\[\-1\].\_\_class\_\_.\_\_name\_\_ \== "LocalOutlierFactor":
        estimator.fit(X)
        y\_score \= estimator\[\-1\].negative\_outlier\_factor\_
    else:  \# "IsolationForest"
        y\_score \= estimator.fit(X).decision\_function(X)
    toc \= [perf\_counter](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
()
    print(f"Duration for {model\_name}: {toc \- tic:.2f} s")
    return y\_score

Copy to clipboard

On the rest of the example we process one dataset per section. After loading the data, the targets are modified to consist of two classes: 0 representing inliers and 1 representing outliers. Due to computational constraints of the scikit-learn documentation, the sample size of some datasets is reduced using a stratified [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
.

Furthermore, we set `n_neighbors` to match the expected number of anomalies `expected_n_anomalies = n_samples * expected_anomaly_fraction`. This is a good heuristic as long as the proportion of outliers is not very low, the reason being that `n_neighbors` should be at least greater than the number of samples in the less populated cluster (see [Outlier detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html#sphx-glr-auto-examples-neighbors-plot-lof-outlier-detection-py)
).

### KDDCup99 - SA dataset[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#kddcup99-sa-dataset "Link to this heading")

The [Kddcup 99 dataset](https://scikit-learn.org/stable/datasets/real_world.html#kddcup99-dataset)
 was generated using a closed network and hand-injected attacks. The SA dataset is a subset of it obtained by simply selecting all the normal data and an anomaly proportion of around 3%.

import numpy as np

from sklearn.datasets import [fetch\_kddcup99](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [fetch\_kddcup99](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
(
    subset\="SA", percent10\=True, random\_state\=42, return\_X\_y\=True, as\_frame\=True
)
y \= (y != b"normal.").astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)
X, \_, y, \_ \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, train\_size\=0.1, stratify\=y, random\_state\=42)

n\_samples, anomaly\_frac \= X.shape\[0\], y.mean()
print(f"{n\_samples} datapoints with {y.sum()} anomalies ({anomaly\_frac:.02%})")

Copy to clipboard

10065 datapoints with 338 anomalies (3.36%)

Copy to clipboard

The SA dataset contains 41 features out of which 3 are categorical: “protocol\_type”, “service” and “flag”.

y\_true \= {}
y\_score \= {"LOF": {}, "IForest": {}}
model\_names \= \["LOF", "IForest"\]
cat\_columns \= \["protocol\_type", "service", "flag"\]

y\_true\["KDDCup99 - SA"\] \= y
for model\_name in model\_names:
    model \= make\_estimator(
        name\=model\_name,
        categorical\_columns\=cat\_columns,
        lof\_kw\={"n\_neighbors": int(n\_samples \* anomaly\_frac)},
        iforest\_kw\={"random\_state": 42},
    )
    y\_score\[model\_name\]\["KDDCup99 - SA"\] \= fit\_predict(model, X)

Copy to clipboard

Duration for LOF: 1.73 s
Duration for IForest: 0.28 s

Copy to clipboard

### Forest covertypes dataset[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#forest-covertypes-dataset "Link to this heading")

The [Forest covertypes](https://scikit-learn.org/stable/datasets/real_world.html#covtype-dataset)
 is a multiclass dataset where the target is the dominant species of tree in a given patch of forest. It contains 54 features, some of which (“Wilderness\_Area” and “Soil\_Type”) are already binary encoded. Though originally meant as a classification task, one can regard inliers as samples encoded with label 2 and outliers as those with label 4.

from sklearn.datasets import [fetch\_covtype](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")

X, y \= [fetch\_covtype](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")
(return\_X\_y\=True, as\_frame\=True)
s \= (y \== 2) + (y \== 4)
X \= X.loc\[s\]
y \= y.loc\[s\]
y \= (y != 2).astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)

X, \_, y, \_ \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, train\_size\=0.05, stratify\=y, random\_state\=42)
X\_forestcover \= X  \# save X for later use

n\_samples, anomaly\_frac \= X.shape\[0\], y.mean()
print(f"{n\_samples} datapoints with {y.sum()} anomalies ({anomaly\_frac:.02%})")

Copy to clipboard

14302 datapoints with 137 anomalies (0.96%)

Copy to clipboard

y\_true\["forestcover"\] \= y
for model\_name in model\_names:
    model \= make\_estimator(
        name\=model\_name,
        lof\_kw\={"n\_neighbors": int(n\_samples \* anomaly\_frac)},
        iforest\_kw\={"random\_state": 42},
    )
    y\_score\[model\_name\]\["forestcover"\] \= fit\_predict(model, X)

Copy to clipboard

Duration for LOF: 1.64 s
Duration for IForest: 0.22 s

Copy to clipboard

### Ames Housing dataset[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#ames-housing-dataset "Link to this heading")

The [Ames housing dataset](http://www.openml.org/d/43926)
 is originally a regression dataset where the target are sales prices of houses in Ames, Iowa. Here we convert it into an outlier detection problem by regarding houses with price over 70 USD/sqft. To make the problem easier, we drop intermediate prices between 40 and 70 USD/sqft.

import matplotlib.pyplot as plt

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(name\="ames\_housing", version\=1, return\_X\_y\=True, as\_frame\=True)
y \= y.div(X\["Lot\_Area"\])

\# None values in pandas 1.5.1 were mapped to np.nan in pandas 2.0.1
X\["Misc\_Feature"\] \= X\["Misc\_Feature"\].cat.add\_categories("NoInfo").fillna("NoInfo")
X\["Mas\_Vnr\_Type"\] \= X\["Mas\_Vnr\_Type"\].cat.add\_categories("NoInfo").fillna("NoInfo")

X.drop(columns\="Lot\_Area", inplace\=True)
mask \= (y < 40) | (y \> 70)
X \= X.loc\[mask\]
y \= y.loc\[mask\]
y.hist(bins\=20, edgecolor\="black")
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("House price in USD/sqft")
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Distribution of house prices in Ames")

Copy to clipboard

![Distribution of house prices in Ames](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_001.png)

y \= (y \> 70).astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)

n\_samples, anomaly\_frac \= X.shape\[0\], y.mean()
print(f"{n\_samples} datapoints with {y.sum()} anomalies ({anomaly\_frac:.02%})")

Copy to clipboard

2714 datapoints with 30 anomalies (1.11%)

Copy to clipboard

The dataset contains 46 categorical features. In this case it is easier use a [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
 to find them instead of passing a list made by hand.

from sklearn.compose import make\_column\_selector as [selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")

categorical\_columns\_selector \= [selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
(dtype\_include\="category")
cat\_columns \= categorical\_columns\_selector(X)

y\_true\["ames\_housing"\] \= y
for model\_name in model\_names:
    model \= make\_estimator(
        name\=model\_name,
        categorical\_columns\=cat\_columns,
        lof\_kw\={"n\_neighbors": int(n\_samples \* anomaly\_frac)},
        iforest\_kw\={"random\_state": 42},
    )
    y\_score\[model\_name\]\["ames\_housing"\] \= fit\_predict(model, X)

Copy to clipboard

Duration for LOF: 0.44 s
Duration for IForest: 0.24 s

Copy to clipboard

### Cardiotocography dataset[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#cardiotocography-dataset "Link to this heading")

The [Cardiotocography dataset](http://www.openml.org/d/1466)
 is a multiclass dataset of fetal cardiotocograms, the classes being the fetal heart rate (FHR) pattern encoded with labels from 1 to 10. Here we set class 3 (the minority class) to represent the outliers. It contains 30 numerical features, some of which are binary encoded and some are continuous.

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(name\="cardiotocography", version\=1, return\_X\_y\=True, as\_frame\=False)
X\_cardiotocography \= X  \# save X for later use
s \= y \== "3"
y \= s.astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)

n\_samples, anomaly\_frac \= X.shape\[0\], y.mean()
print(f"{n\_samples} datapoints with {y.sum()} anomalies ({anomaly\_frac:.02%})")

Copy to clipboard

2126 datapoints with 53 anomalies (2.49%)

Copy to clipboard

y\_true\["cardiotocography"\] \= y
for model\_name in model\_names:
    model \= make\_estimator(
        name\=model\_name,
        lof\_kw\={"n\_neighbors": int(n\_samples \* anomaly\_frac)},
        iforest\_kw\={"random\_state": 42},
    )
    y\_score\[model\_name\]\["cardiotocography"\] \= fit\_predict(model, X)

Copy to clipboard

Duration for LOF: 0.05 s
Duration for IForest: 0.14 s

Copy to clipboard

Plot and interpret results[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#plot-and-interpret-results "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The algorithm performance relates to how good the true positive rate (TPR) is at low value of the false positive rate (FPR). The best algorithms have the curve on the top-left of the plot and the area under curve (AUC) close to 1. The diagonal dashed line represents a random classification of outliers and inliers.

import math

from sklearn.metrics import RocCurveDisplay

cols \= 2
pos\_label \= 0  \# mean 0 belongs to positive class
datasets\_names \= y\_true.keys()
rows \= [math.ceil](https://docs.python.org/3/library/math.html#math.ceil "math.ceil")
(len(datasets\_names) / cols)

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=rows, ncols\=cols, squeeze\=False, figsize\=(10, rows \* 4))

for ax, dataset\_name in zip(axs.ravel(), datasets\_names):
    for model\_idx, model\_name in enumerate(model\_names):
        display \= [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
            y\_true\[dataset\_name\],
            y\_score\[model\_name\]\[dataset\_name\],
            pos\_label\=pos\_label,
            name\=model\_name,
            ax\=ax,
            plot\_chance\_level\=(model\_idx \== len(model\_names) \- 1),
            chance\_level\_kw\={"linestyle": ":"},
        )
    ax.set\_title(dataset\_name)
\_ \= [plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
(pad\=2.0)  \# spacing between subplots

Copy to clipboard

![KDDCup99 - SA, forestcover, ames_housing, cardiotocography](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_002.png)

We observe that once the number of neighbors is tuned, LOF and IForest perform similarly in terms of ROC AUC for the forestcover and cardiotocography datasets. The score for IForest is slightly better for the SA dataset and LOF performs considerably better on the Ames housing dataset than IForest.

Recall however that Isolation Forest tends to train much faster than LOF on datasets with a large number of samples. LOF needs to compute pairwise distances to find nearest neighbors, which has a quadratic complexity with respect to the number of observations. This can make this method prohibitive on large datasets.

Ablation study[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html#ablation-study "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

In this section we explore the impact of the hyperparameter `n_neighbors` and the choice of scaling the numerical variables on the LOF model. Here we use the [Forest covertypes](https://scikit-learn.org/stable/datasets/real_world.html#covtype-dataset)
 dataset as the binary encoded categories introduce a natural scale of euclidean distances between 0 and 1. We then want a scaling method to avoid granting a privilege to non-binary features and that is robust enough to outliers so that the task of finding them does not become too difficult.

X \= X\_forestcover
y \= y\_true\["forestcover"\]

n\_samples \= X.shape\[0\]
n\_neighbors\_list \= (n\_samples \* [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0.2, 0.02, 0.01, 0.001\])).astype([np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
(), [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
())

linestyles \= \["solid", "dashed", "dashdot", ":", (5, (10, 3))\]

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
for model\_idx, (linestyle, n\_neighbors) in enumerate(zip(linestyles, n\_neighbors\_list)):
    model.set\_params(localoutlierfactor\_\_n\_neighbors\=n\_neighbors)
    model.fit(X)
    y\_score \= model\[\-1\].negative\_outlier\_factor\_
    display \= [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
        y,
        y\_score,
        pos\_label\=pos\_label,
        name\=f"n\_neighbors = {n\_neighbors}",
        ax\=ax,
        plot\_chance\_level\=(model\_idx \== len(n\_neighbors\_list) \- 1),
        chance\_level\_kw\={"linestyle": (0, (1, 10))},
        curve\_kwargs\=dict(linestyle\=linestyle, linewidth\=2),
    )
\_ \= ax.set\_title("RobustScaler with varying n\_neighbors\\non forestcover dataset")

Copy to clipboard

![RobustScaler with varying n_neighbors on forestcover dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_003.png)

We observe that the number of neighbors has a big impact on the performance of the model. If one has access to (at least some) ground truth labels, it is then important to tune `n_neighbors` accordingly. A convenient way to do so is to explore values for `n_neighbors` of the order of magnitud of the expected contamination.

from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
, [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

preprocessor\_list \= \[\
    None,\
    [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")\
(),\
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(),\
    [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
(),\
    [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")\
(),\
\]
expected\_anomaly\_fraction \= 0.02
lof \= [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
(n\_neighbors\=int(n\_samples \* expected\_anomaly\_fraction))

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
for model\_idx, (linestyle, preprocessor) in enumerate(
    zip(linestyles, preprocessor\_list)
):
    model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(preprocessor, lof)
    model.fit(X)
    y\_score \= model\[\-1\].negative\_outlier\_factor\_
    display \= [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
        y,
        y\_score,
        pos\_label\=pos\_label,
        name\=str(preprocessor).split("(")\[0\],
        ax\=ax,
        plot\_chance\_level\=(model\_idx \== len(preprocessor\_list) \- 1),
        chance\_level\_kw\={"linestyle": (0, (1, 10))},
        curve\_kwargs\=dict(linestyle\=linestyle, linewidth\=2),
    )
\_ \= ax.set\_title("Fixed n\_neighbors with varying preprocessing\\non forestcover dataset")

Copy to clipboard

![Fixed n_neighbors with varying preprocessing on forestcover dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_004.png)

On the one hand, [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
 scales each feature independently by using the interquartile range (IQR) by default, which is the range between the 25th and 75th percentiles of the data. It centers the data by subtracting the median and then scale it by dividing by the IQR. The IQR is robust to outliers: the median and interquartile range are less affected by extreme values than the range, the mean and the standard deviation. Furthermore, [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
 does not squash marginal outlier values, contrary to [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
.

On the other hand, [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
 scales each feature individually such that its range maps into the range between zero and one. If there are outliers in the data, they can skew it towards either the minimum or maximum values, leading to a completely different distribution of data with large marginal outliers: all non-outlier values can be collapsed almost together as a result.

We also evaluated no preprocessing at all (by passing `None` to the pipeline), [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 and [`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
. Please refer to their respective documentation for more details.

Note that the optimal preprocessing depends on the dataset, as shown below:

X \= X\_cardiotocography
y \= y\_true\["cardiotocography"\]

n\_samples, expected\_anomaly\_fraction \= X.shape\[0\], 0.025
lof \= [LocalOutlierFactor](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
(n\_neighbors\=int(n\_samples \* expected\_anomaly\_fraction))

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
for model\_idx, (linestyle, preprocessor) in enumerate(
    zip(linestyles, preprocessor\_list)
):
    model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(preprocessor, lof)
    model.fit(X)
    y\_score \= model\[\-1\].negative\_outlier\_factor\_
    display \= [RocCurveDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_predictions "sklearn.metrics.RocCurveDisplay.from_predictions")
(
        y,
        y\_score,
        pos\_label\=pos\_label,
        name\=str(preprocessor).split("(")\[0\],
        ax\=ax,
        plot\_chance\_level\=(model\_idx \== len(preprocessor\_list) \- 1),
        chance\_level\_kw\={"linestyle": (0, (1, 10))},
        curve\_kwargs\=dict(linestyle\=linestyle, linewidth\=2),
    )
ax.set\_title(
    "Fixed n\_neighbors with varying preprocessing\\non cardiotocography dataset"
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Fixed n_neighbors with varying preprocessing on cardiotocography dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_005.png)

**Total running time of the script:** (0 minutes 49.713 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_outlier_detection_bench.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_outlier_detection_bench.ipynb)

[`Download Jupyter notebook: plot_outlier_detection_bench.ipynb`](https://scikit-learn.org/stable/_downloads/eacb6a63c887dafcff02b3cee64854ef/plot_outlier_detection_bench.ipynb)

[`Download Python source code: plot_outlier_detection_bench.py`](https://scikit-learn.org/stable/_downloads/b7e32fe54d613dce0d3c376377af061d/plot_outlier_detection_bench.py)

[`Download zipped: plot_outlier_detection_bench.zip`](https://scikit-learn.org/stable/_downloads/622bed78541c980857399459cc7188ca/plot_outlier_detection_bench.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_outlier_detection_thumb.png)

[Outlier detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_outlier_detection.html)

Outlier detection with Local Outlier Factor (LOF)

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lof_novelty_detection_thumb.png)

[Novelty detection with Local Outlier Factor (LOF)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_lof_novelty_detection.html)

Novelty detection with Local Outlier Factor (LOF)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/b7e32fe54d613dce0d3c376377af061d/plot_outlier_detection_bench.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/eacb6a63c887dafcff02b3cee64854ef/plot_outlier_detection_bench.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/622bed78541c980857399459cc7188ca/plot_outlier_detection_bench.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_outlier_detection_bench.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_outlier_detection_bench.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)