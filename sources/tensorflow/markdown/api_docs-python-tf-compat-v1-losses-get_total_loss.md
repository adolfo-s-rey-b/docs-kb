[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.losses.get\_total\_loss Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/losses/get_total_loss#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/losses/util.py#L234-L263)

Returns a tensor whose value represents the total loss.

tf.compat.v1.losses.get_total_loss(
        add_regularization_losses=True, name='total_loss', scope=None
    )

In particular, this adds any losses you have added with `tf.add_loss()` to any regularization losses that have been added by regularization parameters on layers constructors e.g. `tf.layers`. Be very sure to use this if you are constructing a loss\_op manually. Otherwise regularization arguments on `tf.layers` methods will not function.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `add_regularization_losses` | A boolean indicating whether or not to use the regularization losses in the sum. |
| `name` | The name of the returned tensor. |
| `scope` | An optional scope name for filtering the losses to return. Note that this filters the losses added with `tf.add_loss()` as well as the regularization losses to that scope. |

|     |
| --- |
| Returns<br>------- |     |
| A `Tensor` whose value represents the total loss. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `losses` is not iterable. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.