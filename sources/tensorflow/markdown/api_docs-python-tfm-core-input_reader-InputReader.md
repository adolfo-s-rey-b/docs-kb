[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#methods)
    *   [get\_files](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#get_files)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#read)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.core.input\_reader.InputReader Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#methods)
    *   [get\_files](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#get_files)
        
    *   [read](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#read)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tfm/core/input_reader/InputReader#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/core/input_reader.py#L214-L599)

Input reader that returns a tf.data.Dataset instance.

tfm.core.input_reader.InputReader(
        params: tfm.core.config_definitions.DataConfig,
        dataset_fn=tf.data.TFRecordDataset,
        decoder_fn: Optional[Callable[..., Any]] = None,
        combine_fn: Optional[Callable[..., Any]] = None,
        sample_fn: Optional[Callable[..., Any]] = None,
        parser_fn: Optional[Callable[..., Any]] = None,
        filter_fn: Optional[Callable[..., tf.Tensor]] = None,
        transform_and_batch_fn: Optional[Callable[[tf.data.Dataset, Optional[tf.distribute.InputContext]],\
            tf.data.Dataset]] = None,
        postprocess_fn: Optional[Callable[..., Any]] = None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `params` | A config\_definitions.DataConfig object. |
| `dataset_fn` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> that consumes the input files. For example, it can be [`tf.data.TFRecordDataset`](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset)<br>. |
| `decoder_fn` | An optional `callable` that takes the serialized data string and decodes them into the raw tensor dictionary. |
| `combine_fn` | An optional `callable` that takes a dictionarty of [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> objects as input and outputs a combined dataset. It will be executed after the decoder\_fn and before the sample\_fn. |
| `sample_fn` | An optional `callable` that takes a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object as input and outputs the transformed dataset. It performs sampling on the decoded raw tensors dict before the parser\_fn. |
| `parser_fn` | An optional `callable` that takes the decoded raw tensors dict and parse them into a dictionary of tensors that can be consumed by the model. It will be executed after decoder\_fn. |
| `filter_fn` | An optional `callable` mapping a dataset element to a boolean. It will be executed after parser\_fn. |
| `transform_and_batch_fn` | An optional `callable` that takes a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object and an optional [`tf.distribute.InputContext`](https://www.tensorflow.org/api_docs/python/tf/distribute/InputContext)<br> as input, and returns a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object. It will be executed after `parser_fn` to transform and batch the dataset; if None, after `parser_fn` is executed, the dataset will be batched into per-replica batch size. |
| `postprocess_fn` | A optional `callable` that processes batched tensors. It will be executed after batching. |

Methods
-------

### `get_files`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/input_reader.py#L358-L370)

get_files(
        input_path
    )

Gets matched files. Can be overridden by subclasses.

### `read`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/core/input_reader.py#L569-L599)

read(
        input_context: Optional[tf.distribute.InputContext] = None,
        dataset: Optional[tf.data.Dataset] = None
    ) -> tf.data.Dataset

Generates a tf.data.Dataset object.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| static\_randnum | `697568466` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.