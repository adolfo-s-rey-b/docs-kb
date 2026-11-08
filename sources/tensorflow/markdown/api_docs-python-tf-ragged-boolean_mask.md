[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.ragged.boolean\_mask Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/ragged/ragged_array_ops.py#L49-L211)

Applies a boolean mask to `data` without flattening the mask dimensions.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.ragged.boolean_mask`](https://www.tensorflow.org/api_docs/python/tf/ragged/boolean_mask)

tf.ragged.boolean_mask(
        data, mask, name=None
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer) |

Returns a potentially ragged tensor that is formed by retaining the elements in `data` where the corresponding value in `mask` is `True`.

*   `output[a1...aA, i, b1...bB] = data[a1...aA, j, b1...bB]`
    
    Where `j` is the `i`th `True` entry of `mask[a1...aA]`.
    

Note that `output` preserves the mask dimensions `a1...aA`; this differs from [`tf.boolean_mask`](https://www.tensorflow.org/api_docs/python/tf/boolean_mask)
, which flattens those dimensions.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `data` | A potentially ragged tensor. |
| `mask` | A potentially ragged boolean tensor. `mask`'s shape must be a prefix of `data`'s shape. `rank(mask)` must be known statically. |
| `name` | A name prefix for the returned tensor (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A potentially ragged tensor that is formed by retaining the elements in `data` where the corresponding value in `mask` is `True`.<br><br>*   `rank(output) = rank(data)`.<br>*   `output.ragged_rank = max(data.ragged_rank, rank(mask) - 1)`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `rank(mask)` is not known statically; or if `mask.shape` is not a prefix of `data.shape`. |

#### Examples:

    # Aliases for True & False so data and mask line up.

    tf.ragged.boolean_mask(  # Mask a 2D Tensor.

    tf.ragged.boolean_mask(  # Mask a 2D RaggedTensor.

    tf.ragged.boolean_mask(  # Mask rows of a 2D RaggedTensor.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.