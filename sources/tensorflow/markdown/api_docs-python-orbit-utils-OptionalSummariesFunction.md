[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction#attributes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

orbit.utils.OptionalSummariesFunction Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction#args)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/orbit/utils/OptionalSummariesFunction#attributes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/utils/tpu_summaries.py#L34-L145)

Wrapper that provides versions of a function with and without summaries.

orbit.utils.OptionalSummariesFunction(
        function, **tf_function_kwargs
    )

This is a utility class for implementing optimized summary recording via a two-function approach, specifically important for TPUs. Two [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
 versions of a given `function` are created: one with soft device placement enabled (for use on steps that require summary writing), and one with summary writing and soft device placement entirely disabled (for use on all other steps). This removes any performance impact of summaries on steps where they aren't recorded (b/148418718).

This class can be used as a base class to implement summary optimizations for a function with a specific signature. For example, to implement efficient TPU summaries for a standard `train()` method (as in [`orbit.AbstractTrainer`](https://www.tensorflow.org/api_docs/python/orbit/AbstractTrainer)
):

class TrainFunctionWithSummaries(orbit.utils.OptionalSummariesFunction):
      '''Implements a two-program approach for summaries on TPU.'''
    
      def __call__(self, num_steps):
        if tf.summary.should_record_summaries():
          output = self.with_summaries(tf.constant(1))
          num_steps -= 1
        if num_steps >= 1:
          output = self.without_summaries(num_steps)
        return output

This can be used directly or to implement a decorator:

def train_function_with_summaries(function=None, **kwargs):
      if function is not None:
        return TrainFunctionWithSummaries(function, **kwargs)
      return functools.partial(TrainFunctionWithSummaries, **kwargs)

The decorator can be applied directly to `train()` methods:

@train_function_with_summaries
    def train(self, num_steps):
      ...

A similar approach approach can be implemented for functions with different signatures.

This wrapper properly handles instance methods (see `__get__`).

|     |     |
| --- | --- |
| Args<br>---- |     |
| `function` | The underlying function to wrap. |
| `**tf_function_kwargs` | Additional arguments to pass to [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)<br>. |

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `with_summaries` | A wrapped version of the underlying function with summaries enabled (using whatever the active predicate is for [`tf.summary.record_if`](https://www.tensorflow.org/api_docs/python/tf/summary/record_if)<br>), and placed inside a "soft device placement" context to enable summary recording on TPU. |
| `without_summaries` | A wrapped version of the underlying function with all summary recording disabled. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.