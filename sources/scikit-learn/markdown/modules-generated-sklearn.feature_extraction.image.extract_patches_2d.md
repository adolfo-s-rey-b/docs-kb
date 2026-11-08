[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html)

Collapse Sidebar Expand Sidebar

extract\_patches\_2d[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#extract-patches-2d "Link to this heading")

==============================================================================================================================================================================

sklearn.feature\_extraction.image.extract\_patches\_2d(_image_, _patch\_size_, _\*_, _max\_patches\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L353)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "Link to this definition")

Reshape a 2D image into a collection of patches.

The resulting patches are allocated in a dedicated array.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#image-feature-extraction)
.

Parameters:

**image**ndarray of shape (image\_height, image\_width) or (image\_height, image\_width, n\_channels)

The original image data. For color images, the last dimension specifies the channel: a RGB image would have `n_channels=3`.

**patch\_size**tuple of int (patch\_height, patch\_width)

The dimensions of one patch.

**max\_patches**int or float, default=None

The maximum number of patches to extract. If `max_patches` is a float between 0 and 1, it is taken to be a proportion of the total number of patches. If `max_patches` is None it corresponds to the total number of patches that can be extracted.

**random\_state**int, RandomState instance, default=None

Determines the random number generator used for random sampling when `max_patches` is not None. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

Returns:

**patches**array of shape (n\_patches, patch\_height, patch\_width) or (n\_patches, patch\_height, patch\_width, n\_channels)

The collection of patches extracted from the image, where `n_patches` is either `max_patches` or the total number of patches that can be extracted.

Examples

\>>> from sklearn.datasets import load\_sample\_image
\>>> from sklearn.feature\_extraction import image
\>>> \# Use the array data from the first image in this dataset:
\>>> one\_image \= load\_sample\_image("china.jpg")
\>>> print('Image shape: {}'.format(one\_image.shape))
Image shape: (427, 640, 3)
\>>> patches \= image.extract\_patches\_2d(one\_image, (2, 2))
\>>> print('Patches shape: {}'.format(patches.shape))
Patches shape: (272214, 2, 2, 3)
\>>> \# Here are just two of these patches:
\>>> print(patches\[1\])
\[\[\[174 201 231\]\
  \[174 201 231\]\]\
 \[\[173 200 230\]\
  \[173 200 230\]\]\]
\>>> print(patches\[800\])
\[\[\[187 214 243\]\
  \[188 215 244\]\]\
 \[\[187 214 243\]\
  \[188 215 244\]\]\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_thumb.png)

[Image denoising using dictionary learning](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html)

Image denoising using dictionary learning

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)