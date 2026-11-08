[Skip to main content](https://scikit-learn.org/stable/modules/permutation_importance.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/permutation_importance.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/permutation_importance.html)
[1.8.0](https://scikit-learn.org/1.8/modules/permutation_importance.html)
[1.7.2](https://scikit-learn.org/1.7/modules/permutation_importance.html)
[1.6.1](https://scikit-learn.org/1.6/modules/permutation_importance.html)
[1.5.2](https://scikit-learn.org/1.5/modules/permutation_importance.html)
[1.4.2](https://scikit-learn.org/1.4/modules/permutation_importance.html)

Collapse Sidebar Expand Sidebar

5.2. Permutation feature importance[#](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-feature-importance "Link to this heading")

==================================================================================================================================================================

Permutation feature importance is a model inspection technique that measures the contribution of each feature to a [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted)
 model’s statistical performance on a given tabular dataset. This technique is particularly useful for non-linear or opaque [estimators](https://scikit-learn.org/stable/glossary.html#term-estimators)
, and involves randomly shuffling the values of a single feature and observing the resulting degradation of the model’s score [\[1\]](https://scikit-learn.org/stable/modules/permutation_importance.html#id2)
. By breaking the relationship between the feature and the target, we determine how much the model relies on such particular feature.

In the following figures, we observe the effect of permuting features on the correlation between the feature and the target and consequently on the model’s statistical performance.

![../_images/permuted_predictive_feature.png](https://scikit-learn.org/stable/_images/permuted_predictive_feature.png) ![../_images/permuted_non_predictive_feature.png](https://scikit-learn.org/stable/_images/permuted_non_predictive_feature.png)

On the top figure, we observe that permuting a predictive feature breaks the correlation between the feature and the target, and consequently the model’s statistical performance decreases. On the bottom figure, we observe that permuting a non-predictive feature does not significantly degrade the model’s statistical performance.

One key advantage of permutation feature importance is that it is model-agnostic, i.e. it can be applied to any fitted estimator. Moreover, it can be calculated multiple times with different permutations of the feature, further providing a measure of the variance in the estimated feature importances for the specific trained model.

The figure below shows the permutation feature importance of a [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 trained on an augmented version of the titanic dataset that contains a `random_cat` and a `random_num` features, i.e. a categorical and a numerical feature that are not correlated in any way with the target variable:

[![../_images/sphx_glr_plot_permutation_importance_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_002.png)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)

Warning

Features that are deemed of **low importance for a bad model** (low cross-validation score) could be **very important for a good model**. Therefore it is always important to evaluate the predictive power of a model using a held-out set (or better with cross-validation) prior to computing importances. Permutation importance does not reflect the intrinsic predictive value of a feature by itself but **how important this feature is for a particular model**.

The [`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
 function calculates the feature importance of [estimators](https://scikit-learn.org/stable/glossary.html#term-estimators)
 for a given dataset. The `n_repeats` parameter sets the number of times a feature is randomly shuffled and returns a sample of feature importances.

Let’s consider the following trained regression model:

\>>> from sklearn.datasets import load\_diabetes
\>>> from sklearn.model\_selection import train\_test\_split
\>>> from sklearn.linear\_model import Ridge
\>>> diabetes \= load\_diabetes()
\>>> X\_train, X\_val, y\_train, y\_val \= train\_test\_split(
...     diabetes.data, diabetes.target, random\_state\=0)
...
\>>> model \= Ridge(alpha\=1e-2).fit(X\_train, y\_train)
\>>> model.score(X\_val, y\_val)
0.356...

Copy to clipboard

Its validation performance, measured via the R2 score, is significantly larger than the chance level. This makes it possible to use the [`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
 function to probe which features are most predictive:

\>>> from sklearn.inspection import permutation\_importance
\>>> r \= permutation\_importance(model, X\_val, y\_val,
...                            n\_repeats\=30,
...                            random\_state\=0)
...
\>>> for i in r.importances\_mean.argsort()\[::\-1\]:
...     if r.importances\_mean\[i\] \- 2 \* r.importances\_std\[i\] \> 0:
...         print(f"{diabetes.feature\_names\[i\]:<8}"
...               f"{r.importances\_mean\[i\]:.3f}"
...               f" +/- {r.importances\_std\[i\]:.3f}")
...
s5      0.204 +/- 0.050
bmi     0.176 +/- 0.048
bp      0.088 +/- 0.033
sex     0.056 +/- 0.023

Copy to clipboard

Note that the importance values for the top features represent a large fraction of the reference score of 0.356.

Permutation importances can be computed either on the training set or on a held-out testing or validation set. Using a held-out set makes it possible to highlight which features contribute the most to the generalization power of the inspected model. Features that are important on the training set but not on the held-out set might cause the model to overfit.

The permutation feature importance depends on the score function that is specified with the `scoring` argument. This argument accepts multiple scorers, which is more computationally efficient than sequentially calling [`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")
 several times with a different scorer, as it reuses model predictions.

Example of permutation feature importance using multiple scorers[#](https://scikit-learn.org/stable/modules/permutation_importance.html#example-of-permutation-feature-importance-using-multiple-scorers "Link to this dropdown")

In the example below we use a list of metrics, but more input formats are possible, as documented in [Using multiple metric evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html#multimetric-scoring)
.

\>>> scoring \= \['r2', 'neg\_mean\_absolute\_percentage\_error', 'neg\_mean\_squared\_error'\]
\>>> r\_multi \= permutation\_importance(
...     model, X\_val, y\_val, n\_repeats\=30, random\_state\=0, scoring\=scoring)
...
\>>> for metric in r\_multi:
...     print(f"{metric}")
...     r \= r\_multi\[metric\]
...     for i in r.importances\_mean.argsort()\[::\-1\]:
...         if r.importances\_mean\[i\] \- 2 \* r.importances\_std\[i\] \> 0:
...             print(f"    {diabetes.feature\_names\[i\]:<8}"
...                   f"{r.importances\_mean\[i\]:.3f}"
...                   f" +/- {r.importances\_std\[i\]:.3f}")
...
r2
    s5      0.204 +/- 0.050
    bmi     0.176 +/- 0.048
    bp      0.088 +/- 0.033
    sex     0.056 +/- 0.023
neg\_mean\_absolute\_percentage\_error
    s5      0.081 +/- 0.020
    bmi     0.064 +/- 0.015
    bp      0.029 +/- 0.010
neg\_mean\_squared\_error
    s5      1013.866 +/- 246.445
    bmi     872.726 +/- 240.298
    bp      438.663 +/- 163.022
    sex     277.376 +/- 115.123

Copy to clipboard

The ranking of the features is approximately the same for different metrics even if the scales of the importance values are very different. However, this is not guaranteed and different metrics might lead to significantly different feature importances, in particular for models trained for imbalanced classification problems, for which **the choice of the classification metric can be critical**.

5.2.1. Outline of the permutation importance algorithm[#](https://scikit-learn.org/stable/modules/permutation_importance.html#outline-of-the-permutation-importance-algorithm "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Inputs: fitted predictive model m, tabular dataset (training or validation) D.
    
*   Compute the reference score s of the model m on data D (for instance the accuracy for a classifier or the R2 for a regressor).
    
*   For each feature j (column of D):
    
    *   For each repetition k in 1,...,K:
        
        *   Randomly shuffle column j of dataset D to generate a corrupted version of the data named D~k,j.
            
        *   Compute the score sk,j of model m on corrupted data D~k,j.
            
    *   Compute importance ij for feature fj defined as:
        
        ij\=s−1K∑k\=1Ksk,j
        

5.2.2. Relation to impurity-based importance in trees[#](https://scikit-learn.org/stable/modules/permutation_importance.html#relation-to-impurity-based-importance-in-trees "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tree-based models provide an alternative measure of [feature importances based on the mean decrease in impurity](https://scikit-learn.org/stable/modules/ensemble.html#random-forest-feature-importance)
 (MDI). Impurity is quantified by the splitting criterion of the decision trees (Gini, Log Loss or Mean Squared Error). However, this method can give high importance to features that may not be predictive on unseen data when the model is overfitting. Permutation-based feature importance, on the other hand, avoids this issue, since it can be computed on unseen data.

Furthermore, impurity-based feature importance for trees is **strongly biased** and **favor high cardinality features** (typically numerical features) over low cardinality features such as binary features or categorical variables with a small number of possible categories.

Permutation-based feature importances do not exhibit such a bias. Additionally, the permutation feature importance may be computed with any performance metric on the model predictions and can be used to analyze any model class (not just tree-based models).

The following example highlights the limitations of impurity-based feature importance in contrast to permutation-based feature importance: [Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py)
.

5.2.3. Misleading values on strongly correlated features[#](https://scikit-learn.org/stable/modules/permutation_importance.html#misleading-values-on-strongly-correlated-features "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When two features are correlated and one of the features is permuted, the model still has access to the latter through its correlated feature. This results in a lower reported importance value for both features, though they might _actually_ be important.

The figure below shows the permutation feature importance of a [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
 trained using the [Breast cancer Wisconsin (diagnostic) dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset)
, which contains strongly correlated features. A naive interpretation would suggest that all features are unimportant:

[![../_images/sphx_glr_plot_permutation_importance_multicollinear_002.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_002.png)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

One way to handle the issue is to cluster features that are correlated and only keep one feature from each cluster.

[![../_images/sphx_glr_plot_permutation_importance_multicollinear_004.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_004.png)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)

For more details on such strategy, see the example [Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-multicollinear-py)
.

Examples

*   [Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py)
    
*   [Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-multicollinear-py)
    

References

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)