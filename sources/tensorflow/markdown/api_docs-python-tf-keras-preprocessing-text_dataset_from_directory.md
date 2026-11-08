[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.preprocessing.text\_dataset\_from\_directory Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/text_dataset_utils.py#L10-L294)

Generates a dataset from text files in a directory.

#### View aliases

**Main aliases**

[`tf.keras.utils.text_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text_dataset_from_directory)

tf.keras.preprocessing.text_dataset_from_directory(
        directory,
        labels='inferred',
        label_mode='int',
        class_names=None,
        batch_size=32,
        max_length=None,
        shuffle=True,
        seed=None,
        validation_split=None,
        subset=None,
        follow_links=False,
        format='tf',
        verbose=True
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Basic text classification](https://www.tensorflow.org/tutorials/keras/text_classification)<br>    <br>*   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [Classify text with BERT](https://www.tensorflow.org/text/tutorials/classify_text_with_bert)<br>    <br>*   [Warm-start embedding layer matrix](https://www.tensorflow.org/text/tutorials/warmstart_embedding_matrix)<br>    <br>*   [Word embeddings](https://www.tensorflow.org/text/tutorials/word_embeddings) |

If your directory structure is:

main_directory/
    ...class_a/
    ......a_text_1.txt
    ......a_text_2.txt
    ...class_b/
    ......b_text_1.txt
    ......b_text_2.txt

Then calling `text_dataset_from_directory(main_directory, labels='inferred')` will return a dataset that yields batches of texts from the subdirectories `class_a` and `class_b`, together with labels 0 and 1 (0 corresponding to `class_a` and 1 corresponding to `class_b`).

Only `.txt` files are supported at this time.

By default, this function will return a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 object. You can set `format="grain"` to return a `grain.IterDataset` object instead, which removes the TensorFlow dependency.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `directory` | Directory where the data is located. If `labels` is `"inferred"`, it should contain subdirectories, each containing text files for a class. Otherwise, the directory structure is ignored. |
| `labels` | Either `"inferred"` (labels are generated from the directory structure), `None` (no labels), or a list/tuple of integer labels of the same size as the number of text files found in the directory. Labels should be sorted according to the alphanumeric order of the text file paths (obtained via `os.walk(directory)` in Python). |
| `label_mode` | String describing the encoding of `labels`. Options are:<br><br>*   `"int"`: means that the labels are encoded as integers (e.g. for `sparse_categorical_crossentropy` loss).<br>*   `"categorical"` means that the labels are encoded as a categorical vector (e.g. for `categorical_crossentropy` loss).<br>*   `"binary"` means that the labels (there can be only 2) are encoded as `float32` scalars with values 0 or 1 (e.g. for `binary_crossentropy`).<br>*   `None` (no labels). |
| `class_names` | Only valid if `"labels"` is `"inferred"`. This is the explicit list of class names (must match names of subdirectories). Used to control the order of the classes (otherwise alphanumerical order is used). |
| `batch_size` | Size of the batches of data. If `None`, the data will not be batched (the dataset will yield individual samples). Defaults to `32`. |
| `max_length` | Maximum size of a text string. Texts longer than this will be truncated to `max_length`. |
| `shuffle` | Whether to shuffle the data. If set to `False`, sorts the data in alphanumeric order. Defaults to `True`. |
| `seed` | Optional random seed for shuffling and transformations. |
| `validation_split` | Optional float between 0 and 1, fraction of data to reserve for validation. |
| `subset` | Subset of the data to return. One of `"training"`, `"validation"` or `"both"`. Only used if `validation_split` is set. When `subset="both"`, the utility returns a tuple of two datasets (the training and validation datasets respectively). |
| `follow_links` | Whether to visits subdirectories pointed to by symlinks. Defaults to `False`. |
| `format` | The format of the return object. Defaults to `"tf"`. Available options are:*   `"tf"`: returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br>     object. Requires TensorFlow to be installed.<br>*   `"grain"`: returns a `grain.IterDataset` object. Requires Grain to be installed. |
| `verbose` | Whether to display number information on classes and number of files found. Defaults to `True`. |

Returns
-------

A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 (`format="tf"`) or `grain.IterDataset` (`format="grain"`) object.

When `format="tf"`:

*   If `label_mode` is `None`, it yields `string` tensors of shape `(batch_size,)`, containing the contents of a batch of text files.
*   Otherwise, it yields a tuple `(texts, labels)`, where `texts` has shape `(batch_size,)` and `labels` follows the format described below.

When `format="grain"`:

*   If `label_mode` is `None`, it yields a list of Python strings containing the contents of a batch of text files.
*   Otherwise, it yields a tuple `(texts, labels)`, where `texts` is a list of Python strings and `labels` follows the format described below.

Rules regarding labels format:

*   if `label_mode` is `int`, the labels are an `int32` tensor of shape `(batch_size,)`.
*   if `label_mode` is `binary`, the labels are a `float32` tensor of 1s and 0s of shape `(batch_size, 1)`.
*   if `label_mode` is `categorical`, the labels are a `float32` tensor of shape `(batch_size, num_classes)`, representing a one-hot encoding of the class index.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.