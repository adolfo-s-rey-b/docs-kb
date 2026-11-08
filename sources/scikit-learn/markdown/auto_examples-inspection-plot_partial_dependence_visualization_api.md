[Skip to main content](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/inspection/plot_partial_dependence_visualization_api.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/inspection/plot_partial_dependence_visualization_api.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/inspection/plot_partial_dependence_visualization_api.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/inspection/plot_partial_dependence_visualization_api.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/inspection/plot_partial_dependence_visualization_api.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/inspection/plot_partial_dependence_visualization_api.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#sphx-glr-download-auto-examples-inspection-plot-partial-dependence-visualization-api-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Advanced Plotting With Partial Dependence[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#advanced-plotting-with-partial-dependence "Link to this heading")

=======================================================================================================================================================================================================================

The [`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")
 object can be used for plotting without needing to recalculate the partial dependence. In this example, we show how to plot partial dependence plots and how to quickly customize the plot with the visualization API.

Note

See also [ROC Curve with Visualization API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_roc_curve_visualization_api.html#sphx-glr-auto-examples-miscellaneous-plot-roc-curve-visualization-api-py)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
from sklearn.inspection import PartialDependenceDisplay
from sklearn.neural\_network import [MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

Copy to clipboard

Train models on the diabetes dataset[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#train-models-on-the-diabetes-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we train a decision tree and a multi-layer perceptron on the diabetes dataset.

diabetes \= [load\_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")
()
X \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
(diabetes.data, columns\=diabetes.feature\_names)
y \= diabetes.target

tree \= [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
()
mlp \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(),
    [MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
(hidden\_layer\_sizes\=(100, 100), tol\=1e-2, max\_iter\=500, random\_state\=0),
)
tree.fit(X, y)
mlp.fit(X, y)

Copy to clipboard

Pipeline(steps=\[('standardscaler', StandardScaler()),\
                ('mlpregressor',\
                 MLPRegressor(hidden\_layer\_sizes=(100, 100), max\_iter=500,\
                              random\_state=0, tol=0.01))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('standardscaler', ...), ('mlpregressor', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['age','sex','bmi',...,'s4','s5','s6'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 10  |

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['age','sex','bmi',...,'s4','s5','s6'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](10,) | \[-0., 0.,-0.,...,-0., 0., 0.\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 10  |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 442 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](10,) | \[0.05,0.05,0.05,...,0.05,0.05,0.05\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](10,) | \[0.,0.,0.,...,0.,0.,0.\] |

10 features

|     |
| --- |
| age |
| sex |
| bmi |
| bp  |
| s1  |
| s2  |
| s3  |
| s4  |
| s5  |
| s6  |

MLPRegressor

[?Documentation for MLPRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [hidden\_layer\_sizes hidden\_layer\_sizes: array-like of shape(n\_layers - 2,), default=(100,)  <br>  <br>The ith element represents the number of neurons in the ith  <br>hidden layer.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=hidden_layer_sizes,-array-like%20of%20shape%28n_layers%20-%202%2C%29%2C%20default%3D%28100%2C%29) | (100, ...) |
|     | [max\_iter max\_iter: int, default=200  <br>  <br>Maximum number of iterations. The solver iterates until convergence  <br>(determined by 'tol') or this number of iterations. For stochastic  <br>solvers ('sgd', 'adam'), note that this determines the number of epochs  <br>(how many times each data point will be used), not the number of  <br>gradient steps.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=max_iter,-int%2C%20default%3D200) | 500 |
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Determines random number generation for weights and bias  <br>initialization, train-test split if early stopping is used, and batch  <br>sampling when solver='sgd' or 'adam'.  <br>Pass an int for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | 0   |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for the optimization. When the loss or score is not improving  <br>by at least \`\`tol\`\` for \`\`n\_iter\_no\_change\`\` consecutive iterations,  <br>unless \`\`learning\_rate\`\` is set to 'adaptive', convergence is  <br>considered to be reached and training stops.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.01 |
|     | [loss loss: {'squared\_error', 'poisson'}, default='squared\_error'  <br>  <br>The loss function to use when training the weights. Note that the  <br>"squared error" and "poisson" losses actually implement  <br>"half squares error" and "half poisson deviance" to simplify the  <br>computation of the gradient. Furthermore, the "poisson" loss internally uses  <br>a log-link (exponential as the output activation function) and requires  <br>\`\`y >= 0\`\`.  <br>  <br>.. versionchanged:: 1.7  <br>Added parameter \`loss\` and option 'poisson'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27poisson%27%7D%2C%20default%3D%27squared_error%27) | 'squared\_error' |
|     | [activation activation: {'identity', 'logistic', 'tanh', 'relu'}, default='relu'  <br>  <br>Activation function for the hidden layer.  <br>  <br>\- 'identity', no-op activation, useful to implement linear bottleneck,  <br>returns f(x) = x  <br>  <br>\- 'logistic', the logistic sigmoid function,  <br>returns f(x) = 1 / (1 + exp(-x)).  <br>  <br>\- 'tanh', the hyperbolic tan function,  <br>returns f(x) = tanh(x).  <br>  <br>\- 'relu', the rectified linear unit function,  <br>returns f(x) = max(0, x)](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=activation,-%7B%27identity%27%2C%20%27logistic%27%2C%20%27tanh%27%2C%20%27relu%27%7D%2C%20default%3D%27relu%27) | 'relu' |
|     | [solver solver: {'lbfgs', 'sgd', 'adam'}, default='adam'  <br>  <br>The solver for weight optimization.  <br>  <br>\- 'lbfgs' is an optimizer in the family of quasi-Newton methods.  <br>  <br>\- 'sgd' refers to stochastic gradient descent.  <br>  <br>\- 'adam' refers to a stochastic gradient-based optimizer proposed by  <br>Kingma, Diederik, and Jimmy Ba  <br>  <br>For a comparison between Adam optimizer and SGD, see  <br>:ref:\`sphx\_glr\_auto\_examples\_neural\_networks\_plot\_mlp\_training\_curves.py\`.  <br>  <br>Note: The default solver 'adam' works pretty well on relatively  <br>large datasets (with thousands of training samples or more) in terms of  <br>both training time and validation score.  <br>For small datasets, however, 'lbfgs' can converge faster and perform  <br>better.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27sgd%27%2C%20%27adam%27%7D%2C%20default%3D%27adam%27) | 'adam' |
|     | [alpha alpha: float, default=0.0001  <br>  <br>Strength of the L2 regularization term. The L2 regularization term  <br>is divided by the sample size when added to the loss.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=alpha,-float%2C%20default%3D0.0001) | 0.0001 |
|     | [batch\_size batch\_size: int, default='auto'  <br>  <br>Size of minibatches for stochastic optimizers.  <br>If the solver is 'lbfgs', the regressor will not use minibatch.  <br>When set to "auto", \`batch\_size=min(200, n\_samples)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=batch_size,-int%2C%20default%3D%27auto%27) | 'auto' |
|     | [learning\_rate learning\_rate: {'constant', 'invscaling', 'adaptive'}, default='constant'  <br>  <br>Learning rate schedule for weight updates.  <br>  <br>\- 'constant' is a constant learning rate given by  <br>'learning\_rate\_init'.  <br>  <br>\- 'invscaling' gradually decreases the learning rate \`\`learning\_rate\_\`\`  <br>at each time step 't' using an inverse scaling exponent of 'power\_t'.  <br>effective\_learning\_rate = learning\_rate\_init / pow(t, power\_t)  <br>  <br>\- 'adaptive' keeps the learning rate constant to  <br>'learning\_rate\_init' as long as training loss keeps decreasing.  <br>Each time two consecutive epochs fail to decrease training loss by at  <br>least tol, or fail to increase validation score by at least tol if  <br>'early\_stopping' is on, the current learning rate is divided by 5.  <br>  <br>Only used when solver='sgd'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=learning_rate,-%7B%27constant%27%2C%20%27invscaling%27%2C%20%27adaptive%27%7D%2C%20default%3D%27constant%27) | 'constant' |
|     | [learning\_rate\_init learning\_rate\_init: float, default=0.001  <br>  <br>The initial learning rate used. It controls the step-size  <br>in updating the weights. Only used when solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=learning_rate_init,-float%2C%20default%3D0.001) | 0.001 |
|     | [power\_t power\_t: float, default=0.5  <br>  <br>The exponent for inverse scaling learning rate.  <br>It is used in updating effective learning rate when the learning\_rate  <br>is set to 'invscaling'. Only used when solver='sgd'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=power_t,-float%2C%20default%3D0.5) | 0.5 |
|     | [shuffle shuffle: bool, default=True  <br>  <br>Whether to shuffle samples in each iteration. Only used when  <br>solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=shuffle,-bool%2C%20default%3DTrue) | True |
|     | [verbose verbose: bool, default=False  <br>  <br>Whether to print progress messages to stdout.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous  <br>call to fit as initialization, otherwise, just erase the  <br>previous solution. See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [momentum momentum: float, default=0.9  <br>  <br>Momentum for gradient descent update. Should be between 0 and 1. Only  <br>used when solver='sgd'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=momentum,-float%2C%20default%3D0.9) | 0.9 |
|     | [nesterovs\_momentum nesterovs\_momentum: bool, default=True  <br>  <br>Whether to use Nesterov's momentum. Only used when solver='sgd' and  <br>momentum > 0.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=nesterovs_momentum,-bool%2C%20default%3DTrue) | True |
|     | [early\_stopping early\_stopping: bool, default=False  <br>  <br>Whether to use early stopping to terminate training when validation  <br>score is not improving. If set to True, it will automatically set  <br>aside \`\`validation\_fraction\`\` of training data as validation and  <br>terminate training when validation score is not improving by at  <br>least \`\`tol\`\` for \`\`n\_iter\_no\_change\`\` consecutive epochs.  <br>Only effective when solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=early_stopping,-bool%2C%20default%3DFalse) | False |
|     | [validation\_fraction validation\_fraction: float, default=0.1  <br>  <br>The proportion of training data to set aside as validation set for  <br>early stopping. Must be between 0 and 1.  <br>Only used if early\_stopping is True.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=validation_fraction,-float%2C%20default%3D0.1) | 0.1 |
|     | [beta\_1 beta\_1: float, default=0.9  <br>  <br>Exponential decay rate for estimates of first moment vector in adam,  <br>should be in \[0, 1). Only used when solver='adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=beta_1,-float%2C%20default%3D0.9) | 0.9 |\
|     | [beta\_2 beta\_2: float, default=0.999  <br>  <br>Exponential decay rate for estimates of second moment vector in adam,  <br>should be in \[0, 1). Only used when solver='adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=beta_2,-float%2C%20default%3D0.999) | 0.999 |\
|     | [epsilon epsilon: float, default=1e-8  <br>  <br>Value for numerical stability in adam. Only used when solver='adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=epsilon,-float%2C%20default%3D1e-8) | 1e-08 |\
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Maximum number of epochs to not meet \`\`tol\`\` improvement.  <br>Only effective when solver='sgd' or 'adam'.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |\
|     | [max\_fun max\_fun: int, default=15000  <br>  <br>Only used when solver='lbfgs'. Maximum number of function calls.  <br>The solver iterates until convergence (determined by \`\`tol\`\`), number  <br>of iterations reaches max\_iter, or this number of function calls.  <br>Note that number of function calls will be greater than or equal to  <br>the number of iterations for the MLPRegressor.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=max_fun,-int%2C%20default%3D15000) | 15000 |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [best\_loss\_ best\_loss\_: float  <br>  <br>The minimum loss reached by the solver throughout fitting.  <br>If \`early\_stopping=True\`, this attribute is set to \`None\`. Refer to  <br>the \`best\_validation\_score\_\` fitted attribute instead.  <br>Only accessible when solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=best_loss_,-float) | float64 | 1110 |\
| [best\_validation\_score\_ best\_validation\_score\_: float or None  <br>  <br>The best validation score (i.e. R2 score) that triggered the  <br>early stopping. Only available if \`early\_stopping=True\`, otherwise the  <br>attribute is set to \`None\`.  <br>Only accessible when solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=best_validation_score_,-float%20or%20None) | NoneType | None |\
| [coefs\_ coefs\_: list of shape (n\_layers - 1,)  <br>  <br>The ith element in the list represents the weight matrix corresponding  <br>to layer i.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=coefs_,-list%20of%20shape%20%28n_layers%20-%201%2C%29) | list | \[array(\[\[ 2.26...1628603e-01\]\]), array(\[\[ 0.16...pe=(100, 100)), array(\[\[ 0.22... 0.43165108\]\])\] |\
| [intercepts\_ intercepts\_: list of shape (n\_layers - 1,)  <br>  <br>The ith element in the list represents the bias vector corresponding to  <br>layer i + 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=intercepts_,-list%20of%20shape%20%28n_layers%20-%201%2C%29) | list | \[array(\[ 0.369... 0.27554867\]), array(\[ 0.313... 0.03395789\]), array(\[0.3372181\])\] |\
| [loss\_ loss\_: float  <br>  <br>The current loss computed with the loss function.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=loss_,-float) | float64 | 1110 |\
| [loss\_curve\_ loss\_curve\_: list of shape (\`n\_iter\_\`,)  <br>  <br>Loss value evaluated at the end of each training step.  <br>The ith element in the list represents the loss at the ith iteration.  <br>Only accessible when solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=loss_curve_,-list%20of%20shape%20%28n_iter_%2C%29) | list | \[np.float64(14432.825030436637), np.float64(14372.921005126946), np.float64(14311.387710317184), np.float64(14245.964671913125), ...\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=n_features_in_,-int) | int | 10  |\
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations the solver has run.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=n_iter_,-int) | int | 500 |\
| [n\_layers\_ n\_layers\_: int  <br>  <br>Number of layers.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=n_layers_,-int) | int | 4   |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>Number of outputs.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=n_outputs_,-int) | int | 1   |\
| [out\_activation\_ out\_activation\_: str  <br>  <br>Name of the output activation function.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=out_activation_,-str) | str | 'id...ty' |\
| [t\_ t\_: int  <br>  <br>The number of training samples seen by the solver during fitting.  <br>Mathematically equals \`n\_iters \* X.shape\[0\]\`, it means  <br>\`time\_step\` and it is used by optimizer's learning rate scheduler.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=t_,-int) | int | 221000 |\
| [validation\_scores\_ validation\_scores\_: list of shape (\`n\_iter\_\`,) or None  <br>  <br>The score at each iteration on a held-out validation set. The score  <br>reported is the R2 score. Only available if \`early\_stopping=True\`,  <br>otherwise the attribute is set to \`None\`.  <br>Only accessible when solver='sgd' or 'adam'.](https://scikit-learn.org/1.9/modules/generated/sklearn.neural_network.MLPRegressor.html#:~:text=validation_scores_,-list%20of%20shape%20%28n_iter_%2C%29%20or%20None) | NoneType | None |\
\
  \
  \
\
Plotting partial dependence for two features[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#plotting-partial-dependence-for-two-features "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We plot partial dependence curves for features “age” and “bmi” (body mass index) for the decision tree. With two features, [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
 expects to plot two curves. Here the plot function place a grid of two plots using the space defined by `ax` .\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(12, 6))\
ax.set\_title("Decision Tree")\
tree\_disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
(tree, X, \["age", "bmi"\], ax\=ax)\
\
Copy to clipboard\
\
![Decision Tree](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_001.png)\
\
The partial dependence curves can be plotted for the multi-layer perceptron. In this case, `line_kw` is passed to [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
 to change the color of the curve.\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(12, 6))\
ax.set\_title("Multi-layer Perceptron")\
mlp\_disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
(\
    mlp, X, \["age", "bmi"\], ax\=ax, line\_kw\={"color": "red"}\
)\
\
Copy to clipboard\
\
![Multi-layer Perceptron](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_002.png)\
\
Plotting partial dependence of the two models together[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#plotting-partial-dependence-of-the-two-models-together "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The `tree_disp` and `mlp_disp` [`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay")\
 objects contain all the computed information needed to recreate the partial dependence curves. This means we can easily create additional plots without needing to recompute the curves.\
\
One way to plot the curves is to place them in the same figure, with the curves of each model on each row. First, we create a figure with two axes within two rows and one column. The two axes are passed to the [`plot`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "sklearn.inspection.PartialDependenceDisplay.plot")\
 functions of `tree_disp` and `mlp_disp`. The given axes will be used by the plotting function to draw the partial dependence. The resulting plot places the decision tree partial dependence curves in the first row of the multi-layer perceptron in the second row.\
\
fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(2, 1, figsize\=(10, 10))\
tree\_disp.plot(ax\=ax1)\
ax1.set\_title("Decision Tree")\
mlp\_disp.plot(ax\=ax2, line\_kw\={"color": "red"})\
ax2.set\_title("Multi-layer Perceptron")\
\
Copy to clipboard\
\
![Decision Tree, Multi-layer Perceptron](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_003.png)\
\
Text(0.5, 1.0, 'Multi-layer Perceptron')\
\
Copy to clipboard\
\
Another way to compare the curves is to plot them on top of each other. Here, we create a figure with one row and two columns. The axes are passed into the [`plot`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.plot "sklearn.inspection.PartialDependenceDisplay.plot")\
 function as a list, which will plot the partial dependence curves of each model on the same axes. The length of the axes list must be equal to the number of plots drawn.\
\
fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(1, 2, figsize\=(10, 6))\
tree\_disp.plot(ax\=\[ax1, ax2\], line\_kw\={"label": "Decision Tree"})\
mlp\_disp.plot(\
    ax\=\[ax1, ax2\], line\_kw\={"label": "Multi-layer Perceptron", "color": "red"}\
)\
ax1.legend()\
ax2.legend()\
\
Copy to clipboard\
\
![plot partial dependence visualization api](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_004.png)\
\
<matplotlib.legend.Legend object at 0x7e1d3b4b23c0>\
\
Copy to clipboard\
\
`tree_disp.axes_` is a numpy array container the axes used to draw the partial dependence plots. This can be passed to `mlp_disp` to have the same affect of drawing the plots on top of each other. Furthermore, the `mlp_disp.figure_` stores the figure, which allows for resizing the figure after calling `plot`. In this case `tree_disp.axes_` has two dimensions, thus `plot` will only show the y label and y ticks on the left most plot.\
\
tree\_disp.plot(line\_kw\={"label": "Decision Tree"})\
mlp\_disp.plot(\
    line\_kw\={"label": "Multi-layer Perceptron", "color": "red"}, ax\=tree\_disp.axes\_\
)\
tree\_disp.figure\_.set\_size\_inches(10, 6)\
tree\_disp.axes\_\[0, 0\].legend()\
tree\_disp.axes\_\[0, 1\].legend()\
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")\
()\
\
Copy to clipboard\
\
![plot partial dependence visualization api](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_005.png)\
\
Plotting partial dependence for one feature[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html#plotting-partial-dependence-for-one-feature "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Here, we plot the partial dependence curves for a single feature, “age”, on the same axes. In this case, `tree_disp.axes_` is passed into the second plot function.\
\
tree\_disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
(tree, X, \["age"\])\
mlp\_disp \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")\
(\
    mlp, X, \["age"\], ax\=tree\_disp.axes\_, line\_kw\={"color": "red"}\
)\
\
Copy to clipboard\
\
![plot partial dependence visualization api](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_006.png)\
\
**Total running time of the script:** (0 minutes 2.651 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_partial_dependence_visualization_api.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_partial_dependence_visualization_api.ipynb)\
\
[`Download Jupyter notebook: plot_partial_dependence_visualization_api.ipynb`](https://scikit-learn.org/stable/_downloads/abbd34291d325c02bf490b4681c1caaf/plot_partial_dependence_visualization_api.ipynb)\
\
[`Download Python source code: plot_partial_dependence_visualization_api.py`](https://scikit-learn.org/stable/_downloads/2a5bb775f51861a7dac54a57fc8defb3/plot_partial_dependence_visualization_api.py)\
\
[`Download zipped: plot_partial_dependence_visualization_api.zip`](https://scikit-learn.org/stable/_downloads/80756891dc03ef1e57f032fa5e504cd0/plot_partial_dependence_visualization_api.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_thumb.png)\
\
[Partial Dependence and Individual Conditional Expectation Plots](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)\
\
Partial Dependence and Individual Conditional Expectation Plots\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_monotonic_constraints_thumb.png)\
\
[Monotonic Constraints](https://scikit-learn.org/stable/auto_examples/ensemble/plot_monotonic_constraints.html)\
\
Monotonic Constraints\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_thumb.png)\
\
[Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)\
\
Using KBinsDiscretizer to discretize continuous features\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)\
\
Release Highlights for scikit-learn 0.24\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/2a5bb775f51861a7dac54a57fc8defb3/plot_partial_dependence_visualization_api.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/abbd34291d325c02bf490b4681c1caaf/plot_partial_dependence_visualization_api.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/80756891dc03ef1e57f032fa5e504cd0/plot_partial_dependence_visualization_api.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_partial_dependence_visualization_api.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_partial_dependence_visualization_api.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)