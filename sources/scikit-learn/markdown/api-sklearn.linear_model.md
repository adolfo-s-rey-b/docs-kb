[Skip to main content](https://scikit-learn.org/stable/api/sklearn.linear_model.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.linear_model.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.linear_model.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.linear_model.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.linear_model.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.linear_model.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.linear_model.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.linear_model.html)

Collapse Sidebar Expand Sidebar

sklearn.linear\_model[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "Link to this heading")

===========================================================================================================================================

A variety of linear models.

**User guide.** See the [Linear Models](https://scikit-learn.org/stable/modules/linear_model.html#linear-model)
 section for further details.

The following subsections are only rough guidelines: the same estimator can fall into multiple categories, depending on its parameters.

Linear classifiers[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#linear-classifiers "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression") | Logistic Regression (aka logit, MaxEnt) classifier. |
| [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV") | Logistic Regression CV (aka logit, MaxEnt) classifier. |
| [`PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier") | Passive Aggressive Classifier. |
| [`Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron") | Linear perceptron classifier. |
| [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier") | Classifier using Ridge regression. |
| [`RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV") | Ridge classifier with built-in cross-validation. |
| [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier") | Linear classifiers (SVM, logistic regression, etc.) with SGD training. |
| [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM") | Solves linear One-Class SVM using Stochastic Gradient Descent. |

Classical linear regressors[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#classical-linear-regressors "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression") | Ordinary least squares Linear Regression. |
| [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") | Linear least squares with l2 regularization. |
| [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV") | Ridge regression with built-in cross-validation. |
| [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor") | Linear model fitted by minimizing a regularized empirical loss with SGD. |

Regressors with variable selection[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#regressors-with-variable-selection "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The following estimators have built-in variable selection fitting procedures, but any estimator using an L1 or elastic-net penalty also performs variable selection: typically `SGDRegressor` or [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 with an appropriate penalty.

|     |     |
| --- | --- |
| [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet") | Linear regression with combined L1 and L2 priors as regularizer. |
| [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV") | Elastic Net model with iterative fitting along a regularization path. |
| [`Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars") | Least Angle Regression model aka LAR. |
| [`LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV") | Cross-validated Least Angle Regression model. |
| [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso") | Linear Model trained with L1 prior as regularizer (aka the Lasso). |
| [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV") | Lasso linear model with iterative fitting along a regularization path. |
| [`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars") | Lasso model fit with Least Angle Regression aka Lars. |
| [`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV") | Cross-validated Lasso, using the LARS algorithm. |
| [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC") | Lasso model fit with Lars using BIC or AIC for model selection. |
| [`OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit") | Orthogonal Matching Pursuit model (OMP). |
| [`OrthogonalMatchingPursuitCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV") | Cross-validated Orthogonal Matching Pursuit model (OMP). |

Bayesian regressors[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#bayesian-regressors "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression") | Bayesian ARD regression. |
| [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge") | Bayesian ridge regression. |

Multi-task linear regressors with variable selection[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#multi-task-linear-regressors-with-variable-selection "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These estimators fit multiple regression problems (or tasks) jointly, while inducing sparse coefficients. While the inferred coefficients may differ between the tasks, they are constrained to agree on the features that are selected (non-zero coefficients).

|     |     |
| --- | --- |
| [`MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet") | Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer. |
| [`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV") | Multi-task L1/L2 ElasticNet with built-in cross-validation. |
| [`MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso") | Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer. |
| [`MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV") | Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer. |

Outlier-robust regressors[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#outlier-robust-regressors "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Any estimator using the Huber loss would also be robust to outliers, e.g., `SGDRegressor` with `loss='huber'`.

|     |     |
| --- | --- |
| [`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor") | L2-regularized linear regression model that is robust to outliers. |
| [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor") | Linear regression model that predicts conditional quantiles. |
| [`RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor") | RANSAC (RANdom SAmple Consensus) algorithm. |
| [`TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor") | Theil-Sen Estimator: robust multivariate regression model. |

Generalized linear models (GLM) for regression[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#generalized-linear-models-glm-for-regression "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

These models allow for response variables to have error distributions other than a normal distribution.

|     |     |
| --- | --- |
| [`GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor") | Generalized Linear Model with a Gamma distribution. |
| [`PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor") | Generalized Linear Model with a Poisson distribution. |
| [`TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor") | Generalized Linear Model with a Tweedie distribution. |

Miscellaneous[#](https://scikit-learn.org/stable/api/sklearn.linear_model.html#miscellaneous "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor") | Passive Aggressive Regressor. |
| [`enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path") | Compute elastic net path with coordinate descent. |
| [`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path") | Compute Least Angle Regression or Lasso path using the LARS algorithm. |
| [`lars_path_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path_gram.html#sklearn.linear_model.lars_path_gram "sklearn.linear_model.lars_path_gram") | The lars\_path in the sufficient stats mode. |
| [`lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path") | Compute Lasso path with coordinate descent. |
| [`orthogonal_mp`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#sklearn.linear_model.orthogonal_mp "sklearn.linear_model.orthogonal_mp") | Orthogonal Matching Pursuit (OMP). |
| [`orthogonal_mp_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#sklearn.linear_model.orthogonal_mp_gram "sklearn.linear_model.orthogonal_mp_gram") | Gram Orthogonal Matching Pursuit (OMP). |
| [`ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression") | Solve the ridge equation by the method of normal equations. |