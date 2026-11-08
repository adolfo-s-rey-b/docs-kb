[Skip to main content](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/api/sklearn.feature_extraction.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html)
[1.8.0](https://scikit-learn.org/1.8/api/sklearn.feature_extraction.html)
[1.7.2](https://scikit-learn.org/1.7/api/sklearn.feature_extraction.html)
[1.6.1](https://scikit-learn.org/1.6/api/sklearn.feature_extraction.html)
[1.5.2](https://scikit-learn.org/1.5/api/sklearn.feature_extraction.html)
[1.4.2](https://scikit-learn.org/1.4/api/sklearn.feature_extraction.html)

Collapse Sidebar Expand Sidebar

sklearn.feature\_extraction[#](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "Link to this heading")

=============================================================================================================================================================

Feature extraction from raw data.

**User guide.** See the [Feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction)
 section for further details.

|     |     |
| --- | --- |
| [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer") | Transforms lists of feature-value mappings to vectors. |
| [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher") | Implements feature hashing, aka the hashing trick. |

From images[#](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.image "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Utilities to extract features from images.

|     |     |
| --- | --- |
| [`image.PatchExtractor`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor "sklearn.feature_extraction.image.PatchExtractor") | Extracts patches from a collection of images. |
| [`image.extract_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d") | Reshape a 2D image into a collection of patches. |
| [`image.grid_to_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html#sklearn.feature_extraction.image.grid_to_graph "sklearn.feature_extraction.image.grid_to_graph") | Graph of the pixel-to-pixel connections. |
| [`image.img_to_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html#sklearn.feature_extraction.image.img_to_graph "sklearn.feature_extraction.image.img_to_graph") | Graph of the pixel-to-pixel gradient connections. |
| [`image.reconstruct_from_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "sklearn.feature_extraction.image.reconstruct_from_patches_2d") | Reconstruct the image from all of its patches. |

From text[#](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction.text "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Utilities to build feature vectors from text documents.

|     |     |
| --- | --- |
| [`text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer") | Convert a collection of text documents to a matrix of token counts. |
| [`text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer") | Convert a collection of text documents to a matrix of token occurrences. |
| [`text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer") | Transform a count matrix to a normalized tf or tf-idf representation. |
| [`text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer") | Convert a collection of raw documents to a matrix of TF-IDF features. |