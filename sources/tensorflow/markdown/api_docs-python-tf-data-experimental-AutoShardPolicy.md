[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#methods)
    *   [as\_integer\_ratio](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#as_integer_ratio)
        
    *   [bit\_count](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#bit_count)
        
    *   [bit\_length](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#bit_length)
        
    *   [conjugate](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#conjugate)
        
    *   [from\_bytes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#from_bytes)
        
    *   [to\_bytes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#to_bytes)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__and__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__invert__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__le__)
        
    *   [\_\_lshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__lshift__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__lt__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__neg__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__or__)
        
    *   [\_\_pos\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__pos__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rand__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rfloordiv__)
        
    *   [\_\_rlshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rlshift__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rpow__)
        
    *   [\_\_rrshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rrshift__)
        
    *   [\_\_rshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rshift__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__xor__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#class-variables)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.AutoShardPolicy Stay organized with collections Save and categorize content based on your preferences.
===========================================================================================================================

*   On this page
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#attributes)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#methods)
    *   [as\_integer\_ratio](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#as_integer_ratio)
        
    *   [bit\_count](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#bit_count)
        
    *   [bit\_length](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#bit_length)
        
    *   [conjugate](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#conjugate)
        
    *   [from\_bytes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#from_bytes)
        
    *   [to\_bytes](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#to_bytes)
        
    *   [\_\_abs\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__abs__)
        
    *   [\_\_add\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__add__)
        
    *   [\_\_and\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__and__)
        
    *   [\_\_bool\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__bool__)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__eq__)
        
    *   [\_\_floordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__floordiv__)
        
    *   [\_\_ge\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__ge__)
        
    *   [\_\_gt\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__gt__)
        
    *   [\_\_invert\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__invert__)
        
    *   [\_\_le\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__le__)
        
    *   [\_\_lshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__lshift__)
        
    *   [\_\_lt\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__lt__)
        
    *   [\_\_mod\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__mod__)
        
    *   [\_\_mul\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__mul__)
        
    *   [\_\_ne\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__ne__)
        
    *   [\_\_neg\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__neg__)
        
    *   [\_\_or\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__or__)
        
    *   [\_\_pos\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__pos__)
        
    *   [\_\_pow\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__pow__)
        
    *   [\_\_radd\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__radd__)
        
    *   [\_\_rand\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rand__)
        
    *   [\_\_rfloordiv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rfloordiv__)
        
    *   [\_\_rlshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rlshift__)
        
    *   [\_\_rmod\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rmod__)
        
    *   [\_\_rmul\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rmul__)
        
    *   [\_\_ror\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__ror__)
        
    *   [\_\_rpow\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rpow__)
        
    *   [\_\_rrshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rrshift__)
        
    *   [\_\_rshift\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rshift__)
        
    *   [\_\_rsub\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rsub__)
        
    *   [\_\_rtruediv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rtruediv__)
        
    *   [\_\_rxor\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__rxor__)
        
    *   [\_\_sub\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__sub__)
        
    *   [\_\_truediv\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__truediv__)
        
    *   [\_\_xor\_\_](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#__xor__)
        
*   [Class Variables](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy#class-variables)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/ops/options.py#L88-L152)

Represents the type of auto-sharding to use.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.AutoShardPolicy`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/AutoShardPolicy)

tf.data.experimental.AutoShardPolicy(
        *args, **kwds
    )

OFF: No sharding will be performed.

AUTO: Attempts FILE-based sharding, falling back to DATA-based sharding.

FILE: Shards by input files (i.e. each worker will get a set of files to process). When this option is selected, make sure that there is at least as many files as workers. If there are fewer input files than workers, a runtime error will be raised.

DATA: Shards by elements produced by the dataset. Each worker will process the whole dataset and discard the portion that is not for itself. Note that for this mode to correctly partitions the dataset elements, the dataset needs to produce elements in a deterministic order.

HINT: Looks for the presence of `shard(SHARD_HINT, ...)` which is treated as a placeholder to replace with `shard(num_workers, worker_index)`.

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `denominator` | the denominator of a rational number in lowest terms |
| `imag` | the imaginary part of a complex number |
| `numerator` | the numerator of a rational number in lowest terms |
| `real` | the real part of a complex number |

Methods
-------

### `as_integer_ratio`

as_integer_ratio()

Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    (10).as_integer_ratio()

### `bit_count`

bit_count()

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    bin(13)

### `bit_length`

bit_length()

Number of bits necessary to represent self in binary.

    bin(37)

### `conjugate`

conjugate()

Returns self, the complex conjugate of any int.

### `from_bytes`

from_bytes(
        byteorder='big', *, signed=False
    )

Return the integer represented by the given array of bytes.

bytes Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol. byteorder The byte order used to represent the integer. If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder' as the byte order value. Default is to use 'big'. signed Indicates whether two's complement is used to represent the integer.

### `to_bytes`

to_bytes(
        length=1, byteorder='big', *, signed=False
    )

Return an array of bytes representing an integer.

length Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes. Default is length 1. byteorder The byte order used to represent the integer. If byteorder is 'big', the most significant byte is at the beginning of the byte array. If byteorder is 'little', the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder' as the byte order value. Default is to use 'big'. signed Determines whether two's complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

### `__abs__`

__abs__()

abs(self)

### `__add__`

__add__(
        value, /
    )

Return self+value.

### `__and__`

__and__(
        value, /
    )

Return self&value.

### `__bool__`

__bool__()

True if self else False

### `__eq__`

__eq__(
        value, /
    )

Return self==value.

### `__floordiv__`

__floordiv__(
        value, /
    )

Return self//value.

### `__ge__`

__ge__(
        value, /
    )

Return self>=value.

### `__gt__`

__gt__(
        value, /
    )

Return self>value.

### `__invert__`

__invert__()

~self

### `__le__`

__le__(
        value, /
    )

Return self<=value.

### `__lshift__`

__lshift__(
        value, /
    )

Return self<<value.

### `__lt__`

__lt__(
        value, /
    )

Return self<value.

### `__mod__`

__mod__(
        value, /
    )

Return self%value.

### `__mul__`

__mul__(
        value, /
    )

Return self\*value.

### `__ne__`

__ne__(
        value, /
    )

Return self!=value.

### `__neg__`

__neg__()

\-self

### `__or__`

__or__(
        value, /
    )

Return self|value.

### `__pos__`

__pos__()

+self

### `__pow__`

__pow__(
        value, mod, /
    )

Return pow(self, value, mod).

### `__radd__`

__radd__(
        value, /
    )

Return value+self.

### `__rand__`

__rand__(
        value, /
    )

Return value&self.

### `__rfloordiv__`

__rfloordiv__(
        value, /
    )

Return value//self.

### `__rlshift__`

__rlshift__(
        value, /
    )

Return value<<self.

### `__rmod__`

__rmod__(
        value, /
    )

Return value%self.

### `__rmul__`

__rmul__(
        value, /
    )

Return value\*self.

### `__ror__`

__ror__(
        value, /
    )

Return value|self.

### `__rpow__`

__rpow__(
        value, mod, /
    )

Return pow(value, self, mod).

### `__rrshift__`

__rrshift__(
        value, /
    )

Return value>>self.

### `__rshift__`

__rshift__(
        value, /
    )

Return self>>value.

### `__rsub__`

__rsub__(
        value, /
    )

Return value-self.

### `__rtruediv__`

__rtruediv__(
        value, /
    )

Return value/self.

### `__rxor__`

__rxor__(
        value, /
    )

Return value^self.

### `__sub__`

__sub__(
        value, /
    )

Return self-value.

### `__truediv__`

__truediv__(
        value, /
    )

Return self/value.

### `__xor__`

__xor__(
        value, /
    )

Return self^value.

|     |     |
| --- | --- |
| Class Variables<br>--------------- |     |
| AUTO | `<AutoShardPolicy.AUTO: 0>` |
| DATA | `<AutoShardPolicy.DATA: 2>` |
| FILE | `<AutoShardPolicy.FILE: 1>` |
| HINT | `<AutoShardPolicy.HINT: 3>` |
| OFF | `<AutoShardPolicy.OFF: -1>` |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.