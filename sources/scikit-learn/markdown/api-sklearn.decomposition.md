[Skip to main content](https://scikit-learn.org/stable/api/sklearn.decomposition.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.decomposition.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.decomposition.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.decomposition.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.decomposition.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.decomposition.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.decomposition.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.decomposition.html)

Collapse Sidebar Expand Sidebar

sklearn.decomposition[#](https://scikit-learn.org/stable/api/sklearn.decomposition.html#module-sklearn.decomposition "Link to this heading")

=============================================================================================================================================

Matrix decomposition algorithms.

These include PCA, NMF, ICA, and more. Most of the algorithms of this module can be regarded as dimensionality reduction techniques.

**User guide.** See the [Decomposing signals in components (matrix factorization problems)](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
 section for further details.

|     |     |
| --- | --- |
| [`DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning") | Dictionary learning. |
| [`FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis") | Factor Analysis (FA). |
| [`FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA") | FastICA: a fast algorithm for Independent Component Analysis. |
| [`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA") | Incremental principal components analysis (IPCA). |
| [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA") | Kernel Principal component analysis (KPCA). |
| [`LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation") | Latent Dirichlet Allocation with online variational Bayes algorithm. |
| [`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning") | Mini-batch dictionary learning. |
| [`MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF") | Mini-Batch Non-Negative Matrix Factorization (NMF). |
| [`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA") | Mini-batch Sparse Principal Components Analysis. |
| [`NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF") | Non-Negative Matrix Factorization (NMF). |
| [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA") | Principal component analysis (PCA). |
| [`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder") | Sparse coding. |
| [`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA") | Sparse Principal Components Analysis (SparsePCA). |
| [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD") | Dimensionality reduction using truncated SVD (aka LSA). |
| [`dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning") | Solve a dictionary learning matrix factorization problem. |
| [`dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online") | Solve a dictionary learning matrix factorization problem online. |
| [`fastica`](https://scikit-learn.org/stable/modules/generated/fastica-function.html#sklearn.decomposition.fastica "sklearn.decomposition.fastica") | Perform Fast Independent Component Analysis. |
| [`non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization") | Compute Non-negative Matrix Factorization (NMF). |
| [`sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode") | Sparse coding. |