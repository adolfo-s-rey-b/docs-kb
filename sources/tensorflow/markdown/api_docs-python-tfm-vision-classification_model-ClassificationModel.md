[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.classification\_model.ClassificationModel Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/classification_model.py#L23-L131)

A classification class builder.

#### View aliases

**Main aliases**

[`tfm.vision.models.ClassificationModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/classification_model/ClassificationModel)

tfm.vision.classification_model.ClassificationModel(
        backbone: tf_keras.Model,
        num_classes: int,
        input_specs: tf_keras.layers.InputSpec = layers.InputSpec(shape=[None, None, None, 3]),
        dropout_rate: float = 0.0,
        kernel_initializer: str = 'random_uniform',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        bias_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        add_head_batch_norm: bool = False,
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        skip_logits_layer: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `backbone` | a backbone network. |
| `num_classes` | `int` number of classes in classification task. |
| `input_specs` | `tf_keras.layers.InputSpec` specs of the input tensor. |
| `dropout_rate` | `float` rate for dropout regularization. |
| `kernel_initializer` | kernel initializer for the dense layer. |
| `kernel_regularizer` | tf\_keras.regularizers.Regularizer object. Default to None. |
| `bias_regularizer` | tf\_keras.regularizers.Regularizer object. Default to None. |
| `add_head_batch_norm` | `bool` whether to add a batch normalization layer before pool. |
| `use_sync_bn` | `bool` if True, use synchronized batch normalization. |
| `norm_momentum` | `float` normalization momentum for the moving average. |
| `norm_epsilon` | `float` small float added to variance to avoid dividing by zero. |
| `skip_logits_layer` | `bool`, whether to skip the prediction layer. |
| `**kwargs` | keyword arguments to be passed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `backbone` |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |

Methods
-------

### `call`

call(
        inputs, training=None, mask=None
    )

Calls the model on new inputs and returns the outputs as tensors.

In this case `call()` just reapplies all ops in the graph to the new inputs (e.g. build a new computational graph from the provided inputs).

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. |
| `training` | Boolean or boolean scalar tensor, indicating whether to run the `Network` in training mode or inference mode. |
| `mask` | A mask or list of masks. A mask can be either a boolean tensor or None (no mask). For more details, check the guide [here](https://www.tensorflow.org/guide/keras/masking_and_padding)<br>. |

|     |
| --- |
| Returns |     |
| A tensor if there is a single output, or a list of tensors if there are more than one outputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.