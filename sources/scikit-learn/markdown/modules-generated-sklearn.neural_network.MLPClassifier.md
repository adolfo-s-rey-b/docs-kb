[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neural_network.MLPClassifier.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neural_network.MLPClassifier.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neural_network.MLPClassifier.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neural_network.MLPClassifier.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neural_network.MLPClassifier.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neural_network.MLPClassifier.html)

Collapse Sidebar Expand Sidebar

MLPClassifier[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#mlpclassifier "Link to this heading")

===================================================================================================================================================

class sklearn.neural\_network.MLPClassifier(_hidden\_layer\_sizes\=(100,)_, _activation\='relu'_, _\*_, _solver\='adam'_, _alpha\=0.0001_, _batch\_size\='auto'_, _learning\_rate\='constant'_, _learning\_rate\_init\=0.001_, _power\_t\=0.5_, _max\_iter\=200_, _shuffle\=True_, _random\_state\=None_, _tol\=0.0001_, _verbose\=False_, _warm\_start\=False_, _momentum\=0.9_, _nesterovs\_momentum\=True_, _early\_stopping\=False_, _validation\_fraction\=0.1_, _beta\_1\=0.9_, _beta\_2\=0.999_, _epsilon\=1e-08_, _n\_iter\_no\_change\=10_, _max\_fun\=15000_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_multilayer_perceptron.py#L879)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "Link to this definition")

Multi-layer Perceptron classifier.

This model optimizes the log-loss function using LBFGS or stochastic gradient descent.

Added in version 0.18.

Parameters:

**hidden\_layer\_sizes**array-like of shape(n\_layers - 2,), default=(100,)

The ith element represents the number of neurons in the ith hidden layer.

**activation**{‘identity’, ‘logistic’, ‘tanh’, ‘relu’}, default=’relu’

Activation function for the hidden layer.

*   ‘identity’, no-op activation, useful to implement linear bottleneck, returns f(x) = x
    
*   ‘logistic’, the logistic sigmoid function, returns f(x) = 1 / (1 + exp(-x)).
    
*   ‘tanh’, the hyperbolic tan function, returns f(x) = tanh(x).
    
*   ‘relu’, the rectified linear unit function, returns f(x) = max(0, x)
    

**solver**{‘lbfgs’, ‘sgd’, ‘adam’}, default=’adam’

The solver for weight optimization.

*   ‘lbfgs’ is an optimizer in the family of quasi-Newton methods.
    
*   ‘sgd’ refers to stochastic gradient descent.
    
*   ‘adam’ refers to a stochastic gradient-based optimizer proposed by Kingma, Diederik, and Jimmy Ba
    

For a comparison between Adam optimizer and SGD, see [Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html#sphx-glr-auto-examples-neural-networks-plot-mlp-training-curves-py)
.

Note: The default solver ‘adam’ works pretty well on relatively large datasets (with thousands of training samples or more) in terms of both training time and validation score. For small datasets, however, ‘lbfgs’ can converge faster and perform better.

**alpha**float, default=0.0001

Strength of the L2 regularization term. The L2 regularization term is divided by the sample size when added to the loss.

For an example usage and visualization of varying regularization, see [Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html#sphx-glr-auto-examples-neural-networks-plot-mlp-alpha-py)
.

**batch\_size**int, default=’auto’

Size of minibatches for stochastic optimizers. If the solver is ‘lbfgs’, the classifier will not use minibatch. When set to “auto”, `batch_size=min(200, n_samples)`.

**learning\_rate**{‘constant’, ‘invscaling’, ‘adaptive’}, default=’constant’

Learning rate schedule for weight updates.

*   ‘constant’ is a constant learning rate given by ‘learning\_rate\_init’.
    
*   ‘invscaling’ gradually decreases the learning rate at each time step ‘t’ using an inverse scaling exponent of ‘power\_t’. effective\_learning\_rate = learning\_rate\_init / pow(t, power\_t)
    
*   ‘adaptive’ keeps the learning rate constant to ‘learning\_rate\_init’ as long as training loss keeps decreasing. Each time two consecutive epochs fail to decrease training loss by at least tol, or fail to increase validation score by at least tol if ‘early\_stopping’ is on, the current learning rate is divided by 5.
    

Only used when `solver='sgd'`.

**learning\_rate\_init**float, default=0.001

The initial learning rate used. It controls the step-size in updating the weights. Only used when solver=’sgd’ or ‘adam’.

**power\_t**float, default=0.5

The exponent for inverse scaling learning rate. It is used in updating effective learning rate when the learning\_rate is set to ‘invscaling’. Only used when solver=’sgd’.

**max\_iter**int, default=200

Maximum number of iterations. The solver iterates until convergence (determined by ‘tol’) or this number of iterations. For stochastic solvers (‘sgd’, ‘adam’), note that this determines the number of epochs (how many times each data point will be used), not the number of gradient steps.

**shuffle**bool, default=True

Whether to shuffle samples in each iteration. Only used when solver=’sgd’ or ‘adam’.

**random\_state**int, RandomState instance, default=None

Determines random number generation for weights and bias initialization, train-test split if early stopping is used, and batch sampling when solver=’sgd’ or ‘adam’. Pass an int for reproducible results across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**tol**float, default=1e-4

Tolerance for the optimization. When the loss or score is not improving by at least `tol` for `n_iter_no_change` consecutive iterations, unless `learning_rate` is set to ‘adaptive’, convergence is considered to be reached and training stops.

**verbose**bool, default=False

Whether to print progress messages to stdout.

**warm\_start**bool, default=False

When set to True, reuse the solution of the previous call to fit as initialization, otherwise, just erase the previous solution. See [the Glossary](https://scikit-learn.org/stable/glossary.html#term-warm_start)
.

**momentum**float, default=0.9

Momentum for gradient descent update. Should be between 0 and 1. Only used when solver=’sgd’.

**nesterovs\_momentum**bool, default=True

Whether to use Nesterov’s momentum. Only used when solver=’sgd’ and momentum > 0.

**early\_stopping**bool, default=False

Whether to use early stopping to terminate training when validation score is not improving. If set to True, it will automatically set aside `validation_fraction` of training data as validation and terminate training when validation score is not improving by at least `tol` for `n_iter_no_change` consecutive epochs. The split is stratified, except in a multilabel setting. If early stopping is False, then the training stops when the training loss does not improve by more than `tol` for `n_iter_no_change` consecutive passes over the training set. Only effective when solver=’sgd’ or ‘adam’.

**validation\_fraction**float, default=0.1

The proportion of training data to set aside as validation set for early stopping. Must be between 0 and 1. Only used if early\_stopping is True.

**beta\_1**float, default=0.9

Exponential decay rate for estimates of first moment vector in adam, should be in \[0, 1). Only used when solver=’adam’.\
\
**beta\_2**float, default=0.999\
\
Exponential decay rate for estimates of second moment vector in adam, should be in \[0, 1). Only used when solver=’adam’.\
\
**epsilon**float, default=1e-8\
\
Value for numerical stability in adam. Only used when solver=’adam’.\
\
**n\_iter\_no\_change**int, default=10\
\
Maximum number of epochs to not meet `tol` improvement. Only effective when solver=’sgd’ or ‘adam’.\
\
Added in version 0.20.\
\
**max\_fun**int, default=15000\
\
Only used when solver=’lbfgs’. Maximum number of loss function calls. The solver iterates until convergence (determined by ‘tol’), number of iterations reaches max\_iter, or this number of loss function calls. Note that number of loss function calls will be greater than or equal to the number of iterations for the `MLPClassifier`.\
\
Added in version 0.22.\
\
Attributes:\
\
**classes\_**ndarray or list of ndarray of shape (n\_classes,)\
\
Class labels for each output.\
\
**loss\_**float\
\
The current loss computed with the loss function.\
\
**best\_loss\_**float or None\
\
The minimum loss reached by the solver throughout fitting. If `early_stopping=True`, this attribute is set to `None`. Refer to the `best_validation_score_` fitted attribute instead.\
\
**loss\_curve\_**list of shape (`n_iter_`,)\
\
The ith element in the list represents the loss at the ith iteration.\
\
**validation\_scores\_**list of shape (`n_iter_`,) or None\
\
The score at each iteration on a held-out validation set. The score reported is the accuracy score. Only available if `early_stopping=True`, otherwise the attribute is set to `None`.\
\
**best\_validation\_score\_**float or None\
\
The best validation score (i.e. accuracy score) that triggered the early stopping. Only available if `early_stopping=True`, otherwise the attribute is set to `None`.\
\
**t\_**int\
\
The number of training samples seen by the solver during fitting.\
\
**coefs\_**list of shape (n\_layers - 1,)\
\
The ith element in the list represents the weight matrix corresponding to layer i.\
\
**intercepts\_**list of shape (n\_layers - 1,)\
\
The ith element in the list represents the bias vector corresponding to layer i + 1.\
\
**n\_features\_in\_**int\
\
Number of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
.\
\
Added in version 0.24.\
\
**feature\_names\_in\_**ndarray of shape (`n_features_in_`,)\
\
Names of features seen during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)\
. Defined only when `X` has feature names that are all strings.\
\
Added in version 1.0.\
\
**n\_iter\_**int\
\
The number of iterations the solver has run.\
\
**n\_layers\_**int\
\
Number of layers.\
\
**n\_outputs\_**int\
\
Number of outputs.\
\
**out\_activation\_**str\
\
Name of the output activation function.\
\
See also\
\
[`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")\
\
Multi-layer Perceptron regressor.\
\
[`BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")\
\
Bernoulli Restricted Boltzmann Machine (RBM).\
\
Notes\
\
MLPClassifier trains iteratively since at each time step the partial derivatives of the loss function with respect to the model parameters are computed to update the parameters.\
\
It can also have a regularization term added to the loss function that shrinks model parameters to prevent overfitting.\
\
This implementation works with data represented as dense numpy arrays or sparse scipy arrays of floating point values.\
\
References\
\
Hinton, Geoffrey E. “Connectionist learning procedures.” Artificial intelligence 40.1 (1989): 185-234.\
\
Glorot, Xavier, and Yoshua Bengio. “Understanding the difficulty of training deep feedforward neural networks.” International Conference on Artificial Intelligence and Statistics. 2010.\
\
[He, Kaiming, et al (2015). “Delving deep into rectifiers: Surpassing human-level performance on imagenet classification.”](https://arxiv.org/abs/1502.01852)\
\
[Kingma, Diederik, and Jimmy Ba (2014) “Adam: A method for stochastic optimization.”](https://arxiv.org/abs/1412.6980)\
\
Examples\
\
\>>> from sklearn.neural\_network import MLPClassifier\
\>>> from sklearn.datasets import make\_classification\
\>>> from sklearn.model\_selection import train\_test\_split\
\>>> X, y \= make\_classification(n\_samples\=100, random\_state\=1)\
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y, stratify\=y,\
...                                                     random\_state\=1)\
\>>> clf \= MLPClassifier(random\_state\=1, max\_iter\=300).fit(X\_train, y\_train)\
\>>> clf.predict\_proba(X\_test\[:1\])\
array(\[\[0.0383, 0.961\]\])\
\>>> clf.predict(X\_test\[:5, :\])\
array(\[1, 0, 1, 0, 1\])\
\>>> clf.score(X\_test, y\_test)\
0.8...\
\
Copy to clipboard\
\
fit(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_multilayer_perceptron.py#L830)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.fit "Link to this definition")\
\
Fit the model to data matrix X and target(s) y.\
\
Parameters:\
\
**X**ndarray or sparse matrix of shape (n\_samples, n\_features)\
\
The input data.\
\
**y**ndarray of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
The target values (class labels in classification, real numbers in regression).\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Added in version 1.7.\
\
Returns:\
\
**self**object\
\
Returns a trained MLP model.\
\
get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.get_metadata_routing "Link to this definition")\
\
Get metadata routing of this object.\
\
Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
Returns:\
\
**routing**MetadataRequest\
\
A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")\
 encapsulating routing information.\
\
get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.get_params "Link to this definition")\
\
Get parameters for this estimator.\
\
Parameters:\
\
**deep**bool, default=True\
\
If True, will return the parameters for this estimator and contained subobjects that are estimators.\
\
Returns:\
\
**params**dict\
\
Parameter names mapped to their values.\
\
partial\_fit(_X_, _y_, _sample\_weight\=None_, _classes\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_multilayer_perceptron.py#L1297)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.partial_fit "Link to this definition")\
\
Update the model with a single iteration over the given data.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input data.\
\
**y**array-like of shape (n\_samples,)\
\
The target values.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Added in version 1.7.\
\
**classes**array of shape (n\_classes,), default=None\
\
Classes across all calls to partial\_fit. Can be obtained via `np.unique(y_all)`, where y\_all is the target vector of the entire dataset. This argument is required for the first call to partial\_fit and can be omitted in the subsequent calls. Note that y doesn’t need to contain all labels in `classes`.\
\
Returns:\
\
**self**object\
\
Trained MLP model.\
\
predict(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_multilayer_perceptron.py#L1267)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.predict "Link to this definition")\
\
Predict using the multi-layer perceptron classifier.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input data.\
\
Returns:\
\
**y**ndarray, shape (n\_samples,) or (n\_samples, n\_classes)\
\
The predicted classes.\
\
predict\_log\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_multilayer_perceptron.py#L1337)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.predict_log_proba "Link to this definition")\
\
Return the log of probability estimates.\
\
Parameters:\
\
**X**ndarray of shape (n\_samples, n\_features)\
\
The input data.\
\
Returns:\
\
**log\_y\_prob**ndarray of shape (n\_samples, n\_classes)\
\
The predicted log-probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`. Equivalent to `log(predict_proba(X))`.\
\
predict\_proba(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/neural_network/_multilayer_perceptron.py#L1355)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.predict_proba "Link to this definition")\
\
Probability estimates.\
\
Parameters:\
\
**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)\
\
The input data.\
\
Returns:\
\
**y\_prob**ndarray of shape (n\_samples, n\_classes)\
\
The predicted probability of the sample for each class in the model, where classes are ordered as they are in `self.classes_`.\
\
score(_X_, _y_, _sample\_weight\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L602)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.score "Link to this definition")\
\
Return [accuracy](https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score)\
 on provided data and labels.\
\
In multi-label classification, this is the subset accuracy which is a harsh metric since you require for each sample that each label set be correctly predicted.\
\
Parameters:\
\
**X**array-like of shape (n\_samples, n\_features)\
\
Test samples.\
\
**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs)\
\
True labels for `X`.\
\
**sample\_weight**array-like of shape (n\_samples,), default=None\
\
Sample weights.\
\
Returns:\
\
**score**float\
\
Mean accuracy of `self.predict(X)` w.r.t. `y`.\
\
set\_fit\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network._multilayer_perceptron.MLPClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.set_fit_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `fit` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `fit` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `fit`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `fit`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.set_params "Link to this definition")\
\
Set the parameters of this estimator.\
\
The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.\
\
Parameters:\
\
**\*\*params**dict\
\
Estimator parameters.\
\
Returns:\
\
**self**estimator instance\
\
Estimator instance.\
\
set\_partial\_fit\_request(_\*_, _classes: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network._multilayer_perceptron.MLPClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.set_partial_fit_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `partial_fit` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `partial_fit` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `partial_fit`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**classes**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `classes` parameter in `partial_fit`.\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `partial_fit`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
set\_score\_request(_\*_, _sample\_weight: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")\
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")\
 | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
 \= '$UNCHANGED$'_) → [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network._multilayer_perceptron.MLPClassifier")\
[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1440)\
[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier.set_score_request "Link to this definition")\
\
Configure whether metadata should be requested to be passed to the `score` method.\
\
Note that this method is only relevant when this estimator is used as a sub-estimator within a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator)\
 and metadata routing is enabled with `enable_metadata_routing=True` (see [`sklearn.set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")\
). Please check the [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)\
 on how the routing mechanism works.\
\
The options for each parameter are:\
\
*   `True`: metadata is requested, and passed to `score` if provided. The request is ignored if metadata is not provided.\
    \
*   `False`: metadata is not requested and the meta-estimator will not pass it to `score`.\
    \
*   `None`: metadata is not requested, and the meta-estimator will raise an error if the user provides it.\
    \
*   `str`: metadata should be passed to the meta-estimator with this given alias instead of the original name.\
    \
\
The default (`sklearn.utils.metadata_routing.UNCHANGED`) retains the existing request. This allows you to change the request for some parameters and not others.\
\
Added in version 1.3.\
\
Parameters:\
\
**sample\_weight**str, True, False, or None, default=sklearn.utils.metadata\_routing.UNCHANGED\
\
Metadata routing for `sample_weight` parameter in `score`.\
\
Returns:\
\
**self**object\
\
The updated object.\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#gallery-examples "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_thumb.png)\
\
[Classifier comparison](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html)\
\
Classifier comparison\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_alpha_thumb.png)\
\
[Varying regularization in Multi-layer Perceptron](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_alpha.html)\
\
Varying regularization in Multi-layer Perceptron\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_thumb.png)\
\
[Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)\
\
Compare Stochastic learning strategies for MLPClassifier\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mnist_filters_thumb.png)\
\
[Visualization of MLP weights on MNIST](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html)\
\
Visualization of MLP weights on MNIST\
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