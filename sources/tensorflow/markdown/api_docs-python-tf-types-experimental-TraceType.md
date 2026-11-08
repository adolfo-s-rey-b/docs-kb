[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#methods)
    *   [cast](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#cast)
        
    *   [flatten](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#flatten)
        
    *   [from\_tensors](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#from_tensors)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#most_specific_common_supertype)
        
    *   [placeholder\_value](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#placeholder_value)
        
    *   [to\_tensors](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#to_tensors)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#__eq__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.types.experimental.TraceType Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#used-in-the-notebooks)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#methods)
    *   [cast](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#cast)
        
    *   [flatten](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#flatten)
        
    *   [from\_tensors](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#from_tensors)
        
    *   [is\_subtype\_of](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#is_subtype_of)
        
    *   [most\_specific\_common\_supertype](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#most_specific_common_supertype)
        
    *   [placeholder\_value](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#placeholder_value)
        
    *   [to\_tensors](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#to_tensors)
        
    *   [\_\_eq\_\_](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType#__eq__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L39-L259)

Represents the type of object(s) for tf.function tracing purposes.

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Better performance with tf.function](https://www.tensorflow.org/guide/function) |

`TraceType` is an abstract class that other classes might inherit from to provide information regarding associated class(es) for the purposes of tf.function tracing. The typing logic provided through this mechanism will be used to make decisions regarding usage of cached concrete functions and retracing.

For example, if we have the following tf.function and classes:

@tf.function
    def get_mixed_flavor(fruit_a, fruit_b):
      return fruit_a.flavor + fruit_b.flavor
    
    class Fruit:
      flavor = tf.constant([0, 0])
    
    class Apple(Fruit):
      flavor = tf.constant([1, 2])
    
    class Mango(Fruit):
      flavor = tf.constant([3, 4])

tf.function does not know when to re-use an existing concrete function in regards to the `Fruit` class so naively it retraces for every new instance.

get_mixed_flavor(Apple(), Mango()) # Traces a new concrete function
    get_mixed_flavor(Apple(), Mango()) # Traces a new concrete function again

However, we, as the designers of the `Fruit` class, know that each subclass has a fixed flavor and we can reuse an existing traced concrete function if it was the same subclass. Avoiding such unnecessary tracing of concrete functions can have significant performance benefits.

class FruitTraceType(tf.types.experimental.TraceType):
      def __init__(self, fruit):
        self.fruit_type = type(fruit)
        self.fruit_value = fruit
    
      def is_subtype_of(self, other):
         return (type(other) is FruitTraceType and
                 self.fruit_type is other.fruit_type)
    
      def most_specific_common_supertype(self, others):
         return self if all(self == other for other in others) else None
    
      def placeholder_value(self, placeholder_context=None):
        return self.fruit_value
    
    class Fruit:
    
     def __tf_tracing_type__(self, context):
       return FruitTraceType(self)

Now if we try calling it again:

get_mixed_flavor(Apple(), Mango()) # Traces a new concrete function
    get_mixed_flavor(Apple(), Mango()) # Re-uses the traced concrete function

Methods
-------

### `cast`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L233-L251)

cast(
        value, cast_context
    ) -> Any

Cast value to this type.

|     |     |
| --- | --- |
| Args |     |
| `value` | An input value belonging to this TraceType. |
| `cast_context` | A context reserved for internal/future usage. |

|     |
| --- |
| Returns |     |
| The value casted to this TraceType. |     |

|     |     |
| --- | --- |
| Raises |     |
| `AssertionError` | When \_cast is not overloaded in subclass, the value is returned directly, and it should be the same to self.placeholder\_value(). |

### `flatten`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L229-L231)

flatten() -> List['TraceType']

Returns a list of TensorSpecs corresponding to `to_tensors` values.

### `from_tensors`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L215-L227)

from_tensors(
        tensors: Iterator[core.Tensor]
    ) -> Any

Generates a value of this type from Tensors.

Must use the same fixed amount of tensors as `to_tensors`.

|     |     |
| --- | --- |
| Args |     |
| `tensors` | An iterator from which the tensors can be pulled. |

|     |
| --- |
| Returns |     |
| A value of this type. |     |

### `is_subtype_of`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L106-L130)

@abc.abstractmethod

Returns True if `self` is a subtype of `other`.

For example, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 uses subtyping for dispatch: if `a.is_subtype_of(b)` is True, then an argument of `TraceType` `a` can be used as argument to a `ConcreteFunction` traced with an a `TraceType` `b`.

|     |     |
| --- | --- |
| Args |     |
| `other` | A TraceType object to be compared against. |

#### Example:

class Dimension(TraceType):
      def __init__(self, value: Optional[int]):
        self.value = value
    
      def is_subtype_of(self, other):
        # Either the value is the same or other has a generalized value that
        # can represent any specific ones.
        return (self.value == other.value) or (other.value is None)

### `most_specific_common_supertype`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L132-L162)

@abc.abstractmethod

Returns the most specific supertype of `self` and `others`, if exists.

The returned `TraceType` is a supertype of `self` and `others`, that is, they are all subtypes (see `is_subtype_of`) of it. It is also most specific, that is, there it has no subtype that is also a common supertype of `self` and `others`.

If `self` and `others` have no common supertype, this returns `None`.

|     |     |
| --- | --- |
| Args |     |
| `others` | A sequence of TraceTypes. |

#### Example:

 class Dimension(TraceType):
       def __init__(self, value: Optional[int]):
         self.value = value
    
       def most_specific_common_supertype(self, other):
          # Either the value is the same or other has a generalized value that
          # can represent any specific ones.
          if self.value == other.value:
            return self.value
          else:
            return Dimension(None)

### `placeholder_value`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L164-L198)

@abc.abstractmethod

Creates a placeholder for tracing.

tf.funcion traces with the placeholder value rather than the actual value. For example, a placeholder value can represent multiple different actual values. This means that the trace generated with that placeholder value is more general and reusable which saves expensive retracing.

|     |     |
| --- | --- |
| Args |     |
| `placeholder_context` | A context reserved for internal/future usage. |

For the `Fruit` example shared above, implementing:

class FruitTraceType:
      def placeholder_value(self, placeholder_context):
        return Fruit()

instructs tf.function to trace with the `Fruit()` objects instead of the actual `Apple()` and `Mango()` objects when it receives a call to `get_mixed_flavor(Apple(), Mango())`. For example, Tensor arguments are replaced with Tensors of similar shape and dtype, output from a tf.Placeholder op.

More generally, placeholder values are the arguments of a tf.function, as seen from the function's body:

@tf.function
    def foo(x):
      # Here `x` is be the placeholder value
      ...
    
    foo(x) # Here `x` is the actual value

### `to_tensors`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L200-L213)

to_tensors(
        value: Any
    ) -> List[core.Tensor]

Breaks down a value of this type into Tensors.

For a TraceType instance, the number of tensors generated for corresponding value should be constant.

|     |     |
| --- | --- |
| Args |     |
| `value` | A value belonging to this TraceType |

|     |
| --- |
| Returns |     |
| List of Tensors. |     |

### `__eq__`

[View source](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/types/trace.py#L257-L259)

@abc.abstractmethod

Return self==value.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.