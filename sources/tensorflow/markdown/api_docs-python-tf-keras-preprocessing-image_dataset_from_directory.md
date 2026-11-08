[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.image\_dataset\_from\_directory Stay organized with collections Save and categorize content based on your preferences.
=============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/image_dataset_utils.py#L28-L409)

Generates a dataset from image files in a directory.

#### View aliases

**Main aliases**

[`tf.keras.utils.image_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image_dataset_from_directory)

tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        labels='inferred',
        label_mode='int',
        class_names=None,
        color_mode='rgb',
        batch_size=32,
        image_size=(256, 256),
        shuffle=True,
        seed=None,
        validation_split=None,
        subset=None,
        interpolation='bilinear',
        follow_links=False,
        crop_to_aspect_ratio=False,
        pad_to_aspect_ratio=False,
        data_format=None,
        format='tf',
        verbose=True
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Image classification](https://www.tensorflow.org/tutorials/images/classification)<br>    <br>*   [Transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning)<br>    <br>*   [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)<br>    <br>*   [Load and preprocess images](https://www.tensorflow.org/tutorials/load_data/images)<br>    <br>*   [Retraining an Image Classifier](https://www.tensorflow.org/hub/tutorials/tf2_image_retraining) |

If your directory structure is:

main_directory/
    ...class_a/
    ......a_image_1.jpg
    ......a_image_2.jpg
    ...class_b/
    ......b_image_1.jpg
    ......b_image_2.jpg

Then calling `image_dataset_from_directory(main_directory, labels='inferred')` will return a dataset that yields batches of images from the subdirectories `class_a` and `class_b`, together with labels 0 and 1 (0 corresponding to `class_a` and 1 corresponding to `class_b`).

Supported image formats: `.jpeg`, `.jpg`, `.png`, `.bmp`, `.gif`. Animated gifs are truncated to the first frame.

By default, this function will return a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 object. You can set `format="grain"` to return a `grain.IterDataset` object instead, which removes the TensorFlow dependency.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `directory` | Directory where the data is located. If `labels` is `"inferred"`, it should contain subdirectories, each containing images for a class. Otherwise, the directory structure is ignored. |
| `labels` | Either `"inferred"` (labels are generated from the directory structure), `None` (no labels), or a list/tuple of integer labels of the same size as the number of image files found in the directory. Labels should be sorted according to the alphanumeric order of the image file paths (obtained via `os.walk(directory)` in Python). |
| `label_mode` | String describing the encoding of `labels`. Options are:<br><br>*   `"int"`: means that the labels are encoded as integers (e.g. for `sparse_categorical_crossentropy` loss).<br>*   `"categorical"` means that the labels are encoded as a categorical vector (e.g. for `categorical_crossentropy` loss).<br>*   `"binary"` means that the labels (there can be only 2) are encoded as `float32` scalars with values 0 or 1 (e.g. for `binary_crossentropy`).<br>*   `None` (no labels). |
| `class_names` | Only valid if `labels` is `"inferred"`. This is the explicit list of class names (must match names of subdirectories). Used to control the order of the classes (otherwise alphanumerical order is used). |
| `color_mode` | One of `"grayscale"`, `"rgb"`, `"rgba"`. Whether the images will be converted to have 1, 3, or 4 channels. Defaults to `"rgb"`. |
| `batch_size` | Size of the batches of data. Defaults to 32. If `None`, the data will not be batched (the dataset will yield individual samples). |
| `image_size` | Size to resize images to after they are read from disk, specified as `(height, width)`. Since the pipeline processes batches of images that must all have the same size, this must be provided. Defaults to `(256, 256)`. |
| `shuffle` | Whether to shuffle the data. Defaults to `True`. If set to `False`, sorts the data in alphanumeric order. |
| `seed` | Optional random seed for shuffling and transformations. |
| `validation_split` | Optional float between 0 and 1, fraction of data to reserve for validation. |
| `subset` | Subset of the data to return. One of `"training"`, `"validation"`, or `"both"`. Only used if `validation_split` is set. When `subset="both"`, the utility returns a tuple of two datasets (the training and validation datasets respectively). |
| `interpolation` | String, the interpolation method used when resizing images. Supports `"bilinear"`, `"nearest"`, `"bicubic"`, `"area"`, `"lanczos3"`, `"lanczos5"`, `"gaussian"`, `"mitchellcubic"`. Defaults to `"bilinear"`. |
| `follow_links` | Whether to visit subdirectories pointed to by symlinks. Defaults to `False`. |
| `crop_to_aspect_ratio` | If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size `image_size`) that matches the target aspect ratio. By default (`crop_to_aspect_ratio=False`), aspect ratio may not be preserved. |
| `pad_to_aspect_ratio` | If `True`, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be padded so as to return the largest possible window in the image (of size `image_size`) that matches the target aspect ratio. By default (`pad_to_aspect_ratio=False`), aspect ratio may not be preserved. |
| `data_format` | If None uses keras.config.image\_data\_format() otherwise either 'channel\_last' or 'channel\_first'. |
| `format` | The format of the return object. Defaults to `"tf"`. Available options are:*   `"tf"`: returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>     object. Requires TensorFlow to be installed.<br>*   `"grain"`: returns a `grain.IterDataset` object. Requires Grain to be installed. |
| `verbose` | Whether to display number information on classes and number of files found. Defaults to `True`. |

Returns
-------

A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 (`format="tf"`) or `grain.IterDataset` (`format="grain"`) object.

*   If `label_mode` is `None`, it yields `float32` tensors of shape `(batch_size, image_size[0], image_size[1], num_channels)`, encoding images (see below for rules regarding `num_channels`).
*   Otherwise, it yields a tuple `(images, labels)`, where `images` has shape `(batch_size, image_size[0], image_size[1], num_channels)`, and `labels` follows the format described below.

Rules regarding labels format:

*   if `label_mode` is `"int"`, the labels are an `int32` tensor of shape `(batch_size,)`.
*   if `label_mode` is `"binary"`, the labels are a `float32` tensor of 1s and 0s of shape `(batch_size, 1)`.
*   if `label_mode` is `"categorical"`, the labels are a `float32` tensor of shape `(batch_size, num_classes)`, representing a one-hot encoding of the class index.

Rules regarding number of channels in the yielded images:

*   if `color_mode` is `"grayscale"`, there's 1 channel in the image tensors.
*   if `color_mode` is `"rgb"`, there are 3 channels in the image tensors.
*   if `color_mode` is `"rgba"`, there are 4 channels in the image tensors.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.