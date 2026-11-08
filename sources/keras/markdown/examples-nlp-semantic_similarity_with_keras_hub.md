None

[Code examples](https://keras.io/examples/)

[Computer Vision](https://keras.io/examples/vision/)
 [Natural Language Processing](https://keras.io/examples/nlp/)
 [Text classification from scratch](https://keras.io/examples/nlp/text_classification_from_scratch/)
 [Review Classification using Active Learning](https://keras.io/examples/nlp/active_learning_review_classification/)
 [Text Classification using FNet](https://keras.io/examples/nlp/fnet_classification_with_keras_hub/)
 [Large-scale multi-label text classification](https://keras.io/examples/nlp/multi_label_classification/)
 [Text classification with Transformer](https://keras.io/examples/nlp/text_classification_with_transformer/)
 [Text classification with Switch Transformer](https://keras.io/examples/nlp/text_classification_with_switch_transformer/)
 [Text classification using Decision Forests and pretrained embeddings](https://keras.io/examples/nlp/tweet-classification-using-tfdf/)
 [Using pre-trained word embeddings](https://keras.io/examples/nlp/pretrained_word_embeddings/)
 [Bidirectional LSTM on IMDB](https://keras.io/examples/nlp/bidirectional_lstm_imdb/)
 [Data Parallel Training with KerasHub and tf.distribute](https://keras.io/examples/nlp/data_parallel_training_with_keras_hub/)
 [MultipleChoice Task with Transfer Learning](https://keras.io/examples/nlp/multiple_choice_task_with_transfer_learning/)
 [English-to-Spanish translation with KerasHub](https://keras.io/examples/nlp/neural_machine_translation_with_keras_hub/)
 [English-to-Spanish translation with a sequence-to-sequence Transformer](https://keras.io/examples/nlp/neural_machine_translation_with_transformer/)
 [Character-level recurrent sequence-to-sequence model](https://keras.io/examples/nlp/lstm_seq2seq/)
 [Multimodal entailment](https://keras.io/examples/nlp/multimodal_entailment/)
 [Named Entity Recognition using Transformers](https://keras.io/examples/nlp/ner_transformers/)
 [Text Extraction with BERT](https://keras.io/examples/nlp/text_extraction_with_bert/)
 [Sequence to sequence learning for performing number addition](https://keras.io/examples/nlp/addition_rnn/)
 [Semantic Similarity with KerasHub](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/)
 [Semantic Similarity with BERT](https://keras.io/examples/nlp/semantic_similarity_with_bert/)
 [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)
 [End-to-end Masked Language Modeling with BERT](https://keras.io/examples/nlp/masked_language_modeling/)
 [Abstractive Text Summarization with BART](https://keras.io/examples/nlp/abstractive_summarization_with_bart/)
 [Parameter-efficient fine-tuning of GPT-2 with LoRA](https://keras.io/examples/nlp/parameter_efficient_finetuning_of_gpt2_with_lora/)
 [Structured Data](https://keras.io/examples/structured_data/)
 [Timeseries](https://keras.io/examples/timeseries/)
 [Generative Deep Learning](https://keras.io/examples/generative/)
 [Audio Data](https://keras.io/examples/audio/)
 [Reinforcement Learning](https://keras.io/examples/rl/)
 [Graph Data](https://keras.io/examples/graph/)
 [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)

► [Code examples](https://keras.io/examples/)
 / [Natural Language Processing](https://keras.io/examples/nlp/)
 / Semantic Similarity with KerasHub

Semantic Similarity with KerasHub
=================================

**Author:** [Anshuman Mishra](https://github.com/shivance/)
  
**Date created:** 2023/02/25  
**Last modified:** 2023/02/25  
**Description:** Use pretrained models from KerasHub for the Semantic Similarity Task.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/semantic_similarity_with_keras_hub.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/semantic_similarity_with_keras_hub.py)

* * *

Introduction
------------

Semantic similarity refers to the task of determining the degree of similarity between two sentences in terms of their meaning. We already saw in [this](https://keras.io/examples/nlp/semantic_similarity_with_bert/)
 example how to use SNLI (Stanford Natural Language Inference) corpus to predict sentence semantic similarity with the HuggingFace Transformers library. In this tutorial we will learn how to use [KerasHub](https://keras.io/keras_hub/)
, an extension of the core Keras API, for the same task. Furthermore, we will discover how KerasHub effectively reduces boilerplate code and simplifies the process of building and utilizing models. For more information on KerasHub, please refer to [KerasHub's official documentation](https://keras.io/keras_hub/)
.

This guide is broken down into the following parts:

1.  _Setup_, task definition, and establishing a baseline.
2.  _Establishing baseline_ with BERT.
3.  _Saving and Reloading_ the model.
4.  _Performing inference_ with the model. 5 _Improving accuracy_ with RoBERTa

* * *

Setup
-----

The following guide uses [Keras Core](https://keras.io/keras_core/)
 to work in any of `tensorflow`, `jax` or `torch`. Support for Keras Core is baked into KerasHub, simply change the `KERAS_BACKEND` environment variable below to change the backend you would like to use. We select the `jax` backend below, which will give us a particularly fast train step below.

Copied!

`!pip install -q --upgrade keras-hub !pip install -q --upgrade keras  # Upgrade to Keras 3.`

Copied!

`import numpy as np import tensorflow as tf import keras import keras_hub import tensorflow_datasets as tfds`

To load the SNLI dataset, we use the tensorflow-datasets library, which contains over 550,000 samples in total. However, to ensure that this example runs quickly, we use only 20% of the training samples.

* * *

Overview of SNLI Dataset
------------------------

Every sample in the dataset contains three components: `hypothesis`, `premise`, and `label`. epresents the original caption provided to the author of the pair, while the hypothesis refers to the hypothesis caption created by the author of the pair. The label is assigned by annotators to indicate the similarity between the two sentences.

The dataset contains three possible similarity label values: Contradiction, Entailment, and Neutral. Contradiction represents completely dissimilar sentences, while Entailment denotes similar meaning sentences. Lastly, Neutral refers to sentences where no clear similarity or dissimilarity can be established between them.

Copied!

`snli_train = tfds.load("snli", split="train[:20%]") snli_val = tfds.load("snli", split="validation") snli_test = tfds.load("snli", split="test")  # Here's an example of how our training samples look like, where we randomly select # four samples: sample = snli_test.batch(4).take(1).get_single_element() sample`

`{'hypothesis': <tf.Tensor: shape=(4,), dtype=string, numpy=  array([b'A girl is entertaining on stage',         b'A group of people posing in front of a body of water.',         b"The group of people aren't inide of the building.",         b'The people are taking a carriage ride.'], dtype=object)>,  'label': <tf.Tensor: shape=(4,), dtype=int64, numpy=array([0, 0, 0, 0])>,  'premise': <tf.Tensor: shape=(4,), dtype=string, numpy=  array([b'A girl in a blue leotard hula hoops on a stage with balloon shapes in the background.',         b'A group of people taking pictures on a walkway in front of a large body of water.',         b'Many people standing outside of a place talking to each other in front of a building that has a sign that says "HI-POINTE."',         b'Three people are riding a carriage pulled by four horses.'],        dtype=object)>}`

### Preprocessing

In our dataset, we have identified that some samples have missing or incorrectly labeled data, which is denoted by a value of -1. To ensure the accuracy and reliability of our model, we simply filter out these samples from our dataset.

Copied!

`def filter_labels(sample):     return sample["label"] >= 0`

Here's a utility function that splits the example into an `(x, y)` tuple that is suitable for `model.fit()`. By default, `keras_hub.models.BertClassifier` will tokenize and pack together raw strings using a `"[SEP]"` token during training. Therefore, this label splitting is all the data preparation that we need to perform.

Copied!

`def split_labels(sample):     x = (sample["hypothesis"], sample["premise"])     y = sample["label"]     return x, y  train_ds = (     snli_train.filter(filter_labels)     .map(split_labels, num_parallel_calls=tf.data.AUTOTUNE)     .batch(16) ) val_ds = (     snli_val.filter(filter_labels)     .map(split_labels, num_parallel_calls=tf.data.AUTOTUNE)     .batch(16) ) test_ds = (     snli_test.filter(filter_labels)     .map(split_labels, num_parallel_calls=tf.data.AUTOTUNE)     .batch(16) )`

* * *

Establishing baseline with BERT.
--------------------------------

We use the BERT model from KerasHub to establish a baseline for our semantic similarity task. The `keras_hub.models.BertClassifier` class attaches a classification head to the BERT Backbone, mapping the backbone outputs to a logit output suitable for a classification task. This significantly reduces the need for custom code.

KerasHub models have built-in tokenization capabilities that handle tokenization by default based on the selected model. However, users can also use custom preprocessing techniques as per their specific needs. If we pass a tuple as input, the model will tokenize all the strings and concatenate them with a `"[SEP]"` separator.

We use this model with pretrained weights, and we can use the `from_preset()` method to use our own preprocessor. For the SNLI dataset, we set `num_classes` to 3.

Copied!

`bert_classifier = keras_hub.models.BertClassifier.from_preset(     "bert_tiny_en_uncased", num_classes=3 )`

Please note that the BERT Tiny model has only 4,386,307 trainable parameters.

KerasHub task models come with compilation defaults. We can now train the model we just instantiated by calling the `fit()` method.

Copied!

`bert_classifier.fit(train_ds, validation_data=val_ds, epochs=1)`

 `6867/6867 ━━━━━━━━━━━━━━━━━━━━ 61s 8ms/step - loss: 0.8732 - sparse_categorical_accuracy: 0.5864 - val_loss: 0.5900 - val_sparse_categorical_accuracy: 0.7602  <keras.src.callbacks.history.History at 0x7f4660171fc0>`

Our BERT classifier achieved an accuracy of around 76% on the validation split. Now, let's evaluate its performance on the test split.

### Evaluate the performance of the trained model on test data.

Copied!

`bert_classifier.evaluate(test_ds)`

 `614/614 ━━━━━━━━━━━━━━━━━━━━ 2s 3ms/step - loss: 0.5815 - sparse_categorical_accuracy: 0.7628  [0.5895748734474182, 0.7618078589439392]`

Our baseline BERT model achieved a similar accuracy of around 76% on the test split. Now, let's try to improve its performance by recompiling the model with a slightly higher learning rate.

Copied!

`bert_classifier = keras_hub.models.BertClassifier.from_preset(     "bert_tiny_en_uncased", num_classes=3 ) bert_classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.Adam(5e-5),     metrics=["accuracy"], )  bert_classifier.fit(train_ds, validation_data=val_ds, epochs=1) bert_classifier.evaluate(test_ds)`

 `6867/6867 ━━━━━━━━━━━━━━━━━━━━ 59s 8ms/step - accuracy: 0.6007 - loss: 0.8636 - val_accuracy: 0.7648 - val_loss: 0.5800  614/614 ━━━━━━━━━━━━━━━━━━━━ 2s 3ms/step - accuracy: 0.7700 - loss: 0.5692  [0.578984260559082, 0.7686278820037842]`

Just tweaking the learning rate alone was not enough to boost performance, which stayed right around 76%. Let's try again, but this time with [`keras.optimizers.AdamW`](https://keras.io/api/optimizers/adamw#adamw-class)
, and a learning rate schedule.

Copied!

``class TriangularSchedule(keras.optimizers.schedules.LearningRateSchedule):     """Linear ramp up for `warmup` steps, then linear decay to zero at `total` steps."""      def __init__(self, rate, warmup, total):         self.rate = rate         self.warmup = warmup         self.total = total      def get_config(self):         config = {"rate": self.rate, "warmup": self.warmup, "total": self.total}         return config      def __call__(self, step):         step = keras.ops.cast(step, dtype="float32")         rate = keras.ops.cast(self.rate, dtype="float32")         warmup = keras.ops.cast(self.warmup, dtype="float32")         total = keras.ops.cast(self.total, dtype="float32")          warmup_rate = rate * step / self.warmup         cooldown_rate = rate * (total - step) / (total - warmup)         triangular_rate = keras.ops.minimum(warmup_rate, cooldown_rate)         return keras.ops.maximum(triangular_rate, 0.0)  bert_classifier = keras_hub.models.BertClassifier.from_preset(     "bert_tiny_en_uncased", num_classes=3 )  # Get the total count of training batches. # This requires walking the dataset to filter all -1 labels. epochs = 3 total_steps = sum(1 for _ in train_ds.as_numpy_iterator()) * epochs warmup_steps = int(total_steps * 0.2)  bert_classifier.compile(     loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),     optimizer=keras.optimizers.AdamW(         TriangularSchedule(1e-4, warmup_steps, total_steps)     ),     metrics=["accuracy"], )  bert_classifier.fit(train_ds, validation_data=val_ds, epochs=epochs)``

`Epoch 1/3  6867/6867 ━━━━━━━━━━━━━━━━━━━━ 59s 8ms/step - accuracy: 0.5457 - loss: 0.9317 - val_accuracy: 0.7633 - val_loss: 0.5825 Epoch 2/3  6867/6867 ━━━━━━━━━━━━━━━━━━━━ 55s 8ms/step - accuracy: 0.7291 - loss: 0.6515 - val_accuracy: 0.7809 - val_loss: 0.5399 Epoch 3/3  6867/6867 ━━━━━━━━━━━━━━━━━━━━ 55s 8ms/step - accuracy: 0.7708 - loss: 0.5695 - val_accuracy: 0.7918 - val_loss: 0.5214  <keras.src.callbacks.history.History at 0x7f45645b3370>`

Success! With the learning rate scheduler and the `AdamW` optimizer, our validation accuracy improved to around 79%.

Now, let's evaluate our final model on the test set and see how it performs.

Copied!

`bert_classifier.evaluate(test_ds)`

 `614/614 ━━━━━━━━━━━━━━━━━━━━ 2s 3ms/step - accuracy: 0.7956 - loss: 0.5128  [0.5245093703269958, 0.7890879511833191]`

Our Tiny BERT model achieved an accuracy of approximately 79% on the test set with the use of a learning rate scheduler. This is a significant improvement over our previous results. Fine-tuning a pretrained BERT model can be a powerful tool in natural language processing tasks, and even a small model like Tiny BERT can achieve impressive results.

Let's save our model for now and move on to learning how to perform inference with it.

* * *

Save and Reload the model
-------------------------

Copied!

`bert_classifier.save("bert_classifier.keras") restored_model = keras.models.load_model("bert_classifier.keras") restored_model.evaluate(test_ds)`

 `614/614 ━━━━━━━━━━━━━━━━━━━━ 2s 3ms/step - loss: 0.5128 - sparse_categorical_accuracy: 0.7956  [0.5245093703269958, 0.7890879511833191]`

* * *

Performing inference with the model.
------------------------------------

Let's see how to perform inference with KerasHub models

Copied!

`# Convert to Hypothesis-Premise pair, for forward pass through model sample = (sample["hypothesis"], sample["premise"]) sample`

`(<tf.Tensor: shape=(4,), dtype=string, numpy=  array([b'A girl is entertaining on stage',         b'A group of people posing in front of a body of water.',         b"The group of people aren't inide of the building.",         b'The people are taking a carriage ride.'], dtype=object)>,  <tf.Tensor: shape=(4,), dtype=string, numpy=  array([b'A girl in a blue leotard hula hoops on a stage with balloon shapes in the background.',         b'A group of people taking pictures on a walkway in front of a large body of water.',         b'Many people standing outside of a place talking to each other in front of a building that has a sign that says "HI-POINTE."',         b'Three people are riding a carriage pulled by four horses.'],        dtype=object)>)`

The default preprocessor in KerasHub models handles input tokenization automatically, so we don't need to perform tokenization explicitly.

Copied!

`predictions = bert_classifier.predict(sample)  def softmax(x):     return np.exp(x) / np.exp(x).sum(axis=0)  # Get the class predictions with maximum probabilities predictions = softmax(predictions)`

 `1/1 ━━━━━━━━━━━━━━━━━━━━ 1s 711ms/step`

* * *

Improving accuracy with RoBERTa
-------------------------------

Now that we have established a baseline, we can attempt to improve our results by experimenting with different models. Thanks to KerasHub, fine-tuning a RoBERTa checkpoint on the same dataset is easy with just a few lines of code.

Copied!

`# Inittializing a RoBERTa from preset roberta_classifier = keras_hub.models.RobertaClassifier.from_preset(     "roberta_base_en", num_classes=3 )  roberta_classifier.fit(train_ds, validation_data=val_ds, epochs=1)  roberta_classifier.evaluate(test_ds)`

 `6867/6867 ━━━━━━━━━━━━━━━━━━━━ 2049s 297ms/step - loss: 0.5509 - sparse_categorical_accuracy: 0.7740 - val_loss: 0.3292 - val_sparse_categorical_accuracy: 0.8789  614/614 ━━━━━━━━━━━━━━━━━━━━ 56s 88ms/step - loss: 0.3307 - sparse_categorical_accuracy: 0.8784  [0.33771008253097534, 0.874796450138092]`

The RoBERTa base model has significantly more trainable parameters than the BERT Tiny model, with almost 30 times as many at 124,645,635 parameters. As a result, it took approximately 1.5 hours to train on a P100 GPU. However, the performance improvement was substantial, with accuracy increasing to 88% on both the validation and test splits. With RoBERTa, we were able to fit a maximum batch size of 16 on our P100 GPU.

Despite using a different model, the steps to perform inference with RoBERTa are the same as with BERT!

Copied!

`predictions = roberta_classifier.predict(sample) print(tf.math.argmax(predictions, axis=1).numpy())`

 `1/1 ━━━━━━━━━━━━━━━━━━━━ 4s 4s/step [0 0 0 0]`

We hope this tutorial has been helpful in demonstrating the ease and effectiveness of using KerasHub and BERT for semantic similarity tasks.

Throughout this tutorial, we demonstrated how to use a pretrained BERT model to establish a baseline and improve performance by training a larger RoBERTa model using just a few lines of code.

The KerasHub toolbox provides a range of modular building blocks for preprocessing text, including pretrained state-of-the-art models and low-level Transformer Encoder layers. We believe that this makes experimenting with natural language solutions more accessible and efficient.

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 14: Text classification](https://deeplearningwithpython.io/chapters/chapter14_text-classification)
    
*   [Chapter 15: Language models and the Transformer](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer)
    

[Semantic Similarity with KerasHub](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#semantic-similarity-with-kerashub)

[Introduction](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#introduction)

[Setup](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#setup)

[Overview of SNLI Dataset](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#overview-of-snli-dataset)

[Preprocessing](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#preprocessing)

[Establishing baseline with BERT.](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#establishing-baseline-with-bert)

[Evaluate the performance of the trained model on test data.](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#evaluate-the-performance-of-the-trained-model-on-test-data)

[Save and Reload the model](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#save-and-reload-the-model)

[Performing inference with the model.](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#performing-inference-with-the-model)

[Improving accuracy with RoBERTa](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#improving-accuracy-with-roberta)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/nlp/semantic_similarity_with_keras_hub/#relevant-chapters-from-deep-learning-with-python)