[Skip to main content](https://scikit-learn.org/stable/modules/compose.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/compose.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/compose.html)
[1.8.0](https://scikit-learn.org/1.8/modules/compose.html)
[1.7.2](https://scikit-learn.org/1.7/modules/compose.html)
[1.6.1](https://scikit-learn.org/1.6/modules/compose.html)
[1.5.2](https://scikit-learn.org/1.5/modules/compose.html)
[1.4.2](https://scikit-learn.org/1.4/modules/compose.html)

Collapse Sidebar Expand Sidebar

8.1. Pipelines and composite estimators[#](https://scikit-learn.org/stable/modules/compose.html#pipelines-and-composite-estimators "Link to this heading")

===========================================================================================================================================================

To build a composite estimator, transformers are usually combined with other transformers or with [predictors](https://scikit-learn.org/stable/glossary.html#term-predictors)
 (such as classifiers or regressors). The most common tool used for composing estimators is a [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline)
. Pipelines require all steps except the last to be a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer)
. The last step can be anything, a transformer, a [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor)
, or a clustering estimator which might have or not have a `.predict(...)` method. A pipeline exposes all methods provided by the last estimator: if the last step provides a `transform` method, then the pipeline would have a `transform` method and behave like a transformer. If the last step provides a `predict` method, then the pipeline would expose that method, and given a data [X](https://scikit-learn.org/stable/glossary.html#term-X)
, use all steps except the last to transform the data, and then give that transformed data to the `predict` method of the last step of the pipeline. The class `Pipeline` is often used in combination with [ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html#column-transformer)
 or [FeatureUnion](https://scikit-learn.org/stable/modules/compose.html#feature-union)
 which concatenate the output of transformers into a composite feature space. [TransformedTargetRegressor](https://scikit-learn.org/stable/modules/compose.html#transformed-target-regressor)
 deals with transforming the [target](https://scikit-learn.org/stable/glossary.html#term-target)
 (i.e. log-transform [y](https://scikit-learn.org/stable/glossary.html#term-y)
).

8.1.1. Pipeline: chaining estimators[#](https://scikit-learn.org/stable/modules/compose.html#pipeline-chaining-estimators "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

[`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 can be used to chain multiple estimators into one. This is useful as there is often a fixed sequence of steps in processing the data, for example feature selection, normalization and classification. [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 serves multiple purposes here:

Convenience and encapsulation

You only have to call [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
 and [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
 once on your data to fit a whole sequence of estimators.

Joint parameter selection

You can [grid search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
 over parameters of all estimators in the pipeline at once.

Safety

Pipelines help avoid leaking statistics from your test data into the trained model in cross-validation, by ensuring that the same samples are used to train the transformers and predictors.

All estimators in a pipeline, except the last one, must be transformers (i.e. must have a [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
 method). The last estimator may be any type (transformer, classifier, etc.).

Note

Calling `fit` on the pipeline is the same as calling `fit` on each estimator in turn, `transform` the input and pass it on to the next step. The pipeline has all the methods that the last estimator in the pipeline has, i.e. if the last estimator is a classifier, the [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 can be used as a classifier. If the last estimator is a transformer, again, so is the pipeline.

### 8.1.1.1. Usage[#](https://scikit-learn.org/stable/modules/compose.html#usage "Link to this heading")

#### 8.1.1.1.1. Build a pipeline[#](https://scikit-learn.org/stable/modules/compose.html#build-a-pipeline "Link to this heading")

The [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 is built using a list of `(key, value)` pairs, where the `key` is a string containing the name you want to give this step and `value` is an estimator object:

\>>> from sklearn.pipeline import Pipeline
\>>> from sklearn.svm import SVC
\>>> from sklearn.decomposition import PCA
\>>> estimators \= \[('reduce\_dim', PCA()), ('clf', SVC())\]
\>>> pipe \= Pipeline(estimators)
\>>> pipe
Pipeline(steps=\[('reduce\_dim', PCA()), ('clf', SVC())\])

Copy to clipboard

Shorthand version using [`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
[#](https://scikit-learn.org/stable/modules/compose.html#shorthand-version-using-make_pipeline "Link to this dropdown")

The utility function [`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
 is a shorthand for constructing pipelines; it takes a variable number of estimators and returns a pipeline, filling in the names automatically:

\>>> from sklearn.pipeline import make\_pipeline
\>>> make\_pipeline(PCA(), SVC())
Pipeline(steps=\[('pca', PCA()), ('svc', SVC())\])

Copy to clipboard

#### 8.1.1.1.2. Access pipeline steps[#](https://scikit-learn.org/stable/modules/compose.html#access-pipeline-steps "Link to this heading")

The estimators of a pipeline are stored as a list in the `steps` attribute. A sub-pipeline can be extracted using the slicing notation commonly used for Python Sequences such as lists or strings (although only a step of 1 is permitted). This is convenient for performing only some of the transformations (or their inverse):

\>>> pipe\[:1\]
Pipeline(steps=\[('reduce\_dim', PCA())\])
\>>> pipe\[\-1:\]
Pipeline(steps=\[('clf', SVC())\])

Copy to clipboard

Accessing a step by name or position[#](https://scikit-learn.org/stable/modules/compose.html#accessing-a-step-by-name-or-position "Link to this dropdown")

A specific step can also be accessed by index or name by indexing (with `[idx]`) the pipeline:

\>>> pipe.steps\[0\]
('reduce\_dim', PCA())
\>>> pipe\[0\]
PCA()
\>>> pipe\['reduce\_dim'\]
PCA()

Copy to clipboard

`Pipeline`’s `named_steps` attribute allows accessing steps by name with tab completion in interactive environments:

\>>> pipe.named\_steps.reduce\_dim is pipe\['reduce\_dim'\]
True

Copy to clipboard

#### 8.1.1.1.3. Tracking feature names in a pipeline[#](https://scikit-learn.org/stable/modules/compose.html#tracking-feature-names-in-a-pipeline "Link to this heading")

To enable model inspection, [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 has a `get_feature_names_out()` method, just like all transformers. You can use pipeline slicing to get the feature names going into each step:

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.feature\_selection import SelectKBest
\>>> iris \= load\_iris()
\>>> pipe \= Pipeline(steps\=\[\
...    ('select', SelectKBest(k\=2)),\
...    ('clf', LogisticRegression())\])
\>>> pipe.fit(iris.data, iris.target)
Pipeline(steps=\[('select', SelectKBest(...)), ('clf', LogisticRegression(...))\])
\>>> pipe\[:\-1\].get\_feature\_names\_out()
array(\['x2', 'x3'\], ...)

Copy to clipboard

Customize feature names[#](https://scikit-learn.org/stable/modules/compose.html#customize-feature-names "Link to this dropdown")

You can also provide custom feature names for the input data using `get_feature_names_out`:

\>>> pipe\[:\-1\].get\_feature\_names\_out(iris.feature\_names)
array(\['petal length (cm)', 'petal width (cm)'\], ...)

Copy to clipboard

#### 8.1.1.1.4. Access to nested parameters[#](https://scikit-learn.org/stable/modules/compose.html#access-to-nested-parameters "Link to this heading")

It is common to adjust the parameters of an estimator within a pipeline. This parameter is therefore nested because it belongs to a particular sub-step. Parameters of the estimators in the pipeline are accessible using the `<estimator>__<parameter>` syntax:

\>>> pipe \= Pipeline(steps\=\[("reduce\_dim", PCA()), ("clf", SVC())\])
\>>> pipe.set\_params(clf\_\_C\=10)
Pipeline(steps=\[('reduce\_dim', PCA()), ('clf', SVC(C=10))\])

Copy to clipboard

When does it matter?[#](https://scikit-learn.org/stable/modules/compose.html#when-does-it-matter? "Link to this dropdown")

This is particularly important for doing grid searches:

\>>> from sklearn.model\_selection import GridSearchCV
\>>> param\_grid \= dict(reduce\_dim\_\_n\_components\=\[2, 5, 10\],
...                   clf\_\_C\=\[0.1, 10, 100\])
\>>> grid\_search \= GridSearchCV(pipe, param\_grid\=param\_grid)

Copy to clipboard

Individual steps may also be replaced as parameters, and non-final steps may be ignored by setting them to `'passthrough'`:

\>>> param\_grid \= dict(reduce\_dim\=\['passthrough', PCA(5), PCA(10)\],
...                   clf\=\[SVC(), LogisticRegression()\],
...                   clf\_\_C\=\[0.1, 10, 100\])
\>>> grid\_search \= GridSearchCV(pipe, param\_grid\=param\_grid)

Copy to clipboard

See also

*   [Composite estimators and parameter spaces](https://scikit-learn.org/stable/modules/grid_search.html#composite-grid-search)
    

Examples

*   [Pipeline ANOVA SVM](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection_pipeline.html#sphx-glr-auto-examples-feature-selection-plot-feature-selection-pipeline-py)
    
*   [Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html#sphx-glr-auto-examples-model-selection-plot-grid-search-text-feature-extraction-py)
    
*   [Pipelining: chaining a PCA and a logistic regression](https://scikit-learn.org/stable/auto_examples/compose/plot_digits_pipe.html#sphx-glr-auto-examples-compose-plot-digits-pipe-py)
    
*   [Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#sphx-glr-auto-examples-miscellaneous-plot-kernel-approximation-py)
    
*   [SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html#sphx-glr-auto-examples-svm-plot-svm-anova-py)
    
*   [Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#sphx-glr-auto-examples-compose-plot-compare-reduction-py)
    
*   [Displaying Pipelines](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_pipeline_display.html#sphx-glr-auto-examples-miscellaneous-plot-pipeline-display-py)
    

### 8.1.1.2. Caching transformers: avoid repeated computation[#](https://scikit-learn.org/stable/modules/compose.html#caching-transformers-avoid-repeated-computation "Link to this heading")

Fitting transformers may be computationally expensive. With its `memory` parameter set, [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 will cache each transformer after calling `fit`. This feature is used to avoid computing the fit transformers within a pipeline if the parameters and input data are identical. A typical example is the case of a grid search in which the transformers can be fitted only once and reused for each configuration. The last step will never be cached, even if it is a transformer.

The parameter `memory` is needed in order to cache the transformers. `memory` can be either a string containing the directory where to cache the transformers or a [joblib.Memory](https://joblib.readthedocs.io/en/latest/memory.html)
 object:

\>>> from tempfile import mkdtemp
\>>> from shutil import rmtree
\>>> from sklearn.decomposition import PCA
\>>> from sklearn.svm import SVC
\>>> from sklearn.pipeline import Pipeline
\>>> estimators \= \[('reduce\_dim', PCA()), ('clf', SVC())\]
\>>> cachedir \= mkdtemp()
\>>> pipe \= Pipeline(estimators, memory\=cachedir)
\>>> pipe
Pipeline(memory=...,
         steps=\[('reduce\_dim', PCA()), ('clf', SVC())\])
\>>> \# Clear the cache directory when you don't need it anymore
\>>> rmtree(cachedir)

Copy to clipboard

Side effect of caching transformers[#](https://scikit-learn.org/stable/modules/compose.html#side-effect-of-caching-transformers "Link to this dropdown")

Using a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 without cache enabled, it is possible to inspect the original instance such as:

\>>> from sklearn.datasets import load\_digits
\>>> X\_digits, y\_digits \= load\_digits(return\_X\_y\=True)
\>>> pca1 \= PCA(n\_components\=10)
\>>> svm1 \= SVC()
\>>> pipe \= Pipeline(\[('reduce\_dim', pca1), ('clf', svm1)\])
\>>> pipe.fit(X\_digits, y\_digits)
Pipeline(steps=\[('reduce\_dim', PCA(n\_components=10)), ('clf', SVC())\])
\>>> \# The pca instance can be inspected directly
\>>> pca1.components\_.shape
(10, 64)

Copy to clipboard

Enabling caching triggers a clone of the transformers before fitting. Therefore, the transformer instance given to the pipeline cannot be inspected directly. In the following example, accessing the [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 instance `pca2` will raise an `AttributeError` since `pca2` will be an unfitted transformer. Instead, use the attribute `named_steps` to inspect estimators within the pipeline:

\>>> cachedir \= mkdtemp()
\>>> pca2 \= PCA(n\_components\=10)
\>>> svm2 \= SVC()
\>>> cached\_pipe \= Pipeline(\[('reduce\_dim', pca2), ('clf', svm2)\],
...                        memory\=cachedir)
\>>> cached\_pipe.fit(X\_digits, y\_digits)
Pipeline(memory=...,
         steps=\[('reduce\_dim', PCA(n\_components=10)), ('clf', SVC())\])
\>>> cached\_pipe.named\_steps\['reduce\_dim'\].components\_.shape
(10, 64)
\>>> \# Remove the cache directory
\>>> rmtree(cachedir)

Copy to clipboard

Examples

*   [Selecting dimensionality reduction with Pipeline and GridSearchCV](https://scikit-learn.org/stable/auto_examples/compose/plot_compare_reduction.html#sphx-glr-auto-examples-compose-plot-compare-reduction-py)
    

8.1.2. Transforming target in regression[#](https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

[`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
 transforms the targets `y` before fitting a regression model. The predictions are mapped back to the original space via an inverse transform. It takes as an argument the regressor that will be used for prediction, and the transformer that will be applied to the target variable:

\>>> import numpy as np
\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.compose import TransformedTargetRegressor
\>>> from sklearn.preprocessing import QuantileTransformer
\>>> from sklearn.linear\_model import LinearRegression
\>>> from sklearn.model\_selection import train\_test\_split
\>>> \# create a synthetic dataset
\>>> X, y \= make\_regression(n\_samples\=20640,
...                        n\_features\=8,
...                        noise\=100.0,
...                        random\_state\=0)
\>>> y \= np.exp( 1 + (y \- y.min()) \* (4 / (y.max() \- y.min())))
\>>> X, y \= X\[:2000, :\], y\[:2000\]  \# select a subset of data
\>>> transformer \= QuantileTransformer(output\_distribution\='normal')
\>>> regressor \= LinearRegression()
\>>> regr \= TransformedTargetRegressor(regressor\=regressor,
...                                   transformer\=transformer)
\>>> X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y, random\_state\=0)
\>>> regr.fit(X\_train, y\_train)
TransformedTargetRegressor(...)
\>>> print(f"R2 score: {regr.score(X\_test, y\_test):.2f}")
R2 score: 0.67
\>>> raw\_target\_regr \= LinearRegression().fit(X\_train, y\_train)
\>>> print(f"R2 score: {raw\_target\_regr.score(X\_test, y\_test):.2f}")
R2 score: 0.64

Copy to clipboard

For simple transformations, instead of a Transformer object, a pair of functions can be passed, defining the transformation and its inverse mapping:

\>>> def func(x):
...     return np.log(x)
\>>> def inverse\_func(x):
...     return np.exp(x)

Copy to clipboard

Subsequently, the object is created as:

\>>> regr \= TransformedTargetRegressor(regressor\=regressor,
...                                   func\=func,
...                                   inverse\_func\=inverse\_func)
\>>> regr.fit(X\_train, y\_train)
TransformedTargetRegressor(...)
\>>> print(f"R2 score: {regr.score(X\_test, y\_test):.2f}")
R2 score: 0.67

Copy to clipboard

By default, the provided functions are checked at each fit to be the inverse of each other. However, it is possible to bypass this checking by setting `check_inverse` to `False`:

\>>> def inverse\_func(x):
...     return x
\>>> regr \= TransformedTargetRegressor(regressor\=regressor,
...                                   func\=func,
...                                   inverse\_func\=inverse\_func,
...                                   check\_inverse\=False)
\>>> regr.fit(X\_train, y\_train)
TransformedTargetRegressor(...)
\>>> print(f"R2 score: {regr.score(X\_test, y\_test):.2f}")
R2 score: -3.02

Copy to clipboard

Note

The transformation can be triggered by setting either `transformer` or the pair of functions `func` and `inverse_func`. However, setting both options will raise an error.

Examples

*   [Effect of transforming the targets in regression model](https://scikit-learn.org/stable/auto_examples/compose/plot_transformed_target.html#sphx-glr-auto-examples-compose-plot-transformed-target-py)
    

8.1.3. FeatureUnion: composite feature spaces[#](https://scikit-learn.org/stable/modules/compose.html#featureunion-composite-feature-spaces "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 combines several transformer objects into a new transformer that combines their output. A [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 takes a list of transformer objects. During fitting, each of these is fit to the data independently. The transformers are applied in parallel, and the feature matrices they output are concatenated side-by-side into a larger matrix.

When you want to apply different transformations to each field of the data, see the related class [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 (see [user guide](https://scikit-learn.org/stable/modules/compose.html#column-transformer)
).

[`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 serves the same purposes as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 - convenience and joint parameter estimation and validation.

[`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 and [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 can be combined to create complex models.

(A [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 has no way of checking whether two transformers might produce identical features. It only produces a union when the feature sets are disjoint, and making sure they are is the caller’s responsibility.)

### 8.1.3.1. Usage[#](https://scikit-learn.org/stable/modules/compose.html#id1 "Link to this heading")

A [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
 is built using a list of `(key, value)` pairs, where the `key` is the name you want to give to a given transformation (an arbitrary string; it only serves as an identifier) and `value` is an estimator object:

\>>> from sklearn.pipeline import FeatureUnion
\>>> from sklearn.decomposition import PCA
\>>> from sklearn.decomposition import KernelPCA
\>>> estimators \= \[('linear\_pca', PCA()), ('kernel\_pca', KernelPCA())\]
\>>> combined \= FeatureUnion(estimators)
\>>> combined
FeatureUnion(transformer\_list=\[('linear\_pca', PCA()),\
                               ('kernel\_pca', KernelPCA())\])

Copy to clipboard

Like pipelines, feature unions have a shorthand constructor called [`make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union")
 that does not require explicit naming of the components.

Like `Pipeline`, individual steps may be replaced using `set_params`, and ignored by setting to `'drop'`:

\>>> combined.set\_params(kernel\_pca\='drop')
FeatureUnion(transformer\_list=\[('linear\_pca', PCA()),\
                               ('kernel\_pca', 'drop')\])

Copy to clipboard

Examples

*   [Concatenating multiple feature extraction methods](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html#sphx-glr-auto-examples-compose-plot-feature-union-py)
    

8.1.4. ColumnTransformer for heterogeneous data[#](https://scikit-learn.org/stable/modules/compose.html#columntransformer-for-heterogeneous-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many datasets contain features of different types, say text, floats, and dates, where each type of feature requires separate preprocessing or feature extraction steps. Often it is easiest to preprocess data before applying scikit-learn methods, for example using [pandas](https://pandas.pydata.org/)
. Processing your data before passing it to scikit-learn might be problematic for one of the following reasons:

1.  Incorporating statistics from test data into the preprocessors makes cross-validation scores unreliable (known as _data leakage_), for example in the case of scalers or imputing missing values.
    
2.  You may want to include the parameters of the preprocessors in a [parameter search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
    .
    

The [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 helps performing different transformations for different columns of the data, within a [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 that is safe from data leakage and that can be parametrized. [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 works on arrays, sparse matrices, and [pandas DataFrames](https://pandas.pydata.org/pandas-docs/stable/)
.

To each column, a different transformation can be applied, such as preprocessing or a specific feature extraction method:

\>>> import pandas as pd
\>>> X \= pd.DataFrame(
...     {'city': \['London', 'London', 'Paris', 'Sallisaw'\],
...      'title': \["His Last Bow", "How Watson Learned the Trick",\
...                "A Moveable Feast", "The Grapes of Wrath"\],
...      'expert\_rating': \[5, 3, 4, 5\],
...      'user\_rating': \[4, 5, 4, 3\]})

Copy to clipboard

For this data, we might want to encode the `'city'` column as a categorical variable using [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 but apply a [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 to the `'title'` column. As we might use multiple feature extraction methods on the same column, we give each transformer a unique name, say `'city_category'` and `'title_bow'`. By default, the remaining rating columns are ignored (`remainder='drop'`):

\>>> from sklearn.compose import ColumnTransformer
\>>> from sklearn.feature\_extraction.text import CountVectorizer
\>>> from sklearn.preprocessing import OneHotEncoder
\>>> column\_trans \= ColumnTransformer(
...     \[('categories', OneHotEncoder(dtype\='int'), \['city'\]),\
...      ('title\_bow', CountVectorizer(), 'title')\],
...     remainder\='drop', verbose\_feature\_names\_out\=False)

\>>> column\_trans.fit(X)
ColumnTransformer(transformers=\[('categories', OneHotEncoder(dtype='int'),\
                                 \['city'\]),\
                                ('title\_bow', CountVectorizer(), 'title')\],
                  verbose\_feature\_names\_out=False)

\>>> column\_trans.get\_feature\_names\_out()
array(\['city\_London', 'city\_Paris', 'city\_Sallisaw', 'bow', 'feast',\
'grapes', 'his', 'how', 'last', 'learned', 'moveable', 'of', 'the',\
 'trick', 'watson', 'wrath'\], ...)

\>>> column\_trans.transform(X).toarray()
array(\[\[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0\],\
       \[1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0\],\
       \[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0\],\
       \[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1\]\]...)

Copy to clipboard

In the above example, the [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 expects a 1D array as input and therefore the columns were specified as a string (`'title'`). However, [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 as most of other transformers expects 2D data, therefore in that case you need to specify the column as a list of strings (`['city']`).

Apart from a scalar or a single item list, the column selection can be specified as a list of multiple items, an integer array, a slice, a boolean mask, or with a [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
. The [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")
 is used to select columns based on data type or column name:

\>>> from sklearn.preprocessing import StandardScaler
\>>> from sklearn.compose import make\_column\_selector
\>>> ct \= ColumnTransformer(\[\
...       ('scale', StandardScaler(),\
...       make\_column\_selector(dtype\_include\=np.number)),\
...       ('onehot',\
...       OneHotEncoder(),\
...       make\_column\_selector(pattern\='city', dtype\_include\=\[object, "string"\]))\])
\>>> ct.fit\_transform(X)
array(\[\[ 0.904,  0.      ,  1. ,  0. ,  0. \],\
       \[-1.507,  1.414,  1. ,  0. ,  0. \],\
       \[-0.301,  0.      ,  0. ,  1. ,  0. \],\
       \[ 0.904, -1.414,  0. ,  0. ,  1. \]\])

Copy to clipboard

Strings can reference columns if the input is a DataFrame, integers are always interpreted as the positional columns.

We can keep the remaining rating columns by setting `remainder='passthrough'`. The values are appended to the end of the transformation:

\>>> column\_trans \= ColumnTransformer(
...     \[('city\_category', OneHotEncoder(dtype\='int'),\['city'\]),\
...      ('title\_bow', CountVectorizer(), 'title')\],
...     remainder\='passthrough')

\>>> column\_trans.fit\_transform(X)
array(\[\[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5, 4\],\
       \[1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 3, 5\],\
       \[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 4, 4\],\
       \[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 5, 3\]\]...)

Copy to clipboard

The `remainder` parameter can be set to an estimator to transform the remaining rating columns. The transformed values are appended to the end of the transformation:

\>>> from sklearn.preprocessing import MinMaxScaler
\>>> column\_trans \= ColumnTransformer(
...     \[('city\_category', OneHotEncoder(), \['city'\]),\
...      ('title\_bow', CountVectorizer(), 'title')\],
...     remainder\=MinMaxScaler())

\>>> column\_trans.fit\_transform(X)\[:, \-2:\]
array(\[\[1. , 0.5\],\
       \[0. , 1. \],\
       \[0.5, 0.5\],\
       \[1. , 0. \]\])

Copy to clipboard

The [`make_column_transformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")
 function is available to more easily create a [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 object. Specifically, the names will be given automatically. The equivalent for the above example would be:

\>>> from sklearn.compose import make\_column\_transformer
\>>> column\_trans \= make\_column\_transformer(
...     (OneHotEncoder(), \['city'\]),
...     (CountVectorizer(), 'title'),
...     remainder\=MinMaxScaler())
\>>> column\_trans
ColumnTransformer(remainder=MinMaxScaler(),
                  transformers=\[('onehotencoder', OneHotEncoder(), \['city'\]),\
                                ('countvectorizer', CountVectorizer(),\
                                 'title')\])

Copy to clipboard

If [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 is fitted with a dataframe and the dataframe only has string column names, then transforming a dataframe will use the column names to select the columns:

\>>> ct \= ColumnTransformer(
...          \[("scale", StandardScaler(), \["expert\_rating"\])\]).fit(X)
\>>> X\_new \= pd.DataFrame({"expert\_rating": \[5, 6, 1\],
...                       "ignored\_new\_col": \[1.2, 0.3, \-0.1\]})
\>>> ct.transform(X\_new)
array(\[\[ 0.9\],\
       \[ 2.1\],\
       \[-3.9\]\])

Copy to clipboard

8.1.5. Visualizing Composite Estimators[#](https://scikit-learn.org/stable/modules/compose.html#visualizing-composite-estimators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Estimators are displayed with an HTML representation when shown in a jupyter notebook. This is useful to diagnose or visualize a Pipeline with many estimators. This visualization is activated by default:

\>>> column\_trans

Copy to clipboard

It can be deactivated by setting the `display` option in [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
 to ‘text’:

\>>> from sklearn import set\_config
\>>> set\_config(display\='text')
\>>> \# displays text representation in a jupyter context
\>>> column\_trans

Copy to clipboard

An example of the HTML output can be seen in the **HTML representation of Pipeline** section of [Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-auto-examples-compose-plot-column-transformer-mixed-types-py)
. As an alternative, the HTML can be written to a file using [`estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr")
:

\>>> from sklearn.utils import estimator\_html\_repr
\>>> with open('my\_estimator.html', 'w') as f:
...     f.write(estimator\_html\_repr(clf))

Copy to clipboard

Examples

*   [Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#sphx-glr-auto-examples-compose-plot-column-transformer-py)
    
*   [Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-auto-examples-compose-plot-column-transformer-mixed-types-py)
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)