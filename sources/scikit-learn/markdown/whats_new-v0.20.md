[Skip to main content](https://scikit-learn.org/stable/whats_new/v0.20.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v0.20.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v0.20.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v0.20.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v0.20.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v0.20.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v0.20.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v0.20.html)

Collapse Sidebar Expand Sidebar

Version 0.20[#](https://scikit-learn.org/stable/whats_new/v0.20.html#version-0-20 "Link to this heading")

==========================================================================================================

Warning

Version 0.20 is the last version of scikit-learn to support Python 2.7 and Python 3.4. Scikit-learn 0.21 will require Python 3.5 or higher.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 0.20.4[#](https://scikit-learn.org/stable/whats_new/v0.20.html#version-0-20-4 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**July 30, 2019**

This is a bug-fix release with some bug fixes applied to version 0.20.3.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.20.html#changelog "Link to this heading")

The bundled version of joblib was upgraded from 0.13.0 to 0.13.2.

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-cluster "Link to this heading")

*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where KMeans++ initialisation could rarely result in an IndexError. [#11756](https://github.com/scikit-learn/scikit-learn/issues/11756)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-compose "Link to this heading")

*   Fix Fixed an issue in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     where using DataFrames whose column order differs between `fit` and `transform` could lead to silently passing incorrect columns to the `remainder` transformer. [#14237](https://github.com/scikit-learn/scikit-learn/pull/14237)
     by `Andreas Schuderer <schuderer>`.
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-decomposition "Link to this heading")

*   Fix Fixed a bug in [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
     improving numerical stability when `Y` is close to zero. [#13903](https://github.com/scikit-learn/scikit-learn/pull/13903)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-model-selection "Link to this heading")

*   Fix Fixed a bug where [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     shuffles each class’s samples with the same `random_state`, making `shuffle=True` ineffective. [#13124](https://github.com/scikit-learn/scikit-learn/issues/13124)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-neighbors "Link to this heading")

*   Fix Fixed a bug in [`neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
     which could not be restored from a pickle if `sample_weight` had been used. [#13772](https://github.com/scikit-learn/scikit-learn/issues/13772)
     by [Aditya Vyas](https://github.com/aditya1702)
    .
    

Version 0.20.3[#](https://scikit-learn.org/stable/whats_new/v0.20.html#version-0-20-3 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**March 1, 2019**

This is a bug-fix release with some minor documentation improvements and enhancements to features released in 0.20.0.

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id1 "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id2 "Link to this heading")

*   Fix Fixed a bug in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     where computation was single threaded when `n_jobs > 1` or `n_jobs = -1`. [#12949](https://github.com/scikit-learn/scikit-learn/issues/12949)
     by [Prabakaran Kumaresshan](https://github.com/nixphix)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id3 "Link to this heading")

*   Fix Fixed a bug in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     to handle negative indexes in the columns list of the transformers. [#12946](https://github.com/scikit-learn/scikit-learn/issues/12946)
     by [Pierre Tallotte](https://github.com/pierretallotte)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-covariance "Link to this heading")

*   Fix Fixed a regression in [`covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
     so that the case `n_features=2` is handled correctly. [#13276](https://github.com/scikit-learn/scikit-learn/issues/13276)
     by [Aurélien Bellet](https://github.com/bellet)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id4 "Link to this heading")

*   Fix Fixed a bug in [`decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
     where computation was single threaded when `n_jobs > 1` or `n_jobs = -1`. [#13005](https://github.com/scikit-learn/scikit-learn/issues/13005)
     by [Prabakaran Kumaresshan](https://github.com/nixphix)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-datasets "Link to this heading")

*   Efficiency [`sklearn.datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     now loads data by streaming, avoiding high memory usage. [#13312](https://github.com/scikit-learn/scikit-learn/issues/13312)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-feature-extraction "Link to this heading")

*   Fix Fixed a bug in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     which would result in the sparse feature matrix having conflicting `indptr` and `indices` precisions under very large vocabularies. [#11295](https://github.com/scikit-learn/scikit-learn/issues/11295)
     by [Gabriel Vacaliuc](https://github.com/gvacaliuc)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-impute "Link to this heading")

*   Fix add support for non-numeric data in [`sklearn.impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
     which was not supported while [`sklearn.impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     was supporting this for some imputation strategies. [#13046](https://github.com/scikit-learn/scikit-learn/issues/13046)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-linear-model "Link to this heading")

*   Fix Fixed a bug in [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
     and [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
     which were breaking when `warm_start = True`. [#12360](https://github.com/scikit-learn/scikit-learn/issues/12360)
     by [Aakanksha Joshi](https://github.com/joaak)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-preprocessing "Link to this heading")

*   Fix Fixed a bug in [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     where `strategy='kmeans'` fails with an error during transformation due to unsorted bin edges. [#13134](https://github.com/scikit-learn/scikit-learn/issues/13134)
     by [Sandro Casagrande](https://github.com/SandroCasagrande)
    .
    
*   Fix Fixed a bug in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     where the deprecation of `categorical_features` was handled incorrectly in combination with `handle_unknown='ignore'`. [#12881](https://github.com/scikit-learn/scikit-learn/issues/12881)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   Fix Bins whose width are too small (i.e., <= 1e-8) are removed with a warning in [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
    . [#13165](https://github.com/scikit-learn/scikit-learn/issues/13165)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-svm "Link to this heading")

*   Fix Fixed a bug in [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`svm.NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
     and [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     where the `scale` option of parameter `gamma` is erroneously defined as `1 / (n_features * X.std())`. It’s now defined as `1 / (n_features * X.var())`. [#13221](https://github.com/scikit-learn/scikit-learn/issues/13221)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

### Code and Documentation Contributors[#](https://scikit-learn.org/stable/whats_new/v0.20.html#code-and-documentation-contributors "Link to this heading")

With thanks to:

Adrin Jalali, Agamemnon Krasoulis, Albert Thomas, Andreas Mueller, Aurélien Bellet, bertrandhaut, Bharat Raghunathan, Dowon, Emmanuel Arias, Fibinse Xavier, Finn O’Shea, Gabriel Vacaliuc, Gael Varoquaux, Guillaume Lemaitre, Hanmin Qin, joaak, Joel Nothman, Joris Van den Bossche, Jérémie Méhault, kms15, Kossori Aruku, Lakshya KD, maikia, Manuel López-Ibáñez, Marco Gorelli, MarcoGorelli, mferrari3, Mickaël Schoentgen, Nicolas Hug, pavlos kallis, Pierre Glaser, pierretallotte, Prabakaran Kumaresshan, Reshama Shaikh, Rohit Kapoor, Roman Yurchak, SandroCasagrande, Tashay Green, Thomas Fan, Vishaal Kapoor, Zhuyi Xue, Zijie (ZJ) Poh

Version 0.20.2[#](https://scikit-learn.org/stable/whats_new/v0.20.html#version-0-20-2 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**December 20, 2018**

This is a bug-fix release with some minor documentation improvements and enhancements to features released in 0.20.0.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.20.html#changed-models "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
     when `metric=='jaccard'` (bug fix)
    
*   use of `'seuclidean'` or `'mahalanobis'` metrics in some cases (bug fix)
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id5 "Link to this heading")

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id6 "Link to this heading")

*   Fix Fixed an issue in [`compose.make_column_transformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")
     which raises unexpected error when columns is pandas Index or pandas Series. [#12704](https://github.com/scikit-learn/scikit-learn/issues/12704)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-metrics "Link to this heading")

*   Fix Fixed a bug in [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     and [`metrics.pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked")
     where parameters `V` of `"seuclidean"` and `VI` of `"mahalanobis"` metrics were computed after the data was split into chunks instead of being pre-computed on whole data. [#12701](https://github.com/scikit-learn/scikit-learn/issues/12701)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id7 "Link to this heading")

*   Fix Fixed `sklearn.neighbors.DistanceMetric` jaccard distance function to return 0 when two all-zero vectors are compared. [#12685](https://github.com/scikit-learn/scikit-learn/issues/12685)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-utils "Link to this heading")

*   Fix Calling [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     on `pandas.Series` with categorical data, which raised an error in 0.20.0, now returns the expected output again. [#12699](https://github.com/scikit-learn/scikit-learn/issues/12699)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    

### Code and Documentation Contributors[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id8 "Link to this heading")

With thanks to:

adanhawth, Adrin Jalali, Albert Thomas, Andreas Mueller, Dan Stine, Feda Curic, Hanmin Qin, Jan S, jeremiedbb, Joel Nothman, Joris Van den Bossche, josephsalmon, Katrin Leinweber, Loic Esteve, Muhammad Hassaan Rafique, Nicolas Hug, Olivier Grisel, Paul Paczuski, Reshama Shaikh, Sam Waterbury, Shivam Kotwalia, Thomas Fan

Version 0.20.1[#](https://scikit-learn.org/stable/whats_new/v0.20.html#version-0-20-1 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**November 21, 2018**

This is a bug-fix release with some minor documentation improvements and enhancements to features released in 0.20.0. Note that we also include some API changes in this release, so you might get some extra warnings after updating from 0.20.0 to 0.20.1.

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id9 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     (bug fix)
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id10 "Link to this heading")

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id11 "Link to this heading")

*   Efficiency make [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     no longer try to do nested parallelism as the overhead would hurt performance significantly when `n_jobs > 1`. [#12159](https://github.com/scikit-learn/scikit-learn/issues/12159)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Fix Fixed a bug in [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     with precomputed sparse neighbors graph, which would add explicitly zeros on the diagonal even when already present. [#12105](https://github.com/scikit-learn/scikit-learn/issues/12105)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id12 "Link to this heading")

*   Fix Fixed an issue in [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     when stacking columns with types not convertible to a numeric. [#11912](https://github.com/scikit-learn/scikit-learn/issues/11912)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   API Change [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now applies the `sparse_threshold` even if all transformation results are sparse. [#12304](https://github.com/scikit-learn/scikit-learn/issues/12304)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change [`compose.make_column_transformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")
     now expects `(transformer, columns)` instead of `(columns, transformer)` to keep consistent with [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    . [#12339](https://github.com/scikit-learn/scikit-learn/issues/12339)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id13 "Link to this heading")

*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     to correctly use the local cache. [#12246](https://github.com/scikit-learn/scikit-learn/issues/12246)
     by [Jan N. van Rijn](https://github.com/janvanrijn)
    .
    
*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     to correctly handle ignore attributes and row id attributes. [#12330](https://github.com/scikit-learn/scikit-learn/issues/12330)
     by [Jan N. van Rijn](https://github.com/janvanrijn)
    .
    
*   Fix Fixed integer overflow in [`datasets.make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
     for values of `n_informative` parameter larger than 64. [#10811](https://github.com/scikit-learn/scikit-learn/issues/10811)
     by [Roman Feldbauer](https://github.com/VarIr)
    .
    
*   Fix Fixed olivetti faces dataset `DESCR` attribute to point to the right location in [`datasets.fetch_olivetti_faces`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")
    . [#12441](https://github.com/scikit-learn/scikit-learn/issues/12441)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    
*   Fix [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     to retry downloading when reading from local cache fails. [#12517](https://github.com/scikit-learn/scikit-learn/issues/12517)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id14 "Link to this heading")

*   Fix Fixed a regression in [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     where 0.20.0 raised an error if the number of samples in the final batch for fitting IncrementalPCA was smaller than n\_components. [#12234](https://github.com/scikit-learn/scikit-learn/issues/12234)
     by [Ming Li](https://github.com/minggli)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-ensemble "Link to this heading")

*   Fix Fixed a bug mostly affecting [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
     where `class_weight='balanced_subsample'` failed with more than 32 classes. [#12165](https://github.com/scikit-learn/scikit-learn/issues/12165)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix Fixed a bug affecting [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     and [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    , where `max_features` was sometimes rounded down to zero. [#12388](https://github.com/scikit-learn/scikit-learn/issues/12388)
     by [Connor Tann](https://github.com/Connossor)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id15 "Link to this heading")

*   Fix Fixed a regression in v0.20.0 where [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     and other text vectorizers could error during stop words validation with custom preprocessors or tokenizers. [#12393](https://github.com/scikit-learn/scikit-learn/issues/12393)
     by [Roman Yurchak](https://github.com/rth)
    .
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id16 "Link to this heading")

*   Fix [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and variants with `early_stopping=True` would not use a consistent validation split in the multiclass case and this would cause a crash when using those estimators as part of parallel parameter search or cross-validation. [#12122](https://github.com/scikit-learn/scikit-learn/issues/12122)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   Fix Fixed a bug affecting [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     in the multiclass case. Each one-versus-all step is run in a [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
     call and mutating a common parameter, causing a segmentation fault if called within a backend using processes and not threads. We now use `require=sharedmem` at the [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.7)")
     instance creation. [#12518](https://github.com/scikit-learn/scikit-learn/issues/12518)
     by [Pierre Glaser](https://github.com/pierreglaser)
     and [Olivier Grisel](https://github.com/ogrisel)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id17 "Link to this heading")

*   Fix Fixed a bug in `metrics.pairwise.pairwise_distances_argmin_min` which returned the square root of the distance when the metric parameter was set to “euclidean”. [#12481](https://github.com/scikit-learn/scikit-learn/issues/12481)
     by [Jérémie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in `metrics.pairwise.pairwise_distances_chunked` which didn’t ensure the diagonal is zero for euclidean distances. [#12612](https://github.com/scikit-learn/scikit-learn/issues/12612)
     by [Andreas Müller](https://github.com/amueller)
    .
    
*   API Change The `metrics.calinski_harabaz_score` has been renamed to [`metrics.calinski_harabasz_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score "sklearn.metrics.calinski_harabasz_score")
     and will be removed in version 0.23. [#12211](https://github.com/scikit-learn/scikit-learn/issues/12211)
     by [Lisa Thomas](https://github.com/LisaThomas9)
    , [Mark Hannel](https://github.com/markhannel)
     and [Melissa Ferrari](https://github.com/mferrari3)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-mixture "Link to this heading")

*   Fix Ensure that the `fit_predict` method of [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     always yield assignments consistent with `fit` followed by `predict` even if the convergence criterion is too loose or not met. [#12451](https://github.com/scikit-learn/scikit-learn/issues/12451)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id18 "Link to this heading")

*   Fix force the parallelism backend to `threading` for [`neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     and [`neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     in Python 2.7 to avoid pickling errors caused by the serialization of their methods. [#12171](https://github.com/scikit-learn/scikit-learn/issues/12171)
     by [Thomas Moreau](https://github.com/tomMoral)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id19 "Link to this heading")

*   Fix Fixed bug in [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     when passing manually specified categories. [#12365](https://github.com/scikit-learn/scikit-learn/issues/12365)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   Fix Fixed bug in [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     where the `transform` method mutates the `_encoder` attribute. The `transform` method is now thread safe. [#12514](https://github.com/scikit-learn/scikit-learn/issues/12514)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug in [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     where the Yeo-Johnson transform was incorrect for lambda parameters outside of `[0, 2]` [#12522](https://github.com/scikit-learn/scikit-learn/issues/12522)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     where transform failed when set to ignore unknown numpy strings of different lengths [#12471](https://github.com/scikit-learn/scikit-learn/issues/12471)
     by [Gabriel Marzinotto](https://github.com/GMarzinotto)
    .
    
*   API Change The default value of the `method` argument in [`preprocessing.power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform")
     will be changed from `box-cox` to `yeo-johnson` to match [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
     in version 0.23. A FutureWarning is raised when the default value is used. [#12317](https://github.com/scikit-learn/scikit-learn/issues/12317)
     by [Eric Chang](https://github.com/chang)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id20 "Link to this heading")

*   Fix Use float64 for mean accumulator to avoid floating point precision issues in [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     and [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     when using float32 datasets. [#12338](https://github.com/scikit-learn/scikit-learn/issues/12338)
     by [bauks](https://github.com/bauks)
    .
    
*   Fix Calling [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     on `pandas.Series`, which raised an error in 0.20.0, now returns the expected output again. [#12625](https://github.com/scikit-learn/scikit-learn/issues/12625)
     by [Andreas Müller](https://amueller.github.io/)
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.20.html#miscellaneous "Link to this heading")

*   Fix When using site joblib by setting the environment variable `SKLEARN_SITE_JOBLIB`, added compatibility with joblib 0.11 in addition to 0.12+. [#12350](https://github.com/scikit-learn/scikit-learn/issues/12350)
     by [Joel Nothman](https://joelnothman.com/)
     and [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix Make sure to avoid raising `FutureWarning` when calling `np.vstack` with numpy 1.16 and later (use list comprehensions instead of generator expressions in many locations of the scikit-learn code base). [#12467](https://github.com/scikit-learn/scikit-learn/issues/12467)
     by [Olivier Grisel](https://github.com/ogrisel)
    .
    
*   API Change Removed all mentions of `sklearn.externals.joblib`, and deprecated joblib methods exposed in `sklearn.utils`, except for `utils.parallel_backend` and `utils.register_parallel_backend`, which allow users to configure parallel computation in scikit-learn. Other functionalities are part of [joblib](https://joblib.readthedocs.io/)
    . package and should be used directly, by installing it. The goal of this change is to prepare for unvendoring joblib in future version of scikit-learn. [#12345](https://github.com/scikit-learn/scikit-learn/issues/12345)
     by [Thomas Moreau](https://github.com/tomMoral)
    

### Code and Documentation Contributors[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id21 "Link to this heading")

With thanks to:

^\_\_^, Adrin Jalali, Andrea Navarrete, Andreas Mueller, bauks, BenjaStudio, Cheuk Ting Ho, Connossor, Corey Levinson, Dan Stine, daten-kieker, Denis Kataev, Dillon Gardner, Dmitry Vukolov, Dougal J. Sutherland, Edward J Brown, Eric Chang, Federico Caselli, Gabriel Marzinotto, Gael Varoquaux, GauravAhlawat, Gustavo De Mari Pereira, Hanmin Qin, haroldfox, JackLangerman, Jacopo Notarstefano, janvanrijn, jdethurens, jeremiedbb, Joel Nothman, Joris Van den Bossche, Koen, Kushal Chauhan, Lee Yi Jie Joel, Lily Xiong, mail-liam, Mark Hannel, melsyt, Ming Li, Nicholas Smith, Nicolas Hug, Nikolay Shebanov, Oleksandr Pavlyk, Olivier Grisel, Peter Hausamann, Pierre Glaser, Pulkit Maloo, Quentin Batista, Radostin Stoyanov, Ramil Nugmanov, Rebekah Kim, Reshama Shaikh, Rohan Singh, Roman Feldbauer, Roman Yurchak, Roopam Sharma, Sam Waterbury, Scott Lowe, Sebastian Raschka, Stephen Tierney, SylvainLan, TakingItCasual, Thomas Fan, Thomas Moreau, Tom Dupré la Tour, Tulio Casagrande, Utkarsh Upadhyay, Xing Han Lu, Yaroslav Halchenko, Zach Miller

Version 0.20.0[#](https://scikit-learn.org/stable/whats_new/v0.20.html#version-0-20-0 "Link to this heading")

--------------------------------------------------------------------------------------------------------------

**September 25, 2018**

This release packs in a mountain of bug fixes, features and enhancements for the Scikit-learn library, and improvements to the documentation and examples. Thanks to our contributors!

This release is dedicated to the memory of Raghav Rajagopalan.

### Highlights[#](https://scikit-learn.org/stable/whats_new/v0.20.html#highlights "Link to this heading")

We have tried to improve our support for common data-science use-cases including missing values, categorical variables, heterogeneous data, and features/targets with unusual distributions. Missing values in features, represented by NaNs, are now accepted in column-wise preprocessing such as scalers. Each feature is fitted disregarding NaNs, and data containing NaNs can be transformed. The new [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
 module provides estimators for learning despite missing data.

[`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 handles the case where different features or columns of a pandas.DataFrame need different preprocessing. String or pandas Categorical columns can now be encoded with [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 or [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
.

[`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
 helps when the regression target needs to be transformed to be modeled. [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
 and [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
 join [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
 as non-linear transformations.

Beyond this, we have added [sample\_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight)
 support to several estimators (including [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
, [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
 and [`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
) and improved stopping criteria in others (including [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
, [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
 and [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
).

This release is also the first to be accompanied by a [Glossary of Common Terms and API Elements](https://scikit-learn.org/stable/glossary.html#glossary)
 developed by [Joel Nothman](https://joelnothman.com/)
. The glossary is a reference resource to help users and contributors become familiar with the terminology and conventions used in Scikit-learn.

Sorry if your contribution didn’t make it into the highlights. There’s a lot here…

### Changed models[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id22 "Link to this heading")

The following estimators and functions, when fit with the same data and parameters, may produce different models from the previous version. This often occurs due to changes in the modelling logic (bug fixes or enhancements), or in random sampling procedures.

*   [`cluster.MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")
     (bug fix)
    
*   [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     in Python 2 (bug fix)
    
*   [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     (bug fix)
    
*   [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     (bug fix affecting feature importances)
    
*   [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     (bug fix)
    
*   [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     (bug fix)
    
*   [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     (bug fix)
    
*   [`linear_model.OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
     (bug fix)
    
*   [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
     (bug fix)
    
*   [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     (bug fix)
    
*   [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
     (bug fix)
    
*   [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     (bug fix)
    
*   [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     (bug fix)
    
*   [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     (bug fix)
    
*   [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     (bug fix)
    
*   `neural_network.BaseMultilayerPerceptron` (bug fix)
    
*   [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     (bug fix)
    
*   [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     (bug fix)
    
*   The v0.19.0 release notes failed to mention a backwards incompatibility with [`model_selection.StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")
     when `shuffle=True` due to [#7823](https://github.com/scikit-learn/scikit-learn/issues/7823)
    .
    

Details are listed in the changelog below.

(While we are trying to better inform users by providing this information, we cannot assure that this list is complete.)

### Known Major Bugs[#](https://scikit-learn.org/stable/whats_new/v0.20.html#known-major-bugs "Link to this heading")

*   [#11924](https://github.com/scikit-learn/scikit-learn/issues/11924)
    : [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     with `solver='lbfgs'` and `multi_class='multinomial'` may be non-deterministic or otherwise broken on macOS. This appears to be the case on Travis CI servers, but has not been confirmed on personal MacBooks! This issue has been present in previous releases.
    
*   [#9354](https://github.com/scikit-learn/scikit-learn/issues/9354)
    : [`metrics.pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")
     (which is used several times throughout the library) gives results with poor precision, which particularly affects its use with 32-bit float inputs. This became more problematic in versions 0.18 and 0.19 when some algorithms were changed to avoid casting 32-bit data into 64-bit.
    

### Changelog[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id23 "Link to this heading")

Support for Python 3.3 has been officially dropped.

#### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id24 "Link to this heading")

*   Major Feature [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
     now supports Single Linkage clustering via `linkage='single'`. [#9372](https://github.com/scikit-learn/scikit-learn/issues/9372)
     by [Leland McInnes](https://github.com/lmcinnes)
     and [Steve Astels](https://github.com/sastels)
    .
    
*   Feature [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     and [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     now support sample weights via new parameter `sample_weight` in `fit` function. [#10933](https://github.com/scikit-learn/scikit-learn/issues/10933)
     by [Johannes Hansen](https://github.com/jnhansen)
    .
    
*   Efficiency [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    , [`cluster.MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")
     and [`cluster.k_means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "sklearn.cluster.k_means")
     passed with `algorithm='full'` now enforce row-major ordering, improving runtime. [#10471](https://github.com/scikit-learn/scikit-learn/issues/10471)
     by [Gaurav Dhingra](https://github.com/gxyd)
    .
    
*   Efficiency [`cluster.DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")
     now is parallelized according to `n_jobs` regardless of `algorithm`. [#8003](https://github.com/scikit-learn/scikit-learn/issues/8003)
     by [Joël Billaud](https://github.com/recamshak)
    .
    
*   Enhancement [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
     now gives a warning if the number of distinct clusters found is smaller than `n_clusters`. This may occur when the number of distinct points in the data set is actually smaller than the number of cluster one is looking for. [#10059](https://github.com/scikit-learn/scikit-learn/issues/10059)
     by [Christian Braune](https://github.com/christianbraune79)
    .
    
*   Fix Fixed a bug where the `fit` method of [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
     stored cluster centers as 3d array instead of 2d array in case of non-convergence. For the same class, fixed undefined and arbitrary behavior in case of training data where all samples had equal similarity. [#9612](https://github.com/scikit-learn/scikit-learn/issues/9612)
    . By [Jonatan Samoocha](https://github.com/jsamoocha)
    .
    
*   Fix Fixed a bug in [`cluster.spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")
     where the normalization of the spectrum was using a division instead of a multiplication. [#8129](https://github.com/scikit-learn/scikit-learn/issues/8129)
     by [Jan Margeta](https://github.com/jmargeta)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Devansh D.](https://github.com/devanshdalal)
    .
    
*   Fix Fixed a bug in `cluster.k_means_elkan` where the returned `iteration` was 1 less than the correct value. Also added the missing `n_iter_` attribute in the docstring of [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    . [#11353](https://github.com/scikit-learn/scikit-learn/issues/11353)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   Fix Fixed a bug in [`cluster.mean_shift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html#sklearn.cluster.mean_shift "sklearn.cluster.mean_shift")
     where the assigned labels were not deterministic if there were multiple clusters with the same intensities. [#11901](https://github.com/scikit-learn/scikit-learn/issues/11901)
     by [Adrin Jalali](https://github.com/adrinjalali)
    .
    
*   API Change Deprecate `pooling_func` unused parameter in [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
    . [#9875](https://github.com/scikit-learn/scikit-learn/issues/9875)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    

#### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id25 "Link to this heading")

*   New module.
    
*   Major Feature Added [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    , which allows to apply different transformers to different columns of arrays or pandas DataFrames. [#9012](https://github.com/scikit-learn/scikit-learn/issues/9012)
     by [Andreas Müller](https://amueller.github.io/)
     and [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    , and [#11315](https://github.com/scikit-learn/scikit-learn/issues/11315)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Major Feature Added the [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
     which transforms the target y before fitting a regression model. The predictions are mapped back to the original space via an inverse transform. [#9041](https://github.com/scikit-learn/scikit-learn/issues/9041)
     by [Andreas Müller](https://amueller.github.io/)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id26 "Link to this heading")

*   Efficiency Runtime improvements to [`covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
    . [#9858](https://github.com/scikit-learn/scikit-learn/issues/9858)
     by [Steven Brown](https://github.com/stevendbrown)
    .
    
*   API Change The `covariance.graph_lasso`, `covariance.GraphLasso` and `covariance.GraphLassoCV` have been renamed to [`covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
    , [`covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
     and [`covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
     respectively and will be removed in version 0.22. [#9993](https://github.com/scikit-learn/scikit-learn/issues/9993)
     by [Artiem Krinitsyn](https://github.com/artiemq)
    

#### [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id27 "Link to this heading")

*   Major Feature Added [`datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
     to fetch datasets from [OpenML](https://openml.org/)
    . OpenML is a free, open data sharing platform and will be used instead of mldata as it provides better service availability. [#9908](https://github.com/scikit-learn/scikit-learn/issues/9908)
     by [Andreas Müller](https://amueller.github.io/)
     and [Jan N. van Rijn](https://github.com/janvanrijn)
    .
    
*   Feature In [`datasets.make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
    , one can now pass a list to the `n_samples` parameter to indicate the number of samples to generate per cluster. [#8617](https://github.com/scikit-learn/scikit-learn/issues/8617)
     by [Maskani Filali Mohamed](https://github.com/maskani-moh)
     and [Konstantinos Katrioplas](https://github.com/kkatrio)
    .
    
*   Feature Add `filename` attribute to [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")
     that have a CSV file. [#9101](https://github.com/scikit-learn/scikit-learn/issues/9101)
     by [alex-33](https://github.com/alex-33)
     and [Maskani Filali Mohamed](https://github.com/maskani-moh)
    .
    
*   Feature `return_X_y` parameter has been added to several dataset loaders. [#10774](https://github.com/scikit-learn/scikit-learn/issues/10774)
     by [Chris Catalfo](https://github.com/ccatalfo)
    .
    
*   Fix Fixed a bug in `datasets.load_boston` which had a wrong data point. [#10795](https://github.com/scikit-learn/scikit-learn/issues/10795)
     by [Takeshi Yoshizawa](https://github.com/tarcusx)
    .
    
*   Fix Fixed a bug in [`datasets.load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
     which had two wrong data points. [#11082](https://github.com/scikit-learn/scikit-learn/issues/11082)
     by [Sadhana Srinivasan](https://github.com/rotuna)
     and [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug in [`datasets.fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")
    , where data were not properly shuffled. [#9731](https://github.com/scikit-learn/scikit-learn/issues/9731)
     by [Nicolas Goix](https://ngoix.github.io/)
    .
    
*   Fix Fixed a bug in [`datasets.make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
    , where no odd number of data points could be generated. [#10045](https://github.com/scikit-learn/scikit-learn/issues/10045)
     by [Christian Braune](https://github.com/christianbraune79)
    .
    
*   API Change Deprecated `sklearn.datasets.fetch_mldata` to be removed in version 0.22. mldata.org is no longer operational. Until removal it will remain possible to load cached datasets. [#11466](https://github.com/scikit-learn/scikit-learn/issues/11466)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id28 "Link to this heading")

*   Feature [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
     functions and models now support positivity constraints. This applies to the dictionary and sparse code. [#6374](https://github.com/scikit-learn/scikit-learn/issues/6374)
     by [John Kirkham](https://github.com/jakirkham)
    .
    
*   Feature Fix [`decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
     now exposes `normalize_components`. When set to True, the train and test data are centered with the train mean respectively during the fit phase and the transform phase. This fixes the behavior of SparsePCA. When set to False, which is the default, the previous abnormal behaviour still holds. The False value is for backward compatibility and should not be used. [#11585](https://github.com/scikit-learn/scikit-learn/issues/11585)
     by [Ivan Panico](https://github.com/FollowKenny)
    .
    
*   Efficiency Efficiency improvements in [`decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
    . [#11420](https://github.com/scikit-learn/scikit-learn/issues/11420)
     and others by [John Kirkham](https://github.com/jakirkham)
    .
    
*   Fix Fix for uninformative error in [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    : now an error is raised if the number of components is larger than the chosen batch size. The `n_components=None` case was adapted accordingly. [#6452](https://github.com/scikit-learn/scikit-learn/issues/6452)
    . By [Wally Gauze](https://github.com/wallygauze)
    .
    
*   Fix Fixed a bug where the `partial_fit` method of [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
     used integer division instead of float division on Python 2. [#9492](https://github.com/scikit-learn/scikit-learn/issues/9492)
     by [James Bourbeau](https://github.com/jrbourbeau)
    .
    
*   Fix In [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     selecting a n\_components parameter greater than the number of samples now raises an error. Similarly, the `n_components=None` case now selects the minimum of `n_samples` and `n_features`. [#8484](https://github.com/scikit-learn/scikit-learn/issues/8484)
     by [Wally Gauze](https://github.com/wallygauze)
    .
    
*   Fix Fixed a bug in [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     where users will get unexpected error with large datasets when `n_components='mle'` on Python 3 versions. [#9886](https://github.com/scikit-learn/scikit-learn/issues/9886)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed an underflow in calculating KL-divergence for [`decomposition.NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")
     [#10142](https://github.com/scikit-learn/scikit-learn/issues/10142)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix Fixed a bug in [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     when running OMP sparse coding in parallel using read-only memory mapped datastructures. [#5956](https://github.com/scikit-learn/scikit-learn/issues/5956)
     by [Vighnesh Birodkar](https://github.com/vighneshbirodkar)
     and [Olivier Grisel](https://github.com/ogrisel)
    .
    

#### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-discriminant-analysis "Link to this heading")

*   Efficiency Memory usage improvement for `_class_means` and `_class_cov` in [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
    . [#10898](https://github.com/scikit-learn/scikit-learn/issues/10898)
     by [Nanxin Chen](https://github.com/bobchennan)
    .
    

#### [`sklearn.dummy`](https://scikit-learn.org/stable/api/sklearn.dummy.html#module-sklearn.dummy "sklearn.dummy")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-dummy "Link to this heading")

*   Feature [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     now has a `return_std` option in its `predict` method. The returned standard deviations will be zeros.
    
*   Feature [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     now only require X to be an object with finite length or shape. [#9832](https://github.com/scikit-learn/scikit-learn/issues/9832)
     by [Vrishank Bhardwaj](https://github.com/vrishank97)
    .
    
*   Feature [`dummy.DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier")
     and [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
     can now be scored without supplying test samples. [#11951](https://github.com/scikit-learn/scikit-learn/issues/11951)
     by [Rüdiger Busche](https://github.com/JarnoRFB)
    .
    

#### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id29 "Link to this heading")

*   Feature [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     and [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
     can now be fit with missing/non-finite values in X and/or multi-output Y to support wrapping pipelines that perform their own imputation. [#9707](https://github.com/scikit-learn/scikit-learn/issues/9707)
     by [Jimmy Wan](https://github.com/jimmywan)
    .
    
*   Feature [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     and [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     now support early stopping via `n_iter_no_change`, `validation_fraction` and `tol`. [#7071](https://github.com/scikit-learn/scikit-learn/issues/7071)
     by [Raghav RV](https://github.com/raghavrv)
    
*   Feature Added `named_estimators_` parameter in [`ensemble.VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")
     to access fitted estimators. [#9157](https://github.com/scikit-learn/scikit-learn/issues/9157)
     by [Herilalaina Rakotoarison](https://github.com/herilalaina)
    .
    
*   Fix Fixed a bug when fitting [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     or [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     with `warm_start=True` which previously raised a segmentation fault due to a non-conversion of CSC matrix into CSR format expected by `decision_function`. Similarly, Fortran-ordered arrays are converted to C-ordered arrays in the dense case. [#9991](https://github.com/scikit-learn/scikit-learn/issues/9991)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fixed a bug in [`ensemble.GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")
     and [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
     to have feature importances summed and then normalized, rather than normalizing on a per-tree basis. The previous behavior over-weighted the Gini importance of features that appear in later stages. This issue only affected feature importances. [#11176](https://github.com/scikit-learn/scikit-learn/issues/11176)
     by [Gil Forsyth](https://github.com/gforsyth)
    .
    
*   API Change The default value of the `n_estimators` parameter of [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
    , [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    , [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
    , [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    , and [`ensemble.RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")
     will change from 10 in version 0.20 to 100 in 0.22. A FutureWarning is raised when the default value is used. [#11542](https://github.com/scikit-learn/scikit-learn/issues/11542)
     by [Anna Ayzenshtat](https://github.com/annaayzenshtat)
    .
    
*   API Change Classes derived from `ensemble.BaseBagging`. The attribute `estimators_samples_` will return a list of arrays containing the indices selected for each bootstrap instead of a list of arrays containing the mask of the samples selected for each bootstrap. Indices allows to repeat samples while mask does not allow this functionality. [#9524](https://github.com/scikit-learn/scikit-learn/issues/9524)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix `ensemble.BaseBagging` where one could not deterministically reproduce `fit` result using the object attributes when `random_state` is set. [#9723](https://github.com/scikit-learn/scikit-learn/issues/9723)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id30 "Link to this heading")

*   Feature Enable the call to `get_feature_names` in unfitted [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
     initialized with a vocabulary. [#10908](https://github.com/scikit-learn/scikit-learn/issues/10908)
     by [Mohamed Maskani](https://github.com/maskani-moh)
    .
    
*   Enhancement `idf_` can now be set on a [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
    . [#10899](https://github.com/scikit-learn/scikit-learn/issues/10899)
     by [Sergey Melderis](https://github.com/serega)
    .
    
*   Fix Fixed a bug in [`feature_extraction.image.extract_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")
     which would throw an exception if `max_patches` was greater than or equal to the number of all possible patches rather than simply returning the number of possible patches. [#10101](https://github.com/scikit-learn/scikit-learn/issues/10101)
     by [Varun Agrawal](https://github.com/varunagrawal)
    
*   Fix Fixed a bug in [`feature_extraction.text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
    , [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
    , [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
     to support 64 bit sparse array indexing necessary to process large datasets with more than 2·10⁹ tokens (words or n-grams). [#9147](https://github.com/scikit-learn/scikit-learn/issues/9147)
     by [Claes-Fredrik Mannby](https://github.com/mannby)
     and [Roman Yurchak](https://github.com/rth)
    .
    
*   Fix Fixed bug in [`feature_extraction.text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
     which was ignoring the parameter `dtype`. In addition, [`feature_extraction.text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
     will preserve `dtype` for floating and raise a warning if `dtype` requested is integer. [#10441](https://github.com/scikit-learn/scikit-learn/issues/10441)
     by [Mayur Kulkarni](https://github.com/maykulkarni)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-feature-selection "Link to this heading")

*   Feature Added select K best features functionality to [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
    . [#6689](https://github.com/scikit-learn/scikit-learn/issues/6689)
     by [Nihar Sheth](https://github.com/nsheth12)
     and [Quazi Rahman](https://github.com/qmaruf)
    .
    
*   Feature Added `min_features_to_select` parameter to [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
     to bound evaluated features counts. [#11293](https://github.com/scikit-learn/scikit-learn/issues/11293)
     by [Brent Yi](https://github.com/brentyi)
    .
    
*   Feature [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    ’s fit method now supports [groups](https://scikit-learn.org/stable/glossary.html#term-groups)
    . [#9656](https://github.com/scikit-learn/scikit-learn/issues/9656)
     by [Adam Greenhall](https://github.com/adamgreenhall)
    .
    
*   Fix Fixed computation of `n_features_to_compute` for edge case with tied CV scores in [`feature_selection.RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")
    . [#9222](https://github.com/scikit-learn/scikit-learn/issues/9222)
     by [Nick Hoh](https://github.com/nickypie)
    .
    

#### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-gaussian-process "Link to this heading")

*   Efficiency In [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    , method `predict` is faster when using `return_std=True` in particular more when called several times in a row. [#9234](https://github.com/scikit-learn/scikit-learn/issues/9234)
     by [andrewww](https://github.com/andrewww)
     and [Minghui Liu](https://github.com/minghui-liu)
    .
    

#### [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id31 "Link to this heading")

*   New module, adopting `preprocessing.Imputer` as [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     with minor changes (see under preprocessing below).
    
*   Major Feature Added [`impute.MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator")
     which generates a binary indicator for missing values. [#8075](https://github.com/scikit-learn/scikit-learn/issues/8075)
     by [Maniteja Nandana](https://github.com/maniteja123)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature The [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
     has a new strategy, `'constant'`, to complete missing values with a fixed one, given by the `fill_value` parameter. This strategy supports numeric and non-numeric data, and so does the `'most_frequent'` strategy now. [#11211](https://github.com/scikit-learn/scikit-learn/issues/11211)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    

#### [`sklearn.isotonic`](https://scikit-learn.org/stable/api/sklearn.isotonic.html#module-sklearn.isotonic "sklearn.isotonic")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-isotonic "Link to this heading")

*   Fix Fixed a bug in [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     which incorrectly combined weights when fitting a model to data involving points with identical X values. [#9484](https://github.com/scikit-learn/scikit-learn/issues/9484)
     by [Dallas Card](https://github.com/dallascard)
    

#### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id32 "Link to this heading")

*   Feature [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     and [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
     now expose `early_stopping`, `validation_fraction` and `n_iter_no_change` parameters, to stop optimization monitoring the score on a validation set. A new learning rate `"adaptive"` strategy divides the learning rate by 5 each time `n_iter_no_change` consecutive epochs fail to improve the model. [#9043](https://github.com/scikit-learn/scikit-learn/issues/9043)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Feature Add `sample_weight` parameter to the fit method of [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     for weighted linear regression. [#10112](https://github.com/scikit-learn/scikit-learn/issues/10112)
     by [Peter St. John](https://github.com/pstjohn)
    .
    
*   Fix Fixed a bug in `logistic.logistic_regression_path` to ensure that the returned coefficients are correct when `multiclass='multinomial'`. Previously, some of the coefficients would override each other, leading to incorrect results in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
    . [#11724](https://github.com/scikit-learn/scikit-learn/issues/11724)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    
*   Fix Fixed a bug in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     where when using the parameter `multi_class='multinomial'`, the `predict_proba` method was returning incorrect probabilities in the case of binary outcomes. [#9939](https://github.com/scikit-learn/scikit-learn/issues/9939)
     by [Roger Westover](https://github.com/rwolst)
    .
    
*   Fix Fixed a bug in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     where the `score` method always computes accuracy, not the metric given by the `scoring` parameter. [#10998](https://github.com/scikit-learn/scikit-learn/issues/10998)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    
*   Fix Fixed a bug in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     where the ‘ovr’ strategy was always used to compute cross-validation scores in the multiclass setting, even if `'multinomial'` was set. [#8720](https://github.com/scikit-learn/scikit-learn/issues/8720)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    
*   Fix Fixed a bug in [`linear_model.OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
     that was broken when setting `normalize=False`. [#10071](https://github.com/scikit-learn/scikit-learn/issues/10071)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Fix Fixed a bug in [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     which caused incorrectly updated estimates for the standard deviation and the coefficients. [#10153](https://github.com/scikit-learn/scikit-learn/issues/10153)
     by [Jörg Döpfert](https://github.com/jdoepfert)
    .
    
*   Fix Fixed a bug in [`linear_model.ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")
     and [`linear_model.BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge")
     which caused NaN predictions when fitted with a constant target. [#10095](https://github.com/scikit-learn/scikit-learn/issues/10095)
     by [Jörg Döpfert](https://github.com/jdoepfert)
    .
    
*   Fix Fixed a bug in [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     where the parameter `store_cv_values` was not implemented though it was documented in `cv_values` as a way to set up the storage of cross-validation values for different alphas. [#10297](https://github.com/scikit-learn/scikit-learn/issues/10297)
     by [Mabel Villalba-Jiménez](https://github.com/mabelvj)
    .
    
*   Fix Fixed a bug in [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     which caused the input to be overridden when using parameter `copy_X=True` and `check_input=False`. [#10581](https://github.com/scikit-learn/scikit-learn/issues/10581)
     by [Yacine Mazari](https://github.com/ymazari)
    .
    
*   Fix Fixed a bug in [`sklearn.linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     where the coefficient had wrong shape when `fit_intercept=False`. [#10687](https://github.com/scikit-learn/scikit-learn/issues/10687)
     by [Martin Hahn](https://github.com/martin-hahn)
    .
    
*   Fix Fixed a bug in [`sklearn.linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     where the `multi_class='multinomial'` with binary output `with warm_start=True` [#10836](https://github.com/scikit-learn/scikit-learn/issues/10836)
     by [Aishwarya Srinivasan](https://github.com/aishgrt1)
    .
    
*   Fix Fixed a bug in [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
     where using integer `alphas` raised an error. [#10397](https://github.com/scikit-learn/scikit-learn/issues/10397)
     by [Mabel Villalba-Jiménez](https://github.com/mabelvj)
    .
    
*   Fix Fixed condition triggering gap computation in [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     and [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     when working with sparse matrices. [#10992](https://github.com/scikit-learn/scikit-learn/issues/10992)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   Fix Fixed a bug in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
    , [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     and [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
    , where the stopping criterion was stopping the algorithm before convergence. A parameter `n_iter_no_change` was added and set by default to 5. Previous behavior is equivalent to setting the parameter to 1. [#9043](https://github.com/scikit-learn/scikit-learn/issues/9043)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Fix Fixed a bug where liblinear and libsvm-based estimators would segfault if passed a scipy.sparse matrix with 64-bit indices. They now raise a ValueError. [#11327](https://github.com/scikit-learn/scikit-learn/issues/11327)
     by [Karan Dhingra](https://github.com/kdhingra307)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   API Change The default values of the `solver` and `multi_class` parameters of [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     will change respectively from `'liblinear'` and `'ovr'` in version 0.20 to `'lbfgs'` and `'auto'` in version 0.22. A FutureWarning is raised when the default values are used. [#11905](https://github.com/scikit-learn/scikit-learn/issues/11905)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   API Change Deprecate `positive=True` option in [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
     as the underlying implementation is broken. Use [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     instead. [#9837](https://github.com/scikit-learn/scikit-learn/issues/9837)
     by [Alexandre Gramfort](https://alexandre.gramfort.net/)
    .
    
*   API Change `n_iter_` may vary from previous releases in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     with `solver='lbfgs'` and [`linear_model.HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")
    . For Scipy <= 1.0.0, the optimizer could perform more than the requested maximum number of iterations. Now both estimators will report at most `max_iter` iterations even if more were performed. [#10723](https://github.com/scikit-learn/scikit-learn/issues/10723)
     by [Joel Nothman](https://joelnothman.com/)
    .
    

#### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-manifold "Link to this heading")

*   Efficiency Speed improvements for both ‘exact’ and ‘barnes\_hut’ methods in [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")
    . [#10593](https://github.com/scikit-learn/scikit-learn/issues/10593)
     and [#10610](https://github.com/scikit-learn/scikit-learn/issues/10610)
     by [Tom Dupre la Tour](https://github.com/TomDLT)
    .
    
*   Feature Support sparse input in [`manifold.Isomap.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap.fit "sklearn.manifold.Isomap.fit")
    . [#8554](https://github.com/scikit-learn/scikit-learn/issues/8554)
     by [Leland McInnes](https://github.com/lmcinnes)
    .
    
*   Feature `manifold.t_sne.trustworthiness` accepts metrics other than Euclidean. [#9775](https://github.com/scikit-learn/scikit-learn/issues/9775)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    
*   Fix Fixed a bug in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")
     where the normalization of the spectrum was using a division instead of a multiplication. [#8129](https://github.com/scikit-learn/scikit-learn/issues/8129)
     by [Jan Margeta](https://github.com/jmargeta)
    , [Guillaume Lemaitre](https://github.com/glemaitre)
    , and [Devansh D.](https://github.com/devanshdalal)
    .
    
*   API Change Feature Deprecate `precomputed` parameter in function `manifold.t_sne.trustworthiness`. Instead, the new parameter `metric` should be used with any compatible metric including ‘precomputed’, in which case the input matrix `X` should be a matrix of pairwise distances or squared distances. [#9775](https://github.com/scikit-learn/scikit-learn/issues/9775)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    
*   API Change Deprecate `precomputed` parameter in function `manifold.t_sne.trustworthiness`. Instead, the new parameter `metric` should be used with any compatible metric including ‘precomputed’, in which case the input matrix `X` should be a matrix of pairwise distances or squared distances. [#9775](https://github.com/scikit-learn/scikit-learn/issues/9775)
     by [William de Vazelhes](https://github.com/wdevazelhes)
    .
    

#### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id33 "Link to this heading")

*   Major Feature Added the [`metrics.davies_bouldin_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html#sklearn.metrics.davies_bouldin_score "sklearn.metrics.davies_bouldin_score")
     metric for evaluation of clustering models without a ground truth. [#10827](https://github.com/scikit-learn/scikit-learn/issues/10827)
     by [Luis Osa](https://github.com/logc)
    .
    
*   Major Feature Added the [`metrics.balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score")
     metric and a corresponding `'balanced_accuracy'` scorer for binary and multiclass classification. [#8066](https://github.com/scikit-learn/scikit-learn/issues/8066)
     by [@xyguo](https://github.com/xyguo)
     and [Aman Dalmia](https://github.com/dalmia)
    , and [#10587](https://github.com/scikit-learn/scikit-learn/issues/10587)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Feature Partial AUC is available via `max_fpr` parameter in [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
    . [#3840](https://github.com/scikit-learn/scikit-learn/issues/3840)
     by [Alexander Niederbühl](https://github.com/Alexander-N)
    .
    
*   Feature A scorer based on [`metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
     is also available. [#9521](https://github.com/scikit-learn/scikit-learn/issues/9521)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Feature Added control over the normalization in [`metrics.normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")
     and [`metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
     via the `average_method` parameter. In version 0.22, the default normalizer for each will become the _arithmetic_ mean of the entropies of each clustering. [#11124](https://github.com/scikit-learn/scikit-learn/issues/11124)
     by [Arya McCarthy](https://github.com/aryamccarthy)
    .
    
*   Feature Added `output_dict` parameter in [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     to return classification statistics as dictionary. [#11160](https://github.com/scikit-learn/scikit-learn/issues/11160)
     by [Dan Barkhorn](https://github.com/danielbarkhorn)
    .
    
*   Feature [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
     now reports all applicable averages on the given data, including micro, macro and weighted average as well as samples average for multilabel data. [#11679](https://github.com/scikit-learn/scikit-learn/issues/11679)
     by [Alexander Pacha](https://github.com/apacha)
    .
    
*   Feature [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     now supports binary `y_true` other than `{0, 1}` or `{-1, 1}` through `pos_label` parameter. [#9980](https://github.com/scikit-learn/scikit-learn/issues/9980)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Feature [`metrics.label_ranking_average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "sklearn.metrics.label_ranking_average_precision_score")
     now supports `sample_weight`. [#10845](https://github.com/scikit-learn/scikit-learn/issues/10845)
     by [Jose Perez-Parras Toledano](https://github.com/jopepato)
    .
    
*   Feature Add `dense_output` parameter to [`metrics.pairwise.linear_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html#sklearn.metrics.pairwise.linear_kernel "sklearn.metrics.pairwise.linear_kernel")
    . When False and both inputs are sparse, will return a sparse matrix. [#10999](https://github.com/scikit-learn/scikit-learn/issues/10999)
     by [Taylor G Smith](https://github.com/tgsmith61591)
    .
    
*   Efficiency [`metrics.silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")
     and [`metrics.silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")
     are more memory efficient and run faster. This avoids some reported freezes and MemoryErrors. [#11135](https://github.com/scikit-learn/scikit-learn/issues/11135)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix Fixed a bug in [`metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")
     when truncated `range(n_labels)` is passed as value for `labels`. [#10377](https://github.com/scikit-learn/scikit-learn/issues/10377)
     by [Gaurav Dhingra](https://github.com/gxyd)
    .
    
*   Fix Fixed a bug due to floating point error in [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     with non-integer sample weights. [#9786](https://github.com/scikit-learn/scikit-learn/issues/9786)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug where [`metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     sometimes starts on y-axis instead of (0, 0), which is inconsistent with the document and other implementations. Note that this will not influence the result from [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
     [#10093](https://github.com/scikit-learn/scikit-learn/issues/10093)
     by [alexryndin](https://github.com/alexryndin)
     and [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug to avoid integer overflow. Casted product to 64 bits integer in [`metrics.mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")
    . [#9772](https://github.com/scikit-learn/scikit-learn/issues/9772)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    
*   Fix Fixed a bug where [`metrics.average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")
     will sometimes return `nan` when `sample_weight` contains 0. [#9980](https://github.com/scikit-learn/scikit-learn/issues/9980)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   Fix Fixed a bug in [`metrics.fowlkes_mallows_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#sklearn.metrics.fowlkes_mallows_score "sklearn.metrics.fowlkes_mallows_score")
     to avoid integer overflow. Casted return value of `contingency_matrix` to `int64` and computed product of square roots rather than square root of product. [#9515](https://github.com/scikit-learn/scikit-learn/issues/9515)
     by [Alan Liddell](https://github.com/aliddell)
     and [Manh Dao](https://github.com/manhdao)
    .
    
*   API Change Deprecate `reorder` parameter in [`metrics.auc`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")
     as it’s no longer required for [`metrics.roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")
    . Moreover using `reorder=True` can hide bugs due to floating point error in the input. [#9851](https://github.com/scikit-learn/scikit-learn/issues/9851)
     by [Hanmin Qin](https://github.com/qinhanmin2014)
    .
    
*   API Change In [`metrics.normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")
     and [`metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
    , warn that `average_method` will have a new default value. In version 0.22, the default normalizer for each will become the _arithmetic_ mean of the entropies of each clustering. Currently, [`metrics.normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")
     uses the default of `average_method='geometric'`, and [`metrics.adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")
     uses the default of `average_method='max'` to match their behaviors in version 0.19. [#11124](https://github.com/scikit-learn/scikit-learn/issues/11124)
     by [Arya McCarthy](https://github.com/aryamccarthy)
    .
    
*   API Change The `batch_size` parameter to [`metrics.pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")
     and [`metrics.pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")
     is deprecated to be removed in v0.22. It no longer has any effect, as batch size is determined by global `working_memory` config. See [Limiting Working Memory](https://scikit-learn.org/stable/computing/computational_performance.html#working-memory)
    . [#10280](https://github.com/scikit-learn/scikit-learn/issues/10280)
     by [Joel Nothman](https://joelnothman.com/)
     and [Aman Dalmia](https://github.com/dalmia)
    .
    

#### [`sklearn.mixture`](https://scikit-learn.org/stable/api/sklearn.mixture.html#module-sklearn.mixture "sklearn.mixture")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id34 "Link to this heading")

*   Feature Added function [fit\_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict)
     to [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
    , which is essentially equivalent to calling [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
     and [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
    . [#10336](https://github.com/scikit-learn/scikit-learn/issues/10336)
     by [Shu Haoran](https://github.com/haoranShu)
     and [Andrew Peng](https://github.com/Andrew-peng)
    .
    
*   Fix Fixed a bug in `mixture.BaseMixture` where the reported `n_iter_` was missing an iteration. It affected [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
    . [#10740](https://github.com/scikit-learn/scikit-learn/issues/10740)
     by [Erich Schubert](https://github.com/kno10)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Fix Fixed a bug in `mixture.BaseMixture` and its subclasses [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     and [`mixture.BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
     where the `lower_bound_` was not the max lower bound across all initializations (when `n_init > 1`), but just the lower bound of the last initialization. [#10869](https://github.com/scikit-learn/scikit-learn/issues/10869)
     by [Aurélien Géron](https://github.com/ageron)
    .
    

#### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id35 "Link to this heading")

*   Feature Add `return_estimator` parameter in [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
     to return estimators fitted on each split. [#9686](https://github.com/scikit-learn/scikit-learn/issues/9686)
     by [Aurélien Bellet](https://github.com/bellet)
    .
    
*   Feature New `refit_time_` attribute will be stored in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     if `refit` is set to `True`. This will allow measuring the complete time it takes to perform hyperparameter optimization and refitting the best model on the whole dataset. [#11310](https://github.com/scikit-learn/scikit-learn/issues/11310)
     by [Matthias Feurer](https://github.com/mfeurer)
    .
    
*   Feature Expose `error_score` parameter in [`model_selection.cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")
    , [`model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
    , [`model_selection.learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")
     and [`model_selection.validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")
     to control the behavior triggered when an error occurs in `model_selection._fit_and_score`. [#11576](https://github.com/scikit-learn/scikit-learn/issues/11576)
     by [Samuel O. Ronsin](https://github.com/samronsin)
    .
    
*   Feature `BaseSearchCV` now has an experimental, private interface to support customized parameter search strategies, through its `_run_search` method. See the implementations in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     and please provide feedback if you use this. Note that we do not assure the stability of this API beyond version 0.20. [#9599](https://github.com/scikit-learn/scikit-learn/issues/9599)
     by [Joel Nothman](https://joelnothman.com/)
    
*   Enhancement Add improved error message in [`model_selection.cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")
     when multiple metrics are passed in `scoring` keyword. [#11006](https://github.com/scikit-learn/scikit-learn/issues/11006)
     by [Ming Li](https://github.com/minggli)
    .
    
*   API Change The default number of cross-validation folds `cv` and the default number of splits `n_splits` in the [`model_selection.KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")
    \-like splitters will change from 3 to 5 in 0.22 as 3-fold has a lot of variance. [#11557](https://github.com/scikit-learn/scikit-learn/issues/11557)
     by [Alexandre Boucaud](https://github.com/aboucaud)
    .
    
*   API Change The default of `iid` parameter of [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     will change from `True` to `False` in version 0.22 to correspond to the standard definition of cross-validation, and the parameter will be removed in version 0.24 altogether. This parameter is of greatest practical significance where the sizes of different test sets in cross-validation were very unequal, i.e. in group-based CV strategies. [#9085](https://github.com/scikit-learn/scikit-learn/issues/9085)
     by [Laurent Direr](https://github.com/ldirer)
     and [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change The default value of the `error_score` parameter in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
     and [`model_selection.RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")
     will change to `np.NaN` in version 0.22. [#10677](https://github.com/scikit-learn/scikit-learn/issues/10677)
     by [Kirill Zhdanovich](https://github.com/Zhdanovich)
    .
    
*   API Change Changed ValueError exception raised in [`model_selection.ParameterSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#sklearn.model_selection.ParameterSampler "sklearn.model_selection.ParameterSampler")
     to a UserWarning for case where the class is instantiated with a greater value of `n_iter` than the total space of parameters in the parameter grid. `n_iter` now acts as an upper bound on iterations. [#10982](https://github.com/scikit-learn/scikit-learn/issues/10982)
     by [Juliet Lawton](https://github.com/julietcl)
    
*   API Change Invalid input for [`model_selection.ParameterGrid`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#sklearn.model_selection.ParameterGrid "sklearn.model_selection.ParameterGrid")
     now raises TypeError. [#10928](https://github.com/scikit-learn/scikit-learn/issues/10928)
     by [Solutus Immensus](https://github.com/solutusimmensus)
    

#### [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-multioutput "Link to this heading")

*   Major Feature Added [`multioutput.RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
     for multi-target regression. [#9257](https://github.com/scikit-learn/scikit-learn/issues/9257)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    

#### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-naive-bayes "Link to this heading")

*   Major Feature Added [`naive_bayes.ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")
    , which implements the Complement Naive Bayes classifier described in Rennie et al. (2003). [#8190](https://github.com/scikit-learn/scikit-learn/issues/8190)
     by [Michael A. Alcorn](https://github.com/airalcorn2)
    .
    
*   Feature Add `var_smoothing` parameter in [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     to give a precise control over variances calculation. [#9681](https://github.com/scikit-learn/scikit-learn/issues/9681)
     by [Dmitry Mottl](https://github.com/Mottl)
    .
    
*   Fix Fixed a bug in [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     which incorrectly raised error for prior list which summed to 1. [#10005](https://github.com/scikit-learn/scikit-learn/issues/10005)
     by [Gaurav Dhingra](https://github.com/gxyd)
    .
    
*   Fix Fixed a bug in [`naive_bayes.MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB")
     which did not accept vector valued pseudocounts (alpha). [#10346](https://github.com/scikit-learn/scikit-learn/issues/10346)
     by [Tobias Madsen](https://github.com/TobiasMadsen)
    

#### [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id36 "Link to this heading")

*   Efficiency [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
     and [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
     are now parallelized according to `n_jobs` regardless of `algorithm`. [#10887](https://github.com/scikit-learn/scikit-learn/issues/10887)
     by [Joël Billaud](https://github.com/recamshak)
    .
    
*   Efficiency [`sklearn.neighbors`](https://scikit-learn.org/stable/api/sklearn.neighbors.html#module-sklearn.neighbors "sklearn.neighbors")
     query methods are now more memory efficient when `algorithm='brute'`. [#11136](https://github.com/scikit-learn/scikit-learn/issues/11136)
     by [Joel Nothman](https://joelnothman.com/)
     and [Aman Dalmia](https://github.com/dalmia)
    .
    
*   Feature Add `sample_weight` parameter to the fit method of [`neighbors.KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")
     to enable weighting in kernel density estimation. [#4394](https://github.com/scikit-learn/scikit-learn/issues/4394)
     by [Samuel O. Ronsin](https://github.com/samronsin)
    .
    
*   Feature Novelty detection with [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
    : Add a `novelty` parameter to [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
    . When `novelty` is set to True, [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     can then be used for novelty detection, i.e. predict on new unseen data. Available prediction methods are `predict`, `decision_function` and `score_samples`. By default, `novelty` is set to `False`, and only the `fit_predict` method is available. By [Albert Thomas](https://github.com/albertcthomas)
    .
    
*   Fix Fixed a bug in [`neighbors.NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")
     where fitting a NearestNeighbors model fails when a) the distance metric used is a callable and b) the input to the NearestNeighbors model is sparse. [#9579](https://github.com/scikit-learn/scikit-learn/issues/9579)
     by [Thomas Kober](https://github.com/tttthomasssss)
    .
    
*   Fix Fixed a bug so `predict` in [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
     can handle empty neighbor set when using non uniform weights. Also raises a new warning when no neighbors are found for samples. [#9655](https://github.com/scikit-learn/scikit-learn/issues/9655)
     by [Andreas Bjerre-Nielsen](https://github.com/abjer)
    .
    
*   Fix Efficiency Fixed a bug in `KDTree` construction that results in faster construction and querying times. [#11556](https://github.com/scikit-learn/scikit-learn/issues/11556)
     by [Jake VanderPlas](https://github.com/jakevdp)
    
*   Fix Fixed a bug in [`neighbors.KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")
     and [`neighbors.BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")
     where pickled tree objects would change their type to the super class `BinaryTree`. [#11774](https://github.com/scikit-learn/scikit-learn/issues/11774)
     by [Nicolas Hug](https://github.com/NicolasHug)
    .
    

#### [`sklearn.neural_network`](https://scikit-learn.org/stable/api/sklearn.neural_network.html#module-sklearn.neural_network "sklearn.neural_network")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-neural-network "Link to this heading")

*   Feature Add `n_iter_no_change` parameter in `neural_network.BaseMultilayerPerceptron`, [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
    , and [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     to give control over maximum number of epochs to not meet `tol` improvement. [#9456](https://github.com/scikit-learn/scikit-learn/issues/9456)
     by [Nicholas Nadeau](https://github.com/nnadeau)
    .
    
*   Fix Fixed a bug in `neural_network.BaseMultilayerPerceptron`, [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
    , and [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
     with new `n_iter_no_change` parameter now at 10 from previously hardcoded 2. [#9456](https://github.com/scikit-learn/scikit-learn/issues/9456)
     by [Nicholas Nadeau](https://github.com/nnadeau)
    .
    
*   Fix Fixed a bug in [`neural_network.MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")
     where fitting quit unexpectedly early due to local minima or fluctuations. [#9456](https://github.com/scikit-learn/scikit-learn/issues/9456)
     by [Nicholas Nadeau](https://github.com/nnadeau)
    

#### [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-pipeline "Link to this heading")

*   Feature The `predict` method of [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
     now passes keyword arguments on to the pipeline’s last estimator, enabling the use of parameters such as `return_std` in a pipeline with caution. [#9304](https://github.com/scikit-learn/scikit-learn/issues/9304)
     by [Breno Freitas](https://github.com/brenolf)
    .
    
*   API Change [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
     now supports `'drop'` as a transformer to drop features. [#11144](https://github.com/scikit-learn/scikit-learn/issues/11144)
     by [Thomas Fan](https://github.com/thomasjpfan)
    .
    

#### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id37 "Link to this heading")

*   Major Feature Expanded [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     to allow to encode categorical string features as a numeric array using a one-hot (or dummy) encoding scheme, and added [`preprocessing.OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
     to convert to ordinal integers. Those two classes now handle encoding of all feature types (also handles string-valued features) and derives the categories based on the unique values in the features instead of the maximum value in the features. [#9151](https://github.com/scikit-learn/scikit-learn/issues/9151)
     and [#10521](https://github.com/scikit-learn/scikit-learn/issues/10521)
     by [Vighnesh Birodkar](https://github.com/vighneshbirodkar)
     and [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   Major Feature Added [`preprocessing.KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")
     for turning continuous features into categorical or one-hot encoded features. [#7668](https://github.com/scikit-learn/scikit-learn/issues/7668)
    , [#9647](https://github.com/scikit-learn/scikit-learn/issues/9647)
    , [#10195](https://github.com/scikit-learn/scikit-learn/issues/10195)
    , [#10192](https://github.com/scikit-learn/scikit-learn/issues/10192)
    , [#11272](https://github.com/scikit-learn/scikit-learn/issues/11272)
    , [#11467](https://github.com/scikit-learn/scikit-learn/issues/11467)
     and [#11505](https://github.com/scikit-learn/scikit-learn/issues/11505)
    . by [Henry Lin](https://github.com/hlin117)
    , [Hanmin Qin](https://github.com/qinhanmin2014)
    , [Tom Dupre la Tour](https://github.com/TomDLT)
     and [Giovanni Giuseppe Costa](https://github.com/ggc87)
    .
    
*   Major Feature Added [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
    , which implements the Yeo-Johnson and Box-Cox power transformations. Power transformations try to find a set of feature-wise parametric transformations to approximately map data to a Gaussian distribution centered at zero and with unit variance. This is useful as a variance-stabilizing transformation in situations where normality and homoscedasticity are desirable. [#10210](https://github.com/scikit-learn/scikit-learn/issues/10210)
     by [Eric Chang](https://github.com/chang)
     and [Maniteja Nandana](https://github.com/maniteja123)
    , and [#11520](https://github.com/scikit-learn/scikit-learn/issues/11520)
     by [Nicolas Hug](https://github.com/nicolashug)
    .
    
*   Major Feature NaN values are ignored and handled in the following preprocessing methods: [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")
    , [`preprocessing.MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
    , [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
    , [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
    , [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
    , [`preprocessing.QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
     classes and [`preprocessing.maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale")
    , [`preprocessing.minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")
    , [`preprocessing.robust_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "sklearn.preprocessing.robust_scale")
    , [`preprocessing.scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")
    , [`preprocessing.power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform")
    , [`preprocessing.quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")
     functions respectively addressed in issues [#11011](https://github.com/scikit-learn/scikit-learn/issues/11011)
    , [#11005](https://github.com/scikit-learn/scikit-learn/issues/11005)
    , [#11308](https://github.com/scikit-learn/scikit-learn/issues/11308)
    , [#11206](https://github.com/scikit-learn/scikit-learn/issues/11206)
    , [#11306](https://github.com/scikit-learn/scikit-learn/issues/11306)
    , and [#10437](https://github.com/scikit-learn/scikit-learn/issues/10437)
    . By [Lucija Gregov](https://github.com/LucijaGregov)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     now supports sparse input. [#10452](https://github.com/scikit-learn/scikit-learn/issues/10452)
     by [Aman Dalmia](https://github.com/dalmia)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Feature [`preprocessing.RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")
     and [`preprocessing.robust_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "sklearn.preprocessing.robust_scale")
     can be fitted using sparse matrices. [#11308](https://github.com/scikit-learn/scikit-learn/issues/11308)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     now supports the `get_feature_names` method to obtain the transformed feature names. [#10181](https://github.com/scikit-learn/scikit-learn/issues/10181)
     by [Nirvan Anjirbag](https://github.com/Nirvan101)
     and [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   Feature A parameter `check_inverse` was added to [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
     to ensure that `func` and `inverse_func` are the inverse of each other. [#9399](https://github.com/scikit-learn/scikit-learn/issues/9399)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Feature The `transform` method of [`sklearn.preprocessing.MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
     now ignores any unknown classes. A warning is raised stating the unknown classes classes found which are ignored. [#10913](https://github.com/scikit-learn/scikit-learn/issues/10913)
     by [Rodrigo Agundez](https://github.com/rragundez)
    .
    
*   Fix Fixed bugs in [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
     which would sometimes throw errors when `transform` or `inverse_transform` was called with empty arrays. [#10458](https://github.com/scikit-learn/scikit-learn/issues/10458)
     by [Mayur Kulkarni](https://github.com/maykulkarni)
    .
    
*   Fix Fix ValueError in [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
     when using `inverse_transform` on unseen labels. [#9816](https://github.com/scikit-learn/scikit-learn/issues/9816)
     by [Charlie Newey](https://github.com/newey01c)
    .
    
*   Fix Fix bug in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
     which discarded the `dtype` when returning a sparse matrix output. [#11042](https://github.com/scikit-learn/scikit-learn/issues/11042)
     by [Daniel Morales](https://github.com/DanielMorales9)
    .
    
*   Fix Fix `fit` and `partial_fit` in [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     in the rare case when `with_mean=False` and `with_std=False` which was crashing by calling `fit` more than once and giving inconsistent results for `mean_` whether the input was a sparse or a dense matrix. `mean_` will be set to `None` with both sparse and dense inputs. `n_samples_seen_` will be also reported for both input types. [#11235](https://github.com/scikit-learn/scikit-learn/issues/11235)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   API Change Deprecate `n_values` and `categorical_features` parameters and `active_features_`, `feature_indices_` and `n_values_` attributes of [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
    . The `n_values` parameter can be replaced with the new `categories` parameter, and the attributes with the new `categories_` attribute. Selecting the categorical features with the `categorical_features` parameter is now better supported using the [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
    . [#10521](https://github.com/scikit-learn/scikit-learn/issues/10521)
     by [Joris Van den Bossche](https://github.com/jorisvandenbossche)
    .
    
*   API Change Deprecate `preprocessing.Imputer` and move the corresponding module to [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    . [#9726](https://github.com/scikit-learn/scikit-learn/issues/9726)
     by [Kumar Ashutosh](https://github.com/thechargedneutron)
    .
    
*   API Change The `axis` parameter that was in `preprocessing.Imputer` is no longer present in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")
    . The behavior is equivalent to `axis=0` (impute along columns). Row-wise imputation can be performed with FunctionTransformer (e.g., `FunctionTransformer(lambda X: SimpleImputer().fit_transform(X.T).T)`). [#10829](https://github.com/scikit-learn/scikit-learn/issues/10829)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
     and [Gilberto Olimpio](https://github.com/gilbertoolimpio)
    .
    
*   API Change The NaN marker for the missing values has been changed between the `preprocessing.Imputer` and the `impute.SimpleImputer`. `missing_values='NaN'` should now be `missing_values=np.nan`. [#11211](https://github.com/scikit-learn/scikit-learn/issues/11211)
     by [Jeremie du Boisberranger](https://github.com/jeremiedbb)
    .
    
*   API Change In [`preprocessing.FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
    , the default of `validate` will be from `True` to `False` in 0.22. [#10655](https://github.com/scikit-learn/scikit-learn/issues/10655)
     by [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    

#### [`sklearn.svm`](https://scikit-learn.org/stable/api/sklearn.svm.html#module-sklearn.svm "sklearn.svm")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id38 "Link to this heading")

*   Fix Fixed a bug in [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
     where when the argument `kernel` is unicode in Python2, the `predict_proba` method was raising an unexpected TypeError given dense inputs. [#10412](https://github.com/scikit-learn/scikit-learn/issues/10412)
     by [Jiongyan Zhang](https://github.com/qmick)
    .
    
*   API Change Deprecate `random_state` parameter in [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     as the underlying implementation is not random. [#9497](https://github.com/scikit-learn/scikit-learn/issues/9497)
     by [Albert Thomas](https://github.com/albertcthomas)
    .
    
*   API Change The default value of `gamma` parameter of [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
    , [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
    , [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")
    , [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")
    , [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
     will change from `'auto'` to `'scale'` in version 0.22 to account better for unscaled features. [#8361](https://github.com/scikit-learn/scikit-learn/issues/8361)
     by [Gaurav Dhingra](https://github.com/gxyd)
     and [Ting Neo](https://github.com/neokt)
    .
    

#### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#sklearn-tree "Link to this heading")

*   Enhancement Although private (and hence not assured API stability), `tree._criterion.ClassificationCriterion` and `tree._criterion.RegressionCriterion` may now be cimported and extended. [#10325](https://github.com/scikit-learn/scikit-learn/issues/10325)
     by [Camil Staps](https://github.com/camilstaps)
    .
    
*   Fix Fixed a bug in `tree.BaseDecisionTree` with `splitter="best"` where split threshold could become infinite when values in X were near infinite. [#10536](https://github.com/scikit-learn/scikit-learn/issues/10536)
     by [Jonathan Ohayon](https://github.com/Johayon)
    .
    
*   Fix Fixed a bug in `tree.MAE` to ensure sample weights are being used during the calculation of tree MAE impurity. Previous behaviour could cause suboptimal splits to be chosen since the impurity calculation considered all samples to be of equal weight importance. [#11464](https://github.com/scikit-learn/scikit-learn/issues/11464)
     by [John Stott](https://github.com/JohnStott)
    .
    

#### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id39 "Link to this heading")

*   Feature [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     and [`utils.check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
     now have `accept_large_sparse` to control whether scipy.sparse matrices with 64-bit indices should be rejected. [#11327](https://github.com/scikit-learn/scikit-learn/issues/11327)
     by [Karan Dhingra](https://github.com/kdhingra307)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Efficiency Fix Avoid copying the data in [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     when the input data is a memmap (and `copy=False`). [#10663](https://github.com/scikit-learn/scikit-learn/issues/10663)
     by [Arthur Mensch](https://github.com/arthurmensch)
     and [Loïc Estève](https://github.com/lesteve)
    .
    
*   API Change [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     yield a `FutureWarning` indicating that arrays of bytes/strings will be interpreted as decimal numbers beginning in version 0.22. [#10229](https://github.com/scikit-learn/scikit-learn/issues/10229)
     by [Ryan Lee](https://github.com/rtlee9)
    

#### Multiple modules[#](https://scikit-learn.org/stable/whats_new/v0.20.html#multiple-modules "Link to this heading")

*   Feature API Change More consistent outlier detection API: Add a `score_samples` method in [`svm.OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM")
    , [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
    , [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
    , [`covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
    . It allows to access raw score functions from original papers. A new `offset_` parameter allows to link `score_samples` and `decision_function` methods. The `contamination` parameter of [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     and [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")
     `decision_function` methods is used to define this `offset_` such that outliers (resp. inliers) have negative (resp. positive) `decision_function` values. By default, `contamination` is kept unchanged to 0.1 for a deprecation period. In 0.22, it will be set to “auto”, thus using method-specific score offsets. In [`covariance.EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")
     `decision_function` method, the `raw_values` parameter is deprecated as the shifted Mahalanobis distance will be always returned in 0.22. [#9015](https://github.com/scikit-learn/scikit-learn/issues/9015)
     by [Nicolas Goix](https://ngoix.github.io/)
    .
    
*   Feature API Change A `behaviour` parameter has been introduced in [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     to ensure backward compatibility. In the old behaviour, the `decision_function` is independent of the `contamination` parameter. A threshold attribute depending on the `contamination` parameter is thus used. In the new behaviour the `decision_function` is dependent on the `contamination` parameter, in such a way that 0 becomes its natural threshold to detect outliers. Setting behaviour to “old” is deprecated and will not be possible in version 0.22. Beside, the behaviour parameter will be removed in 0.24. [#11553](https://github.com/scikit-learn/scikit-learn/issues/11553)
     by [Nicolas Goix](https://ngoix.github.io/)
    .
    
*   API Change Added convergence warning to [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
     and [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     when `verbose` is set to 0. [#10881](https://github.com/scikit-learn/scikit-learn/issues/10881)
     by [Alexandre Sevin](https://github.com/AlexandreSev)
    .
    
*   API Change Changed warning type from [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "(in Python v3.14)")
     to [`exceptions.ConvergenceWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
     for failing convergence in `linear_model.logistic_regression_path`, [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    , [`linear_model.ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")
    , [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    , [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
    , [`decomposition.fastica`](https://scikit-learn.org/stable/modules/generated/fastica-function.html#sklearn.decomposition.fastica "sklearn.decomposition.fastica")
    , [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    , [`cluster.AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")
    , and [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")
    . [#10306](https://github.com/scikit-learn/scikit-learn/issues/10306)
     by [Jonathan Siebert](https://github.com/jotasi)
    .
    

#### Miscellaneous[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id40 "Link to this heading")

*   Major Feature A new configuration parameter, `working_memory` was added to control memory consumption limits in chunked operations, such as the new [`metrics.pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked")
    . See [Limiting Working Memory](https://scikit-learn.org/stable/computing/computational_performance.html#working-memory)
    . [#10280](https://github.com/scikit-learn/scikit-learn/issues/10280)
     by [Joel Nothman](https://joelnothman.com/)
     and [Aman Dalmia](https://github.com/dalmia)
    .
    
*   Feature The version of [`joblib`](https://joblib.readthedocs.io/en/latest/index.html#module-joblib "(in joblib v1.7)")
     bundled with Scikit-learn is now 0.12. This uses a new default multiprocessing implementation, named [loky](https://github.com/tomMoral/loky)
    . While this may incur some memory and communication overhead, it should provide greater cross-platform stability than relying on Python standard library multiprocessing. [#11741](https://github.com/scikit-learn/scikit-learn/issues/11741)
     by the Joblib developers, especially [Thomas Moreau](https://github.com/tomMoral)
     and [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Feature An environment variable to use the site joblib instead of the vendored one was added (environment\_variable). The main API of joblib is now exposed in [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")
    . [#11166](https://github.com/scikit-learn/scikit-learn/issues/11166)
     by [Gael Varoquaux](https://gael-varoquaux.info/)
    .
    
*   Feature Add almost complete PyPy 3 support. Known unsupported functionalities are [`datasets.load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
    , [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")
     and [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer")
    . For running on PyPy, PyPy3-v5.10+, Numpy 1.14.0+, and scipy 1.1.0+ are required. [#11010](https://github.com/scikit-learn/scikit-learn/issues/11010)
     by [Ronan Lamy](https://github.com/rlamy)
     and [Roman Yurchak](https://github.com/rth)
    .
    
*   Feature A utility method [`sklearn.show_versions`](https://scikit-learn.org/stable/modules/generated/sklearn.show_versions.html#sklearn.show_versions "sklearn.show_versions")
     was added to print out information relevant for debugging. It includes the user system, the Python executable, the version of the main libraries and BLAS binding information. [#11596](https://github.com/scikit-learn/scikit-learn/issues/11596)
     by [Alexandre Boucaud](https://github.com/aboucaud)
    
*   Fix Fixed a bug when setting parameters on meta-estimator, involving both a wrapped estimator and its parameter. [#9999](https://github.com/scikit-learn/scikit-learn/issues/9999)
     by [Marcus Voss](https://github.com/marcus-voss)
     and [Joel Nothman](https://joelnothman.com/)
    .
    
*   Fix Fixed a bug where calling [`sklearn.base.clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")
     was not thread safe and could result in a “pop from empty list” error. [#9569](https://github.com/scikit-learn/scikit-learn/issues/9569)
     by [Andreas Müller](https://amueller.github.io/)
    .
    
*   API Change The default value of `n_jobs` is changed from `1` to `None` in all related functions and classes. `n_jobs=None` means `unset`. It will generally be interpreted as `n_jobs=1`, unless the current `joblib.Parallel` backend context specifies otherwise (See [Glossary](https://scikit-learn.org/stable/glossary.html#term-n_jobs)
     for additional information). Note that this change happens immediately (i.e., without a deprecation cycle). [#11741](https://github.com/scikit-learn/scikit-learn/issues/11741)
     by [Olivier Grisel](https://bsky.app/profile/ogrisel.bsky.social)
    .
    
*   Fix Fixed a bug in validation helpers where passing a Dask DataFrame results in an error. [#12462](https://github.com/scikit-learn/scikit-learn/issues/12462)
     by [Zachariah Miller](https://github.com/zwmiller)
    

### Changes to estimator checks[#](https://scikit-learn.org/stable/whats_new/v0.20.html#changes-to-estimator-checks "Link to this heading")

These changes mostly affect library developers.

*   Checks for transformers now apply if the estimator implements [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
    , regardless of whether it inherits from [`sklearn.base.TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")
    . [#10474](https://github.com/scikit-learn/scikit-learn/issues/10474)
     by [Joel Nothman](https://joelnothman.com/)
    .
    
*   Classifiers are now checked for consistency between [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
     and categorical predictions. [#10500](https://github.com/scikit-learn/scikit-learn/issues/10500)
     by [Narine Kokhlikyan](https://github.com/NarineK)
    .
    
*   Allow tests in [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     to test functions that accept pairwise data. [#9701](https://github.com/scikit-learn/scikit-learn/issues/9701)
     by [Kyle Johnson](https://github.com/gkjohns)
    
*   Allow [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     to check that there is no private settings apart from parameters during estimator initialization. [#9378](https://github.com/scikit-learn/scikit-learn/issues/9378)
     by [Herilalaina Rakotoarison](https://github.com/herilalaina)
    
*   The set of checks in [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     now includes a `check_set_params` test which checks that `set_params` is equivalent to passing parameters in `__init__` and warns if it encounters parameter validation. [#7738](https://github.com/scikit-learn/scikit-learn/issues/7738)
     by [Alvin Chiang](https://github.com/absolutelyNoWarranty)
    
*   Add invariance tests for clustering metrics. [#8102](https://github.com/scikit-learn/scikit-learn/issues/8102)
     by [Ankita Sinha](https://github.com/anki08)
     and [Guillaume Lemaitre](https://github.com/glemaitre)
    .
    
*   Add `check_methods_subset_invariance` to [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
    , which checks that estimator methods are invariant if applied to a data subset. [#10428](https://github.com/scikit-learn/scikit-learn/issues/10428)
     by [Jonathan Ohayon](https://github.com/Johayon)
    
*   Add tests in [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
     to check that an estimator can handle read-only memmap input data. [#10663](https://github.com/scikit-learn/scikit-learn/issues/10663)
     by [Arthur Mensch](https://github.com/arthurmensch)
     and [Loïc Estève](https://github.com/lesteve)
    .
    
*   `check_sample_weights_pandas_series` now uses 8 rather than 6 samples to accommodate for the default number of clusters in [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")
    . [#10933](https://github.com/scikit-learn/scikit-learn/issues/10933)
     by [Johannes Hansen](https://github.com/jnhansen)
    .
    
*   Estimators are now checked for whether `sample_weight=None` equates to `sample_weight=np.ones(...)`. [#11558](https://github.com/scikit-learn/scikit-learn/issues/11558)
     by [Sergul Aydore](https://github.com/sergulaydore)
    .
    

### Code and Documentation Contributors[#](https://scikit-learn.org/stable/whats_new/v0.20.html#id41 "Link to this heading")

Thanks to everyone who has contributed to the maintenance and improvement of the project since version 0.19, including:

211217613, Aarshay Jain, absolutelyNoWarranty, Adam Greenhall, Adam Kleczewski, Adam Richie-Halford, adelr, AdityaDaflapurkar, Adrin Jalali, Aidan Fitzgerald, aishgrt1, Akash Shivram, Alan Liddell, Alan Yee, Albert Thomas, Alexander Lenail, Alexander-N, Alexandre Boucaud, Alexandre Gramfort, Alexandre Sevin, Alex Egg, Alvaro Perez-Diaz, Amanda, Aman Dalmia, Andreas Bjerre-Nielsen, Andreas Mueller, Andrew Peng, Angus Williams, Aniruddha Dave, annaayzenshtat, Anthony Gitter, Antonio Quinonez, Anubhav Marwaha, Arik Pamnani, Arthur Ozga, Artiem K, Arunava, Arya McCarthy, Attractadore, Aurélien Bellet, Aurélien Geron, Ayush Gupta, Balakumaran Manoharan, Bangda Sun, Barry Hart, Bastian Venthur, Ben Lawson, Benn Roth, Breno Freitas, Brent Yi, brett koonce, Caio Oliveira, Camil Staps, cclauss, Chady Kamar, Charlie Brummitt, Charlie Newey, chris, Chris, Chris Catalfo, Chris Foster, Chris Holdgraf, Christian Braune, Christian Hirsch, Christian Hogan, Christopher Jenness, Clement Joudet, cnx, cwitte, Dallas Card, Dan Barkhorn, Daniel, Daniel Ferreira, Daniel Gomez, Daniel Klevebring, Danielle Shwed, Daniel Mohns, Danil Baibak, Darius Morawiec, David Beach, David Burns, David Kirkby, David Nicholson, David Pickup, Derek, Didi Bar-Zev, diegodlh, Dillon Gardner, Dillon Niederhut, dilutedsauce, dlovell, Dmitry Mottl, Dmitry Petrov, Dor Cohen, Douglas Duhaime, Ekaterina Tuzova, Eric Chang, Eric Dean Sanchez, Erich Schubert, Eunji, Fang-Chieh Chou, FarahSaeed, felix, Félix Raimundo, fenx, filipj8, FrankHui, Franz Wompner, Freija Descamps, frsi, Gabriele Calvo, Gael Varoquaux, Gaurav Dhingra, Georgi Peev, Gil Forsyth, Giovanni Giuseppe Costa, gkevinyen5418, goncalo-rodrigues, Gryllos Prokopis, Guillaume Lemaitre, Guillaume “Vermeille” Sanchez, Gustavo De Mari Pereira, hakaa1, Hanmin Qin, Henry Lin, Hong, Honghe, Hossein Pourbozorg, Hristo, Hunan Rostomyan, iampat, Ivan PANICO, Jaewon Chung, Jake VanderPlas, jakirkham, James Bourbeau, James Malcolm, Jamie Cox, Jan Koch, Jan Margeta, Jan Schlüter, janvanrijn, Jason Wolosonovich, JC Liu, Jeb Bearer, jeremiedbb, Jimmy Wan, Jinkun Wang, Jiongyan Zhang, jjabl, jkleint, Joan Massich, Joël Billaud, Joel Nothman, Johannes Hansen, JohnStott, Jonatan Samoocha, Jonathan Ohayon, Jörg Döpfert, Joris Van den Bossche, Jose Perez-Parras Toledano, josephsalmon, jotasi, jschendel, Julian Kuhlmann, Julien Chaumond, julietcl, Justin Shenk, Karl F, Kasper Primdal Lauritzen, Katrin Leinweber, Kirill, ksemb, Kuai Yu, Kumar Ashutosh, Kyeongpil Kang, Kye Taylor, kyledrogo, Leland McInnes, Léo DS, Liam Geron, Liutong Zhou, Lizao Li, lkjcalc, Loic Esteve, louib, Luciano Viola, Lucija Gregov, Luis Osa, Luis Pedro Coelho, Luke M Craig, Luke Persola, Mabel, Mabel Villalba, Maniteja Nandana, MarkIwanchyshyn, Mark Roth, Markus Müller, MarsGuy, Martin Gubri, martin-hahn, martin-kokos, mathurinm, Matthias Feurer, Max Copeland, Mayur Kulkarni, Meghann Agarwal, Melanie Goetz, Michael A. Alcorn, Minghui Liu, Ming Li, Minh Le, Mohamed Ali Jamaoui, Mohamed Maskani, Mohammad Shahebaz, Muayyad Alsadi, Nabarun Pal, Nagarjuna Kumar, Naoya Kanai, Narendran Santhanam, NarineK, Nathaniel Saul, Nathan Suh, Nicholas Nadeau, P.Eng., AVS, Nick Hoh, Nicolas Goix, Nicolas Hug, Nicolau Werneck, nielsenmarkus11, Nihar Sheth, Nikita Titov, Nilesh Kevlani, Nirvan Anjirbag, notmatthancock, nzw, Oleksandr Pavlyk, oliblum90, Oliver Rausch, Olivier Grisel, Oren Milman, Osaid Rehman Nasir, pasbi, Patrick Fernandes, Patrick Olden, Paul Paczuski, Pedro Morales, Peter, Peter St. John, pierreablin, pietruh, Pinaki Nath Chowdhury, Piotr Szymański, Pradeep Reddy Raamana, Pravar D Mahajan, pravarmahajan, QingYing Chen, Raghav RV, Rajendra arora, RAKOTOARISON Herilalaina, Rameshwar Bhaskaran, RankyLau, Rasul Kerimov, Reiichiro Nakano, Rob, Roman Kosobrodov, Roman Yurchak, Ronan Lamy, rragundez, Rüdiger Busche, Ryan, Sachin Kelkar, Sagnik Bhattacharya, Sailesh Choyal, Sam Radhakrishnan, Sam Steingold, Samuel Bell, Samuel O. Ronsin, Saqib Nizam Shamsi, SATISH J, Saurabh Gupta, Scott Gigante, Sebastian Flennerhag, Sebastian Raschka, Sebastien Dubois, Sébastien Lerique, Sebastin Santy, Sergey Feldman, Sergey Melderis, Sergul Aydore, Shahebaz, Shalil Awaley, Shangwu Yao, Sharad Vijalapuram, Sharan Yalburgi, shenhanc78, Shivam Rastogi, Shu Haoran, siftikha, Sinclert Pérez, SolutusImmensus, Somya Anand, srajan paliwal, Sriharsha Hatwar, Sri Krishna, Stefan van der Walt, Stephen McDowell, Steven Brown, syonekura, Taehoon Lee, Takanori Hayashi, tarcusx, Taylor G Smith, theriley106, Thomas, Thomas Fan, Thomas Heavey, Tobias Madsen, tobycheese, Tom Augspurger, Tom Dupré la Tour, Tommy, Trevor Stephens, Trishnendu Ghorai, Tulio Casagrande, twosigmajab, Umar Farouk Umar, Urvang Patel, Utkarsh Upadhyay, Vadim Markovtsev, Varun Agrawal, Vathsala Achar, Vilhelm von Ehrenheim, Vinayak Mehta, Vinit, Vinod Kumar L, Viraj Mavani, Viraj Navkal, Vivek Kumar, Vlad Niculae, vqean3, Vrishank Bhardwaj, vufg, wallygauze, Warut Vijitbenjaronk, wdevazelhes, Wenhao Zhang, Wes Barnett, Will, William de Vazelhes, Will Rosenfeld, Xin Xiong, Yiming (Paul) Li, ymazari, Yufeng, Zach Griffith, Zé Vinícius, Zhenqing Hu, Zhiqing Xiao, Zijie (ZJ) Poh

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)