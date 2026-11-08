[Skip to main content](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/compose/plot_feature_union.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/compose/plot_feature_union.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/compose/plot_feature_union.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/compose/plot_feature_union.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/compose/plot_feature_union.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/compose/plot_feature_union.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html#sphx-glr-download-auto-examples-compose-plot-feature-union-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Concatenating multiple feature extraction methods[#](https://scikit-learn.org/stable/auto_examples/compose/plot_feature_union.html#concatenating-multiple-feature-extraction-methods "Link to this heading")

=============================================================================================================================================================================================================

In many real-world examples, there are many ways to extract features from a dataset. Often it is beneficial to combine several methods to obtain good performance. This example shows how to use `FeatureUnion` to combine features obtained by PCA and univariate selection.

Combining features using this transformer has the benefit that it allows cross validation and grid searches over the whole process.

The combination used in this example is not particularly helpful on this dataset and is only used to illustrate the usage of FeatureUnion.

Combined space has 3 features
Fitting 5 folds for each of 18 candidates, totalling 90 fits
\[CV 1/5; 1/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 1/5; 1/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 2/5; 1/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 2/5; 1/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 3/5; 1/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 3/5; 1/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.867 total time=   0.0s
\[CV 4/5; 1/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 4/5; 1/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 5/5; 1/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 5/5; 1/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 1/5; 2/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 1/5; 2/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.900 total time=   0.0s
\[CV 2/5; 2/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 2/5; 2/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 3/5; 2/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 3/5; 2/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.867 total time=   0.0s
\[CV 4/5; 2/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 4/5; 2/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 5/5; 2/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 5/5; 2/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 1/5; 3/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 1/5; 3/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 2/5; 3/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 2/5; 3/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 3/5; 3/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 3/5; 3/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.900 total time=   0.0s
\[CV 4/5; 3/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 4/5; 3/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 5/5; 3/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 5/5; 3/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 1/5; 4/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 1/5; 4/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 2/5; 4/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 2/5; 4/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.967 total time=   0.0s
\[CV 3/5; 4/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 3/5; 4/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 4/5; 4/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 4/5; 4/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 5/5; 4/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 5/5; 4/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 1/5; 5/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 1/5; 5/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 2/5; 5/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 2/5; 5/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 3/5; 5/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 3/5; 5/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 4/5; 5/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 4/5; 5/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 5/5; 5/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 5/5; 5/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 1/5; 6/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 1/5; 6/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 2/5; 6/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 2/5; 6/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 3/5; 6/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 3/5; 6/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 4/5; 6/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 4/5; 6/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 5/5; 6/18\] START features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 5/5; 6/18\] END features\_\_pca\_\_n\_components=1, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 1/5; 7/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 1/5; 7/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 2/5; 7/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 2/5; 7/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 3/5; 7/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 3/5; 7/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.867 total time=   0.0s
\[CV 4/5; 7/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 4/5; 7/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 5/5; 7/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 5/5; 7/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 1/5; 8/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 1/5; 8/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 2/5; 8/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 2/5; 8/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 3/5; 8/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 3/5; 8/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 4/5; 8/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 4/5; 8/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 5/5; 8/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 5/5; 8/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 1/5; 9/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 1/5; 9/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 2/5; 9/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 2/5; 9/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 3/5; 9/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 3/5; 9/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.900 total time=   0.0s
\[CV 4/5; 9/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 4/5; 9/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 5/5; 9/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 5/5; 9/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 1/5; 10/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 1/5; 10/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.967 total time=   0.0s
\[CV 2/5; 10/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 2/5; 10/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 3/5; 10/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 3/5; 10/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 4/5; 10/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 4/5; 10/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 5/5; 10/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 5/5; 10/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 1/5; 11/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 1/5; 11/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 2/5; 11/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 2/5; 11/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 3/5; 11/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 3/5; 11/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 4/5; 11/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 4/5; 11/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 5/5; 11/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 5/5; 11/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 1/5; 12/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 1/5; 12/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 2/5; 12/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 2/5; 12/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 3/5; 12/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 3/5; 12/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.900 total time=   0.0s
\[CV 4/5; 12/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 4/5; 12/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 5/5; 12/18\] START features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 5/5; 12/18\] END features\_\_pca\_\_n\_components=2, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 1/5; 13/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 1/5; 13/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.967 total time=   0.0s
\[CV 2/5; 13/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 2/5; 13/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 3/5; 13/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 3/5; 13/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 4/5; 13/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 4/5; 13/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=0.967 total time=   0.0s
\[CV 5/5; 13/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1
\[CV 5/5; 13/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 1/5; 14/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 1/5; 14/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 2/5; 14/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 2/5; 14/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 3/5; 14/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 3/5; 14/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.933 total time=   0.0s
\[CV 4/5; 14/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 4/5; 14/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 5/5; 14/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1
\[CV 5/5; 14/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 1/5; 15/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 1/5; 15/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 2/5; 15/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 2/5; 15/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 3/5; 15/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 3/5; 15/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.933 total time=   0.0s
\[CV 4/5; 15/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 4/5; 15/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 5/5; 15/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10
\[CV 5/5; 15/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=1, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 1/5; 16/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 1/5; 16/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.967 total time=   0.0s
\[CV 2/5; 16/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 2/5; 16/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 3/5; 16/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 3/5; 16/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.933 total time=   0.0s
\[CV 4/5; 16/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 4/5; 16/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=0.967 total time=   0.0s
\[CV 5/5; 16/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1
\[CV 5/5; 16/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=0.1;, score=1.000 total time=   0.0s
\[CV 1/5; 17/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 1/5; 17/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 2/5; 17/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 2/5; 17/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 3/5; 17/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 3/5; 17/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 4/5; 17/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 4/5; 17/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=0.967 total time=   0.0s
\[CV 5/5; 17/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1
\[CV 5/5; 17/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=1;, score=1.000 total time=   0.0s
\[CV 1/5; 18/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 1/5; 18/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 2/5; 18/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 2/5; 18/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=1.000 total time=   0.0s
\[CV 3/5; 18/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 3/5; 18/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.900 total time=   0.0s
\[CV 4/5; 18/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 4/5; 18/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=0.967 total time=   0.0s
\[CV 5/5; 18/18\] START features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10
\[CV 5/5; 18/18\] END features\_\_pca\_\_n\_components=3, features\_\_univ\_select\_\_k=2, svm\_\_C=10;, score=1.000 total time=   0.0s
Pipeline(steps=\[('features',\
                 FeatureUnion(transformer\_list=\[('pca', PCA(n\_components=3)),\
                                                ('univ\_select',\
                                                 SelectKBest(k=1))\])),\
                ('svm', SVC(C=10, kernel='linear'))\])

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.feature\_selection import [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
from sklearn.pipeline import [FeatureUnion](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
, [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()

X, y \= iris.data, iris.target

\# This dataset is way too high-dimensional. Better do PCA:
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2)

\# Maybe some original features were good, too?
selection \= [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")
(k\=1)

\# Build estimator from PCA and Univariate selection:

combined\_features \= [FeatureUnion](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")
(\[("pca", pca), ("univ\_select", selection)\])

\# Use combined features to transform dataset:
X\_features \= combined\_features.fit(X, y).transform(X)
print("Combined space has", X\_features.shape\[1\], "features")

svm \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\="linear")

\# Do grid search over k, n\_components and C:

pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(\[("features", combined\_features), ("svm", svm)\])

param\_grid \= dict(
    features\_\_pca\_\_n\_components\=\[1, 2, 3\],
    features\_\_univ\_select\_\_k\=\[1, 2\],
    svm\_\_C\=\[0.1, 1, 10\],
)

grid\_search \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
(pipeline, param\_grid\=param\_grid, verbose\=10)
grid\_search.fit(X, y)
print(grid\_search.best\_estimator\_)

Copy to clipboard

**Total running time of the script:** (0 minutes 0.546 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_feature_union.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_feature_union.ipynb)

[`Download Jupyter notebook: plot_feature_union.ipynb`](https://scikit-learn.org/stable/_downloads/1273a3baa87138f2b817bfc78fe7ecb4/plot_feature_union.ipynb)

[`Download Python source code: plot_feature_union.py`](https://scikit-learn.org/stable/_downloads/01fdc7c95204e4a420de7cd297711693/plot_feature_union.py)

[`Download zipped: plot_feature_union.zip`](https://scikit-learn.org/stable/_downloads/35ddd809a204588ba5e0d93a2ac44682/plot_feature_union.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_selection_thumb.png)

[Univariate Feature Selection](https://scikit-learn.org/stable/auto_examples/feature_selection/plot_feature_selection.html)

Univariate Feature Selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/01fdc7c95204e4a420de7cd297711693/plot_feature_union.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/1273a3baa87138f2b817bfc78fe7ecb4/plot_feature_union.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/35ddd809a204588ba5e0d93a2ac44682/plot_feature_union.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_feature_union.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_feature_union.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)