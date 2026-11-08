[Skip to main content](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/inspection/plot_partial_dependence.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/inspection/plot_partial_dependence.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/inspection/plot_partial_dependence.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/inspection/plot_partial_dependence.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/inspection/plot_partial_dependence.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/inspection/plot_partial_dependence.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#sphx-glr-download-auto-examples-inspection-plot-partial-dependence-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Partial Dependence and Individual Conditional Expectation Plots[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#partial-dependence-and-individual-conditional-expectation-plots "Link to this heading")

=================================================================================================================================================================================================================================================

Partial dependence plots show the dependence between the target function [\[2\]](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#id5)
 and a set of features of interest, marginalizing over the values of all other features (the complement features). Due to the limits of human perception, the size of the set of features of interest must be small (usually, one or two) thus they are usually chosen among the most important features.

Similarly, an individual conditional expectation (ICE) plot [\[3\]](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#id6)
 shows the dependence between the target function and a feature of interest. However, unlike partial dependence plots, which show the average effect of the features of interest, ICE plots visualize the dependence of the prediction on a feature for each [sample](https://scikit-learn.org/stable/glossary.html#term-sample)
 separately, with one line per sample. Only one feature of interest is supported for ICE plots.

This example shows how to obtain partial dependence and ICE plots from a [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 and a [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 trained on the bike sharing dataset. The example is inspired by [\[1\]](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#id4)
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Bike sharing dataset preprocessing[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#bike-sharing-dataset-preprocessing "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We will use the bike sharing dataset. The goal is to predict the number of bike rentals using weather and season data as well as the datetime information.

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")

bikes \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("Bike\_Sharing\_Demand", version\=2, as\_frame\=True)
\# Make an explicit copy to avoid "SettingWithCopyWarning" from pandas
X, y \= bikes.data.copy(), bikes.target

\# We use only a subset of the data to speed up the example.
X \= X.iloc\[::5, :\]
y \= y\[::5\]

Copy to clipboard

The feature `"weather"` has a particularity: the category `"heavy_rain"` is a rare category.

X\["weather"\].value\_counts()

Copy to clipboard

weather
clear         2284
misty          904
rain           287
heavy\_rain       1
Name: count, dtype: int64

Copy to clipboard

Because of this rare category, we collapse it into `"rain"`.

X\["weather"\] \= (
    X\["weather"\]
    .astype(object)
    .replace(to\_replace\="heavy\_rain", value\="rain")
    .astype("category")
)

Copy to clipboard

We now have a closer look at the `"year"` feature:

X\["year"\].value\_counts()

Copy to clipboard

year
1    1747
0    1729
Name: count, dtype: int64

Copy to clipboard

We see that we have data from two years. We use the first year to train the model and the second year to test the model.

mask\_training \= X\["year"\] \== 0.0
X \= X.drop(columns\=\["year"\])
X\_train, y\_train \= X\[mask\_training\], y\[mask\_training\]
X\_test, y\_test \= X\[~mask\_training\], y\[~mask\_training\]

Copy to clipboard

We can check the dataset information to see that we have heterogeneous data types. We have to preprocess the different columns accordingly.

X\_train.info()

Copy to clipboard

<class 'pandas.DataFrame'>
RangeIndex: 1729 entries, 0 to 8640
Data columns (total 11 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   season      1729 non-null   category
 1   month       1729 non-null   int64
 2   hour        1729 non-null   int64
 3   holiday     1729 non-null   category
 4   weekday     1729 non-null   int64
 5   workingday  1729 non-null   category
 6   weather     1729 non-null   category
 7   temp        1729 non-null   float64
 8   feel\_temp   1729 non-null   float64
 9   humidity    1729 non-null   float64
 10  windspeed   1729 non-null   float64
dtypes: category(4), float64(4), int64(3)
memory usage: 101.5 KB

Copy to clipboard

From the previous information, we will consider the `category` columns as nominal categorical features. In addition, we will consider the date and time information as categorical features as well.

We manually define the columns containing numerical and categorical features.

numerical\_features \= \[\
    "temp",\
    "feel\_temp",\
    "humidity",\
    "windspeed",\
\]
categorical\_features \= X\_train.columns.drop(numerical\_features)

Copy to clipboard

Before we go into the details regarding the preprocessing of the different machine learning pipelines, we will try to get some additional intuition regarding the dataset that will be helpful to understand the model’s statistical performance and results of the partial dependence analysis.

We plot the average number of bike rentals by grouping the data by season and by year.

from itertools import [product](https://docs.python.org/3/library/itertools.html#itertools.product "itertools.product")

import matplotlib.pyplot as plt
import numpy as np

days \= ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
hours \= tuple(range(24))
xticklabels \= \[f"{day}\\n{hour}:00" for day, hour in [product](https://docs.python.org/3/library/itertools.html#itertools.product "itertools.product")\
(days, hours)\]
xtick\_start, xtick\_period \= 6, 12

fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, figsize\=(8, 6), sharey\=True, sharex\=True)
average\_bike\_rentals \= bikes.frame.groupby(
    \["year", "season", "weekday", "hour"\], observed\=True
).mean(numeric\_only\=True)\["count"\]
for ax, (idx, df) in zip(axs, average\_bike\_rentals.groupby("year")):
    df.groupby("season", observed\=True).plot(ax\=ax, legend\=True)

    \# decorate the plot
    ax.set\_xticks(
        [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(
            start\=xtick\_start,
            stop\=len(xticklabels),
            num\=len(xticklabels) // xtick\_period,
        )
    )
    ax.set\_xticklabels(xticklabels\[xtick\_start::xtick\_period\])
    ax.set\_xlabel("")
    ax.set\_ylabel("Average number of bike rentals")
    ax.set\_title(
        f"Bike rental for {'2010 (train set)' if idx \== 0.0 else '2011 (test set)'}"
    )
    ax.set\_ylim(0, 1\_000)
    ax.set\_xlim(0, len(xticklabels))
    ax.legend(loc\=2)

Copy to clipboard

![Bike rental for 2010 (train set), Bike rental for 2011 (test set)](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_001.png)

The first striking difference between the train and test set is that the number of bike rentals is higher in the test set. For this reason, it will not be surprising to get a machine learning model that underestimates the number of bike rentals. We also observe that the number of bike rentals is lower during the spring season. In addition, we see that during working days, there is a specific pattern around 6-7 am and 5-6 pm with some peaks of bike rentals. We can keep in mind these different insights and use them to understand the partial dependence plot.

Preprocessor for machine-learning models[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#preprocessor-for-machine-learning-models "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Since we later use two different models, a [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 and a [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
, we create two different preprocessors, specific for each model.

### Preprocessor for the neural network model[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#preprocessor-for-the-neural-network-model "Link to this heading")

We will use a [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 to scale the numerical features and encode the categorical features with a [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
.

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.preprocessing import [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
, [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")

mlp\_preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    transformers\=\[\
        ("num", [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")\
(n\_quantiles\=100), numerical\_features),\
        ("cat", [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
(handle\_unknown\="ignore"), categorical\_features),\
    \]
)
mlp\_preprocessor

Copy to clipboard

ColumnTransformer(transformers=\[('num', QuantileTransformer(n\_quantiles=100),\
                                 \['temp', 'feel\_temp', 'humidity',\
                                  'windspeed'\]),\
                                ('cat', OneHotEncoder(handle\_unknown='ignore'),\
                                 Index(\['season', 'month', 'hour', 'holiday', 'weekday', 'workingday',\
       'weather'\],\
      dtype='str'))\])

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

ColumnTransformer

[?Documentation for ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)
iNot fitted

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

num

\['temp', 'feel\_temp', 'humidity', 'windspeed'\]

QuantileTransformer

[?Documentation for QuantileTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [n\_quantiles n\_quantiles: int, default=1000 or n\_samples  <br>  <br>Number of quantiles to be computed. It corresponds to the number  <br>of landmarks used to discretize the cumulative distribution function.  <br>If n\_quantiles is larger than the number of samples, n\_quantiles is set  <br>to the number of samples as a larger number of quantiles does not give  <br>a better approximation of the cumulative distribution function  <br>estimator.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html#:~:text=n_quantiles,-int%2C%20default%3D1000%20or%20n_samples) | 100 |
|     | [output\_distribution output\_distribution: {'uniform', 'normal'}, default='uniform'  <br>  <br>Marginal distribution for the transformed data. The choices are  <br>'uniform' (default) or 'normal'.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html#:~:text=output_distribution,-%7B%27uniform%27%2C%20%27normal%27%7D%2C%20default%3D%27uniform%27) | 'uniform' |
|     | [ignore\_implicit\_zeros ignore\_implicit\_zeros: bool, default=False  <br>  <br>Only applies to sparse matrices. If True, the sparse entries of the  <br>matrix are discarded to compute the quantile statistics, including  <br>when subsampling. If False, these entries are treated as zeros.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html#:~:text=ignore_implicit_zeros,-bool%2C%20default%3DFalse) | False |
|     | [subsample subsample: int or None, default=10\_000  <br>  <br>Maximum number of samples used to estimate the quantiles for  <br>computational efficiency. Note that the subsampling procedure may  <br>differ for value-identical sparse and dense matrices.  <br>Disable subsampling by setting \`subsample=None\`.  <br>  <br>.. versionadded:: 1.5  <br>The option \`None\` to disable subsampling was added.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html#:~:text=subsample,-int%20or%20None%2C%20default%3D10_000) | 10000 |
|     | [random\_state random\_state: int, RandomState instance or None, default=None  <br>  <br>Determines random number generation for subsampling and smoothing  <br>noise.  <br>Please see \`\`subsample\`\` for more details.  <br>Pass an int for reproducible results across multiple function calls.  <br>See :term:\`Glossary <random\_state>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | None |
|     | [copy copy: bool, default=True  <br>  <br>Set to False to perform inplace transformation and avoid a copy (if the  <br>input is already a numpy array).](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.QuantileTransformer.html#:~:text=copy,-bool%2C%20default%3DTrue) | True |

cat

Index(\['season', 'month', 'hour', 'holiday', 'weekday', 'workingday',\
       'weather'\],
      dtype='str')

OneHotEncoder

[?Documentation for OneHotEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [handle\_unknown handle\_unknown: {'error', 'ignore', 'infrequent\_if\_exist', 'warn'}, default='error'  <br>  <br>Specifies the way unknown categories are handled during :meth:\`transform\`.  <br>  <br>\- 'error' : Raise an error if an unknown category is present during transform.  <br>\- 'ignore' : When an unknown category is encountered during  <br>transform, the resulting one-hot encoded columns for this feature  <br>will be all zeros. In the inverse transform, an unknown category  <br>will be denoted as None.  <br>\- 'infrequent\_if\_exist' : When an unknown category is encountered  <br>during transform, the resulting one-hot encoded columns for this  <br>feature will map to the infrequent category if it exists. The  <br>infrequent category will be mapped to the last position in the  <br>encoding. During inverse transform, an unknown category will be  <br>mapped to the category denoted \`'infrequent'\` if it exists. If the  <br>\`'infrequent'\` category does not exist, then :meth:\`transform\` and  <br>:meth:\`inverse\_transform\` will handle an unknown category as with  <br>\`handle\_unknown='ignore'\`. Infrequent categories exist based on  <br>\`min\_frequency\` and \`max\_categories\`. Read more in the  <br>:ref:\`User Guide <encoder\_infrequent\_categories>\`.  <br>\- 'warn' : When an unknown category is encountered during transform  <br>a warning is issued, and the encoding then proceeds as described for  <br>\`handle\_unknown="infrequent\_if\_exist"\`.  <br>  <br>.. versionchanged:: 1.1  <br>\`'infrequent\_if\_exist'\` was added to automatically handle unknown  <br>categories and infrequent categories.  <br>  <br>.. versionadded:: 1.6  <br>The option \`"warn"\` was added in 1.6.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27ignore%27%2C%20%27infrequent_if_exist%27%2C%20%27warn%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27error%27) | 'ignore' |
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values within a single feature, and should be sorted in case of  <br>numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.  <br>  <br>.. versionadded:: 0.20](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |
|     | [drop drop: {'first', 'if\_binary'} or an array-like of shape (n\_features,), default=None  <br>  <br>Specifies a methodology to use to drop one of the categories per  <br>feature. This is useful in situations where perfectly collinear  <br>features cause problems, such as when feeding the resulting data  <br>into an unregularized linear regression model.  <br>  <br>However, dropping one category breaks the symmetry of the original  <br>representation and can therefore induce a bias in downstream models,  <br>for instance for penalized linear classification or regression models.  <br>  <br>\- None : retain all features (the default).  <br>\- 'first' : drop the first category in each feature. If only one  <br>category is present, the feature will be dropped entirely.  <br>\- 'if\_binary' : drop the first category in each feature with two  <br>categories. Features with 1 or more than 2 categories are  <br>left intact.  <br>\- array : \`\`drop\[i\]\`\` is the category in feature \`\`X\[:, i\]\`\` that  <br>should be dropped.  <br>  <br>When \`max\_categories\` or \`min\_frequency\` is configured to group  <br>infrequent categories, the dropping behavior is handled after the  <br>grouping.  <br>  <br>.. versionadded:: 0.21  <br>The parameter \`drop\` was added in 0.21.  <br>  <br>.. versionchanged:: 0.23  <br>The option \`drop='if\_binary'\` was added in 0.23.  <br>  <br>.. versionchanged:: 1.1  <br>Support for dropping infrequent categories.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=drop,-%7B%27first%27%2C%20%27if_binary%27%7D%20or%20an%20array-like%20of%20shape%20%28n_features%2C%29%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None |
|     | [sparse\_output sparse\_output: bool, default=True  <br>  <br>When \`\`True\`\`, it returns a SciPy sparse matrix/array  <br>in "Compressed Sparse Row" (CSR) format.  <br>  <br>.. versionadded:: 1.2  <br>\`sparse\` was renamed to \`sparse\_output\`](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=sparse_output,-bool%2C%20default%3DTrue) | True |
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output features for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>.. versionadded:: 1.1  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |
|     | [feature\_name\_combiner feature\_name\_combiner: "concat" or callable, default="concat"  <br>  <br>Callable with signature \`def callable(input\_feature, category)\` that returns a  <br>string. This is used to create feature names to be returned by  <br>:meth:\`get\_feature\_names\_out\`.  <br>  <br>\`"concat"\` concatenates encoded feature name and category with  <br>\`feature + "\_" + str(category)\`.E.g. feature X with values 1, 6, 7 create  <br>feature names \`X\_1, X\_6, X\_7\`.  <br>  <br>.. versionadded:: 1.3](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OneHotEncoder.html#:~:text=feature_name_combiner,-%22concat%22%20or%20callable%2C%20default%3D%22concat%22) | 'concat' |

  
  

### Preprocessor for the gradient boosting model[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#preprocessor-for-the-gradient-boosting-model "Link to this heading")

For the gradient boosting model, we leave the numerical features as-is and only encode the categorical features using a [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
.

from sklearn.preprocessing import [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")

hgbdt\_preprocessor \= [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
(
    transformers\=\[\
        ("cat", [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")\
(), categorical\_features),\
        ("num", "passthrough", numerical\_features),\
    \],
    sparse\_threshold\=1,
    verbose\_feature\_names\_out\=False,
).set\_output(transform\="pandas")
hgbdt\_preprocessor

Copy to clipboard

ColumnTransformer(sparse\_threshold=1,
                  transformers=\[('cat', OrdinalEncoder(),\
                                 Index(\['season', 'month', 'hour', 'holiday', 'weekday', 'workingday',\
       'weather'\],\
      dtype='str')),\
                                ('num', 'passthrough',\
                                 \['temp', 'feel\_temp', 'humidity',\
                                  'windspeed'\])\],
                  verbose\_feature\_names\_out=False)

**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.  
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**

ColumnTransformer

[?Documentation for ColumnTransformer](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html)
iNot fitted

Parameters

|     |     |     |
| --- | --- | --- |
|     | [transformers transformers: list of tuples  <br>  <br>List of (name, transformer, columns) tuples specifying the  <br>transformer objects to be applied to subsets of the data.  <br>  <br>name : str  <br>Like in Pipeline and FeatureUnion, this allows the transformer and  <br>its parameters to be set using \`\`set\_params\`\` and searched in grid  <br>search.  <br>transformer : {'drop', 'passthrough'} or estimator  <br>Estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Special-cased strings 'drop' and 'passthrough' are accepted as  <br>well, to indicate to drop the columns or to pass them through  <br>untransformed, respectively.  <br>columns : str, array-like of str, int, array-like of int, array-like of bool, slice or callable  <br>Indexes the data on its second axis. Integers are interpreted as  <br>positional columns, while strings can reference DataFrame columns  <br>by name. A scalar string or int should be used where  <br>\`\`transformer\`\` expects X to be a 1d array-like (vector),  <br>otherwise a 2d array will be passed to the transformer.  <br>A callable is passed the input data \`X\` and can return any of the  <br>above. To select multiple columns by name or dtype, you can use  <br>:obj:\`make\_column\_selector\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformers,-list%20of%20tuples) | \[('cat', ...), ('num', ...)\] |
|     | [sparse\_threshold sparse\_threshold: float, default=0.3  <br>  <br>If the output of the different transformers contains sparse matrices,  <br>these will be stacked as a sparse matrix if the overall density is  <br>lower than this value. Use \`\`sparse\_threshold=0\`\` to always return  <br>dense. When the transformed output consists of all dense data, the  <br>stacked result will be dense, and this keyword will be ignored.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=sparse_threshold,-float%2C%20default%3D0.3) | 1   |
|     | [verbose\_feature\_names\_out verbose\_feature\_names\_out: bool, str or Callable\[\[str, str\], str\], default=True  <br>  <br>\- If True, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will prefix  <br>all feature names with the name of the transformer that generated that  <br>feature. It is equivalent to setting  <br>\`verbose\_feature\_names\_out="{transformer\_name}\_\_{feature\_name}"\`.  <br>\- If False, :meth:\`ColumnTransformer.get\_feature\_names\_out\` will not  <br>prefix any feature names and will error if feature names are not  <br>unique.  <br>\- If \`\`Callable\[\[str, str\], str\]\`\`,  <br>:meth:\`ColumnTransformer.get\_feature\_names\_out\` will rename all the features  <br>using the name of the transformer. The first argument of the callable is the  <br>transformer name and the second argument is the feature name. The returned  <br>string will be the new feature name.  <br>\- If \`\`str\`\`, it must be a string ready for formatting. The given string will  <br>be formatted using two field names: \`\`transformer\_name\`\` and \`\`feature\_name\`\`.  <br>e.g. \`\`"{feature\_name}\_\_{transformer\_name}"\`\`. See :meth:\`str.format\` method  <br>from the standard library for more info.  <br>  <br>.. versionadded:: 1.0  <br>  <br>.. versionchanged:: 1.6  <br>\`verbose\_feature\_names\_out\` can be a callable or a string to be formatted.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose_feature_names_out,-bool%2C%20str%20or%20Callable%5B%5Bstr%2C%20str%5D%2C%20str%5D%2C%20default%3DTrue) | False |
|     | [remainder remainder: {'drop', 'passthrough'} or estimator, default='drop'  <br>  <br>By default, only the specified columns in \`transformers\` are  <br>transformed and combined in the output, and the non-specified  <br>columns are dropped. (default of \`\`'drop'\`\`).  <br>By specifying \`\`remainder='passthrough'\`\`, all remaining columns that  <br>were not specified in \`transformers\`, but present in the data passed  <br>to \`fit\` will be automatically passed through. This subset of columns  <br>is concatenated with the output of the transformers. For dataframes,  <br>extra columns not seen during \`fit\` will be excluded from the output  <br>of \`transform\`.  <br>By setting \`\`remainder\`\` to be an estimator, the remaining  <br>non-specified columns will use the \`\`remainder\`\` estimator. The  <br>estimator must support :term:\`fit\` and :term:\`transform\`.  <br>Note that using this feature requires that the DataFrame columns  <br>input at :term:\`fit\` and :term:\`transform\` have identical order.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=remainder,-%7B%27drop%27%2C%20%27passthrough%27%7D%20or%20estimator%2C%20default%3D%27drop%27) | 'drop' |
|     | [n\_jobs n\_jobs: int, default=None  <br>  <br>Number of jobs to run in parallel.  <br>\`\`None\`\` means 1 unless in a :obj:\`joblib.parallel\_backend\` context.  <br>\`\`-1\`\` means using all processors. See :term:\`Glossary <n\_jobs>\`  <br>for more details.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None |
|     | [transformer\_weights transformer\_weights: dict, default=None  <br>  <br>Multiplicative weights for features per transformer. The output of the  <br>transformer is multiplied by these weights. Keys are transformer names,  <br>values the weights.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=transformer_weights,-dict%2C%20default%3DNone) | None |
|     | [verbose verbose: bool, default=False  <br>  <br>If True, the time elapsed while fitting each transformer will be  <br>printed as it is completed.](https://scikit-learn.org/1.9/modules/generated/sklearn.compose.ColumnTransformer.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False |

cat

Index(\['season', 'month', 'hour', 'holiday', 'weekday', 'workingday',\
       'weather'\],
      dtype='str')

OrdinalEncoder

[?Documentation for OrdinalEncoder](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)

Parameters

|     |     |     |
| --- | --- | --- |
|     | [categories categories: 'auto' or a list of array-like, default='auto'  <br>  <br>Categories (unique values) per feature:  <br>  <br>\- 'auto' : Determine categories automatically from the training data.  <br>\- list : \`\`categories\[i\]\`\` holds the categories expected in the ith  <br>column. The passed categories should not mix strings and numeric  <br>values, and should be sorted in case of numeric values.  <br>  <br>The used categories can be found in the \`\`categories\_\`\` attribute.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=categories,-%27auto%27%20or%20a%20list%20of%20array-like%2C%20default%3D%27auto%27) | 'auto' |
|     | [dtype dtype: number type, default=np.float64  <br>  <br>Desired dtype of output.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=dtype,-number%20type%2C%20default%3Dnp.float64) | <class 'numpy.float64'> |
|     | [handle\_unknown handle\_unknown: {'error', 'use\_encoded\_value'}, default='error'  <br>  <br>When set to 'error' an error will be raised in case an unknown  <br>categorical feature is present during transform. When set to  <br>'use\_encoded\_value', the encoded value of unknown categories will be  <br>set to the value given for the parameter \`unknown\_value\`. In  <br>:meth:\`inverse\_transform\`, an unknown category will be denoted as None.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=handle_unknown,-%7B%27error%27%2C%20%27use_encoded_value%27%7D%2C%20default%3D%27error%27) | 'error' |
|     | [unknown\_value unknown\_value: int or np.nan, default=None  <br>  <br>When the parameter handle\_unknown is set to 'use\_encoded\_value', this  <br>parameter is required and will set the encoded value of unknown  <br>categories. It has to be distinct from the values used to encode any of  <br>the categories in \`fit\`. If set to np.nan, the \`dtype\` parameter must  <br>be a float dtype.  <br>  <br>.. versionadded:: 0.24](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=unknown_value,-int%20or%20np.nan%2C%20default%3DNone) | None |
|     | [encoded\_missing\_value encoded\_missing\_value: int or np.nan, default=np.nan  <br>  <br>Encoded value of missing categories. If set to \`np.nan\`, then the \`dtype\`  <br>parameter must be a float dtype.  <br>  <br>.. versionadded:: 1.1](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=encoded_missing_value,-int%20or%20np.nan%2C%20default%3Dnp.nan) | nan |
|     | [min\_frequency min\_frequency: int or float, default=None  <br>  <br>Specifies the minimum frequency below which a category will be  <br>considered infrequent.  <br>  <br>\- If \`int\`, categories with a smaller cardinality will be considered  <br>infrequent.  <br>  <br>\- If \`float\`, categories with a smaller cardinality than  <br>\`min\_frequency \* n\_samples\` will be considered infrequent.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=min_frequency,-int%20or%20float%2C%20default%3DNone) | None |
|     | [max\_categories max\_categories: int, default=None  <br>  <br>Specifies an upper limit to the number of output categories for each input  <br>feature when considering infrequent categories. If there are infrequent  <br>categories, \`max\_categories\` includes the category representing the  <br>infrequent categories along with the frequent categories. If \`None\`,  <br>there is no limit to the number of output features.  <br>  <br>\`max\_categories\` do \*\*not\*\* take into account missing or unknown  <br>categories. Setting \`unknown\_value\` or \`encoded\_missing\_value\` to an  <br>integer will increase the number of unique integer codes by one each.  <br>This can result in up to \`max\_categories + 2\` integer codes.  <br>  <br>.. versionadded:: 1.3  <br>Read more in the :ref:\`User Guide <encoder\_infrequent\_categories>\`.](https://scikit-learn.org/1.9/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#:~:text=max_categories,-int%2C%20default%3DNone) | None |

num

\['temp', 'feel\_temp', 'humidity', 'windspeed'\]

passthrough

  
  

1-way partial dependence with different models[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#way-partial-dependence-with-different-models "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we will compute 1-way partial dependence with two different machine-learning models: (i) a multi-layer perceptron and (ii) a gradient-boosting model. With these two models, we illustrate how to compute and interpret both partial dependence plot (PDP) for both numerical and categorical features and individual conditional expectation (ICE).

### Multi-layer perceptron[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#multi-layer-perceptron "Link to this heading")

Let’s fit a [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 and compute single-variable partial dependence plots.

from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

from sklearn.neural\_network import [MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")

print("Training MLPRegressor...")
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
mlp\_model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    mlp\_preprocessor,
    [MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
(
        hidden\_layer\_sizes\=(30, 15),
        learning\_rate\_init\=0.01,
        early\_stopping\=True,
        random\_state\=0,
    ),
)
mlp\_model.fit(X\_train, y\_train)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
print(f"Test R2 score: {mlp\_model.score(X\_test, y\_test):.2f}")

Copy to clipboard

Training MLPRegressor...
done in 0.685s
Test R2 score: 0.61

Copy to clipboard

We configured a pipeline using the preprocessor that we created specifically for the neural network and tuned the neural network size and learning rate to get a reasonable compromise between training time and predictive performance on a test set.

Importantly, this tabular dataset has very different dynamic ranges for its features. Neural networks tend to be very sensitive to features with varying scales and forgetting to preprocess the numeric feature would lead to a very poor model.

It would be possible to get even higher predictive performance with a larger neural network but the training would also be significantly more expensive.

Note that it is important to check that the model is accurate enough on a test set before plotting the partial dependence since there would be little use in explaining the impact of a given feature on the prediction function of a model with poor predictive performance. In this regard, our MLP model works reasonably well.

We will plot the averaged partial dependence.

import matplotlib.pyplot as plt

from sklearn.inspection import PartialDependenceDisplay

common\_params \= {
    "subsample": 50,
    "n\_jobs": 2,
    "grid\_resolution": 20,
    "random\_state": 0,
}

print("Computing partial dependence plots...")
features\_info \= {
    \# features of interest
    "features": \["temp", "humidity", "windspeed", "season", "weather", "hour"\],
    \# type of partial dependence plot
    "kind": "average",
    \# information regarding categorical features
    "categorical\_features": categorical\_features,
}
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, nrows\=2, figsize\=(9, 8), constrained\_layout\=True)
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    mlp\_model,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle(
    (
        "Partial dependence of the number of bike rentals\\n"
        "for the bike rental dataset with an MLPRegressor"
    ),
    fontsize\=16,
)

Copy to clipboard

![Partial dependence of the number of bike rentals for the bike rental dataset with an MLPRegressor](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_002.png)

Computing partial dependence plots...
done in 0.814s

Copy to clipboard

### Gradient boosting[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#gradient-boosting "Link to this heading")

Let’s now fit a [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
 and compute the partial dependence on the same features. We also use the specific preprocessor we created for this model.

from sklearn.ensemble import [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")

print("Training HistGradientBoostingRegressor...")
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
hgbdt\_model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(
    hgbdt\_preprocessor,
    [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
(
        categorical\_features\=categorical\_features,
        random\_state\=0,
        max\_iter\=50,
    ),
)
hgbdt\_model.fit(X\_train, y\_train)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
print(f"Test R2 score: {hgbdt\_model.score(X\_test, y\_test):.2f}")

Copy to clipboard

Training HistGradientBoostingRegressor...
done in 0.111s
Test R2 score: 0.62

Copy to clipboard

Here, we used the default hyperparameters for the gradient boosting model without any preprocessing as tree-based models are naturally robust to monotonic transformations of numerical features.

Note that on this tabular dataset, Gradient Boosting Machines are both significantly faster to train and more accurate than neural networks. It is also significantly cheaper to tune their hyperparameters (the defaults tend to work well while this is not often the case for neural networks).

We will plot the partial dependence for some of the numerical and categorical features.

print("Computing partial dependence plots...")
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, nrows\=2, figsize\=(9, 8), constrained\_layout\=True)
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle(
    (
        "Partial dependence of the number of bike rentals\\n"
        "for the bike rental dataset with a gradient boosting"
    ),
    fontsize\=16,
)

Copy to clipboard

![Partial dependence of the number of bike rentals for the bike rental dataset with a gradient boosting](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_003.png)

Computing partial dependence plots...
done in 1.206s

Copy to clipboard

### Analysis of the plots[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#analysis-of-the-plots "Link to this heading")

We will first look at the PDPs for the numerical features. For both models, the general trend of the PDP of the temperature is that the number of bike rentals is increasing with temperature. We can make a similar analysis but with the opposite trend for the humidity features. The number of bike rentals is decreasing when the humidity increases. Finally, we see the same trend for the wind speed feature. The number of bike rentals is decreasing when the wind speed is increasing for both models. We also observe that [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
 has much smoother predictions than [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")
.

Now, we will look at the partial dependence plots for the categorical features.

We observe that the spring season is the lowest bar for the season feature. With the weather feature, the rain category is the lowest bar. Regarding the hour feature, we see two peaks around the 7 am and 6 pm. These findings are in line with the the observations we made earlier on the dataset.

However, it is worth noting that we are creating potential meaningless synthetic samples if features are correlated.

### ICE vs. PDP[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#ice-vs-pdp "Link to this heading")

PDP is an average of the marginal effects of the features. We are averaging the response of all samples of the provided set. Thus, some effects could be hidden. In this regard, it is possible to plot each individual response. This representation is called the Individual Effect Plot (ICE). In the plot below, we plot 50 randomly selected ICEs for the temperature and humidity features.

print("Computing partial dependence plots and individual conditional expectation...")
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(6, 4), sharey\=True, constrained\_layout\=True)

features\_info \= {
    "features": \["temp", "humidity"\],
    "kind": "both",
    "centered": True,
}

display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle("ICE and PDP representations", fontsize\=16)

Copy to clipboard

![ICE and PDP representations](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_004.png)

Computing partial dependence plots and individual conditional expectation...
done in 0.512s

Copy to clipboard

We see that the ICE for the temperature feature gives us some additional information: Some of the ICE lines are flat while some others show a decrease of the dependence for temperature above 35 degrees Celsius. We observe a similar pattern for the humidity feature: some of the ICEs lines show a sharp decrease when the humidity is above 80%.

Not all ICE lines are parallel, this indicates that the model finds interactions between features. We can repeat the experiment by constraining the gradient boosting model to not use any interactions between features using the parameter `interaction_cst`:

from sklearn.base import clone

interaction\_cst \= \[\[i\] for i in range(X\_train.shape\[1\])\]
hgbdt\_model\_without\_interactions \= (
    clone(hgbdt\_model)
    .set\_params(histgradientboostingregressor\_\_interaction\_cst\=interaction\_cst)
    .fit(X\_train, y\_train)
)
print(f"Test R2 score: {hgbdt\_model\_without\_interactions.score(X\_test, y\_test):.2f}")

Copy to clipboard

Test R2 score: 0.38

Copy to clipboard

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(6, 4), sharey\=True, constrained\_layout\=True)

features\_info\["centered"\] \= False
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model\_without\_interactions,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)
\_ \= display.figure\_.suptitle("ICE and PDP representations", fontsize\=16)

Copy to clipboard

![ICE and PDP representations](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_005.png)

2D interaction plots[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#d-interaction-plots "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

PDPs with two features of interest enable us to visualize interactions among them. However, ICEs cannot be plotted in an easy manner and thus interpreted. We will show the representation of available in [`from_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
 that is a 2D heatmap.

print("Computing partial dependence plots...")
features\_info \= {
    "features": \["temp", "humidity", ("temp", "humidity")\],
    "kind": "average",
}
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(10, 4), constrained\_layout\=True)
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle(
    "1-way vs 2-way of numerical PDP using gradient boosting", fontsize\=16
)

Copy to clipboard

![1-way vs 2-way of numerical PDP using gradient boosting](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_006.png)

Computing partial dependence plots...
done in 8.447s

Copy to clipboard

The two-way partial dependence plot shows the dependence of the number of bike rentals on joint values of temperature and humidity. We clearly see an interaction between the two features. For a temperature higher than 20 degrees Celsius, the humidity has an impact on the number of bike rentals that seems independent on the temperature.

On the other hand, for temperatures lower than 20 degrees Celsius, both the temperature and humidity continuously impact the number of bike rentals.

Furthermore, the slope of the of the impact ridge of the 20 degrees Celsius threshold is very dependent on the humidity level: the ridge is steep under dry conditions but much smoother under wetter conditions above 70% of humidity.

We now contrast those results with the same plots computed for the model constrained to learn a prediction function that does not depend on such non-linear feature interactions.

print("Computing partial dependence plots...")
features\_info \= {
    "features": \["temp", "humidity", ("temp", "humidity")\],
    "kind": "average",
}
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(10, 4), constrained\_layout\=True)
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model\_without\_interactions,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle(
    "1-way vs 2-way of numerical PDP using gradient boosting", fontsize\=16
)

Copy to clipboard

![1-way vs 2-way of numerical PDP using gradient boosting](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_007.png)

Computing partial dependence plots...
done in 7.452s

Copy to clipboard

The 1D partial dependence plots for the model constrained to not model feature interactions show local spikes for each features individually, in particular for for the “humidity” feature. Those spikes might be reflecting a degraded behavior of the model that attempts to somehow compensate for the forbidden interactions by overfitting particular training points. Note that the predictive performance of this model as measured on the test set is significantly worse than that of the original, unconstrained model.

Also note that the number of local spikes visible on those plots is depends on the grid resolution parameter of the PD plot itself.

Those local spikes result in a noisily gridded 2D PD plot. It is quite challenging to tell whether or not there are no interaction between those features because of the high frequency oscillations in the humidity feature. However it can clearly be seen that the simple interaction effect observed when the temperature crosses the 20 degrees boundary is no longer visible for this model.

The partial dependence between categorical features will provide a discrete representation that can be shown as a heatmap. For instance the interaction between the season, the weather, and the target would be as follow:

print("Computing partial dependence plots...")
features\_info \= {
    "features": \["season", "weather", ("season", "weather")\],
    "kind": "average",
    "categorical\_features": categorical\_features,
}
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(14, 6), constrained\_layout\=True)
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
)

print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle(
    "1-way vs 2-way PDP of categorical features using gradient boosting", fontsize\=16
)

Copy to clipboard

![1-way vs 2-way PDP of categorical features using gradient boosting](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_008.png)

Computing partial dependence plots...
done in 0.341s

Copy to clipboard

### 3D representation[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#d-representation "Link to this heading")

Let’s make the same partial dependence plot for the 2 features interaction, this time in 3 dimensions.

\# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl\_toolkits.mplot3d  \# noqa: F401
import numpy as np

from sklearn.inspection import [partial\_dependence](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")

fig \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5.5, 5))

features \= ("temp", "humidity")
pdp \= [partial\_dependence](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")
(
    hgbdt\_model, X\_train, features\=features, kind\="average", grid\_resolution\=10
)
XX, YY \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
(pdp\["grid\_values"\]\[0\], pdp\["grid\_values"\]\[1\])
Z \= pdp.average\[0\].T
ax \= fig.add\_subplot(projection\="3d")
fig.add\_axes(ax)

surf \= ax.plot\_surface(XX, YY, Z, rstride\=1, cstride\=1, cmap\=plt.cm.BuPu, edgecolor\="k")
ax.set\_xlabel(features\[0\])
ax.set\_ylabel(features\[1\])
fig.suptitle(
    "PD of number of bike rentals on\\nthe temperature and humidity GBDT model",
    fontsize\=16,
)
\# pretty init view
ax.view\_init(elev\=22, azim\=122)
clb \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
(surf, pad\=0.08, shrink\=0.6, aspect\=10)
clb.ax.set\_title("Partial\\ndependence")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![PD of number of bike rentals on the temperature and humidity GBDT model, Partial dependence](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_009.png)

### Custom Inspection Points[#](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence.html#custom-inspection-points "Link to this heading")

None of the examples so far specify \_which\_ points are evaluated to create the partial dependence plots. By default we use percentiles defined by the input dataset. In some cases it can be helpful to specify the exact points where you would like the model evaluated. For instance, if a user wants to test the model behavior on out-of-distribution data or compare two models that were fit on slightly different data. The `custom_values` parameter allows the user to pass in the values that they want the model to be evaluated on. This overrides the `grid_resolution` and `percentiles` parameters. Let’s return to our gradient boosting example above but with custom values

print("Computing partial dependence plots with custom evaluation values...")
tic \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(6, 4), sharey\=True, constrained\_layout\=True)

features\_info \= {
    "features": \["temp", "humidity"\],
    "kind": "both",
}

display \= [PartialDependenceDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay.from_estimator "sklearn.inspection.PartialDependenceDisplay.from_estimator")
(
    hgbdt\_model,
    X\_train,
    \*\*features\_info,
    ax\=ax,
    \*\*common\_params,
    \# we set custom values for temp feature -
    \# all other features are evaluated based on the data
    custom\_values\={"temp": [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 40, 10)},
)
print(f"done in {[time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tic:.3f}s")
\_ \= display.figure\_.suptitle(
    (
        "Partial dependence of the number of bike rentals\\n"
        "for the bike rental dataset with a gradient boosting"
    ),
    fontsize\=16,
)

Copy to clipboard

![Partial dependence of the number of bike rentals for the bike rental dataset with a gradient boosting](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_010.png)

Computing partial dependence plots with custom evaluation values...
done in 0.478s

Copy to clipboard

**Total running time of the script:** (0 minutes 25.396 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_partial_dependence.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_partial_dependence.ipynb)

[`Download Jupyter notebook: plot_partial_dependence.ipynb`](https://scikit-learn.org/stable/_downloads/21b82d82985712b5de6347f382c77c86/plot_partial_dependence.ipynb)

[`Download Python source code: plot_partial_dependence.py`](https://scikit-learn.org/stable/_downloads/bcd609cfe29c9da1f51c848e18b89c76/plot_partial_dependence.py)

[`Download zipped: plot_partial_dependence.zip`](https://scikit-learn.org/stable/_downloads/71a61bc97b8485c9c30708afd6dbe763/plot_partial_dependence.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_partial_dependence_visualization_api_thumb.png)

[Advanced Plotting With Partial Dependence](https://scikit-learn.org/stable/auto_examples/inspection/plot_partial_dependence_visualization_api.html)

Advanced Plotting With Partial Dependence

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_24_0_thumb.png)

[Release Highlights for scikit-learn 0.24](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_24_0.html)

Release Highlights for scikit-learn 0.24

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)

[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)

Release Highlights for scikit-learn 1.2

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/bcd609cfe29c9da1f51c848e18b89c76/plot_partial_dependence.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/21b82d82985712b5de6347f382c77c86/plot_partial_dependence.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/71a61bc97b8485c9c30708afd6dbe763/plot_partial_dependence.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo17.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/inspection/plot_partial_dependence.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo17.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/inspection/plot_partial_dependence.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)