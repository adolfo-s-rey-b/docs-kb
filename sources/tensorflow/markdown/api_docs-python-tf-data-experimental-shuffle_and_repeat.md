[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.shuffle\_and\_repeat Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/shuffle_ops.py#L58-L112)

Shuffles and repeats a Dataset, reshuffling with each repetition. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.shuffle_and_repeat`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/shuffle_and_repeat)

tf.data.experimental.shuffle_and_repeat(
        buffer_size, count=None, seed=None
    )

    d = tf.data.Dataset.from_tensor_slices([1, 2, 3])

dataset.apply(
      tf.data.experimental.shuffle_and_repeat(buffer_size, count, seed))

produces the same output as

dataset.shuffle(
      buffer_size, seed=seed, reshuffle_each_iteration=True).repeat(count)

In each repetition, this dataset fills a buffer with `buffer_size` elements, then randomly samples elements from this buffer, replacing the selected elements with new elements. For perfect shuffling, set the buffer size equal to the full size of the dataset.

For instance, if your dataset contains 10,000 elements but `buffer_size` is set to 1,000, then `shuffle` will initially select a random element from only the first 1,000 elements in the buffer. Once an element is selected, its space in the buffer is replaced by the next (i.e. 1,001-st) element, maintaining the 1,000 element buffer.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `buffer_size` | A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the maximum number elements that will be buffered when prefetching. |
| `count` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the number of times the dataset should be repeated. The default behavior (if `count` is `None` or `-1`) is for the dataset be repeated indefinitely. |
| `seed` | (Optional.) A [`tf.int64`](https://www.tensorflow.org/api_docs/python/tf#int64)<br> scalar [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br>, representing the random seed that will be used to create the distribution. See [`tf.random.set_seed`](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)<br> for behavior. |

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