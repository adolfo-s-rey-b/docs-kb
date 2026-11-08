[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.linear_model.ridge_regression.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.ridge_regression.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.linear_model.ridge_regression.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.ridge_regression.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.ridge_regression.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.linear_model.ridge_regression.html)

Collapse Sidebar Expand Sidebar

ridge\_regression[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#ridge-regression "Link to this heading")

===========================================================================================================================================================

sklearn.linear\_model.ridge\_regression(_X_, _y_, _alpha_, _\*_, _sample\_weight\=None_, _solver\='auto'_, _max\_iter\=None_, _tol\=0.0001_, _verbose\=0_, _positive\=False_, _random\_state\=None_, _return\_n\_iter\=False_, _return\_intercept\=False_, _check\_input\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/linear_model/_ridge.py#L389)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "Link to this definition")

Solve the ridge equation by the method of normal equations.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)
.

Parameters:

**X**{array-like, sparse matrix, LinearOperator} of shape (n\_samples, n\_features)

Training data.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_targets)

Target values.

**alpha**float or array-like of shape (n\_targets,)

Constant that multiplies the L2 term, controlling regularization strength. `alpha` must be a non-negative float i.e. in `[0, inf)`.\
\
When `alpha = 0`, the objective is equivalent to ordinary least squares, solved by the [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")\
 object. For numerical reasons, using `alpha = 0` with the `Ridge` object is not advised. Instead, you should use the [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")\
 object.\
\
If an array is passed, penalties are assumed to be specific to the targets. Hence they must correspond in number.\
\
For an illustration of the effect of alpha on the model coefficients, see [Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#sphx-glr-auto-examples-linear-model-plot-ridge-coeffs-py)\
.\
\
**sample\_weight**float or array-like of shape (n\_samples,), default=None\
\
Individual weights for each sample. If given a float, every sample will have the same weight. If sample\_weight is not None and solver=’auto’, the solver will be set to ‘cholesky’.\
\
Added in version 0.17.\
\
**solver**{‘auto’, ‘svd’, ‘cholesky’, ‘lsqr’, ‘sparse\_cg’, ‘sag’, ‘saga’, ‘lbfgs’}, default=’auto’\
\
Solver to use in the computational routines:\
\
*   ‘auto’ chooses the solver automatically based on the type of data.\
    \
*   ‘svd’ uses a Singular Value Decomposition of X to compute the Ridge coefficients. It is the most stable solver, in particular more stable for singular matrices than ‘cholesky’ at the cost of being slower.\
    \
*   ‘cholesky’ uses the standard scipy.linalg.solve function to obtain a closed-form solution via a Cholesky decomposition of dot(X.T, X)\
    \
*   ‘sparse\_cg’ uses the conjugate gradient solver as found in scipy.sparse.linalg.cg. As an iterative algorithm, this solver is more appropriate than ‘cholesky’ for large-scale data (possibility to set `tol` and `max_iter`).\
    \
*   ‘lsqr’ uses the dedicated regularized least-squares routine scipy.sparse.linalg.lsqr. It is the fastest and uses an iterative procedure.\
    \
*   ‘sag’ uses a Stochastic Average Gradient descent, and ‘saga’ uses its improved, unbiased version named SAGA. Both methods also use an iterative procedure, and are often faster than other solvers when both n\_samples and n\_features are large. Note that ‘sag’ and ‘saga’ fast convergence is only guaranteed on features with approximately the same scale. You can preprocess the data with a scaler from sklearn.preprocessing.\
    \
*   ‘lbfgs’ uses L-BFGS-B algorithm implemented in `scipy.optimize.minimize`. It can be used only when `positive` is True.\
    \
\
All solvers except ‘svd’ support both dense and sparse data. However, only ‘lsqr’, ‘sag’, ‘sparse\_cg’, and ‘lbfgs’ support sparse input when `fit_intercept` is True.\
\
Added in version 0.17: Stochastic Average Gradient descent solver.\
\
Added in version 0.19: SAGA solver.\
\
**max\_iter**int, default=None\
\
Maximum number of iterations for conjugate gradient solver. For the ‘sparse\_cg’ and ‘lsqr’ solvers, the default value is determined by scipy.sparse.linalg. For ‘sag’ and saga solver, the default value is 1000. For ‘lbfgs’ solver, the default value is 15000.\
\
**tol**float, default=1e-4\
\
Precision of the solution. Note that `tol` has no effect for solvers ‘svd’ and ‘cholesky’.\
\
Changed in version 1.2: Default value changed from 1e-3 to 1e-4 for consistency with other linear models.\
\
**verbose**int, default=0\
\
Verbosity level. Setting verbose > 0 will display additional information depending on the solver used.\
\
**positive**bool, default=False\
\
When set to `True`, forces the coefficients to be positive. Only ‘lbfgs’ solver is supported in this case.\
\
**random\_state**int, RandomState instance, default=None\
\
Used when `solver` == ‘sag’ or ‘saga’ to shuffle the data. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)\
 for details.\
\
**return\_n\_iter**bool, default=False\
\
If True, the method also returns `n_iter`, the actual number of iteration performed by the solver.\
\
Added in version 0.17.\
\
**return\_intercept**bool, default=False\
\
If True and if X is sparse, the method also returns the intercept, and the solver is automatically changed to ‘sag’. This is only a temporary fix for fitting the intercept with sparse data. For dense data, use sklearn.linear\_model.\_preprocess\_data before your regression.\
\
Added in version 0.17.\
\
**check\_input**bool, default=True\
\
If False, the input arrays X and y will not be checked.\
\
Added in version 0.21.\
\
Returns:\
\
**coef**ndarray of shape (n\_features,) or (n\_targets, n\_features)\
\
Weight vector(s).\
\
**n\_iter**int, optional\
\
The actual number of iteration performed by the solver. Only returned if `return_n_iter` is True.\
\
**intercept**float or ndarray of shape (n\_targets,)\
\
The intercept of the model. Only returned if `return_intercept` is True and if X is a scipy sparse array.\
\
Notes\
\
This function won’t compute the intercept.\
\
Regularization improves the conditioning of the problem and reduces the variance of the estimates. Larger values specify stronger regularization. Alpha corresponds to `1 / (2C)` in other linear models such as [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
 or [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
. If an array is passed, penalties are assumed to be specific to the targets. Hence they must correspond in number.\
\
Examples\
\
\>>> import numpy as np\
\>>> from sklearn.datasets import make\_regression\
\>>> from sklearn.linear\_model import ridge\_regression\
\>>> rng \= np.random.RandomState(0)\
\>>> X \= rng.randn(100, 4)\
\>>> y \= 2.0 \* X\[:, 0\] \- 1.0 \* X\[:, 1\] + 0.1 \* rng.standard\_normal(100)\
\>>> coef, intercept \= ridge\_regression(X, y, alpha\=1.0, return\_intercept\=True,\
...                                    random\_state\=0)\
\>>> coef\
array(\[ 1.97, -1., -2.69e-3, -9.27e-4 \])\
\>>> intercept\
np.float64(-.0012)\
\
Copy to clipboard\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)