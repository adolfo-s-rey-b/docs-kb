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
 / KerasTuner Oracles

KerasTuner Oracles
==================

The `Oracle` class is the base class for all the search algorithms in KerasTuner. An `Oracle` object receives evaluation results for a model (from a `Tuner` class) and generates new hyperparameter values.

The built-in `Oracle` classes are `RandomSearchOracle`, `BayesianOptimizationOracle`, and `HyperbandOracle`.

You can also write your own tuning algorithm by subclassing the `Oracle` class.

### [The base Oracle class](https://keras.io/keras_tuner/api/oracles/base_oracle/)

*   [Oracle class](https://keras.io/keras_tuner/api/oracles/base_oracle/#oracle-class)
    
*   [create\_trial function](https://keras.io/keras_tuner/api/oracles/base_oracle/#wrapped_func-function)
    
*   [end\_trial function](https://keras.io/keras_tuner/api/oracles/base_oracle/#wrapped_func-function)
    
*   [get\_best\_trials method](https://keras.io/keras_tuner/api/oracles/base_oracle/#get_best_trials-method)
    
*   [get\_state method](https://keras.io/keras_tuner/api/oracles/base_oracle/#get_state-method)
    
*   [set\_state method](https://keras.io/keras_tuner/api/oracles/base_oracle/#set_state-method)
    
*   [score\_trial method](https://keras.io/keras_tuner/api/oracles/base_oracle/#score_trial-method)
    
*   [populate\_space method](https://keras.io/keras_tuner/api/oracles/base_oracle/#populate_space-method)
    
*   [update\_trial function](https://keras.io/keras_tuner/api/oracles/base_oracle/#wrapped_func-function)
    

### [@synchronized decorator](https://keras.io/keras_tuner/api/oracles/synchronized/)

*   [synchronized function](https://keras.io/keras_tuner/api/oracles/synchronized/#synchronized-function)
    

### [RandomSearch Oracle](https://keras.io/keras_tuner/api/oracles/random/)

*   [RandomSearchOracle class](https://keras.io/keras_tuner/api/oracles/random/#randomsearchoracle-class)
    

### [GridSearch Oracle](https://keras.io/keras_tuner/api/oracles/grid/)

*   [GridSearchOracle class](https://keras.io/keras_tuner/api/oracles/grid/#gridsearchoracle-class)
    

### [BayesianOptimization Oracle](https://keras.io/keras_tuner/api/oracles/bayesian/)

*   [BayesianOptimizationOracle class](https://keras.io/keras_tuner/api/oracles/bayesian/#bayesianoptimizationoracle-class)
    

### [Hyperband Oracle](https://keras.io/keras_tuner/api/oracles/hyperband/)

*   [HyperbandOracle class](https://keras.io/keras_tuner/api/oracles/hyperband/#hyperbandoracle-class)
    

[KerasTuner Oracles](https://keras.io/keras_tuner/api/oracles/#kerastuner-oracles)

[The base Oracle class](https://keras.io/keras_tuner/api/oracles/#the-base-oracle-class)

[@synchronized decorator](https://keras.io/keras_tuner/api/oracles/#synchronized-decorator)

[RandomSearch Oracle](https://keras.io/keras_tuner/api/oracles/#randomsearch-oracle)

[GridSearch Oracle](https://keras.io/keras_tuner/api/oracles/#gridsearch-oracle)

[BayesianOptimization Oracle](https://keras.io/keras_tuner/api/oracles/#bayesianoptimization-oracle)

[Hyperband Oracle](https://keras.io/keras_tuner/api/oracles/#hyperband-oracle)