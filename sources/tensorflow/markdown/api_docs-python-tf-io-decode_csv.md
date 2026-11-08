[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.io.decode\_csv Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/io/decode_csv#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/parsing_ops.py#L1061-L1116)

Convert CSV records to tensors. Each column maps to one tensor.

tf.io.decode_csv(
        records,
        record_defaults,
        field_delim=',',
        use_quote_delim=True,
        na_value='',
        select_cols=None,
        name=None
    )

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [Load CSV data](https://www.tensorflow.org/tutorials/load_data/csv)<br>    <br>*   [Robust machine learning on streaming data using Kafka and Tensorflow-IO](https://www.tensorflow.org/io/tutorials/kafka) |

RFC 4180 format is expected for the CSV records. ([https://tools.ietf.org/html/rfc4180](https://tools.ietf.org/html/rfc4180)
) Note that we allow leading and trailing spaces with int or float field.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `records` | A `Tensor` of type `string`. Each string is a record/row in the csv and all records should have the same format. |
| `record_defaults` | A list of `Tensor` objects with specific types. Acceptable types are `float32`, `float64`, `int32`, `int64`, `string`. One tensor per column of the input record, with either a scalar default value for that column or an empty vector if the column is required. |
| `field_delim` | An optional `string`. Defaults to `","`. char delimiter to separate fields in a record. |
| `use_quote_delim` | An optional `bool`. Defaults to `True`. If false, treats double quotation marks as regular characters inside of the string fields (ignoring RFC 4180, Section 2, Bullet 5). |
| `na_value` | Additional string to recognize as NA/NaN. |
| `select_cols` | Optional sorted list of column indices to select. If specified, only this subset of columns will be parsed and returned. It only works on `records` except for `record_defaults`. |
| `name` | A name for the operation (optional). |

|     |
| --- |
| Returns<br>------- |     |
| A list of `Tensor` objects. Has the same type as `record_defaults`. Each tensor will have the same shape as records. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If any of the arguments is malformed. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.