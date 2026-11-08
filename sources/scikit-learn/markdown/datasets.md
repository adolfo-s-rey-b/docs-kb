[Skip to main content](https://scikit-learn.org/stable/datasets.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/datasets.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/datasets.html)
[1.8.0](https://scikit-learn.org/1.8/datasets.html)
[1.7.2](https://scikit-learn.org/1.7/datasets.html)
[1.6.1](https://scikit-learn.org/1.6/datasets.html)
[1.5.2](https://scikit-learn.org/1.5/datasets.html)
[1.4.2](https://scikit-learn.org/1.4/datasets.html)

Collapse Sidebar Expand Sidebar

9\. Dataset loading utilities[#](https://scikit-learn.org/stable/datasets.html#dataset-loading-utilities "Link to this heading")

=================================================================================================================================

The `sklearn.datasets` package embeds some small toy datasets and provides helpers to fetch larger datasets commonly used by the machine learning community to benchmark algorithms on data that comes from the ‘real world’.

To evaluate the impact of the scale of the dataset (`n_samples` and `n_features`) while controlling the statistical properties of the data (typically the correlation and informativeness of the features), it is also possible to generate synthetic data.

**General dataset API.** There are three main kinds of dataset interfaces that can be used to get datasets depending on the desired type of dataset.

**The dataset loaders.** They can be used to load small standard datasets, described in the [Toy datasets](https://scikit-learn.org/stable/datasets/toy_dataset.html#toy-datasets)
 section.

**The dataset fetchers.** They can be used to download and load larger datasets, described in the [Real world datasets](https://scikit-learn.org/stable/datasets/real_world.html#real-world-datasets)
 section.

Both loaders and fetchers functions return a [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
 object holding at least two items: an array of shape `n_samples` \* `n_features` with key `data` (except for 20newsgroups) and a numpy array of length `n_samples`, containing the target values, with key `target`.

The Bunch object is a dictionary that exposes its keys as attributes. For more information about Bunch object, see [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")
.

It’s also possible for almost all of these functions to constrain the output to be a tuple containing only the data and the target, by setting the `return_X_y` parameter to `True`.

The datasets also contain a full description in their `DESCR` attribute and some contain `feature_names` and `target_names`. See the dataset descriptions below for details.

**The dataset generation functions.** They can be used to generate controlled synthetic datasets, described in the [Generated datasets](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
 section.

These functions return a tuple `(X, y)` consisting of a `n_samples` \* `n_features` numpy array `X` and an array of length `n_samples` containing the targets `y`.

In addition, there are also miscellaneous tools to load datasets of other formats or from other locations, described in the [Loading other datasets](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#loading-other-datasets)
 section.

*   [9.1. Toy datasets](https://scikit-learn.org/stable/datasets/toy_dataset.html)
    *   [9.1.1. Iris plants dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset)
        
    *   [9.1.2. Diabetes dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset)
        
    *   [9.1.3. Optical recognition of handwritten digits dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#optical-recognition-of-handwritten-digits-dataset)
        
    *   [9.1.4. Linnerrud dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset)
        
    *   [9.1.5. Wine recognition dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#wine-recognition-dataset)
        
    *   [9.1.6. Breast cancer Wisconsin (diagnostic) dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-wisconsin-diagnostic-dataset)
        
*   [9.2. Real world datasets](https://scikit-learn.org/stable/datasets/real_world.html)
    *   [9.2.1. The Olivetti faces dataset](https://scikit-learn.org/stable/datasets/real_world.html#the-olivetti-faces-dataset)
        
    *   [9.2.2. The 20 newsgroups text dataset](https://scikit-learn.org/stable/datasets/real_world.html#the-20-newsgroups-text-dataset)
        
    *   [9.2.3. The Labeled Faces in the Wild face recognition dataset](https://scikit-learn.org/stable/datasets/real_world.html#the-labeled-faces-in-the-wild-face-recognition-dataset)
        
    *   [9.2.4. Forest covertypes](https://scikit-learn.org/stable/datasets/real_world.html#forest-covertypes)
        
    *   [9.2.5. RCV1 dataset](https://scikit-learn.org/stable/datasets/real_world.html#rcv1-dataset)
        
    *   [9.2.6. Kddcup 99 dataset](https://scikit-learn.org/stable/datasets/real_world.html#kddcup-99-dataset)
        
    *   [9.2.7. California Housing dataset](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)
        
    *   [9.2.8. Species distribution dataset](https://scikit-learn.org/stable/datasets/real_world.html#species-distribution-dataset)
        
*   [9.3. Generated datasets](https://scikit-learn.org/stable/datasets/sample_generators.html)
    *   [9.3.1. Generators for classification and clustering](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-classification-and-clustering)
        
    *   [9.3.2. Generators for regression](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-regression)
        
    *   [9.3.3. Generators for manifold learning](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-manifold-learning)
        
    *   [9.3.4. Generators for decomposition](https://scikit-learn.org/stable/datasets/sample_generators.html#generators-for-decomposition)
        
*   [9.4. Loading other datasets](https://scikit-learn.org/stable/datasets/loading_other_datasets.html)
    *   [9.4.1. Sample images](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#sample-images)
        
    *   [9.4.2. Datasets in svmlight / libsvm format](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#datasets-in-svmlight-libsvm-format)
        
    *   [9.4.3. Downloading datasets from the openml.org repository](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#downloading-datasets-from-the-openml-org-repository)
        
    *   [9.4.4. Loading from external datasets](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#loading-from-external-datasets)
        

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)