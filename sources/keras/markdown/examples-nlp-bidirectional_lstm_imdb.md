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
 / Bidirectional LSTM on IMDB

Bidirectional LSTM on IMDB
==========================

**Author:** [fchollet](https://twitter.com/fchollet)
  
**Date created:** 2020/05/03  
**Last modified:** 2020/05/03  
**Description:** Train a 2-layer bidirectional LSTM on the IMDB movie review sentiment classification dataset.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/bidirectional_lstm_imdb.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/bidirectional_lstm_imdb.py)

* * *

Setup
-----

Copied!

`import numpy as np import keras from keras import layers  max_features = 20000  # Only consider the top 20k words maxlen = 200  # Only consider the first 200 words of each movie review`

* * *

Build the model
---------------

Copied!

`# Input for variable-length sequences of integers inputs = keras.Input(shape=(None,), dtype="int32") # Embed each integer in a 128-dimensional vector x = layers.Embedding(max_features, 128)(inputs) # Add 2 bidirectional LSTMs x = layers.Bidirectional(layers.LSTM(64, return_sequences=True))(x) x = layers.Bidirectional(layers.LSTM(64))(x) # Add a classifier outputs = layers.Dense(1, activation="sigmoid")(x) model = keras.Model(inputs, outputs) model.summary()`

Model: "functional\_1"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape              ┃    Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ input\_layer (InputLayer)        │ (None, None)              │          0 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ embedding (Embedding)           │ (None, None, 128)         │  2,560,000 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ bidirectional (Bidirectional)   │ (None, None, 128)         │     98,816 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ bidirectional\_1 (Bidirectional) │ (None, 128)               │     98,816 │
├─────────────────────────────────┼───────────────────────────┼────────────┤
│ dense (Dense)                   │ (None, 1)                 │        129 │
└─────────────────────────────────┴───────────────────────────┴────────────┘

 Total params: 2,757,761 (10.52 MB)

 Trainable params: 2,757,761 (10.52 MB)

 Non-trainable params: 0 (0.00 B)

* * *

Load the IMDB movie review sentiment data
-----------------------------------------

Copied!

`(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(     num_words=max_features ) print(len(x_train), "Training sequences") print(len(x_val), "Validation sequences") # Use pad_sequence to standardize sequence length: # this will truncate sequences longer than 200 words and zero-pad sequences shorter than 200 words. x_train = keras.utils.pad_sequences(x_train, maxlen=maxlen) x_val = keras.utils.pad_sequences(x_val, maxlen=maxlen)`

`Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz  17464789/17464789 ━━━━━━━━━━━━━━━━━━━━ 0s 0us/step 25000 Training sequences 25000 Validation sequences`

* * *

Train and evaluate the model
----------------------------

You can use the trained model hosted on [Hugging Face Hub](https://huggingface.co/keras-io/bidirectional-lstm-imdb)
 and try the demo on [Hugging Face Spaces](https://huggingface.co/spaces/keras-io/bidirectional_lstm_imdb)
.

Copied!

`model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]) model.fit(x_train, y_train, batch_size=32, epochs=2, validation_data=(x_val, y_val))`

`Epoch 1/2  782/782 ━━━━━━━━━━━━━━━━━━━━ 61s 75ms/step - accuracy: 0.7540 - loss: 0.4697 - val_accuracy: 0.8269 - val_loss: 0.4202 Epoch 2/2  782/782 ━━━━━━━━━━━━━━━━━━━━ 54s 69ms/step - accuracy: 0.9151 - loss: 0.2263 - val_accuracy: 0.8428 - val_loss: 0.3650  <keras.src.callbacks.history.History at 0x7f3efd663850>`

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 14: Text classification](https://deeplearningwithpython.io/chapters/chapter14_text-classification)
    

[Bidirectional LSTM on IMDB](https://keras.io/examples/nlp/bidirectional_lstm_imdb/#bidirectional-lstm-on-imdb)

[Setup](https://keras.io/examples/nlp/bidirectional_lstm_imdb/#setup)

[Build the model](https://keras.io/examples/nlp/bidirectional_lstm_imdb/#build-the-model)

[Load the IMDB movie review sentiment data](https://keras.io/examples/nlp/bidirectional_lstm_imdb/#load-the-imdb-movie-review-sentiment-data)

[Train and evaluate the model](https://keras.io/examples/nlp/bidirectional_lstm_imdb/#train-and-evaluate-the-model)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/nlp/bidirectional_lstm_imdb/#relevant-chapters-from-deep-learning-with-python)