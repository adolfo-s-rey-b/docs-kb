[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fbounding_boxes%2Fcompute_iou&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.bounding\_boxes.compute\_iou Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/bounding_boxes/compute_iou#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/bounding_boxes/iou.py#L55-L173)

Computes a lookup table vector containing the ious for a given set boxes.

tf.keras.utils.bounding_boxes.compute_iou(
        boxes1,
        boxes2,
        bounding_box_format,
        use_masking=False,
        mask_val=-1,
        image_shape=None
    )

The lookup vector is to be indexed by \[`boxes1_index`,`boxes2_index`\] if boxes are unbatched and by \[`batch`, `boxes1_index`,`boxes2_index`\] if the boxes are batched.

The users can pass `boxes1` and `boxes2` to be different ranks. For example:

1) `boxes1`: \[batch\_size, M, 4\], `boxes2`: \[batch\_size, N, 4\] -> return \[batch\_size, M, N\]. 2) `boxes1`: \[batch\_size, M, 4\], `boxes2`: \[N, 4\] -> return \[batch\_size, M, N\] 3) `boxes1`: \[M, 4\], `boxes2`: \[batch\_size, N, 4\] -> return \[batch\_size, M, N\] 4) `boxes1`: \[M, 4\], `boxes2`: \[N, 4\] -> return \[M, N\]

|     |     |
| --- | --- |
| Args<br>---- |     |
| `boxes1` | a list of bounding boxes in 'corners' format. Can be batched or unbatched. |
| `boxes2` | a list of bounding boxes in 'corners' format. Can be batched or unbatched. |
| `bounding_box_format` | a case-insensitive string which is one of `"xyxy"`, `"rel_xyxy"`, `"xyWH"`, `"center_xyWH"`, `"yxyx"`, `"rel_yxyx"`. For detailed information on the supported format, see the |
| `use_masking` | whether masking will be applied. This will mask all `boxes1` or `boxes2` that have values less than 0 in all its 4 dimensions. Default to `False`. |
| `mask_val` | int to mask those returned IOUs if the masking is True, defaults to -1. |
| `image_shape` | `Tuple[int]`. The shape of the image (height, width, 3). When using relative bounding box format for `box_format` the `image_shape` is used for normalization. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `iou_lookup_table` | a vector containing the pairwise ious of boxes1 and boxes2. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.