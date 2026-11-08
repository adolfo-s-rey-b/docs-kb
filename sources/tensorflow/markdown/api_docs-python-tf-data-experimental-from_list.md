[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.from\_list Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/from_list.py#L78-L122)

Creates a `Dataset` comprising the given list of elements.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.from_list`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/from_list)

tf.data.experimental.from_list(
        elements, name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image captioning with visual attention](https://www.tensorflow.org/text/tutorials/image_captioning) |

The returned dataset will produce the items in the list one by one. The functionality is identical to [`Dataset.from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices)
 when elements are scalars, but different when elements have structure. Consider the following example.

    dataset = tf.data.experimental.from_list([(1, 'a'), (2, 'b'), (3, 'c')])

To get the same output with `from_tensor_slices`, the data needs to be reorganized:

    dataset = tf.data.Dataset.from_tensor_slices(([1, 2, 3], ['a', 'b', 'c']))

Unlike `from_tensor_slices`, `from_list` supports non-rectangular input:

    dataset = tf.data.experimental.from_list([[1], [2, 3]])

Achieving the same with `from_tensor_slices` requires the use of ragged tensors.

`from_list` can be more performant than `from_tensor_slices` in some cases, since it avoids the need for data slicing each epoch. However, it can also be less performant, because data is stored as many small tensors rather than a few large tensors as in `from_tensor_slices`. The general guidance is to prefer `from_list` from a performance perspective when the number of elements is small (less than 1000).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `elements` | A list of elements whose components have the same nested structure. |
| `name` | (Optional.) A name for the tf.data operation. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `Dataset` | A `Dataset` of the `elements`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.