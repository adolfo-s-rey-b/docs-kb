[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.fetch_lfw_people.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.fetch_lfw_people.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.fetch_lfw_people.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.fetch_lfw_people.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.fetch_lfw_people.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.fetch_lfw_people.html)

Collapse Sidebar Expand Sidebar

fetch\_lfw\_people[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#fetch-lfw-people "Link to this heading")

========================================================================================================================================================

sklearn.datasets.fetch\_lfw\_people(_\*_, _data\_home\=None_, _funneled\=True_, _resize\=0.5_, _min\_faces\_per\_person\=0_, _color\=False_, _slice\_\=(slice(70, 195, None), slice(78, 172, None))_, _download\_if\_missing\=True_, _return\_X\_y\=False_, _n\_retries\=3_, _delay\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_lfw.py#L251)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "Link to this definition")

Load the Labeled Faces in the Wild (LFW) people dataset (classification).

Download it if necessary.

|     |     |
| --- | --- |
| Classes | 5749 |
| Samples total | 13233 |
| Dimensionality | 5828 |
| Features | real, between 0 and 255 |

For a usage example of this dataset, see [Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#sphx-glr-auto-examples-applications-plot-face-recognition-py)
.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/real_world.html#labeled-faces-in-the-wild-dataset)
.

Parameters:

**data\_home**str or path-like, default=None

Specify another download and cache folder for the datasets. By default all scikit-learn data is stored in ‘~/scikit\_learn\_data’ subfolders.

**funneled**bool, default=True

Download and use the funneled variant of the dataset.

**resize**float or None, default=0.5

Ratio used to resize the each face picture. If `None`, no resizing is performed.

**min\_faces\_per\_person**int, default=0

The extracted dataset will only retain pictures of people that have at least `min_faces_per_person` different pictures.

**color**bool, default=False

Keep the 3 RGB channels instead of averaging them to a single gray level channel. If color is True the shape of the data has one more dimension than the shape with color = False.

**slice\_**tuple of slice, default=(slice(70, 195), slice(78, 172))

Provide a custom 2D slice (height, width) to extract the ‘interesting’ part of the jpeg files and avoid use statistical correlation from the background.

**download\_if\_missing**bool, default=True

If False, raise an OSError if the data is not locally available instead of trying to download the data from the source site.

**return\_X\_y**bool, default=False

If True, returns `(dataset.data, dataset.target)` instead of a Bunch object. See below for more information about the `dataset.data` and `dataset.target` object.

Added in version 0.20.

**n\_retries**int, default=3

Number of retries when HTTP errors are encountered.

Added in version 1.5.

**delay**float, default=1.0

Number of seconds between retries.

Added in version 1.5.

Returns:

**dataset**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

datanumpy array of shape (13233, 2914)

Each row corresponds to a ravelled face image of original size 62 x 47 pixels. Changing the `slice_` or resize parameters will change the shape of the output.

imagesnumpy array of shape (13233, 62, 47)

Each row is a face image corresponding to one of the 5749 people in the dataset. Changing the `slice_` or resize parameters will change the shape of the output.

targetnumpy array of shape (13233,)

Labels associated to each face image. Those labels range from 0-5748 and correspond to the person IDs.

target\_namesnumpy array of shape (5749,)

Names of all persons in the dataset. Position in array corresponds to the person ID in the target array.

DESCRstr

Description of the Labeled Faces in the Wild (LFW) dataset.

**(data, target)**tuple if `return_X_y` is True

A tuple of two ndarray. The first containing a 2D array of shape (n\_samples, n\_features) with each row representing one sample and each column representing the features. The second ndarray of shape (n\_samples,) containing the target samples.

Added in version 0.20.

Examples

\>>> from sklearn.datasets import fetch\_lfw\_people
\>>> lfw\_people \= fetch\_lfw\_people()
\>>> lfw\_people.data.shape
(13233, 2914)
\>>> lfw\_people.target.shape
(13233,)
\>>> for name in lfw\_people.target\_names\[:5\]:
...    print(name)
AJ Cook
AJ Lamas
Aaron Eckhart
Aaron Guiel
Aaron Patterson

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)