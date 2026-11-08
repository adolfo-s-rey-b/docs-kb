[Skip to main content](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#sphx-glr-download-auto-examples-inspection-plot-linear-model-coefficient-interpretation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Common pitfalls in the interpretation of coefficients of linear models[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#common-pitfalls-in-the-interpretation-of-coefficients-of-linear-models "Link to this heading")

====================================================================================================================================================================================================================================================================================

In linear models, the target value is modeled as a linear combination of the features (see the [Linear Models](https://scikit-learn.org/stable/modules/linear_model.html#linear-model)
 User Guide section for a description of a set of linear models available in scikit-learn). Coefficients in multiple linear models represent the relationship between the given feature, Xi and the target, y, assuming that all the other features remain constant ([conditional dependence](https://en.wikipedia.org/wiki/Conditional_dependence)
). This is different from plotting Xi versus y and fitting a linear relationship: in that case all possible values of the other features are taken into account in the estimation (marginal dependence).

This example will provide some hints in interpreting coefficient in linear models, pointing at problems that arise when either the linear model is not appropriate to describe the dataset, or when features are correlated.

Note

Keep in mind that the features X and the outcome y are in general the result of a data generating process that is unknown to us. Machine learning models are trained to approximate the unobserved mathematical function that links X to y from sample data. As a result, any interpretation made about a model may not necessarily generalize to the true data generating process. This is especially true when the model is of bad quality or when the sample data is not representative of the population.

We will use data from the [“Current Population Survey”](https://www.openml.org/d/534)
 from 1985 to predict wage as a function of various features such as experience, age, or education.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns

Copy to clipboard

The dataset: wages[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#the-dataset-wages "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We fetch the data from [OpenML](http://openml.org/)
. Note that setting the parameter `as_frame` to True will retrieve the data as a pandas dataframe.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

survey \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=534, as\_frame\=True)

Copy to clipboard

Then, we identify features `X` and target `y`: the column WAGE is our target variable (i.e. the variable which we want to predict).

X \= survey.data\[survey.feature\_names\]
X.describe(include\="all")

Copy to clipboard

|     | EDUCATION | SOUTH | SEX | EXPERIENCE | UNION | AGE | RACE | OCCUPATION | SECTOR | MARR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 534.000000 | 534 | 534 | 534.000000 | 534 | 534.000000 | 534 | 534 | 534 | 534 |
| unique | NaN | 2   | 2   | NaN | 2   | NaN | 3   | 6   | 3   | 2   |
| top | NaN | no  | male | NaN | not\_member | NaN | White | Other | Other | Married |
| freq | NaN | 378 | 289 | NaN | 438 | NaN | 440 | 156 | 411 | 350 |
| mean | 13.018727 | NaN | NaN | 17.822097 | NaN | 36.833333 | NaN | NaN | NaN | NaN |
| std | 2.615373 | NaN | NaN | 12.379710 | NaN | 11.726573 | NaN | NaN | NaN | NaN |
| min | 2.000000 | NaN | NaN | 0.000000 | NaN | 18.000000 | NaN | NaN | NaN | NaN |
| 25% | 12.000000 | NaN | NaN | 8.000000 | NaN | 28.000000 | NaN | NaN | NaN | NaN |
| 50% | 12.000000 | NaN | NaN | 15.000000 | NaN | 35.000000 | NaN | NaN | NaN | NaN |
| 75% | 15.000000 | NaN | NaN | 26.000000 | NaN | 44.000000 | NaN | NaN | NaN | NaN |
| max | 18.000000 | NaN | NaN | 55.000000 | NaN | 64.000000 | NaN | NaN | NaN | NaN |

  
  

Note that the dataset contains categorical and numerical variables. We will need to take this into account when preprocessing the dataset thereafter.

X.head()

Copy to clipboard

|     | EDUCATION | SOUTH | SEX | EXPERIENCE | UNION | AGE | RACE | OCCUPATION | SECTOR | MARR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 8   | no  | female | 21  | not\_member | 35  | Hispanic | Other | Manufacturing | Married |
| 1   | 9   | no  | female | 42  | not\_member | 57  | White | Other | Manufacturing | Married |
| 2   | 12  | no  | male | 1   | not\_member | 19  | White | Other | Manufacturing | Unmarried |
| 3   | 12  | no  | male | 4   | not\_member | 22  | White | Other | Other | Unmarried |
| 4   | 12  | no  | male | 17  | not\_member | 35  | White | Other | Other | Married |

  
  

Our target for prediction: the wage. Wages are described as floating-point number in dollars per hour.

y \= survey.target.values.ravel()
survey.target.head()

Copy to clipboard

0    5.10
1    4.95
2    6.67
3    4.00
4    7.50
Name: WAGE, dtype: float64

Copy to clipboard

We split the sample into a train and a test dataset. Only the train dataset will be used in the following exploratory analysis. This is a way to emulate a real situation where predictions are performed on an unknown target, and we don’t want our analysis and decisions to be biased by our knowledge of the test data.

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=42)

Copy to clipboard

First, let’s get some insights by looking at the variables’ distributions and at the pairwise relationships between them. Only numerical variables will be used. In the following plot, each dot represents a sample.

train\_dataset \= X\_train.copy()
train\_dataset.insert(0, "WAGE", y\_train)
\_ \= [sns.pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot "seaborn.pairplot")
(train\_dataset, kind\="reg", diag\_kind\="kde")

Copy to clipboard

![plot linear model coefficient interpretation](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_001.png)

Looking closely at the WAGE distribution reveals that it has a long tail. For this reason, we should take its logarithm to turn it approximately into a normal distribution (linear models such as ridge or lasso work best for a normal distribution of error).

The WAGE is increasing when EDUCATION is increasing. Note that the dependence between WAGE and EDUCATION represented here is a marginal dependence, i.e. it describes the behavior of a specific variable without keeping the others fixed.

Also, the EXPERIENCE and AGE are strongly linearly correlated.

The machine-learning pipeline[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#the-machine-learning-pipeline "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To design our machine-learning pipeline, we first manually check the type of data that we are dealing with:

survey.data.info()

Copy to clipboard

<class 'pandas.DataFrame'>
RangeIndex: 534 entries, 0 to 533
Data columns (total 10 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   EDUCATION   534 non-null    int64
 1   SOUTH       534 non-null    category
 2   SEX         534 non-null    category
 3   EXPERIENCE  534 non-null    int64
 4   UNION       534 non-null    category
 5   AGE         534 non-null    int64
 6   RACE        534 non-null    category
 7   OCCUPATION  534 non-null    category
 8   SECTOR      534 non-null    category
 9   MARR        534 non-null    category
dtypes: category(7), int64(3)
memory usage: 17.3 KB

Copy to clipboard

As seen previously, the dataset contains columns with different data types and we need to apply a specific preprocessing for each data types. In particular categorical variables cannot be included in linear model if not coded as integers first. In addition, to avoid categorical features to be treated as ordered values, we need to one-hot-encode them. Our pre-processor will:

*   one-hot encode (i.e., generate a column by category) the categorical columns, only for non-binary categorical variables;
    
*   as a first approach (we will see after how the normalisation of numerical values will affect our discussion), keep numerical values as they are.
    

from sklearn.compose import [make\_column\_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")

categorical\_columns \= \["RACE", "OCCUPATION", "SECTOR", "MARR", "UNION", "SEX", "SOUTH"\]
numerical\_columns \= \["EDUCATION", "EXPERIENCE", "AGE"\]

preprocessor \= [make\_column\_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")
(
    ([OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
(drop\="if\_binary"), categorical\_columns),
    remainder\="passthrough",
    verbose\_feature\_names\_out\=False,  \# avoid to prepend the preprocessor names
)

Copy to clipboard

We use a ridge regressor with a very small regularization to model the logarithm of the WAGE.

from sklearn.compose import [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
from sklearn.linear\_model import [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    preprocessor,
    [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
(
        regressor\=[Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=1e-10), func\=[np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")
, inverse\_func\=[sp.special.exp10](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp10.html#scipy.special.exp10 "scipy.special.exp10")
    ),
)

Copy to clipboard

Processing the dataset[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#processing-the-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we fit the model.

model.fit(X\_train, y\_train)

Copy to clipboard

Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(remainder='passthrough',\
                                   transformers=\[('onehotencoder',\
                                                  OneHotEncoder(drop='if\_binary'),\
                                                  \['RACE', 'OCCUPATION',\
                                                   'SECTOR', 'MARR', 'UNION',\
                                                   'SEX', 'SOUTH'\])\],\
                                   verbose\_feature\_names\_out=False)),\
                ('transformedtargetregressor',\
                 TransformedTargetRegressor(func=<ufunc 'log10'>,\
                                            inverse\_func=<ufunc 'exp10'>,\
                                            regressor=Ridge(alpha=1e-10)))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iFitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('transformedtargetregressor', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['EDUCATION','SOUTH','SEX',...,'OCCUPATION','SECTOR','MARR'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 10  |

columntransformer: ColumnTransformer

[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('onehotencoder', ...)\] |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'passthrough' |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['EDUCATION','SOUTH','SEX',...,'OCCUPATION','SECTOR','MARR'\] |
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 10  |
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'onehotencod...'one-to-one')} |
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'on...er': slice(0, 16, None), 're...er': slice(16, 19, None)} |
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('on...er', OneHotEncoder...p='if\_binary'), \['RACE', 'OC...ON', 'SECTOR', 'MARR', ...\]), ('re...er', FunctionTrans...='one-to-one'), \['ED...ON', 'EX...CE', 'AGE'\])\] |

onehotencoder

\['RACE', 'OCCUPATION', 'SECTOR', 'MARR', 'UNION', 'SEX', 'SOUTH'\]

OneHotEncoder

[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | 'if\_binary' |
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'error' |
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |

Fitted attributes

| Name | Type | Value |
| --- | --- | --- |
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['Hispa... dtype=object), array(\['Cleri... dtype=object), array(\['Const... dtype=object), array(\['Marri... dtype=object), ...\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[object\](7,) | \[None,None,None,...,0,0,0\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](7,) | \['RACE','OCCUPATION','SECTOR',...,'UNION','SEX','SOUTH'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 7   |\
\
16 features\
\
|     |\
| --- |\
| RACE\_Hispanic |\
| RACE\_Other |\
| RACE\_White |\
| OCCUPATION\_Clerical |\
| OCCUPATION\_Management |\
| OCCUPATION\_Other |\
| OCCUPATION\_Professional |\
| OCCUPATION\_Sales |\
| OCCUPATION\_Service |\
| SECTOR\_Construction |\
| SECTOR\_Manufacturing |\
| SECTOR\_Other |\
| MARR\_Unmarried |\
| UNION\_not\_member |\
| SEX\_male |\
| SOUTH\_yes |\
\
remainder\
\
\['EDUCATION', 'EXPERIENCE', 'AGE'\]\
\
passthrough\
\
[?Documentation for FunctionTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.FunctionTransformer.html)\
\
3 features\
\
|     |\
| --- |\
| EDUCATION |\
| EXPERIENCE |\
| AGE |\
\
19 features\
\
|     |\
| --- |\
| RACE\_Hispanic |\
| RACE\_Other |\
| RACE\_White |\
| OCCUPATION\_Clerical |\
| OCCUPATION\_Management |\
| OCCUPATION\_Other |\
| OCCUPATION\_Professional |\
| OCCUPATION\_Sales |\
| OCCUPATION\_Service |\
| SECTOR\_Construction |\
| SECTOR\_Manufacturing |\
| SECTOR\_Other |\
| MARR\_Unmarried |\
| UNION\_not\_member |\
| SEX\_male |\
| SOUTH\_yes |\
| EDUCATION |\
| EXPERIENCE |\
| AGE |\
\
transformedtargetregressor: TransformedTargetRegressor\
\
[?Documentation for transformedtargetregressor: TransformedTargetRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [regressor regressor: object, default=None  <br>  <br>Regressor object such as derived from  <br>:class:\`~sklearn.base.RegressorMixin\`. This regressor will  <br>automatically be cloned each time prior to fitting. If \`regressor is  <br>None\`, :class:\`~sklearn.linear\_model.LinearRegression\` is created and used.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=regressor,-object%2C%20default%3DNone) | Ridge(alpha=1e-10) |\
|     | [func func: function, default=None  <br>  <br>Function to apply to \`y\` before passing to :meth:\`fit\`. Cannot be set  <br>at the same time as \`transformer\`. If \`func is None\`, the function used will be  <br>the identity function. If \`func\` is set, \`inverse\_func\` also needs to be  <br>provided. The function needs to return a 2-dimensional array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=func,-function%2C%20default%3DNone) | <ufunc 'log10'> |\
|     | [inverse\_func inverse\_func: function, default=None  <br>  <br>Function to apply to the prediction of the regressor. Cannot be set at  <br>the same time as \`transformer\`. The inverse function is used to return  <br>predictions to the same space of the original training labels. If  <br>\`inverse\_func\` is set, \`func\` also needs to be provided. The inverse  <br>function needs to return a 2-dimensional array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=inverse_func,-function%2C%20default%3DNone) | <ufunc 'exp10'> |\
|     | [transformer transformer: object, default=None  <br>  <br>Estimator object such as derived from  <br>:class:\`~sklearn.base.TransformerMixin\`. Cannot be set at the same time  <br>as \`func\` and \`inverse\_func\`. If \`transformer is None\` as well as  <br>\`func\` and \`inverse\_func\`, the transformer will be an identity  <br>transformer. Note that the transformer will be cloned during fitting.  <br>Also, the transformer is restricting \`y\` to be a numpy array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=transformer,-object%2C%20default%3DNone) | None |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that \`transform\` followed by \`inverse\_transform\`  <br>or \`func\` followed by \`inverse\_func\` leads to the original targets.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying regressor exposes such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=n_features_in_,-int) | int | 19  |\
| [regressor\_ regressor\_: object  <br>  <br>Fitted regressor.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=regressor_,-object) | Ridge | Ridge(alpha=1e-10) |\
| [transformer\_ transformer\_: object  <br>  <br>Transformer used in :meth:\`fit\` and :meth:\`predict\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=transformer_,-object) | FunctionTransformer | FunctionTrans...validate=True) |\
\
Ridge\
\
[?Documentation for Ridge](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alpha alpha: float or array-like of shape (n\_targets,), default=1.0  <br>  <br>Constant that multiplies the L2 term, controlling regularization  <br>strength. \`alpha\` must be a non-negative float i.e. in \`\[0, inf)\`.  <br>  <br>When \`alpha = 0\`, the objective is equivalent to ordinary least  <br>squares, solved by the :class:\`LinearRegression\` object. For numerical  <br>reasons, using \`alpha = 0\` with the \`Ridge\` object is not advised.  <br>Instead, you should use the :class:\`LinearRegression\` object.  <br>  <br>If an array is passed, penalties are assumed to be specific to the  <br>targets. Hence they must correspond in number.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`  <br>for an illustration of the effect of alpha on the model coefficients.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=alpha,-float%20or%20array-like%20of%20shape%20%28n_targets%2C%29%2C%20default%3D1.0) | 1e-10 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to fit the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. \`\`X\`\` and \`\`y\`\` are expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [copy\_X copy\_X: bool, default=True  <br>  <br>If True, X will be copied; else, it may be overwritten.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=copy_X,-bool%2C%20default%3DTrue) | True |\
|     | [max\_iter max\_iter: int, default=None  <br>  <br>Maximum number of iterations for conjugate gradient solver.  <br>For 'sparse\_cg' and 'lsqr' solvers, the default value is determined  <br>by scipy.sparse.linalg. For 'sag' solver, the default value is 1000.  <br>For 'lbfgs' solver, the default value is 15000.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=max_iter,-int%2C%20default%3DNone) | None |\
|     | [tol tol: float, default=1e-4  <br>  <br>The precision of the solution (\`coef\_\`) is determined by \`tol\` which  <br>specifies a different convergence criterion for each solver:  <br>  <br>\- 'svd': \`tol\` has no impact.  <br>  <br>\- 'cholesky': \`tol\` has no impact.  <br>  <br>\- 'sparse\_cg': norm of residuals smaller than \`tol\`.  <br>  <br>\- 'lsqr': \`tol\` is set as atol and btol of scipy.sparse.linalg.lsqr,  <br>which control the norm of the residual vector in terms of the norms of  <br>matrix and coefficients.  <br>  <br>\- 'sag' and 'saga': relative change of coef smaller than \`tol\`.  <br>  <br>\- 'lbfgs': maximum of the absolute (projected) gradient=max\|residuals\|  <br>smaller than \`tol\`.  <br>  <br>.. versionchanged:: 1.2  <br>Default value changed from 1e-3 to 1e-4 for consistency with other linear  <br>models.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [solver solver: {'auto', 'svd', 'cholesky', 'lsqr', 'sparse\_cg', 'sag', 'saga', 'lbfgs'}, default='auto'  <br>  <br>Solver to use in the computational routines:  <br>  <br>\- 'auto' chooses the solver automatically based on the type of data.  <br>  <br>\- 'svd' uses a Singular Value Decomposition of X to compute the Ridge  <br>coefficients. It is the most stable solver, in particular more stable  <br>for singular matrices than 'cholesky' at the cost of being slower.  <br>  <br>\- 'cholesky' uses the standard :func:\`scipy.linalg.solve\` function to  <br>obtain a closed-form solution.  <br>  <br>\- 'sparse\_cg' uses the conjugate gradient solver as found in  <br>:func:\`scipy.sparse.linalg.cg\`. As an iterative algorithm, this solver is  <br>more appropriate than 'cholesky' for large-scale data  <br>(possibility to set \`tol\` and \`max\_iter\`).  <br>  <br>\- 'lsqr' uses the dedicated regularized least-squares routine  <br>:func:\`scipy.sparse.linalg.lsqr\`. It is the fastest and uses an iterative  <br>procedure.  <br>  <br>\- 'sag' uses a Stochastic Average Gradient descent, and 'saga' uses  <br>its improved, unbiased version named SAGA. Both methods also use an  <br>iterative procedure, and are often faster than other solvers when  <br>both n\_samples and n\_features are large. Note that 'sag' and  <br>'saga' fast convergence is only guaranteed on features with  <br>approximately the same scale. You can preprocess the data with a  <br>scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>\- 'lbfgs' uses L-BFGS-B algorithm implemented in  <br>:func:\`scipy.optimize.minimize\`. It can be used only when \`positive\`  <br>is True.  <br>  <br>All solvers except 'svd' support both dense and sparse data. However, only  <br>'lsqr', 'sag', 'sparse\_cg', and 'lbfgs' support sparse input when  <br>\`fit\_intercept\` is True.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient descent solver.  <br>.. versionadded:: 0.19  <br>SAGA solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=solver,-%7B%27auto%27%2C%20%27svd%27%2C%20%27cholesky%27%2C%20%27lsqr%27%2C%20%27sparse_cg%27%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%27sag%27%2C%20%27saga%27%2C%20%27lbfgs%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
|     | [positive positive: bool, default=False  <br>  <br>When set to \`\`True\`\`, forces the coefficients to be positive.  <br>Only 'lbfgs' solver is supported in this case.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=positive,-bool%2C%20default%3DFalse) | False |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Used when \`\`solver\`\` == 'sag' or 'saga' to shuffle the data.  <br>See :term:\`Glossary <random\_state>\` for details.  <br>  <br>.. versionadded:: 0.17  <br>\`random\_state\` to support Stochastic Average Gradient.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [coef\_ coef\_: ndarray of shape (n\_features,) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](19,) | \[-0.01,-0.01, 0.02,..., 0.05, 0.04,-0.03\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.7665 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=n_features_in_,-int) | int | 19  |\
| [n\_iter\_ n\_iter\_: None or ndarray of shape (n\_targets,)  <br>  <br>Actual number of iterations for each target. Available only for  <br>'sag' and 'lsqr' solvers. Other solvers will return None.  <br>  <br>.. versionadded:: 0.17](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=n_iter_,-None%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | NoneType | None |\
| [solver\_ solver\_: str  <br>  <br>The solver that was used at fit time by the computational  <br>routines.  <br>  <br>.. versionadded:: 1.5](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=solver_,-str) | str | 'ch...ky' |\
\
  \
  \
\
Then we check the performance of the computed model by plotting its predictions against the actual values on the test set, and by computing the median absolute error.\
\
from sklearn.metrics import PredictionErrorDisplay, [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
\
mae\_train \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_train, model.predict(X\_train))\
y\_pred \= model.predict(X\_test)\
mae\_test \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_test, y\_pred)\
scores \= {\
    "MedAE on training set": f"{mae\_train:.2f} $/hour",\
    "MedAE on testing set": f"{mae\_test:.2f} $/hour",\
}\
\
Copy to clipboard\
\
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(5, 5))\
display \= [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")\
(\
    y\_test, y\_pred, kind\="actual\_vs\_predicted", ax\=ax, scatter\_kwargs\={"alpha": 0.5}\
)\
ax.set\_title("Ridge model, small regularization")\
for name, score in scores.items():\
    ax.plot(\[\], \[\], " ", label\=f"{name}: {score}")\
ax.legend(loc\="upper left")\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![Ridge model, small regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_002.png)\
\
The model learnt is far from being a good model making accurate predictions: this is obvious when looking at the plot above, where good predictions should lie on the black dashed line.\
\
In the following section, we will interpret the coefficients of the model. While we do so, we should keep in mind that any conclusion we draw is about the model that we build, rather than about the true (real-world) generative process of the data.\
\
Interpreting coefficients: scale matters[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#interpreting-coefficients-scale-matters "Link to this heading")\
\
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
First of all, we can take a look to the values of the coefficients of the regressor we have fitted.\
\
feature\_names \= model\[:\-1\].get\_feature\_names\_out()\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    model\[\-1\].regressor\_.coef\_,\
    columns\=\["Coefficients"\],\
    index\=feature\_names,\
)\
\
coefs\
\
Copy to clipboard\
\
|     | Coefficients |\
| --- | --- |\
| RACE\_Hispanic | \-0.013561 |\
| RACE\_Other | \-0.009117 |\
| RACE\_White | 0.022552 |\
| OCCUPATION\_Clerical | 0.000046 |\
| OCCUPATION\_Management | 0.090529 |\
| OCCUPATION\_Other | \-0.025101 |\
| OCCUPATION\_Professional | 0.071964 |\
| OCCUPATION\_Sales | \-0.046635 |\
| OCCUPATION\_Service | \-0.091052 |\
| SECTOR\_Construction | \-0.000187 |\
| SECTOR\_Manufacturing | 0.031266 |\
| SECTOR\_Other | \-0.031015 |\
| MARR\_Unmarried | \-0.032405 |\
| UNION\_not\_member | \-0.117154 |\
| SEX\_male | 0.090808 |\
| SOUTH\_yes | \-0.033823 |\
| EDUCATION | 0.054699 |\
| EXPERIENCE | 0.035005 |\
| AGE | \-0.030867 |\
\
  \
  \
\
The AGE coefficient is expressed in “dollars/hour per living years” while the EDUCATION one is expressed in “dollars/hour per years of education”. This representation of the coefficients has the benefit of making clear the practical predictions of the model: an increase of 1 year in AGE means a decrease of 0.030867 dollars/hour, while an increase of 1 year in EDUCATION means an increase of 0.054699 dollars/hour. On the other hand, categorical variables (as UNION or SEX) are adimensional numbers taking either the value 0 or 1. Their coefficients are expressed in dollars/hour. Then, we cannot compare the magnitude of different coefficients since the features have different natural scales, and hence value ranges, because of their different unit of measure. This is more visible if we plot the coefficients.\
\
coefs.plot.barh(figsize\=(9, 7))\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Ridge model, small regularization")\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Raw coefficient values")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Ridge model, small regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_003.png)\
\
Indeed, from the plot above the most important factor in determining WAGE appears to be the variable UNION, even if our intuition might tell us that variables like EXPERIENCE should have more impact.\
\
Looking at the coefficient plot to gauge feature importance can be misleading as some of them vary on a small scale, while others, like AGE, varies a lot more, several decades.\
\
This is visible if we compare the standard deviations of different features.\
\
X\_train\_preprocessed \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    model\[:\-1\].transform(X\_train), columns\=feature\_names\
)\
\
X\_train\_preprocessed.std(axis\=0).plot.barh(figsize\=(9, 7))\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Feature ranges")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Std. dev. of feature values")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Feature ranges](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_004.png)\
\
Multiplying the coefficients by the standard deviation of the related feature would reduce all the coefficients to the same unit of measure. As we will see [after](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#scaling-num)\
 this is equivalent to normalize numerical variables to their standard deviation, as y\=∑coefi×Xi\=∑(coefi×stdi)×(Xi/stdi).\
\
In that way, we emphasize that the greater the variance of a feature, the larger the weight of the corresponding coefficient on the output, all else being equal.\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    model\[\-1\].regressor\_.coef\_ \* X\_train\_preprocessed.std(axis\=0),\
    columns\=\["Coefficient importance"\],\
    index\=feature\_names,\
)\
coefs.plot(kind\="barh", figsize\=(9, 7))\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Coefficient values corrected by the feature's std. dev.")\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Ridge model, small regularization")\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Ridge model, small regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_005.png)\
\
Now that the coefficients have been scaled, we can safely compare them.\
\
Note\
\
Why does the plot above suggest that an increase in age leads to a decrease in wage? Why is the [initial pairplot](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#marginal-dependencies)\
 telling the opposite? This difference is the difference between marginal and conditional dependence.\
\
The plot above tells us about dependencies between a specific feature and the target when all other features remain constant, i.e., **conditional dependencies**. An increase of the AGE will induce a decrease of the WAGE when all other features remain constant. On the contrary, an increase of the EXPERIENCE will induce an increase of the WAGE when all other features remain constant. Also, AGE, EXPERIENCE and EDUCATION are the three variables that most influence the model.\
\
Interpreting coefficients: being cautious about causality[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#interpreting-coefficients-being-cautious-about-causality "Link to this heading")\
\
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Linear models are a great tool for measuring statistical association, but we should be cautious when making statements about causality, after all correlation doesn’t always imply causation. This is particularly difficult in the social sciences because the variables we observe only function as proxies for the underlying causal process.\
\
In our particular case we can think of the EDUCATION of an individual as a proxy for their professional aptitude, the real variable we’re interested in but can’t observe. We’d certainly like to think that staying in school for longer would increase technical competency, but it’s also quite possible that causality goes the other way too. That is, those who are technically competent tend to stay in school for longer.\
\
An employer is unlikely to care which case it is (or if it’s a mix of both), as long as they remain convinced that a person with more EDUCATION is better suited for the job, they will be happy to pay out a higher WAGE.\
\
This confounding of effects becomes problematic when thinking about some form of intervention e.g. government subsidies of university degrees or promotional material encouraging individuals to take up higher education. The usefulness of these measures could end up being overstated, especially if the degree of confounding is strong. Our model predicts a 0.054699 increase in hourly wage for each year of education. The actual causal effect might be lower because of this confounding.\
\
Checking the variability of the coefficients[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#checking-the-variability-of-the-coefficients "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
We can check the coefficient variability through cross-validation: it is a form of data perturbation (related to [resampling](https://en.wikipedia.org/wiki/Resampling_(statistics))\
).\
\
If coefficients vary significantly when changing the input dataset their robustness is not guaranteed, and they should probably be interpreted with caution.\
\
from sklearn.model\_selection import [RepeatedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold")\
, [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
\
cv \= [RepeatedKFold](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold")\
(n\_splits\=5, n\_repeats\=5, random\_state\=0)\
cv\_model \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
(\
    model,\
    X,\
    y,\
    cv\=cv,\
    return\_estimator\=True,\
    n\_jobs\=2,\
)\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    \[\
        est\[\-1\].regressor\_.coef\_ \* est\[:\-1\].transform(X.iloc\[train\_idx\]).std(axis\=0)\
        for est, (train\_idx, \_) in zip(cv\_model\["estimator"\], cv.split(X, y))\
    \],\
    columns\=feature\_names,\
)\
\
Copy to clipboard\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
(figsize\=(9, 7))\
[sns.stripplot](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")\
(data\=coefs, orient\="h", palette\="dark:k", alpha\=0.5)\
[sns.boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")\
(data\=coefs, orient\="h", color\="cyan", saturation\=0.5, whis\=10)\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Coefficient importance")\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Coefficient importance and its variability")\
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")\
("Ridge model, small regularization")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Ridge model, small regularization, Coefficient importance and its variability](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_006.png)\
\
The problem of correlated variables[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#the-problem-of-correlated-variables "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
The AGE and EXPERIENCE coefficients are affected by strong variability which might be due to the collinearity between the 2 features: as AGE and EXPERIENCE vary together in the data, their effect is difficult to tease apart.\
\
To verify this interpretation we plot the variability of the AGE and EXPERIENCE coefficient.\
\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Age coefficient")\
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")\
("Experience coefficient")\
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")\
(True)\
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")\
(\-0.4, 0.5)\
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")\
(\-0.4, 0.5)\
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")\
(coefs\["AGE"\], coefs\["EXPERIENCE"\])\
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Co-variations of coefficients for AGE and EXPERIENCE across folds")\
\
Copy to clipboard\
\
![Co-variations of coefficients for AGE and EXPERIENCE across folds](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_007.png)\
\
Two regions are populated: when the EXPERIENCE coefficient is positive the AGE one is negative and vice-versa.\
\
To go further we remove one of the two features, AGE, and check what is the impact on the model stability.\
\
column\_to\_drop \= \["AGE"\]\
\
cv\_model \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
(\
    model,\
    X.drop(columns\=column\_to\_drop),\
    y,\
    cv\=cv,\
    return\_estimator\=True,\
    n\_jobs\=2,\
)\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    \[\
        est\[\-1\].regressor\_.coef\_\
        \* est\[:\-1\].transform(X.drop(columns\=column\_to\_drop).iloc\[train\_idx\]).std(axis\=0)\
        for est, (train\_idx, \_) in zip(cv\_model\["estimator"\], cv.split(X, y))\
    \],\
    columns\=feature\_names\[:\-1\],\
)\
\
Copy to clipboard\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
(figsize\=(9, 7))\
[sns.stripplot](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")\
(data\=coefs, orient\="h", palette\="dark:k", alpha\=0.5)\
[sns.boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")\
(data\=coefs, orient\="h", color\="cyan", saturation\=0.5)\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Coefficient importance and its variability")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Coefficient importance")\
[plt.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle")\
("Ridge model, small regularization, AGE dropped")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Ridge model, small regularization, AGE dropped, Coefficient importance and its variability](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_008.png)\
\
The estimation of the EXPERIENCE coefficient now shows a much reduced variability. EXPERIENCE remains important for all models trained during cross-validation.\
\
Preprocessing numerical variables[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#preprocessing-numerical-variables "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
As said above (see “[The machine-learning pipeline](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#the-pipeline)\
”), we could also choose to scale numerical values before training the model. This can be useful when we apply a similar amount of regularization to all of them in the ridge. The preprocessor is redefined in order to subtract the mean and scale variables to unit variance.\
\
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
\
preprocessor \= [make\_column\_transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")\
(\
    ([OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(drop\="if\_binary"), categorical\_columns),\
    ([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")\
(), numerical\_columns),\
)\
\
Copy to clipboard\
\
The model will stay unchanged.\
\
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    preprocessor,\
    [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")\
(\
        regressor\=[Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")\
(alpha\=1e-10), func\=[np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")\
, inverse\_func\=[sp.special.exp10](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp10.html#scipy.special.exp10 "scipy.special.exp10")\
    ),\
)\
model.fit(X\_train, y\_train)\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(transformers=\[('onehotencoder',\
                                                  OneHotEncoder(drop='if\_binary'),\
                                                  \['RACE', 'OCCUPATION',\
                                                   'SECTOR', 'MARR', 'UNION',\
                                                   'SEX', 'SOUTH'\]),\
                                                 ('standardscaler',\
                                                  StandardScaler(),\
                                                  \['EDUCATION', 'EXPERIENCE',\
                                                   'AGE'\])\])),\
                ('transformedtargetregressor',\
                 TransformedTargetRegressor(func=<ufunc 'log10'>,\
                                            inverse\_func=<ufunc 'exp10'>,\
                                            regressor=Ridge(alpha=1e-10)))\])\
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
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('transformedtargetregressor', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['EDUCATION','SOUTH','SEX',...,'OCCUPATION','SECTOR','MARR'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 10  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('onehotencoder', ...), ('standardscaler', ...)\] |\
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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['EDUCATION','SOUTH','SEX',...,'OCCUPATION','SECTOR','MARR'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 10  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'onehotencod...ndardScaler()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'on...er': slice(0, 16, None), 're...er': slice(0, 0, None), 'st...er': slice(16, 19, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('on...er', OneHotEncoder...p='if\_binary'), \['RACE', 'OC...ON', 'SECTOR', 'MARR', ...\]), ('st...er', StandardScaler(), \['ED...ON', 'EX...CE', 'AGE'\])\] |\
\
onehotencoder\
\
\['RACE', 'OCCUPATION', 'SECTOR', 'MARR', 'UNION', 'SEX', 'SOUTH'\]\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | 'if\_binary' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'error' |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['Hispa... dtype=object), array(\['Cleri... dtype=object), array(\['Const... dtype=object), array(\['Marri... dtype=object), ...\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[object\](7,) | \[None,None,None,...,0,0,0\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](7,) | \['RACE','OCCUPATION','SECTOR',...,'UNION','SEX','SOUTH'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 7   |\
\
16 features\
\
|     |\
| --- |\
| RACE\_Hispanic |\
| RACE\_Other |\
| RACE\_White |\
| OCCUPATION\_Clerical |\
| OCCUPATION\_Management |\
| OCCUPATION\_Other |\
| OCCUPATION\_Professional |\
| OCCUPATION\_Sales |\
| OCCUPATION\_Service |\
| SECTOR\_Construction |\
| SECTOR\_Manufacturing |\
| SECTOR\_Other |\
| MARR\_Unmarried |\
| UNION\_not\_member |\
| SEX\_male |\
| SOUTH\_yes |\
\
standardscaler\
\
\['EDUCATION', 'EXPERIENCE', 'AGE'\]\
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
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['EDUCATION','EXPERIENCE','AGE'\] |\
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[13.04,18.19,37.23\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 3   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 400 |\
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 2.63,12.38,11.76\] |\
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 6.9 ,153.23,138.4 \] |\
\
3 features\
\
|     |\
| --- |\
| EDUCATION |\
| EXPERIENCE |\
| AGE |\
\
19 features\
\
|     |\
| --- |\
| onehotencoder\_\_RACE\_Hispanic |\
| onehotencoder\_\_RACE\_Other |\
| onehotencoder\_\_RACE\_White |\
| onehotencoder\_\_OCCUPATION\_Clerical |\
| onehotencoder\_\_OCCUPATION\_Management |\
| onehotencoder\_\_OCCUPATION\_Other |\
| onehotencoder\_\_OCCUPATION\_Professional |\
| onehotencoder\_\_OCCUPATION\_Sales |\
| onehotencoder\_\_OCCUPATION\_Service |\
| onehotencoder\_\_SECTOR\_Construction |\
| onehotencoder\_\_SECTOR\_Manufacturing |\
| onehotencoder\_\_SECTOR\_Other |\
| onehotencoder\_\_MARR\_Unmarried |\
| onehotencoder\_\_UNION\_not\_member |\
| onehotencoder\_\_SEX\_male |\
| onehotencoder\_\_SOUTH\_yes |\
| standardscaler\_\_EDUCATION |\
| standardscaler\_\_EXPERIENCE |\
| standardscaler\_\_AGE |\
\
transformedtargetregressor: TransformedTargetRegressor\
\
[?Documentation for transformedtargetregressor: TransformedTargetRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [regressor regressor: object, default=None  <br>  <br>Regressor object such as derived from  <br>:class:\`~sklearn.base.RegressorMixin\`. This regressor will  <br>automatically be cloned each time prior to fitting. If \`regressor is  <br>None\`, :class:\`~sklearn.linear\_model.LinearRegression\` is created and used.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=regressor,-object%2C%20default%3DNone) | Ridge(alpha=1e-10) |\
|     | [func func: function, default=None  <br>  <br>Function to apply to \`y\` before passing to :meth:\`fit\`. Cannot be set  <br>at the same time as \`transformer\`. If \`func is None\`, the function used will be  <br>the identity function. If \`func\` is set, \`inverse\_func\` also needs to be  <br>provided. The function needs to return a 2-dimensional array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=func,-function%2C%20default%3DNone) | <ufunc 'log10'> |\
|     | [inverse\_func inverse\_func: function, default=None  <br>  <br>Function to apply to the prediction of the regressor. Cannot be set at  <br>the same time as \`transformer\`. The inverse function is used to return  <br>predictions to the same space of the original training labels. If  <br>\`inverse\_func\` is set, \`func\` also needs to be provided. The inverse  <br>function needs to return a 2-dimensional array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=inverse_func,-function%2C%20default%3DNone) | <ufunc 'exp10'> |\
|     | [transformer transformer: object, default=None  <br>  <br>Estimator object such as derived from  <br>:class:\`~sklearn.base.TransformerMixin\`. Cannot be set at the same time  <br>as \`func\` and \`inverse\_func\`. If \`transformer is None\` as well as  <br>\`func\` and \`inverse\_func\`, the transformer will be an identity  <br>transformer. Note that the transformer will be cloned during fitting.  <br>Also, the transformer is restricting \`y\` to be a numpy array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=transformer,-object%2C%20default%3DNone) | None |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that \`transform\` followed by \`inverse\_transform\`  <br>or \`func\` followed by \`inverse\_func\` leads to the original targets.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying regressor exposes such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=n_features_in_,-int) | int | 19  |\
| [regressor\_ regressor\_: object  <br>  <br>Fitted regressor.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=regressor_,-object) | Ridge | Ridge(alpha=1e-10) |\
| [transformer\_ transformer\_: object  <br>  <br>Transformer used in :meth:\`fit\` and :meth:\`predict\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=transformer_,-object) | FunctionTransformer | FunctionTrans...validate=True) |\
\
Ridge\
\
[?Documentation for Ridge](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alpha alpha: float or array-like of shape (n\_targets,), default=1.0  <br>  <br>Constant that multiplies the L2 term, controlling regularization  <br>strength. \`alpha\` must be a non-negative float i.e. in \`\[0, inf)\`.  <br>  <br>When \`alpha = 0\`, the objective is equivalent to ordinary least  <br>squares, solved by the :class:\`LinearRegression\` object. For numerical  <br>reasons, using \`alpha = 0\` with the \`Ridge\` object is not advised.  <br>Instead, you should use the :class:\`LinearRegression\` object.  <br>  <br>If an array is passed, penalties are assumed to be specific to the  <br>targets. Hence they must correspond in number.  <br>  <br>See :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`  <br>for an illustration of the effect of alpha on the model coefficients.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=alpha,-float%20or%20array-like%20of%20shape%20%28n_targets%2C%29%2C%20default%3D1.0) | 1e-10 |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to fit the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. \`\`X\`\` and \`\`y\`\` are expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [copy\_X copy\_X: bool, default=True  <br>  <br>If True, X will be copied; else, it may be overwritten.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=copy_X,-bool%2C%20default%3DTrue) | True |\
|     | [max\_iter max\_iter: int, default=None  <br>  <br>Maximum number of iterations for conjugate gradient solver.  <br>For 'sparse\_cg' and 'lsqr' solvers, the default value is determined  <br>by scipy.sparse.linalg. For 'sag' solver, the default value is 1000.  <br>For 'lbfgs' solver, the default value is 15000.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=max_iter,-int%2C%20default%3DNone) | None |\
|     | [tol tol: float, default=1e-4  <br>  <br>The precision of the solution (\`coef\_\`) is determined by \`tol\` which  <br>specifies a different convergence criterion for each solver:  <br>  <br>\- 'svd': \`tol\` has no impact.  <br>  <br>\- 'cholesky': \`tol\` has no impact.  <br>  <br>\- 'sparse\_cg': norm of residuals smaller than \`tol\`.  <br>  <br>\- 'lsqr': \`tol\` is set as atol and btol of scipy.sparse.linalg.lsqr,  <br>which control the norm of the residual vector in terms of the norms of  <br>matrix and coefficients.  <br>  <br>\- 'sag' and 'saga': relative change of coef smaller than \`tol\`.  <br>  <br>\- 'lbfgs': maximum of the absolute (projected) gradient=max\|residuals\|  <br>smaller than \`tol\`.  <br>  <br>.. versionchanged:: 1.2  <br>Default value changed from 1e-3 to 1e-4 for consistency with other linear  <br>models.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001 |\
|     | [solver solver: {'auto', 'svd', 'cholesky', 'lsqr', 'sparse\_cg', 'sag', 'saga', 'lbfgs'}, default='auto'  <br>  <br>Solver to use in the computational routines:  <br>  <br>\- 'auto' chooses the solver automatically based on the type of data.  <br>  <br>\- 'svd' uses a Singular Value Decomposition of X to compute the Ridge  <br>coefficients. It is the most stable solver, in particular more stable  <br>for singular matrices than 'cholesky' at the cost of being slower.  <br>  <br>\- 'cholesky' uses the standard :func:\`scipy.linalg.solve\` function to  <br>obtain a closed-form solution.  <br>  <br>\- 'sparse\_cg' uses the conjugate gradient solver as found in  <br>:func:\`scipy.sparse.linalg.cg\`. As an iterative algorithm, this solver is  <br>more appropriate than 'cholesky' for large-scale data  <br>(possibility to set \`tol\` and \`max\_iter\`).  <br>  <br>\- 'lsqr' uses the dedicated regularized least-squares routine  <br>:func:\`scipy.sparse.linalg.lsqr\`. It is the fastest and uses an iterative  <br>procedure.  <br>  <br>\- 'sag' uses a Stochastic Average Gradient descent, and 'saga' uses  <br>its improved, unbiased version named SAGA. Both methods also use an  <br>iterative procedure, and are often faster than other solvers when  <br>both n\_samples and n\_features are large. Note that 'sag' and  <br>'saga' fast convergence is only guaranteed on features with  <br>approximately the same scale. You can preprocess the data with a  <br>scaler from :mod:\`sklearn.preprocessing\`.  <br>  <br>\- 'lbfgs' uses L-BFGS-B algorithm implemented in  <br>:func:\`scipy.optimize.minimize\`. It can be used only when \`positive\`  <br>is True.  <br>  <br>All solvers except 'svd' support both dense and sparse data. However, only  <br>'lsqr', 'sag', 'sparse\_cg', and 'lbfgs' support sparse input when  <br>\`fit\_intercept\` is True.  <br>  <br>.. versionadded:: 0.17  <br>Stochastic Average Gradient descent solver.  <br>.. versionadded:: 0.19  <br>SAGA solver.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=solver,-%7B%27auto%27%2C%20%27svd%27%2C%20%27cholesky%27%2C%20%27lsqr%27%2C%20%27sparse_cg%27%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%27sag%27%2C%20%27saga%27%2C%20%27lbfgs%27%7D%2C%20default%3D%27auto%27) | 'auto' |\
|     | [positive positive: bool, default=False  <br>  <br>When set to \`\`True\`\`, forces the coefficients to be positive.  <br>Only 'lbfgs' solver is supported in this case.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=positive,-bool%2C%20default%3DFalse) | False |\
|     | [random\_state random\_state: int, RandomState instance, default=None  <br>  <br>Used when \`\`solver\`\` == 'sag' or 'saga' to shuffle the data.  <br>See :term:\`Glossary <random\_state>\` for details.  <br>  <br>.. versionadded:: 0.17  <br>\`random\_state\` to support Stochastic Average Gradient.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | None |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [coef\_ coef\_: ndarray of shape (n\_features,) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](19,) | \[-0.01,-0.01, 0.02,..., 0.14, 0.43,-0.36\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.9677 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=n_features_in_,-int) | int | 19  |\
| [n\_iter\_ n\_iter\_: None or ndarray of shape (n\_targets,)  <br>  <br>Actual number of iterations for each target. Available only for  <br>'sag' and 'lsqr' solvers. Other solvers will return None.  <br>  <br>.. versionadded:: 0.17](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=n_iter_,-None%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | NoneType | None |\
| [solver\_ solver\_: str  <br>  <br>The solver that was used at fit time by the computational  <br>routines.  <br>  <br>.. versionadded:: 1.5](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.Ridge.html#:~:text=solver_,-str) | str | 'ch...ky' |\
\
  \
  \
\
Again, we check the performance of the computed model using the median absolute error.\
\
mae\_train \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_train, model.predict(X\_train))\
y\_pred \= model.predict(X\_test)\
mae\_test \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_test, y\_pred)\
scores \= {\
    "MedAE on training set": f"{mae\_train:.2f} $/hour",\
    "MedAE on testing set": f"{mae\_test:.2f} $/hour",\
}\
\
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(5, 5))\
display \= [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")\
(\
    y\_test, y\_pred, kind\="actual\_vs\_predicted", ax\=ax, scatter\_kwargs\={"alpha": 0.5}\
)\
ax.set\_title("Ridge model, small regularization")\
for name, score in scores.items():\
    ax.plot(\[\], \[\], " ", label\=f"{name}: {score}")\
ax.legend(loc\="upper left")\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![Ridge model, small regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_009.png)\
\
For the coefficient analysis, scaling is not needed this time because it was performed during the preprocessing step.\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    model\[\-1\].regressor\_.coef\_,\
    columns\=\["Coefficients importance"\],\
    index\=feature\_names,\
)\
coefs.plot.barh(figsize\=(9, 7))\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Ridge model, small regularization, normalized variables")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Raw coefficient values")\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Ridge model, small regularization, normalized variables](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_010.png)\
\
We now inspect the coefficients across several cross-validation folds.\
\
cv\_model \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
(\
    model,\
    X,\
    y,\
    cv\=cv,\
    return\_estimator\=True,\
    n\_jobs\=2,\
)\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    \[est\[\-1\].regressor\_.coef\_ for est in cv\_model\["estimator"\]\], columns\=feature\_names\
)\
\
Copy to clipboard\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
(figsize\=(9, 7))\
[sns.stripplot](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")\
(data\=coefs, orient\="h", palette\="dark:k", alpha\=0.5)\
[sns.boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")\
(data\=coefs, orient\="h", color\="cyan", saturation\=0.5, whis\=10)\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Coefficient variability")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Coefficient variability](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_011.png)\
\
The result is quite similar to the non-normalized case.\
\
Linear models with regularization[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#linear-models-with-regularization "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
In machine-learning practice, ridge regression is more often used with non-negligible regularization.\
\
Above, we limited this regularization to a very little amount. Regularization improves the conditioning of the problem and reduces the variance of the estimates. [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
 applies cross validation in order to determine which value of the regularization parameter (`alpha`) is best suited for prediction.\
\
from sklearn.linear\_model import [RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
\
alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-10, 10, 21)  \# alpha values to be chosen from by cross-validation\
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    preprocessor,\
    [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")\
(\
        regressor\=[RidgeCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")\
(alphas\=alphas),\
        func\=[np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")\
,\
        inverse\_func\=[sp.special.exp10](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp10.html#scipy.special.exp10 "scipy.special.exp10")\
,\
    ),\
)\
model.fit(X\_train, y\_train)\
\
Copy to clipboard\
\
Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(transformers=\[('onehotencoder',\
                                                  OneHotEncoder(drop='if\_binary'),\
                                                  \['RACE', 'OCCUPATION',\
                                                   'SECTOR', 'MARR', 'UNION',\
                                                   'SEX', 'SOUTH'\]),\
                                                 ('standardscaler',\
                                                  StandardScaler(),\
                                                  \['EDUCATION', 'EXPERIENCE',\
                                                   'AGE'\])\])),\
                ('transformedtargetregressor',\
                 TransformedTargetRegressor(func=<ufunc 'log10'>,\
                                            inverse\_func=<ufunc 'exp10'>,\
                                            regressor=RidgeCV(alphas=array(\[1.e-10, 1.e-09, 1.e-08, 1.e-07, 1.e-06, 1.e-05, 1.e-04, 1.e-03,\
       1.e-02, 1.e-01, 1.e+00, 1.e+01, 1.e+02, 1.e+03, 1.e+04, 1.e+05,\
       1.e+06, 1.e+07, 1.e+08, 1.e+09, 1.e+10\]))))\])\
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
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('transformedtargetregressor', ...)\] |\
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |\
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |\
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Only defined if the  <br>underlying estimator exposes such an attribute when fit.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['EDUCATION','SOUTH','SEX',...,'OCCUPATION','SECTOR','MARR'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying first estimator in \`steps\` exposes such an attribute  <br>when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=n_features_in_,-int) | int | 10  |\
\
columntransformer: ColumnTransformer\
\
[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('onehotencoder', ...), ('standardscaler', ...)\] |\
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
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](10,) | \['EDUCATION','SOUTH','SEX',...,'OCCUPATION','SECTOR','MARR'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying transformers expose such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_features_in_,-int) | int | 10  |\
| [named\_transformers\_ named\_transformers\_: :class:\`~sklearn.utils.Bunch\`  <br>  <br>Read-only attribute to access any transformer by given name.  <br>Keys are transformer names and values are the fitted transformer  <br>objects.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=named_transformers_,-%3Aclass%3A~sklearn.utils.Bunch) | Bunch | {'onehotencod...ndardScaler()} |\
| [output\_indices\_ output\_indices\_: dict  <br>  <br>A dictionary from each transformer name to a slice, where the slice  <br>corresponds to indices in the transformed output. This is useful to  <br>inspect which transformer is responsible for which transformed  <br>feature(s).  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=output_indices_,-dict) | dict | {'on...er': slice(0, 16, None), 're...er': slice(0, 0, None), 'st...er': slice(16, 19, None)} |\
| [sparse\_output\_ sparse\_output\_: bool  <br>  <br>Boolean flag indicating whether the output of \`\`transform\`\` is a  <br>sparse matrix or a dense numpy array, which depends on the output  <br>of the individual transformers and the \`sparse\_threshold\` keyword.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_output_,-bool) | bool | False |\
| [transformers\_ transformers\_: list  <br>  <br>The collection of fitted transformers as tuples of (name,  <br>fitted\_transformer, column). \`fitted\_transformer\` can be an estimator,  <br>or \`'drop'\`; \`'passthrough'\` is replaced with an equivalent  <br>:class:\`~sklearn.preprocessing.FunctionTransformer\`. In case there were  <br>no columns selected, this will be the unfitted transformer. If there  <br>are remaining columns, the final element is a tuple of the form:  <br>('remainder', transformer, remaining\_columns) corresponding to the  <br>\`\`remainder\`\` parameter. If there are remaining columns, then  <br>\`\`len(transformers\_)==len(transformers)+1\`\`, otherwise  <br>\`\`len(transformers\_)==len(transformers)\`\`.  <br>  <br>.. versionadded:: 1.7  <br>The format of the remaining columns now attempts to match that of the other  <br>transformers: if all columns were provided as column names (\`str\`), the  <br>remaining columns are stored as column names; if all columns were provided  <br>as mask arrays (\`bool\`), so are the remaining columns; in all other cases  <br>the remaining columns are stored as indices (\`int\`).](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers_,-list) | list | \[('on...er', OneHotEncoder...p='if\_binary'), \['RACE', 'OC...ON', 'SECTOR', 'MARR', ...\]), ('st...er', StandardScaler(), \['ED...ON', 'EX...CE', 'AGE'\])\] |\
\
onehotencoder\
\
\['RACE', 'OCCUPATION', 'SECTOR', 'MARR', 'UNION', 'SEX', 'SOUTH'\]\
\
OneHotEncoder\
\
[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | 'if\_binary' |\
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |\
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |\
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |\
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'error' |\
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |\
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |\
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [categories\_ categories\_: list of arrays  <br>  <br>The categories of each feature determined during fitting  <br>(in order of the features in X and corresponding with the output  <br>of \`\`transform\`\`). This includes the category specified in \`\`drop\`\`  <br>(if any).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories_,-list%20of%20arrays) | list | \[array(\['Hispa... dtype=object), array(\['Cleri... dtype=object), array(\['Const... dtype=object), array(\['Marri... dtype=object), ...\] |\
| [drop\_idx\_ drop\_idx\_: array of shape (n\_features,)  <br>  <br>\- \`\`drop\_idx\_\[i\]\`\` is the index in \`\`categories\_\[i\]\`\` of the category  <br>to be dropped for each feature.  <br>\- \`\`drop\_idx\_\[i\] = None\`\` if no category is to be dropped from the  <br>feature with index \`\`i\`\`, e.g. when \`drop='if\_binary'\` and the  <br>feature isn't binary.  <br>\- \`\`drop\_idx\_ = None\`\` if all the transformed features will be  <br>retained.  <br>  <br>If infrequent categories are enabled by setting \`min\_frequency\` or  <br>\`max\_categories\` to a non-default value and \`drop\_idx\[i\]\` corresponds  <br>to an infrequent category, then the entire infrequent category is  <br>dropped.  <br>  <br>.. versionchanged:: 0.23  <br>Added the possibility to contain \`None\` values.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop_idx_,-array%20of%20shape%20%28n_features%2C%29) | ndarray\[object\](7,) | \[None,None,None,...,0,0,0\] |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](7,) | \['RACE','OCCUPATION','SECTOR',...,'UNION','SEX','SOUTH'\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=n_features_in_,-int) | int | 7   |\
\
16 features\
\
|     |\
| --- |\
| RACE\_Hispanic |\
| RACE\_Other |\
| RACE\_White |\
| OCCUPATION\_Clerical |\
| OCCUPATION\_Management |\
| OCCUPATION\_Other |\
| OCCUPATION\_Professional |\
| OCCUPATION\_Sales |\
| OCCUPATION\_Service |\
| SECTOR\_Construction |\
| SECTOR\_Manufacturing |\
| SECTOR\_Other |\
| MARR\_Unmarried |\
| UNION\_not\_member |\
| SEX\_male |\
| SOUTH\_yes |\
\
standardscaler\
\
\['EDUCATION', 'EXPERIENCE', 'AGE'\]\
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
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [feature\_names\_in\_ feature\_names\_in\_: ndarray of shape (\`n\_features\_in\_\`,)  <br>  <br>Names of features seen during :term:\`fit\`. Defined only when \`X\`  <br>has feature names that are all strings.  <br>  <br>.. versionadded:: 1.0](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=feature_names_in_,-ndarray%20of%20shape%20%28n_features_in_%2C%29) | ndarray\[object\](3,) | \['EDUCATION','EXPERIENCE','AGE'\] |\
| [mean\_ mean\_: ndarray of shape (n\_features,) or None  <br>  <br>The mean value for each feature in the training set.  <br>Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and \`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=mean_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[13.04,18.19,37.23\] |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_features_in_,-int) | int | 3   |\
| [n\_samples\_seen\_ n\_samples\_seen\_: int or ndarray of shape (n\_features,)  <br>  <br>The number of samples processed by the estimator for each feature.  <br>If there are no missing samples, the \`\`n\_samples\_seen\`\` will be an  <br>integer, otherwise it will be an array of dtype int. If  <br>\`sample\_weights\` are used it will be a float (if no missing data)  <br>or an array of dtype float that sums the weights seen so far.  <br>Will be reset on new calls to fit, but increments across  <br>\`\`partial\_fit\`\` calls.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=n_samples_seen_,-int%20or%20ndarray%20of%20shape%20%28n_features%2C%29) | float64 | 400 |\
| [scale\_ scale\_: ndarray of shape (n\_features,) or None  <br>  <br>Per feature relative scaling of the data to achieve zero mean and unit  <br>variance. Generally this is calculated using \`np.sqrt(var\_)\`. If a  <br>variance is zero, we can't achieve unit variance, and the data is left  <br>as-is, giving a scaling factor of 1. \`scale\_\` is equal to \`None\`  <br>when \`with\_std=False\`.  <br>  <br>.. versionadded:: 0.17  <br>\*scale\_\*](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=scale_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 2.63,12.38,11.76\] |\
| [var\_ var\_: ndarray of shape (n\_features,) or None  <br>  <br>The variance for each feature in the training set. Used to compute  <br>\`scale\_\`. Equal to \`\`None\`\` when \`\`with\_mean=False\`\` and  <br>\`\`with\_std=False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=var_,-ndarray%20of%20shape%20%28n_features%2C%29%20or%20None) | ndarray\[float64\](3,) | \[ 6.9 ,153.23,138.4 \] |\
\
3 features\
\
|     |\
| --- |\
| EDUCATION |\
| EXPERIENCE |\
| AGE |\
\
19 features\
\
|     |\
| --- |\
| onehotencoder\_\_RACE\_Hispanic |\
| onehotencoder\_\_RACE\_Other |\
| onehotencoder\_\_RACE\_White |\
| onehotencoder\_\_OCCUPATION\_Clerical |\
| onehotencoder\_\_OCCUPATION\_Management |\
| onehotencoder\_\_OCCUPATION\_Other |\
| onehotencoder\_\_OCCUPATION\_Professional |\
| onehotencoder\_\_OCCUPATION\_Sales |\
| onehotencoder\_\_OCCUPATION\_Service |\
| onehotencoder\_\_SECTOR\_Construction |\
| onehotencoder\_\_SECTOR\_Manufacturing |\
| onehotencoder\_\_SECTOR\_Other |\
| onehotencoder\_\_MARR\_Unmarried |\
| onehotencoder\_\_UNION\_not\_member |\
| onehotencoder\_\_SEX\_male |\
| onehotencoder\_\_SOUTH\_yes |\
| standardscaler\_\_EDUCATION |\
| standardscaler\_\_EXPERIENCE |\
| standardscaler\_\_AGE |\
\
transformedtargetregressor: TransformedTargetRegressor\
\
[?Documentation for transformedtargetregressor: TransformedTargetRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [regressor regressor: object, default=None  <br>  <br>Regressor object such as derived from  <br>:class:\`~sklearn.base.RegressorMixin\`. This regressor will  <br>automatically be cloned each time prior to fitting. If \`regressor is  <br>None\`, :class:\`~sklearn.linear\_model.LinearRegression\` is created and used.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=regressor,-object%2C%20default%3DNone) | RidgeCV(alpha...+09, 1.e+10\])) |\
|     | [func func: function, default=None  <br>  <br>Function to apply to \`y\` before passing to :meth:\`fit\`. Cannot be set  <br>at the same time as \`transformer\`. If \`func is None\`, the function used will be  <br>the identity function. If \`func\` is set, \`inverse\_func\` also needs to be  <br>provided. The function needs to return a 2-dimensional array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=func,-function%2C%20default%3DNone) | <ufunc 'log10'> |\
|     | [inverse\_func inverse\_func: function, default=None  <br>  <br>Function to apply to the prediction of the regressor. Cannot be set at  <br>the same time as \`transformer\`. The inverse function is used to return  <br>predictions to the same space of the original training labels. If  <br>\`inverse\_func\` is set, \`func\` also needs to be provided. The inverse  <br>function needs to return a 2-dimensional array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=inverse_func,-function%2C%20default%3DNone) | <ufunc 'exp10'> |\
|     | [transformer transformer: object, default=None  <br>  <br>Estimator object such as derived from  <br>:class:\`~sklearn.base.TransformerMixin\`. Cannot be set at the same time  <br>as \`func\` and \`inverse\_func\`. If \`transformer is None\` as well as  <br>\`func\` and \`inverse\_func\`, the transformer will be an identity  <br>transformer. Note that the transformer will be cloned during fitting.  <br>Also, the transformer is restricting \`y\` to be a numpy array.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=transformer,-object%2C%20default%3DNone) | None |\
|     | [check\_inverse check\_inverse: bool, default=True  <br>  <br>Whether to check that \`transform\` followed by \`inverse\_transform\`  <br>or \`func\` followed by \`inverse\_func\` leads to the original targets.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=check_inverse,-bool%2C%20default%3DTrue) | True |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`. Only defined if the  <br>underlying regressor exposes such an attribute when fit.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=n_features_in_,-int) | int | 19  |\
| [regressor\_ regressor\_: object  <br>  <br>Fitted regressor.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=regressor_,-object) | RidgeCV | RidgeCV(alpha...+09, 1.e+10\])) |\
| [transformer\_ transformer\_: object  <br>  <br>Transformer used in :meth:\`fit\` and :meth:\`predict\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.TransformedTargetRegressor.html#:~:text=transformer_,-object) | FunctionTransformer | FunctionTrans...validate=True) |\
\
RidgeCV\
\
[?Documentation for RidgeCV](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html)\
\
Parameters\
\
|     |     |     |\
| --- | --- | --- |\
|     | [alphas alphas: array-like of shape (n\_alphas,), default=(0.1, 1.0, 10.0)  <br>  <br>Array of alpha values to try.  <br>Regularization strength; must be a positive float. Regularization  <br>improves the conditioning of the problem and reduces the variance of  <br>the estimates. Larger values specify stronger regularization.  <br>Alpha corresponds to \`\`1 / (2C)\`\` in other linear models such as  <br>:class:\`~sklearn.linear\_model.LogisticRegression\` or  <br>:class:\`~sklearn.svm.LinearSVC\`.  <br>If using Leave-One-Out cross-validation, alphas must be strictly positive.  <br>  <br>For an example on how regularization strength affects the model coefficients,  <br>see :ref:\`sphx\_glr\_auto\_examples\_linear\_model\_plot\_ridge\_coeffs.py\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alphas,-array-like%20of%20shape%20%28n_alphas%2C%29%2C%20default%3D%280.1%2C%201.0%2C%2010.0%29) | array(\[1.e-10...e+09, 1.e+10\]) |\
|     | [fit\_intercept fit\_intercept: bool, default=True  <br>  <br>Whether to calculate the intercept for this model. If set  <br>to false, no intercept will be used in calculations  <br>(i.e. data is expected to be centered).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True |\
|     | [scoring scoring: str, callable, default=None  <br>  <br>The scoring method to use for cross-validation. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: negative :ref:\`mean squared error <mean\_squared\_error>\` if cv is  <br>None (i.e. when using leave-one-out cross-validation), or  <br>:ref:\`coefficient of determination <r2\_score>\` (:math:\`R^2\`) otherwise.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=scoring,-str%2C%20callable%2C%20default%3DNone) | None |\
|     | [cv cv: int, cross-validation generator or an iterable, default=None  <br>  <br>Determines the cross-validation splitting strategy.  <br>Possible inputs for cv are:  <br>  <br>\- None, to use the efficient Leave-One-Out cross-validation  <br>\- integer, to specify the number of folds,  <br>\- :term:\`CV splitter\`,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`\`y\`\` is binary or multiclass,  <br>:class:\`~sklearn.model\_selection.StratifiedKFold\` is used, else,  <br>:class:\`~sklearn.model\_selection.KFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for the various  <br>cross-validation strategies that can be used here.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3DNone) | None |\
|     | [gcv\_mode gcv\_mode: {'auto', 'svd', 'eigen'}, default='auto'  <br>  <br>Flag indicating which strategy to use when performing  <br>Leave-One-Out Cross-Validation. Options are::  <br>  <br>'auto' : same as 'eigen'  <br>'svd' : use singular value decomposition of X when X is dense,  <br>fallback to 'eigen' when X is sparse  <br>'eigen' : use eigendecomposition of X X' when n\_samples <= n\_features  <br>or X' X when n\_features < n\_samples  <br>  <br>The 'auto' mode is the default and is intended to pick the cheaper  <br>option depending on the shape and sparsity of the training data.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=gcv_mode,-%7B%27auto%27%2C%20%27svd%27%2C%20%27eigen%27%7D%2C%20default%3D%27auto%27) | None |\
|     | [store\_cv\_results store\_cv\_results: bool, default=False  <br>  <br>Flag indicating if the cross-validation values corresponding to  <br>each alpha should be stored in the \`\`cv\_results\_\`\` attribute (see  <br>below). This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionchanged:: 1.5  <br>Parameter name changed from \`store\_cv\_values\` to \`store\_cv\_results\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=store_cv_results,-bool%2C%20default%3DFalse) | False |\
|     | [alpha\_per\_target alpha\_per\_target: bool, default=False  <br>  <br>Flag indicating whether to optimize the alpha value (picked from the  <br>\`alphas\` parameter list) for each target separately (for multi-output  <br>settings: multiple prediction targets). When set to \`True\`, after  <br>fitting, the \`alpha\_\` attribute will contain a value for each target.  <br>When set to \`False\`, a single alpha is used for all targets.  <br>This flag is only compatible with \`\`cv=None\`\` (i.e. using  <br>Leave-One-Out Cross-Validation).  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_per_target,-bool%2C%20default%3DFalse) | False |\
\
Fitted attributes\
\
| Name | Type | Value |\
| --- | --- | --- |\
| [alpha\_ alpha\_: float or ndarray of shape (n\_targets,)  <br>  <br>Estimated regularization parameter, or, if \`\`alpha\_per\_target=True\`\`,  <br>the estimated regularization parameter for each target.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=alpha_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float | 10  |\
| [best\_score\_ best\_score\_: float or ndarray of shape (n\_targets,)  <br>  <br>Score of base estimator with best alpha, or, if  <br>\`\`alpha\_per\_target=True\`\`, a score for each target.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=best_score_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | \-0.03611 |\
| [coef\_ coef\_: ndarray of shape (n\_features) or (n\_targets, n\_features)  <br>  <br>Weight vector(s).](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=coef_,-ndarray%20of%20shape%20%28n_features%29%20or%20%28n_targets%2C%20n_features%29) | ndarray\[float64\](19,) | \[-0.01,-0.01, 0.02,..., 0.06, 0.02, 0.03\] |\
| [intercept\_ intercept\_: float or ndarray of shape (n\_targets,)  <br>  <br>Independent term in decision function. Set to 0.0 if  <br>\`\`fit\_intercept = False\`\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=intercept_,-float%20or%20ndarray%20of%20shape%20%28n_targets%2C%29) | float64 | 0.9579 |\
| [n\_features\_in\_ n\_features\_in\_: int  <br>  <br>Number of features seen during :term:\`fit\`.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.linear_model.RidgeCV.html#:~:text=n_features_in_,-int) | int | 19  |\
\
  \
  \
\
First we check which value of α has been selected.\
\
model\[\-1\].regressor\_.alpha\_\
\
Copy to clipboard\
\
10.0\
\
Copy to clipboard\
\
Then we check the quality of the predictions.\
\
mae\_train \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_train, model.predict(X\_train))\
y\_pred \= model.predict(X\_test)\
mae\_test \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_test, y\_pred)\
scores \= {\
    "MedAE on training set": f"{mae\_train:.2f} $/hour",\
    "MedAE on testing set": f"{mae\_test:.2f} $/hour",\
}\
\
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(5, 5))\
display \= [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")\
(\
    y\_test, y\_pred, kind\="actual\_vs\_predicted", ax\=ax, scatter\_kwargs\={"alpha": 0.5}\
)\
ax.set\_title("Ridge model, optimum regularization")\
for name, score in scores.items():\
    ax.plot(\[\], \[\], " ", label\=f"{name}: {score}")\
ax.legend(loc\="upper left")\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![Ridge model, optimum regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_012.png)\
\
The ability to reproduce the data of the regularized model is similar to the one of the non-regularized model.\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    model\[\-1\].regressor\_.coef\_,\
    columns\=\["Coefficients importance"\],\
    index\=feature\_names,\
)\
coefs.plot.barh(figsize\=(9, 7))\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Ridge model, with regularization, normalized variables")\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Raw coefficient values")\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Ridge model, with regularization, normalized variables](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_013.png)\
\
The coefficients are significantly different. AGE and EXPERIENCE coefficients are both positive but they now have less influence on the prediction.\
\
The regularization reduces the influence of correlated variables on the model because the weight is shared between the two predictive variables, so neither alone would have strong weights.\
\
On the other hand, the weights obtained with regularization are more stable (see the [Ridge regression and classification](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)\
 User Guide section). This increased stability is visible from the plot, obtained from data perturbations, in a cross-validation. This plot can be compared with the [previous one](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#covariation)\
.\
\
cv\_model \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
(\
    model,\
    X,\
    y,\
    cv\=cv,\
    return\_estimator\=True,\
    n\_jobs\=2,\
)\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    \[est\[\-1\].regressor\_.coef\_ for est in cv\_model\["estimator"\]\], columns\=feature\_names\
)\
\
Copy to clipboard\
\
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")\
("Age coefficient")\
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")\
("Experience coefficient")\
[plt.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid")\
(True)\
[plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")\
(\-0.4, 0.5)\
[plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")\
(\-0.4, 0.5)\
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")\
(coefs\["AGE"\], coefs\["EXPERIENCE"\])\
\_ \= [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Co-variations of coefficients for AGE and EXPERIENCE across folds")\
\
Copy to clipboard\
\
![Co-variations of coefficients for AGE and EXPERIENCE across folds](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_014.png)\
\
Linear models with sparse coefficients[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#linear-models-with-sparse-coefficients "Link to this heading")\
\
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Another possibility to take into account correlated variables in the dataset, is to estimate sparse coefficients. In some way we already did it manually when we dropped the AGE column in a previous ridge estimation.\
\
Lasso models (see the [Lasso](https://scikit-learn.org/stable/modules/linear_model.html#lasso)\
 User Guide section) estimates sparse coefficients. [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")\
 applies cross validation in order to determine which value of the regularization parameter (`alpha`) is best suited for the model estimation.\
\
from sklearn.linear\_model import [LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")\
\
alphas \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")\
(\-10, 10, 21)  \# alpha values to be chosen from by cross-validation\
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")\
(\
    preprocessor,\
    [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")\
(\
        regressor\=[LassoCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")\
(alphas\=alphas, max\_iter\=100\_000),\
        func\=[np.log10](https://numpy.org/doc/stable/reference/generated/numpy.log10.html#numpy.log10 "numpy.log10")\
,\
        inverse\_func\=[sp.special.exp10](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.exp10.html#scipy.special.exp10 "scipy.special.exp10")\
,\
    ),\
)\
\
\_ \= model.fit(X\_train, y\_train)\
\
Copy to clipboard\
\
First we verify which value of α has been selected.\
\
model\[\-1\].regressor\_.alpha\_\
\
Copy to clipboard\
\
np.float64(0.001)\
\
Copy to clipboard\
\
Then we check the quality of the predictions.\
\
mae\_train \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_train, model.predict(X\_train))\
y\_pred \= model.predict(X\_test)\
mae\_test \= [median\_absolute\_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
(y\_test, y\_pred)\
scores \= {\
    "MedAE on training set": f"{mae\_train:.2f} $/hour",\
    "MedAE on testing set": f"{mae\_test:.2f} $/hour",\
}\
\
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(figsize\=(6, 6))\
display \= [PredictionErrorDisplay.from\_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay.from_predictions "sklearn.metrics.PredictionErrorDisplay.from_predictions")\
(\
    y\_test, y\_pred, kind\="actual\_vs\_predicted", ax\=ax, scatter\_kwargs\={"alpha": 0.5}\
)\
ax.set\_title("Lasso model, optimum regularization")\
for name, score in scores.items():\
    ax.plot(\[\], \[\], " ", label\=f"{name}: {score}")\
ax.legend(loc\="upper left")\
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")\
()\
\
Copy to clipboard\
\
![Lasso model, optimum regularization](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_015.png)\
\
For our dataset, again the model is not very predictive.\
\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    model\[\-1\].regressor\_.coef\_,\
    columns\=\["Coefficients importance"\],\
    index\=feature\_names,\
)\
coefs.plot(kind\="barh", figsize\=(9, 7))\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Lasso model, optimum regularization, normalized variables")\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Lasso model, optimum regularization, normalized variables](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_016.png)\
\
A Lasso model identifies the correlation between AGE and EXPERIENCE and suppresses one of them for the sake of the prediction.\
\
It is important to keep in mind that the coefficients that have been dropped may still be related to the outcome by themselves: the model chose to suppress them because they bring little or no additional information on top of the other features. Additionally, this selection is unstable for correlated features, and should be interpreted with caution.\
\
Indeed, we can check the variability of the coefficients across folds.\
\
cv\_model \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")\
(\
    model,\
    X,\
    y,\
    cv\=cv,\
    return\_estimator\=True,\
    n\_jobs\=2,\
)\
coefs \= [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(\
    \[est\[\-1\].regressor\_.coef\_ for est in cv\_model\["estimator"\]\], columns\=feature\_names\
)\
\
Copy to clipboard\
\
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")\
(figsize\=(9, 7))\
[sns.stripplot](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot "seaborn.stripplot")\
(data\=coefs, orient\="h", palette\="dark:k", alpha\=0.5)\
[sns.boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot "seaborn.boxplot")\
(data\=coefs, orient\="h", color\="cyan", saturation\=0.5, whis\=100)\
[plt.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline")\
(x\=0, color\=".5")\
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")\
("Coefficient variability")\
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")\
(left\=0.3)\
\
Copy to clipboard\
\
![Coefficient variability](https://scikit-learn.org/stable/_images/sphx_glr_plot_linear_model_coefficient_interpretation_017.png)\
\
We observe that the AGE and EXPERIENCE coefficients are varying a lot depending of the fold.\
\
Wrong causal interpretation[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#wrong-causal-interpretation "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
Policy makers might want to know the effect of education on wage to assess whether or not a certain policy designed to entice people to pursue more education would make economic sense. While Machine Learning models are great for measuring statistical associations, they are generally unable to infer causal effects.\
\
It might be tempting to look at the coefficient of education on wage from our last model (or any model for that matter) and conclude that it captures the true effect of a change in the standardized education variable on wages.\
\
Unfortunately there are likely unobserved confounding variables that either inflate or deflate that coefficient. A confounding variable is a variable that causes both EDUCATION and WAGE. One example of such variable is ability. Presumably, more able people are more likely to pursue education while at the same time being more likely to earn a higher hourly wage at any level of education. In this case, ability induces a positive [Omitted Variable Bias](https://en.wikipedia.org/wiki/Omitted-variable_bias)\
 (OVB) on the EDUCATION coefficient, thereby exaggerating the effect of education on wages.\
\
See the [Failure of Machine Learning to infer causal effects](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html#sphx-glr-auto-examples-inspection-plot-causal-interpretation-py)\
 for a simulated case of ability OVB.\
\
Lessons learned[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#lessons-learned "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
*   Coefficients must be scaled to the same unit of measure to retrieve feature importance. Scaling them with the standard-deviation of the feature is a useful proxy.\
    \
*   Coefficients in multivariate linear models represent the dependency between a given feature and the target, **conditional** on the other features.\
    \
*   Correlated features induce instabilities in the coefficients of linear models and their effects cannot be well teased apart.\
    \
*   Different linear models respond differently to feature correlation and coefficients could significantly vary from one another.\
    \
*   Inspecting coefficients across the folds of a cross-validation loop gives an idea of their stability.\
    \
*   Interpreting causality is difficult when there are confounding effects. If the relationship between two variables is also affected by something unobserved, we should be careful when making conclusions about causality.\
    \
\
**Total running time of the script:** (0 minutes 13.587 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_linear_model_coefficient_interpretation.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_linear_model_coefficient_interpretation.ipynb)\
\
[`Download Jupyter notebook: plot_linear_model_coefficient_interpretation.ipynb`](https://scikit-learn.org/stable/_downloads/cf0f90f46eb559facf7f63f124f61e04/plot_linear_model_coefficient_interpretation.ipynb)\
\
[`Download Python source code: plot_linear_model_coefficient_interpretation.py`](https://scikit-learn.org/stable/_downloads/521b554adefca348463adbbe047d7e99/plot_linear_model_coefficient_interpretation.py)\
\
[`Download zipped: plot_linear_model_coefficient_interpretation.zip`](https://scikit-learn.org/stable/_downloads/11651f4eebcf15ff7959e210e82dc45c/plot_linear_model_coefficient_interpretation.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_coeffs_thumb.png)\
\
[Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html)\
\
Ridge coefficients as a function of the L2 Regularization\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_causal_interpretation_thumb.png)\
\
[Failure of Machine Learning to infer causal effects](https://scikit-learn.org/stable/auto_examples/inspection/plot_causal_interpretation.html)\
\
Failure of Machine Learning to infer causal effects\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_thumb.png)\
\
[Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)\
\
Plot Ridge coefficients as a function of the regularization\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_train_error_vs_test_error_thumb.png)\
\
[Effect of model regularization on training and test error](https://scikit-learn.org/stable/auto_examples/model_selection/plot_train_error_vs_test_error.html)\
\
Effect of model regularization on training and test error\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/521b554adefca348463adbbe047d7e99/plot_linear_model_coefficient_interpretation.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/cf0f90f46eb559facf7f63f124f61e04/plot_linear_model_coefficient_interpretation.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/11651f4eebcf15ff7959e210e82dc45c/plot_linear_model_coefficient_interpretation.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_linear_model_coefficient_interpretation.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_linear_model_coefficient_interpretation.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)