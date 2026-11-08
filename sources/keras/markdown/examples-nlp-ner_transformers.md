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
 / Named Entity Recognition using Transformers

Named Entity Recognition using Transformers
===========================================

**Author:** [Varun Singh](https://www.linkedin.com/in/varunsingh2/)
  
**Date created:** 2021/06/23  
**Last modified:** 2024/04/05  
**Description:** NER using the Transformers and data from CoNLL 2003 shared task.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/ner_transformers.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/ner_transformers.py)

* * *

Introduction
------------

Named Entity Recognition (NER) is the process of identifying named entities in text. Example of named entities are: "Person", "Location", "Organization", "Dates" etc. NER is essentially a token classification task where every token is classified into one or more predetermined categories.

In this exercise, we will train a simple Transformer based model to perform NER. We will be using the data from CoNLL 2003 shared task. For more information about the dataset, please visit [the dataset website](https://www.clips.uantwerpen.be/conll2003/ner/)
. However, since obtaining this data requires an additional step of getting a free license, we will be using HuggingFace's datasets library which contains a processed version of this dataset.

* * *

Install the open source datasets library from HuggingFace
---------------------------------------------------------

We also download the script used to evaluate NER models.

Copied!

`!pip3 install datasets !wget https://raw.githubusercontent.com/sighsmile/conlleval/master/conlleval.py`

`Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.111.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 7502 (7.3K) [text/plain] Saving to: ‘conlleval.py’`

`conlleval.py        100%[===================>]   7.33K  --.-KB/s    in 0s`      

`2023-11-10 16:58:25 (217 MB/s) - ‘conlleval.py’ saved [7502/7502]`

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  import keras from keras import ops import numpy as np import tensorflow as tf from keras import layers from datasets import load_dataset from collections import Counter from conlleval import evaluate`

We will be using the transformer implementation from this fantastic [example](https://keras.io/examples/nlp/text_classification_with_transformer/)
.

Let's start by defining a `TransformerBlock` layer:

Copied!

`class TransformerBlock(layers.Layer):     def __init__(self, embed_dim, num_heads, ff_dim, rate=0.1):         super().__init__()         self.att = keras.layers.MultiHeadAttention(             num_heads=num_heads, key_dim=embed_dim         )         self.ffn = keras.Sequential(             [                 keras.layers.Dense(ff_dim, activation="relu"),                 keras.layers.Dense(embed_dim),             ]         )         self.layernorm1 = keras.layers.LayerNormalization(epsilon=1e-6)         self.layernorm2 = keras.layers.LayerNormalization(epsilon=1e-6)         self.dropout1 = keras.layers.Dropout(rate)         self.dropout2 = keras.layers.Dropout(rate)      def call(self, inputs, training=False):         attn_output = self.att(inputs, inputs)         attn_output = self.dropout1(attn_output, training=training)         out1 = self.layernorm1(inputs + attn_output)         ffn_output = self.ffn(out1)         ffn_output = self.dropout2(ffn_output, training=training)         return self.layernorm2(out1 + ffn_output)`

Next, let's define a `TokenAndPositionEmbedding` layer:

Copied!

`class TokenAndPositionEmbedding(layers.Layer):     def __init__(self, maxlen, vocab_size, embed_dim):         super().__init__()         self.token_emb = keras.layers.Embedding(             input_dim=vocab_size, output_dim=embed_dim         )         self.pos_emb = keras.layers.Embedding(input_dim=maxlen, output_dim=embed_dim)      def call(self, inputs):         maxlen = ops.shape(inputs)[-1]         positions = ops.arange(start=0, stop=maxlen, step=1)         position_embeddings = self.pos_emb(positions)         token_embeddings = self.token_emb(inputs)         return token_embeddings + position_embeddings`

* * *

Build the NER model class as a [`keras.Model`](https://keras.io/api/models/model#model-class)
 subclass
-------------------------------------------------------------------------------------------------------

Copied!

`class NERModel(keras.Model):     def __init__(         self, num_tags, vocab_size, maxlen=128, embed_dim=32, num_heads=2, ff_dim=32     ):         super().__init__()         self.embedding_layer = TokenAndPositionEmbedding(maxlen, vocab_size, embed_dim)         self.transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)         self.dropout1 = layers.Dropout(0.1)         self.ff = layers.Dense(ff_dim, activation="relu")         self.dropout2 = layers.Dropout(0.1)         self.ff_final = layers.Dense(num_tags, activation="softmax")      def call(self, inputs, training=False):         x = self.embedding_layer(inputs)         x = self.transformer_block(x)         x = self.dropout1(x, training=training)         x = self.ff(x)         x = self.dropout2(x, training=training)         x = self.ff_final(x)         return x`

* * *

Load the CoNLL 2003 dataset from the datasets library and process it
--------------------------------------------------------------------

Copied!

`conll_data = load_dataset("conll2003")`

We will export this data to a tab-separated file format which will be easy to read as a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 object.

Copied!

`def export_to_file(export_file_path, data):     with open(export_file_path, "w") as f:         for record in data:             ner_tags = record["ner_tags"]             tokens = record["tokens"]             if len(tokens) > 0:                 f.write(                     str(len(tokens))                     + "\t"                     + "\t".join(tokens)                     + "\t"                     + "\t".join(map(str, ner_tags))                     + "\n"                 )  os.mkdir("data") export_to_file("./data/conll_train.txt", conll_data["train"]) export_to_file("./data/conll_val.txt", conll_data["validation"])`

* * *

Make the NER label lookup table
-------------------------------

NER labels are usually provided in IOB, IOB2 or IOBES formats. Checkout this link for more information: [Wikipedia](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging))

Note that we start our label numbering from 1 since 0 will be reserved for padding. We have a total of 10 labels: 9 from the NER dataset and one for padding.

Copied!

`def make_tag_lookup_table():     iob_labels = ["B", "I"]     ner_labels = ["PER", "ORG", "LOC", "MISC"]     all_labels = [(label1, label2) for label2 in ner_labels for label1 in iob_labels]     all_labels = ["-".join([a, b]) for a, b in all_labels]     all_labels = ["[PAD]", "O"] + all_labels     return dict(zip(range(0, len(all_labels) + 1), all_labels))  mapping = make_tag_lookup_table() print(mapping)`

`{0: '[PAD]', 1: 'O', 2: 'B-PER', 3: 'I-PER', 4: 'B-ORG', 5: 'I-ORG', 6: 'B-LOC', 7: 'I-LOC', 8: 'B-MISC', 9: 'I-MISC'}`

Get a list of all tokens in the training dataset. This will be used to create the vocabulary.

Copied!

``all_tokens = sum(conll_data["train"]["tokens"], []) all_tokens_array = np.array(list(map(str.lower, all_tokens)))  counter = Counter(all_tokens_array) print(len(counter))  num_tags = len(mapping) vocab_size = 20000  # We only take (vocab_size - 2) most commons words from the training data since # the `StringLookup` class uses 2 additional tokens - one denoting an unknown # token and another one denoting a masking token vocabulary = [token for token, count in counter.most_common(vocab_size - 2)]  # The StringLook class will convert tokens to token IDs lookup_layer = keras.layers.StringLookup(vocabulary=vocabulary)``

`21009`

Create 2 new `Dataset` objects from the training and validation data

Copied!

`train_data = tf.data.TextLineDataset("./data/conll_train.txt") val_data = tf.data.TextLineDataset("./data/conll_val.txt")`

Print out one line to make sure it looks good. The first record in the line is the number of tokens. After that we will have all the tokens followed by all the ner tags.

Copied!

`print(list(train_data.take(1).as_numpy_iterator()))`

`[b'9\tEU\trejects\tGerman\tcall\tto\tboycott\tBritish\tlamb\t.\t3\t0\t7\t0\t0\t0\t7\t0\t0']`

We will be using the following map function to transform the data in the dataset:

Copied!

``def map_record_to_training_data(record):     record = tf.strings.split(record, sep="\t")     length = tf.strings.to_number(record[0], out_type=tf.int32)     tokens = record[1 : length + 1]     tags = record[length + 1 :]     tags = tf.strings.to_number(tags, out_type=tf.int64)     tags += 1     return tokens, tags  def lowercase_and_convert_to_ids(tokens):     tokens = tf.strings.lower(tokens)     return lookup_layer(tokens)  # We use `padded_batch` here because each record in the dataset has a # different length. batch_size = 32 train_dataset = (     train_data.map(map_record_to_training_data)     .map(lambda x, y: (lowercase_and_convert_to_ids(x), y))     .padded_batch(batch_size) ) val_dataset = (     val_data.map(map_record_to_training_data)     .map(lambda x, y: (lowercase_and_convert_to_ids(x), y))     .padded_batch(batch_size) )  ner_model = NERModel(num_tags, vocab_size, embed_dim=32, num_heads=4, ff_dim=64)``

We will be using a custom loss function that will ignore the loss from padded tokens.

Copied!

`class CustomNonPaddingTokenLoss(keras.losses.Loss):     def __init__(self, name="custom_ner_loss"):         super().__init__(name=name)      def call(self, y_true, y_pred):         loss_fn = keras.losses.SparseCategoricalCrossentropy(             from_logits=False, reduction=None         )         loss = loss_fn(y_true, y_pred)         mask = ops.cast((y_true > 0), dtype="float32")         loss = loss * mask         return ops.sum(loss) / ops.sum(mask)  loss = CustomNonPaddingTokenLoss()`

* * *

Compile and fit the model
-------------------------

Copied!

`tf.config.run_functions_eagerly(True) ner_model.compile(optimizer="adam", loss=loss) ner_model.fit(train_dataset, epochs=10)  def tokenize_and_convert_to_ids(text):     tokens = text.split()     return lowercase_and_convert_to_ids(tokens)  # Sample inference using the trained model sample_input = tokenize_and_convert_to_ids(     "eu rejects german call to boycott british lamb" ) sample_input = ops.reshape(sample_input, shape=[1, -1]) print(sample_input)  output = ner_model.predict(sample_input) prediction = np.argmax(output, axis=-1)[0] prediction = [mapping[i] for i in prediction]  # eu -> B-ORG, german -> B-MISC, british -> B-MISC print(prediction)`

