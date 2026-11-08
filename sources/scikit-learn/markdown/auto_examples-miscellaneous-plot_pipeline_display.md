[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_pipeline_display.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_pipeline_display.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_pipeline_display.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_pipeline_display.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_pipeline_display.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_pipeline_display.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#sphx-glr-download-auto-examples-miscellaneous-plot-pipeline-display-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Displaying Pipelines[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#displaying-pipelines "Link to this heading")

============================================================================================================================================================

The default configuration for displaying a pipeline in a Jupyter Notebook is `'diagram'` where `set_config(display='diagram')`. To deactivate HTML representation, use `set_config(display='text')`.

To see more detailed steps in the visualization of the pipeline, click on the steps in the pipeline.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Displaying a Pipeline with a Preprocessing Step and Classifier[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#displaying-a-pipeline-with-a-preprocessing-step-and-classifier "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section constructs a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 with a preprocessing step, [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
, and classifier, [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
, and displays its visual representation.

from sklearn import [set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

steps \= \[\
    ("preprocessing", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
    ("classifier", [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
()),\
\]
pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(steps)

Copy to clipboard

To visualize the diagram, the default is `display='diagram'`.

[set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(display\="diagram")
pipe  \# click on the diagram below to see the details of each step

Copy to clipboard

Pipeline(steps=\[('preprocessing', StandardScaler()),\
                ('classifier', LogisticRegression())\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('preprocessing', ...), ('classifier', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

LogisticRegression

[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |
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

  
  

To view the text pipeline, change to `display='text'`.

[set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(display\="text")
pipe

Copy to clipboard

Pipeline(steps=\[('preprocessing', StandardScaler()),\
                ('classifier', LogisticRegression())\])

Copy to clipboard

Put back the default display

[set\_config](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
(display\="diagram")

Copy to clipboard

Displaying a Pipeline Chaining Multiple Preprocessing Steps & Classifier[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#displaying-a-pipeline-chaining-multiple-preprocessing-steps-classifier "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section constructs a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 with multiple preprocessing steps, [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
 and [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
, and a classifier step, [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
, and displays its visual representation.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

steps \= \[\
    ("standard\_scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
    ("polynomial", [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")\
(degree\=3)),\
    ("classifier", [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(C\=2.0)),\
\]
pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(steps)
pipe  \# click on the diagram below to see the details of each step

Copy to clipboard

Pipeline(steps=\[('standard\_scaler', StandardScaler()),\
                ('polynomial', PolynomialFeatures(degree=3)),\
                ('classifier', LogisticRegression(C=2.0))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('standard\_scaler', ...), ('polynomial', ...), ...\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

StandardScaler

[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |

PolynomialFeatures

[?Documentation for PolynomialFeatures](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [degree degree: int or tuple (min\_degree, max\_degree), default=2  <br>  <br>If a single int is given, it specifies the maximal degree of the  <br>polynomial features. If a tuple \`(min\_degree, max\_degree)\` is passed,  <br>then \`min\_degree\` is the minimum and \`max\_degree\` is the maximum  <br>polynomial degree of the generated features. Note that \`min\_degree=0\`  <br>and \`min\_degree=1\` are equivalent as outputting the degree zero term is  <br>determined by \`include\_bias\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=degree,-int%20or%20tuple%20%28min_degree%2C%20max_degree%29%2C%20default%3D2) | 3   |
|     | [interaction\_only interaction\_only: bool, default=False  <br>  <br>If \`True\`, only interaction features are produced: features that are  <br>products of at most \`degree\` \*distinct\* input features, i.e. terms with  <br>power of 2 or higher of the same input feature are excluded:  <br>  <br>\- included: \`x\[0\]\`, \`x\[1\]\`, \`x\[0\] \* x\[1\]\`, etc.  <br>\- excluded: \`x\[0\] \*\* 2\`, \`x\[0\] \*\* 2 \* x\[1\]\`, etc.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=interaction_only,-bool%2C%20default%3DFalse) | False |
|     | [include\_bias include\_bias: bool, default=True  <br>  <br>If \`True\` (default), then include a bias column, the feature in which  <br>all polynomial powers are zero (i.e. a column of ones - acts as an  <br>intercept term in a linear model).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=include_bias,-bool%2C%20default%3DTrue) | True |
|     | [order order: {'C', 'F'}, default='C'  <br>  <br>Order of output array in the dense case. \`'F'\` order is faster to  <br>compute, but may slow down subsequent estimators.  <br>  <br>.. versionadded:: 0.21](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#:~:text=order,-%7B%27C%27%2C%20%27F%27%7D%2C%20default%3D%27C%27) | 'C' |

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

  
  

Displaying a Pipeline and Dimensionality Reduction and Classifier[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#displaying-a-pipeline-and-dimensionality-reduction-and-classifier "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section constructs a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 with a dimensionality reduction step, [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, a classifier, [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
, and displays its visual representation.

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

steps \= \[("reduce\_dim", [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(n\_components\=4)), ("classifier", [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")\
(kernel\="linear"))\]
pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(steps)
pipe  \# click on the diagram below to see the details of each step

Copy to clipboard

Pipeline(steps=\[('reduce\_dim', PCA(n\_components=4)),\
                ('classifier', SVC(kernel='linear'))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('reduce\_dim', ...), ('classifier', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

PCA

[?Documentation for PCA](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_components n\_components: int, float or 'mle', default=None  <br>  <br>Number of components to keep.  <br>if n\_components is not set all components are kept::  <br>  <br>n\_components == min(n\_samples, n\_features)  <br>  <br>If \`\`n\_components == 'mle'\`\` and \`\`svd\_solver == 'full'\`\`, Minka's  <br>MLE is used to guess the dimension. Use of \`\`n\_components == 'mle'\`\`  <br>will interpret \`\`svd\_solver == 'auto'\`\` as \`\`svd\_solver == 'full'\`\`.  <br>  <br>If \`\`0 < n\_components < 1\`\` and \`\`svd\_solver == 'full'\`\`, select the  <br>number of components such that the amount of variance that needs to be  <br>explained is greater than the percentage specified by n\_components.  <br>  <br>If \`\`svd\_solver == 'arpack'\`\`, the number of components must be  <br>strictly less than the minimum of n\_features and n\_samples.  <br>  <br>Hence, the None case results in::  <br>  <br>n\_components == min(n\_samples, n\_features) - 1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_components,-int%2C%20float%20or%20%27mle%27%2C%20default%3DNone) | 4   |
|     | [copy copy: bool, default=True  <br>  <br>If False, data passed to fit are overwritten and running  <br>fit(X).transform(X) will not yield the expected results,  <br>use fit\_transform(X) instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [whiten whiten: bool, default=False  <br>  <br>When True (False by default) the \`components\_\` vectors are multiplied  <br>by the square root of n\_samples and then divided by the singular values  <br>to ensure uncorrelated outputs with unit component-wise variances.  <br>  <br>Whitening will remove some information from the transformed signal  <br>(the relative variance scales of the components) but can sometime  <br>improve the predictive accuracy of the downstream estimators by  <br>making their data respect some hard-wired assumptions.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=whiten,-bool%2C%20default%3DFalse) | False |
|     | [svd\_solver svd\_solver: {'auto', 'full', 'covariance\_eigh', 'arpack', 'randomized'}, default='auto'  <br>  <br>"auto" :  <br>The solver is selected by a default 'auto' policy is based on \`X.shape\` and  <br>\`n\_components\`: if the input data has fewer than 1000 features and  <br>more than 10 times as many samples, then the "covariance\_eigh"  <br>solver is used. Otherwise, if the input data is larger than 500x500  <br>and the number of components to extract is lower than 80% of the  <br>smallest dimension of the data, then the more efficient  <br>"randomized" method is selected. Otherwise the exact "full" SVD is  <br>computed and optionally truncated afterwards.  <br>"full" :  <br>Run exact full SVD calling the standard LAPACK solver via  <br>\`scipy.linalg.svd\` and select the components by postprocessing  <br>"covariance\_eigh" :  <br>Precompute the covariance matrix (on centered data), run a  <br>classical eigenvalue decomposition on the covariance matrix  <br>typically using LAPACK and select the components by postprocessing.  <br>This solver is very efficient for n\_samples >> n\_features and small  <br>n\_features. It is, however, not tractable otherwise for large  <br>n\_features (large memory footprint required to materialize the  <br>covariance matrix). Also note that compared to the "full" solver,  <br>this solver effectively doubles the condition number and is  <br>therefore less numerical stable (e.g. on input data with a large  <br>range of singular values).  <br>"arpack" :  <br>Run SVD truncated to \`n\_components\` calling ARPACK solver via  <br>\`scipy.sparse.linalg.svds\`. It requires strictly  <br>\`0 < n\_components < min(X.shape)\`  <br>"randomized" :  <br>Run randomized SVD by the method of Halko et al.  <br>  <br>.. versionadded:: 0.18.0  <br>  <br>.. versionchanged:: 1.5  <br>Added the 'covariance\_eigh' solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=svd_solver,-%7B%27auto%27%2C%20%27full%27%2C%20%27covariance_eigh%27%2C%20%27arpack%27%2C%20%27randomized%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27auto%27) | 'auto' |
|     | [tol tol: float, default=0.0  <br>  <br>Tolerance for singular values computed by svd\_solver == 'arpack'.  <br>Must be of range \[0.0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=tol,-float%2C%20default%3D0.0) | 0.0 |\
|     | [iterated\_power iterated\_power: int or 'auto', default='auto'  <br>  <br>Number of iterations for the power method computed by  <br>svd\_solver == 'randomized'.  <br>Must be of range \[0, infinity).  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=iterated_power,-int%20or%20%27auto%27%2C%20default%3D%27auto%27) | 'auto' |\
|     | [n\_oversamples n\_oversamples: int, default=10  <br>  <br>This parameter is only relevant when \`svd\_solver="randomized"\`.  <br>It corresponds to the additional number of random vectors to sample the  <br>range of \`X\` so as to ensure proper conditioning. See  <br>:func:\`~sklearn.utils.extmath.randomized\_svd\` for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=n_oversamples,-int%2C%20default%3D10) | 10  |\
|     | [power\_iteration\_normalizer power\_iteration\_normalizer: {'auto', 'QR', 'LU', 'none'}, default='auto'  <br>  <br>Power iteration normalizer for randomized SVD solver.  <br>Not used by ARPACK. See :func:\`~sklearn.utils.extmath.randomized\_svd\`  <br>for more details.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=power_iteration_normalizer,-%7B%27auto%27%2C%20%27QR%27%2C%20%27LU%27%2C%20%27none%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Used when the 'arpack' or 'randomized' solvers are used. Pass an int  <br>for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.  <br>  <br>.. versionadded:: 0.18.0](https://scikit-learn.org/1.9/modules/generated/sklearn.decomposition.PCA.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
\
SVC\
\
[?Documentation for SVC](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [kernel kernel: {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'} or callable, default='rbf'  <br>  <br>Specifies the kernel type to be used in the algorithm. If  <br>none is given, 'rbf' will be used. If a callable is given it is used to  <br>pre-compute the kernel matrix from data matrices; that matrix should be  <br>an array of shape \`\`(n\_samples, n\_samples)\`\`. For an intuitive  <br>visualization of different kernel types see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_kernels.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=kernel,-%7B%27linear%27%2C%20%27poly%27%2C%20%27rbf%27%2C%20%27sigmoid%27%2C%20%27precomputed%27%7D%20or%20callable%2C%20%20%20%20%20%20%20%20%20%20default%3D%27rbf%27) | 'linear' |\
|     | [C C: float, default=1.0  <br>  <br>Regularization parameter. The strength of the regularization is  <br>inversely proportional to C. Must be strictly positive. The penalty  <br>is a squared l2 penalty. For an intuitive visualization of the effects  <br>of scaling the regularization parameter C, see  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_scale\_c.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [degree degree: int, default=3  <br>  <br>Degree of the polynomial kernel function ('poly').  <br>Must be non-negative. Ignored by all other kernels.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=degree,-int%2C%20default%3D3) | 3   |\
|     | [gamma gamma: {'scale', 'auto'} or float, default='scale'  <br>  <br>Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.  <br>  <br>\- if \`\`gamma='scale'\`\` (default) is passed then it uses  <br>1 / (n\_features \* X.var()) as value of gamma,  <br>\- if 'auto', uses 1 / n\_features  <br>\- if float, must be non-negative.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`gamma\`\` changed from 'auto' to 'scale'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=gamma,-%7B%27scale%27%2C%20%27auto%27%7D%20or%20float%2C%20default%3D%27scale%27) | 'scale' |\
|     | [coef0 coef0: float, default=0.0  <br>  <br>Independent term in kernel function.  <br>It is only significant in 'poly' and 'sigmoid'.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=coef0,-float%2C%20default%3D0.0) | 0.0 |\
|     | [shrinking shrinking: bool, default=True  <br>  <br>Whether to use the shrinking heuristic.  <br>See the :ref:\`User Guide <shrinking\_svm>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=shrinking,-bool%2C%20default%3DTrue) | True |\
|     | [probability probability: bool, default=False  <br>  <br>Whether to enable probability estimates. This must be enabled prior  <br>to calling \`fit\`, will slow down that method as it internally uses  <br>5-fold cross-validation, and \`predict\_proba\` may be inconsistent with  <br>\`predict\`. Read more in the :ref:\`User Guide <scores\_probabilities>\`.  <br>  <br>..deprecated:: 1.9  <br>The \`probability\` parameter is deprecated and will be removed in 1.11.  <br>Use \`CalibratedClassifierCV(SVC(), ensemble=False)\` instead of  <br>\`SVC(probability=True)\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=probability,-bool%2C%20default%3DFalse) | 'deprecated' |\
|     | [tol tol: float, default=1e-3  <br>  <br>Tolerance for stopping criterion.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=tol,-float%2C%20default%3D1e-3) | 0.001 |\
|     | [cache\_size cache\_size: float, default=200  <br>  <br>Specify the size of the kernel cache (in MB).](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=cache_size,-float%2C%20default%3D200) | 200 |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Set the parameter C of class i to class\_weight\[i\]\*C for  <br>SVC. If not given, all classes are supposed to have  <br>weight one.  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>Enable verbose output. Note that this setting takes advantage of a  <br>per-process runtime setting in libsvm that, if enabled, may not work  <br>properly in a multithreaded context.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [max\_iter max\_iter: int, default=-1  <br>  <br>Hard limit on iterations within solver, or -1 for no limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=max_iter,-int%2C%20default%3D-1) | \-1 |\
|     | [decision\_function\_shape decision\_function\_shape: {'ovo', 'ovr'}, default='ovr'  <br>  <br>Whether to return a one-vs-rest ('ovr') decision function of shape  <br>(n\_samples, n\_classes) as all other classifiers, or the original  <br>one-vs-one ('ovo') decision function of libsvm which has shape  <br>(n\_samples, n\_classes \* (n\_classes - 1) / 2). However, note that  <br>internally, one-vs-one ('ovo') is always used as a multi-class strategy  <br>to train models; an ovr matrix is only constructed from the ovo matrix.  <br>The parameter is ignored for binary classification.  <br>  <br>.. versionchanged:: 0.19  <br>decision\_function\_shape is 'ovr' by default.  <br>  <br>.. versionadded:: 0.17  <br>\*decision\_function\_shape='ovr'\* is recommended.  <br>  <br>.. versionchanged:: 0.17  <br>Deprecated \*decision\_function\_shape='ovo' and None\*.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=decision_function_shape,-%7B%27ovo%27%2C%20%27ovr%27%7D%2C%20default%3D%27ovr%27) | 'ovr' |\
|     | [break\_ties break\_ties: bool, default=False  <br>  <br>If true, \`\`decision\_function\_shape='ovr'\`\`, and number of classes > 2,  <br>:term:\`predict\` will break ties according to the confidence values of  <br>:term:\`decision\_function\`; otherwise the first class among the tied  <br>classes is returned. Please note that breaking ties comes at a  <br>relatively high computational cost compared to a simple predict. See  <br>:ref:\`sphx\_glr\_auto\_examples\_svm\_plot\_svm\_tie\_breaking.py\` for an  <br>example of its usage with \`\`decision\_function\_shape='ovr'\`\`.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=break_ties,-bool%2C%20default%3DFalse) | False |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls the pseudo random number generation for shuffling the data for  <br>probability estimates. Ignored when \`probability\` is False.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.svm.SVC.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
\
  \
  \
\
Displaying a Complex Pipeline Chaining a Column Transformer[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#displaying-a-complex-pipeline-chaining-a-column-transformer "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
This section constructs a complex [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
 with a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
 and a classifier, [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
, and displays its visual representation.\
\
import numpy as np\
\
from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
from sklearn.impute import [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
, [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
\
numeric\_preprocessor \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    steps\=\[\
        ("imputation\_mean", [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
(missing\_values\=[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
, strategy\="mean")),\
        ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
    \]\
)\
\
categorical\_preprocessor \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    steps\=\[\
        (\
            "imputation\_constant",\
            [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
(fill\_value\="missing", strategy\="constant"),\
        ),\
        ("onehot", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore")),\
    \]\
)\
\
preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
    \[\
        ("categorical", categorical\_preprocessor, \["state", "gender"\]),\
        ("numerical", numeric\_preprocessor, \["age", "weight"\]),\
    \]\
)\
\
pipe \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(preprocessor, [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
(max\_iter\=500))\
pipe  \# click on the diagram below to see the details of each step\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(transformers=\[('categorical',\
                                                  Pipeline(steps=\[('imputation\_constant',\
                                                                   SimpleImputer(fill\_value='missing',\
                                                                                 strategy='constant')),\
                                                                  ('onehot',\
                                                                   OneHotEncoder(handle\_unknown='ignore'))\]),\
                                                  \['state', 'gender'\]),\
                                                 ('numerical',\
                                                  Pipeline(steps=\[('imputation\_mean',\
                                                                   SimpleImputer()),\
                                                                  ('scaler',\
                                                                   StandardScaler())\]),\
                                                  \['age', 'weight'\])\])),\
                ('logisticregression', LogisticRegression(max\_iter=500))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iNot fitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('logisticregression', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('numerical', ...)\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |\
\
categorical\
\
\['state', 'gender'\]\
\
SimpleImputer\
\
[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'constant' |\
|     | [fill\_value fill\_value: str or numerical value, default=None  <br>  <br>When strategy == "constant", \`fill\_value\` is used to replace all  <br>occurrences of missing\_values. For string or object data types,  <br>\`fill\_value\` must be a string.  <br>If \`None\`, \`fill\_value\` will be 0 when imputing numerical  <br>data and "missing\_value" for strings or object data types.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=fill_value,-str%20or%20numerical%20value%2C%20default%3DNone) | 'missing' |\
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |\
|     | [copy copy: bool, default=True  <br>  <br>If True, a copy of X will be created. If False, imputation will  <br>be done in-place whenever possible. Note that, in the following cases,  <br>a new copy will always be made, even if \`copy=False\`:  <br>  <br>\- If \`X\` is not an array of floating values;  <br>\- If \`X\` is encoded as a CSR matrix;  <br>\- If \`add\_indicator=True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [add\_indicator add\_indicator: bool, default=False  <br>  <br>If True, a :class:\`MissingIndicator\` transform will stack onto output  <br>of the imputer's transform. This allows a predictive estimator  <br>to account for missingness despite imputation. If a feature has no  <br>missing values at fit/train time, the feature won't appear on  <br>the missing indicator even if there are missing values at  <br>transform/test time.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=add_indicator,-bool%2C%20default%3DFalse) | False |\
|     | [keep\_empty\_features keep\_empty\_features: bool, default=False  <br>  <br>If True, features that consist exclusively of missing values when  <br>\`fit\` is called are returned in results when \`transform\` is called.  <br>The imputed value is always \`0\` except when \`strategy="constant"\`  <br>in which case \`fill\_value\` will be used instead.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=keep_empty_features,-bool%2C%20default%3DFalse) | False |\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
numerical\
\
\['age', 'weight'\]\
\
SimpleImputer\
\
[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |\
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'mean' |\
|     | [fill\_value fill\_value: str or numerical value, default=None  <br>  <br>When strategy == "constant", \`fill\_value\` is used to replace all  <br>occurrences of missing\_values. For string or object data types,  <br>\`fill\_value\` must be a string.  <br>If \`None\`, \`fill\_value\` will be 0 when imputing numerical  <br>data and "missing\_value" for strings or object data types.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=fill_value,-str%20or%20numerical%20value%2C%20default%3DNone) | None |\
|     | [copy copy: bool, default=True  <br>  <br>If True, a copy of X will be created. If False, imputation will  <br>be done in-place whenever possible. Note that, in the following cases,  <br>a new copy will always be made, even if \`copy=False\`:  <br>  <br>\- If \`X\` is not an array of floating values;  <br>\- If \`X\` is encoded as a CSR matrix;  <br>\- If \`add\_indicator=True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [add\_indicator add\_indicator: bool, default=False  <br>  <br>If True, a :class:\`MissingIndicator\` transform will stack onto output  <br>of the imputer's transform. This allows a predictive estimator  <br>to account for missingness despite imputation. If a feature has no  <br>missing values at fit/train time, the feature won't appear on  <br>the missing indicator even if there are missing values at  <br>transform/test time.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=add_indicator,-bool%2C%20default%3DFalse) | False |\
|     | [keep\_empty\_features keep\_empty\_features: bool, default=False  <br>  <br>If True, features that consist exclusively of missing values when  <br>\`fit\` is called are returned in results when \`transform\` is called.  <br>The imputed value is always \`0\` except when \`strategy="constant"\`  <br>in which case \`fill\_value\` will be used instead.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=keep_empty_features,-bool%2C%20default%3DFalse) | False |\
\
StandardScaler\
\
[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |\
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 500 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 1.0 |\
|     | [l1\_ratio l1\_ratio: float, default=0.0  <br>  <br>The Elastic-Net mixing parameter, with \`0 <= l1\_ratio <= 1\`. Setting  <br>\`l1\_ratio=1\` gives a pure L1-penalty, setting \`l1\_ratio=0\` a pure L2-penalty.  <br>Any value between 0 and 1 gives an Elastic-Net penalty of the form  <br>\`l1\_ratio \* L1 + (1 - l1\_ratio) \* L2\`.  <br>  <br>.. warning::  <br>Certain values of \`l1\_ratio\`, i.e. some penalties, may not work with some  <br>solvers. See the parameter \`solver\` below, to know the compatibility between  <br>the penalty and solver.  <br>  <br>.. versionchanged:: 1.8  <br>Default value changed from None to 0.0.  <br>  <br>.. deprecated:: 1.8  <br>\`None\` is deprecated and will be removed in version 1.10. Always use  <br>\`l1\_ratio\` to specify the penalty type.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0 |\
|     | [dual dual: bool, default=False  <br>  <br>Dual (constrained) or primal (regularized, see also  <br>:ref:\`this equation <regularized-logistic-loss>\`) formulation. Dual formulation  <br>is only implemented for l2 penalty with liblinear solver. Prefer \`dual=False\`  <br>when n\_samples > n\_features.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False |\
|     | [tol tol: float, default=1e-4  <br>  <br>Tolerance for stopping criteria.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Specifies if a constant (a.k.a. bias or intercept) should be  <br>added to the decision function.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [intercept\_scaling intercept\_scaling: float, default=1  <br>  <br>Useful only when the solver \`liblinear\` is used  <br>and \`self.fit\_intercept\` is set to \`True\`. In this case, \`x\` becomes  <br>\`\[x, self.intercept\_scaling\]\`,  <br>i.e. a "synthetic" feature with constant value equal to  <br>\`intercept\_scaling\` is appended to the instance vector.  <br>The intercept becomes  <br>\`\`intercept\_scaling \* synthetic\_feature\_weight\`\`.  <br>  <br>.. note::  <br>The synthetic feature weight is subject to L1 or L2  <br>regularization as all other features.  <br>To lessen the effect of regularization on synthetic feature weight  <br>(and therefore on the intercept) \`intercept\_scaling\` has to be increased.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1   |\
|     | [class\_weight class\_weight: dict or 'balanced', default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one.  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.  <br>  <br>.. versionadded:: 0.17  <br>\*class\_weight='balanced'\*](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Only used for \`solver\` == 'sag', 'saga' or 'liblinear' to shuffle the  <br>data. It has no effect on the other solvers.  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
|     | [solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'  <br>  <br>Algorithm to use in the optimization problem. Default is 'lbfgs'.  <br>To choose a solver, you might want to consider the following aspects:  <br>  <br>\- 'lbfgs' is a good default solver because it works reasonably well for a wide  <br>class of problems.  <br>\- For :term:\`multiclass\` problems (\`n\_classes >= 3\`), all solvers except  <br>'liblinear' minimize the full multinomial loss, 'liblinear' will raise an  <br>error.  <br>\- 'newton-cholesky' is a good choice for  <br>\`n\_samples\` >> \`n\_features \* n\_classes\`, especially with one-hot encoded  <br>categorical features with rare categories. Be aware that the memory usage  <br>of this solver has a quadratic dependency on \`n\_features \* n\_classes\`  <br>because it explicitly computes the full Hessian matrix.  <br>\- For small datasets, 'liblinear' is a good choice, whereas 'sag'  <br>and 'saga' are faster for large ones;  <br>\- 'liblinear' can only handle binary classification by default. To apply a  <br>one-versus-rest scheme for the multiclass setting one can wrap it with the  <br>:class:\`~sklearn.multiclass.OneVsRestClassifier\`.  <br>  <br>.. warning::  <br>The choice of the algorithm depends on the penalty chosen (\`l1\_ratio=0\`  <br>for L2-penalty, \`l1\_ratio=1\` for L1-penalty and \`0 < l1\_ratio < 1\` for  <br>Elastic-Net) and on (multinomial) multiclass support:  <br>  <br>\================= ======================== ======================  <br>solver l1\_ratio multinomial multiclass  <br>\================= ======================== ======================  <br>'lbfgs' l1\_ratio=0 yes  <br>'liblinear' l1\_ratio=1 or l1\_ratio=0 no  <br>'newton-cg' l1\_ratio=0 yes  <br>'newton-cholesky' l1\_ratio=0 yes  <br>'sag' l1\_ratio=0 yes  <br>'saga' 0<=l1\_ratio<=1 yes  <br>\================= ======================== ======================  <br>  <br>.. note::  <br>'sag' and 'saga' fast convergence is only guaranteed on features  <br>with approximately the same scale. You can preprocess the data with  <br>a scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>.. seealso::  <br>Refer to the :ref:\`User Guide <Logistic\_regression>\` for more  <br>information regarding :class:\`LogisticRegression\` and more specifically the  <br>:ref:\`Table <logistic\_regression\_solvers>\`  <br>summarizing solver/penalty supports.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient (SAG) descent solver. Multinomial support in  <br>version 0.18.  <br>.. versionadded:: 0.19  <br>SAGA solver.  <br>.. versionchanged:: 0.22  <br>The default solver changed from 'liblinear' to 'lbfgs' in 0.22.  <br>.. versionadded:: 1.2  <br>newton-cholesky solver. Multinomial support in version 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs' |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
  \
  \
\
Displaying a Grid Search over a Pipeline with a Classifier[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#displaying-a-grid-search-over-a-pipeline-with-a-classifier "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
This section constructs a [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
 over a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
 with [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
 and displays its visual representation.\
\
import numpy as np\
\
from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
from sklearn.impute import [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
, [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
\
numeric\_preprocessor \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    steps\=\[\
        ("imputation\_mean", [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
(missing\_values\=[np.nan](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")\
, strategy\="mean")),\
        ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
()),\
    \]\
)\
\
categorical\_preprocessor \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    steps\=\[\
        (\
            "imputation\_constant",\
            [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
(fill\_value\="missing", strategy\="constant"),\
        ),\
        ("onehot", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore")),\
    \]\
)\
\
preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
    \[\
        ("categorical", categorical\_preprocessor, \["state", "gender"\]),\
        ("numerical", numeric\_preprocessor, \["age", "weight"\]),\
    \]\
)\
\
pipe \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    steps\=\[("preprocessor", preprocessor), ("classifier", [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
())\]\
)\
\
param\_grid \= {\
    "classifier\_\_n\_estimators": \[200, 500\],\
    "classifier\_\_max\_features": \["auto", "sqrt", "log2"\],\
    "classifier\_\_max\_depth": \[4, 5, 6, 7, 8\],\
    "classifier\_\_criterion": \["gini", "entropy"\],\
}\
\
grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
(pipe, param\_grid\=param\_grid, n\_jobs\=1)\
grid\_search  \# click on the diagram below to see the details of each step\
\
Copy to clipboard\
\
GridSearchCV(estimator=Pipeline(steps=\[('preprocessor',\
                                        ColumnTransformer(transformers=\[('categorical',\
                                                                         Pipeline(steps=\[('imputation\_constant',\
                                                                                          SimpleImputer(fill\_value='missing',\
                                                                                                        strategy='constant')),\
                                                                                         ('onehot',\
                                                                                          OneHotEncoder(handle\_unknown='ignore'))\]),\
                                                                         \['state',\
                                                                          'gender'\]),\
                                                                        ('numerical',\
                                                                         Pipeline(steps=\[('imputation\_mean',\
                                                                                          SimpleImputer()),\
                                                                                         ('scaler',\
                                                                                          StandardScaler())\]),\
                                                                         \['age',\
                                                                          'weight'\])\])),\
                                       ('classifier',\
                                        RandomForestClassifier())\]),\
             n\_jobs=1,\
             param\_grid={'classifier\_\_criterion': \['gini', 'entropy'\],\
                         'classifier\_\_max\_depth': \[4, 5, 6, 7, 8\],\
                         'classifier\_\_max\_features': \['auto', 'sqrt', 'log2'\],\
                         'classifier\_\_n\_estimators': \[200, 500\]})\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
GridSearchCV\
\
[?Documentation for GridSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html)\
iNot fitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [estimator estimator: estimator object  <br>  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...lassifier())\]) |\
|     | [param\_grid param\_grid: dict or list of dictionaries  <br>  <br>Dictionary with parameters names (\`str\`) as keys and lists of  <br>parameter settings to try as values, or a list of such  <br>dictionaries, in which case the grids spanned by each dictionary  <br>in the list are explored. This enables searching over any sequence  <br>of parameter settings.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=param_grid,-dict%20or%20list%20of%20dictionaries) | {'classifier\_\_criterion': \['gini', 'entropy'\], 'classifier\_\_max\_depth': \[4, 5, ...\], 'classifier\_\_max\_features': \['auto', 'sqrt', ...\], 'classifier\_\_n\_estimators': \[200, 500\]} |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | 1   |\
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | None |\
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`GridSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_digits.py\`  <br>to see how to design a custom selection strategy using a callable  <br>via \`refit\`.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |\
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |\
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.GridSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |\
\
estimator: Pipeline\
\
preprocessor: ColumnTransformer\
\
[?Documentation for preprocessor: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('categorical', ...), ('numerical', ...)\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |\
\
categorical\
\
\['state', 'gender'\]\
\
SimpleImputer\
\
[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'constant' |\
|     | [fill\_value fill\_value: str or numerical value, default=None  <br>  <br>When strategy == "constant", \`fill\_value\` is used to replace all  <br>occurrences of missing\_values. For string or object data types,  <br>\`fill\_value\` must be a string.  <br>If \`None\`, \`fill\_value\` will be 0 when imputing numerical  <br>data and "missing\_value" for strings or object data types.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=fill_value,-str%20or%20numerical%20value%2C%20default%3DNone) | 'missing' |\
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |\
|     | [copy copy: bool, default=True  <br>  <br>If True, a copy of X will be created. If False, imputation will  <br>be done in-place whenever possible. Note that, in the following cases,  <br>a new copy will always be made, even if \`copy=False\`:  <br>  <br>\- If \`X\` is not an array of floating values;  <br>\- If \`X\` is encoded as a CSR matrix;  <br>\- If \`add\_indicator=True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [add\_indicator add\_indicator: bool, default=False  <br>  <br>If True, a :class:\`MissingIndicator\` transform will stack onto output  <br>of the imputer's transform. This allows a predictive estimator  <br>to account for missingness despite imputation. If a feature has no  <br>missing values at fit/train time, the feature won't appear on  <br>the missing indicator even if there are missing values at  <br>transform/test time.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=add_indicator,-bool%2C%20default%3DFalse) | False |\
|     | [keep\_empty\_features keep\_empty\_features: bool, default=False  <br>  <br>If True, features that consist exclusively of missing values when  <br>\`fit\` is called are returned in results when \`transform\` is called.  <br>The imputed value is always \`0\` except when \`strategy="constant"\`  <br>in which case \`fill\_value\` will be used instead.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=keep_empty_features,-bool%2C%20default%3DFalse) | False |\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
numerical\
\
\['age', 'weight'\]\
\
SimpleImputer\
\
[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |\
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'mean' |\
|     | [fill\_value fill\_value: str or numerical value, default=None  <br>  <br>When strategy == "constant", \`fill\_value\` is used to replace all  <br>occurrences of missing\_values. For string or object data types,  <br>\`fill\_value\` must be a string.  <br>If \`None\`, \`fill\_value\` will be 0 when imputing numerical  <br>data and "missing\_value" for strings or object data types.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=fill_value,-str%20or%20numerical%20value%2C%20default%3DNone) | None |\
|     | [copy copy: bool, default=True  <br>  <br>If True, a copy of X will be created. If False, imputation will  <br>be done in-place whenever possible. Note that, in the following cases,  <br>a new copy will always be made, even if \`copy=False\`:  <br>  <br>\- If \`X\` is not an array of floating values;  <br>\- If \`X\` is encoded as a CSR matrix;  <br>\- If \`add\_indicator=True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [add\_indicator add\_indicator: bool, default=False  <br>  <br>If True, a :class:\`MissingIndicator\` transform will stack onto output  <br>of the imputer's transform. This allows a predictive estimator  <br>to account for missingness despite imputation. If a feature has no  <br>missing values at fit/train time, the feature won't appear on  <br>the missing indicator even if there are missing values at  <br>transform/test time.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=add_indicator,-bool%2C%20default%3DFalse) | False |\
|     | [keep\_empty\_features keep\_empty\_features: bool, default=False  <br>  <br>If True, features that consist exclusively of missing values when  <br>\`fit\` is called are returned in results when \`transform\` is called.  <br>The imputed value is always \`0\` except when \`strategy="constant"\`  <br>in which case \`fill\_value\` will be used instead.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=keep_empty_features,-bool%2C%20default%3DFalse) | False |\
\
StandardScaler\
\
[?Documentation for StandardScaler](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [copy copy: bool, default=True  <br>  <br>If False, try to avoid a copy and do inplace scaling instead.  <br>This is not guaranteed to always work inplace; e.g. if the data is  <br>not a NumPy array or scipy.sparse CSR matrix, a copy may still be  <br>returned.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |\
|     | [with\_mean with\_mean: bool, default=True  <br>  <br>If True, center the data before scaling.  <br>This does not work (and will raise an exception) when attempted on  <br>sparse matrices, because centering them entails building a dense  <br>matrix which in common use cases is likely to be too large to fit in  <br>memory.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True |\
|     | [with\_std with\_std: bool, default=True  <br>  <br>If True, scale the data to unit variance (or equivalently,  <br>unit standard deviation).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True |\
\
RandomForestClassifier\
\
[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |\
|     | [criterion criterion: {"gini", "entropy", "log\_loss"}, default="gini"  <br>  <br>The function to measure the quality of a split. Supported criteria are  <br>"gini" for the Gini impurity and "log\_loss" and "entropy" both for the  <br>Shannon information gain, see :ref:\`tree\_mathematical\_formulation\`.  <br>Note: This parameter is tree-specific.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'gini' |\
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |\
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |\
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1   |\
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_features max\_features: {"sqrt", "log2", None}, int or float, default="sqrt"  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>.. versionchanged:: 1.1  <br>The default of \`max\_features\` changed from \`"auto"\` to \`"sqrt"\`.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D%22sqrt%22) | 'sqrt' |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |\
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |\
|     | [bootstrap bootstrap: bool, default=True  <br>  <br>Whether bootstrap samples are used when building trees. If False, the  <br>whole dataset is used to build each tree.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | True |\
|     | [oob\_score oob\_score: bool or callable, default=False  <br>  <br>Whether to use out-of-bag samples to estimate the generalization score.  <br>By default, :func:\`~sklearn.metrics.accuracy\_score\` is used.  <br>Provide a callable with signature \`metric(y\_true, y\_pred)\` to use a  <br>custom metric. Only available if \`bootstrap=True\`.  <br>  <br>For an illustration of out-of-bag (OOB) error estimation, see the example  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_ensemble\_oob.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`predict\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |\
\
  \
  \
\
**Total running time of the script:** (0 minutes 0.129 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_pipeline_display.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_pipeline_display.ipynb)\
\
[`Download Jupyter notebook: plot_pipeline_display.ipynb`](https://scikit-learn.org/stable/_downloads/6ebaebc92484478ceb119d24fe9df21c/plot_pipeline_display.ipynb)\
\
[`Download Python source code: plot_pipeline_display.py`](https://scikit-learn.org/stable/_downloads/85d246b1849cf51d95634621ea0b7dd2/plot_pipeline_display.py)\
\
[`Download zipped: plot_pipeline_display.zip`](https://scikit-learn.org/stable/_downloads/4212c599ad39f31d06640bbe0ddf2807/plot_pipeline_display.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_estimator_representation_thumb.png)\
\
[Displaying estimators and complex pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_estimator_representation.html)\
\
Displaying estimators and complex pipelines\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)\
\
[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)\
\
Column Transformer with Mixed Types\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_set_output_thumb.png)\
\
[Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html)\
\
Introducing the set\_output API\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)\
\
Release Highlights for scikit-learn 0.23\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/85d246b1849cf51d95634621ea0b7dd2/plot_pipeline_display.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6ebaebc92484478ceb119d24fe9df21c/plot_pipeline_display.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/4212c599ad39f31d06640bbe0ddf2807/plot_pipeline_display.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_pipeline_display.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_pipeline_display.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)