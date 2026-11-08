[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.maskrcnn\_model.MaskRCNNModel Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/maskrcnn_model.py#L25-L508)

The Mask R-CNN(-RS) and Cascade RCNN-RS models.

#### View aliases

**Main aliases**

[`tfm.vision.models.MaskRCNNModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/maskrcnn_model/MaskRCNNModel)

tfm.vision.maskrcnn_model.MaskRCNNModel(
        backbone: tf_keras.Model,
        decoder: tf_keras.Model,
        rpn_head: tf_keras.layers.Layer,
        detection_head: Union[tf_keras.layers.Layer, List[tf_keras.layers.Layer]],
        roi_generator: tf_keras.layers.Layer,
        roi_sampler: Union[tf_keras.layers.Layer, List[tf_keras.layers.Layer]],
        roi_aligner: tf_keras.layers.Layer,
        detection_generator: tf_keras.layers.Layer,
        mask_head: Optional[tf_keras.layers.Layer] = None,
        mask_sampler: Optional[tf_keras.layers.Layer] = None,
        mask_roi_aligner: Optional[tf_keras.layers.Layer] = None,
        class_agnostic_bbox_pred: bool = False,
        cascade_class_ensemble: bool = False,
        min_level: Optional[int] = None,
        max_level: Optional[int] = None,
        num_scales: Optional[int] = None,
        aspect_ratios: Optional[List[float]] = None,
        anchor_size: Optional[float] = None,
        outer_boxes_scale: float = 1.0,
        **kwargs
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `backbone` | `tf_keras.Model`, the backbone network. |
| `decoder` | `tf_keras.Model`, the decoder network. |
| `rpn_head` | the RPN head. |
| `detection_head` | the detection head or a list of heads. |
| `roi_generator` | the ROI generator. |
| `roi_sampler` | a single ROI sampler or a list of ROI samplers for cascade detection heads. |
| `roi_aligner` | the ROI aligner. |
| `detection_generator` | the detection generator. |
| `mask_head` | the mask head. |
| `mask_sampler` | the mask sampler. |
| `mask_roi_aligner` | the ROI alginer for mask prediction. |
| `class_agnostic_bbox_pred` | if True, perform class agnostic bounding box prediction. Needs to be `True` for Cascade RCNN models. |
| `cascade_class_ensemble` | if True, ensemble classification scores over all detection heads. |
| `min_level` | Minimum level in output feature maps. |
| `max_level` | Maximum level in output feature maps. |
| `num_scales` | A number representing intermediate scales added on each level. For instances, num\_scales=2 adds one additional intermediate anchor scales \[2^0, 2^0.5\] on each level. |
| `aspect_ratios` | A list representing the aspect raito anchors added on each level. The number indicates the ratio of width to height. For instances, aspect\_ratios=\[1.0, 2.0, 0.5\] adds three anchors on each scale level. |
| `anchor_size` | A number representing the scale of size of the base anchor to the feature stride 2^level. |
| `outer_boxes_scale` | a float to scale up the bounding boxes to generate more inclusive masks. The scale is expected to be >=1.0. |
| `**kwargs` | keyword arguments to be passed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/maskrcnn_model.py#L144-L188)

call(
        images: tf.Tensor,
        image_shape: tf.Tensor,
        anchor_boxes: Optional[Mapping[str, tf.Tensor]] = None,
        gt_boxes: Optional[tf.Tensor] = None,
        gt_classes: Optional[tf.Tensor] = None,
        gt_masks: Optional[tf.Tensor] = None,
        gt_outer_boxes: Optional[tf.Tensor] = None,
        training: Optional[bool] = None
    ) -> Mapping[str, Optional[tf.Tensor]]

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