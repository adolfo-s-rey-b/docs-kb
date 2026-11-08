[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.parallel\_interleave Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/interleave_ops.py#L24-L87)

A parallel version of the [`Dataset.interleave()`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)
 transformation. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.parallel_interleave`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/parallel_interleave)

tf.data.experimental.parallel_interleave(
        map_func,
        cycle_length,
        block_length=1,
        sloppy=False,
        buffer_output_elements=None,
        prefetch_input_elements=None
    )

`parallel_interleave()` maps `map_func` across its input to produce nested datasets, and outputs their elements interleaved. Unlike [`tf.data.Dataset.interleave`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave)
, it gets elements from `cycle_length` nested datasets in parallel, which increases the throughput, especially in the presence of stragglers. Furthermore, the `sloppy` argument can be used to improve performance, by relaxing the requirement that the outputs are produced in a deterministic order, and allowing the implementation to skip over nested datasets whose elements are not readily available when requested.

#### Example usage:

# Preprocess 4 files concurrently.
    filenames = tf.data.Dataset.list_files("/path/to/data/train*.tfrecords")
    dataset = filenames.apply(
        tf.data.experimental.parallel_interleave(
            lambda filename: tf.data.TFRecordDataset(filename),
            cycle_length=4))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `map_func` | A function mapping a nested structure of tensors to a `Dataset`. |
| `cycle_length` | The number of input `Dataset`s to interleave from in parallel. |
| `block_length` | The number of consecutive elements to pull from an input `Dataset` before advancing to the next input `Dataset`. |
| `sloppy` | A boolean controlling whether determinism should be traded for performance by allowing elements to be produced out of order. If `sloppy` is `None`, the [`tf.data.Options.deterministic`](https://www.tensorflow.org/api_docs/python/tf/data/Options#deterministic)<br> dataset option (`True` by default) is used to decide whether to enforce a deterministic order. |
| `buffer_output_elements` | The number of elements each iterator being interleaved should buffer (similar to the `.prefetch()` transformation for each interleaved iterator). |
| `prefetch_input_elements` | The number of input elements to transform to iterators before they are needed for interleaving. |

|     |
| --- |
| Returns<br>------- |     |
| A `Dataset` transformation function, which can be passed to [`tf.data.Dataset.apply`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#apply)<br>. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.