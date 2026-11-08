[Skip to main content](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/compose/plot_column_transformer_mixed_types.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/compose/plot_column_transformer_mixed_types.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/compose/plot_column_transformer_mixed_types.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/compose/plot_column_transformer_mixed_types.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/compose/plot_column_transformer_mixed_types.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/compose/plot_column_transformer_mixed_types.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-download-auto-examples-compose-plot-column-transformer-mixed-types-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Column Transformer with Mixed Types[#](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#column-transformer-with-mixed-types "Link to this heading")

==================================================================================================================================================================================================

This example illustrates how to apply different preprocessing and feature extraction pipelines to different subsets of features, using [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
. This is particularly handy for the case of datasets that contain heterogeneous data types, since we may want to scale the numeric features and one-hot encode the categorical ones.

In this example, the numeric data is standard-scaled after mean-imputation. The categorical data is one-hot encoded via `OneHotEncoder`, which creates a new category for missing values. We further reduce the dimensionality by selecting categories using a chi-squared test.

In addition, we show two different ways to dispatch the columns to the particular pre-processor: by column names and by column data types.

Finally, the preprocessing pipeline is integrated in a full prediction pipeline using [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
, together with a simple classification model.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import numpy as np

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.feature\_selection import [SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")
, [chi2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")
from sklearn.impute import [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.model\_selection import [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
, [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

Copy to clipboard

Load data from [https://www.openml.org/d/40945](https://www.openml.org/d/40945)

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("titanic", version\=1, as\_frame\=True, return\_X\_y\=True)

\# Alternatively X and y can be obtained directly from the frame attribute:
\# X = titanic.frame.drop('survived', axis=1)
\# y = titanic.frame\['survived'\]

Copy to clipboard

Use `ColumnTransformer` by selecting column by names

We will train our classifier with the following features:

Numeric Features:

*   `age`: float;
    
*   `fare`: float.
    

Categorical Features:

*   `embarked`: categories encoded as strings `{'C', 'S', 'Q'}`;
    
*   `sex`: categories encoded as strings `{'female', 'male'}`;
    
*   `pclass`: ordinal integers `{1, 2, 3}`.
    

We create the preprocessing pipelines for both numeric and categorical data. Note that `pclass` could either be treated as a categorical or numeric feature.

numeric\_features \= \["age", "fare"\]
numeric\_transformer \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    steps\=\[("imputer", [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")\
(strategy\="median")), ("scaler", [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
())\]
)

categorical\_features \= \["embarked", "sex", "pclass"\]
categorical\_transformer \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    steps\=\[\
        ("encoder", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore", sparse\_output\=False)),\
        ("selector", [SelectPercentile](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")\
([chi2](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")\
, percentile\=50)),\
    \]
)
preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    transformers\=\[\
        ("num", numeric\_transformer, numeric\_features),\
        ("cat", categorical\_transformer, categorical\_features),\
    \]
)

Copy to clipboard

Append classifier to preprocessing pipeline. Now we have a full prediction pipeline.

clf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    steps\=\[("preprocessor", preprocessor), ("classifier", [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
())\]
).set\_output(transform\="pandas")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, test\_size\=0.2, random\_state\=0)

clf.fit(X\_train, y\_train)
print("model score: %.3f" % clf.score(X\_test, y\_test))

Copy to clipboard

model score: 0.798

Copy to clipboard

HTML representation of `Pipeline` (display diagram)

When the `Pipeline` is printed out in a jupyter notebook an HTML representation of the estimator is displayed:

clf

Copy to clipboard

Pipeline(steps=\[('preprocessor',\
                 ColumnTransformer(transformers=\[('num',\
                                                  Pipeline(steps=\[('imputer',\
                                                                   SimpleImputer(strategy='median')),\
                                                                  ('scaler',\
                                                                   StandardScaler())\]),\
                                                  \['age', 'fare'\]),\
                                                 ('cat',\
                                                  Pipeline(steps=\[('encoder',\
                                                                   OneHotEncoder(handle\_unknown='ignore',\
                                                                                 sparse\_output=False)),\
                                                                  ('selector',\
                                                                   SelectPercentile(percentile=50,\
                                                                                    score\_func=<function chi2 at 0x7e1df6819380>))\]),\
                                                  \['embarked', 'sex',\
                                                   'pclass'\])\])),\
                ('classifier', LogisticRegression())\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('preprocessor', ...), ('classifier', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['0','1'\] |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](13,) | \['pclass','name','sex',...,'boat','body','home.dest'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 13  |

preprocessor: ColumnTransformer

[?Documentation for preprocessor: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('num', ...), ('cat', ...)\] |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](13,) | \['pclass','name','sex',...,'boat','body','home.dest'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 13  |
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'num': Pipel...nder': 'drop'} |
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cat': slice(2, 6, None), 'num': slice(0, 2, None), 're...er': slice(0, 0, None)} |
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('num', Pipeline(step...ardScaler())\]), \['age', 'fare'\]), ('cat', Pipeline(step...df6819380>))\]), \['em...ed', 'sex', 'pclass'\]), ('re...er', 'drop', \['name', 'sibsp', 'parch', 'ticket', ...\])\] |

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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['age','fare'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[29.65,33.73\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 2   |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1047 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[12.56,51.11\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](2,) | \[ 157.68,2612.62\] |

2 features

|     |
| --- |
| age |
| fare |

cat

\['embarked', 'sex', 'pclass'\]

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
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['C', '... dtype=object), array(\['femal... dtype=object), array(\[1, 2, 3\])\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['embarked','sex','pclass'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 3   |\
\
9 features\
\
|     |\
| --- |\
| embarked\_C |\
| embarked\_Q |\
| embarked\_S |\
| embarked\_nan |\
| sex\_female |\
| sex\_male |\
| pclass\_1 |\
| pclass\_2 |\
| pclass\_3 |\
\
SelectPercentile\
\
[?Documentation for SelectPercentile](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [score\_func score\_func: callable, default=f\_classif  <br>  <br>Function taking two arrays X and y, and returning a pair of arrays  <br>(scores, pvalues) or a single array with scores.  <br>Default is f\_classif (see below "See Also"). The default function only  <br>works with classification tasks.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=score_func,-callable%2C%20default%3Df_classif) | <function chi...x7e1df6819380> |\
|     | [percentile percentile: int, default=10  <br>  <br>Percent of features to keep.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=percentile,-int%2C%20default%3D10) | 50  |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](9,) | \['embarked\_C','embarked\_Q','embarked\_S',...,'pclass\_1','pclass\_2', 'pclass\_3'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=n_features_in_,-int) | int | 9   |\
| [pvalues\_ pvalues\_: array-like of shape (n\_features,)  <br>  <br>p-values of feature scores, None if \`score\_func\` returned only scores.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=pvalues_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](9,) | \[0. ,0.67,0.01,...,0. ,0.05,0. \] |\
| [scores\_ scores\_: array-like of shape (n\_features,)  <br>  <br>Scores of features.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=scores_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](9,) | \[27.8 , 0.18, 7.33,...,60.96, 4.02,42.24\] |\
\
4 features\
\
|     |\
| --- |\
| sex\_female |\
| sex\_male |\
| pclass\_1 |\
| pclass\_3 |\
\
6 features\
\
|     |\
| --- |\
| num\_\_age |\
| num\_\_fare |\
| cat\_\_sex\_female |\
| cat\_\_sex\_male |\
| cat\_\_pclass\_1 |\
| cat\_\_pclass\_3 |\
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
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 6) | \[\[-0.31, 0.03, 1.22,-1.22, 0.93,-1. \]\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](6,) | \['num\_\_age','num\_\_fare','cat\_\_sex\_female','cat\_\_sex\_male','cat\_\_pclass\_1', 'cat\_\_pclass\_3'\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 6   |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[12\] |\
\
  \
  \
\
Use `ColumnTransformer` by selecting column by data types\
\
When dealing with a cleaned dataset, the preprocessing can be automatic by using the data types of the column to decide whether to treat a column as a numerical or categorical feature. [`sklearn.compose.make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")\
 gives this possibility. First, let’s only select a subset of columns to simplify our example.\
\
subset\_feature \= \["embarked", "sex", "pclass", "age", "fare"\]\
X\_train, X\_test \= X\_train\[subset\_feature\], X\_test\[subset\_feature\]\
\
Copy to clipboard\
\
Then, we introspect the information regarding each column data type.\
\
X\_train.info()\
\
Copy to clipboard\
\
<class 'pandas.DataFrame'>\
Index: 1047 entries, 1118 to 684\
Data columns (total 5 columns):\
 #   Column    Non-Null Count  Dtype\
---  ------    --------------  -----\
 0   embarked  1045 non-null   category\
 1   sex       1047 non-null   category\
 2   pclass    1047 non-null   int64\
 3   age       841 non-null    float64\
 4   fare      1046 non-null   float64\
dtypes: category(2), float64(2), int64(1)\
memory usage: 34.8 KB\
\
Copy to clipboard\
\
We can observe that the `embarked` and `sex` columns were tagged as `category` columns when loading the data with `fetch_openml`. Therefore, we can use this information to dispatch the categorical columns to the `categorical_transformer` and the remaining columns to the `numerical_transformer`.\
\
Note\
\
In practice, you will have to handle yourself the column data type. If you want some columns to be considered as `category`, you will have to convert them into categorical columns. If you are using pandas, you can refer to their documentation regarding [Categorical data](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)\
.\
\
from sklearn.compose import make\_column\_selector as [selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")\
\
preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
    transformers\=\[\
        ("num", numeric\_transformer, [selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")\
(dtype\_exclude\="category")),\
        ("cat", categorical\_transformer, [selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")\
(dtype\_include\="category")),\
    \]\
)\
clf \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
    steps\=\[("preprocessor", preprocessor), ("classifier", [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
())\]\
)\
\
clf.fit(X\_train, y\_train)\
print("model score: %.3f" % clf.score(X\_test, y\_test))\
clf\
\
Copy to clipboard\
\
model score: 0.798\
\
Copy to clipboard\
\
Pipeline(steps=\[('preprocessor',\
                 ColumnTransformer(transformers=\[('num',\
                                                  Pipeline(steps=\[('imputer',\
                                                                   SimpleImputer(strategy='median')),\
                                                                  ('scaler',\
                                                                   StandardScaler())\]),\
                                                  <sklearn.compose.\_column\_transformer.make\_column\_selector object at 0x7e1dbda45f70>),\
                                                 ('cat',\
                                                  Pipeline(steps=\[('encoder',\
                                                                   OneHotEncoder(handle\_unknown='ignore',\
                                                                                 sparse\_output=False)),\
                                                                  ('selector',\
                                                                   SelectPercentile(percentile=50,\
                                                                                    score\_func=<function chi2 at 0x7e1df6819380>))\]),\
                                                  <sklearn.compose.\_column\_transformer.make\_column\_selector object at 0x7e1dbda460f0>)\])),\
                ('classifier', LogisticRegression())\])\
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
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('preprocessor', ...), ('classifier', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. Only exist if the last step of the pipeline is a  <br>classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['0','1'\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['embarked','sex','pclass','age','fare'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 5   |\
\
preprocessor: ColumnTransformer\
\
[?Documentation for preprocessor: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('num', ...), ('cat', ...)\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['embarked','sex','pclass','age','fare'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 5   |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'num': Pipel...f6819380>))\])} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cat': slice(3, 6, None), 'num': slice(0, 3, None), 're...er': slice(0, 0, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('num', Pipeline(step...ardScaler())\]), \['pclass', 'age', 'fare'\]), ('cat', Pipeline(step...df6819380>))\]), \['em...ed', 'sex'\])\] |

num

\['pclass', 'age', 'fare'\]

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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['pclass','age','fare'\] |
| [indicator\_ indicator\_: :class:\`~sklearn.impute.MissingIndicator\`  <br>  <br>Indicator used to add binary indicators for missing values.  <br>\`None\` if \`add\_indicator=False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=indicator_,-%3Aclass%3A~sklearn.impute.MissingIndicator) | NoneType | None |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=n_features_in_,-int) | int | 3   |
| [statistics\_ statistics\_: array of shape (n\_features,)  <br>  <br>The imputation fill value for each feature.  <br>Computing statistics can result in \`np.nan\` values.  <br>During :meth:\`transform\`, features corresponding to \`np.nan\`  <br>statistics will be discarded.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=statistics_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](3,) | \[ 3. ,28. ,14.45\] |

3 features

|     |
| --- |
| pclass |
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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['pclass','age','fare'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 2.3 ,29.65,33.73\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 3   |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1047 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 0.84,12.56,51.11\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 0.71, 157.68,2612.62\] |

3 features

|     |
| --- |
| pclass |
| age |
| fare |

cat

\['embarked', 'sex'\]

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
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['C', '... dtype=object), array(\['femal... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['embarked','sex'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 2   |\
\
6 features\
\
|     |\
| --- |\
| embarked\_C |\
| embarked\_Q |\
| embarked\_S |\
| embarked\_nan |\
| sex\_female |\
| sex\_male |\
\
SelectPercentile\
\
[?Documentation for SelectPercentile](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [score\_func score\_func: callable, default=f\_classif  <br>  <br>Function taking two arrays X and y, and returning a pair of arrays  <br>(scores, pvalues) or a single array with scores.  <br>Default is f\_classif (see below "See Also"). The default function only  <br>works with classification tasks.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=score_func,-callable%2C%20default%3Df_classif) | <function chi...x7e1df6819380> |\
|     | [percentile percentile: int, default=10  <br>  <br>Percent of features to keep.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=percentile,-int%2C%20default%3D10) | 50  |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](6,) | \['embarked\_C','embarked\_Q','embarked\_S','embarked\_nan','sex\_female', 'sex\_male'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=n_features_in_,-int) | int | 6   |\
| [pvalues\_ pvalues\_: array-like of shape (n\_features,)  <br>  <br>p-values of feature scores, None if \`score\_func\` returned only scores.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=pvalues_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](6,) | \[0. ,0.67,0.01,0.07,0. ,0. \] |\
| [scores\_ scores\_: array-like of shape (n\_features,)  <br>  <br>Scores of features.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=scores_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](6,) | \[ 27.8 , 0.18, 7.33, 3.23,187.26,108.46\] |\
\
3 features\
\
|     |\
| --- |\
| embarked\_C |\
| sex\_female |\
| sex\_male |\
\
6 features\
\
|     |\
| --- |\
| num\_\_pclass |\
| num\_\_age |\
| num\_\_fare |\
| cat\_\_embarked\_C |\
| cat\_\_sex\_female |\
| cat\_\_sex\_male |\
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
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 6) | \[\[-0.8 ,-0.31,-0.04, 0.65, 1.24,-1.24\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.44\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 6   |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[18\] |\
\
  \
  \
\
The resulting score is not exactly the same as the one from the previous pipeline because the dtype-based selector treats the `pclass` column as a numeric feature instead of a categorical feature as previously:\
\
[selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")\
(dtype\_exclude\="category")(X\_train)\
\
Copy to clipboard\
\
\['pclass', 'age', 'fare'\]\
\
Copy to clipboard\
\
[selector](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")\
(dtype\_include\="category")(X\_train)\
\
Copy to clipboard\
\
\['embarked', 'sex'\]\
\
Copy to clipboard\
\
Using the prediction pipeline in a grid search\
\
Grid search can also be performed on the different preprocessing steps defined in the `ColumnTransformer` object, together with the classifier’s hyperparameters as part of the `Pipeline`. We will search for both the imputer strategy of the numeric preprocessing and the regularization parameter of the logistic regression using [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")\
. This hyperparameter search randomly selects a fixed number of parameter settings configured by `n_iter`. Alternatively, one can use [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")\
 but the cartesian product of the parameter space will be evaluated.\
\
param\_grid \= {\
    "preprocessor\_\_num\_\_imputer\_\_strategy": \["mean", "median"\],\
    "preprocessor\_\_cat\_\_selector\_\_percentile": \[10, 30, 50, 70\],\
    "classifier\_\_C": \[0.1, 1.0, 10, 100\],\
}\
\
search\_cv \= [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")\
(clf, param\_grid, n\_iter\=10, random\_state\=0)\
search\_cv\
\
Copy to clipboard\
\
RandomizedSearchCV(estimator=Pipeline(steps=\[('preprocessor',\
                                              ColumnTransformer(transformers=\[('num',\
                                                                               Pipeline(steps=\[('imputer',\
                                                                                                SimpleImputer(strategy='median')),\
                                                                                               ('scaler',\
                                                                                                StandardScaler())\]),\
                                                                               <sklearn.compose.\_column\_transformer.make\_column\_selector object at 0x7e1dbda45f70>),\
                                                                              ('cat',\
                                                                               Pipeline(steps=\[('encoder',\
                                                                                                OneHotEncoder(handle\_unknown='ignore',\
                                                                                                              spars...\
                                                                                                                 score\_func=<function chi2 at 0x7e1df6819380>))\]),\
                                                                               <sklearn.compose.\_column\_transformer.make\_column\_selector object at 0x7e1dbda460f0>)\])),\
                                             ('classifier',\
                                              LogisticRegression())\]),\
                   param\_distributions={'classifier\_\_C': \[0.1, 1.0, 10, 100\],\
                                        'preprocessor\_\_cat\_\_selector\_\_percentile': \[10,\
                                                                                    30,\
                                                                                    50,\
                                                                                    70\],\
                                        'preprocessor\_\_num\_\_imputer\_\_strategy': \['mean',\
                                                                                 'median'\]},\
                   random\_state=0)\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
RandomizedSearchCV\
\
[?Documentation for RandomizedSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)\
iNot fitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [estimator estimator: estimator object  <br>  <br>An object of that type is instantiated for each grid point.  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...egression())\]) |\
|     | [param\_distributions param\_distributions: dict or list of dicts  <br>  <br>Dictionary with parameters names (\`str\`) as keys and distributions  <br>or lists of parameters to try. Distributions must provide a \`\`rvs\`\`  <br>method for sampling (such as those from scipy.stats.distributions).  <br>If a list is given, it is sampled uniformly.  <br>If a list of dicts is given, first a dict is sampled uniformly, and  <br>then a parameter is sampled using that dict as above.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=param_distributions,-dict%20or%20list%20of%20dicts) | {'classifier\_\_C': \[0.1, 1.0, ...\], 'preprocessor\_\_cat\_\_selector\_\_percentile': \[10, 30, ...\], 'preprocessor\_\_num\_\_imputer\_\_strategy': \['mean', 'median'\]} |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo random number generator state used for random uniform sampling  <br>from lists of possible values instead of scipy.stats distributions.  <br>Pass an int for reproducible output across multiple  <br>function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |\
|     | [n\_iter n\_iter: int, default=10  <br>  <br>Number of parameter settings that are sampled. n\_iter trades  <br>off runtime vs quality of the solution.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=n_iter,-int%2C%20default%3D10) | 10  |\
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.  <br>  <br>If None, the estimator's score method is used.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | None |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given the \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`RandomizedSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [verbose verbose: int, default = 0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=verbose,-int%2C%20default%20%3D%200) | 0   |\
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |\
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |\
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |\
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
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('num', ...), ('cat', ...)\] |\
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |\
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |\
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |\
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |\
\
num\
\
\['pclass', 'age', 'fare'\]\
\
SimpleImputer\
\
[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'median' |\
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |\
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
cat\
\
\['embarked', 'sex'\]\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | False |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
SelectPercentile\
\
[?Documentation for SelectPercentile](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [score\_func score\_func: callable, default=f\_classif  <br>  <br>Function taking two arrays X and y, and returning a pair of arrays  <br>(scores, pvalues) or a single array with scores.  <br>Default is f\_classif (see below "See Also"). The default function only  <br>works with classification tasks.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=score_func,-callable%2C%20default%3Df_classif) | <function chi...x7e1df6819380> |\
|     | [percentile percentile: int, default=10  <br>  <br>Percent of features to keep.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=percentile,-int%2C%20default%3D10) | 50  |\
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
  \
  \
\
Calling ‘fit’ triggers the cross-validated search for the best hyper-parameters combination:\
\
search\_cv.fit(X\_train, y\_train)\
\
print("Best params:")\
print(search\_cv.best\_params\_)\
search\_cv\
\
Copy to clipboard\
\
Best params:\
{'preprocessor\_\_num\_\_imputer\_\_strategy': 'mean', 'preprocessor\_\_cat\_\_selector\_\_percentile': 30, 'classifier\_\_C': 100}\
\
Copy to clipboard\
\
RandomizedSearchCV(estimator=Pipeline(steps=\[('preprocessor',\
                                              ColumnTransformer(transformers=\[('num',\
                                                                               Pipeline(steps=\[('imputer',\
                                                                                                SimpleImputer(strategy='median')),\
                                                                                               ('scaler',\
                                                                                                StandardScaler())\]),\
                                                                               <sklearn.compose.\_column\_transformer.make\_column\_selector object at 0x7e1dbda45f70>),\
                                                                              ('cat',\
                                                                               Pipeline(steps=\[('encoder',\
                                                                                                OneHotEncoder(handle\_unknown='ignore',\
                                                                                                              spars...\
                                                                                                                 score\_func=<function chi2 at 0x7e1df6819380>))\]),\
                                                                               <sklearn.compose.\_column\_transformer.make\_column\_selector object at 0x7e1dbda460f0>)\])),\
                                             ('classifier',\
                                              LogisticRegression())\]),\
                   param\_distributions={'classifier\_\_C': \[0.1, 1.0, 10, 100\],\
                                        'preprocessor\_\_cat\_\_selector\_\_percentile': \[10,\
                                                                                    30,\
                                                                                    50,\
                                                                                    70\],\
                                        'preprocessor\_\_num\_\_imputer\_\_strategy': \['mean',\
                                                                                 'median'\]},\
                   random\_state=0)\
\
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  \
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**\
\
RandomizedSearchCV\
\
[?Documentation for RandomizedSearchCV](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html)\
iFitted\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [estimator estimator: estimator object  <br>  <br>An object of that type is instantiated for each grid point.  <br>This is assumed to implement the scikit-learn estimator interface.  <br>Either estimator needs to provide a \`\`score\`\` function,  <br>or \`\`scoring\`\` must be passed.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=estimator,-estimator%20object) | Pipeline(step...egression())\]) |
|     | [param\_distributions param\_distributions: dict or list of dicts  <br>  <br>Dictionary with parameters names (\`str\`) as keys and distributions  <br>or lists of parameters to try. Distributions must provide a \`\`rvs\`\`  <br>method for sampling (such as those from scipy.stats.distributions).  <br>If a list is given, it is sampled uniformly.  <br>If a list of dicts is given, first a dict is sampled uniformly, and  <br>then a parameter is sampled using that dict as above.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=param_distributions,-dict%20or%20list%20of%20dicts) | {'classifier\_\_C': \[0.1, 1.0, ...\], 'preprocessor\_\_cat\_\_selector\_\_percentile': \[10, 30, ...\], 'preprocessor\_\_num\_\_imputer\_\_strategy': \['mean', 'median'\]} |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo random number generator state used for random uniform sampling  <br>from lists of possible values instead of scipy.stats distributions.  <br>Pass an int for reproducible output across multiple  <br>function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |
|     | [n\_iter n\_iter: int, default=10  <br>  <br>Number of parameter settings that are sampled. n\_iter trades  <br>off runtime vs quality of the solution.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=n_iter,-int%2C%20default%3D10) | 10  |
|     | [scoring scoring: str, callable, list, tuple or dict, default=None  <br>  <br>Strategy to evaluate the performance of the cross-validated model on  <br>the test set.  <br>  <br>If \`scoring\` represents a single score, one can use:  <br>  <br>\- a single string (see :ref:\`scoring\_string\_names\`);  <br>\- a callable (see :ref:\`scoring\_callable\`) that returns a single value;  <br>\- \`None\`, the \`estimator\`'s  <br>:ref:\`default evaluation criterion <scoring\_api\_overview>\` is used.  <br>  <br>If \`scoring\` represents multiple scores, one can use:  <br>  <br>\- a list or tuple of unique strings;  <br>\- a callable returning a dictionary where the keys are the metric  <br>names and the values are the metric scores;  <br>\- a dictionary with metric names as keys and callables as values.  <br>  <br>See :ref:\`multimetric\_grid\_search\` for an example.  <br>  <br>If None, the estimator's score method is used.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=scoring,-str%2C%20callable%2C%20list%2C%20tuple%20or%20dict%2C%20default%3DNone) | None |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.  <br>  <br>.. versionchanged:: v0.20  <br>\`n\_jobs\` default changed from 1 to None](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [refit refit: bool, str, or callable, default=True  <br>  <br>Refit an estimator using the best found parameters on the whole  <br>dataset.  <br>  <br>For multiple metric evaluation, this needs to be a \`str\` denoting the  <br>scorer that would be used to find the best parameters for refitting  <br>the estimator at the end.  <br>  <br>Where there are considerations other than maximum score in  <br>choosing a best estimator, \`\`refit\`\` can be set to a function which  <br>returns the selected \`\`best\_index\_\`\` given the \`\`cv\_results\_\`\`. In that  <br>case, the \`\`best\_estimator\_\`\` and \`\`best\_params\_\`\` will be set  <br>according to the returned \`\`best\_index\_\`\` while the \`\`best\_score\_\`\`  <br>attribute will not be available.  <br>  <br>The refitted estimator is made available at the \`\`best\_estimator\_\`\`  <br>attribute and permits using \`\`predict\`\` directly on this  <br>\`\`RandomizedSearchCV\`\` instance.  <br>  <br>Also for multiple metric evaluation, the attributes \`\`best\_index\_\`\`,  <br>\`\`best\_score\_\`\` and \`\`best\_params\_\`\` will only be available if  <br>\`\`refit\`\` is set and all of them will be determined w.r.t this specific  <br>scorer.  <br>  <br>See \`\`scoring\`\` parameter to know more about multiple metric  <br>evaluation.  <br>  <br>See :ref:\`this example  <br><sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_refit\_callable.py>\`  <br>for an example of how to use \`\`refit=callable\`\` to balance model  <br>complexity and cross-validated score.  <br>  <br>.. versionchanged:: 0.20  <br>Support for callable added.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=refit,-bool%2C%20str%2C%20or%20callable%2C%20default%3DTrue) | True |
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the default 5-fold cross validation,  <br>\- integer, to specify the number of folds in a \`(Stratified)KFold\`,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if the estimator is a classifier and \`\`y\`\` is  <br>either binary or multiclass, :class:\`StratifiedKFold\` is used. In all  <br>other cases, :class:\`KFold\` is used. These splitters are instantiated  <br>with \`shuffle=False\` so the splits will be the same across calls.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.  <br>  <br>.. versionchanged:: 0.22  <br>\`\`cv\`\` default value if None changed from 3-fold to 5-fold.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |
|     | [verbose verbose: int, default = 0  <br>  <br>Controls the verbosity of information printed during fitting, with higher  <br>values yielding more detailed logging.  <br>  <br>\- 0 : no messages are printed;  <br>\- >=1 : summary of the total number of fits;  <br>\- >=2 : computation time for each fold and parameter candidate;  <br>\- >=3 : fold indices and scores;  <br>\- >=10 : parameter candidate indices and START messages before each fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=verbose,-int%2C%20default%20%3D%200) | 0   |
|     | [pre\_dispatch pre\_dispatch: int, or str, default='2\*n\_jobs'  <br>  <br>Controls the number of jobs that get dispatched during parallel  <br>execution. Reducing this number can be useful to avoid an  <br>explosion of memory consumption when more jobs get dispatched  <br>than CPUs can process. This parameter can be:  <br>  <br>\- None, in which case all the jobs are immediately created and spawned. Use  <br>this for lightweight and fast-running jobs, to avoid delays due to on-demand  <br>spawning of the jobs  <br>\- An int, giving the exact number of total jobs that are spawned  <br>\- A str, giving an expression as a function of n\_jobs, as in '2\*n\_jobs'](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=pre_dispatch,-int%2C%20or%20str%2C%20default%3D%272%2An_jobs%27) | '2\*n\_jobs' |
|     | [error\_score error\_score: 'raise' or numeric, default=np.nan  <br>  <br>Value to assign to the score if an error occurs in estimator fitting.  <br>If set to 'raise', the error is raised. If a numeric value is given,  <br>FitFailedWarning is raised. This parameter does not affect the refit  <br>step, which will always raise the error.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=error_score,-%27raise%27%20or%20numeric%2C%20default%3Dnp.nan) | nan |
|     | [return\_train\_score return\_train\_score: bool, default=False  <br>  <br>If \`\`False\`\`, the \`\`cv\_results\_\`\` attribute will not include training  <br>scores.  <br>Computing training scores is used to get insights on how different  <br>parameter settings impact the overfitting/underfitting trade-off.  <br>However computing the scores on the training set can be computationally  <br>expensive and is not strictly required to select the parameters that  <br>yield the best generalization performance.  <br>  <br>.. versionadded:: 0.19  <br>  <br>.. versionchanged:: 0.21  <br>Default value was changed from \`\`True\`\` to \`\`False\`\`](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=return_train_score,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [best\_estimator\_ best\_estimator\_: estimator  <br>  <br>Estimator that was chosen by the search, i.e. estimator  <br>which gave highest score (or smallest loss if specified)  <br>on the left out data. Not available if \`\`refit=False\`\`.  <br>  <br>For multi-metric evaluation, this attribute is present only if  <br>\`\`refit\`\` is specified.  <br>  <br>See \`\`refit\`\` parameter for more information on allowed values.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=best_estimator_,-estimator) | Pipeline | Pipeline(step...sion(C=100))\]) |
| [best\_index\_ best\_index\_: int  <br>  <br>The index (of the \`\`cv\_results\_\`\` arrays) which corresponds to the best  <br>candidate parameter setting.  <br>  <br>The dict at \`\`search.cv\_results\_\['params'\]\[search.best\_index\_\]\`\` gives  <br>the parameter setting for the best model, that gives the highest  <br>mean score (\`\`search.best\_score\_\`\`).  <br>  <br>For multi-metric evaluation, this is not available if \`\`refit\`\` is  <br>\`\`False\`\`. See \`\`refit\`\` parameter for more information.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=best_index_,-int) | int64 | np.int64(7) |
| [best\_params\_ best\_params\_: dict  <br>  <br>Parameter setting that gave the best results on the hold out data.  <br>  <br>For multi-metric evaluation, this is not available if \`\`refit\`\` is  <br>\`\`False\`\`. See \`\`refit\`\` parameter for more information.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=best_params_,-dict) | dict | {'cl...\_C': 100, 'pr...le': 30, 'pr...gy': 'mean'} |
| [best\_score\_ best\_score\_: float  <br>  <br>Mean cross-validated score of the best\_estimator.  <br>  <br>For multi-metric evaluation, this is not available if \`\`refit\`\` is  <br>\`\`False\`\`. See \`\`refit\`\` parameter for more information.  <br>  <br>This attribute is not available if \`\`refit\`\` is a function.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=best_score_,-float) | float64 | 0.786 |
| [classes\_ classes\_: ndarray of shape (n\_classes,)  <br>  <br>The classes labels. This is present only if \`\`refit\`\` is specified and  <br>the underlying estimator is a classifier.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=classes_,-ndarray%20of%20shape%20%28n_classes%2C%29) | ndarray\[object\](2,) | \['0','1'\] |
| [cv\_results\_ cv\_results\_: dict of numpy (masked) ndarrays  <br>  <br>A dict with keys as column headers and values as columns, that can be  <br>imported into a pandas \`\`DataFrame\`\`.  <br>  <br>For instance the below given table  <br>  <br>+--------------+-------------+-------------------+---+---------------+  <br>\| param\_kernel \| param\_gamma \| split0\_test\_score \|...\|rank\_test\_score\|  <br>+==============+=============+===================+===+===============+  <br>\| 'rbf' \| 0.1 \| 0.80 \|...\| 1 \|  <br>+--------------+-------------+-------------------+---+---------------+  <br>\| 'rbf' \| 0.2 \| 0.84 \|...\| 3 \|  <br>+--------------+-------------+-------------------+---+---------------+  <br>\| 'rbf' \| 0.3 \| 0.70 \|...\| 2 \|  <br>+--------------+-------------+-------------------+---+---------------+  <br>  <br>will be represented by a \`\`cv\_results\_\`\` dict of::  <br>  <br>{  <br>'param\_kernel' : masked\_array(data = \['rbf', 'rbf', 'rbf'\],  <br>mask = False),  <br>'param\_gamma' : masked\_array(data = \[0.1 0.2 0.3\], mask = False),  <br>'split0\_test\_score' : \[0.80, 0.84, 0.70\],  <br>'split1\_test\_score' : \[0.82, 0.50, 0.70\],  <br>'mean\_test\_score' : \[0.81, 0.67, 0.70\],  <br>'std\_test\_score' : \[0.01, 0.24, 0.00\],  <br>'rank\_test\_score' : \[1, 3, 2\],  <br>'split0\_train\_score' : \[0.80, 0.92, 0.70\],  <br>'split1\_train\_score' : \[0.82, 0.55, 0.70\],  <br>'mean\_train\_score' : \[0.81, 0.74, 0.70\],  <br>'std\_train\_score' : \[0.01, 0.19, 0.00\],  <br>'mean\_fit\_time' : \[0.73, 0.63, 0.43\],  <br>'std\_fit\_time' : \[0.01, 0.02, 0.01\],  <br>'mean\_score\_time' : \[0.01, 0.06, 0.04\],  <br>'std\_score\_time' : \[0.00, 0.00, 0.00\],  <br>'params' : \[{'kernel' : 'rbf', 'gamma' : 0.1}, ...\],  <br>}  <br>  <br>For an example of analysing \`\`cv\_results\_\`\`,  <br>see :ref:\`sphx\_glr\_auto\_examples\_model\_selection\_plot\_grid\_search\_stats.py\`.  <br>  <br>NOTE  <br>  <br>The key \`\`'params'\`\` is used to store a list of parameter  <br>settings dicts for all the parameter candidates.  <br>  <br>The \`\`mean\_fit\_time\`\`, \`\`std\_fit\_time\`\`, \`\`mean\_score\_time\`\` and  <br>\`\`std\_score\_time\`\` are all in seconds.  <br>  <br>For multi-metric evaluation, the scores for all the scorers are  <br>available in the \`\`cv\_results\_\`\` dict at the keys ending with that  <br>scorer's name (\`\`'\_<scorer\_name>'\`\`) instead of \`\`'\_score'\`\` shown  <br>above. ('split0\_test\_precision', 'mean\_train\_precision' etc.)](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=cv_results_,-dict%20of%20numpy%20%28masked%29%20ndarrays) | dict | {'me...me': array(\[0.02, ..., 0.02, 0.02\]), 'me...me': array(\[0.01, ..., 0.01, 0.01\]), 'me...re': array(\[0.79, ..., 0.78, 0.78\]), 'pa...\_C': masked\_array(...l\_value=1e+20), ...} |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`feature\_names\_in\_\` when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['embarked','sex','pclass','age','fare'\] |
| [multimetric\_ multimetric\_: bool  <br>  <br>Whether or not the scorers compute several metrics.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=multimetric_,-bool) | bool | False |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if  <br>\`best\_estimator\_\` is defined (see the documentation for the \`refit\`  <br>parameter for more details) and that \`best\_estimator\_\` exposes  <br>\`n\_features\_in\_\` when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=n_features_in_,-int) | int | 5   |
| [n\_splits\_ n\_splits\_: int  <br>  <br>The number of cross-validation splits (folds/iterations).](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=n_splits_,-int) | int | 5   |
| [refit\_time\_ refit\_time\_: float  <br>  <br>Seconds used for refitting the best model on the whole dataset.  <br>  <br>This is present only if \`\`refit\`\` is not False.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=refit_time_,-float) | float | 0.01773 |
| [scorer\_ scorer\_: function or a dict  <br>  <br>Scorer function used on the held out data to choose the best  <br>parameters for the model.  <br>  <br>For multi-metric evaluation, this attribute holds the validated  <br>\`\`scoring\`\` dict which maps the scorer key to the scorer callable.](https://scikit-learn.org/1.9/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#:~:text=scorer_,-function%20or%20a%20dict) | \_PassthroughScorer | Pipeline.score |

best\_estimator\_: Pipeline

preprocessor: ColumnTransformer

[?Documentation for preprocessor: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('num', ...), ('cat', ...)\] |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | True |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](5,) | \['embarked','sex','pclass','age','fare'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 5   |
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'num': Pipel...f6819380>))\])} |
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'cat': slice(3, 5, None), 'num': slice(0, 3, None), 're...er': slice(0, 0, None)} |
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('num', Pipeline(step...ardScaler())\]), \['pclass', 'age', 'fare'\]), ('cat', Pipeline(step...df6819380>))\]), \['em...ed', 'sex'\])\] |

num

\['pclass', 'age', 'fare'\]

SimpleImputer

[?Documentation for SimpleImputer](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [missing\_values missing\_values: int, float, str, np.nan, None or pandas.NA, default=np.nan  <br>  <br>The placeholder for the missing values. All occurrences of  <br>\`missing\_values\` will be imputed. For pandas' dataframes with  <br>nullable integer dtypes with missing values, \`missing\_values\`  <br>can be set to either \`np.nan\` or \`pd.NA\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=missing_values,-int%2C%20float%2C%20str%2C%20np.nan%2C%20None%20or%20pandas.NA%2C%20default%3Dnp.nan) | nan |
|     | [strategy strategy: str or Callable, default='mean'  <br>  <br>The imputation strategy.  <br>  <br>\- If "mean", then replace missing values using the mean along  <br>each column. Can only be used with numeric data.  <br>\- If "median", then replace missing values using the median along  <br>each column. Can only be used with numeric data.  <br>\- If "most\_frequent", then replace missing using the most frequent  <br>value along each column. Can be used with strings or numeric data.  <br>If there is more than one such value, only the smallest is returned.  <br>\- If "constant", then replace missing values with fill\_value. Can be  <br>used with strings or numeric data.  <br>\- If an instance of Callable, then replace missing values using the  <br>scalar statistic returned by running the callable over a dense 1d  <br>array containing non-missing values of each column.  <br>  <br>.. versionadded:: 0.20  <br>strategy="constant" for fixed value imputation.  <br>  <br>.. versionadded:: 1.5  <br>strategy=callable for custom value imputation.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=strategy,-str%20or%20Callable%2C%20default%3D%27mean%27) | 'mean' |
|     | [fill\_value fill\_value: str or numerical value, default=None  <br>  <br>When strategy == "constant", \`fill\_value\` is used to replace all  <br>occurrences of missing\_values. For string or object data types,  <br>\`fill\_value\` must be a string.  <br>If \`None\`, \`fill\_value\` will be 0 when imputing numerical  <br>data and "missing\_value" for strings or object data types.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=fill_value,-str%20or%20numerical%20value%2C%20default%3DNone) | None |
|     | [copy copy: bool, default=True  <br>  <br>If True, a copy of X will be created. If False, imputation will  <br>be done in-place whenever possible. Note that, in the following cases,  <br>a new copy will always be made, even if \`copy=False\`:  <br>  <br>\- If \`X\` is not an array of floating values;  <br>\- If \`X\` is encoded as a CSR matrix;  <br>\- If \`add\_indicator=True\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |
|     | [add\_indicator add\_indicator: bool, default=False  <br>  <br>If True, a :class:\`MissingIndicator\` transform will stack onto output  <br>of the imputer's transform. This allows a predictive estimator  <br>to account for missingness despite imputation. If a feature has no  <br>missing values at fit/train time, the feature won't appear on  <br>the missing indicator even if there are missing values at  <br>transform/test time.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=add_indicator,-bool%2C%20default%3DFalse) | False |
|     | [keep\_empty\_features keep\_empty\_features: bool, default=False  <br>  <br>If True, features that consist exclusively of missing values when  <br>\`fit\` is called are returned in results when \`transform\` is called.  <br>The imputed value is always \`0\` except when \`strategy="constant"\`  <br>in which case \`fill\_value\` will be used instead.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=keep_empty_features,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['pclass','age','fare'\] |
| [indicator\_ indicator\_: :class:\`~sklearn.impute.MissingIndicator\`  <br>  <br>Indicator used to add binary indicators for missing values.  <br>\`None\` if \`add\_indicator=False\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=indicator_,-%3Aclass%3A~sklearn.impute.MissingIndicator) | NoneType | None |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=n_features_in_,-int) | int | 3   |
| [statistics\_ statistics\_: array of shape (n\_features,)  <br>  <br>The imputation fill value for each feature.  <br>Computing statistics can result in \`np.nan\` values.  <br>During :meth:\`transform\`, features corresponding to \`np.nan\`  <br>statistics will be discarded.](https://scikit-learn.org/1.9/modules/generated/sklearn.impute.SimpleImputer.html#:~:text=statistics_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](3,) | \[ 2.3 ,30.05,33.74\] |

3 features

|     |
| --- |
| pclass |
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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['pclass','age','fare'\] |
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 2.3 ,30.05,33.74\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 3   |
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 1047 |
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 0.84,12.53,51.11\] |
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 0.71, 157.01,2612.27\] |

3 features

|     |
| --- |
| pclass |
| age |
| fare |

cat

\['embarked', 'sex'\]

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
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['C', '... dtype=object), array(\['femal... dtype=object)\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | NoneType | None |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](2,) | \['embarked','sex'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 2   |\
\
6 features\
\
|     |\
| --- |\
| embarked\_C |\
| embarked\_Q |\
| embarked\_S |\
| embarked\_nan |\
| sex\_female |\
| sex\_male |\
\
SelectPercentile\
\
[?Documentation for SelectPercentile](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [score\_func score\_func: callable, default=f\_classif  <br>  <br>Function taking two arrays X and y, and returning a pair of arrays  <br>(scores, pvalues) or a single array with scores.  <br>Default is f\_classif (see below "See Also"). The default function only  <br>works with classification tasks.  <br>  <br>.. versionadded:: 0.18](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=score_func,-callable%2C%20default%3Df_classif) | <function chi...x7e1df6819380> |\
|     | [percentile percentile: int, default=10  <br>  <br>Percent of features to keep.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=percentile,-int%2C%20default%3D10) | 30  |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](6,) | \['embarked\_C','embarked\_Q','embarked\_S','embarked\_nan','sex\_female', 'sex\_male'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=n_features_in_,-int) | int | 6   |\
| [pvalues\_ pvalues\_: array-like of shape (n\_features,)  <br>  <br>p-values of feature scores, None if \`score\_func\` returned only scores.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=pvalues_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](6,) | \[0. ,0.67,0.01,0.07,0. ,0. \] |\
| [scores\_ scores\_: array-like of shape (n\_features,)  <br>  <br>Scores of features.](https://scikit-learn.org/1.9/modules/generated/sklearn.feature_selection.SelectPercentile.html#:~:text=scores_,-array-like%20of%20shape%20%28n_features%2C%29) | ndarray\[float64\](6,) | \[ 27.8 , 0.18, 7.33, 3.23,187.26,108.46\] |\
\
2 features\
\
|     |\
| --- |\
| sex\_female |\
| sex\_male |\
\
5 features\
\
|     |\
| --- |\
| num\_\_pclass |\
| num\_\_age |\
| num\_\_fare |\
| cat\_\_sex\_female |\
| cat\_\_sex\_male |\
\
LogisticRegression\
\
[?Documentation for LogisticRegression](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [C C: float, default=1.0  <br>  <br>Inverse of regularization strength; must be a positive float.  <br>Like in support vector machines, smaller values specify stronger  <br>regularization. \`C=np.inf\` results in unpenalized logistic regression.  <br>For a visual example on the effect of tuning the \`C\` parameter  <br>with an L1 penalty, see:  <br>:ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_logistic\_path.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 100 |\
|     | [penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'  <br>  <br>Specify the norm of the penalty:  <br>  <br>\- \`None\`: no penalty is added;  <br>\- \`'l2'\`: add an L2 penalty term and it is the default choice;  <br>\- \`'l1'\`: add an L1 penalty term;  <br>\- \`'elasticnet'\`: both L1 and L2 penalty terms are added.  <br>  <br>.. warning::  <br>Some penalties may not work with some solvers. See the parameter  <br>\`solver\` below, to know the compatibility between the penalty and  <br>solver.  <br>  <br>.. versionadded:: 0.19  <br>l1 penalty with SAGA solver (allowing 'multinomial' + L1)  <br>  <br>.. deprecated:: 1.8  <br>\`penalty\` was deprecated in version 1.8 and will be removed in 1.10.  <br>Use \`l1\_ratio\` and \`C\` instead. \`l1\_ratio=0\` for \`penalty='l2'\`,  <br>\`l1\_ratio=1\` for \`penalty='l1'\`, \`l1\_ratio\` set to any float between 0 and 1  <br>for \`penalty='elasticnet'\`, and \`C=np.inf\` for \`penalty=None\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated' |\
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
| [coef\_ coef\_: ndarray or CSR matrix of shape (1, n\_features) or (n\_classes, n\_features)  <br>  <br>Coefficients of the features in the decision function.  <br>  <br>\`coef\_\` is of shape (1, n\_features) when the given problem is binary.  <br>  <br>By default, it will be created as a dense array, but can be turned to  <br>sparse (CSR format) through :meth:\`sparsify\` (which can be beneficial  <br>under L1 regularization when many coefficients are zero), and back to  <br>dense through :meth:\`densify\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=coef_,-ndarray%20or%20CSR%20matrix%20of%20shape%20%281%2C%20n_features%29%20or%20%28n_classes%2C%20n_features%29) | ndarray\[float64\](1, 5) | \[\[-0.85,-0.33, 0.01, 1.14,-1.35\]\] |\
| [intercept\_ intercept\_: ndarray of shape (1,) or (n\_classes,)  <br>  <br>Intercept (a.k.a. bias) added to the decision function.  <br>  <br>If \`fit\_intercept\` is set to False, the intercept is set to zero.  <br>\`intercept\_\` is of shape (1,) when the given problem is binary.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_,-ndarray%20of%20shape%20%281%2C%29%20or%20%28n_classes%2C%29) | ndarray\[float64\](1,) | \[-0.21\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_features_in_,-int) | int | 5   |\
| [n\_iter\_ n\_iter\_: ndarray of shape (1, )  <br>  <br>Actual number of iterations for all classes.  <br>  <br>.. versionchanged:: 0.20  <br>  <br>In SciPy <= 1.0.0 the number of lbfgs iterations may exceed  <br>\`\`max\_iter\`\`. \`\`n\_iter\_\`\` will now report at most \`\`max\_iter\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_iter_,-ndarray%20of%20shape%20%281%2C%20%29) | ndarray\[int32\](1,) | \[7\] |\
\
  \
  \
\
The internal cross-validation scores obtained by those parameters is:\
\
print(f"Internal CV score: {search\_cv.best\_score\_:.3f}")\
\
Copy to clipboard\
\
Internal CV score: 0.786\
\
Copy to clipboard\
\
We can also introspect the top grid search results as a pandas dataframe:\
\
import pandas as pd\
\
cv\_results \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(search\_cv.cv\_results\_)\
cv\_results \= cv\_results.sort\_values("mean\_test\_score", ascending\=False)\
cv\_results\[\
    \[\
        "mean\_test\_score",\
        "std\_test\_score",\
        "param\_preprocessor\_\_num\_\_imputer\_\_strategy",\
        "param\_preprocessor\_\_cat\_\_selector\_\_percentile",\
        "param\_classifier\_\_C",\
    \]\
\].head(5)\
\
Copy to clipboard\
\
|     | mean\_test\_score | std\_test\_score | param\_preprocessor\_\_num\_\_imputer\_\_strategy | param\_preprocessor\_\_cat\_\_selector\_\_percentile | param\_classifier\_\_C |\
| --- | --- | --- | --- | --- | --- |\
| 7   | 0.786015 | 0.031020 | mean | 30  | 100.0 |\
| 0   | 0.785063 | 0.030498 | median | 30  | 1.0 |\
| 4   | 0.785063 | 0.030498 | mean | 10  | 10.0 |\
| 2   | 0.785063 | 0.030498 | mean | 30  | 1.0 |\
| 3   | 0.783149 | 0.030462 | mean | 30  | 0.1 |\
\
  \
  \
\
The best hyper-parameters have be used to re-fit a final model on the full training set. We can evaluate that final model on held out test data that was not used for hyperparameter tuning.\
\
print(\
    "accuracy of the best model from randomized search: "\
    f"{search\_cv.score(X\_test, y\_test):.3f}"\
)\
\
Copy to clipboard\
\
accuracy of the best model from randomized search: 0.798\
\
Copy to clipboard\
\
**Total running time of the script:** (0 minutes 1.767 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_column_transformer_mixed_types.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_column_transformer_mixed_types.ipynb)\
\
[`Download Jupyter notebook: plot_column_transformer_mixed_types.ipynb`](https://scikit-learn.org/stable/_downloads/26f110ad6cff1a8a7c58b1a00d8b8b5a/plot_column_transformer_mixed_types.ipynb)\
\
[`Download Python source code: plot_column_transformer_mixed_types.py`](https://scikit-learn.org/stable/_downloads/79c38d2f2cb1f2ef7d68e0cc7ea7b4e4/plot_column_transformer_mixed_types.py)\
\
[`Download zipped: plot_column_transformer_mixed_types.zip`](https://scikit-learn.org/stable/_downloads/3344592b61c45b04f094dd038d2e2efd/plot_column_transformer_mixed_types.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_thumb.png)\
\
[Comparing Target Encoder with Other Encoders](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)\
\
Comparing Target Encoder with Other Encoders\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pipeline_display_thumb.png)\
\
[Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html)\
\
Displaying Pipelines\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)\
\
[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)\
\
Categorical Feature Support in Gradient Boosting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)\
\
Release Highlights for scikit-learn 1.2\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
[Download source code](https://scikit-learn.org/stable/_downloads/79c38d2f2cb1f2ef7d68e0cc7ea7b4e4/plot_column_transformer_mixed_types.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/26f110ad6cff1a8a7c58b1a00d8b8b5a/plot_column_transformer_mixed_types.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/3344592b61c45b04f094dd038d2e2efd/plot_column_transformer_mixed_types.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_column_transformer_mixed_types.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_column_transformer_mixed_types.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)