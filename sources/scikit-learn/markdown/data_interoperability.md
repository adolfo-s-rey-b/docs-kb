[Skip to main content](https://scikit-learn.org/stable/data_interoperability.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/data_interoperability.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/data_interoperability.html)
[1.8.0](https://scikit-learn.org/1.8/data_interoperability.html)
[1.7.2](https://scikit-learn.org/1.7/data_interoperability.html)
[1.6.1](https://scikit-learn.org/1.6/data_interoperability.html)
[1.5.2](https://scikit-learn.org/1.5/data_interoperability.html)
[1.4.2](https://scikit-learn.org/1.4/data_interoperability.html)

Collapse Sidebar Expand Sidebar

13\. Data Interoperability[#](https://scikit-learn.org/stable/data_interoperability.html#data-interoperability "Link to this heading")

=======================================================================================================================================

Scikit-learn handles four kinds of data for [X](https://scikit-learn.org/stable/glossary.html#term-X)
 as used in `fit(X, y)`, `fit(X)`, `fit_transform(X)` and `transform(X)` as well as [Xt](https://scikit-learn.org/stable/glossary.html#term-Xt)
 as returned by `transform(X)` and `fit_transform(X)`:

*   [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like)
     objects
    
    In `fit(X)` and `transform(X)`, array-like `X` is converted to a numpy ndarray by calling `numpy.asarray` upon them. The returned `Xt` of `transform` and `fit_transform` is also a numpy ndarray or it is a sparse matrix or sparse array, see next bullet.
    
*   [sparse matrices](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix)
     and sparse arrays
    
    Many estimators can deal with sparse `X`, some cannot and will raise an error. For instance, [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
     can be fit on sparse `X`, [`isotonic.IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")
     can not.
    
    Some transformers return sparse `Xt` from `transform` and `fit_transform`. Most often, it can be controlled by a `sparse_output` parameter as in [`preprocessing.SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
    .
    
    To control whether it returns a sparse matrix or a sparse array, use `sparse_interface` in [`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context")
     or [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")
    . This also controls whether sparse attributes are sparse matrices or sparse arrays.
    
*   tabular data: pandas and polars dataframes
    
    See [Pandas/Polars Output for Transformers with set\_output API](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
    .
    
*   Array API compliant arrays
    
    Very importantly, this includes arrays on the GPU, see [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api)
    .
    

*   [13.1. Pandas/Polars Output for Transformers with `set_output` API](https://scikit-learn.org/stable/modules/df_output_transform.html)
    *   [13.1.1. Propagation of Feature Names](https://scikit-learn.org/stable/modules/df_output_transform.html#propagation-of-feature-names)
        
    *   [13.1.2. Introducing the `set_output` API](https://scikit-learn.org/stable/modules/df_output_transform.html#introducing-the-set-output-api)
        
*   [13.2. Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html)
    *   [13.2.1. Supported array libraries](https://scikit-learn.org/stable/modules/array_api.html#supported-array-libraries)
        
    *   [13.2.2. Enabling array API support](https://scikit-learn.org/stable/modules/array_api.html#enabling-array-api-support)
        
    *   [13.2.3. Example usage](https://scikit-learn.org/stable/modules/array_api.html#example-usage)
        
    *   [13.2.4. Support for array API compatible inputs](https://scikit-learn.org/stable/modules/array_api.html#support-for-array-api-compatible-inputs)
        
    *   [13.2.5. Input and output array type handling](https://scikit-learn.org/stable/modules/array_api.html#input-and-output-array-type-handling)
        
    *   [13.2.6. Common estimator checks (for developers)](https://scikit-learn.org/stable/modules/array_api.html#common-estimator-checks-for-developers)
        
    *   [13.2.7. Notes](https://scikit-learn.org/stable/modules/array_api.html#notes)
        

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)