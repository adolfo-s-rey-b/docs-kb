[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fcreate_global_step&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.create\_global\_step Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#description)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/create_global_step#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/training_util.py#L164-L255)

Create global step tensor in graph.

tf.compat.v1.train.create_global_step(
        graph=None
    )

Migrate to TF2
--------------

With the deprecation of global graphs, TF no longer tracks variables in collections. In other words, there are no global variables in TF2. Thus, the global step functions have been removed (`get_or_create_global_step`, `create_global_step`, `get_global_step`) . You have two options for migrating:

1.  Create a Keras optimizer, which generates an `iterations` variable. This variable is automatically incremented when calling `apply_gradients`.
2.  Manually create and increment a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
    .

Below is an example of migrating away from using a global step to using a Keras optimizer:

Define a dummy model and loss:

    def compute_loss(x):

Before migrating:

    g = tf.Graph()

Migrating to a Keras optimizer:

    optimizer = tf.keras.optimizers.SGD(.01)

Description
-----------

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | The graph in which to create the global step tensor. If missing, use default graph. |

|     |
| --- |
| Returns<br>------- |     |
| Global step tensor. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if global step tensor is already defined. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.