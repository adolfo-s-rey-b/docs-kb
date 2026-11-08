[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_olivetti_faces.html)

Collapse Sidebar Expand Sidebar

fetch\_olivetti\_faces[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#fetch-olivetti-faces "Link to this heading")

====================================================================================================================================================================

sklearn.datasets.fetch\_olivetti\_faces(_\*_, _data\_home\=None_, _shuffle\=False_, _random\_state\=0_, _download\_if\_missing\=True_, _return\_X\_y\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_olivetti_faces.py#L43)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "Link to this definition")

Load the Olivetti faces data-set from AT&T (classification).

Download it if necessary.

|     |     |
| --- | --- |
| Classes | 40  |
| Samples total | 400 |
| Dimensionality | 4096 |
| Features | real, between 0 and 1 |

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#olivetti-faces-dataset)
.

Parameters:

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**shuffle**bool, default=False

If True the order of the dataset is shuffled to avoid having images of the same person grouped.

**random\_state**int, RandomState instance or None, default=0

Determines random number generation for dataset shuffling. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**return\_X\_y**bool, default=False

If True, returns `(data, target)` instead of a `Bunch` object. See below for more information about the `data` and `target` objects.

Added in version 0.22.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

data: ndarray, shape (400, 4096)

Each row corresponds to a ravelled face image of original size 64 x 64 pixels.

imagesndarray, shape (400, 64, 64)

Each row is a face image corresponding to one of the 40 subjects of the dataset.

targetndarray, shape (400,)

Labels associated to each face image. Those labels are ranging from 0-39 and correspond to the Subject IDs.

DESCRstr

Description of the modified Olivetti Faces Dataset.

**(data, target)**tuple if `return_X_y=True`

Tuple with the `data` and `target` objects described above.

Added in version 0.22.

Examples

\>>> from sklearn.datasets import fetch\_olivetti\_faces
\>>> olivetti\_faces \= fetch\_olivetti\_faces()
\>>> olivetti\_faces.data.shape
(400, 4096)
\>>> olivetti\_faces.target.shape
(400,)
\>>> olivetti\_faces.images.shape
(400, 64, 64)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multioutput_face_completion_thumb.png)

[Face completion with a multi-output estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html)

Face completion with a multi-output estimators

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)