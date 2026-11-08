[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_all_scaling.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_all_scaling.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_all_scaling.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_all_scaling.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_all_scaling.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_all_scaling.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-download-auto-examples-preprocessing-plot-all-scaling-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Compare the effect of different scalers on data with outliers[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#compare-the-effect-of-different-scalers-on-data-with-outliers "Link to this heading")

=========================================================================================================================================================================================================================================

Feature 0 (median income in a block) and feature 5 (average house occupancy) of the [California Housing dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
 have very different scales and contain some very large outliers. These two characteristics lead to difficulties to visualize the data and, more importantly, they can degrade the predictive performance of many machine learning algorithms. Unscaled data can also slow down or even prevent the convergence of many gradient-based estimators.

Indeed many estimators are designed with the assumption that each feature takes values close to zero or more importantly that all features vary on comparable scales. In particular, metric-based and gradient-based estimators often assume approximately standardized data (centered features with unit variances). A notable exception are decision tree-based estimators that are robust to arbitrary scaling of the data.

This example uses different scalers, transformers, and normalizers to bring the data within a pre-defined range.

Scalers are linear (or more precisely affine) transformers and differ from each other in the way they estimate the parameters used to shift and scale each feature.

[`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 provides non-linear transformations in which distances between marginal outliers and inliers are shrunk. [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
 provides non-linear transformations in which data is mapped to a normal distribution to stabilize variance and minimize skewness.

Unlike the previous transformations, normalization refers to a per sample transformation instead of a per feature transformation.

The following code is a bit verbose, feel free to jump directly to the analysis of the [results](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#results)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib as mpl
import numpy as np
from matplotlib import [cm](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
from matplotlib import pyplot as plt

from sklearn.datasets import [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
from sklearn.preprocessing import (
    [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
,
    [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
,
    [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
,
    [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
,
    [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
,
    [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
,
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
,
    [minmax\_scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")
,
)

dataset \= [fetch\_california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")
()
X\_full, y\_full \= dataset.data, dataset.target
feature\_names \= dataset.feature\_names

feature\_mapping \= {
    "MedInc": "Median income in block",
    "HouseAge": "Median house age in block",
    "AveRooms": "Average number of rooms",
    "AveBedrms": "Average number of bedrooms",
    "Population": "Block population",
    "AveOccup": "Average house occupancy",
    "Latitude": "House block latitude",
    "Longitude": "House block longitude",
}

\# Take only 2 features to make visualization easier
\# Feature MedInc has a long tail distribution.
\# Feature AveOccup has a few but very large outliers.
features \= \["MedInc", "AveOccup"\]
features\_idx \= \[feature\_names.index(feature) for feature in features\]
X \= X\_full\[:, features\_idx\]
distributions \= \[\
    ("Unscaled data", X),\
    ("Data after standard scaling", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
().fit\_transform(X)),\
    ("Data after min-max scaling", [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")\
().fit\_transform(X)),\
    ("Data after max-abs scaling", [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")\
().fit\_transform(X)),\
    (\
        "Data after robust scaling",\
        [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")\
(quantile\_range\=(25, 75)).fit\_transform(X),\
    ),\
    (\
        "Data after power transformation (Yeo-Johnson)",\
        [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")\
(method\="yeo-johnson").fit\_transform(X),\
    ),\
    (\
        "Data after power transformation (Box-Cox)",\
        [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")\
(method\="box-cox").fit\_transform(X),\
    ),\
    (\
        "Data after quantile transformation (uniform pdf)",\
        [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")\
(\
            output\_distribution\="uniform", random\_state\=42\
        ).fit\_transform(X),\
    ),\
    (\
        "Data after quantile transformation (gaussian pdf)",\
        [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")\
(\
            output\_distribution\="normal", random\_state\=42\
        ).fit\_transform(X),\
    ),\
    ("Data after sample-wise L2 normalizing", [Normalizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")\
().fit\_transform(X)),\
\]

\# scale the output between 0 and 1 for the colorbar
y \= [minmax\_scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")
(y\_full)

\# plasma does not exist in matplotlib < 1.5
cmap \= getattr([cm](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
, "plasma\_r", [cm](https://matplotlib.org/stable/api/cm_api.html#module-matplotlib.cm "matplotlib.cm")
.hot\_r)

def create\_axes(title, figsize\=(16, 6)):
    fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=figsize)
    fig.suptitle(title)

    \# define the axis for the first plot
    left, width \= 0.1, 0.22
    bottom, height \= 0.1, 0.7
    bottom\_h \= height + 0.15
    left\_h \= left + width + 0.02

    rect\_scatter \= \[left, bottom, width, height\]
    rect\_histx \= \[left, bottom\_h, width, 0.1\]
    rect\_histy \= \[left\_h, bottom, 0.05, height\]

    ax\_scatter \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_scatter)
    ax\_histx \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_histx)
    ax\_histy \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_histy)

    \# define the axis for the zoomed-in plot
    left \= width + left + 0.2
    left\_h \= left + width + 0.02

    rect\_scatter \= \[left, bottom, width, height\]
    rect\_histx \= \[left, bottom\_h, width, 0.1\]
    rect\_histy \= \[left\_h, bottom, 0.05, height\]

    ax\_scatter\_zoom \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_scatter)
    ax\_histx\_zoom \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_histx)
    ax\_histy\_zoom \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_histy)

    \# define the axis for the colorbar
    left, width \= width + left + 0.13, 0.01

    rect\_colorbar \= \[left, bottom, width, height\]
    ax\_colorbar \= [plt.axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")
(rect\_colorbar)

    return (
        (ax\_scatter, ax\_histy, ax\_histx),
        (ax\_scatter\_zoom, ax\_histy\_zoom, ax\_histx\_zoom),
        ax\_colorbar,
    )

def plot\_distribution(axes, X, y, hist\_nbins\=50, title\="", x0\_label\="", x1\_label\=""):
    ax, hist\_X1, hist\_X0 \= axes

    ax.set\_title(title)
    ax.set\_xlabel(x0\_label)
    ax.set\_ylabel(x1\_label)

    \# The scatter plot
    colors \= cmap(y)
    ax.scatter(X\[:, 0\], X\[:, 1\], alpha\=0.5, marker\="o", s\=5, lw\=0, c\=colors)

    \# Removing the top and the right spine for aesthetics
    \# make nice axis layout
    ax.spines\["top"\].set\_visible(False)
    ax.spines\["right"\].set\_visible(False)
    ax.get\_xaxis().tick\_bottom()
    ax.get\_yaxis().tick\_left()
    ax.spines\["left"\].set\_position(("outward", 10))
    ax.spines\["bottom"\].set\_position(("outward", 10))

    \# Histogram for axis X1 (feature 5)
    hist\_X1.set\_ylim(ax.get\_ylim())
    hist\_X1.hist(
        X\[:, 1\], bins\=hist\_nbins, orientation\="horizontal", color\="grey", ec\="grey"
    )
    hist\_X1.axis("off")

    \# Histogram for axis X0 (feature 0)
    hist\_X0.set\_xlim(ax.get\_xlim())
    hist\_X0.hist(
        X\[:, 0\], bins\=hist\_nbins, orientation\="vertical", color\="grey", ec\="grey"
    )
    hist\_X0.axis("off")

Copy to clipboard

Two plots will be shown for each scaler/normalizer/transformer. The left figure will show a scatter plot of the full data set while the right figure will exclude the extreme values considering only 99 % of the data set, excluding marginal outliers. In addition, the marginal distributions for each feature will be shown on the sides of the scatter plot.

def make\_plot(item\_idx):
    title, X \= distributions\[item\_idx\]
    ax\_zoom\_out, ax\_zoom\_in, ax\_colorbar \= create\_axes(title)
    axarr \= (ax\_zoom\_out, ax\_zoom\_in)
    plot\_distribution(
        axarr\[0\],
        X,
        y,
        hist\_nbins\=200,
        x0\_label\=feature\_mapping\[features\[0\]\],
        x1\_label\=feature\_mapping\[features\[1\]\],
        title\="Full data",
    )

    \# zoom-in
    zoom\_in\_percentile\_range \= (0, 99)
    cutoffs\_X0 \= [np.percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
(X\[:, 0\], zoom\_in\_percentile\_range)
    cutoffs\_X1 \= [np.percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
(X\[:, 1\], zoom\_in\_percentile\_range)

    non\_outliers\_mask \= [np.all](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
(X \> \[cutoffs\_X0\[0\], cutoffs\_X1\[0\]\], axis\=1) & [np.all](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
(
        X < \[cutoffs\_X0\[1\], cutoffs\_X1\[1\]\], axis\=1
    )
    plot\_distribution(
        axarr\[1\],
        X\[non\_outliers\_mask\],
        y\[non\_outliers\_mask\],
        hist\_nbins\=50,
        x0\_label\=feature\_mapping\[features\[0\]\],
        x1\_label\=feature\_mapping\[features\[1\]\],
        title\="Zoom-in",
    )

    norm \= [mpl.colors.Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
(y\_full.min(), y\_full.max())
    [mpl.colorbar.ColorbarBase](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.ColorbarBase "matplotlib.colorbar.ColorbarBase")
(
        ax\_colorbar,
        cmap\=cmap,
        norm\=norm,
        orientation\="vertical",
        label\="Color mapping for values of y",
    )

Copy to clipboard

Original data[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#original-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Each transformation is plotted showing two transformed features, with the left plot showing the entire dataset, and the right zoomed-in to show the dataset without the marginal outliers. A large majority of the samples are compacted to a specific range, \[0, 10\] for the median income and \[0, 6\] for the average house occupancy. Note that there are some marginal outliers (some blocks have average occupancy of more than 1200). Therefore, a specific pre-processing can be very beneficial depending of the application. In the following, we present some insights and behaviors of those pre-processing methods in the presence of marginal outliers.

make\_plot(0)

Copy to clipboard

![Unscaled data, Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_001.png)

StandardScaler[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#standardscaler "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

[`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 removes the mean and scales the data to unit variance. The scaling shrinks the range of the feature values as shown in the left figure below. However, the outliers have an influence when computing the empirical mean and standard deviation. Note in particular that because the outliers on each feature have different magnitudes, the spread of the transformed data on each feature is very different: most of the data lie in the \[-2, 4\] range for the transformed median income feature while the same data is squeezed in the smaller \[-0.2, 0.2\] range for the transformed average house occupancy.

[`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 therefore cannot guarantee balanced feature scales in the presence of outliers.

make\_plot(1)

Copy to clipboard

![Data after standard scaling, Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_002.png)

MinMaxScaler[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#minmaxscaler "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

[`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
 rescales the data set such that all feature values are in the range \[0, 1\] as shown in the right panel below. However, this scaling compresses all inliers into the narrow range \[0, 0.005\] for the transformed average house occupancy.

Both [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
 and [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
 are very sensitive to the presence of outliers.

make\_plot(2)

Copy to clipboard

![Data after min-max scaling, Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_003.png)

MaxAbsScaler[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#maxabsscaler "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

[`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
 is similar to [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
 except that the values are mapped across several ranges depending on whether negative OR positive values are present. If only positive values are present, the range is \[0, 1\]. If only negative values are present, the range is \[-1, 0\]. If both negative and positive values are present, the range is \[-1, 1\]. On positive only data, both [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
 and [`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
 behave similarly. [`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
 therefore also suffers from the presence of large outliers.

make\_plot(3)

Copy to clipboard

![Data after max-abs scaling, Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_004.png)

RobustScaler[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#robustscaler "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Unlike the previous scalers, the centering and scaling statistics of [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
 are based on percentiles and are therefore not influenced by a small number of very large marginal outliers. Consequently, the resulting range of the transformed feature values is larger than for the previous scalers and, more importantly, are approximately similar: for both features most of the transformed values lie in a \[-2, 3\] range as seen in the zoomed-in figure. Note that the outliers themselves are still present in the transformed data. If a separate outlier clipping is desirable, a non-linear transformation is required (see below).

make\_plot(4)

Copy to clipboard

![Data after robust scaling, Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_005.png)

PowerTransformer[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#powertransformer "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

[`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
 applies a power transformation to each feature to make the data more Gaussian-like in order to stabilize variance and minimize skewness. Currently the Yeo-Johnson and Box-Cox transforms are supported and the optimal scaling factor is determined via maximum likelihood estimation in both methods. By default, [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
 applies zero-mean, unit variance normalization. Note that Box-Cox can only be applied to strictly positive data. Income and average house occupancy happen to be strictly positive, but if negative values are present the Yeo-Johnson transformed is preferred.

make\_plot(5)
make\_plot(6)

Copy to clipboard

*   ![Data after power transformation (Yeo-Johnson), Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_006.png)
*   ![Data after power transformation (Box-Cox), Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_007.png)

QuantileTransformer (uniform output)[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#quantiletransformer-uniform-output "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 applies a non-linear transformation such that the probability density function of each feature will be mapped to a uniform or Gaussian distribution. In this case, all the data, including outliers, will be mapped to a uniform distribution with the range \[0, 1\], making outliers indistinguishable from inliers.

[`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
 and [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 are robust to outliers in the sense that adding or removing outliers in the training set will yield approximately the same transformation. But contrary to [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
, [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 will also automatically collapse any outlier by setting them to the a priori defined range boundaries (0 and 1). This can result in saturation artifacts for extreme values.

make\_plot(7)

Copy to clipboard

![Data after quantile transformation (uniform pdf), Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_008.png)

QuantileTransformer (Gaussian output)[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#quantiletransformer-gaussian-output "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To map to a Gaussian distribution, set the parameter `output_distribution='normal'`.

make\_plot(8)

Copy to clipboard

![Data after quantile transformation (gaussian pdf), Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_009.png)

Normalizer[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#normalizer "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

The [`Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")
 rescales the vector for each sample to have unit norm, independently of the distribution of the samples. It can be seen on both figures below where all samples are mapped onto the unit circle. In our example the two selected features have only positive values; therefore the transformed data only lie in the positive quadrant. This would not be the case if some original features had a mix of positive and negative values.

make\_plot(9)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Data after sample-wise L2 normalizing, Full data, Zoom-in](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_010.png)

**Total running time of the script:** (0 minutes 7.806 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_all_scaling.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_all_scaling.ipynb)

[`Download Jupyter notebook: plot_all_scaling.ipynb`](https://scikit-learn.org/stable/_downloads/e60e99adef360baabc49b925646a39d9/plot_all_scaling.ipynb)

[`Download Python source code: plot_all_scaling.py`](https://scikit-learn.org/stable/_downloads/24475810034a0d0d190a9de0f87d72b5/plot_all_scaling.py)

[`Download zipped: plot_all_scaling.zip`](https://scikit-learn.org/stable/_downloads/8c94a38055d85a44378c1684b4c671ac/plot_all_scaling.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_map_data_to_normal_thumb.png)

[Map data to a normal distribution](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html)

Map data to a normal distribution

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_outlier_detection_bench_thumb.png)

[Evaluation of outlier detection estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_outlier_detection_bench.html)

Evaluation of outlier detection estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_theilsen_thumb.png)

[Theil-Sen Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_theilsen.html)

Theil-Sen Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_isolation_forest_thumb.png)

[IsolationForest example](https://scikit-learn.org/stable/auto_examples/ensemble/plot_isolation_forest.html)

IsolationForest example

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/24475810034a0d0d190a9de0f87d72b5/plot_all_scaling.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/e60e99adef360baabc49b925646a39d9/plot_all_scaling.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/8c94a38055d85a44378c1684b4c671ac/plot_all_scaling.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_all_scaling.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_all_scaling.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)