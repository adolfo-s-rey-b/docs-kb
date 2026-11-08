None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [The Model class](https://keras.io/api/models/model/)
 [The Sequential class](https://keras.io/api/models/sequential/)
 [Model training APIs](https://keras.io/api/models/model_training_apis/)
 [Saving & serialization](https://keras.io/api/models/model_saving_apis/)
 [Knowledge distillation](https://keras.io/api/models/distillation/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / Models API

Models API
==========

There are three ways to create Keras models:

*   The [Sequential model](https://keras.io/guides/sequential_model)
    , which is very straightforward (a simple list of layers), but is limited to single-input, single-output stacks of layers (as the name gives away).
*   The [Functional API](https://keras.io/guides/functional_api)
    , which is an easy-to-use, fully-featured API that supports arbitrary model architectures. For most people and most use cases, this is what you should be using. This is the Keras "industry strength" model.
*   [Model subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing)
    , where you implement everything from scratch on your own. Use this if you have complex, out-of-the-box research use cases.

Models API overview
-------------------

### [The Model class](https://keras.io/api/models/model/)

*   [Model class](https://keras.io/api/models/model/#model-class)
    
*   [KerasTensor class](https://keras.io/api/models/model/#kerastensor-class)
    
*   [summary method](https://keras.io/api/models/model/#summary-method)
    
*   [get\_layer method](https://keras.io/api/models/model/#get_layer-method)
    
*   [get\_state\_tree method](https://keras.io/api/models/model/#get_state_tree-method)
    
*   [set\_state\_tree method](https://keras.io/api/models/model/#set_state_tree-method)
    
*   [quantize method](https://keras.io/api/models/model/#quantize-method)
    

### [The Sequential class](https://keras.io/api/models/sequential/)

*   [Sequential class](https://keras.io/api/models/sequential/#sequential-class)
    
*   [add method](https://keras.io/api/models/sequential/#add-method)
    
*   [pop method](https://keras.io/api/models/sequential/#pop-method)
    

### [Model training APIs](https://keras.io/api/models/model_training_apis/)

*   [compile method](https://keras.io/api/models/model_training_apis/#compile-method)
    
*   [fit method](https://keras.io/api/models/model_training_apis/#fit-method)
    
*   [evaluate method](https://keras.io/api/models/model_training_apis/#evaluate-method)
    
*   [predict method](https://keras.io/api/models/model_training_apis/#predict-method)
    
*   [train\_on\_batch method](https://keras.io/api/models/model_training_apis/#train_on_batch-method)
    
*   [test\_on\_batch method](https://keras.io/api/models/model_training_apis/#test_on_batch-method)
    
*   [predict\_on\_batch method](https://keras.io/api/models/model_training_apis/#predict_on_batch-method)
    
*   [History class](https://keras.io/api/models/model_training_apis/#history-class)
    

### [Saving & serialization](https://keras.io/api/models/model_saving_apis/)

*   [Whole model saving & loading](https://keras.io/api/models/model_saving_apis/model_saving_and_loading)
    
*   [Weights-only saving & loading](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading)
    
*   [Model config serialization](https://keras.io/api/models/model_saving_apis/model_config_serialization)
    
*   [Model export for inference](https://keras.io/api/models/model_saving_apis/export)
    
*   [Serialization utilities](https://keras.io/api/models/model_saving_apis/serialization_utils)
    
*   [Keras weights file editor](https://keras.io/api/models/model_saving_apis/keras_file_editor)
    

### [Knowledge distillation](https://keras.io/api/models/distillation/)

*   [Distiller model](https://keras.io/api/models/distillation/distiller)
    
*   [Base distillation loss](https://keras.io/api/models/distillation/distillation_loss)
    
*   [Logits distillation loss](https://keras.io/api/models/distillation/logits_distillation)
    
*   [Feature distillation loss](https://keras.io/api/models/distillation/feature_distillation)
    

[Models API](https://keras.io/api/models/#models-api)

[Models API overview](https://keras.io/api/models/#models-api-overview)

[The Model class](https://keras.io/api/models/#the-model-class)

[The Sequential class](https://keras.io/api/models/#the-sequential-class)

[Model training APIs](https://keras.io/api/models/#model-training-apis)

[Saving & serialization](https://keras.io/api/models/#saving-amp-serialization)

[Knowledge distillation](https://keras.io/api/models/#knowledge-distillation)