[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/function)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/function?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#used-in-the-notebooks_1)
    
*   [Features](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#features_2)
    
*   [tf.function creates polymorphic callables](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#tffunction_creates_polymorphic_callables_2)
    
*   [Retracing](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#retracing_2)
    
*   [Input signatures](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#input_signatures_2)
    
*   [Variables may only be created once](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#variables_may_only_be_created_once_2)
    
*   [Python operations execute only once per trace](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#python_operations_execute_only_once_per_trace_2)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#raises_1)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.function Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#used-in-the-notebooks_1)
    
*   [Features](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#features_2)
    
*   [tf.function creates polymorphic callables](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#tffunction_creates_polymorphic_callables_2)
    
*   [Retracing](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#retracing_2)
    
*   [Input signatures](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#input_signatures_2)
    
*   [Variables may only be created once](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#variables_may_only_be_created_once_2)
    
*   [Python operations execute only once per trace](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#python_operations_execute_only_once_per_trace_2)
    
*   [Args](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#args_1)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#returns_1)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/function?version=stable#raises_1)
    

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/eager/polymorphic_function/polymorphic_function.py#L1305-L1691)

Compiles a function into a callable TensorFlow graph. (deprecated arguments) (deprecated arguments) (deprecated arguments)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.function`](https://www.tensorflow.org/api_docs/python/tf/function)

tf.function(
        func=None,
        input_signature=None,
        autograph=True,
        jit_compile=None,
        reduce_retracing=False,
        experimental_implements=None,
        experimental_autograph_options=None,
        experimental_attributes=None,
        experimental_relax_shapes=None,
        experimental_compile=None,
        experimental_follow_type_hints=None
    ) -> tf.types.experimental.PolymorphicFunction

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Better performance with tf.function](https://www.tensorflow.org/guide/function)<br>    <br>*   [Introduction to graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs)<br>    <br>*   [Extension types](https://www.tensorflow.org/guide/extension_type)<br>    <br>*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)<br>    <br>*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf) | *   [Custom training with tf.distribute.Strategy](https://www.tensorflow.org/tutorials/distribute/custom_training)<br>    <br>*   [Distributed Input](https://www.tensorflow.org/tutorials/distribute/input)<br>    <br>*   [Distributed training with DTensors](https://www.tensorflow.org/tutorials/distribute/dtensor_ml_tutorial)<br>    <br>*   [Parameter server training with ParameterServerStrategy](https://www.tensorflow.org/tutorials/distribute/parameter_server_training)<br>    <br>*   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial) |

[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 constructs a [`tf.types.experimental.PolymorphicFunction`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/PolymorphicFunction)
 that executes a TensorFlow graph ([`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
) created by trace-compiling the TensorFlow operations in `func`. More information on the topic can be found in [Introduction to Graphs and tf.function](https://www.tensorflow.org/guide/intro_to_graphs)
.

See [Better Performance with tf.function](https://www.tensorflow.org/guide/function)
 for tips on performance and known limitations.

#### Example usage:

    @tf.function

The trace-compilation allows non-TensorFlow operations to execute, but under special conditions. In general, only TensorFlow operations are guaranteed to run and create fresh results whenever the `PolymorphicFunction` is called.

Features
--------

`func` may use data-dependent Python control flow statements, including `if`, `for`, `while` `break`, `continue` and `return`:

    @tf.function

`func`'s closure may include [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
 and [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 objects:

    @tf.function

`func` may also use ops with side effects, such as [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
, [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 and others:

    v = tf.Variable(1)

    l = []

Instead, use TensorFlow collections like [`tf.TensorArray`](https://www.tensorflow.org/api_docs/python/tf/TensorArray)
:

    @tf.function

[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 creates polymorphic callables
------------------------------------------------------------------------------------------------------

Internally, [`tf.types.experimental.PolymorphicFunction`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/PolymorphicFunction)
 may contain multiple [`tf.types.experimental.ConcreteFunction`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction)
s, each specialized to arguments with different data types or shapes, since TensorFlow can perform more optimizations on graphs of specific shapes, dtypes and values of constant arguments. [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 treats any pure Python values as opaque objects (best thought of as compile-time constants), and builds a separate [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
 for each set of Python arguments that it encounters. For more information, see the [tf.function guide](https://www.tensorflow.org/guide/function#rules_of_tracing)

Executing a `PolymorphicFunction` will select and execute the appropriate `ConcreteFunction` based on the argument types and values.

To obtain an individual `ConcreteFunction`, use the [`PolymorphicFunction.get_concrete_function`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/PolymorphicFunction#get_concrete_function)
 method. It can be called with the same arguments as `func` and returns a [`tf.types.experimental.ConcreteFunction`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/ConcreteFunction)
. `ConcreteFunction`s are backed by a single [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph)
:

    @tf.function

`ConcreteFunction`s can be executed just like `PolymorphicFunction`s, but their input is restricted to the types to which they're specialized.

Retracing
---------

`ConcreteFunctions` are built (traced) on the fly, as the `PolymorphicFunction` is called with new TensorFlow types or shapes, or with new Python values as arguments. When `PolymorphicFunction` builds a new trace, it is said that `func` is retraced. Retracing is a frequent performance concern for [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 as it can be considerably slower than executing a graph that's already been traced. It is ideal to minimize the amount of retracing in your code.

    @tf.function

Python numerical arguments should only be used when they take few distinct values, such as hyperparameters like the number of layers in a neural network.

Input signatures
----------------

For Tensor arguments, `PolymorphicFunction`creates a new `ConcreteFunction` for every unique set of input shapes and datatypes. The example below creates two separate `ConcreteFunction`s, each specialized to a different shape:

    @tf.function

An "input signature" can be optionally provided to [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 to control this process. The input signature specifies the shape and type of each Tensor argument to the function using a [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)
 object. More general shapes can be used. This ensures only one `ConcreteFunction` is created, and restricts the `PolymorphicFunction` to the specified shapes and types. It is an effective way to limit retracing when Tensors have dynamic shapes.

    @tf.function(

Variables may only be created once
----------------------------------

[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 only allows creating new [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
 objects when it is called for the first time:

    class MyModule(tf.Module):

In general, it is recommended to create [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
s outside of [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
. In simple cases, persisting state across [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 boundaries may be implemented using a pure functional style in which state is represented by [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
s passed as arguments and returned as return values.

Contrast the two styles below:

    state = tf.Variable(1)

    state = tf.constant(1)

Python operations execute only once per trace
---------------------------------------------

`func` may contain TensorFlow operations mixed with pure Python operations. However, when the function is executed, only the TensorFlow operations will run. The Python operations run only once, at trace time. If TensorFlow operations depend on results from Python operations, those results will be frozen into the graph.

    @tf.function

    f(1, tf.constant(2))

    f(2, tf.constant(1))

    f(2, tf.constant(2))

|     |     |
| --- | --- |
| Args<br>---- |     |
| `func` | The function to be compiled. If `func` is None, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> returns a decorator that can be invoked with a single argument - `func`. In other words, `tf.function(input_signature=...)(func)` is equivalent to [`tf.function(func, input_signature=...)`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. The former can be used as decorator. |
| `input_signature` | A possibly nested sequence of [`tf.TensorSpec`](https://www.tensorflow.org/api_docs/python/tf/TensorSpec)<br> objects specifying the shapes and dtypes of the Tensors that will be supplied to this function. If `None`, a separate function is instantiated for each inferred input signature. If input\_signature is specified, every input to `func` must be a `Tensor`, and `func` cannot accept `**kwargs`. |
| `autograph` | Whether autograph should be applied on `func` before tracing a graph. Data-dependent Python control flow statements require `autograph=True`. For more information, see the [tf.function and AutoGraph guide](https://www.tensorflow.org/guide/function#autograph_transformations)<br>. |
| `jit_compile` | If `True`, compiles the function using [XLA](https://tensorflow.org/xla)<br>. XLA performs compiler optimizations, such as fusion, and attempts to emit more efficient code. This may drastically improve the performance. If set to `True`, the whole function needs to be compilable by XLA, or an [`errors.InvalidArgumentError`](https://www.tensorflow.org/api_docs/python/tf/errors/InvalidArgumentError)<br> is thrown. If `None` (default), compiles the function with XLA when running on TPU and goes through the regular function execution path when running on other devices. If `False`, executes the function without XLA compilation. Set this value to `False` when directly running a multi-device function on TPUs (e.g. two TPU cores, one TPU core and its host CPU). Not all functions are compilable, see a list of [sharp corners](https://tensorflow.org/xla/known_issues)<br>. |
| `reduce_retracing` | When True, [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br> attempts to reduce the amount of retracing, for example by using more generic shapes. This can be controlled for user objects by customizing their associated [`tf.types.experimental.TraceType`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/TraceType)<br>. |
| `experimental_implements` | If provided, contains a name of a "known" function this implements. For example "mycompany.my\_recurrent\_cell". This is stored as an attribute in inference function, which can then be detected when processing serialized function. See [standardizing composite ops](https://github.com/tensorflow/community/blob/master/rfcs/20190610-standardizing-composite_ops.md)<br><br>this attribute see this [example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/mlir/lite/transforms/prepare_composite_functions_tf.cc)<br> The code above automatically detects and substitutes function that implements "embedded\_matmul" and allows TFLite to substitute its own implementations. For instance, a tensorflow user can use this attribute to mark that their function also implements `embedded_matmul` (perhaps more efficiently!) by specifying it using this parameter: `@tf.function(experimental_implements="embedded_matmul")` This can either be specified as just the string name of the function or a NameAttrList corresponding to a list of key-value attributes associated with the function name. The name of the function will be in the 'name' field of the NameAttrList. To define a formal TF op for this function implements, try the experimental [composite TF](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/compiler/mlir/tfr)<br> project. |
| `experimental_autograph_options` | Optional tuple of [`tf.autograph.experimental.Feature`](https://www.tensorflow.org/api_docs/python/tf/autograph/experimental/Feature)<br> values. |
| `experimental_attributes` | Optional dictionary of attributes to include in the generated FunctionDefs. |
| `experimental_relax_shapes` | Deprecated. Use `reduce_retracing` instead. |
| `experimental_compile` | Deprecated alias to 'jit\_compile'. |
| `experimental_follow_type_hints` | Deprecated. Please use input\_signature or reduce\_retracing instead. |

|     |
| --- |
| Returns<br>------- |     |
| If `func` is not None, returns a [`tf.types.experimental.PolymorphicFunction`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/PolymorphicFunction)<br>. If `func` is None, returns a decorator that, when invoked with a single `func` argument, returns a [`tf.types.experimental.PolymorphicFunction`](https://www.tensorflow.org/api_docs/python/tf/types/experimental/PolymorphicFunction)<br>. |     |

|     |
| --- |
| Raises<br>------ |     |
| `ValueError` when attempting to use `jit_compile=True`, but XLA support is not available. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.