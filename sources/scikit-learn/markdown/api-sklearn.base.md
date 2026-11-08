[Skip to main content](https://scikit-learn.org/stable/api/sklearn.base.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.base.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.base.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.base.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.base.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.base.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.base.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.base.html)

Collapse Sidebar Expand Sidebar

sklearn.base[#](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "Link to this heading")

==================================================================================================================

Base classes for all estimators and various utility functions.

|     |     |
| --- | --- |
| [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator") | Base class for all estimators in scikit-learn. |
| [`BiclusterMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#sklearn.base.BiclusterMixin "sklearn.base.BiclusterMixin") | Mixin class for all bicluster estimators in scikit-learn. |
| [`ClassNamePrefixFeaturesOutMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin "sklearn.base.ClassNamePrefixFeaturesOutMixin") | Mixin class for transformers that generate their own names by prefixing. |
| [`ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin") | Mixin class for all classifiers in scikit-learn. |
| [`ClusterMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin "sklearn.base.ClusterMixin") | Mixin class for all cluster estimators in scikit-learn. |
| [`DensityMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html#sklearn.base.DensityMixin "sklearn.base.DensityMixin") | Mixin class for all density estimators in scikit-learn. |
| [`MetaEstimatorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin") | Mixin class for all meta estimators in scikit-learn. |
| [`OneToOneFeatureMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#sklearn.base.OneToOneFeatureMixin "sklearn.base.OneToOneFeatureMixin") | Provides `get_feature_names_out` for simple transformers. |
| [`OutlierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin "sklearn.base.OutlierMixin") | Mixin class for all outlier detection estimators in scikit-learn. |
| [`RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin") | Mixin class for all regression estimators in scikit-learn. |
| [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin") | Mixin class for all transformers in scikit-learn. |
| [`clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone") | Construct a new unfitted estimator with the same parameters. |
| [`is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier") | Return True if the given estimator is (probably) a classifier. |
| [`is_clusterer`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_clusterer.html#sklearn.base.is_clusterer "sklearn.base.is_clusterer") | Return True if the given estimator is (probably) a clusterer. |
| [`is_regressor`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_regressor.html#sklearn.base.is_regressor "sklearn.base.is_regressor") | Return True if the given estimator is (probably) a regressor. |
| [`is_outlier_detector`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_outlier_detector.html#sklearn.base.is_outlier_detector "sklearn.base.is_outlier_detector") | Return True if the given estimator is (probably) an outlier detector. |