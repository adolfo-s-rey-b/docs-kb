[Skip to main content](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/datasets/loading_other_datasets.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/datasets/loading_other_datasets.html)
[1.8.0](https://scikit-learn.org/1.8/datasets/loading_other_datasets.html)
[1.7.2](https://scikit-learn.org/1.7/datasets/loading_other_datasets.html)
[1.6.1](https://scikit-learn.org/1.6/datasets/loading_other_datasets.html)
[1.5.2](https://scikit-learn.org/1.5/datasets/loading_other_datasets.html)
[1.4.2](https://scikit-learn.org/1.4/datasets/loading_other_datasets.html)

Collapse Sidebar Expand Sidebar

9.4. Loading other datasets[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#loading-other-datasets "Link to this heading")

===================================================================================================================================================

9.4.1. Sample images[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#sample-images "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Scikit-learn also embeds a couple of sample JPEG images published under Creative Commons license by their authors. Those images can be useful to test algorithms and pipelines on 2D data.

|     |     |
| --- | --- |
| [`load_sample_images`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#sklearn.datasets.load_sample_images "sklearn.datasets.load_sample_images")<br>() | Load sample images for image manipulation. |
| [`load_sample_image`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html#sklearn.datasets.load_sample_image "sklearn.datasets.load_sample_image")<br>(image\_name) | Load the numpy array of a single sample image. |

[![../_images/loading_other_datasets-1.png](https://scikit-learn.org/stable/_images/loading_other_datasets-1.png)](https://scikit-learn.org/stable/_images/loading_other_datasets-1.png)

Warning

The default coding of images is based on the `uint8` dtype to spare memory. Often machine learning algorithms work best if the input is converted to a floating point representation first. Also, if you plan to use `matplotlib.pyplot.imshow`, don’t forget to scale to the range 0 - 1 as done in the following example.

9.4.2. Datasets in svmlight / libsvm format[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#datasets-in-svmlight-libsvm-format "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

scikit-learn includes utility functions for loading datasets in the svmlight / libsvm format. In this format, each line takes the form `<label> <feature-id>:<feature-value> <feature-id>:<feature-value> ...`. This format is especially suitable for sparse datasets. In this module, scipy sparse CSR matrices are used for `X` and numpy arrays are used for `y`.

You may load a dataset like this as follows:

\>>> from sklearn.datasets import load\_svmlight\_file
\>>> X\_train, y\_train \= load\_svmlight\_file("/path/to/train\_dataset.txt")
...

Copy to clipboard

You may also load two (or more) datasets at once:

\>>> X\_train, y\_train, X\_test, y\_test \= load\_svmlight\_files(
...     ("/path/to/train\_dataset.txt", "/path/to/test\_dataset.txt"))
...

Copy to clipboard

In this case, `X_train` and `X_test` are guaranteed to have the same number of features. Another way to achieve the same result is to fix the number of features:

\>>> X\_test, y\_test \= load\_svmlight\_file(
...     "/path/to/test\_dataset.txt", n\_features\=X\_train.shape\[1\])
...

Copy to clipboard

Related links

*   `Public datasets in svmlight / libsvm format`: [https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets](https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets)
    
*   `Faster API-compatible implementation`: [mblondel/svmlight-loader](https://github.com/mblondel/svmlight-loader)
    

9.4.3. Downloading datasets from the openml.org repository[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#downloading-datasets-from-the-openml-org-repository "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[openml.org](https://openml.org/)
 is a public repository for machine learning data and experiments, that allows everybody to upload open datasets.

The `sklearn.datasets` package is able to download datasets from the repository using the function [`sklearn.datasets.fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
.

For example, to download a dataset of gene expressions in mice brains:

\>>> from sklearn.datasets import fetch\_openml
\>>> mice \= fetch\_openml(name\='miceprotein', version\=4)

Copy to clipboard

To fully specify a dataset, you need to provide a name and a version, though the version is optional, see [Dataset Versions](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#openml-versions)
 below. The dataset contains a total of 1080 examples belonging to 8 different classes:

\>>> mice.data.shape
(1080, 77)
\>>> mice.target.shape
(1080,)
\>>> np.unique(mice.target)
array(\['c-CS-m', 'c-CS-s', 'c-SC-m', 'c-SC-s', 't-CS-m', 't-CS-s', 't-SC-m', 't-SC-s'\], dtype=object)

Copy to clipboard

You can get more information on the dataset by looking at the `DESCR` and `details` attributes:

\>>> print(mice.DESCR)
\*\*Author\*\*: Clara Higuera, Katheleen J. Gardiner, Krzysztof J. Cios
\*\*Source\*\*: \[UCI\](https://archive.ics.uci.edu/ml/datasets/Mice+Protein+Expression) - 2015
\*\*Please cite\*\*: Higuera C, Gardiner KJ, Cios KJ (2015) Self-Organizing
Feature Maps Identify Proteins Critical to Learning in a Mouse Model of Down
Syndrome. PLoS ONE 10(6): e0129126...

\>>> mice.details
{'id': '40966', 'name': 'MiceProtein', 'version': '4', 'format': 'ARFF',
'upload\_date': '2017-11-08T16:00:15', 'licence': 'Public',
'url': 'https://www.openml.org/data/v1/download/17928620/MiceProtein.arff',
'file\_id': '17928620', 'default\_target\_attribute': 'class',
'row\_id\_attribute': 'MouseID',
'ignore\_attribute': \['Genotype', 'Treatment', 'Behavior'\],
'tag': \['OpenML-CC18', 'study\_135', 'study\_98', 'study\_99'\],
'visibility': 'public', 'status': 'active',
'md5\_checksum': '3c479a6885bfa0438971388283a1ce32'}

Copy to clipboard

The `DESCR` contains a free-text description of the data, while `details` contains a dictionary of meta-data stored by openml, like the dataset id. For more details, see the [OpenML documentation](https://docs.openml.org/#data)
 The `data_id` of the mice protein dataset is 40966, and you can use this (or the name) to get more information on the dataset on the openml website:

\>>> mice.url
'https://www.openml.org/d/40966'

Copy to clipboard

The `data_id` also uniquely identifies a dataset from OpenML:

\>>> mice \= fetch\_openml(data\_id\=40966)
\>>> mice.details
{'id': '4550', 'name': 'MiceProtein', 'version': '1', 'format': 'ARFF',
'creator': ...,
'upload\_date': '2016-02-17T14:32:49', 'licence': 'Public', 'url':
'https://www.openml.org/data/v1/download/1804243/MiceProtein.ARFF', 'file\_id':
'1804243', 'default\_target\_attribute': 'class', 'citation': 'Higuera C,
Gardiner KJ, Cios KJ (2015) Self-Organizing Feature Maps Identify Proteins
Critical to Learning in a Mouse Model of Down Syndrome. PLoS ONE 10(6):
e0129126. \[Web Link\] journal.pone.0129126', 'tag': \['OpenML100', 'study\_14',\
'study\_34'\], 'visibility': 'public', 'status': 'active', 'md5\_checksum':
'3c479a6885bfa0438971388283a1ce32'}

Copy to clipboard

### 9.4.3.1. Dataset Versions[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#dataset-versions "Link to this heading")

A dataset is uniquely specified by its `data_id`, but not necessarily by its name. Several different “versions” of a dataset with the same name can exist which can contain entirely different datasets. If a particular version of a dataset has been found to contain significant issues, it might be deactivated. Using a name to specify a dataset will yield the earliest version of a dataset that is still active. That means that `fetch_openml(name="miceprotein")` can yield different results at different times if earlier versions become inactive. You can see that the dataset with `data_id` 40966 that we fetched above is the first version of the “miceprotein” dataset:

\>>> mice.details\['version'\]
'1'

Copy to clipboard

In fact, this dataset only has one version. The iris dataset on the other hand has multiple versions:

\>>> iris \= fetch\_openml(name\="iris")
\>>> iris.details\['version'\]
'1'
\>>> iris.details\['id'\]
'61'

\>>> iris\_61 \= fetch\_openml(data\_id\=61)
\>>> iris\_61.details\['version'\]
'1'
\>>> iris\_61.details\['id'\]
'61'

\>>> iris\_969 \= fetch\_openml(data\_id\=969)
\>>> iris\_969.details\['version'\]
'3'
\>>> iris\_969.details\['id'\]
'969'

Copy to clipboard

Specifying the dataset by the name “iris” yields the lowest version, version 1, with the `data_id` 61. To make sure you always get this exact dataset, it is safest to specify it by the dataset `data_id`. The other dataset, with `data_id` 969, is version 3 (version 2 has become inactive), and contains a binarized version of the data:

\>>> np.unique(iris\_969.target)
array(\['N', 'P'\], dtype=object)

Copy to clipboard

You can also specify both the name and the version, which also uniquely identifies the dataset:

\>>> iris\_version\_3 \= fetch\_openml(name\="iris", version\=3)
\>>> iris\_version\_3.details\['version'\]
'3'
\>>> iris\_version\_3.details\['id'\]
'969'

Copy to clipboard

References

*   [Vanschoren, van Rijn, Bischl and Torgo. “OpenML: networked science in machine learning” ACM SIGKDD Explorations Newsletter, 15(2), 49-60, 2014.](https://arxiv.org/abs/1407.7722)
    

### 9.4.3.2. ARFF parser[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#arff-parser "Link to this heading")

From version 1.2, scikit-learn provides a new keyword argument `parser` that provides several options to parse the ARFF files provided by OpenML. The legacy parser (i.e. `parser="liac-arff"`) is based on the project [LIAC-ARFF](https://github.com/renatopp/liac-arff)
. This parser is however slow and consumes more memory than required. A new parser based on pandas (i.e. `parser="pandas"`) is both faster and more memory efficient. However, this parser does not support sparse data. Therefore, we recommend using `parser="auto"` which will use the best parser available for the requested dataset.

The `"pandas"` and `"liac-arff"` parsers can lead to different data types in the output. The notable differences are the following:

*   The `"liac-arff"` parser always encodes categorical features as `str` objects. To the contrary, the `"pandas"` parser instead infers the type while reading and numerical categories will be casted into integers whenever possible.
    
*   The `"liac-arff"` parser uses float64 to encode numerical features tagged as ‘REAL’ and ‘NUMERICAL’ in the metadata. The `"pandas"` parser instead infers if these numerical features correspond to integers and uses pandas’ Integer extension dtype.
    
*   In particular, classification datasets with integer categories are typically loaded as such `(0, 1, ...)` with the `"pandas"` parser while `"liac-arff"` will force the use of string encoded class labels such as `"0"`, `"1"` and so on.
    
*   The `"pandas"` parser will not strip single quotes - i.e. `'` - from string columns. For instance, a string `'my string'` will be kept as is while the `"liac-arff"` parser will strip the single quotes. For categorical columns, the single quotes are stripped from the values.
    

In addition, when `as_frame=False` is used, the `"liac-arff"` parser returns ordinally encoded data where the categories are provided in the attribute `categories` of the `Bunch` instance. Instead, `"pandas"` returns a NumPy array were the categories. Then it’s up to the user to design a feature engineering pipeline with an instance of `OneHotEncoder` or `OrdinalEncoder` typically wrapped in a `ColumnTransformer` to preprocess the categorical columns explicitly. See for instance: [Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html#sphx-glr-auto-examples-compose-plot-column-transformer-mixed-types-py)
.

9.4.4. Loading from external datasets[#](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#loading-from-external-datasets "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

scikit-learn works on any numeric data stored as numpy arrays or scipy sparse matrices. Other types that are convertible to numeric arrays such as pandas DataFrame are also acceptable.

Here are some recommended ways to load standard columnar data into a format usable by scikit-learn:

*   [pandas.io](https://pandas.pydata.org/pandas-docs/stable/io.html)
     provides tools to read data from common formats including CSV, Excel, JSON and SQL. DataFrames may also be constructed from lists of tuples or dicts. Pandas handles heterogeneous data smoothly and provides tools for manipulation and conversion into a numeric array suitable for scikit-learn.
    
*   [scipy.io](https://docs.scipy.org/doc/scipy/reference/io.html)
     specializes in binary formats often used in scientific computing contexts such as .mat and .arff
    
*   [numpy/routines.io](https://docs.scipy.org/doc/numpy/reference/routines.io.html)
     for standard loading of columnar data into numpy arrays
    
*   scikit-learn’s [`load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")
     for the svmlight or libSVM sparse format
    
*   scikit-learn’s [`load_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#sklearn.datasets.load_files "sklearn.datasets.load_files")
     for directories of text files where the name of each directory is the name of each category and each file inside of each directory corresponds to one sample from that category
    

For some miscellaneous data such as images, videos, and audio, you may wish to refer to:

*   [skimage.io](https://scikit-image.org/docs/dev/api/skimage.io.html)
     or [Imageio](https://imageio.readthedocs.io/en/stable/reference/core_v3.html)
     for loading images and videos into numpy arrays
    
*   [scipy.io.wavfile.read](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html)
     for reading WAV files into a numpy array
    

Categorical (or nominal) features stored as strings (common in pandas DataFrames) will need converting to numerical features using [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")
 or [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")
 or similar. See [Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
.

Note: if you manage your own numerical data it is recommended to use an optimized file format such as HDF5 to reduce data load times. Various libraries such as H5Py, PyTables and pandas provide a Python interface for reading and writing data in that format.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)