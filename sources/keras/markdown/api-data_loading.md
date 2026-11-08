None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Image data loading](https://keras.io/api/data_loading/image/)
 [Timeseries data loading](https://keras.io/api/data_loading/timeseries/)
 [Text data loading](https://keras.io/api/data_loading/text/)
 [Audio data loading](https://keras.io/api/data_loading/audio/)
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
 / Data loading

Data loading
============

Keras data loading utilities, located in `keras.utils`, help you go from raw data on disk to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 object that can be used to efficiently train a model.

These loading utilites can be combined with [preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 to futher transform your input dataset before training.

Here's a quick example: let's say you have 10 folders, each containing 10,000 images from a different category, and you want to train a classifier that maps an image to its category.

Your training data folder would look like this:

Copied!

`training_data/ ...class_a/ ......a_image_1.jpg ......a_image_2.jpg ...class_b/ ......b_image_1.jpg ......b_image_2.jpg etc.`

You may also have a validation data folder `validation_data/` structured in the same way.

You could simply do:

Copied!

`import keras  train_ds = keras.utils.image_dataset_from_directory(     directory='training_data/',     labels='inferred',     label_mode='categorical',     batch_size=32,     image_size=(256, 256)) validation_ds = keras.utils.image_dataset_from_directory(     directory='validation_data/',     labels='inferred',     label_mode='categorical',     batch_size=32,     image_size=(256, 256))  model = keras.applications.Xception(     weights=None, input_shape=(256, 256, 3), classes=10) model.compile(optimizer='rmsprop', loss='categorical_crossentropy') model.fit(train_ds, epochs=10, validation_data=validation_ds)`

Available dataset loading utilities
-----------------------------------

### [Image data loading](https://keras.io/api/data_loading/image/)

*   [image\_dataset\_from\_directory function](https://keras.io/api/data_loading/image/#image_dataset_from_directory-function)
    
*   [load\_img function](https://keras.io/api/data_loading/image/#load_img-function)
    
*   [img\_to\_array function](https://keras.io/api/data_loading/image/#img_to_array-function)
    
*   [save\_img function](https://keras.io/api/data_loading/image/#save_img-function)
    
*   [array\_to\_img function](https://keras.io/api/data_loading/image/#array_to_img-function)
    

### [Timeseries data loading](https://keras.io/api/data_loading/timeseries/)

*   [timeseries\_dataset\_from\_array function](https://keras.io/api/data_loading/timeseries/#timeseries_dataset_from_array-function)
    
*   [pad\_sequences function](https://keras.io/api/data_loading/timeseries/#pad_sequences-function)
    

### [Text data loading](https://keras.io/api/data_loading/text/)

*   [text\_dataset\_from\_directory function](https://keras.io/api/data_loading/text/#text_dataset_from_directory-function)
    

### [Audio data loading](https://keras.io/api/data_loading/audio/)

*   [audio\_dataset\_from\_directory function](https://keras.io/api/data_loading/audio/#audio_dataset_from_directory-function)
    

[Data loading](https://keras.io/api/data_loading/#data-loading)

[Available dataset loading utilities](https://keras.io/api/data_loading/#available-dataset-loading-utilities)

[Image data loading](https://keras.io/api/data_loading/#image-data-loading)

[Timeseries data loading](https://keras.io/api/data_loading/#timeseries-data-loading)

[Text data loading](https://keras.io/api/data_loading/#text-data-loading)

[Audio data loading](https://keras.io/api/data_loading/#audio-data-loading)