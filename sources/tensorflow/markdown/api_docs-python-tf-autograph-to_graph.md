[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.autograph.to\_graph Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/autograph/to_graph#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/autograph/impl/api.py#L707-L776)

Converts a Python entity into a TensorFlow graph.

tf.autograph.to_graph(
        entity, recursive=True, experimental_optional_features=None
    )

Also see: [`tf.autograph.to_code`](https://www.tensorflow.org/api_docs/python/tf/autograph/to_code)
, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
.

Unlike [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
, `to_graph` is a low-level transpiler that converts Python code to TensorFlow graph code. It does not implement any caching, variable management or create any actual ops, and is best used where greater control over the generated TensorFlow graph is desired. Another difference from [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 is that `to_graph` will not wrap the graph into a TensorFlow function or a Python callable. Internally, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 uses `to_graph`.

#### Example usage:

    def f(x):

Supported Python entities include:

*   functions
*   classes
*   object methods

Functions are converted into new functions with converted code.

Classes are converted by generating a new class whose methods use converted code.

Methods are converted into unbound function that have an additional first argument called `self`.

For a tutorial, see the [tf.function and AutoGraph guide](https://www.tensorflow.org/guide/function)
. For more detailed information, see the [AutoGraph reference documentation](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/autograph/g3doc/reference/index.md)
.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `entity` | Python callable or class to convert. |
| `recursive` | Whether to recursively convert any functions that the converted function may call. |
| `experimental_optional_features` | `None`, a tuple of, or a single [`tf.autograph.experimental.Feature`](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature)<br> value. |

|     |
| --- |
| Returns<br>------- |     |
| Same as `entity`, the converted Python function or class. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If the entity could not be converted. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.