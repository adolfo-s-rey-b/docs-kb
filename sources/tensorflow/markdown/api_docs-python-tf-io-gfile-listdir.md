[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fio%2Fgfile%2Flistdir&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.gfile.listdir Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/lib/io/file_io.py#L751-L778)

Returns a list of entries contained within a directory.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.io.gfile.listdir`](https://www.tensorflow.org/api_docs/python/tf/io/gfile/listdir)

tf.io.gfile.listdir(
        path
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Simple audio recognition: Recognizing keywords](https://www.tensorflow.org/tutorials/audio/simple_audio)<br>    <br>*   [Fine-tuning a BERT model](https://www.tensorflow.org/tfmodels/nlp/fine_tune_bert)<br>    <br>*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit/index)<br>    <br>*   [Text Searcher with TensorFlow Lite Model Maker](https://www.tensorflow.org/lite/models/modify/model_maker/text_searcher) |

The list is in arbitrary order. It does not contain the special entries "." and "..".

|     |     |
| --- | --- |
| Args<br>---- |     |
| `path` | string, path to a directory |

|     |
| --- |
| Returns<br>------- |     |
| \[filename1, filename2, ... filenameN\] as strings |     |

|     |
| --- |
| Raises<br>------ |     |
| errors.NotFoundError if directory doesn't exist |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.