[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/oauth2authorize?return_url=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fmake_template&scopes=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdeveloperprofiles.award+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdevprofiles.full_control.firstparty)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.make\_template Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/template.py#L33-L174)

Given an arbitrary function, wrap it so that it does variable sharing.

tf.compat.v1.make_template(
        name_,
        func_,
        create_scope_now_=False,
        unique_name_=None,
        custom_getter_=None,
        **kwargs
    )

Migrate to TF2
--------------

[`tf.compat.v1.make_template`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template)
 is a legacy API that is only compatible with eager execution enabled and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 if you combine it with `tf.compat.v1.keras.utils.track_tf1_style_variables`. See the model mapping migration guide section on `make_template` for more info:

[https://www.tensorflow.org/guide/migrate/model\_mapping#using\_tfcompatv1make\_template\_in\_the\_decorated\_method](https://www.tensorflow.org/guide/migrate/model_mapping#using_tfcompatv1make_template_in_the_decorated_method)

Even if you use legacy apis for `variable_scope`\-based variable reuse, we recommend using `tf.compat.v1.keras.utils.track_tf1_style_variables` directly and not using [`tf.compat.v1.make_template`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/make_template)
, as it interoperates with eager execution in a simpler and more predictable fashion than `make_template`.

The TF2 API approach would be tracking your variables using [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module)
s or Keras layers and models rather than relying on `make_template`.

Description
-----------

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping) | *   [Linear Mixed-Effect Regression in {TF Probability, R, Stan}](https://www.tensorflow.org/probability/examples/HLM_TFP_R_Stan) |

This wraps `func_` in a Template and partially evaluates it. Templates are functions that create variables the first time they are called and reuse them thereafter. In order for `func_` to be compatible with a `Template` it must have the following properties:

*   The function should create all trainable variables and any variables that should be reused by calling [`tf.compat.v1.get_variable`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable)
    . If a trainable variable is created using [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
    , then a ValueError will be thrown. Variables that are intended to be locals can be created by specifying [`tf.Variable(..., trainable=false)`](https://www.tensorflow.org/api_docs/python/tf/Variable)
    .
*   The function may use variable scopes and other templates internally to create and reuse variables, but it shouldn't use [`tf.compat.v1.global_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables)
     to capture variables that are defined outside of the scope of the function.
*   Internal scopes and variable names should not depend on any arguments that are not supplied to `make_template`. In general you will get a ValueError telling you that you are trying to reuse a variable that doesn't exist if you make a mistake.

In the following example, both `z` and `w` will be scaled by the same `y`. It is important to note that if we didn't assign `scalar_name` and used a different name for z and w that a `ValueError` would be thrown because it couldn't reuse the variable.

def my_op(x, scalar_name):
      var1 = tf.compat.v1.get_variable(scalar_name,
                             shape=[],
                             initializer=tf.compat.v1.constant_initializer(1))
      return x * var1
    
    scale_by_y = tf.compat.v1.make_template('scale_by_y', my_op, scalar_name='y')
    
    z = scale_by_y(input1)
    w = scale_by_y(input2)

As a safe-guard, the returned function will raise a `ValueError` after the first call if trainable variables are created by calling [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)
.

If all of these are true, then 2 properties are enforced by the template:

1.  Calling the same template multiple times will share all non-local variables.
2.  Two different templates are guaranteed to be unique, unless you reenter the same variable scope as the initial definition of a template and redefine it. An examples of this exception:

def my_op(x, scalar_name):
      var1 = tf.compat.v1.get_variable(scalar_name,
                             shape=[],
                             initializer=tf.compat.v1.constant_initializer(1))
      return x * var1
    
    with tf.compat.v1.variable_scope('scope') as vs:
      scale_by_y = tf.compat.v1.make_template('scale_by_y', my_op,
      scalar_name='y')
      z = scale_by_y(input1)
      w = scale_by_y(input2)
    
    # Creates a template that reuses the variables above.
    with tf.compat.v1.variable_scope(vs, reuse=True):
      scale_by_y2 = tf.compat.v1.make_template('scale_by_y', my_op,
      scalar_name='y')
      z2 = scale_by_y2(input1)
      w2 = scale_by_y2(input2)

Depending on the value of `create_scope_now_`, the full variable scope may be captured either at the time of first call or at the time of construction. If this option is set to True, then all Tensors created by repeated calls to the template will have an extra trailing \_N+1 to their name, as the first time the scope is entered in the Template constructor no Tensors are created.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `name_` | A name for the scope created by this template. If necessary, the name will be made unique by appending `_N` to the name. |
| `func_` | The function to wrap. |
| `create_scope_now_` | Boolean controlling whether the scope should be created when the template is constructed or when the template is called. Default is False, meaning the scope is created when the template is called. |
| `unique_name_` | When used, it overrides name\_ and is not made unique. If a template of the same scope/unique\_name already exists and reuse is false, an error is raised. Defaults to None. |
| `custom_getter_` | Optional custom getter for variables used in `func_`. See the [`tf.compat.v1.get_variable`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/get_variable)<br> `custom_getter` documentation for more information. |
| `**kwargs` | Keyword arguments to apply to `func_`. |

|     |
| --- |
| Returns<br>------- |     |
| A function to encapsulate a set of variables which should be created once and reused. An enclosing scope will be created either when `make_template` is called or when the result is called, depending on the value of `create_scope_now_`. Regardless of the value, the first time the template is called it will enter the scope with no reuse, and call `func_` to create variables, which are guaranteed to be unique. All subsequent calls will re-enter the scope and reuse those variables. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | if `name_` is None. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.