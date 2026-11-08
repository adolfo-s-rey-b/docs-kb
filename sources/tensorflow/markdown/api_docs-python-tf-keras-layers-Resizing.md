[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FResizing%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#used-in-the-notebooks_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#output-shape_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.Resizing Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#used-in-the-notebooks_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#output-shape_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Resizing?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/resizing.py#L15-L325)

A preprocessing layer which resizes images.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.Resizing(
        height,
        width,
        interpolation='bilinear',
        crop_to_aspect_ratio=False,
        pad_to_aspect_ratio=False,
        fill_mode='constant',
        fill_value=0.0,
        antialias=False,
        data_format=None,
        **kwargs
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Data augmentation](https://www.tensorflow.org/tutorials/images/data_augmentation) |

This layer resizes an image input to a target height and width. The input should be a 4D (batched) or 3D (unbatched) tensor in `"channels_last"` format. Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`).\
\
|     |     |\
| --- | --- |\
| Input shape<br>----------- |     |\
| `3D` | `unbatched) or 4D (batched) tensor with shape`<br><br>`(..., height, width, channels)`, in `"channels_last"` format, or `(..., channels, height, width)`, in `"channels_first"` format. |\
\
|     |     |\
| --- | --- |\
| Output shape<br>------------ |     |\
| `3D` | `unbatched) or 4D (batched) tensor with shape`<br><br>`(..., target_height, target_width, channels)`, or `(..., channels, target_height, target_width)`, in `"channels_first"` format. |\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `height` | Integer, the height of the output shape. |\
| `width` | Integer, the width of the output shape. |\
| `interpolation` | String, the interpolation method. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"lanczos3"`, `"lanczos5"`. Defaults to `"bilinear"`. |\
| `crop_to_aspect_ratio` | If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `(height, width)`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved. |\
| `pad_to_aspect_ratio` | If `True`, pad the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be evenly padded on the short side. |\
| `fill_mode` | When using `pad_to_aspect_ratio=True`, padded areas are filled according to the given mode. Only `"constant"` is supported at this time (fill with constant value, equal to `fill_value`). |\
| `fill_value` | Float. Padding value to use when `pad_to_aspect_ratio=True`. |\
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |\
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |\
\
#### Example:\
\
(x_train, y_train), _ = keras.datasets.cifar10.load_data()\
    image = x_train[0]\
    resizer = keras.layers.Resizing(128, 128)\
    resized_image = resizer(image)\
    print("original:", image.shape, "resized:", resized_image.shape)\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |\
\
Methods\
-------\
\
### `convert_weight`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)\
\
convert_weight(\
        weight\
    )\
\
Convert the weight if it is from the a different backend.\
\
### `from_config`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)\
\
@classmethod\
\
Creates an operation from its config.\
\
This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.\
\
if "dtype" in config and isinstance(config["dtype"], dict):\
        policy = dtype_policies.deserialize(config["dtype"])\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `config` | A Python dictionary, typically the output of `get_config`. |\
\
|     |\
| --- |\
| Returns |     |\
| An operation instance. |     |\
\
### `get_random_transformation`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/resizing.py#L147-L158)\
\
get_random_transformation(\
        data, training=True, seed=None\
    )\
\
### `transform_bounding_boxes`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/resizing.py#L160-L208)\
\
transform_bounding_boxes(\
        bounding_boxes, transformation, training=True\
    )\
\
### `transform_images`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/resizing.py#L132-L135)\
\
transform_images(\
        images, transformation=None, training=True\
    )\
\
### `transform_labels`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/resizing.py#L144-L145)\
\
transform_labels(\
        labels, transformation=None, training=True\
    )\
\
### `transform_segmentation_masks`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/resizing.py#L137-L142)\
\
transform_segmentation_masks(\
        segmentation_masks, transformation=None, training=True\
    )\
\
### `transform_single_bounding_box`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L106-L119)\
\
transform_single_bounding_box(\
        bounding_box, transformation, training=True\
    )\
\
### `transform_single_image`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L92-L97)\
\
transform_single_image(\
        image, transformation, training=True\
    )\
\
### `transform_single_label`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L99-L104)\
\
transform_single_label(\
        label, transformation, training=True\
    )\
\
### `transform_single_segmentation_mask`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L121-L130)\
\
transform_single_segmentation_mask(\
        segmentation_mask, transformation, training=True\
    )\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.