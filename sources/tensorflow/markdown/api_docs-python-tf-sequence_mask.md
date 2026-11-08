[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/sequence_mask)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/sequence_mask?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.sequence\_mask Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/sequence_mask#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/array_ops.py#L4166-L4230)

Returns a mask tensor representing the first N positions of each cell.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.sequence_mask`](https://www.tensorflow.org/api_docs/python/tf/sequence_mask)

tf.sequence_mask(
        lengths,
        maxlen=None,
        dtype=tf.dtypes.bool,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TFP Release Notes notebook (0.13.0)](https://www.tensorflow.org/probability/examples/TFP_Release_Notebook_0_13_0) |

If `lengths` has shape `[d_1, d_2, ..., d_n]` the resulting tensor `mask` has dtype `dtype` and shape `[d_1, d_2, ..., d_n, maxlen]`, with

mask[i_1, i_2, ..., i_n, j] = (j < lengths[i_1, i_2, ..., i_n])

#### Examples:

tf.sequence_mask([1, 3, 2], 5)  # [[True, False, False, False, False],\
                                    #  [True, True, True, False, False],\
                                    #  [True, True, False, False, False]]
    
    tf.sequence_mask([[1, 3],[2,0]])  # [[[True, False, False],\
                                      #   [True, True, True]],\
                                      #  [[True, True, False],\
                                      #   [False, False, False]]]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `lengths` | integer tensor, all its values <= maxlen. |
| `maxlen` | scalar integer tensor, size of last dimension of returned tensor. Default is the maximum value in `lengths`. |
| `dtype` | output type of the resulting tensor. |
| `name` | name of the op. |

|     |
| --- |
| Returns<br>------- |     |
| A mask tensor of shape `lengths.shape + (maxlen,)`, cast to specified dtype. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `maxlen` is not a scalar. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.