[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#methods)
    *   [count](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#count)
        
    *   [index](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#index)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__contains__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__len__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.augment.Sequence Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#methods)
    *   [count](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#count)
        
    *   [index](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#index)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__contains__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__getitem__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__iter__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/augment/Sequence#__len__)
        

All the operations on a read-only sequence.

Concrete subclasses must override **new** or **init**, **getitem**, and **len**.

Methods
-------

### `count`

count(
        value
    )

S.count(value) -> integer -- return number of occurrences of value

### `index`

index(
        value, start=0, stop=None
    )

S.index(value, \[start, \[stop\]\]) -> integer -- return first index of value. Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

### `__contains__`

__contains__(
        value
    )

### `__getitem__`

__getitem__(
        index
    )

### `__iter__`

__iter__()

### `__len__`

__len__()

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.