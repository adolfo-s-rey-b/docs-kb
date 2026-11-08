[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Ftrain%2Fget_global_step&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.get\_global\_step Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_global_step#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/training_util.py#L70-L161)

Get the global step tensor.

tf.compat.v1.train.get_global_step(
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

Using `get_global_step`:

    with g.as_default():

Migrating to a Keras optimizer:

    optimizer = tf.keras.optimizers.SGD(.01)

Description
-----------

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Migration examples: Canned Estimators](https://www.tensorflow.org/guide/migrate/canned_estimators)<br>    <br>*   [Migrate early stopping](https://www.tensorflow.org/guide/migrate/early_stopping)<br>    <br>*   [Migrate LoggingTensorHook and StopAtStepHook to Keras callbacks](https://www.tensorflow.org/guide/migrate/logging_stop_hook)<br>    <br>*   [Migrate metrics and optimizers](https://www.tensorflow.org/guide/migrate/metrics_optimizers) | *   [Checkpointer and PolicySaver](https://www.tensorflow.org/agents/tutorials/10_checkpointer_policysaver_tutorial) |

The global step tensor must be an integer variable. We first try to find it in the collection `GLOBAL_STEP`, or by name `global_step:0`.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | The graph to find the global step in. If missing, use default graph. |

|     |
| --- |
| Returns<br>------- |     |
| The global step variable, or `None` if none was found. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | If the global step tensor has a non-integer type, or if it is not a `Variable`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.