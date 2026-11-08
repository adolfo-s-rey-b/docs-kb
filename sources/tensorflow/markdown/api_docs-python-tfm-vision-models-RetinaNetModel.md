[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.models.RetinaNetModel Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/retinanet_model.py#L24-L252)

The RetinaNet model class.

#### View aliases

**Main aliases**

[`tfm.vision.retinanet_model.RetinaNetModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/models/RetinaNetModel)

tfm.vision.models.RetinaNetModel(
        backbone: tf_keras.Model,
        decoder: tf_keras.Model,
        head: tf_keras.layers.Layer,
        detection_generator: tf_keras.layers.Layer,
        anchor_boxes: (Mapping[str, tf.Tensor] | None) = None,
        min_level: Optional[int] = None,
        max_level: Optional[int] = None,
        num_scales: Optional[int] = None,
        aspect_ratios: Optional[List[float]] = None,
        anchor_size: Optional[float] = None,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `backbone` | `tf_keras.Model` a backbone network. |
| `decoder` | `tf_keras.Model` a decoder network. |
| `head` | `RetinaNetHead`, the RetinaNet head. |
| `detection_generator` | the detection generator. |
| `anchor_boxes` | a dict of tensors which includes multilevel anchors.<br><br>*   key: `str`, the level of the multilevel predictions.<br>*   values: `Tensor`, the anchor coordinates of a particular feature level, whose shape is \[height\_l, width\_l, 4 \* num\_anchors\_per\_location\_l\]. If provided, these anchors will be used for inference (training=False). |
| `min_level` | Minimum level in output feature maps. |
| `max_level` | Maximum level in output feature maps. |
| `num_scales` | A number representing intermediate scales added on each level. For instances, num\_scales=2 adds one additional intermediate anchor scales \[2^0, 2^0.5\] on each level. |
| `aspect_ratios` | A list representing the aspect raito anchors added on each level. The number indicates the ratio of width to height. For instances, aspect\_ratios=\[1.0, 2.0, 0.5\] adds three anchors on each scale level. |
| `anchor_size` | A number representing the scale of size of the base anchor to the feature stride 2^level. |
| `**kwargs` | keyword arguments to be passed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `anchor_boxes` |     |
| `backbone` |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |
| `decoder` |     |
| `detection_generator` |     |
| `head` |     |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/retinanet_model.py#L84-L215)

call(
        images: Union[tf.Tensor, Sequence[tf.Tensor]],
        image_shape: Optional[tf.Tensor] = None,
        anchor_boxes: (Mapping[str, tf.Tensor] | None) = None,
        output_intermediate_features: bool = False,
        training: bool = None
    ) -> Mapping[str, tf.Tensor]

Forward pass of the RetinaNet model.

|     |     |
| --- | --- |
| Args |     |
| `images` | `Tensor` or a sequence of `Tensor`, the input batched images to the backbone network, whose shape(s) is \[batch, height, width, 3\]. If it is a sequence of `Tensor`, we will assume the anchors are generated based on the shape of the first image(s). |
| `image_shape` | `Tensor`, the actual shape of the input images, whose shape is \[batch, 2\] where the last dimension is \[height, width\]. Note that this is the actual image shape excluding paddings. For example, images in the batch may be resized into different shapes before padding to the fixed size. |
| `anchor_boxes` | the anchor boxes to use for inference (training=False) if not provided in the init. |
| `output_intermediate_features` | `bool` indicating whether to return the intermediate feature maps generated by backbone and decoder. |
| `training` | `bool`, indicating whether it is in training mode. |

|     |     |
| --- | --- |
| Returns |     |
| `scores` | a dict of tensors which includes scores of the predictions.<br><br>*   key: `str`, the level of the multilevel predictions.<br>*   values: `Tensor`, the box scores predicted from a particular feature level, whose shape is \[batch, height\_l, width\_l, num\_classes \* num\_anchors\_per\_location\]. |
| `boxes` | a dict of tensors which includes coordinates of the predictions.*   key: `str`, the level of the multilevel predictions.<br>*   values: `Tensor`, the box coordinates predicted from a particular feature level, whose shape is \[batch, height\_l, width\_l, 4 \* num\_anchors\_per\_location\]. |
| `attributes` | a dict of (attribute\_name, attribute\_predictions). Each attribute prediction is a dict that includes:*   key: `str`, the level of the multilevel predictions.<br>*   values: `Tensor`, the attribute predictions from a particular feature level, whose shape is \[batch, height\_l, width\_l, att\_size \* num\_anchors\_per\_location\]. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.