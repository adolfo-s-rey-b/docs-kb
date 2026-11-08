[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.distribute.experimental\_set\_strategy Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/distribute/distribute_lib.py#L583-L629)

Set a [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)
 as current without `with strategy.scope()`.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.distribute.experimental_set_strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental_set_strategy)

tf.distribute.experimental_set_strategy(
        strategy
    )

tf.distribute.experimental_set_strategy(strategy1)
    f()
    tf.distribute.experimental_set_strategy(strategy2)
    g()
    tf.distribute.experimental_set_strategy(None)
    h()

is equivalent to:

with strategy1.scope():
      f()
    with strategy2.scope():
      g()
    h()

In general, you should use the `with strategy.scope():` API, but this alternative may be convenient in notebooks where you would have to put each cell in a `with strategy.scope():` block.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `strategy` | A [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)<br> object or None. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `RuntimeError` | If called inside a `with strategy.scope():`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.