`Epoch 1/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 300s 671ms/step - loss: 0.9260 Epoch 2/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.2909 Epoch 3/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.1589 Epoch 4/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.1176 Epoch 5/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.0941 Epoch 6/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.0747 Epoch 7/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.0597 Epoch 8/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.0534 Epoch 9/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.0459 Epoch 10/10  439/439 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step - loss: 0.0408 tf.Tensor([[  988 10950   204   628     6  3938   215  5773]], shape=(1, 8), dtype=int64)  1/1 ━━━━━━━━━━━━━━━━━━━━ 1s 600ms/step ['B-ORG', 'O', 'B-MISC', 'O', 'O', 'O', 'B-MISC', 'O']`

* * *

Metrics calculation
-------------------

Here is a function to calculate the metrics. The function calculates F1 score for the overall NER dataset as well as individual scores for each NER tag.

Copied!

`def calculate_metrics(dataset):     all_true_tag_ids, all_predicted_tag_ids = [], []      for x, y in dataset:         output = ner_model.predict(x, verbose=0)         predictions = ops.argmax(output, axis=-1)         predictions = ops.reshape(predictions, [-1])          true_tag_ids = ops.reshape(y, [-1])          mask = (true_tag_ids > 0) & (predictions > 0)         true_tag_ids = true_tag_ids[mask]         predicted_tag_ids = predictions[mask]          all_true_tag_ids.append(true_tag_ids)         all_predicted_tag_ids.append(predicted_tag_ids)      all_true_tag_ids = np.concatenate(all_true_tag_ids)     all_predicted_tag_ids = np.concatenate(all_predicted_tag_ids)      predicted_tags = [mapping[tag] for tag in all_predicted_tag_ids]     real_tags = [mapping[tag] for tag in all_true_tag_ids]      evaluate(real_tags, predicted_tags)  calculate_metrics(val_dataset)`

