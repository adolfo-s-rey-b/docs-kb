[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon?version=stable#args_1)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon?version=stable#yields_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.forward\_compatibility\_horizon Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon?version=stable#args_1)
    
*   [Yields](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon?version=stable#yields_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/compat/compat.py#L125-L168)

Context manager for testing forward compatibility of generated graphs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.compat.forward_compatibility_horizon`](https://www.tensorflow.org/api_docs/python/tf/compat/forward_compatibility_horizon)

@tf_contextlib.contextmanager

See [Version compatibility](https://www.tensorflow.org/guide/versions#backward_and_partial_forward_compatibility)
.

To ensure forward compatibility of generated graphs (see `forward_compatible`) with older binaries, new features can be gated with:

if compat.forward_compatible(year=2018, month=08, day=01):
      generate_graph_with_new_features()
    else:
      generate_graph_so_older_binaries_can_consume_it()

However, when adding new features, one may want to unittest it before the forward compatibility window expires. This context manager enables such tests. For example:

from tensorflow.python.compat import compat
    
    def testMyNewFeature(self):
      with compat.forward_compatibility_horizon(2018, 08, 02):
         # Test that generate_graph_with_new_features() has an effect

|     |     |
| --- | --- |
| Args<br>---- |     |
| `year` | A year (e.g., 2018). Must be an `int`. |
| `month` | A month (1 <= month <= 12) in year. Must be an `int`. |
| `day` | A day (1 <= day <= 31, or 30, or 29, or 28) in month. Must be an `int`. |

|     |
| --- |
| Yields<br>------ |     |
| Nothing. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.