[Skip to main content](https://scikit-learn.org/stable/modules/sgd.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/sgd.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/sgd.html)
[1.8.0](https://scikit-learn.org/1.8/modules/sgd.html)
[1.7.2](https://scikit-learn.org/1.7/modules/sgd.html)
[1.6.1](https://scikit-learn.org/1.6/modules/sgd.html)
[1.5.2](https://scikit-learn.org/1.5/modules/sgd.html)
[1.4.2](https://scikit-learn.org/1.4/modules/sgd.html)

Collapse Sidebar Expand Sidebar

1.5. Stochastic Gradient Descent[#](https://scikit-learn.org/stable/modules/sgd.html#stochastic-gradient-descent "Link to this heading")

=========================================================================================================================================

**Stochastic Gradient Descent (SGD)** is a simple yet very efficient approach to fitting linear classifiers and regressors under convex loss functions such as (linear) [Support Vector Machines](https://en.wikipedia.org/wiki/Support_vector_machine)
 and [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression)
. Even though SGD has been around in the machine learning community for a long time, it has received a considerable amount of attention just recently in the context of large-scale learning.

SGD has been successfully applied to large-scale and sparse machine learning problems often encountered in text classification and natural language processing. Given that the data is sparse, the classifiers in this module easily scale to problems with more than 105 training examples and more than 105 features.

Strictly speaking, SGD is merely an optimization technique and does not correspond to a specific family of machine learning models. It is only a _way_ to train a model. Often, an instance of [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 or [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 will have an equivalent estimator in the scikit-learn API, potentially using a different optimization technique. For example, using `SGDClassifier(loss='log_loss')` results in logistic regression, i.e. a model equivalent to [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 which is fitted via SGD instead of being fitted by one of the other solvers in [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
. Similarly, `SGDRegressor(loss='squared_error', penalty='l2')` and [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
 solve the same optimization problem, via different means.

The advantages of Stochastic Gradient Descent are:

*   Efficiency.
    
*   Ease of implementation (lots of opportunities for code tuning).
    

The disadvantages of Stochastic Gradient Descent include:

*   SGD requires a number of hyperparameters such as the regularization parameter and the number of iterations.
    
*   SGD is sensitive to feature scaling.
    

Warning

Make sure you permute (shuffle) your training data before fitting the model or use `shuffle=True` to shuffle after each iteration (used by default). Also, ideally, features should be standardized using e.g. `make_pipeline(StandardScaler(), SGDClassifier())` (see [Pipelines](https://scikit-learn.org/stable/modules/compose.html#combining-estimators)
).

1.5.1. Classification[#](https://scikit-learn.org/stable/modules/sgd.html#classification "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

The class [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 implements a plain stochastic gradient descent learning routine which supports different loss functions and penalties for classification. Below is the decision boundary of a [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 trained with the hinge loss, equivalent to a linear SVM.

[![../_images/sphx_glr_plot_sgd_separating_hyperplane_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_001.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

As other classifiers, SGD has to be fitted with two arrays: an array `X` of shape (n\_samples, n\_features) holding the training samples, and an array `y` of shape (n\_samples,) holding the target values (class labels) for the training samples:

\>>> from sklearn.linear\_model import SGDClassifier
\>>> X \= \[\[0., 0.\], \[1., 1.\]\]
\>>> y \= \[0, 1\]
\>>> clf \= SGDClassifier(loss\="hinge", penalty\="l2", max\_iter\=5)
\>>> clf.fit(X, y)
SGDClassifier(max\_iter=5)

Copy to clipboard

After being fitted, the model can then be used to predict new values:

\>>> clf.predict(\[\[2., 2.\]\])
array(\[1\])

Copy to clipboard

SGD fits a linear model to the training data. The `coef_` attribute holds the model parameters:

\>>> clf.coef\_
array(\[\[9.9, 9.9\]\])

Copy to clipboard

The `intercept_` attribute holds the intercept (aka offset or bias):

\>>> clf.intercept\_
array(\[-9.9\])

Copy to clipboard

Whether or not the model should use an intercept, i.e. a biased hyperplane, is controlled by the parameter `fit_intercept`.

The signed distance to the hyperplane (computed as the dot product between the coefficients and the input sample, plus the intercept) is given by [`SGDClassifier.decision_function`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier.decision_function "sklearn.linear_model.SGDClassifier.decision_function")
:

\>>> clf.decision\_function(\[\[2., 2.\]\])
array(\[29.6\])

Copy to clipboard

The concrete loss function can be set via the `loss` parameter. [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 supports the following loss functions:

*   `loss="hinge"`: (soft-margin) linear Support Vector Machine,
    
*   `loss="modified_huber"`: smoothed hinge loss,
    
*   `loss="log_loss"`: logistic regression,
    
*   and all regression losses below. In this case the target is encoded as −1 or 1, and the problem is treated as a regression problem. The predicted class then corresponds to the sign of the predicted target.
    

Please refer to the [mathematical section below](https://scikit-learn.org/stable/modules/sgd.html#sgd-mathematical-formulation)
 for formulas. The first two loss functions are lazy, they only update the model parameters if an example violates the margin constraint, which makes training very efficient and may result in sparser models (i.e. with more zero coefficients), even when L2 penalty is used.

Using `loss="log_loss"` or `loss="modified_huber"` enables the `predict_proba` method, which gives a vector of probability estimates P(y|x) per sample x:

\>>> clf \= SGDClassifier(loss\="log\_loss", max\_iter\=5).fit(X, y)
\>>> clf.predict\_proba(\[\[1., 1.\]\])
array(\[\[0.00, 0.99\]\])

Copy to clipboard

The concrete penalty can be set via the `penalty` parameter. SGD supports the following penalties:

*   `penalty="l2"`: L2 norm penalty on `coef_`.
    
*   `penalty="l1"`: L1 norm penalty on `coef_`.
    
*   `penalty="elasticnet"`: Convex combination of L2 and L1; `(1 - l1_ratio) * L2 + l1_ratio * L1`.
    

The default setting is `penalty="l2"`. The L1 penalty leads to sparse solutions, driving most coefficients to zero. The Elastic Net [\[11\]](https://scikit-learn.org/stable/modules/sgd.html#id15)
 solves some deficiencies of the L1 penalty in the presence of highly correlated attributes. The parameter `l1_ratio` controls the convex combination of L1 and L2 penalty.

[`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 supports multi-class classification by combining multiple binary classifiers in a “one versus all” (OVA) scheme. For each of the K classes, a binary classifier is learned that discriminates between that and all other K−1 classes. At testing time, we compute the confidence score (i.e. the signed distances to the hyperplane) for each classifier and choose the class with the highest confidence. The Figure below illustrates the OVA approach on the iris dataset. The dashed lines represent the three OVA classifiers; the background colors show the decision surface induced by the three classifiers.

[![../_images/sphx_glr_plot_sgd_iris_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_001.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

In the case of multi-class classification `coef_` is a two-dimensional array of shape (n\_classes, n\_features) and `intercept_` is a one-dimensional array of shape (n\_classes,). The i\-th row of `coef_` holds the weight vector of the OVA classifier for the i\-th class; classes are indexed in ascending order (see attribute `classes_`). Note that, in principle, since they allow to create a probability model, `loss="log_loss"` and `loss="modified_huber"` are more suitable for one-vs-all classification.

[`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 supports both weighted classes and weighted instances via the fit parameters `class_weight` and `sample_weight`. See the examples below and the docstring of [`SGDClassifier.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier.fit "sklearn.linear_model.SGDClassifier.fit")
 for further information.

[`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 supports averaged SGD (ASGD) [\[10\]](https://scikit-learn.org/stable/modules/sgd.html#id14)
. Averaging can be enabled by setting `average=True`. ASGD performs the same updates as the regular SGD (see [Mathematical formulation](https://scikit-learn.org/stable/modules/sgd.html#sgd-mathematical-formulation)
), but instead of using the last value of the coefficients as the `coef_` attribute (i.e. the values of the last update), `coef_` is set instead to the **average** value of the coefficients across all updates. The same is done for the `intercept_` attribute. When using ASGD the learning rate can be larger and even constant, leading on some datasets to a speed up in training time.

For classification with a logistic loss, another variant of SGD with an averaging strategy is available with Stochastic Average Gradient (SAG) algorithm, available as a solver in [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
.

Examples

*   [SGD: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html#sphx-glr-auto-examples-linear-model-plot-sgd-separating-hyperplane-py)
    
*   [Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html#sphx-glr-auto-examples-linear-model-plot-sgd-iris-py)
    
*   [SGD: Weighted samples](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_weighted_samples.html#sphx-glr-auto-examples-linear-model-plot-sgd-weighted-samples-py)
    
*   [SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html#sphx-glr-auto-examples-svm-plot-separating-hyperplane-unbalanced-py)
     (See the Note in the example)
    

1.5.2. Regression[#](https://scikit-learn.org/stable/modules/sgd.html#regression "Link to this heading")

---------------------------------------------------------------------------------------------------------

The class [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 implements a plain stochastic gradient descent learning routine which supports different loss functions and penalties to fit linear regression models. [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 is well suited for regression problems with a large number of training samples (> 10.000), for other problems we recommend [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
, [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
, or [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
.

The concrete loss function can be set via the `loss` parameter. [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 supports the following loss functions:

*   `loss="squared_error"`: Ordinary least squares,
    
*   `loss="huber"`: Huber loss for robust regression,
    
*   `loss="epsilon_insensitive"`: linear Support Vector Regression.
    

Please refer to the [mathematical section below](https://scikit-learn.org/stable/modules/sgd.html#sgd-mathematical-formulation)
 for formulas. The Huber and epsilon-insensitive loss functions can be used for robust regression. The width of the insensitive region has to be specified via the parameter `epsilon`. This parameter depends on the scale of the target variables.

The `penalty` parameter determines the regularization to be used (see description above in the classification section).

[`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 also supports averaged SGD [\[10\]](https://scikit-learn.org/stable/modules/sgd.html#id14)
 (here again, see description above in the classification section).

For regression with a squared loss and a L2 penalty, another variant of SGD with an averaging strategy is available with Stochastic Average Gradient (SAG) algorithm, available as a solver in [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
.

Examples

*   [Prediction Latency](https://scikit-learn.org/stable/auto_examples/applications/plot_prediction_latency.html#sphx-glr-auto-examples-applications-plot-prediction-latency-py)
    

1.5.3. Online One-Class SVM[#](https://scikit-learn.org/stable/modules/sgd.html#online-one-class-svm "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

The class [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 implements an online linear version of the One-Class SVM using a stochastic gradient descent. Combined with kernel approximation techniques, [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 can be used to approximate the solution of a kernelized One-Class SVM, implemented in [`sklearn.svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
, with a linear complexity in the number of samples. Note that the complexity of a kernelized One-Class SVM is at best quadratic in the number of samples. [`sklearn.linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 is thus well suited for datasets with a large number of training samples (over 10,000) for which the SGD variant can be several orders of magnitude faster.

Mathematical details[#](https://scikit-learn.org/stable/modules/sgd.html#mathematical-details "Link to this dropdown")

Its implementation is based on the implementation of the stochastic gradient descent. Indeed, the original optimization problem of the One-Class SVM is given by

minw,ρ,ξ12‖w‖2−ρ+1νn∑i\=1nξis.t.⟨w,xi⟩≥ρ−ξi1≤i≤nξi≥01≤i≤n

where ν∈(0,1\] is the user-specified parameter controlling the proportion of outliers and the proportion of support vectors. Getting rid of the slack variables ξi this problem is equivalent to

minw,ρ12‖w‖2−ρ+1νn∑i\=1nmax(0,ρ−⟨w,xi⟩).

Multiplying by the constant ν and introducing the intercept b\=1−ρ we obtain the following equivalent optimization problem

minw,bν2‖w‖2+bν+1n∑i\=1nmax(0,1−(⟨w,xi⟩+b)).

This is similar to the optimization problems studied in section [Mathematical formulation](https://scikit-learn.org/stable/modules/sgd.html#sgd-mathematical-formulation)
 with yi\=1,1≤i≤n and α\=ν, L being the hinge loss function and R being the L2 norm. We just need to add the term bν in the optimization loop.

As [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 and [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
, [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
 supports averaged SGD. Averaging can be enabled by setting `average=True`.

Examples

*   [One-Class SVM versus One-Class SVM using Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgdocsvm_vs_ocsvm.html#sphx-glr-auto-examples-linear-model-plot-sgdocsvm-vs-ocsvm-py)
    

1.5.4. Stochastic Gradient Descent for sparse data[#](https://scikit-learn.org/stable/modules/sgd.html#stochastic-gradient-descent-for-sparse-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

The sparse implementation produces slightly different results from the dense implementation, due to a shrunk learning rate for the intercept. See [Implementation details](https://scikit-learn.org/stable/modules/sgd.html#implementation-details)
.

There is built-in support for sparse data given in any matrix in a format supported by [scipy.sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html)
. For maximum efficiency, however, use the CSR matrix format as defined in [scipy.sparse.csr\_matrix](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html)
.

Examples

*   [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)
    

1.5.5. Complexity[#](https://scikit-learn.org/stable/modules/sgd.html#complexity "Link to this heading")

---------------------------------------------------------------------------------------------------------

The major advantage of SGD is its efficiency, which is basically linear in the number of training examples. If X is a matrix of size n×p (with n samples and p features), training has a cost of O(knp¯), where k is the number of iterations (epochs) and p¯ is the average number of non-zero attributes per sample.

Recent theoretical results, however, show that the runtime to get some desired optimization accuracy does not increase as the training set size increases.

1.5.6. Stopping criterion[#](https://scikit-learn.org/stable/modules/sgd.html#stopping-criterion "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

The classes [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 and [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
 provide two criteria to stop the algorithm when a given level of convergence is reached:

*   With `early_stopping=True`, the input data is split into a training set and a validation set. The model is then fitted on the training set, and the stopping criterion is based on the prediction score (using the `score` method) computed on the validation set. The size of the validation set can be changed with the parameter `validation_fraction`.
    
*   With `early_stopping=False`, the model is fitted on the entire input data and the stopping criterion is based on the objective function computed on the training data.
    

In both cases, the criterion is evaluated once by epoch, and the algorithm stops when the criterion does not improve `n_iter_no_change` times in a row. The improvement is evaluated with absolute tolerance `tol`, and the algorithm stops in any case after a maximum number of iterations `max_iter`.

See [Early stopping of Stochastic Gradient Descent](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_early_stopping.html#sphx-glr-auto-examples-linear-model-plot-sgd-early-stopping-py)
 for an example of the effects of early stopping.

1.5.7. Tips on Practical Use[#](https://scikit-learn.org/stable/modules/sgd.html#tips-on-practical-use "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   Stochastic Gradient Descent is sensitive to feature scaling, so it is highly recommended to scale your data. For example, scale each attribute on the input vector X to \[0,1\] or \[−1,1\], or standardize it to have mean 0 and variance 1. Note that the _same_ scaling must be applied to the test vector to obtain meaningful results. This can be easily done using [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    :
    
    from sklearn.preprocessing import StandardScaler
    scaler \= StandardScaler()
    scaler.fit(X\_train)  \# Don't cheat - fit only on training data
    X\_train \= scaler.transform(X\_train)
    X\_test \= scaler.transform(X\_test)  \# apply same transformation to test data
    
    \# Or better yet: use a pipeline!
    from sklearn.pipeline import make\_pipeline
    est \= make\_pipeline(StandardScaler(), SGDClassifier())
    est.fit(X\_train)
    est.predict(X\_test)
    
    Copy to clipboard
    
    If your attributes have an intrinsic scale (e.g. word frequencies or indicator features) scaling is not needed.
    
*   Finding a reasonable regularization term α is best done using automatic hyper-parameter search, e.g. [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     or [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
    , usually in the range `10.0**-np.arange(1,7)`.
    
*   Empirically, we found that SGD converges after observing approximately 106 training samples. Thus, a reasonable first guess for the number of iterations is `max_iter = np.ceil(10**6 / n)`, where `n` is the size of the training set.
    
*   If you apply SGD to features extracted using PCA we found that it is often wise to scale the feature values by some constant `c` such that the average L2 norm of the training data equals one.
    
*   We found that Averaged SGD works best with a larger number of features and a higher `eta0`.
    

References

*   [“Efficient BackProp”](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)
     Y. LeCun, L. Bottou, G. Orr, K. Müller - In Neural Networks: Tricks of the Trade 1998.
    

1.5.8. Mathematical formulation[#](https://scikit-learn.org/stable/modules/sgd.html#mathematical-formulation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

We describe here the mathematical details of the SGD procedure. A good overview with convergence rates can be found in [\[12\]](https://scikit-learn.org/stable/modules/sgd.html#id16)
.

Given a set of training examples {(x1,y1),…,(xn,yn)} where xi∈Rm and yi∈R (yi∈{−1,1} for classification), our goal is to learn a linear scoring function f(x)\=wTx+b with model parameters w∈Rm and intercept b∈R. In order to make predictions for binary classification, we simply look at the sign of f(x). To find the model parameters, we minimize the regularized training error given by

E(w,b)\=1n∑i\=1nL(yi,f(xi))+αR(w)

where L is a loss function that measures model (mis)fit and R is a regularization term (aka penalty) that penalizes model complexity; α\>0 is a non-negative hyperparameter that controls the regularization strength.

Loss functions details[#](https://scikit-learn.org/stable/modules/sgd.html#loss-functions-details "Link to this dropdown")

Different choices for L entail different classifiers or regressors:

*   Hinge (soft-margin): equivalent to Support Vector Classification. L(yi,f(xi))\=max(0,1−yif(xi)).
    
*   Perceptron: L(yi,f(xi))\=max(0,−yif(xi)).
    
*   Modified Huber: L(yi,f(xi))\=max(0,1−yif(xi))2 if yif(xi)\>−1, and L(yi,f(xi))\=−4yif(xi) otherwise.
    
*   Log Loss: equivalent to Logistic Regression. L(yi,f(xi))\=log⁡(1+exp⁡(−yif(xi))).
    
*   Squared Error: Linear regression (Ridge or Lasso depending on R). L(yi,f(xi))\=12(yi−f(xi))2.
    
*   Huber: less sensitive to outliers than least-squares. It is equivalent to least squares when |yi−f(xi)|≤ε, and L(yi,f(xi))\=ε|yi−f(xi)|−12ε2 otherwise.
    
*   Epsilon-Insensitive: (soft-margin) equivalent to Support Vector Regression. L(yi,f(xi))\=max(0,|yi−f(xi)|−ε).
    

All of the above loss functions can be regarded as an upper bound on the misclassification error (Zero-one loss) as shown in the Figure below.

[![../_images/sphx_glr_plot_sgd_loss_functions_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_loss_functions_001.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html)

Popular choices for the regularization term R (the `penalty` parameter) include:

*   L2 norm: R(w):=12∑j\=1mwj2\=12||w||22,
    
*   L1 norm: R(w):=∑j\=1m|wj|, which leads to sparse solutions.
    
*   Elastic Net: R(w):=ρ2∑j\=1nwj2+(1−ρ)∑j\=1m|wj|, a convex combination of L2 and L1, where ρ is given by `1 - l1_ratio`.
    

The Figure below shows the contours of the different regularization terms in a 2-dimensional parameter space (m\=2) when R(w)\=1.

[![../_images/sphx_glr_plot_sgd_penalties_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_penalties_001.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_penalties.html)

### 1.5.8.1. SGD[#](https://scikit-learn.org/stable/modules/sgd.html#id5 "Link to this heading")

Stochastic gradient descent is an optimization method for unconstrained optimization problems. In contrast to (batch) gradient descent, SGD approximates the true gradient of E(w,b) by considering a single training example at a time.

The class [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
 implements a first-order SGD learning routine. The algorithm iterates over the training examples and for each example updates the model parameters according to the update rule given by

w←w−η\[α∂R(w)∂w+∂L(wTxi+b,yi)∂w\]

where η is the learning rate which controls the step-size in the parameter space. The intercept b is updated similarly but without regularization (and with additional decay for sparse matrices, as detailed in [Implementation details](https://scikit-learn.org/stable/modules/sgd.html#implementation-details)
).

The learning rate η can be either constant or gradually decaying. For classification, the default learning rate schedule (`learning_rate='optimal'`) is given by

η(t)\=1α(t0+t)

where t is the time step (there are a total of `n_samples * n_iter` time steps), t0 is determined based on a heuristic proposed by Léon Bottou such that the expected initial updates are comparable with the expected size of the weights (this assumes that the norm of the training samples is approximately 1). The exact definition can be found in `_init_t` in `BaseSGD`.

For regression the default learning rate schedule is inverse scaling (`learning_rate='invscaling'`), given by

η(t)\=η0tpower\_t

where η0 and power\_t are hyperparameters chosen by the user via `eta0` and `power_t`, respectively.

For a constant learning rate use `learning_rate='constant'` and use `eta0` to specify the learning rate.

For an adaptively decreasing learning rate, use `learning_rate='adaptive'` and use `eta0` to specify the starting learning rate. When the stopping criterion is reached, the learning rate is divided by 5, and the algorithm does not stop. The algorithm stops when the learning rate goes below `1e-6`.

The model parameters can be accessed through the `coef_` and `intercept_` attributes: `coef_` holds the weights w and `intercept_` holds b.

When using Averaged SGD (with the `average` parameter), `coef_` is set to the average weight across all updates: `coef_` \=1T∑t\=0T−1w(t), where T is the total number of updates, found in the `t_` attribute.

1.5.9. Implementation details[#](https://scikit-learn.org/stable/modules/sgd.html#implementation-details "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The implementation of SGD is influenced by the `Stochastic Gradient SVM` of [\[7\]](https://scikit-learn.org/stable/modules/sgd.html#id10)
. Similar to SvmSGD, the weight vector is represented as the product of a scalar and a vector which allows an efficient weight update in the case of L2 regularization. In the case of sparse input `X`, the intercept is updated with a smaller learning rate (multiplied by 0.01) to account for the fact that it is updated more frequently. Training examples are picked up sequentially and the learning rate is lowered after each observed example. We adopted the learning rate schedule from [\[8\]](https://scikit-learn.org/stable/modules/sgd.html#id12)
. For multi-class classification, a “one versus all” approach is used. We use the truncated gradient algorithm proposed in [\[9\]](https://scikit-learn.org/stable/modules/sgd.html#id13)
 for L1 regularization (and the Elastic Net). The code is written in Cython.

References

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)