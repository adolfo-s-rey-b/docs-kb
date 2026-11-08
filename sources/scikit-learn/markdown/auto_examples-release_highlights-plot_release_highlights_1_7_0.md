[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-7-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.7[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#release-highlights-for-scikit-learn-1-7 "Link to this heading")

===============================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 1.7! Many bug fixes and improvements were added, as well as some key new features. Below we detail the highlights of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.7.html#release-notes-1-7)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

Improved estimator’s HTML representation[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#improved-estimator-s-html-representation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The HTML representation of estimators now includes a section containing the list of parameters and their values. Non-default parameters are highlighted in orange. A copy button is also available to copy the “fully-qualified” parameter name without the need to call the `get_params` method. It is particularly useful when defining a parameter grid for a grid-search or a randomized-search with a complex pipeline.

See the example below and click on the different estimator’s blocks to see the improved HTML representation.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
(with\_std\=False), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(C\=2.0))
model

Copy to clipboard

Pipeline(steps=\[('standardscaler', StandardScaler(with\_std=False)),\
                ('logisticregression', LogisticRegression(C=2.0))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('standardscaler', ...), ('logisticregression', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | False |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 2.0 |
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |

  
  

Custom validation set for histogram-based Gradient Boosting estimators[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#custom-validation-set-for-histogram-based-gradient-boosting-estimators "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`ensemble.HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
 and [`ensemble.HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 now support directly passing a custom validation set for early stopping to the `fit` method, using the `X_val`, `y_val`, and `sample_weight_val` parameters. In a [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
, the validation set `X_val` can be transformed along with `X` using the `transform_input` parameter.

import sklearn
from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.ensemble import [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

[sklearn.set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(enable\_metadata\_routing\=True)

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(random\_state\=0)
X\_train, X\_val, y\_train, y\_val \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.2, random\_state\=0)

clf \= [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier")
()
clf.set\_fit\_request(X\_val\=True, y\_val\=True)

model \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(\[("sc", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()), ("clf", clf)\], transform\_input\=\["X\_val"\])
model.fit(X, y, X\_val\=X\_val, y\_val\=y\_val)

Copy to clipboard

Pipeline(steps=\[('sc', StandardScaler()),\
                ('clf', HistGradientBoostingClassifier())\],
         transform\_input=\['X\_val'\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('sc', ...), ('clf', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | \['X\_val'\] |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 20  |

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
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](20,) | \[-0.2 ,-0.07,-0.02,...,-0.05, 0.22,-0.15\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 20  |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 100 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](20,) | \[0.92,1.06,0.98,...,1.28,1.08,0.88\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](20,) | \[0.84,1.13,0.96,...,1.65,1.17,0.77\] |

20 features

|     |
| --- |
| x0  |
| x1  |
| x2  |
| x3  |
| x4  |
| x5  |
| x6  |
| x7  |
| x8  |
| x9  |
| x10 |
| x11 |
| x12 |
| x13 |
| x14 |
| x15 |
| x16 |
| x17 |
| x18 |
| x19 |

HistGradientBoostingClassifier

[?Documentation for HistGradientBoostingClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [loss loss: {'log\_loss'}, default='log\_loss'  <br>  <br>The loss function to use in the boosting process.  <br>  <br>For binary classification problems, 'log\_loss' is also known as logistic loss,  <br>binomial deviance or binary crossentropy. Internally, the model fits one tree  <br>per boosting iteration and uses the logistic sigmoid function (expit) as  <br>inverse link function to compute the predicted positive class probability.  <br>  <br>For multiclass classification problems, 'log\_loss' is also known as multinomial  <br>deviance or categorical crossentropy. Internally, the model fits one tree per  <br>boosting iteration and per class and uses the softmax function as inverse link  <br>function to compute the predicted probabilities of the classes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=loss,-%7B%27log_loss%27%7D%2C%20default%3D%27log_loss%27) | 'log\_loss' |
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees for binary classification. For multiclass  <br>classification, \`n\_classes\` trees per iteration are built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | 'from\_dtype' |
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>The constraints are only valid for binary classifications and hold  <br>over the probability of the positive class.  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: :ref:\`accuracy <accuracy\_score>\` is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores. The higher the  <br>tolerance, the more likely we are to early stop: higher tolerance  <br>means that it will be harder for subsequent iterations to be  <br>considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`{class\_label: weight}\`.  <br>If not given, all classes are supposed to have weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`n\_samples / (n\_classes \* np.bincount(y))\`.  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if \`sample\_weight\` is specified.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: array, shape = (n\_classes,)  <br>  <br>Class labels.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=classes_,-array%2C%20shape%20%3D%20%28n_classes%2C%29) | ndarray\[int64\](2,) | \[0,1\] |
| [do\_early\_stopping\_ do\_early\_stopping\_: bool  <br>  <br>Indicates whether early stopping is used during training.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=do_early_stopping_,-bool) | bool | False |
| [is\_categorical\_ is\_categorical\_: ndarray, shape (n\_features, ) or None  <br>  <br>Boolean mask for the categorical features. \`\`None\`\` if there are no  <br>categorical features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=is_categorical_,-ndarray%2C%20shape%20%28n_features%2C%20%29%20or%20None) | NoneType | None |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_features_in_,-int) | int | 20  |
| [n\_iter\_ n\_iter\_: int  <br>  <br>The number of iterations as selected by early stopping, depending on  <br>the \`early\_stopping\` parameter. Otherwise it corresponds to max\_iter.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_iter_,-int) | int | 100 |
| [n\_trees\_per\_iteration\_ n\_trees\_per\_iteration\_: int  <br>  <br>The number of tree that are built at each iteration. This is equal to 1  <br>for binary classification, and to \`\`n\_classes\`\` for multiclass  <br>classification.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=n_trees_per_iteration_,-int) | int | 1   |
| [train\_score\_ train\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the training data. The first entry  <br>is the score of the ensemble before the first iteration. Scores are  <br>computed according to the \`\`scoring\`\` parameter. If \`\`scoring\`\` is  <br>not 'loss', scores are computed on a subset of at most 10 000  <br>samples. Empty if no early stopping.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=train_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |
| [validation\_score\_ validation\_score\_: ndarray, shape (n\_iter\_+1,)  <br>  <br>The scores at each iteration on the held-out validation data. The  <br>first entry is the score of the ensemble before the first iteration.  <br>Scores are computed according to the \`\`scoring\`\` parameter. Empty if  <br>no early stopping or if \`\`validation\_fraction\`\` is None.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#:~:text=validation_score_,-ndarray%2C%20shape%20%28n_iter_%2B1%2C%29) | ndarray\[float64\](0,) | \[\] |

  
  

Plotting ROC curves from cross-validation results[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#plotting-roc-curves-from-cross-validation-results "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The class [`metrics.RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")
 has a new class method `from_cv_results` that allows to easily plot multiple ROC curves from the results of [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
.

from sklearn.datasets import [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import RocCurveDisplay
from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")

X, y \= [make\_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
(n\_samples\=150, random\_state\=0)
clf \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
(random\_state\=0)
cv\_results \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(clf, X, y, cv\=5, return\_estimator\=True, return\_indices\=True)
\_ \= [RocCurveDisplay.from\_cv\_results](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")
(cv\_results, X, y)

Copy to clipboard

![plot release highlights 1 7 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_001.png)

Array API support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#array-api-support "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Several functions have been updated to support array API compatible inputs since version 1.6, especially metrics from the [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
 module.

In addition, it is no longer required to install the `array-api-compat` package to use the experimental array API support in scikit-learn.

Please refer to the [array API support](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 page for instructions to use scikit-learn with array API compatible libraries such as PyTorch or CuPy.

Improved API consistency of Multi-layer Perceptron[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#improved-api-consistency-of-multi-layer-perceptron "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 has a new parameter `loss` and now supports the “poisson” loss in addition to the default “squared\_error” loss. Moreover, the [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
 and [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 estimators now support sample weights. These improvements have been made to improve the consistency of these estimators with regard to the other estimators in scikit-learn.

Migration toward sparse arrays[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html#migration-toward-sparse-arrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to prepare [SciPy migration from sparse matrices to sparse arrays](https://docs.scipy.org/doc/scipy/reference/sparse.migration_to_sparray.html)
, all scikit-learn estimators that accept sparse matrices as input now also accept sparse arrays.

**Total running time of the script:** (0 minutes 0.163 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_7_0.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_7_0.ipynb)

[`Download Jupyter notebook: plot_release_highlights_1_7_0.ipynb`](https://scikit-learn.org/stable/_downloads/b7d178d09f44d400894015228deb0ddb/plot_release_highlights_1_7_0.ipynb)

[`Download Python source code: plot_release_highlights_1_7_0.py`](https://scikit-learn.org/stable/_downloads/27dd4dbb41dee53fc86e0d5b6d3254d3/plot_release_highlights_1_7_0.py)

[`Download zipped: plot_release_highlights_1_7_0.zip`](https://scikit-learn.org/stable/_downloads/0f052545c78541815099d62501f25a9e/plot_release_highlights_1_7_0.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/27dd4dbb41dee53fc86e0d5b6d3254d3/plot_release_highlights_1_7_0.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/b7d178d09f44d400894015228deb0ddb/plot_release_highlights_1_7_0.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/0f052545c78541815099d62501f25a9e/plot_release_highlights_1_7_0.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_7_0.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_7_0.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)