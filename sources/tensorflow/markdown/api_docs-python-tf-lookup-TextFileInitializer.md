[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#methods)
    *   [initialize](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#initialize)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.lookup.TextFileInitializer Stay organized with collections Save and categorize content based on your preferences.
====================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#methods)
    *   [initialize](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer#initialize)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L609-L813)

Table initializers from a text file.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.lookup.TextFileInitializer`](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileInitializer)

tf.lookup.TextFileInitializer(
        filename,
        key_dtype,
        key_index,
        value_dtype,
        value_index,
        vocab_size=None,
        delimiter='\t',
        name=None,
        value_index_offset=0
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer) |

This initializer assigns one entry in the table for each line in the file.

The key and value type of the table to initialize is given by `key_dtype` and `value_dtype`.

The key and value content to get from each line is specified by the `key_index` and `value_index`.

*   [`TextFileIndex.LINE_NUMBER`](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileIndex#LINE_NUMBER)
     means use the line number starting from zero, expects data type int64.
*   [`TextFileIndex.WHOLE_LINE`](https://www.tensorflow.org/api_docs/python/tf/lookup/TextFileIndex#WHOLE_LINE)
     means use the whole line content, expects data type string.
*   A value `>=0` means use the index (starting at zero) of the split line based on `delimiter`.

For example if we have a file with the following content:

    import tempfile

The following snippet initializes a table with the first column as keys and second column as values:

*   `emerson -> 10`
*   `lake -> 20`
*   `palmer -> 30`

    init= tf.lookup.TextFileInitializer(

Similarly to initialize the whole line as keys and the line number as values.

*   `emerson 10 -> 0`
*   `lake 20 -> 1`
*   `palmer 30 -> 2`

    init = tf.lookup.TextFileInitializer(

|     |     |
| --- | --- |
| Args<br>---- |     |
| `filename` | The filename of the text file to be used for initialization. The path must be accessible from wherever the graph is initialized (eg. trainer or eval workers). The filename may be a scalar `Tensor`. |
| `key_dtype` | The `key` data type. |
| `key_index` | the index that represents information of a line to get the table 'key' values from. |
| `value_dtype` | The `value` data type. |
| `value_index` | the index that represents information of a line to get the table 'value' values from.' |
| `vocab_size` | The number of elements in the file, if known. |
| `delimiter` | The delimiter to separate fields in a line. |
| `name` | A name for the operation (optional). |
| `value_index_offset` | A number to add to all indices extracted from the file This is useful for cases where a user would like to reserve one or more low index values for control characters. For instance, if you would like to ensure that no vocabulary item is mapped to index 0 (so you can reserve 0 for a masking value), you can set value\_index\_offset to 1; this will mean that the first vocabulary element is mapped to 1 instead of 0. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | when the filename is empty, or when the table key and value data types do not match the expected data types. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `key_dtype` | The expected table key dtype. |
| `value_dtype` | The expected table value dtype. |

Methods
-------

### `initialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L760-L787)

initialize(
        table
    )

Initializes the table from a text file.

|     |     |
| --- | --- |
| Args |     |
| `table` | The table to be initialized. |

|     |
| --- |
| Returns |     |
| The operation that initializes the table. |     |

|     |     |
| --- | --- |
| Raises |     |
| `TypeError` | when the keys and values data types do not match the table key and value data types. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.