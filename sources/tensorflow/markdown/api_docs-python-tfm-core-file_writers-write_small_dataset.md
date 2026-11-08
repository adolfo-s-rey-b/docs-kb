[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/file_writers/write_small_dataset#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/file_writers/write_small_dataset)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/file_writers/write_small_dataset?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/file_writers/write_small_dataset#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.file\_writers.write\_small\_dataset Stay organized with collections Save and categorize content based on your preferences.
===================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/file_writers/write_small_dataset#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/file_writers.py#L23-L49)

Writes `examples` to a file at `output_path` with type `file_type`.

tfm.core.file_writers.write_small_dataset(
        examples: Sequence[Union[tf.train.Example, tf.train.SequenceExample]],
        output_path: str,
        file_type: str = 'tfrecord'
    ) -> None

CAVEAT: This function is not recommended for writing large datasets, since it will loop through `examples` and perform write operation sequentially.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `examples` | List of tf.train.Example or tf.train.SequenceExample. |
| `output_path` | Output path for the dataset. |
| `file_type` | A string indicating the file format, could be: 'tfrecord', 'tfrecords', 'tfrecord\_compressed', 'tfrecords\_gzip', 'riegeli'. The string is case insensitive. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.