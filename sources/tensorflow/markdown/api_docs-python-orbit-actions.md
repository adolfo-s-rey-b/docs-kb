[Skip to main content](https://www.tensorflow.org/api_docs/python/orbit/actions#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/orbit/actions)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/orbit/actions?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/orbit/actions#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

Module: orbit.actions Stay organized with collections Save and categorize content based on your preferences.
============================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/orbit/actions#classes)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/orbit/actions/__init__.py)

Defines an "action" abstraction for use with [`orbit.Controller`](https://www.tensorflow.org/api_docs/python/orbit/Controller)
.

"Actions" are simply arbitrary callables that are applied by the `Controller` to the output of train steps (after each inner loop of `steps_per_loop` steps) or an evaluation. This provides a hook mechanism, enabling things like reporting metrics to Vizier, model exporting, additional logging, etc.

The basic `Action` abstraction (just a type alias) is defined in the `controller` module. This `actions` module adds a `ConditionalAction` utility class to make it easy to trigger actions conditionally based on reusable predicates, as well as a small handful of predefined conditions/actions (in particular, a `NewBestMetric` condition and an `ExportSavedModel` action).

One example of using actions to do metric-conditional export:

new_best_metric = orbit.actions.NewBestMetric('accuracy')
    export_action = orbit.actions.ConditionalAction(
        condition=lambda x: x['accuracy'] > 0.9 and new_best_metric(x),
        action=orbit.actions.ExportSavedModel(
            model,
            orbit.actions.ExportFileManager(
                base_name=f'{FLAGS.model_dir}/saved_model',
                next_id_fn=trainer.global_step.numpy),
            signatures=model.infer))
    
    controller = orbit.Controller(
        strategy=strategy,
        trainer=trainer,
        evaluator=evaluator,
        eval_actions=[export_action],
        global_step=trainer.global_step,
        steps_per_loop=FLAGS.steps_per_loop,
        checkpoint_manager=checkpoint_manager,
        summary_interval=1000)

client_0_actions = orbit.actions.ConditionalAction(
        condition=lambda _: client_id() == 0,
        action=[\
            ...\
        ])

In particular, the `NewBestMetric` condition may be used in multi-client settings if all clients are guaranteed to compute the same metric (ensuring this is up to client code, not Orbit). However, when saving metrics it may be helpful to avoid unnecessary writes by setting the `write_value` parameter to `False` for most clients.

Classes
-------

[`class ConditionalAction`](https://www.tensorflow.org/api_docs/python/orbit/actions/ConditionalAction)
: Represents an action that is only taken when a given condition is met.

[`class ExportFileManager`](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportFileManager)
: Utility class that manages a group of files with a shared base name.

[`class ExportSavedModel`](https://www.tensorflow.org/api_docs/python/orbit/actions/ExportSavedModel)
: Action that exports the given model as a SavedModel.

[`class JSONPersistedValue`](https://www.tensorflow.org/api_docs/python/orbit/actions/JSONPersistedValue)
: Represents a value that is persisted via a file-based backing store.

[`class NewBestMetric`](https://www.tensorflow.org/api_docs/python/orbit/actions/NewBestMetric)
: Condition that is satisfied when a new best metric is achieved.

[`class SaveCheckpointIfPreempted`](https://www.tensorflow.org/api_docs/python/orbit/actions/SaveCheckpointIfPreempted)
: Action that saves on-demand checkpoints after a preemption.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-02-13 UTC.