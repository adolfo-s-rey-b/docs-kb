[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#methods)
    *   [lookup](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#lookup)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#size)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#__getitem__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.lookup.StaticVocabularyTable Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#used-in-the-notebooks)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#raises)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#methods)
    *   [lookup](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#lookup)
        
    *   [size](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#size)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tf/lookup/StaticVocabularyTable#__getitem__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1190-L1408)

String to Id table that assigns out-of-vocabulary keys to hash buckets.

Inherits From: [`TrackableResource`](https://www.tensorflow.org/api_docs/python/tf/saved_model/experimental/TrackableResource)

tf.lookup.StaticVocabularyTable(
        initializer,
        num_oov_buckets,
        lookup_key_dtype=None,
        name=None,
        experimental_is_anonymous=False
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Subword tokenizers](https://www.tensorflow.org/text/guide/subwords_tokenizer)<br>    <br>*   [BERT Preprocessing with TF Text](https://www.tensorflow.org/text/guide/bert_preprocessing_guide) | *   [Load text](https://www.tensorflow.org/tutorials/load_data/text)<br>    <br>*   [Apache ORC Reader](https://www.tensorflow.org/io/tutorials/orc) |

For example, if an instance of `StaticVocabularyTable` is initialized with a string-to-id initializer that maps:

    init = tf.lookup.KeyValueTensorInitializer(

The `Vocabulary` object will performs the following mapping:

*   `emerson -> 0`
*   `lake -> 1`
*   `palmer -> 2`
*   `<other term> -> bucket_id`, where `bucket_id` will be between `3` and `3 + num_oov_buckets - 1 = 7`, calculated by: `hash(<term>) % num_oov_buckets + vocab_size`

#### If input\_tensor is:

    input_tensor = tf.constant(["emerson", "lake", "palmer",\
\
If `initializer` is None, only out-of-vocabulary buckets are used.\
\
#### Example usage:\
\
    num_oov_buckets = 3\
\
    init = tf.lookup.TextFileInitializer(\
\
The hash function used for generating out-of-vocabulary buckets ID is Fingerprint64.\
\
Note that the out-of-vocabulary bucket IDs always range from the table `size` up to `size + num_oov_buckets - 1` regardless of the table values, which could cause unexpected collisions:\
\
    init = tf.lookup.KeyValueTensorInitializer(\
\
|     |     |\
| --- | --- |\
| Args<br>---- |     |\
| `initializer` | A `TableInitializerBase` object that contains the data used to initialize the table. If None, then we only use out-of-vocab buckets. |\
| `num_oov_buckets` | Number of buckets to use for out-of-vocabulary keys. Must be greater than zero. If out-of-vocab buckets are not required, use `StaticHashTable` instead. |\
| `lookup_key_dtype` | Data type of keys passed to `lookup`. Defaults to `initializer.key_dtype` if `initializer` is specified, otherwise [`tf.string`](https://www.tensorflow.org/api_docs/python/tf#string)<br>. Must be string or integer, and must be castable to `initializer.key_dtype`. |\
| `name` | A name for the operation (optional). |\
| `experimental_is_anonymous` | Whether to use anonymous mode for the table (default is False). In anonymous mode, the table resource can only be accessed via a resource handle. It can't be looked up by a name. When all resource handles pointing to that resource are gone, the resource will be deleted automatically. |\
\
|     |     |\
| --- | --- |\
| Raises<br>------ |     |\
| `ValueError` | when `num_oov_buckets` is not positive. |\
| `TypeError` | when lookup\_key\_dtype or initializer.key\_dtype are not integer or string. Also when initializer.value\_dtype != int64. |\
\
|     |     |\
| --- | --- |\
| Attributes<br>---------- |     |\
| `key_dtype` | The table key dtype. |\
| `name` | The name of the table. |\
| `resource_handle` | Returns the resource handle associated with this Resource. |\
| `value_dtype` | The table value dtype. |\
\
Methods\
-------\
\
### `lookup`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1362-L1408)\
\
lookup(\
        keys, name=None\
    )\
\
Looks up `keys` in the table, outputs the corresponding values.\
\
It assigns out-of-vocabulary keys to buckets based in their hashes.\
\
|     |     |\
| --- | --- |\
| Args |     |\
| `keys` | Keys to look up. May be either a `SparseTensor` or dense `Tensor`. |\
| `name` | Optional name for the op. |\
\
|     |\
| --- |\
| Returns |     |\
| A `SparseTensor` if keys are sparse, a `RaggedTensor` if keys are ragged, otherwise a dense `Tensor`. |     |\
\
|     |     |\
| --- | --- |\
| Raises |     |\
| `TypeError` | when `keys` doesn't match the table key data type. |\
\
### `size`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L1353-L1360)\
\
size(\
        name=None\
    )\
\
Compute the number of elements in this table.\
\
### `__getitem__`\
\
[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/lookup_ops.py#L171-L173)\
\
__getitem__(\
        keys\
    )\
\
Looks up `keys` in a table, outputs the corresponding values.\
\
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)\
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)\
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)\
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)\
.\
\
Last updated 2026-10-31 UTC.