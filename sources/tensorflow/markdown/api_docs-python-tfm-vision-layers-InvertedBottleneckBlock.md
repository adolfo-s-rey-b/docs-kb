[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.InvertedBottleneckBlock Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/InvertedBottleneckBlock#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_blocks.py#L496-L773)

An inverted bottleneck block.

tfm.vision.layers.InvertedBottleneckBlock(
        in_filters,
        out_filters,
        expand_ratio,
        strides,
        kernel_size=3,
        se_ratio=None,
        stochastic_depth_drop_rate=None,
        kernel_initializer='VarianceScaling',
        kernel_regularizer=None,
        bias_regularizer=None,
        activation='relu',
        se_inner_activation='relu',
        se_gating_activation='sigmoid',
        se_round_down_protect=True,
        expand_se_in_filters=False,
        depthwise_activation=None,
        use_sync_bn=False,
        dilation_rate=1,
        divisible_by=1,
        regularize_depthwise=False,
        use_depthwise=True,
        use_residual=True,
        norm_momentum=0.99,
        norm_epsilon=0.001,
        output_intermediate_endpoints=False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `in_filters` | An `int` number of filters of the input tensor. |
| `out_filters` | An `int` number of filters of the output tensor. |
| `expand_ratio` | An `int` of expand\_ratio for an inverted bottleneck block. |
| `strides` | An `int` block stride. If greater than 1, this block will ultimately downsample the input. |
| `kernel_size` | An `int` kernel\_size of the depthwise conv layer. |
| `se_ratio` | A `float` or None. If not None, se ratio for the squeeze and excitation layer. |
| `stochastic_depth_drop_rate` | A `float` or None. if not None, drop rate for the stochastic depth layer. |
| `kernel_initializer` | A `str` of kernel\_initializer for convolutional layers. |
| `kernel_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2D. Default to None. |
| `bias_regularizer` | A `tf_keras.regularizers.Regularizer` object for Conv2d. Default to None. |
| `activation` | A `str` name of the activation function. |
| `se_inner_activation` | A `str` name of squeeze-excitation inner activation. |
| `se_gating_activation` | A `str` name of squeeze-excitation gating activation. |
| `se_round_down_protect` | A `bool` of whether round down more than 10% will be allowed in SE layer. |
| `expand_se_in_filters` | A `bool` of whether or not to expand in\_filter in squeeze and excitation layer. |
| `depthwise_activation` | A `str` name of the activation function for depthwise only. |
| `use_sync_bn` | A `bool`. If True, use synchronized batch normalization. |
| `dilation_rate` | An `int` that specifies the dilation rate to use for. |
| `divisible_by` | An `int` that ensures all inner dimensions are divisible by this number. dilated convolution: An `int` to specify the same value for all spatial dimensions. |
| `regularize_depthwise` | A `bool` of whether or not apply regularization on depthwise. |
| `use_depthwise` | A `bool` of whether to uses fused convolutions instead of depthwise. |
| `use_residual` | A `bool` of whether to include residual connection between input and output. |
| `norm_momentum` | A `float` of normalization momentum for the moving average. |
| `norm_epsilon` | A `float` added to variance to avoid dividing by zero. |
| `output_intermediate_endpoints` | A `bool` of whether or not output the intermediate endpoints. |
| `**kwargs` | Additional keyword arguments to be passed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/nn_blocks.py#L742-L773)

call(
        inputs, training=None
    )

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