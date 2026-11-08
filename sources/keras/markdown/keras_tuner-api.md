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
 / KerasTuner API documentation

KerasTuner API documentation
============================

The **Hyperparameters** class is used to specify a set of hyperparameters and their values, to be used in the model building function.

The **Tuner** subclasses corresponding to different tuning algorithms are called directly by the user to start the search or to get the best models.

The **Oracle** subclasses are the core search algorithms, receiving model evaluation results from the Tuner and providing new hyperparameter values.

The **HyperModel** subclasses are predefined search spaces for certain model families like ResNet and XceptionNet.

### [HyperParameters](https://keras.io/keras_tuner/api/hyperparameters/)

*   [HyperParameters class](https://keras.io/keras_tuner/api/hyperparameters/#hyperparameters-class)
    
*   [Boolean method](https://keras.io/keras_tuner/api/hyperparameters/#boolean-method)
    
*   [Choice method](https://keras.io/keras_tuner/api/hyperparameters/#choice-method)
    
*   [Fixed method](https://keras.io/keras_tuner/api/hyperparameters/#fixed-method)
    
*   [Float method](https://keras.io/keras_tuner/api/hyperparameters/#float-method)
    
*   [Int method](https://keras.io/keras_tuner/api/hyperparameters/#int-method)
    
*   [conditional\_scope method](https://keras.io/keras_tuner/api/hyperparameters/#conditional_scope-method)
    
*   [get method](https://keras.io/keras_tuner/api/hyperparameters/#get-method)
    

### [Tuners](https://keras.io/keras_tuner/api/tuners/)

*   [The base Tuner class](https://keras.io/keras_tuner/api/tuners/base_tuner)
    
*   [Objective class](https://keras.io/keras_tuner/api/tuners/objective)
    
*   [RandomSearch Tuner](https://keras.io/keras_tuner/api/tuners/random)
    
*   [GridSearch Tuner](https://keras.io/keras_tuner/api/tuners/grid)
    
*   [BayesianOptimization Tuner](https://keras.io/keras_tuner/api/tuners/bayesian)
    
*   [Hyperband Tuner](https://keras.io/keras_tuner/api/tuners/hyperband)
    
*   [Sklearn Tuner](https://keras.io/keras_tuner/api/tuners/sklearn)
    

### [Oracles](https://keras.io/keras_tuner/api/oracles/)

*   [The base Oracle class](https://keras.io/keras_tuner/api/oracles/base_oracle)
    
*   [@synchronized decorator](https://keras.io/keras_tuner/api/oracles/synchronized)
    
*   [RandomSearch Oracle](https://keras.io/keras_tuner/api/oracles/random)
    
*   [GridSearch Oracle](https://keras.io/keras_tuner/api/oracles/grid)
    
*   [BayesianOptimization Oracle](https://keras.io/keras_tuner/api/oracles/bayesian)
    
*   [Hyperband Oracle](https://keras.io/keras_tuner/api/oracles/hyperband)
    

### [HyperModels](https://keras.io/keras_tuner/api/hypermodels/)

*   [The base HyperModel class](https://keras.io/keras_tuner/api/hypermodels/base_hypermodel)
    
*   [HyperEfficientNet](https://keras.io/keras_tuner/api/hypermodels/hyper_efficientnet)
    
*   [HyperImageAugment](https://keras.io/keras_tuner/api/hypermodels/hyper_image_augment)
    
*   [HyperResNet](https://keras.io/keras_tuner/api/hypermodels/hyper_resnet)
    
*   [HyperXception](https://keras.io/keras_tuner/api/hypermodels/hyper_xception)
    

### [Errors](https://keras.io/keras_tuner/api/errors/)

*   [FailedTrialError class](https://keras.io/keras_tuner/api/errors/#failedtrialerror-class)
    
*   [FatalError class](https://keras.io/keras_tuner/api/errors/#fatalerror-class)
    
*   [FatalValueError class](https://keras.io/keras_tuner/api/errors/#fatalvalueerror-class)
    
*   [FatalTypeError class](https://keras.io/keras_tuner/api/errors/#fataltypeerror-class)
    
*   [FatalRuntimeError class](https://keras.io/keras_tuner/api/errors/#fatalruntimeerror-class)
    

[KerasTuner API documentation](https://keras.io/keras_tuner/api/#kerastuner-api-documentation)

[HyperParameters](https://keras.io/keras_tuner/api/#hyperparameters)

[Tuners](https://keras.io/keras_tuner/api/#tuners)

[Oracles](https://keras.io/keras_tuner/api/#oracles)

[HyperModels](https://keras.io/keras_tuner/api/#hypermodels)

[Errors](https://keras.io/keras_tuner/api/#errors)