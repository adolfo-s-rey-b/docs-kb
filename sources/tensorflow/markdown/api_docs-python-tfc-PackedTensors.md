[Skip to main content](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#methods)
    *   [pack](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#pack)
        
    *   [unpack](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#unpack)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfc.PackedTensors Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#methods)
    *   [pack](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#pack)
        
    *   [unpack](https://www.tensorflow.org/api_docs/python/tfc/PackedTensors#unpack)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/util/packed_tensors.py#L25-L100)

Packed representation of compressed tensors.

tfc.PackedTensors(
        string=None
    )

This class can pack and unpack several tensor values into a single string. It can also optionally store a model identifier.

The tensors currently must be rank 1 (vectors) and either have integer or string type.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `model` | A model identifier. |
| `string` | The string representation of this object. |

Methods
-------

### `pack`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/util/packed_tensors.py#L64-L84)

pack(
        tensors
    )

Packs `Tensor` values into this object.

### `unpack`

[View source](https://github.com/tensorflow/compression/blob/v2.14.1/tensorflow_compression/python/util/packed_tensors.py#L86-L100)

unpack(
        dtypes
    )

Unpacks values from this object based on dtypes.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.