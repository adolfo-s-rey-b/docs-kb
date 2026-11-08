[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html)

Collapse Sidebar Expand Sidebar

PatchExtractor[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#patchextractor "Link to this heading")

================================================================================================================================================================

class sklearn.feature\_extraction.image.PatchExtractor(_\*_, _patch\_size\=None_, _max\_patches\=None_, _random\_state\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L530)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor "Link to this definition")

Extracts patches from a collection of images.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#image-feature-extraction)
.

Added in version 0.9.

Parameters:

**patch\_size**tuple of int (patch\_height, patch\_width), default=None

The dimensions of one patch. If set to None, the patch size will be automatically set to `(img_height // 10, img_width // 10)`, where `img_height` and `img_width` are the dimensions of the input images.

**max\_patches**int or float, default=None

The maximum number of patches per image to extract. If `max_patches` is a float in (0, 1), it is taken to mean a proportion of the total number of patches. If set to None, extract all possible patches.

**random\_state**int, RandomState instance, default=None

Determines the random number generator used for random sampling when `max_patches is not None`. Use an int to make the randomness deterministic. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

See also

[`reconstruct_from_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "sklearn.feature_extraction.image.reconstruct_from_patches_2d")

Reconstruct image from all of its patches.

Notes

This estimator is stateless and does not need to be fitted. However, we recommend to call [`fit_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.fit_transform "sklearn.feature_extraction.image.PatchExtractor.fit_transform")
 instead of [`transform`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.transform "sklearn.feature_extraction.image.PatchExtractor.transform")
, as parameter validation is only performed in [`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.fit "sklearn.feature_extraction.image.PatchExtractor.fit")
.

Examples

\>>> from sklearn.datasets import load\_sample\_images
\>>> from sklearn.feature\_extraction import image
\>>> \# Use the array data from the second image in this dataset:
\>>> X \= load\_sample\_images().images\[1\]
\>>> X \= X\[None, ...\]
\>>> print(f"Image shape: {X.shape}")
Image shape: (1, 427, 640, 3)
\>>> pe \= image.PatchExtractor(patch\_size\=(10, 10))
\>>> pe\_trans \= pe.transform(X)
\>>> print(f"Patches shape: {pe\_trans.shape}")
Patches shape: (263758, 10, 10, 3)
\>>> X\_reconstructed \= image.reconstruct\_from\_patches\_2d(pe\_trans, X.shape\[1:\])
\>>> print(f"Reconstructed shape: {X\_reconstructed.shape}")
Reconstructed shape: (427, 640, 3)

Copy to clipboard

fit(_X_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L598)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.fit "Link to this definition")

Only validate the parameters of the estimator.

This method allows to: (i) validate the parameters of the estimator and (ii) be consistent with the scikit-learn transformer API.

Parameters:

**X**ndarray of shape (n\_samples, image\_height, image\_width) or (n\_samples, image\_height, image\_width, n\_channels)

Array of images from which to extract patches. For color images, the last dimension specifies the channel: a RGB image would have `n_channels=3`.

**y**Ignored

Not used, present for API consistency by convention.

Returns:

**self**object

Returns the instance itself.

fit\_transform(_X_, _y\=None_, _\*\*fit\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L913)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.fit_transform "Link to this definition")

Fit to data, then transform it.

Fits transformer to `X` and `y` with optional parameters `fit_params` and returns a transformed version of `X`.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

Input samples.

**y**array-like of shape (n\_samples,) or (n\_samples, n\_outputs), default=None

Target values (None for unsupervised transformations).

**\*\*fit\_params**dict

Additional fit parameters. Pass only if the estimator accepts additional params in its `fit` method.

Returns:

**X\_new**ndarray array of shape (n\_samples, n\_features\_new)

Transformed array.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

set\_output(_\*_, _transform\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_set_output.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.set_output "Link to this definition")

Set output container.

Refer to the [user guide](https://scikit-learn.org/stable/modules/df_output_transform.html#df-output-transform)
 for more details and [Introducing the set\_output API](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_set_output.html#sphx-glr-auto-examples-miscellaneous-plot-set-output-py)
 for an example on how to use the API.

Parameters:

**transform**{“default”, “pandas”, “polars”}, default=None

Configure output of `transform` and `fit_transform`.

*   `"default"`: Default output format of a transformer
    
*   `"pandas"`: DataFrame output
    
*   `"polars"`: Polars output
    
*   `None`: Transform configuration is unchanged
    

Added in version 1.4: `"polars"` option was added.

Returns:

**self**estimator instance

Estimator instance.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L623)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor.transform "Link to this definition")

Transform the image samples in `X` into a matrix of patch data.

Parameters:

**X**ndarray of shape (n\_samples, image\_height, image\_width) or (n\_samples, image\_height, image\_width, n\_channels)

Array of images from which to extract patches. For color images, the last dimension specifies the channel: a RGB image would have `n_channels=3`.

Returns:

**patches**array of shape (n\_patches, patch\_height, patch\_width) or (n\_patches, patch\_height, patch\_width, n\_channels)

The collection of patches extracted from the images, where `n_patches` is either `n_samples * max_patches` or the total number of patches that can be extracted.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)