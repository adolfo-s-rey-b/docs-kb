[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_files.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_files.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_files.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_files.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_files.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_files.html)

Collapse Sidebar Expand Sidebar

load\_files[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#load-files "Link to this heading")

=====================================================================================================================================

sklearn.datasets.load\_files(_container\_path_, _\*_, _description\=None_, _categories\=None_, _load\_content\=True_, _shuffle\=True_, _encoding\=None_, _decode\_error\='strict'_, _random\_state\=0_, _allowed\_extensions\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L131)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#sklearn.datasets.load_files "Link to this definition")

Load text files with categories as subfolder names.

Individual samples are assumed to be files stored a two levels folder structure such as the following:

container\_folder/
    category\_1\_folder/
        file\_1.txt
        file\_2.txt
        ...
        file\_42.txt
    category\_2\_folder/
        file\_43.txt
        file\_44.txt
        ...

Copy to clipboard

The folder names are used as supervised signal label names. The individual file names are not important.

This function does not try to extract features into a numpy array or scipy sparse matrix. In addition, if load\_content is false it does not try to load the files in memory.

To use text files in a scikit-learn classification or clustering algorithm, you will need to use the [`text`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.text "sklearn.feature_extraction.text")
 module to build a feature extraction transformer that suits your problem.

If you set load\_content=True, you should also specify the encoding of the text using the ‘encoding’ parameter. For many modern text files, ‘utf-8’ will be the correct encoding. If you leave encoding equal to None, then the content will be made of bytes instead of Unicode, and you will not be able to use most functions in [`text`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.text "sklearn.feature_extraction.text")
.

Similar feature extractors should be built for other kind of unstructured data input such as images, audio, video, …

If you want files with a specific file extension (e.g. `.txt`) then you can pass a list of those file extensions to `allowed_extensions`.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets.html#datasets)
.

Parameters:

**container\_path**str

Path to the main folder holding one subfolder per category.

**description**str, default=None

A paragraph describing the characteristic of the dataset: its source, reference, etc.

**categories**list of str, default=None

If None (default), load all the categories. If not None, list of category names to load (other categories ignored).

**load\_content**bool, default=True

Whether to load or not the content of the different files. If true a ‘data’ attribute containing the text information is present in the data structure returned. If not, a filenames attribute gives the path to the files.

**shuffle**bool, default=True

Whether or not to shuffle the data: might be important for models that make the assumption that the samples are independent and identically distributed (i.i.d.), such as stochastic gradient descent.

**encoding**str, default=None

If None, do not try to decode the content of the files (e.g. for images or other non-text content). If not None, encoding to use to decode text files to Unicode if load\_content is True.

**decode\_error**{‘strict’, ‘ignore’, ‘replace’}, default=’strict’

Instruction on what to do if a byte sequence is given to analyze that contains characters not of the given `encoding`. Passed as keyword argument ‘errors’ to bytes.decode.

**random\_state**int, RandomState instance or None, default=0

Determines random number generation for dataset shuffling. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**allowed\_extensions**list of str, default=None

List of desired file extensions to filter the files to be loaded.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datalist of str

Only present when `load_content=True`. The raw text data to learn.

targetndarray

The target labels (integer index).

target\_nameslist

The names of target classes.

DESCRstr

The full description of the dataset.

filenames: ndarray

The filenames holding the dataset.

Examples

\>>> from sklearn.datasets import load\_files
\>>> container\_path \= "./"
\>>> load\_files(container\_path)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)