[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_target_encoder.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_target_encoder.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_target_encoder.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_target_encoder.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_target_encoder.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_target_encoder.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#sphx-glr-download-auto-examples-preprocessing-plot-target-encoder-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Comparing Target Encoder with Other Encoders[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#comparing-target-encoder-with-other-encoders "Link to this heading")

==========================================================================================================================================================================================================

The [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
 uses the value of the target to encode each categorical feature. In this example, we will compare three different approaches for handling categorical features: [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")
, [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
, [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 and dropping the category.

Note

`fit(X, y).transform(X)` does not equal `fit_transform(X, y)` because a cross fitting scheme is used in `fit_transform` for encoding. See the [User Guide](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder)
 for details.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading Data from OpenML[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#loading-data-from-openml "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

First, we load the wine reviews dataset, where the target is the points given be a reviewer:

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

wine\_reviews \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=42074, as\_frame\=True)

df \= wine\_reviews.frame
df.head()

Copy to clipboard

|     | country | description | designation | points | price | province | region\_1 | region\_2 | variety | winery |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | US  | This tremendous 100% varietal wine hails from ... | Martha's Vineyard | 96  | 235.0 | California | Napa Valley | Napa | Cabernet Sauvignon | Heitz |
| 1   | Spain | Ripe aromas of fig, blackberry and cassis are ... | Carodorum Selección Especial Reserva | 96  | 110.0 | Northern Spain | Toro | NaN | Tinta de Toro | Bodega Carmen Rodríguez |
| 2   | US  | Mac Watson honors the memory of a wine once ma... | Special Selected Late Harvest | 96  | 90.0 | California | Knights Valley | Sonoma | Sauvignon Blanc | Macauley |
| 3   | US  | This spent 20 months in 30% new French oak, an... | Reserve | 96  | 65.0 | Oregon | Willamette Valley | Willamette Valley | Pinot Noir | Ponzi |
| 4   | France | This is the top wine from La Bégude, named aft... | La Brûlade | 95  | 66.0 | Provence | Bandol | NaN | Provence red blend | Domaine de la Bégude |

  
  

For this example, we use the following subset of numerical and categorical features in the data. The target are continuous values from 80 to 100:

numerical\_features \= \["price"\]
categorical\_features \= \[\
    "country",\
    "province",\
    "region\_1",\
    "region\_2",\
    "variety",\
    "winery",\
\]
target\_name \= "points"

X \= df\[numerical\_features + categorical\_features\]
y \= df\[target\_name\]

\_ \= y.hist()

Copy to clipboard

![plot target encoder](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_001.png)

Training and Evaluating Pipelines with Different Encoders[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#training-and-evaluating-pipelines-with-different-encoders "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we will evaluate pipelines with [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 with different encoding strategies. First, we list out the encoders we will be using to preprocess the categorical features:

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
, [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")

categorical\_preprocessors \= \[\
    ("drop", "drop"),\
    ("ordinal", [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")\
(handle\_unknown\="use\_encoded\_value", unknown\_value\=-1)),\
    (\
        "one\_hot",\
        [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore", max\_categories\=20, sparse\_output\=False),\
    ),\
    ("target", [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")\
(target\_type\="continuous")),\
\]

Copy to clipboard

Next, we evaluate the models using cross validation and record the results:

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
from sklearn.model\_selection import [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

n\_cv\_folds \= 3
max\_iter \= 20
results \= \[\]

def evaluate\_model\_and\_store(name, pipe):
    result \= [cross\_validate](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
(
        pipe,
        X,
        y,
        scoring\="neg\_root\_mean\_squared\_error",
        cv\=n\_cv\_folds,
        return\_train\_score\=True,
    )
    rmse\_test\_score \= \-result\["test\_score"\]
    rmse\_train\_score \= \-result\["train\_score"\]
    results.append(
        {
            "preprocessor": name,
            "rmse\_test\_mean": rmse\_test\_score.mean(),
            "rmse\_test\_std": rmse\_train\_score.std(),
            "rmse\_train\_mean": rmse\_train\_score.mean(),
            "rmse\_train\_std": rmse\_train\_score.std(),
        }
    )

for name, categorical\_preprocessor in categorical\_preprocessors:
    preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
        \[\
            ("numerical", "passthrough", numerical\_features),\
            ("categorical", categorical\_preprocessor, categorical\_features),\
        \]
    )
    pipe \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
        preprocessor, [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(random\_state\=0, max\_iter\=max\_iter)
    )
    evaluate\_model\_and\_store(name, pipe)

Copy to clipboard

Native Categorical Feature Support[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#native-categorical-feature-support "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we build and evaluate a pipeline that uses native categorical feature support in [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
, which only supports up to 255 unique categories. In our dataset, the most of the categorical features have more than 255 unique categories:

n\_unique\_categories \= df\[categorical\_features\].nunique().sort\_values(ascending\=False)
n\_unique\_categories

Copy to clipboard

winery      14810
region\_1     1236
variety       632
province      455
country        48
region\_2       18
dtype: int64

Copy to clipboard

To workaround the limitation above, we group the categorical features into low cardinality and high cardinality features. The high cardinality features will be target encoded and the low cardinality features will use the native categorical feature in gradient boosting.

high\_cardinality\_features \= n\_unique\_categories\[n\_unique\_categories \> 255\].index
low\_cardinality\_features \= n\_unique\_categories\[n\_unique\_categories <= 255\].index
mixed\_encoded\_preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    \[\
        ("numerical", "passthrough", numerical\_features),\
        (\
            "high\_cardinality",\
            [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")\
(target\_type\="continuous"),\
            high\_cardinality\_features,\
        ),\
        (\
            "low\_cardinality",\
            [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")\
(handle\_unknown\="use\_encoded\_value", unknown\_value\=-1),\
            low\_cardinality\_features,\
        ),\
    \],
    verbose\_feature\_names\_out\=False,
)

\# The output of the of the preprocessor must be set to pandas so the
\# gradient boosting model can detect the low cardinality features.
mixed\_encoded\_preprocessor.set\_output(transform\="pandas")
mixed\_pipe \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    mixed\_encoded\_preprocessor,
    [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
        random\_state\=0, max\_iter\=max\_iter, categorical\_features\=low\_cardinality\_features
    ),
)
mixed\_pipe

Copy to clipboard

Pipeline(steps=\[('columntransformer',\
                 ColumnTransformer(transformers=\[('numerical', 'passthrough',\
                                                  \['price'\]),\
                                                 ('high\_cardinality',\
                                                  TargetEncoder(target\_type='continuous'),\
                                                  Index(\['winery', 'region\_1', 'variety', 'province'\], dtype='str')),\
                                                 ('low\_cardinality',\
                                                  OrdinalEncoder(handle\_unknown='use\_encoded\_value',\
                                                                 unknown\_value=-1),\
                                                  Index(\['country', 'region\_2'\], dtype='str'))\],\
                                   verbose\_feature\_names\_out=False)),\
                ('histgradientboostingregressor',\
                 HistGradientBoostingRegressor(categorical\_features=Index(\['country', 'region\_2'\], dtype='str'),\
                                               max\_iter=20, random\_state=0))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

Pipeline

[?Documentation for Pipeline](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [steps steps: list of tuples  <br>  <br>List of (name of step, estimator) tuples that are to be chained in  <br>sequential order. To be compatible with the scikit-learn API, all steps  <br>must define \`fit\`. All non-last steps must also define \`transform\`. See  <br>:ref:\`Combining Estimators <combining\_estimators>\` for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | \[('columntransformer', ...), ('histgradientboostingregressor', ...)\] |
|     | [transform\_input transform\_input: list of str, default=None  <br>  <br>The names of the :term:\`metadata\` parameters that should be transformed by the  <br>pipeline before passing it to the step consuming it.  <br>  <br>This enables transforming some input arguments to \`\`fit\`\` (other than \`\`X\`\`)  <br>to be transformed by the steps of the pipeline up to the step which requires  <br>them. Requirement is defined via :ref:\`metadata routing <metadata\_routing>\`.  <br>For instance, this can be used to pass a validation set through the pipeline.  <br>  <br>You can only set this if metadata routing is enabled, which you  <br>can enable using \`\`sklearn.set\_config(enable\_metadata\_routing=True)\`\`.  <br>  <br>.. versionadded:: 1.6](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None |
|     | [memory memory: str or object with the joblib.Memory interface, default=None  <br>  <br>Used to cache the fitted transformers of the pipeline. The last step  <br>will never be cached, even if it is a transformer. By default, no  <br>caching is performed. If a string is given, it is the path to the  <br>caching directory. Enabling caching triggers a clone of the transformers  <br>before fitting. Therefore, the transformer instance given to the  <br>pipeline cannot be inspected directly. Use the attribute \`\`named\_steps\`\`  <br>or \`\`steps\`\` to inspect estimators within the pipeline. Caching the  <br>transformers is advantageous when fitting is time consuming. See  <br>:ref:\`sphx\_glr\_auto\_examples\_neighbors\_plot\_caching\_nearest\_neighbors.py\`  <br>for an example on how to enable caching.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each step will be printed as it  <br>is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

columntransformer: ColumnTransformer

[?Documentation for columntransformer: ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('numerical', ...), ('high\_cardinality', ...), ...\] |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 0.3 |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

numerical

\['price'\]

passthrough

high\_cardinality

Index(\['winery', 'region\_1', 'variety', 'province'\], dtype='str')

TargetEncoder

[?Documentation for TargetEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [target\_type target\_type: {"auto", "continuous", "binary", "multiclass"}, default="auto"  <br>  <br>Type of target.  <br>  <br>\- \`"auto"\` : Type of target is inferred with  <br>:func:\`~sklearn.utils.multiclass.type\_of\_target\`.  <br>\- \`"continuous"\` : Continuous target  <br>\- \`"binary"\` : Binary target  <br>\- \`"multiclass"\` : Multiclass target  <br>  <br>.. note::  <br>The type of target inferred with \`"auto"\` may not be the desired target  <br>type used for modeling. For example, if the target consisted of integers  <br>between 0 and 100, then :func:\`~sklearn.utils.multiclass.type\_of\_target\`  <br>will infer the target as \`"multiclass"\`. In this case, setting  <br>\`target\_type="continuous"\` will specify the target as a regression  <br>problem. The \`target\_type\_\` attribute gives the target type used by the  <br>encoder.  <br>  <br>.. versionchanged:: 1.4  <br>Added the option 'multiclass'.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html#:~:text=target_type,-%7B%22auto%22%2C%20%22continuous%22%2C%20%22binary%22%2C%20%22multiclass%22%7D%2C%20default%3D%22auto%22) | 'continuous' |
|     | [categories categories: "auto" or list of shape (n\_features,) of array-like, default="auto"  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- \`"auto"\` : Determine categories automatically from the training data.  <br>\- list : \`categories\[i\]\` holds the categories expected in the i-th column. The  <br>passed categories should not mix strings and numeric values within a single  <br>feature, and should be sorted in case of numeric values.  <br>  <br>The used categories are stored in the \`categories\_\` fitted attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html#:~:text=categories,-%22auto%22%20or%20list%20of%20shape%20%28n_features%2C%29%20of%20array-like%2C%20default%3D%22auto%22) | 'auto' |
|     | [smooth smooth: "auto" or float, default="auto"  <br>  <br>The amount of mixing of the target mean conditioned on the value of the  <br>category with the global target mean. A larger \`smooth\` value will put  <br>more weight on the global target mean.  <br>If \`"auto"\`, then \`smooth\` is set to an empirical Bayes estimate.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html#:~:text=smooth,-%22auto%22%20or%20float%2C%20default%3D%22auto%22) | 'auto' |
|     | [cv cv: int, cross-validation generator or an iterable, default=5  <br>  <br>Determines the splitting strategy used in the internal :term:\`cross fitting\`  <br>during :meth:\`fit\_transform\`. Splitters where each sample index doesn't appear  <br>in the validation fold exactly once, raise a \`ValueError\`.  <br>Possible inputs for cv are:  <br>  <br>\- \`None\`, to use a 5-fold cross-validation chosen internally based on  <br>\`target\_type\`,  <br>\- integer, to specify the number of folds for the cross-validation chosen  <br>internally based on \`target\_type\`,  <br>\- :term:\`CV splitter\` that does not repeat samples across validation folds,  <br>\- an iterable yielding (train, test) splits as arrays of indices.  <br>  <br>For integer/None inputs, if \`target\_type\` is \`"continuous"\`, :class:\`KFold\` is  <br>used, otherwise :class:\`StratifiedKFold\` is used.  <br>  <br>Refer :ref:\`User Guide <cross\_validation>\` for more information on  <br>cross-validation strategies.  <br>  <br>.. versionchanged:: 1.9  <br>Cross-validation generators and iterables can also be passed as \`cv\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html#:~:text=cv,-int%2C%20cross-validation%20generator%20or%20an%20iterable%2C%20default%3D5) | 5   |
|     | [shuffle shuffle: bool, default=True  <br>  <br>Whether to shuffle the data in :meth:\`fit\_transform\` before splitting into  <br>folds. Note that the samples within each split will not be shuffled. Only  <br>applies if \`cv\` is an int or \`None\`. If \`cv\` is a cross-validation generator or  <br>an iterable, \`shuffle\` is ignored.  <br>  <br>.. deprecated:: 1.9  <br>\`shuffle\` is deprecated and will be removed in 1.11. Pass a cross-validation  <br>generator as \`cv\` argument to specify the shuffling instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html#:~:text=shuffle,-bool%2C%20default%3DTrue) | 'deprecated' |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>When \`shuffle\` is True, \`random\_state\` affects the ordering of the  <br>indices, which controls the randomness of each fold. Otherwise, this  <br>parameter has no effect.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.  <br>  <br>.. deprecated:: 1.9  <br>\`random\_state\` is deprecated and will be removed in 1.11. Pass a  <br>cross-validation generator as \`cv\` argument to specify the random state of  <br>the shuffling instead.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.TargetEncoder.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 'deprecated' |

low\_cardinality

Index(\['country', 'region\_2'\], dtype='str')

OrdinalEncoder

[?Documentation for OrdinalEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [handle\_unknown handle\_unknown: {'error', 'use\_encoded\_value'}, default='error'  <br>  <br>When set to 'error' an error will be raised in case an unknown  <br>categorical feature is present during transform. When set to  <br>'use\_encoded\_value', the encoded value of unknown categories will be  <br>set to the value given for the parameter \`unknown\_value\`. In  <br>:meth:\`inverse\_transform\`, an unknown category will be denoted as None.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27use_encoded_value%27%7D%2C%20default%3D%27error%27) | 'use\_encoded\_value' |
|     | [unknown\_value unknown\_value: int or np.nan, default=None  <br>  <br>When the parameter handle\_unknown is set to 'use\_encoded\_value', this  <br>parameter is required and will set the encoded value of unknown  <br>categories. It has to be distinct from the values used to encode any of  <br>the categories in \`fit\`. If set to np.nan, the \`dtype\` parameter must  <br>be a float dtype.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=unknown_value,-int%20or%20np.nan%2C%20default%3DNone) | \-1 |
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values, and should be sorted in case of numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |
|     | [encoded\_missing\_value encoded\_missing\_value: int or np.nan, default=np.nan  <br>  <br>Encoded value of missing categories. If set to \`np.nan\`, then the \`dtype\`  <br>parameter must be a float dtype.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=encoded_missing_value,-int%20or%20np.nan%2C%20default%3Dnp.nan) | nan |
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output categories for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>\`max\_categories\` do \*\*not\*\* take into account missing or unknown  <br>categories. Setting \`unknown\_value\` or \`encoded\_missing\_value\` to an  <br>integer will increase the number of unique integer codes by one each.  <br>This can result in up to \`max\_categories + 2\` integer codes.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |

HistGradientBoostingRegressor

[?Documentation for HistGradientBoostingRegressor](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [max\_iter max\_iter: int, default=100  <br>  <br>The maximum number of iterations of the boosting process, i.e. the  <br>maximum number of trees.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_iter,-int%2C%20default%3D100) | 20  |
|     | [categorical\_features categorical\_features: array-like of {bool, int, str} of shape (n\_features) or shape (n\_categorical\_features,), default='from\_dtype'  <br>  <br>Indicates the categorical features.  <br>  <br>\- None : no feature will be considered categorical.  <br>\- boolean array-like : boolean mask indicating categorical features.  <br>\- integer array-like : integer indices indicating categorical  <br>features.  <br>\- str array-like: names of categorical features (assuming the training  <br>data has feature names).  <br>\- \`"from\_dtype"\`: dataframe columns with dtype "Categorical" and "Enum" are  <br>considered to be categorical features. The input must be a dataframe that  <br>is supported by narwhals (or supports it): :func:\`narwhals.from\_native\` must  <br>work. This is the case, for instance, for pandas and polars DataFrames.  <br>  <br>For each categorical feature, there must be at most \`max\_bins\` unique  <br>categories. Negative values for categorical features encoded as numeric  <br>dtypes are treated as missing values. All categorical values are  <br>converted to floating point numbers. This means that categorical values  <br>of 1.0 and 1 are treated as the same category.  <br>  <br>Read more in the :ref:\`User Guide <categorical\_support\_gbdt>\` and  <br>:ref:\`sphx\_glr\_auto\_examples\_ensemble\_plot\_gradient\_boosting\_categorical.py\`.  <br>  <br>.. versionadded:: 0.24  <br>  <br>.. versionchanged:: 1.2  <br>Added support for feature names.  <br>  <br>.. versionchanged:: 1.4  <br>Added \`"from\_dtype"\` option.  <br>  <br>.. versionchanged:: 1.6  <br>The default value changed from \`None\` to \`"from\_dtype"\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=categorical_features,-array-like%20of%20%7Bbool%2C%20int%2C%20str%7D%20of%20shape%20%28n_features%29%20%20%20%20%20%20%20%20%20%20%20%20%20or%20shape%20%28n_categorical_features%2C%29%2C%20default%3D%27from_dtype%27) | Index(\['count..., dtype='str') |\
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Pseudo-random number generator to control the subsampling in the  <br>binning process, and the train/validation data split if early stopping  <br>is enabled.  <br>Pass an int for reproducible output across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0   |\
|     | [loss loss: {'squared\_error', 'absolute\_error', 'gamma', 'poisson', 'quantile'}, default='squared\_error'  <br>  <br>The loss function to use in the boosting process. Note that the  <br>"squared error", "gamma" and "poisson" losses actually implement  <br>"half least squares loss", "half gamma deviance" and "half poisson  <br>deviance" to simplify the computation of the gradient. Furthermore,  <br>"gamma" and "poisson" losses internally use a log-link, "gamma"  <br>requires \`\`y > 0\`\` and "poisson" requires \`\`y >= 0\`\`.  <br>"quantile" uses the pinball loss.  <br>  <br>.. versionchanged:: 0.23  <br>Added option 'poisson'.  <br>  <br>.. versionchanged:: 1.1  <br>Added option 'quantile'.  <br>  <br>.. versionchanged:: 1.3  <br>Added option 'gamma'.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=loss,-%7B%27squared_error%27%2C%20%27absolute_error%27%2C%20%27gamma%27%2C%20%27poisson%27%2C%20%27quantile%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27squared_error%27) | 'squared\_error' |\
|     | [quantile quantile: float, default=None  <br>  <br>If loss is "quantile", this parameter specifies which quantile to be estimated  <br>and must be between 0 and 1.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=quantile,-float%2C%20default%3DNone) | None |\
|     | [learning\_rate learning\_rate: float, default=0.1  <br>  <br>The learning rate, also known as \*shrinkage\*. This is used as a  <br>multiplicative factor for the leaves values. Use \`\`1\`\` for no  <br>shrinkage.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=learning_rate,-float%2C%20default%3D0.1) | 0.1 |\
|     | [max\_leaf\_nodes max\_leaf\_nodes: int or None, default=31  <br>  <br>The maximum number of leaves for each tree. Must be strictly greater  <br>than 1. If None, there is no maximum limit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_leaf_nodes,-int%20or%20None%2C%20default%3D31) | 31  |\
|     | [max\_depth max\_depth: int or None, default=None  <br>  <br>The maximum depth of each tree. The depth of a tree is the number of  <br>edges to go from the root to the deepest leaf.  <br>Depth isn't constrained by default.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_depth,-int%20or%20None%2C%20default%3DNone) | None |\
|     | [min\_samples\_leaf min\_samples\_leaf: int, default=20  <br>  <br>The minimum number of samples per leaf. For small datasets with less  <br>than a few hundred samples, it is recommended to lower this value  <br>since only very shallow trees would be built.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=min_samples_leaf,-int%2C%20default%3D20) | 20  |\
|     | [l2\_regularization l2\_regularization: float, default=0  <br>  <br>The L2 regularization parameter penalizing leaves with small hessians.  <br>Use \`\`0\`\` for no regularization (default).](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=l2_regularization,-float%2C%20default%3D0) | 0.0 |\
|     | [max\_features max\_features: float, default=1.0  <br>  <br>Proportion of randomly chosen features in each and every node split.  <br>This is a form of regularization, smaller values make the trees weaker  <br>learners and might prevent overfitting.  <br>If interaction constraints from \`interaction\_cst\` are present, only allowed  <br>features are taken into account for the subsampling.  <br>  <br>.. versionadded:: 1.4](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_features,-float%2C%20default%3D1.0) | 1.0 |\
|     | [max\_bins max\_bins: int, default=255  <br>  <br>The maximum number of bins to use for non-missing values. Before  <br>training, each feature of the input array \`X\` is binned into  <br>integer-valued bins, which allows for a much faster training stage.  <br>Features with a small number of unique values may use less than  <br>\`\`max\_bins\`\` bins. In addition to the \`\`max\_bins\`\` bins, one more bin  <br>is always reserved for missing values. Must be no larger than 255.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=max_bins,-int%2C%20default%3D255) | 255 |\
|     | [monotonic\_cst monotonic\_cst: array-like of int of shape (n\_features) or dict, default=None  <br>  <br>Monotonic constraint to enforce on each feature are specified using the  <br>following integer values:  <br>  <br>\- 1: monotonic increase  <br>\- 0: no constraint  <br>\- -1: monotonic decrease  <br>  <br>If a dict with str keys, map feature to monotonic constraints by name.  <br>If an array, the features are mapped to constraints by position. See  <br>:ref:\`monotonic\_cst\_features\_names\` for a usage example.  <br>  <br>Read more in the :ref:\`User Guide <monotonic\_cst\_gbdt>\`.  <br>  <br>.. versionadded:: 0.23  <br>  <br>.. versionchanged:: 1.2  <br>Accept dict of constraints with feature names as keys.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%20or%20dict%2C%20default%3DNone) | None |\
|     | [interaction\_cst interaction\_cst: {"pairwise", "no\_interactions"} or sequence of lists/tuples/sets of int, default=None  <br>  <br>Specify interaction constraints, the sets of features which can  <br>interact with each other in child node splits.  <br>  <br>Each item specifies the set of feature indices that are allowed  <br>to interact with each other. If there are more features than  <br>specified in these constraints, they are treated as if they were  <br>specified as an additional set.  <br>  <br>The strings "pairwise" and "no\_interactions" are shorthands for  <br>allowing only pairwise or no interactions, respectively.  <br>  <br>For instance, with 5 features in total, \`interaction\_cst=\[{0, 1}\]\`  <br>is equivalent to \`interaction\_cst=\[{0, 1}, {2, 3, 4}\]\`,  <br>and specifies that each branch of a tree will either only split  <br>on features 0 and 1 or only split on features 2, 3 and 4.  <br>  <br>See :ref:\`this example<ice-vs-pdp>\` on how to use \`interaction\_cst\`.  <br>  <br>.. versionadded:: 1.2](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=interaction_cst,-%7B%22pairwise%22%2C%20%22no_interactions%22%7D%20or%20sequence%20of%20lists/tuples/sets%20%20%20%20%20%20%20%20%20%20%20%20%20of%20int%2C%20default%3DNone) | None |\
|     | [warm\_start warm\_start: bool, default=False  <br>  <br>When set to \`\`True\`\`, reuse the solution of the previous call to fit  <br>and add more estimators to the ensemble. For results to be valid, the  <br>estimator should be re-trained on the same data only.  <br>See :term:\`the Glossary <warm\_start>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False |\
|     | [early\_stopping early\_stopping: 'auto' or bool, default='auto'  <br>  <br>If 'auto', early stopping is enabled if the sample size is larger than  <br>10000 or if \`X\_val\` and \`y\_val\` are passed to \`fit\`. If True, early stopping  <br>is enabled, otherwise early stopping is disabled.  <br>  <br>.. versionadded:: 0.23](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=early_stopping,-%27auto%27%20or%20bool%2C%20default%3D%27auto%27) | 'auto' |\
|     | [scoring scoring: str or callable or None, default='loss'  <br>  <br>Scoring method to use for early stopping. Only used if \`early\_stopping\`  <br>is enabled. Options:  <br>  <br>\- str: see :ref:\`scoring\_string\_names\` for options.  <br>\- callable: a scorer callable object (e.g., function) with signature  <br>\`\`scorer(estimator, X, y)\`\`. See :ref:\`scoring\_callable\` for details.  <br>\- \`None\`: the :ref:\`coefficient of determination <r2\_score>\`  <br>(:math:\`R^2\`) is used.  <br>\- 'loss': early stopping is checked w.r.t the loss value.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=scoring,-str%20or%20callable%20or%20None%2C%20default%3D%27loss%27) | 'loss' |\
|     | [validation\_fraction validation\_fraction: int or float or None, default=0.1  <br>  <br>Proportion (or absolute size) of training data to set aside as  <br>validation data for early stopping. If None, early stopping is done on  <br>the training data.  <br>The value is ignored if either early stopping is not performed, e.g.  <br>\`early\_stopping=False\`, or if \`X\_val\` and \`y\_val\` are passed to fit.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=validation_fraction,-int%20or%20float%20or%20None%2C%20default%3D0.1) | 0.1 |\
|     | [n\_iter\_no\_change n\_iter\_no\_change: int, default=10  <br>  <br>Used to determine when to "early stop". The fitting process is  <br>stopped when none of the last \`\`n\_iter\_no\_change\`\` scores are better  <br>than the \`\`n\_iter\_no\_change - 1\`\` -th-to-last one, up to some  <br>tolerance. Only used if early stopping is performed.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=n_iter_no_change,-int%2C%20default%3D10) | 10  |\
|     | [tol tol: float, default=1e-7  <br>  <br>The absolute tolerance to use when comparing scores during early  <br>stopping. The higher the tolerance, the more likely we are to early  <br>stop: higher tolerance means that it will be harder for subsequent  <br>iterations to be considered an improvement upon the reference score.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=tol,-float%2C%20default%3D1e-7) | 1e-07 |\
|     | [verbose verbose: int, default=0  <br>  <br>The verbosity level. If not zero, print some information about the  <br>fitting process. \`\`1\`\` prints only summary info, \`\`2\`\` prints info per  <br>iteration.](https://scikit-learn.org/1.9/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#:~:text=verbose,-int%2C%20default%3D0) | 0   |\
\
  \
  \
\
Finally, we evaluate the pipeline using cross validation and record the results:\
\
evaluate\_model\_and\_store("mixed\_target", mixed\_pipe)\
\
Copy to clipboard\
\
Plotting the Results[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder.html#plotting-the-results "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------\
\
In this section, we display the results by plotting the test and train scores:\
\
import matplotlib.pyplot as plt\
import pandas as pd\
\
results\_df \= (\
    [pd.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")\
(results).set\_index("preprocessor").sort\_values("rmse\_test\_mean")\
)\
\
fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")\
(\
    1, 2, figsize\=(12, 8), sharey\=True, constrained\_layout\=True\
)\
xticks \= range(len(results\_df))\
name\_to\_color \= dict(\
    zip((r\["preprocessor"\] for r in results), \["C0", "C1", "C2", "C3", "C4"\])\
)\
\
for subset, ax in zip(\["test", "train"\], \[ax1, ax2\]):\
    mean, std \= f"rmse\_{subset}\_mean", f"rmse\_{subset}\_std"\
    data \= results\_df\[\[mean, std\]\].sort\_values(mean)\
    ax.bar(\
        x\=xticks,\
        height\=data\[mean\],\
        yerr\=data\[std\],\
        width\=0.9,\
        color\=\[name\_to\_color\[name\] for name in data.index\],\
    )\
    ax.set(\
        title\=f"RMSE ({subset.title()})",\
        xlabel\="Encoding Scheme",\
        xticks\=xticks,\
        xticklabels\=data.index,\
    )\
\
Copy to clipboard\
\
![RMSE (Test), RMSE (Train)](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_002.png)\
\
When evaluating the predictive performance on the test set, dropping the categories perform the worst and the target encoders performs the best. This can be explained as follows:\
\
*   Dropping the categorical features makes the pipeline less expressive and underfitting as a result;\
    \
*   Due to the high cardinality and to reduce the training time, the one-hot encoding scheme uses `max_categories=20` which prevents the features from expanding too much, which can result in underfitting.\
    \
*   If we had not set `max_categories=20`, the one-hot encoding scheme would have likely made the pipeline overfitting as the number of features explodes with rare category occurrences that are correlated with the target by chance (on the training set only);\
    \
*   The ordinal encoding imposes an arbitrary order to the features which are then treated as numerical values by the [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")\
    . Since this model groups numerical features in 256 bins per feature, many unrelated categories can be grouped together and as a result overall pipeline can underfit;\
    \
*   When using the target encoder, the same binning happens, but since the encoded values are statistically ordered by marginal association with the target variable, the binning use by the [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")\
     makes sense and leads to good results: the combination of smoothed target encoding and binning works as a good regularizing strategy against overfitting while not limiting the expressiveness of the pipeline too much.\
    \
\
**Total running time of the script:** (0 minutes 20.973 seconds)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_target_encoder.ipynb)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_target_encoder.ipynb)\
\
[`Download Jupyter notebook: plot_target_encoder.ipynb`](https://scikit-learn.org/stable/_downloads/7b414ce0c39e11cf961fd4fa23008246/plot_target_encoder.ipynb)\
\
[`Download Python source code: plot_target_encoder.py`](https://scikit-learn.org/stable/_downloads/c62ac915428f3a173ccfc19ab3de33bd/plot_target_encoder.py)\
\
[`Download zipped: plot_target_encoder.zip`](https://scikit-learn.org/stable/_downloads/2dd2f734250e8481fde18f8cd2e3820c/plot_target_encoder.zip)\
\
Related examples\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_categorical_thumb.png)\
\
[Categorical Feature Support in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_categorical.html)\
\
Categorical Feature Support in Gradient Boosting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_target_encoder_cross_val_thumb.png)\
\
[Target Encoder’s Internal Cross fitting](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_target_encoder_cross_val.html)\
\
Target Encoder's Internal Cross fitting\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)\
\
[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)\
\
Column Transformer with Mixed Types\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)\
\
[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)\
\
Release Highlights for scikit-learn 1.4\
\
[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)\
\
On this page\
\
[Download source code](https://scikit-learn.org/stable/_downloads/c62ac915428f3a173ccfc19ab3de33bd/plot_target_encoder.py)\
\
[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/7b414ce0c39e11cf961fd4fa23008246/plot_target_encoder.ipynb)\
\
[Download zipped](https://scikit-learn.org/stable/_downloads/2dd2f734250e8481fde18f8cd2e3820c/plot_target_encoder.zip)\
\
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_target_encoder.ipynb)\
\
[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_target_encoder.ipynb)\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)