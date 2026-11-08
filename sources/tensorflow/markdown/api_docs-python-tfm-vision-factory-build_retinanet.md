[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/factory/build_retinanet#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.factory.build\_retinanet Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/factory.py#L260-L375)

Builds a RetinaNet model.

tfm.vision.factory.build_retinanet(
        input_specs: tf_keras.layers.InputSpec,
        model_config: tfm.vision.configs.retinanet.RetinaNet,
        l2_regularizer: Optional[tf_keras.regularizers.Regularizer] = None,
        backbone: Optional[tf_keras.Model] = None,
        decoder: Optional[tf_keras.Model] = None,
        num_anchors_per_location: (int | dict[str, int] | None) = None,
        anchor_boxes: (Mapping[str, tf.Tensor] | None) = None
    ) -> tf_keras.Model

|     |     |
| --- | --- |
| Args<br>---- |     |
| `input_specs` | The InputSpec of the input image tensor to the model. |
| `model_config` | The RetinaNet model configuration to build from. |
| `l2_regularizer` | Optional l2 regularizer to use for building the backbone, decorder, and head. |
| `backbone` | Optional instance of the backbone model. |
| `decoder` | Optional instance of the decoder model. |
| `num_anchors_per_location` | Optional number of anchors per pixel location for building the RetinaNetHead. If an `int`, the same number is used for all levels. If a `dict`, it specifies the number at each level. If `none`, it uses `len(aspect_ratios) * num_scales` from the anchor config by default. |
| `anchor_boxes` | Optional fixed multilevel anchor boxes for inference. |

|     |
| --- |
| Returns<br>------- |     |
| RetinaNet model. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.