[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.train.get\_or\_create\_global\_step Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/get_or_create_global_step#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/training/training_util.py#L258-L326)

Returns and create (if necessary) the global step tensor.

tf.compat.v1.train.get_or_create_global_step(
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

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) | *   [Multi-worker training with Estimator](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_estimator)<br>    <br>*   [Checkpointer and PolicySaver](https://www.tensorflow.org/agents/tutorials/10_checkpointer_policysaver_tutorial)<br>    <br>*   [Exploring the TF-Hub CORD-19 Swivel Embeddings](https://www.tensorflow.org/hub/tutorials/cord_19_embeddings)<br>    <br>*   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan)<br>    <br>*   [Graph-based Neural Structured Learning in TFX](https://www.tensorflow.org/tfx/tutorials/tfx/neural_structured_learning) |

|     |     |
| --- | --- |
| Args<br>---- |     |
| `graph` | The graph in which to create the global step tensor. If missing, use default graph. |

|     |
| --- |
| Returns<br>------- |     |
| The global step tensor. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.