[Skip to main content](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#sphx-glr-download-auto-examples-release-highlights-plot-release-highlights-1-1-0-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Release Highlights for scikit-learn 1.1[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#release-highlights-for-scikit-learn-1-1 "Link to this heading")

===============================================================================================================================================================================================================

We are pleased to announce the release of scikit-learn 1.1! Many bug fixes and improvements were added, as well as some new key features. We detail below a few of the major features of this release. **For an exhaustive list of all the changes**, please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.1.html#release-notes-1-1)
.

To install the latest version (with pip):

pip install \--upgrade scikit\-learn

Copy to clipboard

or with conda:

conda install \-c conda\-forge scikit\-learn

Copy to clipboard

Quantile loss in [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#quantile-loss-in-histgradientboostingregressor "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 can model quantiles with `loss="quantile"` and the new parameter `quantile`.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")

\# Simple regression function for X \* cos(X)
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(42)
X\_1d \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, num\=2000)
X \= X\_1d.reshape(\-1, 1)
y \= X\_1d \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(X\_1d) + rng.normal(scale\=X\_1d / 3)

quantiles \= \[0.95, 0.5, 0.05\]
parameters \= dict(loss\="quantile", max\_bins\=32, max\_iter\=50)
hist\_quantiles \= {
    f"quantile={quantile:.2f}": [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
        \*\*parameters, quantile\=quantile
    ).fit(X, y)
    for quantile in quantiles
}

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.plot(X\_1d, y, "o", alpha\=0.5, markersize\=1)
for quantile, hist in hist\_quantiles.items():
    ax.plot(X\_1d, hist.predict(X), label\=quantile)
\_ \= ax.legend(loc\="lower left")

Copy to clipboard

![plot release highlights 1 1 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_001.png)

For a usecase example, see [Features in Histogram Gradient Boosting Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_hgbt_regression.html#sphx-glr-auto-examples-ensemble-plot-hgbt-regression-py)

`get_feature_names_out` Available in all Transformers[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#get-feature-names-out-available-in-all-transformers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[get\_feature\_names\_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)
 is now available in all transformers, thereby concluding the implementation of [SLEP007](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep007/proposal.html)
. This enables [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 to construct the output feature names for more complex pipelines:

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.feature\_selection import [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
from sklearn.impute import [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(
    "titanic", version\=1, as\_frame\=True, return\_X\_y\=True, parser\="pandas"
)
numeric\_features \= \["age", "fare"\]
numeric\_transformer \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
(strategy\="median"), [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
())
categorical\_features \= \["embarked", "pclass"\]

preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        ("num", numeric\_transformer, numeric\_features),\
        (\
            "cat",\
            [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore", sparse\_output\=False),\
            categorical\_features,\
        ),\
    \],
    verbose\_feature\_names\_out\=False,
)
log\_reg \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(preprocessor, [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
(k\=7), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
())
log\_reg.fit(X, y)

Copy to clipboard

Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(transformers=\[('num',\
                                                  Pipeline(steps=\[('simpleimputer',\
                                                                   SimpleImputer(strategy='median')),\
                                                                  ('standardscaler',\
                                                                   StandardScaler())\]),\
                                                  \['age', 'fare'\]),\
                                                 ('cat',\
                                                  OneHotEncoder(handle\_unknown='ignore',\
                                                                sparse\_output=False),\
                                                  \['embarked', 'pclass'\])\],\
                                   verbose\_feature\_names\_out=False)),\
                ('selectkbest', SelectKBest(k=7)),\
                ('logisticregression', LogisticRegression())\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('selectkbest', ...), ...\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['0','1'\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](13,) | \['pclass','name','sex',...,'boat','body','home.dest'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 13  |

columntransformer: ColumnTransformer

[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('num', ...), ('cat', ...)\] |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](13,) | \['pclass','name','sex',...,'boat','body','home.dest'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 13  |
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'num': Pipel...nder': 'drop'} |
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cat': slice(2, 9, None), 'num': slice(0, 2, None), 're...er': slice(0, 0, None)} |
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('num', Pipeline(step...ardScaler())\]), \['age', 'fare'\]), ('cat', OneHotEncoder...\_output=False), \['em...ed', 'pclass'\]), ('re...er', 'drop', \['name', 'sex', 'sibsp', 'parch', ...\])\] |

num

\['age', 'fare'\]

SimpleImputer

[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'median' |
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |
|     | [fill\_value fill\_value: str or numerical value, default=None  <br>  <br>When strategy == "constant", \`fill\_value\` is used to replace all  <br>occurrences of missing\_values. For string or object data types,  <br>\`fill\_value\` must be a string.  <br>If \`None\`, \`fill\_value\` will be 0 when imputing numerical  <br>data and "missing\_value" for strings or object data types.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=fill_value,-str%20or%20numerical%20value%2C%20default%3DNone) | None |
|     | [copy copy: bool, default=True  <br>  <br>If True, a copy of X will be created. If False, imputation will  <br>be done in-place whenever possible. Note that, in the following cases,  <br>a new copy will always be made, even if \`copy=False\`:  <br>  <br>\- If \`X\` is not an array of floating values;  <br>\- If \`X\` is encoded as a CSR matrix;  <br>\- If \`add\_indicator=True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [add\_indicator add\_indicator: bool, default=False  <br>  <br>If True, a :class:\`MissingIndicator\` transform will stack onto output  <br>of the imputer's transform. This allows a predictive estimator  <br>to account for missingness despite imputation. If a feature has no  <br>missing values at fit/train time, the feature won't appear on  <br>the missing indicator even if there are missing values at  <br>transform/test time.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=add_indicator,-bool%2C%20default%3DFalse) | False |
|     | [keep\_empty\_features keep\_empty\_features: bool, default=False  <br>  <br>If True, features that consist exclusively of missing values when  <br>\`fit\` is called are returned in results when \`transform\` is called.  <br>The imputed value is always \`0\` except when \`strategy="constant"\`  <br>in which case \`fill\_value\` will be used instead.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=keep_empty_features,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['age','fare'\] |
| [indicator\_ indicator\_: :class:\`~sklearn.impute.MissingIndicator\`  <br>  <br>Indicator used to add binary indicators for missing values.  <br>\`None\` if \`add\_indicator=False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=indicator_,-%3Aclass%3A~sklearn.impute.MissingIndicator) | NoneType | None |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=n_features_in_,-int) | int | 2   |
| [statistics\_ statistics\_: array of shape (n\_features,)  <br>  <br>The imputation fill value for each feature.  <br>Computing statistics can result in \`np.nan\` values.  <br>During :meth:\`transform\`, features corresponding to \`np.nan\`  <br>statistics will be discarded.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=statistics_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](2,) | \[28. ,14.45\] |

2 features

|     |
| --- |
| age |
| fare |

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
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[29.5 ,33.28\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1309 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[12.9 ,51.72\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[ 166.42,2675.14\] |

2 features

|     |
| --- |
| x0  |
| x1  |

cat

\['embarked', 'pclass'\]

OneHotEncoder

[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['C', '... dtype=object), array(\[1, 2, 3\])\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['embarked','pclass'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 2   |\
\
7 features\
\
|     |\
| --- |\
| embarked\_C |\
| embarked\_Q |\
| embarked\_S |\
| embarked\_nan |\
| pclass\_1 |\
| pclass\_2 |\
| pclass\_3 |\
\
9 features\
\
|     |\
| --- |\
| age |\
| fare |\
| embarked\_C |\
| embarked\_Q |\
| embarked\_S |\
| embarked\_nan |\
| pclass\_1 |\
| pclass\_2 |\
| pclass\_3 |\
\
SelectKBest\
\
[?Documentation for SelectKBest](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [k k: int or "all", default=10  <br>  <br>Number of top features to select.  <br>The "all" option bypasses selection, for use in a parameter search.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=k,-int%20or%20%22all%22%2C%20default%3D10) | 7   |\
|     | [score\_func score\_func: callable, default=f\_classif  <br>  <br>Function taking two arrays X and y, and returning a pair of arrays  <br>(scores, pvalues) or a single array with scores.  <br>Default is f\_classif (see below "See Also"). The default function only  <br>works with classification tasks.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=score_func,-callable%2C%20default%3Df_classif) | <function f\_c...x7e1df6819170> |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=n_features_in_,-int) | int | 9   |\
| [pvalues\_ pvalues\_: array-like of shape (n\_features,)  <br>  <br>p-values of feature scores, None if \`score\_func\` returned only scores.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=pvalues_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](9,) | \[0.11,0. ,0. ,...,0. ,0.07,0. \] |\
| [scores\_ scores\_: array-like of shape (n\_features,)  <br>  <br>Scores of features.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectKBest.html#:~:text=scores_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](9,) | \[ 2.51, 83.04, 44.84,...,110.71, 3.38,114.16\] |\
\
7 features\
\
|     |\
| --- |\
| x1  |\
| x2  |\
| x4  |\
| x5  |\
| x6  |\
| x7  |\
| x8  |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
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
|     | [max\_iter max\_iter: int, default=100  <br>  <br>Maximum number of iterations taken for the solvers to converge.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100 |\
|     | [verbose verbose: int, default=0  <br>  <br>For the liblinear and lbfgs solvers set verbose to any positive  <br>number for verbosity.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to True, reuse the solution of the previous call to fit as  <br>initialization, otherwise, just erase the previous solution.  <br>Useless for liblinear solver. See :term:\`the Glossary <warm\_start>\`.  <br>  <br>.. versionadded:: 0.17  <br>\*warm\_start\* to support \*lbfgs\*, \*newton-cg\*, \*sag\*, \*saga\* solvers.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Does not have any effect.  <br>  <br>.. deprecated:: 1.8  <br>\`n\_jobs\` is deprecated in version 1.8 and will be removed in 1.10.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes, )  <br>  <br>A list of class labels known to the classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%20%29) | ndarray\[object\](2,) | \['0','1'\] |\
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 7) | \[\[ 0.25, 0.01,-0.59,..., 0.49, 0.2 ,-0.66\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[0.09\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 7   |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[20\] |\
\
  \
  \
\
Here we slice the pipeline to include all the steps but the last one. The output feature names of this pipeline slice are the features put into logistic regression. These names correspond directly to the coefficients in the logistic regression:\
\
import pandas as pd\
\
log\_reg\_input\_features \= log\_reg\[:\-1\].get\_feature\_names\_out()\
[pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")\
(log\_reg\[\-1\].coef\_.ravel(), index\=log\_reg\_input\_features).plot.bar()\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![plot release highlights 1 1 0](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_002.png)\
\
Grouping infrequent categories in [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#grouping-infrequent-categories-in-onehotencoder "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
 supports aggregating infrequent categories into a single output for each feature. The parameters to enable the gathering of infrequent categories are `min_frequency` and `max_categories`. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#encoder-infrequent-categories)\
 for more details.\
\
import numpy as np\
\
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
\
X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\
    \[\["dog"\] \* 5 + \["cat"\] \* 20 + \["rabbit"\] \* 10 + \["snake"\] \* 3\], dtype\=object\
).T\
enc \= [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(min\_frequency\=6, sparse\_output\=False).fit(X)\
enc.infrequent\_categories\_\
\
Copy to clipboard\
\
\[array(\['dog', 'snake'\], dtype=object)\]\
\
Copy to clipboard\
\
Since dog and snake are infrequent categories, they are grouped together when transformed:\
\
encoded \= enc.transform([np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\[\["dog"\], \["snake"\], \["cat"\], \["rabbit"\]\]))\
[pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(encoded, columns\=enc.get\_feature\_names\_out())\
\
Copy to clipboard\
\
|     | x0\_cat | x0\_rabbit | x0\_infrequent\_sklearn |\
| --- | --- | --- | --- |\
| 0   | 0.0 | 0.0 | 1.0 |\
| 1   | 0.0 | 0.0 | 1.0 |\
| 2   | 1.0 | 0.0 | 0.0 |\
| 3   | 0.0 | 1.0 | 0.0 |\
\
  \
  \
\
Performance improvements[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#performance-improvements "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Reductions on pairwise distances for dense float64 datasets has been refactored to better take advantage of non-blocking thread parallelism. For example, [`neighbors.NearestNeighbors.kneighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.kneighbors "sklearn.neighbors.NearestNeighbors.kneighbors")\
 and [`neighbors.NearestNeighbors.radius_neighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors.radius_neighbors "sklearn.neighbors.NearestNeighbors.radius_neighbors")\
 can respectively be up to ×20 and ×5 faster than previously. In summary, the following functions and estimators now benefit from improved performance:\
\
*   [`metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")\
    \
*   [`metrics.pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")\
    \
*   [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")\
    \
*   [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")\
    \
*   [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")\
    \
*   [`cluster.OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")\
    \
*   [`cluster.SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")\
    \
*   [`feature_selection.mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")\
    \
*   [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")\
    \
*   [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")\
    \
*   [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")\
    \
*   [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")\
    \
*   [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")\
    \
*   [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")\
    \
*   [`manifold.Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")\
    \
*   [`manifold.LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")\
    \
*   [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")\
    \
*   [`manifold.trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")\
    \
*   [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")\
    \
*   [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")\
    \
\
To know more about the technical details of this work, you can read [this suite of blog posts](https://blog.scikit-learn.org/technical/performances/)\
.\
\
Moreover, the computation of loss functions has been refactored using Cython resulting in performance improvements for the following estimators:\
\
*   [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
    \
*   [`linear_model.GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")\
    \
*   [`linear_model.PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor")\
    \
*   [`linear_model.TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor")\
    \
\
[`MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")\
: an online version of NMF[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#minibatchnmf-an-online-version-of-nmf "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The new class [`MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")\
 implements a faster but less accurate version of non-negative matrix factorization ([`NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")\
). [`MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")\
 divides the data into mini-batches and optimizes the NMF model in an online manner by cycling over the mini-batches, making it better suited for large datasets. In particular, it implements `partial_fit`, which can be used for online learning when the data is not readily available from the start, or when the data does not fit into memory.\
\
import numpy as np\
\
from sklearn.decomposition import [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")\
\
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")\
(0)\
n\_samples, n\_features, n\_components \= 10, 10, 5\
true\_W \= rng.uniform(size\=(n\_samples, n\_components))\
true\_H \= rng.uniform(size\=(n\_components, n\_features))\
X \= true\_W @ true\_H\
\
nmf \= [MiniBatchNMF](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")\
(n\_components\=n\_components, random\_state\=0)\
\
for \_ in range(10):\
    nmf.partial\_fit(X)\
\
W \= nmf.transform(X)\
H \= nmf.components\_\
X\_reconstructed \= W @ H\
\
print(\
    "relative reconstruction error: ",\
    f"{[np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")\
((X \- X\_reconstructed) \*\* 2) / [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")\
(X\*\*2):.5f}",\
)\
\
Copy to clipboard\
\
relative reconstruction error:  0.00364\
\
Copy to clipboard\
\
[`BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")\
: divide and cluster[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#bisectingkmeans-divide-and-cluster "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The new class [`BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")\
 is a variant of [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")\
, using divisive hierarchical clustering. Instead of creating all centroids at once, centroids are picked progressively based on a previous clustering: a cluster is split into two new clusters repeatedly until the target number of clusters is reached, giving a hierarchical structure to the clustering.\
\
import matplotlib.pyplot as plt\
\
from sklearn.cluster import [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")\
, [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")\
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
\
X, \_ \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")\
(n\_samples\=1000, centers\=2, random\_state\=0)\
\
km \= [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")\
(n\_clusters\=5, random\_state\=0, n\_init\="auto").fit(X)\
bisect\_km \= [BisectingKMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")\
(n\_clusters\=5, random\_state\=0).fit(X)\
\
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(1, 2, figsize\=(10, 5))\
ax\[0\].scatter(X\[:, 0\], X\[:, 1\], s\=10, c\=km.labels\_)\
ax\[0\].scatter(km.cluster\_centers\_\[:, 0\], km.cluster\_centers\_\[:, 1\], s\=20, c\="r")\
ax\[0\].set\_title("KMeans")\
\
ax\[1\].scatter(X\[:, 0\], X\[:, 1\], s\=10, c\=bisect\_km.labels\_)\
ax\[1\].scatter(\
    bisect\_km.cluster\_centers\_\[:, 0\], bisect\_km.cluster\_centers\_\[:, 1\], s\=20, c\="r"\
)\
\_ \= ax\[1\].set\_title("BisectingKMeans")\
\
Copy to clipboard\
\
![KMeans, BisectingKMeans](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_003.png)\
\
**Total running time of the script:** (0 minutes 0.789 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_1_0.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_1_0.ipynb)\
\
[`Download Jupyter notebook: plot_release_highlights_1_1_0.ipynb`](https://scikit-learn.org/stable/_downloads/68fdea23e50d165632d4bd4e36453cd5/plot_release_highlights_1_1_0.ipynb)\
\
[`Download Python source code: plot_release_highlights_1_1_0.py`](https://scikit-learn.org/stable/_downloads/4cf0456267ced0f869a458ef4776d4c5/plot_release_highlights_1_1_0.py)\
\
[`Download zipped: plot_release_highlights_1_1_0.zip`](https://scikit-learn.org/stable/_downloads/a4ca19d099be76c1c7cbb53108c7b00b/plot_release_highlights_1_1_0.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_0_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html)\
\
Release Highlights for scikit-learn 1.0\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_3_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.3](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_3_0.html)\
\
Release Highlights for scikit-learn 1.3\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)\
\
Release Highlights for scikit-learn 0.23\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)\
\
Release Highlights for scikit-learn 1.2\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/4cf0456267ced0f869a458ef4776d4c5/plot_release_highlights_1_1_0.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/68fdea23e50d165632d4bd4e36453cd5/plot_release_highlights_1_1_0.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/a4ca19d099be76c1c7cbb53108c7b00b/plot_release_highlights_1_1_0.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo29.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_1_0.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo29.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/release_highlights/plot_release_highlights_1_1_0.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)