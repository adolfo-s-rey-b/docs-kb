[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#methods)
    *   [bind](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#bind)
        
    *   [bind\_partial](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#bind_partial)
        
    *   [from\_callable](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#from_callable)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#replace)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.types.experimental.FunctionType Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#attributes)
    
*   [Child Classes](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#child_classes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#methods)
    *   [bind](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#bind)
        
    *   [bind\_partial](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#bind_partial)
        
    *   [from\_callable](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#from_callable)
        
    *   [replace](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#replace)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/core.py#L90-L108)

Represents the type of a TensorFlow callable.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.types.experimental.FunctionType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType)

tf.types.experimental.FunctionType(
        parameters=None, *, return_annotation, __validate_parameters__=True
    )

FunctionType inherits from inspect.Signature which canonically represents the structure (and optionally type) information of input parameters and output of a Python function. Additionally, it integrates with the tf.function type system ([`tf.types.experimental.TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)
) to provide a holistic representation of the I/O contract of the callable. It is used for:

*   Canonicalization and type-checking of Python input arguments
*   Type-based dispatch to concrete functions
*   Packing/unpacking structured python values to Tensors
*   Generation of structured placeholder values for tracing

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `parameters` |     |
| `return_annotation` |     |

Child Classes
-------------

[`class empty`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/FunctionType/empty)

Methods
-------

### `bind`

bind(
        *args, **kwargs
    )

Get a BoundArguments object, that maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

### `bind_partial`

bind_partial(
        *args, **kwargs
    )

Get a BoundArguments object, that partially maps the passed `args` and `kwargs` to the function's signature. Raises `TypeError` if the passed arguments can not be bound.

### `from_callable`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/core.py#L106-L108)

@classmethod

Constructs Signature for the given callable object.

### `replace`

replace(
        *, parameters=_void, return_annotation=_void
    )

Creates a customized copy of the Signature. Pass 'parameters' and/or 'return\_annotation' arguments to override them in the new copy.

### `__eq__`

__eq__(
        other
    )

Return self==value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.