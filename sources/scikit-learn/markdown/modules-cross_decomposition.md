[Skip to main content](https://scikit-learn.org/stable/modules/cross_decomposition.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/cross_decomposition.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/cross_decomposition.html)
[1.8.0](https://scikit-learn.org/1.8/modules/cross_decomposition.html)
[1.7.2](https://scikit-learn.org/1.7/modules/cross_decomposition.html)
[1.6.1](https://scikit-learn.org/1.6/modules/cross_decomposition.html)
[1.5.2](https://scikit-learn.org/1.5/modules/cross_decomposition.html)
[1.4.2](https://scikit-learn.org/1.4/modules/cross_decomposition.html)

Collapse Sidebar Expand Sidebar

1.8. Cross decomposition[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#cross-decomposition "Link to this heading")

=========================================================================================================================================

The cross decomposition module contains **supervised** estimators for dimensionality reduction and regression, belonging to the “Partial Least Squares” family.

[![../_images/sphx_glr_plot_compare_cross_decomposition_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_compare_cross_decomposition_001.png)](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html)

Cross decomposition algorithms find the fundamental relations between two matrices (X and Y). They are latent variable approaches to modeling the covariance structures in these two spaces. They will try to find the multidimensional direction in the X space that explains the maximum multidimensional variance direction in the Y space. In other words, PLS projects both `X` and `Y` into a lower-dimensional subspace such that the covariance between `transformed(X)` and `transformed(Y)` is maximal.

PLS draws similarities with [Principal Component Regression](https://en.wikipedia.org/wiki/Principal_component_regression)
 (PCR), where the samples are first projected into a lower-dimensional subspace, and the targets `y` are predicted using `transformed(X)`. One issue with PCR is that the dimensionality reduction is unsupervised, and may lose some important variables: PCR would keep the features with the most variance, but it’s possible that features with small variances are relevant for predicting the target. In a way, PLS allows for the same kind of dimensionality reduction, but by taking into account the targets `y`. An illustration of this fact is given in the following example: \* [Principal Component Regression vs Partial Least Squares Regression](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#sphx-glr-auto-examples-cross-decomposition-plot-pcr-vs-pls-py)
.

Apart from CCA, the PLS estimators are particularly suited when the matrix of predictors has more variables than observations, and when there is multicollinearity among the features. By contrast, standard linear regression would fail in these cases unless it is regularized.

Classes included in this module are [`PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
, [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
, [`CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
 and [`PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")

1.8.1. PLSCanonical[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#plscanonical "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

We here describe the algorithm used in [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
. The other estimators use variants of this algorithm, and are detailed below. We recommend section [\[1\]](https://scikit-learn.org/stable/modules/cross_decomposition.html#id6)
 for more details and comparisons between these algorithms. In [\[1\]](https://scikit-learn.org/stable/modules/cross_decomposition.html#id6)
, [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
 corresponds to “PLSW2A”.

Given two centered matrices X∈Rn×d and Y∈Rn×t, and a number of components K, [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
 proceeds as follows:

Set X1 to X and Y1 to Y. Then, for each k∈\[1,K\]:

*   a) compute uk∈Rd and vk∈Rt, the first left and right singular vectors of the cross-covariance matrix C\=XkTYk. uk and vk are called the _weights_. By definition, uk and vk are chosen so that they maximize the covariance between the projected Xk and the projected target, that is Cov(Xkuk,Ykvk).
    
*   b) Project Xk and Yk on the singular vectors to obtain _scores_: ξk\=Xkuk and ωk\=Ykvk
    
*   c) Regress Xk on ξk, i.e. find a vector γk∈Rd such that the rank-1 matrix ξkγkT is as close as possible to Xk. Do the same on Yk with ωk to obtain δk. The vectors γk and δk are called the _loadings_.
    
*   d) _deflate_ Xk and Yk, i.e. subtract the rank-1 approximations: Xk+1\=Xk−ξkγkT, and Yk+1\=Yk−ωkδkT.
    

At the end, we have approximated X as a sum of rank-1 matrices: X\=ΞΓT where Ξ∈Rn×K contains the scores in its columns, and ΓT∈RK×d contains the loadings in its rows. Similarly for Y, we have Y\=ΩΔT.

Note that the scores matrices Ξ and Ω correspond to the projections of the training data X and Y, respectively.

Step _a)_ may be performed in two ways: either by computing the whole SVD of C and only retaining the singular vectors with the biggest singular values, or by directly computing the singular vectors using the power method (cf section 11.3 in [\[1\]](https://scikit-learn.org/stable/modules/cross_decomposition.html#id6)
), which corresponds to the `'nipals'` option of the `algorithm` parameter.

Transforming data[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#transforming-data "Link to this dropdown")

To transform X into X¯, we need to find a projection matrix P such that X¯\=XP. We know that for the training data, Ξ\=XP, and X\=ΞΓT. Setting P\=U(ΓTU)−1 where U is the matrix with the uk in the columns, we have XP\=XU(ΓTU)−1\=Ξ(ΓTU)(ΓTU)−1\=Ξ as desired. The rotation matrix P can be accessed from the `x_rotations_` attribute.

Similarly, Y can be transformed using the rotation matrix V(ΔTV)−1, accessed via the `y_rotations_` attribute.

Predicting the targets `Y`[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#predicting-the-targets-y "Link to this dropdown")

To predict the targets of some data X, we are looking for a coefficient matrix β∈Rd×t such that Y\=Xβ.

The idea is to try to predict the transformed targets Ω as a function of the transformed samples Ξ, by computing α∈R such that Ω\=αΞ.

Then, we have Y\=ΩΔT\=αΞΔT, and since Ξ is the transformed training data we have that Y\=XαPΔT, and as a result the coefficient matrix β\=αPΔT.

β can be accessed through the `coef_` attribute.

1.8.2. PLSSVD[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#plssvd "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

[`PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
 is a simplified version of [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
 described earlier: instead of iteratively deflating the matrices Xk and Yk, [`PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
 computes the SVD of C\=XTY only _once_, and stores the `n_components` singular vectors corresponding to the biggest singular values in the matrices `U` and `V`, corresponding to the `x_weights_` and `y_weights_` attributes. Here, the transformed data is simply `transformed(X) = XU` and `transformed(Y) = YV`.

If `n_components == 1`, [`PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")
 and [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
 are strictly equivalent.

1.8.3. PLSRegression[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#plsregression "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

The [`PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
 estimator is similar to [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
 with `algorithm='nipals'`, with 2 significant differences:

*   at step a) in the power method to compute uk and vk, vk is never normalized.
    
*   at step c), the targets Yk are approximated using the projection of Xk (i.e. ξk) instead of the projection of Yk (i.e. ωk). In other words, the loadings computation is different. As a result, the deflation in step d) will also be affected.
    

These two modifications affect the output of `predict` and `transform`, which are not the same as for [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
. Also, while the number of components is limited by `min(n_samples, n_features, n_targets)` in [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
, here the limit is the rank of XTX, i.e. `min(n_samples, n_features)`.

[`PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
 is also known as PLS1 (single targets) and PLS2 (multiple targets). Much like [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
, [`PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
 is a form of regularized linear regression where the number of components controls the strength of the regularization.

1.8.4. Canonical Correlation Analysis[#](https://scikit-learn.org/stable/modules/cross_decomposition.html#canonical-correlation-analysis "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Canonical Correlation Analysis was developed prior and independently to PLS. But it turns out that [`CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
 is a special case of PLS, and corresponds to PLS in “Mode B” in the literature.

[`CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
 differs from [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
 in the way the weights uk and vk are computed in the power method of step a). Details can be found in section 10 of [\[1\]](https://scikit-learn.org/stable/modules/cross_decomposition.html#id6)
.

Since [`CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
 involves the inversion of XkTXk and YkTYk, this estimator can be unstable if the number of features or targets is greater than the number of samples.

References

Examples

*   [Compare cross decomposition methods](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_compare_cross_decomposition.html#sphx-glr-auto-examples-cross-decomposition-plot-compare-cross-decomposition-py)
    
*   [Principal Component Regression vs Partial Least Squares Regression](https://scikit-learn.org/stable/auto_examples/cross_decomposition/plot_pcr_vs_pls.html#sphx-glr-auto-examples-cross-decomposition-plot-pcr-vs-pls-py)
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)