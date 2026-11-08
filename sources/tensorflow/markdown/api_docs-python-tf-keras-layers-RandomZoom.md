[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#used-in-the-notebooks_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#output-shape_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#from_config)
        
    *   [get\_clipped\_bbox](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#get_clipped_bbox)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#get_random_transformation)
        
    *   [get\_transformed\_x\_y](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#get_transformed_x_y)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.RandomZoom Stay organized with collections Save and categorize content based on your preferences.
=================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#used-in-the-notebooks_1)
    
*   [Input shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#input-shape_1)
    
*   [Output shape](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#output-shape_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#args_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#from_config)
        
    *   [get\_clipped\_bbox](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#get_clipped_bbox)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#get_random_transformation)
        
    *   [get\_transformed\_x\_y](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#get_transformed_x_y)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L16-L420)

A preprocessing layer which randomly zooms images during training.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.RandomZoom(
        height_factor,
        width_factor=None,
        fill_mode='reflect',
        interpolation='bilinear',
        seed=None,
        fill_value=0.0,
        data_format=None,
        **kwargs
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers) | *   [Image classification](https://www.tensorflow.org/tutorials/images/classification)<br>    <br>*   [Retraining an Image Classifier](https://www.tensorflow.org/hub/tutorials/tf2_image_retraining) |

This layer will randomly zoom in or out on each axis of an image independently, filling empty space according to `fill_mode`.

Input pixel values can be of any range (e.g. `[0., 1.)` or `[0, 255]`) and of integer or floating point dtype. By default, the layer will output floats.\
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
| `height_factor` | a float represented as fraction of value, or a tuple of size 2 representing lower and upper bound for zooming vertically. When represented as a single float, this value is used for both the upper and lower bound. A positive value means zooming out, while a negative value means zooming in. For instance, `height_factor=(0.2, 0.3)` result in an output zoomed out by a random amount in the range `[+20%, +30%]`. `height_factor=(-0.3, -0.2)` result in an output zoomed in by a random amount in the range `[+20%, +30%]`. |\
| `width_factor` | a float represented as fraction of value, or a tuple of size 2 representing lower and upper bound for zooming horizontally. When represented as a single float, this value is used for both the upper and lower bound. For instance, `width_factor=(0.2, 0.3)` result in an output zooming out between 20% to 30%. `width_factor=(-0.3, -0.2)` result in an output zooming in between 20% to 30%. `None` means i.e., zooming vertical and horizontal directions by preserving the aspect ratio. Defaults to `None`. |\
| `fill_mode` | Points outside the boundaries of the input are filled according to the given mode. Available methods are `"constant"`, `"nearest"`, `"wrap"` and `"reflect"`. Defaults to `"reflect"`.<br><br>*   `"reflect"`: `(d c b a \| a b c d \| d c b a)` The input is extended by reflecting about the edge of the last pixel.<br>*   `"constant"`: `(k k k k \| a b c d \| k k k k)` The input is extended by filling all values beyond the edge with the same constant value k specified by `fill_value`.<br>*   `"wrap"`: `(a b c d \| a b c d \| a b c d)` The input is extended by wrapping around to the opposite edge.<br>*   `"nearest"`: `(a a a a \| a b c d \| d d d d)` The input is extended by the nearest pixel. Note that when using torch backend, `"reflect"` is redirected to `"mirror"` `(c d c b \| a b c d \| c b a b)` because torch does not support `"reflect"`. Note that torch backend does not support `"wrap"`. |\
| `interpolation` | Interpolation mode. Supported values: `"nearest"`, `"bilinear"`. |\
| `seed` | Integer. Used to create a random seed. |\
| `fill_value` | a float that represents the value to be filled outside the boundaries when `fill_mode="constant"`. |\
| `data_format` | string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, height, width, channels)` while `"channels_first"` corresponds to inputs with shape `(batch, channels, height, width)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`. |\
| `**kwargs` | Base layer keyword arguments, such as `name` and `dtype`. |\
\
#### Example:\
\
    input_img = np.random.random((32, 224, 224, 3))\
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
### `get_clipped_bbox`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L192-L209)\
\
get_clipped_bbox(\
        bounding_boxes, h_end, h_start, w_end, w_start\
    )\
\
### `get_random_transformation`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L301-L341)\
\
get_random_transformation(\
        data, training=True, seed=None\
    )\
\
### `get_transformed_x_y`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L182-L190)\
\
get_transformed_x_y(\
        x, y, transform\
    )\
\
### `transform_bounding_boxes`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L211-L299)\
\
transform_bounding_boxes(\
        bounding_boxes, transformation, training=True\
    )\
\
### `transform_images`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L64-L70)\
\
transform_images(\
        images, transformation, training=True\
    )\
\
### `transform_labels`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_zoom.py#L179-L180)\
\
transform_labels(\
        labels, transformation, training=True\
    )\
\
### `transform_segmentation_masks`\
\
[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L83-L90)\
\
transform_segmentation_masks(\
        segmentation_masks, transformation, training=True\
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