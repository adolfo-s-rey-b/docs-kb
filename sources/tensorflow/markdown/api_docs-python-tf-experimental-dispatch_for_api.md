[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_api#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.experimental.dispatch\_for\_api Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/util/dispatch.py#L334-L449)

Decorator that overrides the default implementation for a TensorFlow API.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.experimental.dispatch_for_api`](https://www.tensorflow.org/api_docs/python/tf/experimental/dispatch_for_api)

tf.experimental.dispatch_for_api(
        api, *signatures
    )

### Used in the notebooks

| Used in the guide |
| --- |
| *   [Extension types](https://www.tensorflow.org/guide/extension_type) |

The decorated function (known as the "dispatch target") will override the default implementation for the API when the API is called with parameters that match a specified type signature. Signatures are specified using dictionaries that map parameter names to type annotations. E.g., in the following example, `masked_add` will be called for [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add)
 if both `x` and `y` are `MaskedTensor`s:

    class MaskedTensor(tf.experimental.ExtensionType):

    @dispatch_for_api(tf.math.add, {'x': MaskedTensor, 'y': MaskedTensor})

    mt = tf.add(MaskedTensor([1, 2], [True, False]), MaskedTensor(10, True))

If multiple type signatures are specified, then the dispatch target will be called if any of the signatures match. For example, the following code registers `masked_add` to be called if `x` is a `MaskedTensor` _or_ `y` is a `MaskedTensor`.

    @dispatch_for_api(tf.math.add, {'x': MaskedTensor}, {'y':MaskedTensor})

The type annotations in type signatures may be type objects (e.g., `MaskedTensor`), `typing.List` values, or `typing.Union` values. For example, the following will register `masked_concat` to be called if `values` is a list of `MaskedTensor` values:

    @dispatch_for_api(tf.concat, {'values': typing.List[MaskedTensor]})

Each type signature must contain at least one subclass of `tf.CompositeTensor` (which includes subclasses of `tf.ExtensionType`), and dispatch will only be triggered if at least one type-annotated parameter contains a `CompositeTensor` value. This rule avoids invoking dispatch in degenerate cases, such as the following examples:

*   `@dispatch_for_api(tf.concat, {'values': List[MaskedTensor]})`: Will not dispatch to the decorated dispatch target when the user calls `tf.concat([])`.
    
*   `@dispatch_for_api(tf.add, {'x': Union[MaskedTensor, Tensor], 'y': Union[MaskedTensor, Tensor]})`: Will not dispatch to the decorated dispatch target when the user calls `tf.add(tf.constant(1), tf.constant(2))`.
    

The dispatch target's signature must match the signature of the API that is being overridden. In particular, parameters must have the same names, and must occur in the same order. The dispatch target may optionally elide the "name" parameter, in which case it will be wrapped with a call to [`tf.name_scope`](https://www.tensorflow.org/api_docs/python/tf/name_scope)
 when appropriate.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `api` | The TensorFlow API to override. |
| `*signatures` | Dictionaries mapping parameter names or indices to type annotations, specifying when the dispatch target should be called. In particular, the dispatch target will be called if any signature matches; and a signature matches if all of the specified parameters have types that match with the indicated type annotations. If no signatures are specified, then a signature will be read from the dispatch target function's type annotations. |

|     |
| --- |
| Returns<br>------- |     |
| A decorator that overrides the default implementation for `api`. |     |

#### Registered APIs

The TensorFlow APIs that may be overridden by `@dispatch_for_api` are:

<\>

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.