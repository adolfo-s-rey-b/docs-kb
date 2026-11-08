[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.register\_filesystem\_plugin Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/load_library.py#L199-L220)

Loads a TensorFlow FileSystem plugin.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.register_filesystem_plugin`](https://www.tensorflow.org/api_docs/python/tf/experimental/register_filesystem_plugin)

tf.experimental.register_filesystem_plugin(
        plugin_location
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `plugin_location` | Path to the plugin. Relative or absolute filesystem plugin path to a dynamic library file. |

|     |
| --- |
| Returns<br>------- |     |
| None |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `OSError` | When the file to be loaded is not found. |
| `RuntimeError` | when unable to load the library. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.