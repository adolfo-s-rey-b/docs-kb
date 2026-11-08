[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.actions.ConditionalAction Stay organized with collections Save and categorize content based on your preferences.
======================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#args)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/conditional_action.py#L33-L61)

Represents an action that is only taken when a given condition is met.

orbit.actions.ConditionalAction(
        condition: Condition,
        action: Union[controller.Action, Sequence[controller.Action]]
    )

This class is itself an `Action` (a callable that can be applied to train or eval outputs), but is intended to make it easier to write modular and reusable conditions by decoupling "when" something whappens (the condition) from "what" happens (the action).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `condition` | A callable accepting train or eval outputs and returning a bool. |
| `action` | The action (or optionally sequence of actions) to perform when `condition` is met. |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/conditional_action.py#L58-L61)

__call__(
        output: runner.Output
    ) -> None

Call self as a function.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.