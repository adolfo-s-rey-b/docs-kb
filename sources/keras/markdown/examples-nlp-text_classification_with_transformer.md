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
 / Text classification with Transformer

Text classification with Transformer
====================================

**Author:** [Apoorv Nandan](https://twitter.com/NandanApoorv)
  
**Date created:** 2020/05/10  
**Last modified:** 2024/01/18  
**Description:** Implement a Transformer block as a Keras layer and use it for text classification.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/text_classification_with_transformer.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/text_classification_with_transformer.py)

* * *

Setup
-----

Copied!

`import keras from keras import ops from keras import layers`

* * *

Implement a Transformer block as a layer
----------------------------------------

Copied!

`class TransformerBlock(layers.Layer):     def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):         super().__init__()         self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embed_dim)         self.ffn = keras.Sequential(             [layers.Dense(ff_dim, activation="relu"), layers.Dense(embed_dim),]         )         self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)         self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)         self.dropout1 = layers.Dropout(rate)         self.dropout2 = layers.Dropout(rate)      def call(self, inputs):         attn_output = self.att(inputs, inputs)         attn_output = self.dropout1(attn_output)         out1 = self.layernorm1(inputs + attn_output)         ffn_output = self.ffn(out1)         ffn_output = self.dropout2(ffn_output)         return self.layernorm2(out1 + ffn_output)`

* * *

Implement embedding layer
-------------------------

Two separate embedding layers, one for tokens, one for token index (positions).

Copied!

`class TokenAndPositionEmbedding(layers.Layer):     def __init__(self, maxlen, vocab_size, embed_dim):         super().__init__()         self.token_emb = layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)         self.pos_emb = layers.Embedding(input_dim=maxlen, output_dim=embed_dim)      def call(self, x):         maxlen = ops.shape(x)[-1]         positions = ops.arange(start=0, stop=maxlen, step=1)         positions = self.pos_emb(positions)         x = self.token_emb(x)         return x + positions`

* * *

Download and prepare dataset
----------------------------

Copied!

`vocab_size = 20000  # Only consider the top 20k words maxlen = 200  # Only consider the first 200 words of each movie review (x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=vocab_size) print(len(x_train), "Training sequences") print(len(x_val), "Validation sequences") x_train = keras.utils.pad_sequences(x_train, maxlen=maxlen) x_val = keras.utils.pad_sequences(x_val, maxlen=maxlen)`

`Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz 17465344/17464789 [==============================] - 0s 0us/step  <string>:6: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray /usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/datasets/imdb.py:159: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray   x_train, y_train = np.array(xs[:idx]), np.array(labels[:idx]) /usr/local/lib/python3.6/dist-packages/tensorflow/python/keras/datasets/imdb.py:160: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray   x_test, y_test = np.array(xs[idx:]), np.array(labels[idx:])  25000 Training sequences 25000 Validation sequences`

* * *

Create classifier model using transformer layer
-----------------------------------------------

Transformer layer outputs one vector for each time step of our input sequence. Here, we take the mean across all time steps and use a feed forward network on top of it to classify text.

Copied!

`embed_dim = 32  # Embedding size for each token num_heads = 2  # Number of attention heads ff_dim = 32  # Hidden layer size in feed forward network inside transformer  inputs = layers.Input(shape=(maxlen,)) embedding_layer = TokenAndPositionEmbedding(maxlen, vocab_size, embed_dim) x = embedding_layer(inputs) transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim) x = transformer_block(x) x = layers.GlobalAveragePooling1D()(x) x = layers.Dropout(0.1)(x) x = layers.Dense(20, activation="relu")(x) x = layers.Dropout(0.1)(x) outputs = layers.Dense(2, activation="softmax")(x)  model = keras.Model(inputs=inputs, outputs=outputs)`

* * *

Train and Evaluate
------------------

Copied!

`model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]) history = model.fit(     x_train, y_train, batch_size=32, epochs=2, validation_data=(x_val, y_val) )`

`Epoch 1/2 782/782 [==============================] - 15s 18ms/step - loss: 0.5112 - accuracy: 0.7070 - val_loss: 0.3598 - val_accuracy: 0.8444 Epoch 2/2 782/782 [==============================] - 13s 17ms/step - loss: 0.1942 - accuracy: 0.9297 - val_loss: 0.2977 - val_accuracy: 0.8745`

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 14: Text classification](https://deeplearningwithpython.io/chapters/chapter14_text-classification)
    
*   [Chapter 15: Language models and the Transformer](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer)
    

[Text classification with Transformer](https://keras.io/examples/nlp/text_classification_with_transformer/#text-classification-with-transformer)

[Setup](https://keras.io/examples/nlp/text_classification_with_transformer/#setup)

[Implement a Transformer block as a layer](https://keras.io/examples/nlp/text_classification_with_transformer/#implement-a-transformer-block-as-a-layer)

[Implement embedding layer](https://keras.io/examples/nlp/text_classification_with_transformer/#implement-embedding-layer)

[Download and prepare dataset](https://keras.io/examples/nlp/text_classification_with_transformer/#download-and-prepare-dataset)

[Create classifier model using transformer layer](https://keras.io/examples/nlp/text_classification_with_transformer/#create-classifier-model-using-transformer-layer)

[Train and Evaluate](https://keras.io/examples/nlp/text_classification_with_transformer/#train-and-evaluate)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/nlp/text_classification_with_transformer/#relevant-chapters-from-deep-learning-with-python)