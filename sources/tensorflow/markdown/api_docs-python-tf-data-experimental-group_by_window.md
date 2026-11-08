[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.group\_by\_window Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/grouping.py#L58-L107)

A transformation that groups windows of elements by key and reduces them. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.group_by_window`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/group_by_window)

tf.data.experimental.group_by_window(
        key_func, reduce_func, window_size=None, window_size_func=None
    )

This transformation maps each consecutive element in a dataset to a key using `key_func` and groups the elements by key. It then applies `reduce_func` to at most `window_size_func(key)` elements matching the same key. All except the final window for each key will contain `window_size_func(key)` elements; the final window may be smaller.

You may provide either a constant `window_size` or a window size determined by the key through `window_size_func`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `key_func` | A function mapping a nested structure of tensors (having shapes and types defined by `self.output_shapes` and `self.output_types`) to a scalar [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> tensor. |
| `reduce_func` | A function mapping a key and a dataset of up to `window_size` consecutive elements matching that key to another dataset. |
| `window_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements matching the same key to combine in a single batch, which will be passed to `reduce_func`. Mutually exclusive with `window_size_func`. |
| `window_size_func` | A function mapping a key to a [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of consecutive elements matching the same key to combine in a single batch, which will be passed to `reduce_func`. Mutually exclusive with `window_size`. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if neither or both of {`window_size`, `window_size_func`} are passed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.