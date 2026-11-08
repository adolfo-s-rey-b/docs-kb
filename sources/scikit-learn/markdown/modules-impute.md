[Skip to main content](https://scikit-learn.org/stable/modules/impute.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/impute.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/impute.html)
[1.8.0](https://scikit-learn.org/1.8/modules/impute.html)
[1.7.2](https://scikit-learn.org/1.7/modules/impute.html)
[1.6.1](https://scikit-learn.org/1.6/modules/impute.html)
[1.5.2](https://scikit-learn.org/1.5/modules/impute.html)
[1.4.2](https://scikit-learn.org/1.4/modules/impute.html)

Collapse Sidebar Expand Sidebar

8.4. Imputation of missing values[#](https://scikit-learn.org/stable/modules/impute.html#imputation-of-missing-values "Link to this heading")

==============================================================================================================================================

For various reasons, many real world datasets contain missing values, often encoded as blanks, NaNs or other placeholders. Such datasets however are incompatible with scikit-learn estimators which assume that all values in an array are numerical, and that all have and hold meaning. A basic strategy to use incomplete datasets is to discard entire rows and/or columns containing missing values. However, this comes at the price of losing data which may be valuable (even though incomplete). A better strategy is to impute the missing values, i.e., to infer them from the known part of the data. See the glossary entry on [imputation](https://scikit-learn.org/stable/glossary.html#term-imputation)
.

8.4.1. Univariate vs. Multivariate Imputation[#](https://scikit-learn.org/stable/modules/impute.html#univariate-vs-multivariate-imputation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

One type of imputation algorithm is univariate, which imputes values in the i-th feature dimension using only non-missing values in that feature dimension (e.g. [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
). By contrast, multivariate imputation algorithms use the entire set of available feature dimensions to estimate the missing values (e.g. [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
).

8.4.2. Univariate feature imputation[#](https://scikit-learn.org/stable/modules/impute.html#univariate-feature-imputation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

The [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 class provides basic strategies for imputing missing values. Missing values can be imputed with a provided constant value, or using the statistics (mean, median or most frequent) of each column in which the missing values are located. This class also allows for different missing values encodings.

The following snippet demonstrates how to replace missing values, encoded as `np.nan`, using the mean value of the columns (axis 0) that contain the missing values:

\>>> import numpy as np
\>>> from sklearn.impute import SimpleImputer
\>>> imp \= SimpleImputer(missing\_values\=np.nan, strategy\='mean')
\>>> imp.fit(\[\[1, 2\], \[np.nan, 3\], \[7, 6\]\])
SimpleImputer()
\>>> X \= \[\[np.nan, 2\], \[6, np.nan\], \[7, 6\]\]
\>>> print(imp.transform(X))
\[\[4.          2.        \]\
 \[6.          3.666\]\
 \[7.          6.        \]\]

Copy to clipboard

The [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 class also supports sparse matrices:

\>>> import scipy.sparse as sp
\>>> X \= sp.csc\_array(\[\[1, 2\], \[0, \-1\], \[8, 4\]\])
\>>> imp \= SimpleImputer(missing\_values\=-1, strategy\='mean')
\>>> imp.fit(X)
SimpleImputer(missing\_values=-1)
\>>> X\_test \= sp.csc\_array(\[\[\-1, 2\], \[6, \-1\], \[7, 6\]\])
\>>> print(imp.transform(X\_test).toarray())
\[\[3. 2.\]\
 \[6. 3.\]\
 \[7. 6.\]\]

Copy to clipboard

Note that this format is not meant to be used to implicitly store missing values in the matrix because it would densify it at transform time. Missing values encoded by 0 must be used with dense input.

The [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 class also supports categorical data represented as string values or pandas categoricals when using the `'most_frequent'` or `'constant'` strategy:

\>>> import pandas as pd
\>>> df \= pd.DataFrame(\[\["a", "x"\],\
...                    \[np.nan, "y"\],\
...                    \["a", np.nan\],\
...                    \["b", "y"\]\], dtype\="category")
...
\>>> imp \= SimpleImputer(strategy\="most\_frequent")
\>>> print(imp.fit\_transform(df))
\[\['a' 'x'\]\
 \['a' 'y'\]\
 \['a' 'y'\]\
 \['b' 'y'\]\]

Copy to clipboard

For another example on usage, see [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)
.

8.4.3. Multivariate feature imputation[#](https://scikit-learn.org/stable/modules/impute.html#multivariate-feature-imputation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

A more sophisticated approach is to use the [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 class, which models each feature with missing values as a function of other features, and uses that estimate for imputation. It does so in an iterated round-robin fashion: at each step, a feature column is designated as output `y` and the other feature columns are treated as inputs `X`. A regressor is fit on `(X, y)` for known `y`. Then, the regressor is used to predict the missing values of `y`. This is done for each feature in an iterative fashion, and then is repeated for `max_iter` imputation rounds. The results of the final imputation round are returned.

Note

This estimator is still **experimental** for now: default parameters or details of behaviour might change without any deprecation cycle. Resolving the following issues would help stabilize [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
: convergence criteria ([#14338](https://github.com/scikit-learn/scikit-learn/issues/14338)
) and default estimators ([#13286](https://github.com/scikit-learn/scikit-learn/issues/13286)
). To use it, you need to explicitly import `enable_iterative_imputer`.

\>>> import numpy as np
\>>> from sklearn.experimental import enable\_iterative\_imputer
\>>> from sklearn.impute import IterativeImputer
\>>> imp \= IterativeImputer(max\_iter\=10, random\_state\=0)
\>>> imp.fit(\[\[1, 2\], \[3, 6\], \[4, 8\], \[np.nan, 3\], \[7, np.nan\]\])
IterativeImputer(random\_state=0)
\>>> X\_test \= \[\[np.nan, 2\], \[6, np.nan\], \[np.nan, 6\]\]
\>>> \# the model learns that the second feature is double the first
\>>> print(np.round(imp.transform(X\_test)))
\[\[ 1.  2.\]\
 \[ 6. 12.\]\
 \[ 3.  6.\]\]

Copy to clipboard

Both [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 and [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 can be used in a Pipeline as a way to build a composite estimator that supports imputation. See [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)
.

### 8.4.3.1. Flexibility of IterativeImputer[#](https://scikit-learn.org/stable/modules/impute.html#flexibility-of-iterativeimputer "Link to this heading")

There are many well-established imputation packages in the R data science ecosystem: Amelia, mi, mice, missForest, etc. missForest is popular, and turns out to be a particular instance of different sequential imputation algorithms that can all be implemented with [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 by passing in different regressors to be used for predicting missing feature values. In the case of missForest, this regressor is a Random Forest. See [Imputing missing values with variants of IterativeImputer](https://scikit-learn.org/stable/auto_examples/impute/plot_iterative_imputer_variants_comparison.html#sphx-glr-auto-examples-impute-plot-iterative-imputer-variants-comparison-py)
.

### 8.4.3.2. Multiple vs. Single Imputation[#](https://scikit-learn.org/stable/modules/impute.html#multiple-vs-single-imputation "Link to this heading")

In the statistics community, it is common practice to perform multiple imputations, generating, for example, `m` separate imputations for a single feature matrix. Each of these `m` imputations is then put through the subsequent analysis pipeline (e.g. feature engineering, clustering, regression, classification). The `m` final analysis results (e.g. held-out validation errors) allow the data scientist to obtain understanding of how analytic results may differ as a consequence of the inherent uncertainty caused by the missing values. The above practice is called multiple imputation.

Our implementation of [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 was inspired by the R MICE package (Multivariate Imputation by Chained Equations) [\[1\]](https://scikit-learn.org/stable/modules/impute.html#id3)
, but differs from it by returning a single imputation instead of multiple imputations. However, [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 can also be used for multiple imputations by applying it repeatedly to the same dataset with different random seeds when `sample_posterior=True`. See [\[2\]](https://scikit-learn.org/stable/modules/impute.html#id4)
, chapter 4 for more discussion on multiple vs. single imputations.

It is still an open problem as to how useful single vs. multiple imputation is in the context of prediction and classification when the user is not interested in measuring uncertainty due to missing values.

Note that a call to the `transform` method of [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 is not allowed to change the number of samples. Therefore multiple imputations cannot be achieved by a single call to `transform`.

References

8.4.4. Nearest neighbors imputation[#](https://scikit-learn.org/stable/modules/impute.html#nearest-neighbors-imputation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

The [`KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")
 class provides imputation for filling in missing values using the k-Nearest Neighbors approach. By default, a euclidean distance metric that supports missing values, [`nan_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#sklearn.metrics.pairwise.nan_euclidean_distances "sklearn.metrics.pairwise.nan_euclidean_distances")
, is used to find the nearest neighbors. Each missing feature is imputed using values from `n_neighbors` nearest neighbors that have a value for the feature. The feature of the neighbors are averaged uniformly or weighted by distance to each neighbor. If a sample has more than one feature missing, then the neighbors for that sample can be different depending on the particular feature being imputed. When the number of available neighbors is less than `n_neighbors` and there are no defined distances to the training set, the training set average for that feature is used during imputation. If there is at least one neighbor with a defined distance, the weighted or unweighted average of the remaining neighbors will be used during imputation. If a feature is always missing in training, it is removed during `transform`. For more information on the methodology, see ref. [\[OL2001\]](https://scikit-learn.org/stable/modules/impute.html#ol2001)
.

The following snippet demonstrates how to replace missing values, encoded as `np.nan`, using the mean feature value of the two nearest neighbors of samples with missing values:

\>>> import numpy as np
\>>> from sklearn.impute import KNNImputer
\>>> nan \= np.nan
\>>> X \= \[\[1, 2, nan\], \[3, 4, 3\], \[nan, 6, 5\], \[8, 8, 7\]\]
\>>> imputer \= KNNImputer(n\_neighbors\=2, weights\="uniform")
\>>> imputer.fit\_transform(X)
array(\[\[1. , 2. , 4. \],\
       \[3. , 4. , 3. \],\
       \[5.5, 6. , 5. \],\
       \[8. , 8. , 7. \]\])

Copy to clipboard

For another example on usage, see [Imputing missing values before building an estimator](https://scikit-learn.org/stable/auto_examples/impute/plot_missing_values.html#sphx-glr-auto-examples-impute-plot-missing-values-py)
.

References

\[[OL2001](https://scikit-learn.org/stable/modules/impute.html#id5)\
\]

[Olga Troyanskaya, Michael Cantor, Gavin Sherlock, Pat Brown, Trevor Hastie, Robert Tibshirani, David Botstein and Russ B. Altman, Missing value estimation methods for DNA microarrays, BIOINFORMATICS Vol. 17 no. 6, 2001 Pages 520-525.](https://academic.oup.com/bioinformatics/article/17/6/520/272365)

8.4.5. Keeping the number of features constant[#](https://scikit-learn.org/stable/modules/impute.html#keeping-the-number-of-features-constant "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, the scikit-learn imputers will drop fully empty features, i.e. columns containing only missing values. For instance:

\>>> imputer \= SimpleImputer()
\>>> X \= np.array(\[\[np.nan, 1\], \[np.nan, 2\], \[np.nan, 3\]\])
\>>> imputer.fit\_transform(X)
array(\[\[1.\],\
       \[2.\],\
       \[3.\]\])

Copy to clipboard

The first feature in `X` containing only `np.nan` was dropped after the imputation. While this feature will not help in predictive setting, dropping the columns will change the shape of `X` which could be problematic when using imputers in a more complex machine-learning pipeline. The parameter `keep_empty_features` offers the option to keep the empty features by imputing with a constant value. In most of the cases, this constant value is zero:

\>>> imputer.set\_params(keep\_empty\_features\=True)
SimpleImputer(keep\_empty\_features=True)
\>>> imputer.fit\_transform(X)
array(\[\[0., 1.\],\
       \[0., 2.\],\
       \[0., 3.\]\])

Copy to clipboard

8.4.6. Marking imputed values[#](https://scikit-learn.org/stable/modules/impute.html#marking-imputed-values "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

The [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
 transformer is useful to transform a dataset into corresponding binary matrix indicating the presence of missing values in the dataset. This transformation is useful in conjunction with imputation. When using imputation, preserving the information about which values had been missing can be informative. Note that both the [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
 and [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer")
 have the boolean parameter `add_indicator` (`False` by default) which when set to `True` provides a convenient way of stacking the output of the [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
 transformer with the output of the imputer.

`NaN` is usually used as the placeholder for missing values. However, it enforces the data type to be float. The parameter `missing_values` allows to specify other placeholder such as integer. In the following example, we will use `-1` as missing values:

\>>> from sklearn.impute import MissingIndicator
\>>> X \= np.array(\[\[\-1, \-1, 1, 3\],\
...               \[4, \-1, 0, \-1\],\
...               \[8, \-1, 1, 0\]\])
\>>> indicator \= MissingIndicator(missing\_values\=-1)
\>>> mask\_missing\_values\_only \= indicator.fit\_transform(X)
\>>> mask\_missing\_values\_only
array(\[\[ True,  True, False\],\
       \[False,  True,  True\],\
       \[False,  True, False\]\])

Copy to clipboard

The `features` parameter is used to choose the features for which the mask is constructed. By default, it is `'missing-only'` which returns the imputer mask of the features containing missing values at `fit` time:

\>>> indicator.features\_
array(\[0, 1, 3\])

Copy to clipboard

The `features` parameter can be set to `'all'` to return all features whether or not they contain missing values:

\>>> indicator \= MissingIndicator(missing\_values\=-1, features\="all")
\>>> mask\_all \= indicator.fit\_transform(X)
\>>> mask\_all
array(\[\[ True,  True, False, False\],\
       \[False,  True, False,  True\],\
       \[False,  True, False, False\]\])
\>>> indicator.features\_
array(\[0, 1, 2, 3\])

Copy to clipboard

When using the [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
 in a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
, be sure to use the [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 or [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 to add the indicator features to the regular features. First we obtain the `iris` dataset, and add some missing values to it.

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.impute import SimpleImputer, MissingIndicator
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.pipeline import FeatureUnion, make\_pipeline
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> X, y \= load\_iris(return\_X\_y\=True)
\>>> mask \= np.random.randint(0, 2, size\=X.shape).astype(bool)
\>>> X\[mask\] \= np.nan
\>>> X\_train, X\_test, y\_train, \_ \= train\_test\_split(X, y, test\_size\=100,
...                                                random\_state\=0)

Copy to clipboard

Now we create a [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
. All features will be imputed using [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
, in order to enable classifiers to work with this data. Additionally, it adds the indicator variables from [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
.

\>>> transformer \= FeatureUnion(
...     transformer\_list\=\[\
...         ('features', SimpleImputer(strategy\='mean')),\
...         ('indicators', MissingIndicator())\])
\>>> transformer \= transformer.fit(X\_train, y\_train)
\>>> results \= transformer.transform(X\_test)
\>>> results.shape
(100, 8)

Copy to clipboard

Of course, we cannot use the transformer to make any predictions. We should wrap this in a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 with a classifier (e.g., a [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
) to be able to make predictions.

\>>> clf \= make\_pipeline(transformer, DecisionTreeClassifier())
\>>> clf \= clf.fit(X\_train, y\_train)
\>>> results \= clf.predict(X\_test)
\>>> results.shape
(100,)

Copy to clipboard

8.4.7. Estimators that handle NaN values[#](https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Some estimators are designed to handle NaN values without preprocessing. Below is the list of these estimators, classified by type (cluster, regressor, classifier, transform):

*   **Estimators that allow NaN values for type** `cluster`**:**
    *   [HDBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html)
        
*   **Estimators that allow NaN values for type** `regressor`**:**
    *   [BaggingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html)
        
    *   [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html)
        
    *   [ExtraTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html)
        
    *   [ExtraTreesRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html)
        
    *   [HistGradientBoostingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)
        
    *   [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
        
    *   [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html)
        
    *   [VotingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html)
        
*   **Estimators that allow NaN values for type** `classifier`**:**
    *   [BaggingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html)
        
    *   [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
        
    *   [ExtraTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html)
        
    *   [ExtraTreesClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html)
        
    *   [HistGradientBoostingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html)
        
    *   [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
        
    *   [StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html)
        
    *   [VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html)
        
*   **Estimators that allow NaN values for type** `transformer`**:**
    *   [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html)
        
    *   [KNNImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html)
        
    *   [MaxAbsScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html)
        
    *   [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
        
    *   [MissingIndicator](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html)
        
    *   [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
        
    *   [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html)
        
    *   [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html)
        
    *   [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)
        
    *   [RandomTreesEmbedding](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html)
        
    *   [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)
        
    *   [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
        
    *   [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html)
        
    *   [StackingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html)
        
    *   [StackingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html)
        
    *   [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
        
    *   [TargetEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html)
        
    *   [VarianceThreshold](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html)
        
    *   [VotingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html)
        
    *   [VotingRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html)
        

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)