None

[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)

[Getting started](https://keras.io/keras_tuner/getting_started/)
 [Developer guides](https://keras.io/keras_tuner/guides/)
 [API documentation](https://keras.io/keras_tuner/api/)
 [HyperParameters](https://keras.io/keras_tuner/api/hyperparameters/)
 [Tuners](https://keras.io/keras_tuner/api/tuners/)
 [Oracles](https://keras.io/keras_tuner/api/oracles/)
 [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)
 [Errors](https://keras.io/keras_tuner/api/errors/)

► [KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)
 / [API documentation](https://keras.io/keras_tuner/api/)
 / The Tuner classes in KerasTuner

The Tuner classes in KerasTuner
===============================

The base `Tuner` class is the class that manages the hyperparameter search process, including model creation, training, and evaluation. For each trial, a `Tuner` receives new hyperparameter values from an `Oracle` instance. After calling `model.fit(...)`, it sends the evaluation results back to the `Oracle` instance and it retrieves the next set of hyperparameters to try.

There are a few built-in `Tuner` subclasses available for widely-used tuning algorithms: `RandomSearch`, `BayesianOptimization` and `Hyperband`.

You can also subclass the `Tuner` class to customize your tuning process. In particular, you can [override the `run_trial` function](https://keras.io/guides/keras_tuner/custom_tuner/#overriding-runtrial)
 to customize model building and training.

### [The base Tuner class](https://keras.io/keras_tuner/api/tuners/base_tuner/)

*   [Tuner class](https://keras.io/keras_tuner/api/tuners/base_tuner/#tuner-class)
    
*   [get\_best\_hyperparameters method](https://keras.io/keras_tuner/api/tuners/base_tuner/#get_best_hyperparameters-method)
    
*   [get\_best\_models method](https://keras.io/keras_tuner/api/tuners/base_tuner/#get_best_models-method)
    
*   [get\_state method](https://keras.io/keras_tuner/api/tuners/base_tuner/#get_state-method)
    
*   [load\_model method](https://keras.io/keras_tuner/api/tuners/base_tuner/#load_model-method)
    
*   [on\_epoch\_begin method](https://keras.io/keras_tuner/api/tuners/base_tuner/#on_epoch_begin-method)
    
*   [on\_batch\_begin method](https://keras.io/keras_tuner/api/tuners/base_tuner/#on_batch_begin-method)
    
*   [on\_batch\_end method](https://keras.io/keras_tuner/api/tuners/base_tuner/#on_batch_end-method)
    
*   [on\_epoch\_end method](https://keras.io/keras_tuner/api/tuners/base_tuner/#on_epoch_end-method)
    
*   [run\_trial method](https://keras.io/keras_tuner/api/tuners/base_tuner/#run_trial-method)
    
*   [results\_summary method](https://keras.io/keras_tuner/api/tuners/base_tuner/#results_summary-method)
    
*   [save\_model method](https://keras.io/keras_tuner/api/tuners/base_tuner/#save_model-method)
    
*   [search method](https://keras.io/keras_tuner/api/tuners/base_tuner/#search-method)
    
*   [search\_space\_summary method](https://keras.io/keras_tuner/api/tuners/base_tuner/#search_space_summary-method)
    
*   [set\_state method](https://keras.io/keras_tuner/api/tuners/base_tuner/#set_state-method)
    

### [Objective class](https://keras.io/keras_tuner/api/tuners/objective/)

*   [Objective class](https://keras.io/keras_tuner/api/tuners/objective/#objective-class)
    

### [RandomSearch Tuner](https://keras.io/keras_tuner/api/tuners/random/)

*   [RandomSearch class](https://keras.io/keras_tuner/api/tuners/random/#randomsearch-class)
    

### [GridSearch Tuner](https://keras.io/keras_tuner/api/tuners/grid/)

*   [GridSearch class](https://keras.io/keras_tuner/api/tuners/grid/#gridsearch-class)
    

### [BayesianOptimization Tuner](https://keras.io/keras_tuner/api/tuners/bayesian/)

*   [BayesianOptimization class](https://keras.io/keras_tuner/api/tuners/bayesian/#bayesianoptimization-class)
    

### [Hyperband Tuner](https://keras.io/keras_tuner/api/tuners/hyperband/)

*   [Hyperband class](https://keras.io/keras_tuner/api/tuners/hyperband/#hyperband-class)
    

### [Sklearn Tuner](https://keras.io/keras_tuner/api/tuners/sklearn/)

*   [SklearnTuner class](https://keras.io/keras_tuner/api/tuners/sklearn/#sklearntuner-class)
    

[The Tuner classes in KerasTuner](https://keras.io/keras_tuner/api/tuners/#the-tuner-classes-in-kerastuner)

[The base Tuner class](https://keras.io/keras_tuner/api/tuners/#the-base-tuner-class)

[Objective class](https://keras.io/keras_tuner/api/tuners/#objective-class)

[RandomSearch Tuner](https://keras.io/keras_tuner/api/tuners/#randomsearch-tuner)

[GridSearch Tuner](https://keras.io/keras_tuner/api/tuners/#gridsearch-tuner)

[BayesianOptimization Tuner](https://keras.io/keras_tuner/api/tuners/#bayesianoptimization-tuner)

[Hyperband Tuner](https://keras.io/keras_tuner/api/tuners/#hyperband-tuner)

[Sklearn Tuner](https://keras.io/keras_tuner/api/tuners/#sklearn-tuner)