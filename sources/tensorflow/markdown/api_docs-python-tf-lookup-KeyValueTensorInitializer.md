[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Flookup%2FKeyValueTensorInitializer&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#methods)
    *   [initialize](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#initialize)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.lookup.KeyValueTensorInitializer Stay organized with collections Save and categorize content based on your preferences.
==========================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#methods)
    *   [initialize](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer#initialize)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L521-L586)

Table initializers given `keys` and `values` tensors.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.lookup.KeyValueTensorInitializer`](https://www.tensorflow.org/api_docs/python/tf/lookup/KeyValueTensorInitializer)

tf.lookup.KeyValueTensorInitializer(
        keys, values, key_dtype=None, value_dtype=None, name=None
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [BERT Preprocessing with TF Text](https://www.tensorflow.org/text/guide/bert_preprocessing_guide)<br>    <br>*   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer) | *   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [Federated Learning for Text Generation](https://www.tensorflow.org/federated/tutorials/federated_learning_for_text_generation)<br>    <br>*   [Apache ORC Reader](https://www.tensorflow.org/io/tutorials/orc)<br>    <br>*   [Feature Engineering using TFX Pipeline and TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/tfx/penguin_tft)<br>    <br>*   [Preprocessing data with TensorFlow Transform](https://www.tensorflow.org/tfx/tutorials/transform/census) |

    keys_tensor = tf.constant(['a', 'b', 'c'])

|     |     |
| --- | --- |
| Args<br>---- |     |
| `keys` | The tensor for the keys. |
| `values` | The tensor for the values. |
| `key_dtype` | The `keys` data type. Used when `keys` is a python array. |
| `value_dtype` | The `values` data type. Used when `values` is a python array. |
| `name` | A name for the operation (optional). |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `key_dtype` | The expected table key dtype. |
| `value_dtype` | The expected table value dtype. |

Methods
-------

### `initialize`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L567-L586)

initialize(
        table
    )

Initializes the given `table` with `keys` and `values` tensors.

|     |     |
| --- | --- |
| Args |     |
| `table` | The table to initialize. |

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