`processed 51362 tokens with 5942 phrases; found: 5659 phrases; correct: 3941. accuracy:  64.49%; (non-O) accuracy:  93.23%; precision:  69.64%; recall:  66.32%; FB1:  67.94               LOC: precision:  82.77%; recall:  79.26%; FB1:  80.98  1759              MISC: precision:  74.94%; recall:  68.11%; FB1:  71.36  838               ORG: precision:  55.94%; recall:  65.32%; FB1:  60.27  1566               PER: precision:  65.57%; recall:  53.26%; FB1:  58.78  1496`

* * *

Conclusions
-----------

In this exercise, we created a simple transformer based named entity recognition model. We trained it on the CoNLL 2003 shared task data and got an overall F1 score of around 70%. State of the art NER models fine-tuned on pretrained models such as BERT or ELECTRA can easily get much higher F1 score -between 90-95% on this dataset owing to the inherent knowledge of words as part of the pretraining process and the usage of subword tokenization.

You can use the trained model hosted on [Hugging Face Hub](https://huggingface.co/keras-io/ner-with-transformers)
 and try the demo on [Hugging Face Spaces](https://huggingface.co/spaces/keras-io/ner_with_transformers)
."""

* * *

Relevant Chapters from Deep Learning with Python
------------------------------------------------

*   [Chapter 14: Text classification](https://deeplearningwithpython.io/chapters/chapter14_text-classification)
    
*   [Chapter 15: Language models and the Transformer](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer)
    

[Named Entity Recognition using Transformers](https://keras.io/examples/nlp/ner_transformers/#named-entity-recognition-using-transformers)

[Introduction](https://keras.io/examples/nlp/ner_transformers/#introduction)

[Install the open source datasets library from HuggingFace](https://keras.io/examples/nlp/ner_transformers/#install-the-open-source-datasets-library-from-huggingface)

[Build the NER model class as a `keras.Model` subclass](https://keras.io/examples/nlp/ner_transformers/#build-the-ner-model-class-as-a-kerasmodel-subclass)

[Load the CoNLL 2003 dataset from the datasets library and process it](https://keras.io/examples/nlp/ner_transformers/#load-the-conll-2003-dataset-from-the-datasets-library-and-process-it)

[Make the NER label lookup table](https://keras.io/examples/nlp/ner_transformers/#make-the-ner-label-lookup-table)

[Compile and fit the model](https://keras.io/examples/nlp/ner_transformers/#compile-and-fit-the-model)

[Metrics calculation](https://keras.io/examples/nlp/ner_transformers/#metrics-calculation)

[Conclusions](https://keras.io/examples/nlp/ner_transformers/#conclusions)

[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/nlp/ner_transformers/#relevant-chapters-from-deep-learning-with-python)