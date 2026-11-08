[Skip to main content](https://scikit-learn.org/stable/modules/kernel_approximation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/kernel_approximation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/kernel_approximation.html)
[1.8.0](https://scikit-learn.org/1.8/modules/kernel_approximation.html)
[1.7.2](https://scikit-learn.org/1.7/modules/kernel_approximation.html)
[1.6.1](https://scikit-learn.org/1.6/modules/kernel_approximation.html)
[1.5.2](https://scikit-learn.org/1.5/modules/kernel_approximation.html)
[1.4.2](https://scikit-learn.org/1.4/modules/kernel_approximation.html)

Collapse Sidebar Expand Sidebar

8.7. Kernel Approximation[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation "Link to this heading")

============================================================================================================================================

This submodule contains functions that approximate the feature mappings that correspond to certain kernels, as they are used for example in support vector machines (see [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html#svm)
). The following feature functions perform non-linear transformations of the input, which can serve as a basis for linear classification or other algorithms.

The advantage of using approximate explicit feature maps compared to the [kernel trick](https://en.wikipedia.org/wiki/Kernel_trick)
, which makes use of feature maps implicitly, is that explicit mappings can be better suited for online learning and can significantly reduce the cost of learning with very large datasets. Standard kernelized SVMs do not scale well to large datasets, but using an approximate kernel map it is possible to use much more efficient linear SVMs. In particular, the combination of kernel map approximations with [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 can make non-linear learning on large datasets possible.

Since there has not been much empirical work using approximate embeddings, it is advisable to compare results against exact kernel methods when possible.

See also

[Polynomial regression: extending linear models with basis functions](https://scikit-learn.org/stable/modules/linear_model.html#polynomial-regression)
 for an exact polynomial transformation.

8.7.1. Nystroem Method for Kernel Approximation[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#nystroem-method-for-kernel-approximation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Nystroem method, as implemented in [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 is a general method for reduced rank approximations of kernels. It achieves this by subsampling without replacement rows/columns of the data on which the kernel is evaluated. While the computational complexity of the exact method is O(nsamples3), the complexity of the approximation is O(ncomponents2⋅nsamples), where one can set ncomponents≪nsamples without a significant decrease in performance [\[WS2001\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#ws2001)
.

We can construct the eigendecomposition of the kernel matrix K, based on the features of the data, and then split it into sampled and unsampled data points.

K\=UΛUT\=\[U1U2\]Λ\[U1U2\]T\=\[U1ΛU1TU1ΛU2TU2ΛU1TU2ΛU2T\]≡\[K11K12K21K22\]

where:

*   U is orthonormal
    
*   Λ is diagonal matrix of eigenvalues
    
*   U1 is orthonormal matrix of samples that were chosen
    
*   U2 is orthonormal matrix of samples that were not chosen
    

Given that U1ΛU1T can be obtained by orthonormalization of the matrix K11, and U2ΛU1T can be evaluated (as well as its transpose), the only remaining term to elucidate is U2ΛU2T. To do this we can express it in terms of the already evaluated matrices:

U2ΛU2T\=(K21U1Λ−1)Λ(K21U1Λ−1)T\=K21U1(Λ−1Λ)Λ−1U1TK21T\=K21U1Λ−1U1TK21T\=K21K11−1K21T\=(K21K11−12)(K21K11−12)T.

During `fit`, the class [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 evaluates the basis U1, and computes the normalization constant, K11−12. Later, during `transform`, the kernel matrix is determined between the basis (given by the `components_` attribute) and the new data points, `X`. This matrix is then multiplied by the `normalization_` matrix for the final result.

By default [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 uses the `rbf` kernel, but it can use any kernel function or a precomputed kernel matrix. The number of samples used - which is also the dimensionality of the features computed - is given by the parameter `n_components`.

Examples

*   See the example entitled [Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html#sphx-glr-auto-examples-applications-plot-cyclical-feature-engineering-py)
    , that shows an efficient machine learning pipeline that uses a [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     kernel.
    
*   See [Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#sphx-glr-auto-examples-miscellaneous-plot-kernel-approximation-py)
     for a comparison of [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     kernel with [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
    .
    

8.7.2. Radial Basis Function Kernel[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#radial-basis-function-kernel "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
 constructs an approximate mapping for the radial basis function kernel, also known as _Random Kitchen Sinks_ [\[RR2007\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#rr2007)
. This transformation can be used to explicitly model a kernel map, prior to applying a linear algorithm, for example a linear SVM:

\>>> from sklearn.kernel\_approximation import RBFSampler
\>>> from sklearn.linear\_model import SGDClassifier
\>>> X \= \[\[0, 0\], \[1, 1\], \[1, 0\], \[0, 1\]\]
\>>> y \= \[0, 0, 1, 1\]
\>>> rbf\_feature \= RBFSampler(gamma\=1, random\_state\=1)
\>>> X\_features \= rbf\_feature.fit\_transform(X)
\>>> clf \= SGDClassifier(max\_iter\=5)
\>>> clf.fit(X\_features, y)
SGDClassifier(max\_iter=5)
\>>> clf.score(X\_features, y)
1.0

Copy to clipboard

The mapping relies on a Monte Carlo approximation to the kernel values. The `fit` function performs the Monte Carlo sampling, whereas the `transform` method performs the mapping of the data. Because of the inherent randomness of the process, results may vary between different calls to the `fit` function.

The `fit` function takes two arguments: `n_components`, which is the target dimensionality of the feature transform, and `gamma`, the parameter of the RBF-kernel. A higher `n_components` will result in a better approximation of the kernel and will yield results more similar to those produced by a kernel SVM. Note that “fitting” the feature function does not actually depend on the data given to the `fit` function. Only the dimensionality of the data is used. Details on the method can be found in [\[RR2007\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#rr2007)
.

For a given value of `n_components` [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
 is often less accurate as [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
. [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
 is cheaper to compute, though, making use of larger feature spaces more efficient.

[![../_images/sphx_glr_plot_kernel_approximation_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_002.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)

Comparing an exact RBF kernel (left) with the approximation (right)[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#id12 "Link to this image")

Examples

*   See [Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#sphx-glr-auto-examples-miscellaneous-plot-kernel-approximation-py)
     for a comparison of [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
     kernel with [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
    .
    

8.7.3. Additive Chi Squared Kernel[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#additive-chi-squared-kernel "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

The additive chi squared kernel is a kernel on histograms, often used in computer vision.

The additive chi squared kernel as used here is given by

k(x,y)\=∑i2xiyixi+yi

This is not exactly the same as [`sklearn.metrics.pairwise.additive_chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#sklearn.metrics.pairwise.additive_chi2_kernel "sklearn.metrics.pairwise.additive_chi2_kernel")
. The authors of [\[VZ2010\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#vz2010)
 prefer the version above as it is always positive definite. Since the kernel is additive, it is possible to treat all components xi separately for embedding. This makes it possible to sample the Fourier transform in regular intervals, instead of approximating using Monte Carlo sampling.

The class [`AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")
 implements this component wise deterministic sampling. Each component is sampled n times, yielding 2n+1 dimensions per input dimension (the multiple of two stems from the real and complex part of the Fourier transform). In the literature, n is usually chosen to be 1 or 2, transforming the dataset to size `n_samples * 5 * n_features` (in the case of n\=2).

The approximate feature map provided by [`AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")
 can be combined with the approximate feature map provided by [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
 to yield an approximate feature map for the exponentiated chi squared kernel. See the [\[VZ2010\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#vz2010)
 for details and [\[VVZ2010\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#vvz2010)
 for combination with the [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
.

8.7.4. Skewed Chi Squared Kernel[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#skewed-chi-squared-kernel "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

The skewed chi squared kernel is given by:

k(x,y)\=∏i2xi+cyi+cxi+yi+2c

It has properties that are similar to the exponentiated chi squared kernel often used in computer vision, but allows for a simple Monte Carlo approximation of the feature map.

The usage of the [`SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")
 is the same as the usage described above for the [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
. The only difference is in the free parameter, that is called c. For a motivation for this mapping and the mathematical details see [\[LS2010\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#ls2010)
.

8.7.5. Polynomial Kernel Approximation via Tensor Sketch[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#polynomial-kernel-approximation-via-tensor-sketch "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [polynomial kernel](https://scikit-learn.org/stable/modules/metrics.html#polynomial-kernel)
 is a popular type of kernel function given by:

k(x,y)\=(γx⊤y+c0)d

where:

*   `x`, `y` are the input vectors
    
*   `d` is the kernel degree
    

Intuitively, the feature space of the polynomial kernel of degree `d` consists of all possible degree-`d` products among input features, which enables learning algorithms using this kernel to account for interactions between features.

The TensorSketch [\[PP2013\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#pp2013)
 method, as implemented in [`PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch")
, is a scalable, input data independent method for polynomial kernel approximation. It is based on the concept of Count sketch [\[WIKICS\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#wikics)
 [\[CCF2002\]](https://scikit-learn.org/stable/modules/kernel_approximation.html#ccf2002)
 , a dimensionality reduction technique similar to feature hashing, which instead uses several independent hash functions. TensorSketch obtains a Count Sketch of the outer product of two vectors (or a vector with itself), which can be used as an approximation of the polynomial kernel feature space. In particular, instead of explicitly computing the outer product, TensorSketch computes the Count Sketch of the vectors and then uses polynomial multiplication via the Fast Fourier Transform to compute the Count Sketch of their outer product.

Conveniently, the training phase of TensorSketch simply consists of initializing some random variables. It is thus independent of the input data, i.e. it only depends on the number of input features, but not the data values. In addition, this method can transform samples in O(nsamples(nfeatures+ncomponentslog⁡(ncomponents))) time, where ncomponents is the desired output dimension, determined by `n_components`.

Examples

*   [Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html#sphx-glr-auto-examples-kernel-approximation-plot-scalable-poly-kernels-py)
    

8.7.6. Mathematical Details[#](https://scikit-learn.org/stable/modules/kernel_approximation.html#mathematical-details "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Kernel methods like support vector machines or kernelized PCA rely on a property of reproducing kernel Hilbert spaces. For any positive definite kernel function k (a so called Mercer kernel), it is guaranteed that there exists a mapping ϕ into a Hilbert space H, such that

k(x,y)\=⟨ϕ(x),ϕ(y)⟩

Where ⟨⋅,⋅⟩ denotes the inner product in the Hilbert space.

If an algorithm, such as a linear support vector machine or PCA, relies only on the scalar product of data points xi, one may use the value of k(xi,xj), which corresponds to applying the algorithm to the mapped data points ϕ(xi). The advantage of using k is that the mapping ϕ never has to be calculated explicitly, allowing for arbitrary large features (even infinite).

One drawback of kernel methods is, that it might be necessary to store many kernel values k(xi,xj) during optimization. If a kernelized classifier is applied to new data yj, k(xi,yj) needs to be computed to make predictions, possibly for many different xi in the training set.

The classes in this submodule allow to approximate the embedding ϕ, thereby working explicitly with the representations ϕ(xi), which obviates the need to apply the kernel or store training examples.

References

\[[WS2001](https://scikit-learn.org/stable/modules/kernel_approximation.html#id2)\
\]

[“Using the Nyström method to speed up kernel machines”](https://papers.nips.cc/paper_files/paper/2000/hash/19de10adbaa1b2ee13f77f679fa1483a-Abstract.html)
 Williams, C.K.I.; Seeger, M. - 2001.

\[RR2007\] ([1](https://scikit-learn.org/stable/modules/kernel_approximation.html#id3)
,[2](https://scikit-learn.org/stable/modules/kernel_approximation.html#id4)
)

[“Random features for large-scale kernel machines”](https://papers.nips.cc/paper/2007/hash/013a006f03dbc5392effeb8f18fda755-Abstract.html)
 Rahimi, A. and Recht, B. - Advances in neural information processing 2007,

\[[LS2010](https://scikit-learn.org/stable/modules/kernel_approximation.html#id8)\
\]

[“Random Fourier approximations for skewed multiplicative histogram kernels”](https://www.researchgate.net/publication/221114584_Random_Fourier_Approximations_for_Skewed_Multiplicative_Histogram_Kernels)
 Li, F., Ionescu, C., and Sminchisescu, C. - Pattern Recognition, DAGM 2010, Lecture Notes in Computer Science.

\[VZ2010\] ([1](https://scikit-learn.org/stable/modules/kernel_approximation.html#id5)
,[2](https://scikit-learn.org/stable/modules/kernel_approximation.html#id6)
)

[“Efficient additive kernels via explicit feature maps”](https://www.robots.ox.ac.uk/~vgg/publications/2011/Vedaldi11/vedaldi11.pdf)
 Vedaldi, A. and Zisserman, A. - Computer Vision and Pattern Recognition 2010

\[[VVZ2010](https://scikit-learn.org/stable/modules/kernel_approximation.html#id7)\
\]

[“Generalized RBF feature maps for Efficient Detection”](https://www.robots.ox.ac.uk/~vgg/publications/2010/Sreekanth10/sreekanth10.pdf)
 Vempati, S. and Vedaldi, A. and Zisserman, A. and Jawahar, CV - 2010

\[[PP2013](https://scikit-learn.org/stable/modules/kernel_approximation.html#id9)\
\]

[“Fast and scalable polynomial kernels via explicit feature maps”](https://doi.org/10.1145/2487575.2487591)
 Pham, N., & Pagh, R. - 2013

\[[CCF2002](https://scikit-learn.org/stable/modules/kernel_approximation.html#id11)\
\]

[“Finding frequent items in data streams”](https://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarCF.pdf)
 Charikar, M., Chen, K., & Farach-Colton - 2002

\[[WIKICS](https://scikit-learn.org/stable/modules/kernel_approximation.html#id10)\
\]

[“Wikipedia: Count sketch”](https://en.wikipedia.org/wiki/Count_sketch)

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)