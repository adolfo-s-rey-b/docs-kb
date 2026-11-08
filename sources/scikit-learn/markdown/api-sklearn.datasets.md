[Skip to main content](https://scikit-learn.org/stable/api/sklearn.datasets.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.datasets.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.datasets.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.datasets.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.datasets.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.datasets.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.datasets.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.datasets.html)

Collapse Sidebar Expand Sidebar

sklearn.datasets[#](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "Link to this heading")

==============================================================================================================================

Utilities to load popular datasets and artificial data generators.

**User guide.** See the [Dataset loading utilities](https://scikit-learn.org/stable/datasets.html#datasets)
 section for further details.

Loaders[#](https://scikit-learn.org/stable/api/sklearn.datasets.html#loaders "Link to this heading")

-----------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`clear_data_home`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html#sklearn.datasets.clear_data_home "sklearn.datasets.clear_data_home") | Delete all the content of the data home cache. |
| [`dump_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "sklearn.datasets.dump_svmlight_file") | Dump the dataset in svmlight / libsvm file format. |
| [`fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups") | Load the filenames and data from the 20 newsgroups dataset (classification). |
| [`fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized") | Load and vectorize the 20 newsgroups dataset (classification). |
| [`fetch_california_housing`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing") | Load the California housing dataset (regression). |
| [`fetch_covtype`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype") | Load the covertype dataset (classification). |
| [`fetch_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_file.html#sklearn.datasets.fetch_file "sklearn.datasets.fetch_file") | Fetch a file from the web if not already present in the local folder. |
| [`fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99") | Load the kddcup99 dataset (classification). |
| [`fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs") | Load the Labeled Faces in the Wild (LFW) pairs dataset (classification). |
| [`fetch_lfw_people`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people") | Load the Labeled Faces in the Wild (LFW) people dataset (classification). |
| [`fetch_olivetti_faces`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces") | Load the Olivetti faces data-set from AT&T (classification). |
| [`fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml") | Fetch dataset from openml by name or dataset id. |
| [`fetch_rcv1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1 "sklearn.datasets.fetch_rcv1") | Load the RCV1 multilabel dataset (classification). |
| [`fetch_species_distributions`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions") | Loader for species distribution dataset from Phillips et. |
| [`get_data_home`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#sklearn.datasets.get_data_home "sklearn.datasets.get_data_home") | Return the path of the scikit-learn data directory. |
| [`load_breast_cancer`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer") | Load and return the breast cancer Wisconsin dataset (classification). |
| [`load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes") | Load and return the diabetes dataset (regression). |
| [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits") | Load and return the digits dataset (classification). |
| [`load_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#sklearn.datasets.load_files "sklearn.datasets.load_files") | Load text files with categories as subfolder names. |
| [`load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris") | Load and return the iris dataset (classification). |
| [`load_linnerud`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud "sklearn.datasets.load_linnerud") | Load and return the physical exercise Linnerud dataset. |
| [`load_sample_image`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html#sklearn.datasets.load_sample_image "sklearn.datasets.load_sample_image") | Load the numpy array of a single sample image. |
| [`load_sample_images`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#sklearn.datasets.load_sample_images "sklearn.datasets.load_sample_images") | Load sample images for image manipulation. |
| [`load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file") | Load datasets in the svmlight / libsvm format into sparse CSR matrix. |
| [`load_svmlight_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#sklearn.datasets.load_svmlight_files "sklearn.datasets.load_svmlight_files") | Load dataset from multiple files in SVMlight format. |
| [`load_wine`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine") | Load and return the wine dataset (classification). |

Sample generators[#](https://scikit-learn.org/stable/api/sklearn.datasets.html#sample-generators "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`make_biclusters`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters") | Generate a constant block diagonal structure array for biclustering. |
| [`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs") | Generate isotropic Gaussian blobs for clustering. |
| [`make_checkerboard`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard") | Generate an array with block checkerboard structure for biclustering. |
| [`make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles") | Make a large circle containing a smaller circle in 2d. |
| [`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification") | Generate a random n-class classification problem. |
| [`make_friedman1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html#sklearn.datasets.make_friedman1 "sklearn.datasets.make_friedman1") | Generate the "Friedman #1" regression problem. |
| [`make_friedman2`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html#sklearn.datasets.make_friedman2 "sklearn.datasets.make_friedman2") | Generate the "Friedman #2" regression problem. |
| [`make_friedman3`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman3.html#sklearn.datasets.make_friedman3 "sklearn.datasets.make_friedman3") | Generate the "Friedman #3" regression problem. |
| [`make_gaussian_quantiles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles") | Generate isotropic Gaussian and label samples by quantile. |
| [`make_hastie_10_2`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "sklearn.datasets.make_hastie_10_2") | Generate data for binary classification used in Hastie et al. 2009, Example 10.2. |
| [`make_low_rank_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix") | Generate a mostly low rank matrix with bell-shaped singular values. |
| [`make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons") | Make two interleaving half circles. |
| [`make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification") | Generate a random multilabel classification problem. |
| [`make_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression") | Generate a random regression problem. |
| [`make_s_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "sklearn.datasets.make_s_curve") | Generate an S curve dataset. |
| [`make_sparse_coded_signal`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal") | Generate a signal as a sparse combination of dictionary elements. |
| [`make_sparse_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix") | Generate a sparse symmetric definite positive matrix. |
| [`make_sparse_uncorrelated`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html#sklearn.datasets.make_sparse_uncorrelated "sklearn.datasets.make_sparse_uncorrelated") | Generate a random regression problem with sparse uncorrelated design. |
| [`make_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#sklearn.datasets.make_spd_matrix "sklearn.datasets.make_spd_matrix") | Generate a random symmetric, positive-definite matrix. |
| [`make_swiss_roll`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll") | Generate a swiss roll dataset. |