[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#methods)
    *   [count](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#count)
        
    *   [index](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#index)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__bool__)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__gt__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__le__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__len__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__lt__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__ne__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.preprocess\_ops.range Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#methods)
    *   [count](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#count)
        
    *   [index](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#index)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__bool__)
        
    *   [\_\_contains\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__contains__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__eq__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__ge__)
        
    *   [\_\_getitem\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__getitem__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__gt__)
        
    *   [\_\_iter\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__iter__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__le__)
        
    *   [\_\_len\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__len__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__lt__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/preprocess_ops/range#__ne__)
        

range(stop) -> range object range(start, stop\[, step\]) -> range object

tfm.vision.preprocess_ops.range(
        *args, **kwargs
    )

Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `start` |     |
| `step` |     |
| `stop` |     |

Methods
-------

### `count`

count()

rangeobject.count(value) -> integer -- return number of occurrences of value

### `index`

index()

rangeobject.index(value) -> integer -- return index of value. Raise ValueError if the value is not present.

### `__bool__`

__bool__()

True if self else False

### `__contains__`

__contains__(
        key, /
    )

Return key in self.

### `__eq__`

__eq__(
        value, /
    )

Return self==value.

### `__ge__`

__ge__(
        value, /
    )

Return self>=value.

### `__getitem__`

__getitem__(
        key, /
    )

Return self\[key\].

### `__gt__`

__gt__(
        value, /
    )

Return self>value.

### `__iter__`

__iter__()

Implement iter(self).

### `__le__`

__le__(
        value, /
    )

Return self<=value.

### `__len__`

__len__()

Return len(self).

### `__lt__`

__lt__(
        value, /
    )

Return self<value.

### `__ne__`

__ne__(
        value, /
    )

Return self!=value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.