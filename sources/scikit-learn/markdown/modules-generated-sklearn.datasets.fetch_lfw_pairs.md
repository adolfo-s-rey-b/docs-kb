[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_lfw_pairs.html)

Collapse Sidebar Expand Sidebar

fetch\_lfw\_pairs[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#fetch-lfw-pairs "Link to this heading")

=====================================================================================================================================================

sklearn.datasets.fetch\_lfw\_pairs(_\*_, _subset\='train'_, _data\_home\=None_, _funneled\=True_, _resize\=0.5_, _color\=False_, _slice\_\=(slice(70, 195, None), slice(78, 172, None))_, _download\_if\_missing\=True_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_lfw.py#L484)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "Link to this definition")

Load the Labeled Faces in the Wild (LFW) pairs dataset (classification).

Download it if necessary.

|     |     |
| --- | --- |
| Classes | 2   |
| Samples total | 13233 |
| Dimensionality | 5828 |
| Features | real, between 0 and 255 |

In the [original paper](https://people.cs.umass.edu/~elm/papers/lfw.pdf)
 the “pairs” version corresponds to the “restricted task”, where the experimenter should not use the name of a person to infer the equivalence or non-equivalence of two face images that are not explicitly given in the training set.

The original images are 250 x 250 pixels, but the default slice and resize arguments reduce them to 62 x 47.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#labeled-faces-in-the-wild-dataset)
.

Parameters:

**subset**{‘train’, ‘test’, ‘10\_folds’}, default=’train’

Select the dataset to load: ‘train’ for the development training set, ‘test’ for the development test set, and ‘10\_folds’ for the official evaluation set that is meant to be used with a 10-folds cross validation.

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**funneled**bool, default=True

Download and use the funneled variant of the dataset.

**resize**float, default=0.5

Ratio used to resize the each face picture.

**color**bool, default=False

Keep the 3 RGB channels instead of averaging them to a single gray level channel. If color is True the shape of the data has one more dimension than the shape with color = False.

**slice\_**tuple of slice, default=(slice(70, 195), slice(78, 172))

Provide a custom 2D slice (height, width) to extract the ‘interesting’ part of the jpeg files and avoid use statistical correlation from the background.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datandarray of shape (2200, 5828). Shape depends on `subset`.

Each row corresponds to 2 ravel’d face images of original size 62 x 47 pixels. Changing the `slice_`, `resize` or `subset` parameters will change the shape of the output.

pairsndarray of shape (2200, 2, 62, 47). Shape depends on `subset`

Each row has 2 face images corresponding to same or different person from the dataset containing 5749 people. Changing the `slice_`, `resize` or `subset` parameters will change the shape of the output.

targetnumpy array of shape (2200,). Shape depends on `subset`.

Labels associated to each pair of images. The two label values being different persons or the same person.

target\_namesnumpy array of shape (2,)

Explains the target values of the target array. 0 corresponds to “Different person”, 1 corresponds to “same person”.

DESCRstr

Description of the Labeled Faces in the Wild (LFW) dataset.

Examples

\>>> from sklearn.datasets import fetch\_lfw\_pairs
\>>> lfw\_pairs\_train \= fetch\_lfw\_pairs(subset\='train')
\>>> list(lfw\_pairs\_train.target\_names)
\[np.str\_('Different persons'), np.str\_('Same person')\]
\>>> lfw\_pairs\_train.pairs.shape
(2200, 2, 62, 47)
\>>> lfw\_pairs\_train.data.shape
(2200, 5828)
\>>> lfw\_pairs\_train.target.shape
(2200,)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)