[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.nn.compute\_average\_loss Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/nn_impl_distribute.py#L70-L142)

Scales per-example losses with sample\_weights and computes their average.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.nn.compute_average_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss)

tf.nn.compute_average_loss(
        per_example_loss, sample_weight=None, global_batch_size=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TPUs](https://www.tensorflow.org/guide/tpu)<br>    <br>*   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) | *   [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)<br>    <br>*   [Custom training loop with Keras and MultiWorkerMirroredStrategy](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) |

Usage with distribution strategy and custom training loop:

with strategy.scope():
      def compute_loss(labels, predictions, sample_weight=None):
    
        # If you are using a `Loss` class instead, set reduction to `NONE` so that
        # we can do the reduction afterwards and divide by global batch size.
        per_example_loss = tf.keras.losses.sparse_categorical_crossentropy(
            labels, predictions)
    
        # Compute loss that is scaled by sample_weight and by global batch size.
        return tf.nn.compute_average_loss(
            per_example_loss,
            sample_weight=sample_weight,
            global_batch_size=GLOBAL_BATCH_SIZE)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `per_example_loss` | Per-example loss. |
| `sample_weight` | Optional weighting for each example. |
| `global_batch_size` | Optional global batch size value. Defaults to (size of first dimension of `losses`) \* (number of replicas). |

|     |
| --- |
| Returns<br>------- |     |
| Scalar loss value, obtained by summing the `per_example_loss` and dividing by `global_batch_size`. If `global_batch_size` is zero, the result is zero. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.