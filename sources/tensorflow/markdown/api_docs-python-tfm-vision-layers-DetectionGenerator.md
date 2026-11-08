[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.layers.DetectionGenerator Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/layers/DetectionGenerator#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/layers/detection_generator.py#L914-L1123)

Generates the final detected boxes with scores and classes.

tfm.vision.layers.DetectionGenerator(
        apply_nms: bool = True,
        pre_nms_top_k: int = 5000,
        pre_nms_score_threshold: float = 0.05,
        nms_iou_threshold: float = 0.5,
        max_num_detections: int = 100,
        nms_version: str = 'v2',
        use_cpu_nms: bool = False,
        soft_nms_sigma: Optional[float] = None,
        use_sigmoid_probability: bool = False,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `apply_nms` | A `bool` of whether or not apply non maximum suppression. If False, the decoded boxes and their scores are returned. |
| `pre_nms_top_k` | An `int` of the number of top scores proposals to be kept before applying NMS. |
| `pre_nms_score_threshold` | A `float` of the score threshold to apply before applying NMS. Proposals whose scores are below this threshold are thrown away. |
| `nms_iou_threshold` | A `float` in \[0, 1\], the NMS IoU threshold. |
| `max_num_detections` | An `int` of the final number of total detections to generate. |
| `nms_version` | A string of `batched`, [`v1`](https://www.tensorflow.org/api_docs/python/tf/compat/v1)<br> or `v2` specifies NMS version. |
| `use_cpu_nms` | A `bool` of whether or not enforce NMS to run on CPU. |
| `soft_nms_sigma` | A `float` representing the sigma parameter for Soft NMS. When soft\_nms\_sigma=0.0, we fall back to standard NMS. |
| `use_sigmoid_probability` | A `bool`, if true, use sigmoid to get probability, otherwise use softmax. |
| `**kwargs` | Additional keyword arguments passed to Layer. |

Methods
-------

### `call`

call(
        inputs, *args, **kwargs
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