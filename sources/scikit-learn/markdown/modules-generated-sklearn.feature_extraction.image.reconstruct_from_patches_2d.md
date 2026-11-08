[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html)

Collapse Sidebar Expand Sidebar

reconstruct\_from\_patches\_2d[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#reconstruct-from-patches-2d "Link to this heading")

==========================================================================================================================================================================================================

sklearn.feature\_extraction.image.reconstruct\_from\_patches\_2d(_patches_, _image\_size_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L464)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "Link to this definition")

Reconstruct the image from all of its patches.

Patches are assumed to overlap and the image is constructed by filling in the patches from left to right, top to bottom, averaging the overlapping regions.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#image-feature-extraction)
.

Parameters:

**patches**ndarray of shape (n\_patches, patch\_height, patch\_width) or (n\_patches, patch\_height, patch\_width, n\_channels)

The complete set of patches. If the patches contain colour information, channels are indexed along the last dimension: RGB patches would have `n_channels=3`.

**image\_size**tuple of int (image\_height, image\_width) or (image\_height, image\_width, n\_channels)

The size of the image that will be reconstructed.

Returns:

**image**ndarray of shape image\_size

The reconstructed image.

Examples

\>>> from sklearn.datasets import load\_sample\_image
\>>> from sklearn.feature\_extraction import image
\>>> one\_image \= load\_sample\_image("china.jpg")
\>>> print('Image shape: {}'.format(one\_image.shape))
Image shape: (427, 640, 3)
\>>> image\_patches \= image.extract\_patches\_2d(image\=one\_image, patch\_size\=(10, 10))
\>>> print('Patches shape: {}'.format(image\_patches.shape))
Patches shape: (263758, 10, 10, 3)
\>>> image\_reconstructed \= image.reconstruct\_from\_patches\_2d(
...     patches\=image\_patches,
...     image\_size\=one\_image.shape
... )
\>>> print(f"Reconstructed shape: {image\_reconstructed.shape}")
Reconstructed shape: (427, 640, 3)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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