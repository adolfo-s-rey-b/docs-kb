[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_sample_images.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_sample_images.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_sample_images.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_sample_images.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_sample_images.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_sample_images.html)

Collapse Sidebar Expand Sidebar

load\_sample\_images[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#load-sample-images "Link to this heading")

==============================================================================================================================================================

sklearn.datasets.load\_sample\_images()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L1296)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#sklearn.datasets.load_sample_images "Link to this definition")

Load sample images for image manipulation.

Loads both, `china` and `flower`.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#sample-images)
.

Returns:

**data**[`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")

Dictionary-like object, with the following attributes.

imageslist of ndarray of shape (427, 640, 3)

The two sample image.

filenameslist

The filenames for the images.

DESCRstr

The full description of the dataset.

Examples

To load the data and visualize the images:

\>>> from sklearn.datasets import load\_sample\_images
\>>> dataset \= load\_sample\_images()
\>>> len(dataset.images)
2
\>>> first\_img\_data \= dataset.images\[0\]
\>>> first\_img\_data.shape
(427, 640, 3)
\>>> first\_img\_data.dtype
dtype('uint8')

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)