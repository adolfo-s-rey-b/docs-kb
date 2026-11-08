[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.unbatch Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/batching.py#L268-L295)

Splits elements of a dataset into multiple elements on the batch dimension. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.unbatch`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/unbatch)

tf.data.experimental.unbatch()

For example, if elements of the dataset are shaped `[B, a0, a1, ...]`, where `B` may vary for each input element, then for each element in the dataset, the unbatched dataset will contain `B` consecutive elements of shape `[a0, a1, ...]`.

# NOTE: The following example uses `{ ... }` to represent the contents
    # of a dataset.
    a = { ['a', 'b', 'c'], ['a', 'b'], ['a', 'b', 'c', 'd'] }
    
    a.unbatch() == {
        'a', 'b', 'c', 'a', 'b', 'a', 'b', 'c', 'd'}

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