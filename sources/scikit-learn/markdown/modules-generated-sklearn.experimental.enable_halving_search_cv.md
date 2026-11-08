[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.experimental.enable_halving_search_cv.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.experimental.enable_halving_search_cv.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.experimental.enable_halving_search_cv.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.experimental.enable_halving_search_cv.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.experimental.enable_halving_search_cv.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.experimental.enable_halving_search_cv.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.experimental.enable_halving_search_cv.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.experimental.enable_halving_search_cv.html)

Collapse Sidebar Expand Sidebar

enable\_halving\_search\_cv[#](https://scikit-learn.org/stable/modules/generated/sklearn.experimental.enable_halving_search_cv.html#module-sklearn.experimental.enable_halving_search_cv "Link to this heading")

=================================================================================================================================================================================================================

Enables Successive Halving search-estimators

The API and results of these estimators might change without any deprecation cycle.

Importing this file dynamically sets the [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV")
 and [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")
 as attributes of the `model_selection` module:

\>>> \# explicitly require this experimental feature
\>>> from sklearn.experimental import enable\_halving\_search\_cv \# noqa
\>>> \# now you can import normally from model\_selection
\>>> from sklearn.model\_selection import HalvingRandomSearchCV
\>>> from sklearn.model\_selection import HalvingGridSearchCV

Copy to clipboard

The `# noqa` comment comment can be removed: it just tells linters like flake8 to ignore the import, which appears as unused.

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)