[Skip to main content](https://scikit-learn.org/stable/modules/df_output_transform.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/df_output_transform.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/df_output_transform.html)
[1.8.0](https://scikit-learn.org/1.8/modules/df_output_transform.html)
[1.7.2](https://scikit-learn.org/1.7/modules/df_output_transform.html)
[1.6.1](https://scikit-learn.org/1.6/modules/df_output_transform.html)
[1.5.2](https://scikit-learn.org/1.5/modules/df_output_transform.html)
[1.4.2](https://scikit-learn.org/1.4/modules/df_output_transform.html)

Collapse Sidebar Expand Sidebar

13.1. Pandas/Polars Output for Transformers with `set_output` API[#](https://scikit-learn.org/stable/modules/df_output_transform.html#pandas-polars-output-for-transformers-with-set-output-api "Link to this heading")

========================================================================================================================================================================================================================

This part of the user guide explains how scikit-learn supports tabular data.

13.1.1. Propagation of Feature Names[#](https://scikit-learn.org/stable/modules/df_output_transform.html#propagation-of-feature-names "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, scikit-learn [transformers](https://scikit-learn.org/stable/glossary.html#term-transformers)
 (estimators with a `transform` method) return numpy arrays (sometimes also sparse arrays). Because numpy arrays do not provide names for the indices of axes/dimensions, prior to version 1.0 the [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
 did not know how to propagate feature names:

*   The single step estimators did not know how to handle incoming feature names.
    
*   The pipeline did not know how to pass feature names from step to step.
    

In practice, a lot of use cases start with tabular data like a [pandas dataframe](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)
 or a [polars dataframe](https://docs.pola.rs/api/python/stable/reference/dataframe/index.html)
 which have column/feature names.

A first step to support this important use case was made by the addition of the [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 in [version 0.20](https://scikit-learn.org/stable/whats_new/v0.20.html#changes-0-20)
. It acts as a gateway to apply different estimators on the different features. Most notably it understands incoming feature names.

It was then properly solved by [SLEP007: Feature names, their generation and the API](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep007/proposal.html)
 and fully implemented in [version 1.1](https://scikit-learn.org/stable/whats_new/v1.1.html#release-notes-1-1)
, see the [release highlights 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html#feature-names-in-release-highlights-1-0-0)
 and [release highlights 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html#get-feature-names-out-release-highlights-1-1-0)
. When an estimator is passed a dataframe during [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
, the estimator will set a `feature_names_in_` attribute containing the feature names. It understands pandas dataframes as well as dataframes with the [Python dataframe interchange protocol](https://data-apis.org/dataframe-protocol/latest/index.html)
 `__dataframe__`. Furthermore, fitted estimators have the method `get_feature_names_out`. The `get_feature_names_out` of a transformer returns⸺you guessed it⸺the feature names of what `transform` returns.

13.1.2. Introducing the `set_output` API[#](https://scikit-learn.org/stable/modules/df_output_transform.html#introducing-the-set-output-api "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

A further major step to support dataframes in a “dataframe in, dataframe out” fashion was [SLEP018](https://scikit-learn-enhancement-proposals.readthedocs.io/en/latest/slep018/proposal.html)
, implemented for pandas dataframes in [version 1.2](https://scikit-learn.org/stable/whats_new/v1.2.html#release-notes-1-2)
 and for polars dataframes in [version 1.4](https://scikit-learn.org/stable/whats_new/v1.4.html#release-notes-1-4)
. It introduced the `set_output` API to configure transformers to output pandas or polars DataFrames. The output of transformers can be configured per estimator by calling the `set_output` method or globally, by setting `set_config(transform_output="pandas")`. Set it to `"polars"` instead of `"pandas"` if you want the same thing to happen but with polars DataFrames.

The usage is basically as follows:

\>>> import numpy as np
\>>> import pandas as pd
\>>> from sklearn.compose import ColumnTransformer
\>>> from sklearn.pipeline import make\_pipeline
\>>> from sklearn.preprocessing import OneHotEncoder
\>>> from sklearn.linear\_model import LinearRegression

\>>> X \= pd.DataFrame(
...     {"animals": \["cat", "cat", "dog", "dog"\], "numeric": np.linspace(\-1, 1, 4)}
... )
\>>> y \= np.array(\[\-1.5, 0, 0.1, 1.0\])
\>>> ct \= ColumnTransformer(
...     \[("categorical", OneHotEncoder(sparse\_output\=False), \["animals"\])\],
...     remainder\="passthrough",
... )
\>>> model \= make\_pipeline(ct, LinearRegression()).fit(X, y)
\>>> model.feature\_names\_in\_
array(\['animals', 'numeric'\], dtype=object)
\>>> model\[0\].get\_feature\_names\_out()
array(\['categorical\_\_animals\_cat', 'categorical\_\_animals\_dog',\
   'remainder\_\_numeric'\], dtype=object)
\>>> model\[0\].transform(X)
array(\[\[ 1.        ,  0.        , -1.        \],\
       \[ 1.        ,  0.        , -0.33333333\],\
       \[ 0.        ,  1.        ,  0.33333333\],\
       \[ 0.        ,  1.        ,  1.        \]\])

Copy to clipboard

Now the same, but with pandas set as output:

\>>> from sklearn import set\_config
\>>> set\_config(transform\_output\="pandas")
\>>> model\[0\].transform(X)
       c...

Copy to clipboard

|     | categorical\_\_animals\_cat | categorical\_\_animals\_dog | remainder\_\_numeric |
| --- | --- | --- | --- |
| 0   | 1.0 | 0.0 | \-1.000000 |
| 1   | 1.0 | 0.0 | \-0.333333 |
| 2   | 0.0 | 1.0 | 0.333333 |
| 3   | 0.0 | 1.0 | 1.000000 |

To return to the default, simply run:

\>>> set\_config(transform\_output\="default")

Copy to clipboard

A more detailed example can be found in [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)