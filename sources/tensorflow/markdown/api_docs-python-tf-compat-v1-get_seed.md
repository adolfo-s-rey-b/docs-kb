[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.get\_seed Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/random_seed.py#L38-L93)

Returns the local seeds an operation should use given an op-specific seed.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.get_seed`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_seed)

tf.compat.v1.get_seed(
        op_seed
    )

Given operation-specific seed, `op_seed`, this helper function returns two seeds derived from graph-level and op-level seeds. Many random operations internally use the two seeds to allow user to change the seed globally for a graph, or for only specific operations.

For details on how the graph-level seed interacts with op seeds, see [`tf.compat.v1.random.set_random_seed`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `op_seed` | integer. |

|     |
| --- |
| Returns<br>------- |     |
| A tuple of two integers that should be used for the local seed of this operation. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.