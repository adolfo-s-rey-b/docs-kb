[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Flayers%2FRandomGaussianBlur%3Fversion%3Dstable&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_segmentation_mask)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.layers.RandomGaussianBlur Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#methods_2)
    *   [convert\_weight](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#convert_weight)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#from_config)
        
    *   [get\_random\_transformation](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#get_random_transformation)
        
    *   [transform\_bounding\_boxes](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_bounding_boxes)
        
    *   [transform\_images](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_images)
        
    *   [transform\_labels](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_labels)
        
    *   [transform\_segmentation\_masks](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_segmentation_masks)
        
    *   [transform\_single\_bounding\_box](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_bounding_box)
        
    *   [transform\_single\_image](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_image)
        
    *   [transform\_single\_label](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_label)
        
    *   [transform\_single\_segmentation\_mask](https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomGaussianBlur?version=stable#transform_single_segmentation_mask)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L11-L227)

Applies random Gaussian blur to images for data augmentation.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.layers.RandomGaussianBlur(
        factor=1.0,
        kernel_size=3,
        sigma=1.0,
        value_range=(0, 255),
        data_format=None,
        seed=None,
        **kwargs
    )

This layer performs a Gaussian blur operation on input images with a
    randomly selected degree of blurring, controlled by the `factor` and
    `sigma` arguments.
    
    Note: This layer is safe to use inside a <a href="../../../tf/data"><code>tf.data</code></a> or `grain` pipeline
    (independently of which backend you're using).
    
    Args:
        factor: A single float or a tuple of two floats.
            `factor` controls the extent to which the image hue is impacted.
            `factor=0.0` makes this layer perform a no-op operation,
            while a value of `1.0` performs the most aggressive
            blurring available. If a tuple is used, a `factor` is
            sampled between the two values for every image augmented. If a
            single float is used, a value between `0.0` and the passed float is
            sampled. Default is 1.0.
        kernel_size: Integer. Size of the Gaussian kernel used for blurring.
            Must be an odd integer. Default is 3.
        sigma: Float or tuple of two floats. Standard deviation of the Gaussian
            kernel. Controls the intensity of the blur. If a tuple is provided,
            a value is sampled between the two for each image. Default is 1.0.
        value_range: the range of values the incoming images will have.
            Represented as a two-number tuple written `[low, high]`. This is
            typically either `[0, 1]` or `[0, 255]` depending on how your
            preprocessing pipeline is set up.
        seed: Integer. Used to create a random seed.
    
    Example:

layer = keras.layers.RandomGaussianBlur(value_range=(0, 255))
    images = np.random.randint(0, 255, (8, 224, 224, 3), dtype="uint8")
    
    labels = keras.ops.one_hot(
        np.array([0, 1, 2, 0, 1, 2, 0, 1]),
        num_classes=3
    )
    
    segmentation_masks = np.random.randint(0, 3, (8, 224, 224, 1), dtype="uint8")
    
    output = layer(
        {
            "images": images,
            "labels": labels,
            "segmentation_masks": segmentation_masks
        },
        training=True
    )

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `convert_weight`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/data_layer.py#L153-L159)

convert_weight(
        weight
    )

Convert the weight if it is from the a different backend.

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/operation.py#L322-L362)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_random_transformation`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L119-L171)

get_random_transformation(
        data, training=True, seed=None
    )

### `transform_bounding_boxes`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L208-L211)

transform_bounding_boxes(
        bounding_boxes, transformation, training=True
    )

### `transform_images`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L173-L198)

transform_images(
        images, transformation=None, training=True
    )

### `transform_labels`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L200-L201)

transform_labels(
        labels, transformation, training=True
    )

### `transform_segmentation_masks`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/random_gaussian_blur.py#L203-L206)

transform_segmentation_masks(
        segmentation_masks, transformation, training=True
    )

### `transform_single_bounding_box`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L106-L119)

transform_single_bounding_box(
        bounding_box, transformation, training=True
    )

### `transform_single_image`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L92-L97)

transform_single_image(
        image, transformation, training=True
    )

### `transform_single_label`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L99-L104)

transform_single_label(
        label, transformation, training=True
    )

### `transform_single_segmentation_mask`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/image_preprocessing/base_image_preprocessing_layer.py#L121-L130)

transform_single_segmentation_mask(
        segmentation_mask, transformation, training=True
    )

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.