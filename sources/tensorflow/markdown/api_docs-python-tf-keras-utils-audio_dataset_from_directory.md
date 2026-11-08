[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Faudio_dataset_from_directory%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#returns_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.audio\_dataset\_from\_directory Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#used-in-the-notebooks_1)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/audio_dataset_from_directory?version=stable#returns_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/audio_dataset_utils.py#L11-L254)

Generates a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 from audio files in a directory.

tf.keras.utils.audio_dataset_from_directory(
        directory,
        labels='inferred',
        label_mode='int',
        class_names=None,
        batch_size=32,
        sampling_rate=None,
        output_sequence_length=None,
        ragged=False,
        shuffle=True,
        seed=None,
        validation_split=None,
        subset=None,
        follow_links=False,
        verbose=True
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio) |

If your directory structure is:

main_directory/
    ...class_a/
    ......a_audio_1.wav
    ......a_audio_2.wav
    ...class_b/
    ......b_audio_1.wav
    ......b_audio_2.wav

Then calling `audio_dataset_from_directory(main_directory, labels='inferred')` will return a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 that yields batches of audio files from the subdirectories `class_a` and `class_b`, together with labels 0 and 1 (0 corresponding to `class_a` and 1 corresponding to `class_b`).

Only `.wav` files are supported at this time.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `directory` | Directory where the data is located. If `labels` is `"inferred"`, it should contain subdirectories, each containing audio files for a class. Otherwise, the directory structure is ignored. |
| `labels` | Either "inferred" (labels are generated from the directory structure), `None` (no labels), or a list/tuple of integer labels of the same size as the number of audio files found in the directory. Labels should be sorted according to the alphanumeric order of the audio file paths (obtained via `os.walk(directory)` in Python). |
| `label_mode` | String describing the encoding of `labels`. Options are:<br><br>*   `"int"`: means that the labels are encoded as integers (e.g. for `sparse_categorical_crossentropy` loss).<br>*   `"categorical"` means that the labels are encoded as a categorical vector (e.g. for `categorical_crossentropy` loss)<br>*   `"binary"` means that the labels (there can be only 2) are encoded as `float32` scalars with values 0 or 1 (e.g. for `binary_crossentropy`).<br>*   `None` (no labels). |
| `class_names` | Only valid if "labels" is `"inferred"`. This is the explicit list of class names (must match names of subdirectories). Used to control the order of the classes (otherwise alphanumerical order is used). |
| `batch_size` | Size of the batches of data. Default: 32. If `None`, the data will not be batched (the dataset will yield individual samples). |
| `sampling_rate` | Audio sampling rate (in samples per second). |
| `output_sequence_length` | Maximum length of an audio sequence. Audio files longer than this will be truncated to `output_sequence_length`. If set to `None`, then all sequences in the same batch will be padded to the length of the longest sequence in the batch. |
| `ragged` | Whether to return a Ragged dataset (where each sequence has its own length). Defaults to `False`. |
| `shuffle` | Whether to shuffle the data. If set to `False`, sorts the data in alphanumeric order. Defaults to `True`. |
| `seed` | Optional random seed for shuffling and transformations. |
| `validation_split` | Optional float between 0 and 1, fraction of data to reserve for validation. |
| `subset` | Subset of the data to return. One of `"training"`, `"validation"` or `"both"`. Only used if `validation_split` is set. |
| `follow_links` | Whether to visits subdirectories pointed to by symlinks. Defaults to `False`. |
| `verbose` | Whether to display number information on classes and number of files found. Defaults to `True`. |

Returns
-------

A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 object.

*   If `label_mode` is `None`, it yields `string` tensors of shape `(batch_size,)`, containing the contents of a batch of audio files.
*   Otherwise, it yields a tuple `(audio, labels)`, where `audio` has shape `(batch_size, sequence_length, num_channels)` and `labels` follows the format described below.

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