[Skip to main content](https://scikit-learn.org/stable/api/sklearn.multiclass.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

sklearn.multiclass[#](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "Link to this heading")

====================================================================================================================================

Multiclass learning algorithms.

*   one-vs-the-rest / one-vs-all
    
*   one-vs-one
    
*   error correcting output codes
    

The estimators provided in this module are meta-estimators: they require a base estimator to be provided in their constructor. For example, it is possible to use these estimators to turn a binary classifier or a regressor into a multiclass classifier. It is also possible to use these estimators with multiclass estimators in the hope that their accuracy or runtime performance improves.

All classifiers in scikit-learn implement multiclass classification; you only need to use this module if you want to experiment with custom multiclass strategies.

The one-vs-the-rest meta-classifier also implements a `predict_proba` method, so long as such a method is implemented by the base classifier. This method returns probabilities of class membership in both the single label and multilabel case. Note that in the multilabel case, probabilities are the marginal probability that a given sample falls in the given class. As such, in the multilabel case the sum of these probabilities over all possible labels for a given sample _will not_ sum to unity, as they do in the single label case.

**User guide.** See the [Multiclass classification](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification)
 section for further details.

|     |     |
| --- | --- |
| [`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier") | One-vs-one multiclass strategy. |
| [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier") | One-vs-the-rest (OvR) multiclass strategy. |
| [`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier") | (Error-Correcting) Output-Code multiclass strategy. |