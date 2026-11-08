[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#call)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.models.SegmentationModel Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#methods)
    *   [call](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel#call)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/segmentation_model.py#L23-L94)

A Segmentation class model.

#### View aliases

**Main aliases**

[`tfm.vision.segmentation_model.SegmentationModel`](https://www.tensorflow.org/api_docs/python/tfm/vision/models/SegmentationModel)

tfm.vision.models.SegmentationModel(
        backbone: tf_keras.Model,
        decoder: tf_keras.Model,
        head: tf_keras.layers.Layer,
        mask_scoring_head: Optional[tf_keras.layers.Layer] = None,
        **kwargs
    )

Input images are passed through backbone first. Decoder network is then applied, and finally, segmentation head is applied on the output of the decoder network. Layers such as ASPP should be part of decoder. Any feature fusion is done as part of the segmentation head (i.e. deeplabv3+ feature fusion is not part of the decoder, instead it is part of the segmentation head). This way, different feature fusion techniques can be combined with different backbones, and decoders.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `backbone` | a backbone network. |
| `decoder` | a decoder network. E.g. FPN. |
| `head` | segmentation head. |
| `mask_scoring_head` | mask scoring head. |
| `**kwargs` | keyword arguments to be passed. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `checkpoint_items` | Returns a dictionary of items to be additionally checkpointed. |

Methods
-------

### `call`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/modeling/segmentation_model.py#L61-L76)

call(
        inputs: tf.Tensor, training: bool = None
    ) -> Dict[str, tf.Tensor]

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