[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.BottleneckResidualInner Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/BottleneckResidualInner#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_blocks.py#L1861-L2000)

Creates a single inner block of a bottleneck.

tfm.vision.layers.BottleneckResidualInner(
        filters: int,
        strides: int,
        kernel_initializer: Union[str, Callable[..., tf_keras.initializers.Initializer]] = 'VarianceScaling',
        kernel_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        activation: Union[str, Callable[..., tf.Tensor]] = 'relu',
        use_sync_bn: bool = False,
        norm_momentum: float = 0.99,
        norm_epsilon: float = 0.001,
        batch_norm_first: bool = True,
        **kwargs
    )

This corresponds to `F`/`G` functions in the RevNet paper: Aidan N. Gomez, Mengye Ren, Raquel Urtasun, Roger B. Grosse. The Reversible Residual Network: Backpropagation Without Storing Activations. ([https://arxiv.org/pdf/1707.04585.pdf](https://arxiv.org/pdf/1707.04585.pdf)
)

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filters` | An `int` number of filters for first 2 convolutions. Last Last, and thus the number of output channels from the bottlneck block is `4*filters` |
| `strides` | An `int` of stride size for convolution for the residual block. |
| `kernel_initializer` | A `str` or `tf_keras.initializers.Initializer` instance for convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` for Conv2D. |
| `activation` | A `str` or `callable` instance of the activation function. |
| `use_sync_bn` | A `bool`. If True, use synchronized batch normalization. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `batch_norm_first` | A `bool` of whether to apply activation and batch norm before conv. |
| `**kwargs` | Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_blocks.py#L1983-L2000)

call(
        inputs: tf.Tensor, training: Optional[bool] = None
    ) -> tf.Tensor

This is where the layer's logic lives.

The `call()` method may not create state (except in its first invocation, wrapping the creation of variables or other resources in [`tf.init_scope()`](https://www.tensorflow.org/api_docs/python/tf/init_scope)
). It is recommended to create state, including [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 instances and nested `Layer` instances, in `__init__()`, or in the `build()` method that is called automatically before `call()` executes for the first time.

|     |     |
| --- | --- |
| Args |     |
| `inputs` | Input tensor, or dict/list/tuple of input tensors. The first positional `inputs` argument is subject to special rules:<br><br>*   `inputs` must be explicitly passed. A layer cannot have zero arguments, and `inputs` cannot be provided via the default value of a keyword argument.<br>*   NumPy array or Python scalar values in `inputs` get cast as tensors.<br>*   TF-Keras mask metadata is only collected from `inputs`.<br>*   Layers are built (`build(input_shape)` method) using shape info from `inputs` only.<br>*   `input_spec` compatibility is only checked against `inputs`.<br>*   Mixed precision input casting is only applied to `inputs`. If a layer has tensor arguments in `*args` or `**kwargs`, their casting behavior in mixed precision should be handled manually.<br>*   The SavedModel input specification is generated using `inputs` only.<br>*   Integration with various ecosystem packages like TFMOT, TFLite, TF.js, etc is only supported for `inputs` and not for tensors in positional and keyword arguments. |
| `*args` | Additional positional arguments. May contain tensors, although this is not recommended, for the reasons above. |
| `**kwargs` | Additional keyword arguments. May contain tensors, although this is not recommended, for the reasons above. The following optional keyword arguments are reserved:*   `training`: Boolean scalar tensor of Python boolean indicating whether the `call` is meant for training or inference.<br>*   `mask`: Boolean input mask. If the layer's `call()` method takes a `mask` argument, its default value will be set to the mask generated for `inputs` by the previous layer (if `input` did come from a layer that generated a corresponding mask, i.e. if it came from a TF-Keras layer with masking support). |

|     |
| --- |
| Returns |     |
| A tensor or list/tuple of tensors. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.