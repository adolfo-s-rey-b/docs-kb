[Skip to main content](https://scikit-learn.org/stable/whats_new/v1.8.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/whats_new/v1.8.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/whats_new/v1.8.html)
[1.8.0](https://scikit-learn.org/1.8/whats_new/v1.8.html)
[1.7.2](https://scikit-learn.org/1.7/whats_new/v1.8.html)
[1.6.1](https://scikit-learn.org/1.6/whats_new/v1.8.html)
[1.5.2](https://scikit-learn.org/1.5/whats_new/v1.8.html)
[1.4.2](https://scikit-learn.org/1.4/whats_new/v1.8.html)

Collapse Sidebar Expand Sidebar

Version 1.8[#](https://scikit-learn.org/stable/whats_new/v1.8.html#version-1-8 "Link to this heading")

=======================================================================================================

For a short description of the main highlights of the release, please refer to [Release Highlights for scikit-learn 1.8](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#sphx-glr-auto-examples-release-highlights-plot-release-highlights-1-8-0-py)
.

Legend for changelogs

*   Major Feature something big that you couldn’t do before.
    
*   Feature something that you couldn’t do before.
    
*   Efficiency an existing feature now may not require as much computation or memory.
    
*   Enhancement a miscellaneous minor improvement.
    
*   Fix something that previously didn’t work as documented – or according to reasonable expectations – should now work.
    
*   API Change you will need to change your code to have the same effect in the future; or a feature will be removed in the future.
    

Version 1.8.0[#](https://scikit-learn.org/stable/whats_new/v1.8.html#version-1-8-0 "Link to this heading")

-----------------------------------------------------------------------------------------------------------

**December 2025**

### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.8.html#changes-impacting-many-modules "Link to this heading")

*   Efficiency Improved CPU and memory usage in estimators and metric functions that rely on weighted percentiles and better match NumPy and Scipy (un-weighted) implementations of percentiles. By [Lucy Liu](https://github.com/lucyleeow)
     [#31775](https://github.com/scikit-learn/scikit-learn/pull/31775)
    

### Support for Array API[#](https://scikit-learn.org/stable/whats_new/v1.8.html#support-for-array-api "Link to this heading")

Additional estimators and functions have been updated to include support for all [Array API](https://data-apis.org/array-api/latest/)
 compliant inputs.

See [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

*   Feature [`sklearn.preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
     now supports Array API compliant inputs. By [Alexander Fabisch](https://github.com/AlexanderFabisch)
    , [Edoardo Abati](https://github.com/EdAbati)
    , [Olivier Grisel](https://github.com/ogrisel)
     and [Charles Hill](https://github.com/charlesjhill)
    . [#27113](https://github.com/scikit-learn/scikit-learn/pull/27113)
    
*   Feature [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    , [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
     and [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
     now support array API compatible inputs with `solver="svd"`. By [Jérôme Dockès](https://github.com/jeromedockes)
    . [#27961](https://github.com/scikit-learn/scikit-learn/pull/27961)
    
*   Feature [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")
     for any kernel except “laplacian” and [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")
     for metrics “cosine”, “euclidean” and “l2” now support array API inputs. By [Emily Chen](https://github.com/EmilyXinyi)
     and [Lucy Liu](https://github.com/lucyleeow)
     [#29822](https://github.com/scikit-learn/scikit-learn/pull/29822)
    
*   Feature [`sklearn.metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")
     now supports Array API compatible inputs. By [Stefanie Senger](https://github.com/StefanieSenger)
     [#30562](https://github.com/scikit-learn/scikit-learn/pull/30562)
    
*   Feature [`sklearn.mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
     with `init_params="random"` or `init_params="random_from_data"` and `warm_start=False` now supports Array API compatible inputs. By [Stefanie Senger](https://github.com/StefanieSenger)
     and [Loïc Estève](https://github.com/lesteve)
     [#30777](https://github.com/scikit-learn/scikit-learn/pull/30777)
    
*   Feature [`sklearn.metrics.roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")
     now supports Array API compatible inputs. By [Thomas Li](https://github.com/lithomas1)
     [#30878](https://github.com/scikit-learn/scikit-learn/pull/30878)
    
*   Feature [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     now supports array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#31580](https://github.com/scikit-learn/scikit-learn/pull/31580)
    
*   Feature [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
     now supports array API compatible inputs with `method="temperature"` and when the underlying `estimator` also supports the array API. By [Omar Salman](https://github.com/OmarManzoor)
     [#32246](https://github.com/scikit-learn/scikit-learn/pull/32246)
    
*   Feature [`sklearn.metrics.precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")
     now supports array API compatible inputs. By [Lucy Liu](https://github.com/lucyleeow)
     [#32249](https://github.com/scikit-learn/scikit-learn/pull/32249)
    
*   Feature [`sklearn.model_selection.cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")
     now supports array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#32270](https://github.com/scikit-learn/scikit-learn/pull/32270)
    
*   Feature [`sklearn.metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")
    , [`sklearn.metrics.log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")
    , [`sklearn.metrics.d2_brier_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "sklearn.metrics.d2_brier_score")
     and [`sklearn.metrics.d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")
     now support array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#32422](https://github.com/scikit-learn/scikit-learn/pull/32422)
    
*   Feature [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
     now supports array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
     [#32497](https://github.com/scikit-learn/scikit-learn/pull/32497)
    
*   Feature [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
     and [`preprocessing.label_binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")
     now support numeric array API compatible inputs with `sparse_output=False`. By [Virgil Chan](https://github.com/virchan)
    . [#32582](https://github.com/scikit-learn/scikit-learn/pull/32582)
    
*   Feature [`sklearn.metrics.det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")
     now supports Array API compliant inputs. By [Josef Affourtit](https://github.com/jaffourt)
    . [#32586](https://github.com/scikit-learn/scikit-learn/pull/32586)
    
*   Feature [`sklearn.metrics.pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances")
     now supports array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
    . [#32597](https://github.com/scikit-learn/scikit-learn/pull/32597)
    
*   Feature [`sklearn.metrics.calinski_harabasz_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score "sklearn.metrics.calinski_harabasz_score")
     now supports Array API compliant inputs. By [Josef Affourtit](https://github.com/jaffourt)
    . [#32600](https://github.com/scikit-learn/scikit-learn/pull/32600)
    
*   Feature [`sklearn.metrics.balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score")
     now supports array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
    . [#32604](https://github.com/scikit-learn/scikit-learn/pull/32604)
    
*   Feature [`sklearn.metrics.pairwise.laplacian_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#sklearn.metrics.pairwise.laplacian_kernel "sklearn.metrics.pairwise.laplacian_kernel")
     now supports array API compatible inputs. By [Zubair Shakoor](https://github.com/zubairshakoorarbisoft)
    . [#32613](https://github.com/scikit-learn/scikit-learn/pull/32613)
    
*   Feature [`sklearn.metrics.cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")
     now supports array API compatible inputs. By [Omar Salman](https://github.com/OmarManzoor)
    . [#32619](https://github.com/scikit-learn/scikit-learn/pull/32619)
    
*   Feature `sklearn.metrics.cluster.davies_bouldin_score` now supports Array API compliant inputs. By [Josef Affourtit](https://github.com/jaffourt)
    . [#32693](https://github.com/scikit-learn/scikit-learn/pull/32693)
    
*   Fix Estimators with array API support no longer reject dataframe inputs when array API support is enabled. By [Tim Head](https://github.com/betatim)
     [#32838](https://github.com/scikit-learn/scikit-learn/pull/32838)
    

### Metadata routing[#](https://scikit-learn.org/stable/whats_new/v1.8.html#metadata-routing "Link to this heading")

Refer to the [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 for more details.

*   Fix Fixed an issue where passing `sample_weight` to a `Pipeline` inside a `GridSearchCV` would raise an error with metadata routing enabled. By [Adrin Jalali](https://github.com/adrinjalali)
    . [#31898](https://github.com/scikit-learn/scikit-learn/pull/31898)
    

### Free-threaded CPython 3.14 support[#](https://scikit-learn.org/stable/whats_new/v1.8.html#free-threaded-cpython-3-14-support "Link to this heading")

scikit-learn has support for free-threaded CPython, in particular free-threaded wheels are available for all of our supported platforms on Python 3.14.

Free-threaded (also known as nogil) CPython is a version of CPython that aims at enabling efficient multi-threaded use cases by removing the Global Interpreter Lock (GIL).

If you want to try out free-threaded Python, the recommendation is to use Python 3.14, that has fixed a number of issues compared to Python 3.13. Feel free to try free-threaded on your use case and report any issues!

For more details about free-threaded CPython see [py-free-threading doc](https://py-free-threading.github.io/)
, in particular [how to install a free-threaded CPython](https://py-free-threading.github.io/installing_cpython/)
 and [Ecosystem compatibility tracking](https://py-free-threading.github.io/tracking/)
.

By [Loïc Estève](https://github.com/lesteve)
 and [Olivier Grisel](https://github.com/ogrisel)
 and many other people in the wider Scientific Python and CPython ecosystem, for example [Nathan Goldbaum](https://github.com/ngoldbaum)
, [Ralf Gommers](https://github.com/rgommers)
, [Edgar Andrés Margffoy Tuay](https://github.com/andfoy)
. [#32079](https://github.com/scikit-learn/scikit-learn/pull/32079)

### [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-base "Link to this heading")

*   Feature Refactored `dir` in `BaseEstimator` to recognize condition check in `available_if`. By [John Hendricks](https://github.com/j-hendricks)
     and [Miguel Parece](https://github.com/MiguelParece)
    . [#31928](https://github.com/scikit-learn/scikit-learn/pull/31928)
    
*   Fix Fixed the handling of pandas missing values in HTML display of all estimators. By [Dea María Léon](https://github.com/deamarialeon)
    . [#32341](https://github.com/scikit-learn/scikit-learn/pull/32341)
    

### [`sklearn.calibration`](https://scikit-learn.org/stable/api/sklearn.calibration.html#module-sklearn.calibration "sklearn.calibration")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-calibration "Link to this heading")

*   Feature Added temperature scaling method in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
    . By [Virgil Chan](https://github.com/virchan)
     and [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31068](https://github.com/scikit-learn/scikit-learn/pull/31068)
    

### [`sklearn.cluster`](https://scikit-learn.org/stable/api/sklearn.cluster.html#module-sklearn.cluster "sklearn.cluster")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-cluster "Link to this heading")

*   Efficiency [`cluster.kmeans_plusplus`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")
     now uses `np.cumsum` directly without extra numerical stability checks and without casting to `np.float64`. By [Tiziano Zito](https://github.com/otizonaizit)
     [#31991](https://github.com/scikit-learn/scikit-learn/pull/31991)
    
*   Fix The default value of the `copy` parameter in [`cluster.HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")
     will change from `False` to `True` in 1.10 to avoid data modification and maintain consistency with other estimators. By [Sarthak Puri](https://github.com/sarthakpurii)
    . [#31973](https://github.com/scikit-learn/scikit-learn/pull/31973)
    

### [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-compose "Link to this heading")

*   Fix The [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
     now correctly fits on data provided as a `polars.DataFrame` when any transformer has a sparse output. By [Phillipp Gnan](https://github.com/ph-ll-pp)
    . [#32188](https://github.com/scikit-learn/scikit-learn/pull/32188)
    

### [`sklearn.covariance`](https://scikit-learn.org/stable/api/sklearn.covariance.html#module-sklearn.covariance "sklearn.covariance")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-covariance "Link to this heading")

*   Efficiency [`sklearn.covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
    , [`sklearn.covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
     and [`sklearn.covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
     with `mode="cd"` profit from the fit time performance improvement of [`sklearn.linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     by means of gap safe screening rules. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31987](https://github.com/scikit-learn/scikit-learn/pull/31987)
    
*   Fix Fixed uncontrollable randomness in [`sklearn.covariance.GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")
    , [`sklearn.covariance.GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")
     and [`sklearn.covariance.graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")
    . For `mode="cd"`, they now use cyclic coordinate descent. Before, it was random coordinate descent with uncontrollable random number seeding. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31987](https://github.com/scikit-learn/scikit-learn/pull/31987)
    
*   Fix Added correction to [`covariance.MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")
     to adjust for consistency at the normal distribution. This reduces the bias present when applying this method to data that is normally distributed. By [Daniel Herrera-Esposito](https://github.com/dherrera1911)
     [#32117](https://github.com/scikit-learn/scikit-learn/pull/32117)
    

### [`sklearn.decomposition`](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "sklearn.decomposition")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-decomposition "Link to this heading")

*   Efficiency [`sklearn.decomposition.DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")
     and [`sklearn.decomposition.MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning")
     with `fit_algorithm="cd"`, [`sklearn.decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     with `transform_algorithm="lasso_cd"`, [`sklearn.decomposition.MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")
    , [`sklearn.decomposition.SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")
    , [`sklearn.decomposition.dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")
     and [`sklearn.decomposition.dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")
     with `method="cd"`, [`sklearn.decomposition.sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")
     with `algorithm="lasso_cd"` all profit from the fit time performance improvement of [`sklearn.linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     by means of gap safe screening rules. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31987](https://github.com/scikit-learn/scikit-learn/pull/31987)
    
*   Enhancement [`decomposition.SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
     now follows the transformer API of scikit-learn. In addition, the `fit` method now validates the input and parameters. By [François Paugam](https://github.com/FrancoisPgm)
    . [#32077](https://github.com/scikit-learn/scikit-learn/pull/32077)
    
*   Fix Add input checks to the `inverse_transform` method of [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
     and [`decomposition.IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")
    . [#29310](https://github.com/scikit-learn/scikit-learn/pull/29310)
     by [Ian Faust](https://github.com/icfaust)
    . [#29310](https://github.com/scikit-learn/scikit-learn/pull/29310)
    

### [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/api/sklearn.discriminant_analysis.html#module-sklearn.discriminant_analysis "sklearn.discriminant_analysis")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-discriminant-analysis "Link to this heading")

*   Feature Added `solver`, `covariance_estimator` and `shrinkage` in [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
    . The resulting class is more similar to [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
     and allows for more flexibility in the estimation of the covariance matrices. By [Daniel Herrera-Esposito](https://github.com/dherrera1911)
    . [#32108](https://github.com/scikit-learn/scikit-learn/pull/32108)
    

### [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-ensemble "Link to this heading")

*   Fix [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")
    , [`ensemble.BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")
     and [`ensemble.IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")
     now use `sample_weight` to draw the samples instead of forwarding them multiplied by a uniformly sampled mask to the underlying estimators. Furthermore, when `max_samples` is a float, it is now interpreted as a fraction of `sample_weight.sum()` instead of `X.shape[0]`. The new default `max_samples=None` draws `X.shape[0]` samples, irrespective of `sample_weight`. By [Antoine Baker](https://github.com/antoinebaker)
    . [#31414](https://github.com/scikit-learn/scikit-learn/pull/31414)
     and [#32825](https://github.com/scikit-learn/scikit-learn/pull/32825)
    

### [`sklearn.feature_selection`](https://scikit-learn.org/stable/api/sklearn.feature_selection.html#module-sklearn.feature_selection "sklearn.feature_selection")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-feature-selection "Link to this heading")

*   Enhancement [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")
     now does not force `max_features` to be less than or equal to the number of input features. By [Thibault](https://github.com/ThibaultDECO)
     [#31939](https://github.com/scikit-learn/scikit-learn/pull/31939)
    

### [`sklearn.gaussian_process`](https://scikit-learn.org/stable/api/sklearn.gaussian_process.html#module-sklearn.gaussian_process "sklearn.gaussian_process")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-gaussian-process "Link to this heading")

*   Efficiency make `GaussianProcessRegressor.predict` faster when `return_cov` and `return_std` are both `False`. By [Rafael Ayllón Gavilán](https://github.com/RafaAyGar)
    . [#31431](https://github.com/scikit-learn/scikit-learn/pull/31431)
    

### [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-linear-model "Link to this heading")

*   Efficiency [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     with `precompute=False` use less memory for dense `X` and are a bit faster. Previously, they used twice the memory of `X` even for Fortran-contiguous `X`. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#31665](https://github.com/scikit-learn/scikit-learn/pull/31665)
    
*   Efficiency [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
     and [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
     avoid double input checking and are therefore a bit faster. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31848](https://github.com/scikit-learn/scikit-learn/pull/31848)
    
*   Efficiency [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
    , [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
     and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     are faster to fit by avoiding a BLAS level 1 (axpy) call in the innermost loop. Same for functions [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     and [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
    . By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#31956](https://github.com/scikit-learn/scikit-learn/pull/31956)
     and [#31880](https://github.com/scikit-learn/scikit-learn/pull/31880)
    
*   Efficiency [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     and [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     avoid an additional copy of `X` with default `copy_X=True`. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31946](https://github.com/scikit-learn/scikit-learn/pull/31946)
    
*   Efficiency [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    , [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
     [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
    , [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
     as well as [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     and [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     now implement gap safe screening rules in the coordinate descent solver for dense and sparse `X`. The speedup of fitting time is particularly pronounced (10-times is possible) when computing regularization paths like the \*CV-variants of the above estimators do. There is now an additional check of the stopping criterion before entering the main loop of descent steps. As the stopping criterion requires the computation of the dual gap, the screening happens whenever the dual gap is computed. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#31882](https://github.com/scikit-learn/scikit-learn/pull/31882)
    , [#31986](https://github.com/scikit-learn/scikit-learn/pull/31986)
    , [#31987](https://github.com/scikit-learn/scikit-learn/pull/31987)
     and [#32014](https://github.com/scikit-learn/scikit-learn/pull/32014)
    
*   Enhancement [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    , [`linear_model.ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")
    , [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    , [`linear_model.LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")
    , `MultiTaskElasticNet`, `MultiTaskElasticNetCV`, `MultiTaskLasso`, `MultiTaskLassoCV`, as well as [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")
     and [`linear_model.lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")
     now use `dual gap <= tol` instead of `dual gap < tol` as stopping criterion. The resulting coefficients might differ to previous versions of scikit-learn in rare cases. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31906](https://github.com/scikit-learn/scikit-learn/pull/31906)
    
*   Fix Fix the convergence criteria for SGD models, to avoid premature convergence when `tol != None`. This primarily impacts `SGDOneClassSVM` but also affects `SGDClassifier` and `SGDRegressor`. Before this fix, only the loss function without penalty was used as the convergence check, whereas now, the full objective with regularization is used. By [Guillaume Lemaitre](https://github.com/glemaitre)
     and [kostayScr](https://github.com/kostayScr)
     [#31856](https://github.com/scikit-learn/scikit-learn/pull/31856)
    
*   Fix The allowed parameter range for the initial learning rate `eta0` in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
     and [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
     changed from non-negative numbers to strictly positive numbers. As a consequence, the default `eta0` of [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     changed from 0 to 0.01. But note that `eta0` is not used by the default learning rate “optimal” of those two estimators. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#31933](https://github.com/scikit-learn/scikit-learn/pull/31933)
    
*   Enhancement [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
     is able to handle CV splits where some class labels are missing in some folds. Before, it raised an error whenever a class label were missing in a fold. By [Christian Lorentzen](https://github.com/lorentzenchr)
    . [#32747](https://github.com/scikit-learn/scikit-learn/pull/32747)
    
*   API Change [`linear_model.PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier")
     and [`linear_model.PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor")
     are deprecated and will be removed in 1.10. Equivalent estimators are available with [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
     and `SGDRegressor`, both of which expose the options `learning_rate="pa1"` and `"pa2"`. The parameter `eta0` can be used to specify the aggressiveness parameter of the Passive-Aggressive-Algorithms, called C in the reference paper. By [Christian Lorentzen](https://github.com/lorentzenchr)
     [#31932](https://github.com/scikit-learn/scikit-learn/pull/31932)
     and [#29097](https://github.com/scikit-learn/scikit-learn/pull/29097)
    
*   API Change [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
    , [`linear_model.SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")
    , and [`linear_model.SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")
     now deprecate negative values for the `power_t` parameter. Using a negative value will raise a warning in version 1.8 and will raise an error in version 1.10. A value in the range \[0.0, inf) must be used instead. By [Ritvi Alagusankar](https://github.com/ritvi-alagusankar)\
     [#31474](https://github.com/scikit-learn/scikit-learn/pull/31474)\
    \
*   API Change Raising error in [`sklearn.linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
     when liblinear solver is used and input X values are larger than 1e30, the liblinear solver freezes otherwise. By [Shruti Nath](https://github.com/snath-xoc)\
    . [#31888](https://github.com/scikit-learn/scikit-learn/pull/31888)\
    \
*   API Change [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")\
     got a new parameter `use_legacy_attributes` to control the types and shapes of the fitted attributes `C_`, `l1_ratio_`, `coefs_paths_`, `scores_` and `n_iter_`. The current default value `True` keeps the legacy behaviour. If `False` then:\
    \
    *   `C_` is a float.\
        \
    *   `l1_ratio_` is a float.\
        \
    *   `coefs_paths_` is an ndarray of shape (n\_folds, n\_l1\_ratios, n\_cs, n\_classes, n\_features). For binary problems (n\_classes=2), the 2nd last dimension is 1.\
        \
    *   `scores_` is an ndarray of shape (n\_folds, n\_l1\_ratios, n\_cs).\
        \
    *   `n_iter_` is an ndarray of shape (n\_folds, n\_l1\_ratios, n\_cs).\
        \
    \
    In version 1.10, the default will change to `False` and `use_legacy_attributes` will be deprecated. In 1.12 `use_legacy_attributes` will be removed. By [Christian Lorentzen](https://github.com/lorentzenchr)\
    . [#32114](https://github.com/scikit-learn/scikit-learn/pull/32114)\
    \
*   API Change Parameter `penalty` of [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
     and [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")\
     is deprecated and will be removed in version 1.10. The equivalent behaviour can be obtained as follows:\
    \
    *   for [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
        \
        *   use `l1_ratio=0` instead of `penalty="l2"`\
            \
        *   use `l1_ratio=1` instead of `penalty="l1"`\
            \
        *   use `0<l1_ratio<1` instead of `penalty="elasticnet"`\
            \
        *   use `C=np.inf` instead of `penalty=None`\
            \
    *   for [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")\
        \
        *   use `l1_ratios=(0,)` instead of `penalty="l2"`\
            \
        *   use `l1_ratios=(1,)` instead of `penalty="l1"`\
            \
        *   the equivalent of `penalty=None` is to have `np.inf` as an element of the `Cs` parameter\
            \
    \
    For [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
    , the default value of `l1_ratio` has changed from `None` to `0.0`. Setting `l1_ratio=None` is deprecated and will raise an error in version 1.10\
    \
    For [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")\
    , the default value of `l1_ratios` has changed from `None` to `"warn"`. It will be changed to `(0,)` in version 1.10. Setting `l1_ratios=None` is deprecated and will raise an error in version 1.10.\
    \
    By [Christian Lorentzen](https://github.com/lorentzenchr)\
    . [#32659](https://github.com/scikit-learn/scikit-learn/pull/32659)\
    \
*   API Change The `n_jobs` parameter of [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")\
     is deprecated and will be removed in 1.10. It has no effect since 1.8. By [Loïc Estève](https://github.com/lesteve)\
    . [#32742](https://github.com/scikit-learn/scikit-learn/pull/32742)\
    \
\
### [`sklearn.manifold`](https://scikit-learn.org/stable/api/sklearn.manifold.html#module-sklearn.manifold "sklearn.manifold")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-manifold "Link to this heading")\
\
*   Major Feature [`manifold.ClassicalMDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")\
     was implemented to perform classical MDS (eigendecomposition of the double-centered distance matrix). By [Dmitry Kobak](https://github.com/dkobak)\
     and [Meekail Zain](https://github.com/Micky774)\
     [#31322](https://github.com/scikit-learn/scikit-learn/pull/31322)\
    \
*   Feature [`manifold.MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")\
     now supports arbitrary distance metrics (via `metric` and `metric_params` parameters) and initialization via classical MDS (via `init` parameter). The `dissimilarity` parameter was deprecated. The old `metric` parameter was renamed into `metric_mds`. By [Dmitry Kobak](https://github.com/dkobak)\
     [#32229](https://github.com/scikit-learn/scikit-learn/pull/32229)\
    \
*   Feature [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")\
     now supports PCA initialization with sparse input matrices. By [Arturo Amor](https://github.com/ArturoAmorQ)\
    . [#32433](https://github.com/scikit-learn/scikit-learn/pull/32433)\
    \
\
### [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-metrics "Link to this heading")\
\
*   Feature [`metrics.d2_brier_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "sklearn.metrics.d2_brier_score")\
     has been added which calculates the D^2 for the Brier score. By [Omar Salman](https://github.com/OmarManzoor)\
    . [#28971](https://github.com/scikit-learn/scikit-learn/pull/28971)\
    \
*   Feature Add [`metrics.confusion_matrix_at_thresholds`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix_at_thresholds.html#sklearn.metrics.confusion_matrix_at_thresholds "sklearn.metrics.confusion_matrix_at_thresholds")\
     function that returns the number of true negatives, false positives, false negatives and true positives per threshold. By [Success Moses](https://github.com/SuccessMoses)\
    . [#30134](https://github.com/scikit-learn/scikit-learn/pull/30134)\
    \
*   Efficiency Avoid redundant input validation in [`metrics.d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")\
     leading to a 1.2x speedup in large scale benchmarks. By [Olivier Grisel](https://github.com/ogrisel)\
     and [Omar Salman](https://github.com/OmarManzoor)\
     [#32356](https://github.com/scikit-learn/scikit-learn/pull/32356)\
    \
*   Enhancement [`metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
     now supports Array API compatible inputs. By [Lucy Liu](https://github.com/lucyleeow)\
    . [#31406](https://github.com/scikit-learn/scikit-learn/pull/31406)\
    \
*   Enhancement Improved the error message for sparse inputs for the following metrics: [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")\
    , [`metrics.multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")\
    , [`metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")\
    , [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")\
    , [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")\
    , [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")\
    , [`metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")\
    , [`metrics.class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")\
    , [`metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")\
    , [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")\
    , [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")\
    , [`metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")\
    . By [Lucy Liu](https://github.com/lucyleeow)\
    . [#32047](https://github.com/scikit-learn/scikit-learn/pull/32047)\
    \
*   Fix [`metrics.median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")\
     now uses `_averaged_weighted_percentile` instead of `_weighted_percentile` to calculate median when `sample_weight` is not `None`. This is equivalent to using the “averaged\_inverted\_cdf” instead of the “inverted\_cdf” quantile method, which gives results equivalent to `numpy.median` if equal weights used. By [Lucy Liu](https://github.com/lucyleeow)\
     [#30787](https://github.com/scikit-learn/scikit-learn/pull/30787)\
    \
*   Fix Additional `sample_weight` checking has been added to [`metrics.accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")\
    , [`metrics.balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score")\
    , [`metrics.brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")\
    , [`metrics.class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")\
    , [`metrics.classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")\
    , [`metrics.cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")\
    , [`metrics.confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")\
    , [`metrics.f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")\
    , [`metrics.fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")\
    , [`metrics.hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")\
    , [`metrics.jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")\
    , [`metrics.matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")\
    , [`metrics.multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")\
    , [`metrics.precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support")\
    , [`metrics.precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")\
    , [`metrics.recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")\
     and [`metrics.zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")\
    . `sample_weight` can only be 1D, consistent to `y_true` and `y_pred` in length,and all values must be finite and not complex. By [Lucy Liu](https://github.com/lucyleeow)\
    . [#31701](https://github.com/scikit-learn/scikit-learn/pull/31701)\
    \
*   Fix `y_pred` is deprecated in favour of `y_score` in [`metrics.DetCurveDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay.from_predictions "sklearn.metrics.DetCurveDisplay.from_predictions")\
     and [`metrics.PrecisionRecallDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay.from_predictions "sklearn.metrics.PrecisionRecallDisplay.from_predictions")\
    . `y_pred` will be removed in v1.10. By [Luis](https://github.com/luiser1401)\
     [#31764](https://github.com/scikit-learn/scikit-learn/pull/31764)\
    \
*   Fix `repr` on a scorer which has been created with a `partial` `score_func` now correctly works and uses the `repr` of the given `partial` object. By [Adrin Jalali](https://github.com/adrinjalali)\
    . [#31891](https://github.com/scikit-learn/scikit-learn/pull/31891)\
    \
*   Fix kwargs specified in the `curve_kwargs` parameter of [`metrics.RocCurveDisplay.from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")\
     now only overwrite their corresponding default value before being passed to Matplotlib’s `plot`. Previously, passing any `curve_kwargs` would overwrite all default kwargs. By [Lucy Liu](https://github.com/lucyleeow)\
    . [#32313](https://github.com/scikit-learn/scikit-learn/pull/32313)\
    \
*   Fix Registered named scorer objects for [`metrics.d2_brier_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_brier_score.html#sklearn.metrics.d2_brier_score "sklearn.metrics.d2_brier_score")\
     and [`metrics.d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")\
     and updated their input validation to be consistent with related metric functions. By [Olivier Grisel](https://github.com/ogrisel)\
     and [Omar Salman](https://github.com/OmarManzoor)\
     [#32356](https://github.com/scikit-learn/scikit-learn/pull/32356)\
    \
*   Fix [`metrics.RocCurveDisplay.from_cv_results`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay.from_cv_results "sklearn.metrics.RocCurveDisplay.from_cv_results")\
     will now infer `pos_label` as `estimator.classes_[-1]`, using the estimator from `cv_results`, when `pos_label=None`. Previously, an error was raised when `pos_label=None`. By [Lucy Liu](https://github.com/lucyleeow)\
    . [#32372](https://github.com/scikit-learn/scikit-learn/pull/32372)\
    \
*   Fix All classification metrics now raise a `ValueError` when required input arrays (`y_pred`, `y_true`, `y1`, `y2`, `pred_decision`, or `y_proba`) are empty. Previously, `accuracy_score`, `class_likelihood_ratios`, `classification_report`, `confusion_matrix`, `hamming_loss`, `jaccard_score`, `matthews_corrcoef`, `multilabel_confusion_matrix`, and `precision_recall_fscore_support` did not raise this error consistently. By [Stefanie Senger](https://github.com/StefanieSenger)\
    . [#32549](https://github.com/scikit-learn/scikit-learn/pull/32549)\
    \
*   API Change `metrics.cluster.entropy` is deprecated and will be removed in v1.10. By [Lucy Liu](https://github.com/lucyleeow)\
     [#31294](https://github.com/scikit-learn/scikit-learn/pull/31294)\
    \
*   API Change The `estimator_name` parameter is deprecated in favour of `name` in [`metrics.PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay")\
     and will be removed in 1.10. By [Lucy Liu](https://github.com/lucyleeow)\
    . [#32310](https://github.com/scikit-learn/scikit-learn/pull/32310)\
    \
\
### [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-model-selection "Link to this heading")\
\
*   Enhancement [`model_selection.StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")\
     will now specify which classes\
    \
    have too few members when raising a `ValueError` if any class has less than 2 members. This is useful to identify which classes are causing the error. By [Marc Bresson](https://github.com/MarcBresson)\
     [#32265](https://github.com/scikit-learn/scikit-learn/pull/32265)\
    \
*   Fix Fix shuffle behaviour in [`model_selection.StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")\
    . Now stratification among folds is also preserved when `shuffle=True`. By [Pau Folch](https://github.com/pfolch)\
    . [#32540](https://github.com/scikit-learn/scikit-learn/pull/32540)\
    \
\
### [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-multiclass "Link to this heading")\
\
*   Fix Fix tie-breaking behavior in [`multiclass.OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")\
     to match `np.argmax` tie-breaking behavior. By [Lakshmi Krishnan](https://github.com/lakrish)\
    . [#15504](https://github.com/scikit-learn/scikit-learn/pull/15504)\
    \
\
### [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-naive-bayes "Link to this heading")\
\
*   Fix [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")\
     preserves the dtype of the fitted attributes according to the dtype of `X`. By [Omar Salman](https://github.com/OmarManzoor)\
     [#32497](https://github.com/scikit-learn/scikit-learn/pull/32497)\
    \
\
### [`sklearn.preprocessing`](https://scikit-learn.org/stable/api/sklearn.preprocessing.html#module-sklearn.preprocessing "sklearn.preprocessing")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-preprocessing "Link to this heading")\
\
*   Enhancement [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")\
     can now handle missing values with the parameter `handle_missing`. By [Stefanie Senger](https://github.com/StefanieSenger)\
    . [#28043](https://github.com/scikit-learn/scikit-learn/pull/28043)\
    \
*   Enhancement The [`preprocessing.PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")\
     now returns a warning when NaN values are encountered in the inverse transform, `inverse_transform`, typically caused by extremely skewed data. By [Roberto Mourao](https://github.com/maf-rnmourao)\
     [#29307](https://github.com/scikit-learn/scikit-learn/pull/29307)\
    \
*   Enhancement [`preprocessing.MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")\
     can now clip out-of-range values in held-out data with the parameter `clip`. By [Hleb Levitski](https://github.com/glevv)\
    . [#31790](https://github.com/scikit-learn/scikit-learn/pull/31790)\
    \
*   Fix Fixed a bug in [`preprocessing.OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")\
     where `handle_unknown='warn'` incorrectly behaved like `'ignore'` instead of `'infrequent_if_exist'`. By [Nithurshen](https://github.com/nithurshen)\
     [#32592](https://github.com/scikit-learn/scikit-learn/pull/32592)\
    \
\
### [`sklearn.semi_supervised`](https://scikit-learn.org/stable/api/sklearn.semi_supervised.html#module-sklearn.semi_supervised "sklearn.semi_supervised")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-semi-supervised "Link to this heading")\
\
*   Fix User written kernel results are now normalized in [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")\
     so all row sums equal 1 even if kernel gives asymmetric or non-uniform row sums. By [Dan Schult](https://github.com/dschult)\
    . [#31924](https://github.com/scikit-learn/scikit-learn/pull/31924)\
    \
\
### [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-tree "Link to this heading")\
\
*   Efficiency [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
     with `criterion="absolute_error"` now runs much faster: O(n log n) complexity against previous O(n^2) allowing to scale to millions of data points, even hundred of millions. By [Arthur Lacote](https://github.com/cakedev0)\
     [#32100](https://github.com/scikit-learn/scikit-learn/pull/32100)\
    \
*   Fix Make [`tree.export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")\
     thread-safe. By [Olivier Grisel](https://github.com/ogrisel)\
    . [#30041](https://github.com/scikit-learn/scikit-learn/pull/30041)\
    \
*   Fix [`export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz")\
     now raises a `ValueError` if given feature names are not all strings. By [Guilherme Peixoto](https://github.com/guilhermecsnpeixoto)\
     [#31036](https://github.com/scikit-learn/scikit-learn/pull/31036)\
    \
*   Fix [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
     with `criterion="absolute_error"` would sometimes make sub-optimal splits (i.e. splits that don’t minimize the absolute error). Now it’s fixed. Hence retraining trees might gives slightly different results. By [Arthur Lacote](https://github.com/cakedev0)\
     [#32100](https://github.com/scikit-learn/scikit-learn/pull/32100)\
    \
*   Fix Fixed a regression in [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree)\
     where almost constant features were not handled properly. By [Sercan Turkmen](https://github.com/sercant)\
    . [#32259](https://github.com/scikit-learn/scikit-learn/pull/32259)\
    \
*   Fix Fixed splitting logic during training in `tree.DecisionTree*` (and consequently in `ensemble.RandomForest*`) for nodes containing near-constant feature values and missing values. Beforehand, trees were cut short if a constant feature was found, even if there was more splitting that could be done on the basis of missing values. By [Arthur Lacote](https://github.com/cakedev0)\
     [#32274](https://github.com/scikit-learn/scikit-learn/pull/32274)\
    \
*   Fix Fix handling of missing values in method `decision_path` of trees ([`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")\
    , [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")\
    , [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")\
     and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")\
    ) By [Arthur Lacote](https://github.com/cakedev0)\
    . [#32280](https://github.com/scikit-learn/scikit-learn/pull/32280)\
    \
*   Fix Fix decision tree splitting with missing values present in some features. In some cases the last non-missing sample would not be partitioned correctly. By [Tim Head](https://github.com/betatim)\
     and [Arthur Lacote](https://github.com/cakedev0)\
    . [#32351](https://github.com/scikit-learn/scikit-learn/pull/32351)\
    \
\
### [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")\
[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-utils "Link to this heading")\
\
*   Efficiency The function [`sklearn.utils.extmath.safe_sparse_dot`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#sklearn.utils.extmath.safe_sparse_dot "sklearn.utils.extmath.safe_sparse_dot")\
     was improved by a dedicated Cython routine for the case of `a @ b` with sparse 2-dimensional `a` and `b` and when a dense output is required, i.e., `dense_output=True`. This improves several algorithms in scikit-learn when dealing with sparse arrays (or matrices). By [Christian Lorentzen](https://github.com/lorentzenchr)\
    . [#31952](https://github.com/scikit-learn/scikit-learn/pull/31952)\
    \
*   Enhancement The parameter table in the HTML representation of all scikit-learn estimators and more generally of estimators inheriting from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")\
     now displays the parameter description as a tooltip and has a link to the online documentation for each parameter. By [Dea María Léon](https://github.com/DeaMariaLeon)\
    . [#31564](https://github.com/scikit-learn/scikit-learn/pull/31564)\
    \
*   Enhancement `sklearn.utils._check_sample_weight` now raises a clearer error message when the provided weights are neither a scalar nor a 1-D array-like of the same size as the input data. By [Kapil Parekh](https://github.com/kapslock123)\
    . [#31873](https://github.com/scikit-learn/scikit-learn/pull/31873)\
    \
*   Enhancement [`sklearn.utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")\
     now lets you configure strict mode for xfailing checks. Tests that unexpectedly pass will lead to a test failure. The default behaviour is unchanged. By [Tim Head](https://github.com/betatim)\
    . [#31951](https://github.com/scikit-learn/scikit-learn/pull/31951)\
    \
*   Enhancement Fixed the alignment of the “?” and “i” symbols and improved the color style of the HTML representation of estimators. By [Guillaume Lemaitre](https://github.com/glemaitre)\
    . [#31969](https://github.com/scikit-learn/scikit-learn/pull/31969)\
    \
*   Fix Changes the way color are chosen when displaying an estimator as an HTML representation. Colors are not adapted anymore to the user’s theme, but chosen based on theme declared color scheme (light or dark) for VSCode and JupyterLab. If theme does not declare a color scheme, scheme is chosen according to default text color of the page, if it fails fallbacks to a media query. By [Matt J.](https://github.com/rouk1)\
    . [#32330](https://github.com/scikit-learn/scikit-learn/pull/32330)\
    \
*   API Change `utils.extmath.stable_cumsum` is deprecated and will be removed in v1.10. Use `np.cumulative_sum` with the desired dtype directly instead. By [Tiziano Zito](https://github.com/opossumnano)\
    . [#32258](https://github.com/scikit-learn/scikit-learn/pull/32258)\
    \
\
Code and documentation contributors\
\
Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.7, including:\
\
$id, 4hm3d, Acciaro Gennaro Daniele, achyuthan.s, Adam J. Stewart, Adriano Leão, Adrien Linares, Adrin Jalali, Aitsaid Azzedine Idir, Alexander Fabisch, Alexandre Abraham, Andrés H. Zapke, Anne Beyer, Anthony Gitter, AnthonyPrudent, antoinebaker, Arpan Mukherjee, Arthur, Arthur Lacote, Arturo Amor, ayoub.agouzoul, Ayrat, Ayush, Ayush Tanwar, Basile Jezequel, Bhavya Patwa, BRYANT MUSI BABILA, Casey Heath, Chems Ben, Christian Lorentzen, Christian Veenhuis, Christine P. Chai, cstec, C. Titus Brown, Daniel Herrera-Esposito, Dan Schult, dbXD320, Dea María Léon, Deepyaman Datta, dependabot\[bot\], Dhyey Findoriya, Dimitri Papadopoulos Orfanos, Dipak Dhangar, Dmitry Kobak, elenafillo, Elham Babaei, EmilyXinyi, Emily (Xinyi) Chen, Eugen-Bleck, Evgeni Burovski, fabarca, Fabrizio Damicelli, Faizan-Ul Huda, François Goupil, François Paugam, Gaetan, GaetandeCast, Gesa Loof, Gonçalo Guiomar, Gordon Grey, Gowtham Kumar K., Guilherme Peixoto, Guillaume Lemaitre, hakan çanakçı, Harshil Sanghvi, Henri Bonamy, Hleb Levitski, HulusiOzy, hvtruong, Ian Faust, Imad Saddik, Jérémie du Boisberranger, Jérôme Dockès, John Hendricks, Joris Van den Bossche, Josef Affourtit, Josh, jshn9515, Junaid, KALLA GANASEKHAR, Kapil Parekh, Kenneth Enevoldsen, Kian Eliasi, kostayScr, Krishnan Vignesh, kryggird, Kyle S, Lakshmi Krishnan, Leomax, Loic Esteve, Luca Bittarello, Lucas Colley, Lucy Liu, Luigi Giugliano, Luis, Mahdi Abid, Mahi Dhiman, Maitrey Talware, Mamduh Zabidi, Manikandan Gobalakrishnan, Marc Bresson, Marco Edward Gorelli, Marek Pokropiński, Maren Westermann, Marie Sacksick, Marija Vlajic, Matt J., Mayank Raj, Michael Burkhart, Michael Šimáček, Miguel Fernandes, Miro Hrončok, Mohamed DHIFALLAH, Muhammad Waseem, MUHAMMED SINAN D, Natalia Mokeeva, Nicholas Farr, Nicolas Bolle, Nicolas Hug, nithish-74, Nithurshen, Nitin Pratap Singh, NotAceNinja, Olivier Grisel, omahs, Omar Salman, Patrick Walsh, Peter Holzer, pfolch, ph-ll-pp, Prashant Bansal, Quan H. Nguyen, Radovenchyk, Rafael Ayllón Gavilán, Raghvender, Ranjodh Singh, Ravichandranayakar, Remi Gau, Reshama Shaikh, Richard Harris, RishiP2006, Ritvi Alagusankar, Roberto Mourao, Robert Pollak, Roshangoli, roychan, R Sagar Shresti, Sarthak Puri, saskra, scikit-learn-bot, Scott Huberty, Sercan Turkmen, Sergio P, Shashank S, Shaurya Bisht, Shivam, Shruti Nath, SIKAI ZHANG, sisird864, SiyuJin-1, S. M. Mohiuddin Khan Shiam, Somdutta Banerjee, sotagg, Sota Goto, Spencer Bradkin, Stefan, Stefanie Senger, Steffen Rehberg, Steven Hur, Success Moses, Sylvain Combettes, ThibaultDECO, Thomas J. Fan, Thomas Li, Thomas S., Tim Head, Tingwei Zhu, Tiziano Zito, TJ Norred, Username46786, Utsab Dahal, Vasanth K, Veghit, VirenPassi, Virgil Chan, Vivaan Nanavati, Xiao Yuan, xuzhang0327, Yaroslav Halchenko, Yaswanth Kumar, Zijun yi, zodchi94, Zubair Shakoor\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)