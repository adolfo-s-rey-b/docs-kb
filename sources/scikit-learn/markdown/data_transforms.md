[Skip to main content](https://scikit-learn.org/stable/data_transforms.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/data_transforms.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/data_transforms.html)
[1.8.0](https://scikit-learn.org/1.8/data_transforms.html)
[1.7.2](https://scikit-learn.org/1.7/data_transforms.html)
[1.6.1](https://scikit-learn.org/1.6/data_transforms.html)
[1.5.2](https://scikit-learn.org/1.5/data_transforms.html)
[1.4.2](https://scikit-learn.org/1.4/data_transforms.html)

Collapse Sidebar Expand Sidebar

8\. Dataset transformations[#](https://scikit-learn.org/stable/data_transforms.html#dataset-transformations "Link to this heading")

====================================================================================================================================

scikit-learn provides a library of transformers, which may clean (see [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
), reduce (see [Unsupervised dimensionality reduction](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#data-reduction)
), expand (see [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)
) or generate (see [Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction)
) feature representations.

Like other estimators, these are represented by classes with a `fit` method, which learns model parameters (e.g. mean and standard deviation for normalization) from a training set, and a `transform` method which applies this transformation model to unseen data. `fit_transform` may be more convenient and efficient for modelling and transforming the training data simultaneously.

Combining such transformers, either in parallel or series is covered in [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html#combining-estimators)
. [Pairwise metrics, Affinities and Kernels](https://scikit-learn.org/stable/modules/metrics.html#metrics)
 covers transforming feature spaces into affinity matrices, while [Transforming the prediction target (y)](https://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
 considers transformations of the target space (e.g. categorical labels) for use in scikit-learn.

*   [8.1. Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html)
    *   [8.1.1. Pipeline: chaining estimators](https://scikit-learn.org/stable/modules/compose.html#pipeline-chaining-estimators)
        
    *   [8.1.2. Transforming target in regression](https://scikit-learn.org/stable/modules/compose.html#transforming-target-in-regression)
        
    *   [8.1.3. FeatureUnion: composite feature spaces](https://scikit-learn.org/stable/modules/compose.html#featureunion-composite-feature-spaces)
        
    *   [8.1.4. ColumnTransformer for heterogeneous data](https://scikit-learn.org/stable/modules/compose.html#columntransformer-for-heterogeneous-data)
        
    *   [8.1.5. Visualizing Composite Estimators](https://scikit-learn.org/stable/modules/compose.html#visualizing-composite-estimators)
        
*   [8.2. Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html)
    *   [8.2.1. Loading features from dicts](https://scikit-learn.org/stable/modules/feature_extraction.html#loading-features-from-dicts)
        
    *   [8.2.2. Feature hashing](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-hashing)
        
    *   [8.2.3. Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
        
    *   [8.2.4. Image feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#image-feature-extraction)
        
*   [8.3. Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)
    *   [8.3.1. Standardization, or mean removal and variance scaling](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling)
        
    *   [8.3.2. Non-linear transformation](https://scikit-learn.org/stable/modules/preprocessing.html#non-linear-transformation)
        
    *   [8.3.3. Normalization](https://scikit-learn.org/stable/modules/preprocessing.html#normalization)
        
    *   [8.3.4. Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features)
        
    *   [8.3.5. Discretization](https://scikit-learn.org/stable/modules/preprocessing.html#discretization)
        
    *   [8.3.6. Imputation of missing values](https://scikit-learn.org/stable/modules/preprocessing.html#imputation-of-missing-values)
        
    *   [8.3.7. Generating polynomial features](https://scikit-learn.org/stable/modules/preprocessing.html#generating-polynomial-features)
        
    *   [8.3.8. Custom transformers](https://scikit-learn.org/stable/modules/preprocessing.html#custom-transformers)
        
*   [8.4. Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html)
    *   [8.4.1. Univariate vs. Multivariate Imputation](https://scikit-learn.org/stable/modules/impute.html#univariate-vs-multivariate-imputation)
        
    *   [8.4.2. Univariate feature imputation](https://scikit-learn.org/stable/modules/impute.html#univariate-feature-imputation)
        
    *   [8.4.3. Multivariate feature imputation](https://scikit-learn.org/stable/modules/impute.html#multivariate-feature-imputation)
        
    *   [8.4.4. Nearest neighbors imputation](https://scikit-learn.org/stable/modules/impute.html#nearest-neighbors-imputation)
        
    *   [8.4.5. Keeping the number of features constant](https://scikit-learn.org/stable/modules/impute.html#keeping-the-number-of-features-constant)
        
    *   [8.4.6. Marking imputed values](https://scikit-learn.org/stable/modules/impute.html#marking-imputed-values)
        
    *   [8.4.7. Estimators that handle NaN values](https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values)
        
*   [8.5. Unsupervised dimensionality reduction](https://scikit-learn.org/stable/modules/unsupervised_reduction.html)
    *   [8.5.1. PCA: principal component analysis](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#pca-principal-component-analysis)
        
    *   [8.5.2. Random projections](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#random-projections)
        
    *   [8.5.3. Feature agglomeration](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#feature-agglomeration)
        
*   [8.6. Random Projection](https://scikit-learn.org/stable/modules/random_projection.html)
    *   [8.6.1. The Johnson-Lindenstrauss lemma](https://scikit-learn.org/stable/modules/random_projection.html#the-johnson-lindenstrauss-lemma)
        
    *   [8.6.2. Gaussian random projection](https://scikit-learn.org/stable/modules/random_projection.html#gaussian-random-projection)
        
    *   [8.6.3. Sparse random projection](https://scikit-learn.org/stable/modules/random_projection.html#sparse-random-projection)
        
    *   [8.6.4. Inverse Transform](https://scikit-learn.org/stable/modules/random_projection.html#inverse-transform)
        
*   [8.7. Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html)
    *   [8.7.1. Nystroem Method for Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#nystroem-method-for-kernel-approximation)
        
    *   [8.7.2. Radial Basis Function Kernel](https://scikit-learn.org/stable/modules/kernel_approximation.html#radial-basis-function-kernel)
        
    *   [8.7.3. Additive Chi Squared Kernel](https://scikit-learn.org/stable/modules/kernel_approximation.html#additive-chi-squared-kernel)
        
    *   [8.7.4. Skewed Chi Squared Kernel](https://scikit-learn.org/stable/modules/kernel_approximation.html#skewed-chi-squared-kernel)
        
    *   [8.7.5. Polynomial Kernel Approximation via Tensor Sketch](https://scikit-learn.org/stable/modules/kernel_approximation.html#polynomial-kernel-approximation-via-tensor-sketch)
        
    *   [8.7.6. Mathematical Details](https://scikit-learn.org/stable/modules/kernel_approximation.html#mathematical-details)
        
*   [8.8. Pairwise metrics, Affinities and Kernels](https://scikit-learn.org/stable/modules/metrics.html)
    *   [8.8.1. Cosine similarity](https://scikit-learn.org/stable/modules/metrics.html#cosine-similarity)
        
    *   [8.8.2. Linear kernel](https://scikit-learn.org/stable/modules/metrics.html#linear-kernel)
        
    *   [8.8.3. Polynomial kernel](https://scikit-learn.org/stable/modules/metrics.html#polynomial-kernel)
        
    *   [8.8.4. Sigmoid kernel](https://scikit-learn.org/stable/modules/metrics.html#sigmoid-kernel)
        
    *   [8.8.5. RBF kernel](https://scikit-learn.org/stable/modules/metrics.html#rbf-kernel)
        
    *   [8.8.6. Laplacian kernel](https://scikit-learn.org/stable/modules/metrics.html#laplacian-kernel)
        
    *   [8.8.7. Chi-squared kernel](https://scikit-learn.org/stable/modules/metrics.html#chi-squared-kernel)
        
*   [8.9. Transforming the prediction target (`y`)](https://scikit-learn.org/stable/modules/preprocessing_targets.html)
    *   [8.9.1. Label binarization](https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-binarization)
        
    *   [8.9.2. Label encoding](https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding)
        

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)