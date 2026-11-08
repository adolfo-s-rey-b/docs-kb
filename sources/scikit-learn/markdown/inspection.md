[Skip to main content](https://scikit-learn.org/stable/inspection.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/inspection.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/inspection.html)
[1.8.0](https://scikit-learn.org/1.8/inspection.html)
[1.7.2](https://scikit-learn.org/1.7/inspection.html)
[1.6.1](https://scikit-learn.org/1.6/inspection.html)
[1.5.2](https://scikit-learn.org/1.5/inspection.html)
[1.4.2](https://scikit-learn.org/1.4/inspection.html)

Collapse Sidebar Expand Sidebar

5\. Inspection[#](https://scikit-learn.org/stable/inspection.html#inspection "Link to this heading")

=====================================================================================================

Predictive performance is often the main goal of developing machine learning models. Yet summarizing performance with an evaluation metric is often insufficient: it assumes that the evaluation metric and test dataset perfectly reflect the target domain, which is rarely true. In certain domains, a model needs a certain level of interpretability before it can be deployed. A model that is exhibiting performance issues needs to be debugged for one to understand the model’s underlying issue. The [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")
 module provides tools to help understand the predictions from a model and what affects them. This can be used to evaluate assumptions and biases of a model, design a better model, or to diagnose issues with model performance.

Examples

*   [Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#sphx-glr-auto-examples-inspection-plot-linear-model-coefficient-interpretation-py)
    

*   [5.1. Partial Dependence and Individual Conditional Expectation plots](https://scikit-learn.org/stable/modules/partial_dependence.html)
    *   [5.1.1. Partial dependence plots](https://scikit-learn.org/stable/modules/partial_dependence.html#partial-dependence-plots)
        
    *   [5.1.2. Individual conditional expectation (ICE) plot](https://scikit-learn.org/stable/modules/partial_dependence.html#individual-conditional-expectation-ice-plot)
        
    *   [5.1.3. Mathematical Definition](https://scikit-learn.org/stable/modules/partial_dependence.html#mathematical-definition)
        
    *   [5.1.4. Computation methods](https://scikit-learn.org/stable/modules/partial_dependence.html#computation-methods)
        
*   [5.2. Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html)
    *   [5.2.1. Outline of the permutation importance algorithm](https://scikit-learn.org/stable/modules/permutation_importance.html#outline-of-the-permutation-importance-algorithm)
        
    *   [5.2.2. Relation to impurity-based importance in trees](https://scikit-learn.org/stable/modules/permutation_importance.html#relation-to-impurity-based-importance-in-trees)
        
    *   [5.2.3. Misleading values on strongly correlated features](https://scikit-learn.org/stable/modules/permutation_importance.html#misleading-values-on-strongly-correlated-features)
        

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)