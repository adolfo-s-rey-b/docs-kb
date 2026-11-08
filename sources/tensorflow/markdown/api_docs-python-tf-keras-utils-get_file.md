[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2Fget_file&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.get\_file Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/keras/utils/get_file#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/file_utils.py#L213-L430)

Downloads a file from a URL if it not already in the cache.

tf.keras.utils.get_file(
        fname=None,
        origin=None,
        untar=False,
        md5_hash=None,
        file_hash=None,
        cache_subdir='datasets',
        hash_algorithm='auto',
        extract=False,
        archive_format='auto',
        cache_dir=None,
        force_download=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [tf.data: Build TensorFlow input pipelines](https://www.tensorflow.org/guide/data)<br>    <br>*   [Using the SavedModel format](https://www.tensorflow.org/guide/saved_model)<br>    <br>*   [Estimators](https://www.tensorflow.org/guide/estimator)<br>    <br>*   [Migrating your TFLite code to TF2](https://www.tensorflow.org/guide/migrate/tflite)<br>    <br>*   [Using Counterfactual Logit Pairing with Keras](https://www.tensorflow.org/responsible_ai/model_remediation/counterfactual/guide/counterfactual_keras) | *   [Transfer learning with TensorFlow Hub](https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub)<br>    <br>*   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [Transfer learning with YAMNet for environmental sound classification](https://www.tensorflow.org/tutorials/audio/transfer_learning_audio)<br>    <br>*   [Premade Estimators](https://www.tensorflow.org/tutorials/estimator/premade)<br>    <br>*   [Neural style transfer](https://www.tensorflow.org/tutorials/generative/style_transfer) |

By default the file at the url `origin` is downloaded to the cache\_dir `~/.keras`, placed in the cache\_subdir `datasets`, and given the filename `fname`. The final location of a file `example.txt` would therefore be `~/.keras/datasets/example.txt`. Files in `.tar`, `.tar.gz`, `.tar.bz`, and `.zip` formats can also be extracted.

Passing a hash will verify the file after download. The command line programs `shasum` and `sha256sum` can compute the hash.

#### Example:

path_to_downloaded_file = get_file(
        origin="https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",
        extract=True
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `fname` | If the target is a single file, this is your desired local name for the file. If `None`, the name of the file at `origin` will be used. If downloading and extracting a directory archive, the provided `fname` will be used as extraction directory name (only if it doesn't have an extension). |
| `origin` | Original URL of the file. |
| `untar` | Deprecated in favor of `extract` argument. Boolean, whether the file is a tar archive that should be extracted. |
| `md5_hash` | Deprecated in favor of `file_hash` argument. md5 hash of the file for file integrity verification. |
| `file_hash` | The expected hash string of the file after download. The sha256 and md5 hash algorithms are both supported. |
| `cache_subdir` | Subdirectory under the Keras cache dir where the file is saved. If an absolute path, e.g. `"/path/to/folder"` is specified, the file will be saved at that location. |
| `hash_algorithm` | Select the hash algorithm to verify the file. options are `"md5'`, `"sha256'`, and `"auto'`. The default 'auto' detects the hash algorithm in use. |
| `extract` | If `True`, extracts the archive. Only applicable to compressed archive files like tar or zip. |
| `archive_format` | Archive format to try for extracting the file. Options are `"auto'`, `"tar'`, `"zip'`, and `None`. `"tar"` includes tar, tar.gz, and tar.bz files. The default `"auto"` corresponds to `["tar", "zip"]`. None or an empty list will return no matches found. |
| `cache_dir` | Location to store cached files, when None it defaults ether `$KERAS_HOME` if the `KERAS_HOME` environment variable is set or `~/.keras/`. |
| `force_download` | If `True`, the file will always be re-downloaded regardless of the cache state. |

|     |
| --- |
| Returns<br>------- |     |
| Path to the downloaded file. |     |

**⚠️ Warning on malicious downloads ⚠️**

Downloading something from the Internet carries a risk. NEVER download a file/archive if you do not trust the source. We recommend that you specify the `file_hash` argument (if the hash of the source file is known) to make sure that the file you are getting is the one you expect.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.