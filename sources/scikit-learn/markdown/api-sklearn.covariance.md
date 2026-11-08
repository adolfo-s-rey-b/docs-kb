[Skip to main content](https://scikit-learn.org/stable/api/sklearn.covariance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

sklearn.covariance[#](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "Link to this heading")

====================================================================================================================================

Methods and algorithms to robustly estimate covariance.

They estimate the covariance of features at given sets of points, as well as the precision matrix defined as the inverse of the covariance. Covariance estimation is closely related to the theory of Gaussian graphical models.

**User guide.** See the [Covariance estimation](https://scikit-learn.org/stable/modules/covariance.html#covariance)
 section for further details.

|     |     |
| --- | --- |
| [`EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope") | An object for detecting outliers in a Gaussian distributed dataset. |
| [`EmpiricalCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance") | Maximum likelihood covariance estimator. |
| [`GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso") | Sparse inverse covariance estimation with an l1-penalized estimator. |
| [`GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV") | Sparse inverse covariance w/ cross-validated choice of the l1 penalty. |
| [`LedoitWolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf") | LedoitWolf Estimator. |
| [`MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet") | Minimum Covariance Determinant (MCD): robust estimator of covariance. |
| [`OAS`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS") | Oracle Approximating Shrinkage Estimator. |
| [`ShrunkCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance") | Covariance estimator with shrinkage. |
| [`empirical_covariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#sklearn.covariance.empirical_covariance "sklearn.covariance.empirical_covariance") | Compute the Maximum likelihood covariance estimator. |
| [`graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso") | L1-penalized covariance estimator. |
| [`ledoit_wolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "sklearn.covariance.ledoit_wolf") | Estimate the shrunk Ledoit-Wolf covariance matrix. |
| [`ledoit_wolf_shrinkage`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf_shrinkage.html#sklearn.covariance.ledoit_wolf_shrinkage "sklearn.covariance.ledoit_wolf_shrinkage") | Estimate the shrunk Ledoit-Wolf covariance matrix. |
| [`oas`](https://scikit-learn.org/stable/modules/generated/oas-function.html#sklearn.covariance.oas "sklearn.covariance.oas") | Estimate covariance with the Oracle Approximating Shrinkage. |
| [`shrunk_covariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html#sklearn.covariance.shrunk_covariance "sklearn.covariance.shrunk_covariance") | Calculate covariance matrices shrunk on the diagonal. |