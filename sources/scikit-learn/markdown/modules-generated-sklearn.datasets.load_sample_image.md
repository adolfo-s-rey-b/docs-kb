[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.load_sample_image.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.load_sample_image.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.load_sample_image.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.load_sample_image.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_sample_image.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_sample_image.html)

Collapse Sidebar Expand Sidebar

load\_sample\_image[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html#load-sample-image "Link to this heading")

===========================================================================================================================================================

sklearn.datasets.load\_sample\_image(_image\_name_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_base.py#L1359)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html#sklearn.datasets.load_sample_image "Link to this definition")

Load the numpy array of a single sample image.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/loading_other_datasets.html#sample-images)
.

Parameters:

**image\_name**{`china.jpg`, `flower.jpg`}

The name of the sample image loaded.

Returns:

**img**3D array

The image as a numpy array: height x width x color.

Examples

\>>> from sklearn.datasets import load\_sample\_image
\>>> china \= load\_sample\_image('china.jpg')
\>>> china.dtype
dtype('uint8')
\>>> china.shape
(427, 640, 3)
\>>> flower \= load\_sample\_image('flower.jpg')
\>>> flower.dtype
dtype('uint8')
\>>> flower.shape
(427, 640, 3)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)