[Skip to main content](https://scikit-learn.org/stable/modules/density.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/density.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/density.html)
[1.8.0](https://scikit-learn.org/1.8/modules/density.html)
[1.7.2](https://scikit-learn.org/1.7/modules/density.html)
[1.6.1](https://scikit-learn.org/1.6/modules/density.html)
[1.5.2](https://scikit-learn.org/1.5/modules/density.html)
[1.4.2](https://scikit-learn.org/1.4/modules/density.html)

Collapse Sidebar Expand Sidebar

2.8. Density Estimation[#](https://scikit-learn.org/stable/modules/density.html#density-estimation "Link to this heading")

===========================================================================================================================

Density estimation walks the line between unsupervised learning, feature engineering, and data modeling. Some of the most popular and useful density estimation techniques are mixture models such as Gaussian Mixtures ([`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
), and neighbor-based approaches such as the kernel density estimate ([`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
). Gaussian Mixtures are discussed more fully in the context of [clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering)
, because the technique is also useful as an unsupervised clustering scheme.

Density estimation is a very simple concept, and most people are already familiar with one common density estimation technique: the histogram.

2.8.1. Density Estimation: Histograms[#](https://scikit-learn.org/stable/modules/density.html#density-estimation-histograms "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

A histogram is a simple visualization of data where bins are defined, and the number of data points within each bin is tallied. An example of a histogram can be seen in the upper-left panel of the following figure:

**[![hist_to_kde](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_001.png)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)
**

A major problem with histograms, however, is that the choice of binning can have a disproportionate effect on the resulting visualization. Consider the upper-right panel of the above figure. It shows a histogram over the same data, with the bins shifted right. The results of the two visualizations look entirely different, and might lead to different interpretations of the data.

Intuitively, one can also think of a histogram as a stack of blocks, one block per point. By stacking the blocks in the appropriate grid space, we recover the histogram. But what if, instead of stacking the blocks on a regular grid, we center each block on the point it represents, and sum the total height at each location? This idea leads to the lower-left visualization. It is perhaps not as clean as a histogram, but the fact that the data drive the block locations means that it is a much better representation of the underlying data.

This visualization is an example of a _kernel density estimation_, in this case with a top-hat kernel (i.e. a square block at each point). We can recover a smoother distribution by using a smoother kernel. The bottom-right plot shows a Gaussian kernel density estimate, in which each point contributes a Gaussian curve to the total. The result is a smooth density estimate which is derived from the data, and functions as a powerful non-parametric model of the distribution of points.

2.8.2. Kernel Density Estimation[#](https://scikit-learn.org/stable/modules/density.html#kernel-density-estimation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

Kernel density estimation in scikit-learn is implemented in the [`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
 estimator, which uses the Ball Tree or KD Tree for efficient queries (see [Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html#neighbors)
 for a discussion of these). Though the above example uses a 1D data set for simplicity, kernel density estimation can be performed in any number of dimensions, though in practice the curse of dimensionality causes its performance to degrade in high dimensions.

In the following figure, 100 points are drawn from a bimodal distribution, and the kernel density estimates are shown for three choices of kernels:

**[![kde_1d_distribution](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_003.png)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)
**

It’s clear how the kernel shape affects the smoothness of the resulting distribution. The scikit-learn kernel density estimator can be used as follows:

\>>> from sklearn.neighbors import KernelDensity
\>>> import numpy as np
\>>> X \= np.array(\[\[\-1, \-1\], \[\-2, \-1\], \[\-3, \-2\], \[1, 1\], \[2, 1\], \[3, 2\]\])
\>>> kde \= KernelDensity(kernel\='gaussian', bandwidth\=0.2).fit(X)
\>>> kde.score\_samples(X)
array(\[-0.41075698, -0.41075698, -0.41076071, -0.41075698, -0.41075698,\
       -0.41076071\])

Copy to clipboard

Here we have used `kernel='gaussian'`, as seen above. Mathematically, a kernel is a positive function K(x;h) which is controlled by the bandwidth parameter h. Given this kernel form, the density estimate at a point y within a group of points xi;i\=1,⋯,N is given by:

ρK(y)\=∑i\=1NK(y−xi;h)

The bandwidth here acts as a smoothing parameter, controlling the tradeoff between bias and variance in the result. A large bandwidth leads to a very smooth (i.e. high-bias) density distribution. A small bandwidth leads to an unsmooth (i.e. high-variance) density distribution.

The parameter `bandwidth` controls this smoothing. One can either set manually this parameter or use Scott’s and Silverman’s estimation methods.

[`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
 implements several common kernel forms, which are shown in the following figure:

**[![kde_kernels](https://scikit-learn.org/stable/_images/sphx_glr_plot_kde_1d_002.png)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html)
**

Kernels’ mathematical expressions[#](https://scikit-learn.org/stable/modules/density.html#kernels%E2%80%99-mathematical-expressions "Link to this dropdown")

The form of these kernels is as follows:

*   Gaussian kernel (`kernel = 'gaussian'`)
    
    K(x;h)∝exp⁡(−x22h2)
    
*   Tophat kernel (`kernel = 'tophat'`)
    
    K(x;h)∝1 if x<h
    
*   Epanechnikov kernel (`kernel = 'epanechnikov'`)
    
    K(x;h)∝1−x2h2
    
*   Exponential kernel (`kernel = 'exponential'`)
    
    K(x;h)∝exp⁡(−x/h)
    
*   Linear kernel (`kernel = 'linear'`)
    
    K(x;h)∝1−x/h if x<h
    
*   Cosine kernel (`kernel = 'cosine'`)
    
    K(x;h)∝cos⁡(πx2h) if x<h
    

The kernel density estimator can be used with any of the valid distance metrics (see [`DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
 for a list of available metrics), though the results are properly normalized only for the Euclidean metric. One particularly useful metric is the [Haversine distance](https://en.wikipedia.org/wiki/Haversine_formula)
 which measures the angular distance between points on a sphere. Here is an example of using a kernel density estimate for a visualization of geospatial data, in this case the distribution of observations of two different species on the South American continent:

**[![species_kde](https://scikit-learn.org/stable/_images/sphx_glr_plot_species_kde_001.png)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html)
**

One other useful application of kernel density estimation is to learn a non-parametric generative model of a dataset in order to efficiently draw new samples from this generative model. Here is an example of using this process to create a new set of hand-written digits, using a Gaussian kernel learned on a PCA projection of the data:

**[![digits_kde](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_kde_sampling_001.png)](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html)
**

The “new” data consists of linear combinations of the input data, with weights probabilistically drawn given the KDE model.

Examples

*   [Simple 1D Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_kde_1d.html#sphx-glr-auto-examples-neighbors-plot-kde-1d-py)
    : computation of simple kernel density estimates in one dimension.
    
*   [Kernel Density Estimation](https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html#sphx-glr-auto-examples-neighbors-plot-digits-kde-sampling-py)
    : an example of using Kernel Density estimation to learn a generative model of the hand-written digits data, and drawing new samples from this model.
    
*   [Kernel Density Estimate of Species Distributions](https://scikit-learn.org/stable/auto_examples/neighbors/plot_species_kde.html#sphx-glr-auto-examples-neighbors-plot-species-kde-py)
    : an example of Kernel Density estimation using the Haversine distance metric to visualize geospatial data
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)