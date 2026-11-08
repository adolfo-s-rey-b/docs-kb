[Skip to main content](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/inspection/plot_permutation_importance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/inspection/plot_permutation_importance.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/inspection/plot_permutation_importance.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/inspection/plot_permutation_importance.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/inspection/plot_permutation_importance.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/inspection/plot_permutation_importance.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-download-auto-examples-inspection-plot-permutation-importance-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Permutation Importance vs Random Forest Feature Importance (MDI)[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#permutation-importance-vs-random-forest-feature-importance-mdi "Link to this heading")

=====================================================================================================================================================================================================================================================

In this example, we will compare the impurity-based feature importance of [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 with the permutation importance on the titanic dataset using [`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
. We will show that the impurity-based feature importance can inflate the importance of numerical features.

Furthermore, the impurity-based feature importance of random forests suffers from being computed on statistics derived from the training dataset: the importances can be high even for features that are not predictive of the target variable, as long as the model has the capacity to use them to overfit.

This example shows how to use Permutation Importances as an alternative that can mitigate those limitations.

References

*   [L. Breiman, “Random Forests”, Machine Learning, 45(1), 5-32, 2001.](https://doi.org/10.1023/A:1010933404324)
    

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Data Loading and Feature Engineering[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#data-loading-and-feature-engineering "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s use pandas to load a copy of the titanic dataset. The following shows how to apply separate preprocessing on numerical and categorical features.

We further include two random variables that are not correlated in any way with the target variable (`survived`):

*   `random_num` is a high cardinality numerical variable (as many unique values as records).
    
*   `random_cat` is a low cardinality categorical variable (3 possible values).
    

import numpy as np

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("titanic", version\=1, as\_frame\=True, return\_X\_y\=True)
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(seed\=42)
X\["random\_cat"\] \= rng.randint(3, size\=X.shape\[0\])
X\["random\_num"\] \= rng.randn(X.shape\[0\])

categorical\_columns \= \["pclass", "sex", "embarked", "random\_cat"\]
numerical\_columns \= \["age", "sibsp", "parch", "fare", "random\_num"\]

X \= X\[categorical\_columns + numerical\_columns\]
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=42)

Copy to clipboard

We define a predictive model based on a random forest. Therefore, we will make the following preprocessing steps:

*   use [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     to encode the categorical features;
    
*   use [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     to fill missing values for numerical features using a mean strategy.
    

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.impute import [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

categorical\_encoder \= [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
(
    handle\_unknown\="use\_encoded\_value", unknown\_value\=-1, encoded\_missing\_value\=-1
)
numerical\_pipe \= [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
(strategy\="mean")

preprocessing \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        ("cat", categorical\_encoder, categorical\_columns),\
        ("num", numerical\_pipe, numerical\_columns),\
    \],
    verbose\_feature\_names\_out\=False,
)

rf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("preprocess", preprocessing),\
        ("classifier", [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")\
(random\_state\=42)),\
    \]
)
rf.fit(X\_train, y\_train)

Copy to clipboard

Pipeline(steps=\[('preprocess',\
                 ColumnTransformer(transformers=\[('cat',\
                                                  OrdinalEncoder(encoded\_missing\_value=-1,\
                                                                 handle\_unknown='use\_encoded\_value',\
                                                                 unknown\_value=-1),\
                                                  \['pclass', 'sex', 'embarked',\
                                                   'random\_cat'\]),\
                                                 ('num', SimpleImputer(),\
                                                  \['age', 'sibsp', 'parch',\
                                                   'fare', 'random\_num'\])\],\
                                   verbose\_feature\_names\_out=False)),\
                ('classifier', RandomForestClassifier(random\_state=42))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('preprocess', ...), ('classifier', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['0','1'\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](9,) | \['pclass','sex','embarked',...,'parch','fare','random\_num'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 9   |

preprocess: ColumnTransformer

[?Documentation for preprocess: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('cat', ...), ('num', ...)\] |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](9,) | \['pclass','sex','embarked',...,'parch','fare','random\_num'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 9   |
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'cat': Ordin...mpleImputer()} |
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cat': slice(0, 4, None), 'num': slice(4, 9, None), 're...er': slice(0, 0, None)} |
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('cat', OrdinalEncode...nown\_value=-1), \['pclass', 'sex', 'em...ed', 'ra...at'\]), ('num', SimpleImputer(), \['age', 'sibsp', 'parch', 'fare', ...\])\] |

cat

\['pclass', 'sex', 'embarked', 'random\_cat'\]

OrdinalEncoder

[?Documentation for OrdinalEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [handle\_unknown handle\_unknown: {'error', 'use\_encoded\_value'}, default='error'  <br>  <br>When set to 'error' an error will be raised in case an unknown  <br>categorical feature is present during transform. When set to  <br>'use\_encoded\_value', the encoded value of unknown categories will be  <br>set to the value given for the parameter \`unknown\_value\`. In  <br>:meth:\`inverse\_transform\`, an unknown category will be denoted as None.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27use_encoded_value%27%7D%2C%20default%3D%27error%27) | 'use\_encoded\_value' |
|     | [unknown\_value unknown\_value: int or np.nan, default=None  <br>  <br>When the parameter handle\_unknown is set to 'use\_encoded\_value', this  <br>parameter is required and will set the encoded value of unknown  <br>categories. It has to be distinct from the values used to encode any of  <br>the categories in \`fit\`. If set to np.nan, the \`dtype\` parameter must  <br>be a float dtype.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=unknown_value,-int%20or%20np.nan%2C%20default%3DNone) | \-1 |
|     | [encoded\_missing\_value encoded\_missing\_value: int or np.nan, default=np.nan  <br>  <br>Encoded value of missing categories. If set to \`np.nan\`, then the \`dtype\`  <br>parameter must be a float dtype.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=encoded_missing_value,-int%20or%20np.nan%2C%20default%3Dnp.nan) | \-1 |
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values, and should be sorted in case of numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output categories for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>\`max\_categories\` do \*\*not\*\* take into account missing or unknown  <br>categories. Setting \`unknown\_value\` or \`encoded\_missing\_value\` to an  <br>integer will increase the number of unique integer codes by one each.  <br>This can result in up to \`max\_categories + 2\` integer codes.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during \`\`fit\`\` (in order of  <br>the features in X and corresponding with the output of \`\`transform\`\`).  <br>This does not include categories that weren't seen during \`\`fit\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\[1, 2, 3\]), array(\['femal... dtype=object), array(\['C', '... dtype=object), array(\[0, 1, 2\])\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['pclass','sex','embarked','random\_cat'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
4 features\
\
|     |\
| --- |\
| pclass |\
| sex |\
| embarked |\
| random\_cat |\
\
num\
\
\['age', 'sibsp', 'parch', 'fare', 'random\_num'\]\
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
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['age','sibsp','parch','fare','random\_num'\] |\
| [indicator\_ indicator\_: :class:\`~sklearn.impute.MissingIndicator\`  <br>  <br>Indicator used to add binary indicators for missing values.  <br>\`None\` if \`add\_indicator=False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=indicator_,-%3Aclass%3A~sklearn.impute.MissingIndicator) | NoneType | None |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=n_features_in_,-int) | int | 5   |\
| [statistics\_ statistics\_: array of shape (n\_features,)  <br>  <br>The imputation fill value for each feature.  <br>Computing statistics can result in \`np.nan\` values.  <br>During :meth:\`transform\`, features corresponding to \`np.nan\`  <br>statistics will be discarded.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=statistics_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[29.96, 0.48, 0.39,32.54, 0.07\] |\
\
5 features\
\
|     |\
| --- |\
| age |\
| sibsp |\
| parch |\
| fare |\
| random\_num |\
\
9 features\
\
|     |\
| --- |\
| pclass |\
| sex |\
| embarked |\
| random\_cat |\
| age |\
| sibsp |\
| parch |\
| fare |\
| random\_num |\
\
RandomForestClassifier\
\
[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |\
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
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,) or a list of such arrays  <br>  <br>The classes labels (single output problem), or a list of arrays of  <br>class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20a%20list%20of%20such%20arrays) | ndarray\[object\](2,) | \['0','1'\] |\
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeClassifier\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeClassifier) | DecisionTreeClassifier | DecisionTreeClassifier() |\
| [estimators\_ estimators\_: list of DecisionTreeClassifier  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_,-list%20of%20DecisionTreeClassifier) | list | \[DecisionTreeC...te=1608637542), DecisionTreeC...te=1273642419), DecisionTreeC...te=1935803228), DecisionTreeC...ate=787846414), ...\] |\
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[475, ..., dtype=int32), array(\[686, 6..., dtype=int32), array(\[342, 4..., dtype=int32), array(\[800, 5..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](9,) | \[0.07,0.23,0.03,...,0.03,0.19,0.19\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 2   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 9   |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
Accuracy of the Model[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#accuracy-of-the-model "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Before inspecting the feature importances, it is important to check that the model predictive performance is high enough. Indeed, there would be little interest in inspecting the important features of a non-predictive model.\
\
print(f"RF train accuracy: {rf.score(X\_train, y\_train):.3f}")\
print(f"RF test accuracy: {rf.score(X\_test, y\_test):.3f}")\
\
Copy to clipboard\
\
RF train accuracy: 1.000\
RF test accuracy: 0.814\
\
Copy to clipboard\
\
Here, one can observe that the train accuracy is very high (the forest model has enough capacity to completely memorize the training set) but it can still generalize well enough to the test set thanks to the built-in bagging of random forests.\
\
It might be possible to trade some accuracy on the training set for a slightly better accuracy on the test set by limiting the capacity of the trees (for instance by setting `min_samples_leaf=5` or `min_samples_leaf=10`) so as to limit overfitting while not introducing too much underfitting.\
\
However, let us keep our high capacity random forest model for now so that we can illustrate some pitfalls about feature importance on variables with many unique values.\
\
Tree’s Feature Importance from Mean Decrease in Impurity (MDI)[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#tree-s-feature-importance-from-mean-decrease-in-impurity-mdi "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The impurity-based feature importance ranks the numerical features to be the most important features. As a result, the non-predictive `random_num` variable is ranked as one of the most important features!\
\
This problem stems from two limitations of impurity-based feature importances:\
\
*   impurity-based importances are biased towards high cardinality features;\
    \
*   impurity-based importances are computed on training set statistics and therefore do not reflect the ability of feature to be useful to make predictions that generalize to the test set (when the model has enough capacity).\
    \
\
The bias towards high cardinality features explains why the `random_num` has a really large importance in comparison with `random_cat` while we would expect that both random features have a null importance.\
\
The fact that we use training set statistics explains why both the `random_num` and `random_cat` features have a non-null importance.\
\
import pandas as pd\
\
feature\_names \= rf\[:\-1\].get\_feature\_names\_out()\
\
mdi\_importances \= [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "pandas.Series")\
(\
    rf\[\-1\].feature\_importances\_, index\=feature\_names\
).sort\_values(ascending\=True)\
\
Copy to clipboard\
\
ax \= mdi\_importances.plot.barh()\
ax.set\_title("Random Forest Feature Importances (MDI)")\
ax.figure.tight\_layout()\
\
Copy to clipboard\
\
![Random Forest Feature Importances (MDI)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_001.png)\
\
As an alternative, the permutation importances of `rf` are computed on a held out test set. This shows that the low cardinality categorical feature, `sex` and `pclass` are the most important features. Indeed, permuting the values of these features will lead to the most decrease in accuracy score of the model on the test set.\
\
Also, note that both random features have very low importances (close to 0) as expected.\
\
import matplotlib\
import matplotlib.pyplot as plt\
\
from sklearn.inspection import [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
from sklearn.utils.fixes import parse\_version\
\
\# \`pandas.DataFrame.plot.box\` forwards its \`vert\` and \`labels\` arguments to matplotlib.\
\# These arguments are deprecated and removed in version 3.11 and 3.9, respectively. We\
\# therefore draw the horizontal boxplots directly with matplotlib in a way that is\
\# compatible with the matplotlib versions we support. As a user you probably can write\
\# simpler code by using \`pandas.DataFrame.plot.box\` directly with the appropriate\
\# arguments.\
tick\_labels\_parameter\_name \= (\
    "tick\_labels"\
    if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.9")\
    else "labels"\
)\
orientation\_dict \= (\
    {"orientation": "horizontal"}\
    if parse\_version(matplotlib.\_\_version\_\_) \>= parse\_version("3.10")\
    else {"vert": False}\
)\
\
def plot\_importances\_box(importances, title):\
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
()\
    ax.boxplot(\
        importances.values,\
        whis\=10,\
        \*\*orientation\_dict,\
        \*\*{tick\_labels\_parameter\_name: importances.columns},\
    )\
    ax.set\_title(title)\
    ax.axvline(x\=0, color\="k", linestyle\="--")\
    ax.set\_xlabel("Decrease in accuracy score")\
    fig.tight\_layout()\
    return ax\
\
result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
(\
    rf, X\_test, y\_test, n\_repeats\=10, random\_state\=42, n\_jobs\=2\
)\
\
sorted\_importances\_idx \= result.importances\_mean.argsort()\
importances \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    result.importances\[sorted\_importances\_idx\].T,\
    columns\=X.columns\[sorted\_importances\_idx\],\
)\
plot\_importances\_box(importances, "Permutation Importances (test set)")\
\
Copy to clipboard\
\
![Permutation Importances (test set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_002.png)\
\
<Axes: title={'center': 'Permutation Importances (test set)'}, xlabel='Decrease in accuracy score'>\
\
Copy to clipboard\
\
It is also possible to compute the permutation importances on the training set. This reveals that `random_num` and `random_cat` get a significantly higher importance ranking than when computed on the test set. The difference between those two plots is a confirmation that the RF model has enough capacity to use that random numerical and categorical features to overfit.\
\
result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
(\
    rf, X\_train, y\_train, n\_repeats\=10, random\_state\=42, n\_jobs\=2\
)\
\
sorted\_importances\_idx \= result.importances\_mean.argsort()\
importances \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    result.importances\[sorted\_importances\_idx\].T,\
    columns\=X.columns\[sorted\_importances\_idx\],\
)\
plot\_importances\_box(importances, "Permutation Importances (train set)")\
\
Copy to clipboard\
\
![Permutation Importances (train set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_003.png)\
\
<Axes: title={'center': 'Permutation Importances (train set)'}, xlabel='Decrease in accuracy score'>\
\
Copy to clipboard\
\
We can further retry the experiment by limiting the capacity of the trees to overfit by setting `min_samples_leaf` at 20 data points.\
\
rf.set\_params(classifier\_\_min\_samples\_leaf\=20).fit(X\_train, y\_train)\
\
Copy to clipboard\
\
Pipeline(steps=\[('preprocess',\
                 ColumnTransformer(transformers=\[('cat',\
                                                  OrdinalEncoder(encoded\_missing\_value=-1,\
                                                                 handle\_unknown='use\_encoded\_value',\
                                                                 unknown\_value=-1),\
                                                  \['pclass', 'sex', 'embarked',\
                                                   'random\_cat'\]),\
                                                 ('num', SimpleImputer(),\
                                                  \['age', 'sibsp', 'parch',\
                                                   'fare', 'random\_num'\])\],\
                                   verbose\_feature\_names\_out=False)),\
                ('classifier',\
                 RandomForestClassifier(min\_samples\_leaf=20, random\_state=42))\])\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
Pipeline\
\
[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('preprocess', ...), ('classifier', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['0','1'\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](9,) | \['pclass','sex','embarked',...,'parch','fare','random\_num'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 9   |\
\
preprocess: ColumnTransformer\
\
[?Documentation for preprocess: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('cat', ...), ('num', ...)\] |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](9,) | \['pclass','sex','embarked',...,'parch','fare','random\_num'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 9   |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'cat': Ordin...mpleImputer()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cat': slice(0, 4, None), 'num': slice(4, 9, None), 're...er': slice(0, 0, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('cat', OrdinalEncode...nown\_value=-1), \['pclass', 'sex', 'em...ed', 'ra...at'\]), ('num', SimpleImputer(), \['age', 'sibsp', 'parch', 'fare', ...\])\] |\
\
cat\
\
\['pclass', 'sex', 'embarked', 'random\_cat'\]\
\
OrdinalEncoder\
\
[?Documentation for OrdinalEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [handle\_unknown handle\_unknown: {'error', 'use\_encoded\_value'}, default='error'  <br>  <br>When set to 'error' an error will be raised in case an unknown  <br>categorical feature is present during transform. When set to  <br>'use\_encoded\_value', the encoded value of unknown categories will be  <br>set to the value given for the parameter \`unknown\_value\`. In  <br>:meth:\`inverse\_transform\`, an unknown category will be denoted as None.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27use_encoded_value%27%7D%2C%20default%3D%27error%27) | 'use\_encoded\_value' |\
|     | [unknown\_value unknown\_value: int or np.nan, default=None  <br>  <br>When the parameter handle\_unknown is set to 'use\_encoded\_value', this  <br>parameter is required and will set the encoded value of unknown  <br>categories. It has to be distinct from the values used to encode any of  <br>the categories in \`fit\`. If set to np.nan, the \`dtype\` parameter must  <br>be a float dtype.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=unknown_value,-int%20or%20np.nan%2C%20default%3DNone) | \-1 |\
|     | [encoded\_missing\_value encoded\_missing\_value: int or np.nan, default=np.nan  <br>  <br>Encoded value of missing categories. If set to \`np.nan\`, then the \`dtype\`  <br>parameter must be a float dtype.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=encoded_missing_value,-int%20or%20np.nan%2C%20default%3Dnp.nan) | \-1 |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values, and should be sorted in case of numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output categories for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>\`max\_categories\` do \*\*not\*\* take into account missing or unknown  <br>categories. Setting \`unknown\_value\` or \`encoded\_missing\_value\` to an  <br>integer will increase the number of unique integer codes by one each.  <br>This can result in up to \`max\_categories + 2\` integer codes.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during \`\`fit\`\` (in order of  <br>the features in X and corresponding with the output of \`\`transform\`\`).  <br>This does not include categories that weren't seen during \`\`fit\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\[1, 2, 3\]), array(\['femal... dtype=object), array(\['C', '... dtype=object), array(\[0, 1, 2\])\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](4,) | \['pclass','sex','embarked','random\_cat'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=n_features_in_,-int) | int | 4   |\
\
4 features\
\
|     |\
| --- |\
| pclass |\
| sex |\
| embarked |\
| random\_cat |\
\
num\
\
\['age', 'sibsp', 'parch', 'fare', 'random\_num'\]\
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
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['age','sibsp','parch','fare','random\_num'\] |\
| [indicator\_ indicator\_: :class:\`~sklearn.impute.MissingIndicator\`  <br>  <br>Indicator used to add binary indicators for missing values.  <br>\`None\` if \`add\_indicator=False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=indicator_,-%3Aclass%3A~sklearn.impute.MissingIndicator) | NoneType | None |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=n_features_in_,-int) | int | 5   |\
| [statistics\_ statistics\_: array of shape (n\_features,)  <br>  <br>The imputation fill value for each feature.  <br>Computing statistics can result in \`np.nan\` values.  <br>During :meth:\`transform\`, features corresponding to \`np.nan\`  <br>statistics will be discarded.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=statistics_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](5,) | \[29.96, 0.48, 0.39,32.54, 0.07\] |\
\
5 features\
\
|     |\
| --- |\
| age |\
| sibsp |\
| parch |\
| fare |\
| random\_num |\
\
9 features\
\
|     |\
| --- |\
| pclass |\
| sex |\
| embarked |\
| random\_cat |\
| age |\
| sibsp |\
| parch |\
| fare |\
| random\_num |\
\
RandomForestClassifier\
\
[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [min\_samples\_leaf min\_samples\_leaf: int or float, default=1  <br>  <br>The minimum number of samples required to be at a leaf node.  <br>A split point at any depth will only be considered if it leaves at  <br>least \`\`min\_samples\_leaf\`\` training samples in each of the left and  <br>right branches. This may have the effect of smoothing the model,  <br>especially in regression.  <br>  <br>\- If int, then consider \`min\_samples\_leaf\` as the minimum number.  <br>\- If float, then \`min\_samples\_leaf\` is a fraction and  <br>\`ceil(min\_samples\_leaf \* n\_samples)\` are the minimum  <br>number of samples for each node.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 20  |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Controls both the randomness of the bootstrapping of the samples used  <br>when building trees (if \`\`bootstrap=True\`\`) and the sampling of the  <br>features to consider when looking for the best split at each node  <br>(if \`\`max\_features < n\_features\`\`).  <br>See :term:\`Glossary <random\_state>\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 42  |\
|     | [n\_estimators n\_estimators: int, default=100  <br>  <br>The number of trees in the forest.  <br>  <br>.. versionchanged:: 0.22  <br>The default value of \`\`n\_estimators\`\` changed from 10 to 100  <br>in 0.22.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100 |\
|     | [criterion criterion: {"gini", "entropy", "log\_loss"}, default="gini"  <br>  <br>The function to measure the quality of a split. Supported criteria are  <br>"gini" for the Gini impurity and "log\_loss" and "entropy" both for the  <br>Shannon information gain, see :ref:\`tree\_mathematical\_formulation\`.  <br>Note: This parameter is tree-specific.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'gini' |\
|     | [max\_depth max\_depth: int, default=None  <br>  <br>The maximum depth of the tree. If None, then nodes are expanded until  <br>all leaves are pure or until all leaves contain less than  <br>min\_samples\_split samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None |\
|     | [min\_samples\_split min\_samples\_split: int or float, default=2  <br>  <br>The minimum number of samples required to split an internal node:  <br>  <br>\- If int, then consider \`min\_samples\_split\` as the minimum number.  <br>\- If float, then \`min\_samples\_split\` is a fraction and  <br>\`ceil(min\_samples\_split \* n\_samples)\` are the minimum  <br>number of samples for each split.  <br>  <br>.. versionchanged:: 0.18  <br>Added float values for fractions.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2   |\
|     | [min\_weight\_fraction\_leaf min\_weight\_fraction\_leaf: float, default=0.0  <br>  <br>The minimum weighted fraction of the sum total of weights (of all  <br>the input samples) required to be at a leaf node. Samples have  <br>equal weight when sample\_weight is not provided.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_features max\_features: {"sqrt", "log2", None}, int or float, default="sqrt"  <br>  <br>The number of features to consider when looking for the best split:  <br>  <br>\- If int, then consider \`max\_features\` features at each split.  <br>\- If float, then \`max\_features\` is a fraction and  <br>\`max(1, int(max\_features \* n\_features\_in\_))\` features are considered at each  <br>split.  <br>\- If "sqrt", then \`max\_features=sqrt(n\_features)\`.  <br>\- If "log2", then \`max\_features=log2(n\_features)\`.  <br>\- If None, then \`max\_features=n\_features\`.  <br>  <br>.. versionchanged:: 1.1  <br>The default of \`max\_features\` changed from \`"auto"\` to \`"sqrt"\`.  <br>  <br>Note: the search for a split does not stop until at least one  <br>valid partition of the node samples is found, even if it requires to  <br>effectively inspect more than \`\`max\_features\`\` features.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D%22sqrt%22) | 'sqrt' |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int, default=None  <br>  <br>Grow trees with \`\`max\_leaf\_nodes\`\` in best-first fashion.  <br>Best nodes are defined as relative reduction in impurity.  <br>If None then unlimited number of leaf nodes.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None |\
|     | [min\_impurity\_decrease min\_impurity\_decrease: float, default=0.0  <br>  <br>A node will be split if this split induces a decrease of the impurity  <br>greater than or equal to this value.  <br>  <br>The weighted impurity decrease equation is the following::  <br>  <br>N\_t / N \* (impurity - N\_t\_R / N\_t \* right\_impurity  <br>\- N\_t\_L / N\_t \* left\_impurity)  <br>  <br>where \`\`N\`\` is the total number of samples, \`\`N\_t\`\` is the number of  <br>samples at the current node, \`\`N\_t\_L\`\` is the number of samples in the  <br>left child, and \`\`N\_t\_R\`\` is the number of samples in the right child.  <br>  <br>\`\`N\`\`, \`\`N\_t\`\`, \`\`N\_t\_R\`\` and \`\`N\_t\_L\`\` all refer to the weighted sum,  <br>if \`\`sample\_weight\`\` is passed.  <br>  <br>.. versionadded:: 0.19](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0 |\
|     | [bootstrap bootstrap: bool, default=True  <br>  <br>Whether bootstrap samples are used when building trees. If False, the  <br>whole dataset is used to build each tree.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | True |\
|     | [oob\_score oob\_score: bool or callable, default=False  <br>  <br>Whether to use out-of-bag samples to estimate the generalization score.  <br>By default, :func:\`~sklearn.metrics.accuracy\_score\` is used.  <br>Provide a callable with signature \`metric(y\_true, y\_pred)\` to use a  <br>custom metric. Only available if \`bootstrap=True\`.  <br>  <br>For an illustration of out-of-bag (OOB) error estimation, see the example  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_ensemble\_oob.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>The number of jobs to run in parallel. :meth:\`fit\`, :meth:\`predict\`,  <br>:meth:\`decision\_path\` and :meth:\`apply\` are all parallelized over the  <br>trees. \`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\`  <br>context. \`\`-1\`\` means using all processors. See :term:\`Glossary  <br><n\_jobs>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default=0  <br>  <br>Controls the verbosity when fitting and predicting.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble, otherwise, just fit a whole  <br>new forest. See :term:\`Glossary <warm\_start>\` and  <br>:ref:\`tree\_ensemble\_warm\_start\` for details.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [class\_weight class\_weight: {"balanced", "balanced\_subsample"}, dict or list of dicts, default=None  <br>  <br>Weights associated with classes in the form \`\`{class\_label: weight}\`\`.  <br>If not given, all classes are supposed to have weight one. For  <br>multi-output problems, a list of dicts can be provided in the same  <br>order as the columns of y.  <br>  <br>Note that for multioutput (including multilabel) weights should be  <br>defined for each class of every column in its own dict. For example,  <br>for four-class multilabel classification weights should be  <br>\[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}\] instead of  <br>\[{1:1}, {2:5}, {3:1}, {4:1}\].  <br>  <br>The "balanced" mode uses the values of y to automatically adjust  <br>weights inversely proportional to class frequencies in the input data  <br>as \`\`n\_samples / (n\_classes \* np.bincount(y))\`\`  <br>  <br>The "balanced\_subsample" mode is the same as "balanced" except that  <br>weights are computed based on the bootstrap sample for every tree  <br>grown.  <br>  <br>For multi-output, the weights of each column of y will be multiplied.  <br>  <br>Note that these weights will be multiplied with sample\_weight (passed  <br>through the fit method) if sample\_weight is specified.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [ccp\_alpha ccp\_alpha: non-negative float, default=0.0  <br>  <br>Complexity parameter used for Minimal Cost-Complexity Pruning. The  <br>subtree with the largest cost complexity that is smaller than  <br>\`\`ccp\_alpha\`\` will be chosen. By default, no pruning is performed. See  <br>:ref:\`minimal\_cost\_complexity\_pruning\` for details. See  <br>:ref:\`sphx\_glr\_auto\_examples\_tree\_plot\_cost\_complexity\_pruning.py\`  <br>for an example of such pruning.  <br>  <br>.. versionadded:: 0.22](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0 |\
|     | [max\_samples max\_samples: int or float, default=None  <br>  <br>If bootstrap is True, the number of samples to draw from X  <br>to train each base estimator.  <br>  <br>\- If None (default), then draw \`X.shape\[0\]\` samples irrespective of  <br>\`sample\_weight\`.  <br>\- If int, then draw \`max\_samples\` samples.  <br>\- If float, then draw \`max\_samples \* X.shape\[0\]\` unweighted samples  <br>or \`max\_samples \* sample\_weight.sum()\` weighted samples.  <br>  <br>.. versionadded:: 0.22  <br>  <br>.. versionchanged:: 1.9  <br>Float \`max\_samples\` is relative to \`sample\_weight.sum()\` instead of  <br>\`X.shape\[0\]\` for weighted samples.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features,), default=None  <br>  <br>Indicates the monotonicity constraint to enforce on each feature.  <br>\- 1: monotonically increasing  <br>\- 0: no constraint  <br>\- -1: monotonically decreasing  <br>  <br>If monotonic\_cst is None, no constraints are applied.  <br>  <br>Monotonicity constraints are not supported for:  <br>\- multiclass classifications (i.e. when \`n\_classes > 2\`),  <br>\- multioutput classifications (i.e. when \`n\_outputs\_ > 1\`).  <br>  <br>The constraints hold over the probability of the positive class.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%2C%29%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,) or a list of such arrays  <br>  <br>The classes labels (single output problem), or a list of arrays of  <br>class labels (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29%20or%20a%20list%20of%20such%20arrays) | ndarray\[object\](2,) | \['0','1'\] |\
| [estimator\_ estimator\_: :class:\`~sklearn.tree.DecisionTreeClassifier\`  <br>  <br>The child estimator template used to create the collection of fitted  <br>sub-estimators.  <br>  <br>.. versionadded:: 1.2  <br>\`base\_estimator\_\` was renamed to \`estimator\_\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimator_,-%3Aclass%3A~sklearn.tree.DecisionTreeClassifier) | DecisionTreeClassifier | DecisionTreeClassifier() |\
| [estimators\_ estimators\_: list of DecisionTreeClassifier  <br>  <br>The collection of fitted sub-estimators.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_,-list%20of%20DecisionTreeClassifier) | list | \[DecisionTreeC...te=1608637542), DecisionTreeC...te=1273642419), DecisionTreeC...te=1935803228), DecisionTreeC...ate=787846414), ...\] |\
| [estimators\_samples\_ estimators\_samples\_: list of arrays  <br>  <br>The subset of drawn samples (i.e., the in-bag samples) for each base  <br>estimator. Each subset is defined by an array of the indices selected.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=estimators_samples_,-list%20of%20arrays) | list | \[array(\[475, ..., dtype=int32), array(\[686, 6..., dtype=int32), array(\[342, 4..., dtype=int32), array(\[800, 5..., dtype=int32), ...\] |\
| [feature\_importances\_ feature\_importances\_: ndarray of shape (n\_features,)  <br>  <br>The impurity-based feature importances.  <br>The higher, the more important the feature.  <br>The importance of a feature is computed as the (normalized)  <br>total reduction of the criterion brought by that feature. It is also  <br>known as the Gini importance.  <br>  <br>Warning: impurity-based feature importances can be misleading for  <br>high cardinality features (many unique values). See  <br>:func:\`sklearn.inspection.permutation\_importance\` as an alternative.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=feature_importances_,-ndarray%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](9,) | \[0.13,0.5 ,0.03,...,0.03,0.14,0.06\] |\
| [n\_classes\_ n\_classes\_: int or list  <br>  <br>The number of classes (single output problem), or a list containing the  <br>number of classes for each output (multi-output problem).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_classes_,-int%20or%20list) | int | 2   |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_features_in_,-int) | int | 9   |\
| [n\_outputs\_ n\_outputs\_: int  <br>  <br>The number of outputs when \`\`fit\`\` is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_outputs_,-int) | int | 1   |\
\
  \
  \
\
Observing the accuracy score on the training and testing set, we observe that the two metrics are very similar now. Therefore, our model is not overfitting anymore. We can then check the permutation importances with this new model.\
\
print(f"RF train accuracy: {rf.score(X\_train, y\_train):.3f}")\
print(f"RF test accuracy: {rf.score(X\_test, y\_test):.3f}")\
\
Copy to clipboard\
\
RF train accuracy: 0.810\
RF test accuracy: 0.832\
\
Copy to clipboard\
\
train\_result \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
(\
    rf, X\_train, y\_train, n\_repeats\=10, random\_state\=42, n\_jobs\=2\
)\
test\_results \= [permutation\_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")\
(\
    rf, X\_test, y\_test, n\_repeats\=10, random\_state\=42, n\_jobs\=2\
)\
sorted\_importances\_idx \= train\_result.importances\_mean.argsort()\
\
Copy to clipboard\
\
train\_importances \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    train\_result.importances\[sorted\_importances\_idx\].T,\
    columns\=X.columns\[sorted\_importances\_idx\],\
)\
test\_importances \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    test\_results.importances\[sorted\_importances\_idx\].T,\
    columns\=X.columns\[sorted\_importances\_idx\],\
)\
\
Copy to clipboard\
\
for name, importances in zip(\["train", "test"\], \[train\_importances, test\_importances\]):\
    plot\_importances\_box(importances, f"Permutation Importances ({name} set)")\
\
Copy to clipboard\
\
*   ![Permutation Importances (train set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_004.png)\
*   ![Permutation Importances (test set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_005.png)\
\
Now, we can observe that on both sets, the `random_num` and `random_cat` features have a lower importance compared to the overfitting random forest. However, the conclusions regarding the importance of the other features are still valid.\
\
**Total running time of the script:** (0 minutes 6.975 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_permutation_importance.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_permutation_importance.ipynb)\
\
[`Download Jupyter notebook: plot_permutation_importance.ipynb`](https://scikit-learn.org/stable/_downloads/f99bb35c32eb8028063a1428c3999b84/plot_permutation_importance.ipynb)\
\
[`Download Python source code: plot_permutation_importance.py`](https://scikit-learn.org/stable/_downloads/3c3c738275484acc54821615bf72894a/plot_permutation_importance.py)\
\
[`Download zipped: plot_permutation_importance.zip`](https://scikit-learn.org/stable/_downloads/4727c89312a4840b10accd3381f1b354/plot_permutation_importance.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_thumb.png)\
\
[Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html)\
\
Feature importances with a forest of trees\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)\
\
[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)\
\
Permutation Importance with Multicollinear or Correlated Features\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)\
\
[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)\
\
Gradient Boosting regression\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)\
\
[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)\
\
Release Highlights for scikit-learn 0.22\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/3c3c738275484acc54821615bf72894a/plot_permutation_importance.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f99bb35c32eb8028063a1428c3999b84/plot_permutation_importance.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/4727c89312a4840b10accd3381f1b354/plot_permutation_importance.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_permutation_importance.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_permutation_importance.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)