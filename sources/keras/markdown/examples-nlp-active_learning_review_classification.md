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
 / Review Classification using Active Learning

Review Classification using Active Learning
===========================================

**Author:** [Darshan Deshpande](https://twitter.com/getdarshan)
  
**Date created:** 2021/10/29  
**Last modified:** 2024/05/08  
**Description:** Demonstrating the advantages of active learning through review classification.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/active_learning_review_classification.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/active_learning_review_classification.py)

* * *

Introduction
------------

With the growth of data-centric Machine Learning, Active Learning has grown in popularity amongst businesses and researchers. Active Learning seeks to progressively train ML models so that the resultant model requires lesser amount of training data to achieve competitive scores.

The structure of an Active Learning pipeline involves a classifier and an oracle. The oracle is an annotator that cleans, selects, labels the data, and feeds it to the model when required. The oracle is a trained individual or a group of individuals that ensure consistency in labeling of new data.

The process starts with annotating a small subset of the full dataset and training an initial model. The best model checkpoint is saved and then tested on a balanced test set. The test set must be carefully sampled because the full training process will be dependent on it. Once we have the initial evaluation scores, the oracle is tasked with labeling more samples; the number of data points to be sampled is usually determined by the business requirements. After that, the newly sampled data is added to the training set, and the training procedure repeats. This cycle continues until either an acceptable score is reached or some other business metric is met.

This tutorial provides a basic demonstration of how Active Learning works by demonstrating a ratio-based (least confidence) sampling strategy that results in lower overall false positive and negative rates when compared to a model trained on the entire dataset. This sampling falls under the domain of _uncertainty sampling_, in which new datasets are sampled based on the uncertainty that the model outputs for the corresponding label. In our example, we compare our model's false positive and false negative rates and annotate the new data based on their ratio.

Some other sampling techniques include:

1.  [Committee sampling](https://www.researchgate.net/publication/51909346_Committee-Based_Sample_Selection_for_Probabilistic_Classifiers)
    : Using multiple models to vote for the best data points to be sampled
2.  [Entropy reduction](https://www.researchgate.net/publication/51909346_Committee-Based_Sample_Selection_for_Probabilistic_Classifiers)
    : Sampling according to an entropy threshold, selecting more of the samples that produce the highest entropy score.
3.  [Minimum margin based sampling](https://arxiv.org/abs/1906.00025v1)
    : Selects data points closest to the decision boundary

* * *

Importing required libraries
----------------------------

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  # @param ["tensorflow", "jax", "torch"] import keras from keras import ops from keras import layers import tensorflow_datasets as tfds import tensorflow as tf import matplotlib.pyplot as plt import re import string  tfds.disable_progress_bar()`

* * *

Loading and preprocessing the data
----------------------------------

We will be using the IMDB reviews dataset for our experiments. This dataset has 50,000 reviews in total, including training and testing splits. We will merge these splits and sample our own, balanced training, validation and testing sets.

Copied!

`dataset = tfds.load(     "imdb_reviews",     split="train + test",     as_supervised=True,     batch_size=-1,     shuffle_files=False, ) reviews, labels = tfds.as_numpy(dataset)  print("Total examples:", reviews.shape[0])`

`Total examples: 50000`

Active learning starts with labeling a subset of data. For the ratio sampling technique that we will be using, we will need well-balanced training, validation and testing splits.

Copied!

`val_split = 2500 test_split = 2500 train_split = 7500  # Separating the negative and positive samples for manual stratification x_positives, y_positives = reviews[labels == 1], labels[labels == 1] x_negatives, y_negatives = reviews[labels == 0], labels[labels == 0]  # Creating training, validation and testing splits x_val, y_val = (     tf.concat((x_positives[:val_split], x_negatives[:val_split]), 0),     tf.concat((y_positives[:val_split], y_negatives[:val_split]), 0), ) x_test, y_test = (     tf.concat(         (             x_positives[val_split : val_split + test_split],             x_negatives[val_split : val_split + test_split],         ),         0,     ),     tf.concat(         (             y_positives[val_split : val_split + test_split],             y_negatives[val_split : val_split + test_split],         ),         0,     ), ) x_train, y_train = (     tf.concat(         (             x_positives[val_split + test_split : val_split + test_split + train_split],             x_negatives[val_split + test_split : val_split + test_split + train_split],         ),         0,     ),     tf.concat(         (             y_positives[val_split + test_split : val_split + test_split + train_split],             y_negatives[val_split + test_split : val_split + test_split + train_split],         ),         0,     ), )  # Remaining pool of samples are stored separately. These are only labeled as and when required x_pool_positives, y_pool_positives = (     x_positives[val_split + test_split + train_split :],     y_positives[val_split + test_split + train_split :], ) x_pool_negatives, y_pool_negatives = (     x_negatives[val_split + test_split + train_split :],     y_negatives[val_split + test_split + train_split :], )  # Creating TF Datasets for faster prefetching and parallelization train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)) val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val)) test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))  pool_negatives = tf.data.Dataset.from_tensor_slices(     (x_pool_negatives, y_pool_negatives) ) pool_positives = tf.data.Dataset.from_tensor_slices(     (x_pool_positives, y_pool_positives) )  print(f"Initial training set size: {len(train_dataset)}") print(f"Validation set size: {len(val_dataset)}") print(f"Testing set size: {len(test_dataset)}") print(f"Unlabeled negative pool: {len(pool_negatives)}") print(f"Unlabeled positive pool: {len(pool_positives)}")`

`Initial training set size: 15000 Validation set size: 5000 Testing set size: 5000 Unlabeled negative pool: 12500 Unlabeled positive pool: 12500`

### Fitting the `TextVectorization` layer

Since we are working with text data, we will need to encode the text strings as vectors which would then be passed through an `Embedding` layer. To make this tokenization process faster, we use the `map()` function with its parallelization functionality.

Copied!

`vectorizer = layers.TextVectorization(     3000, standardize="lower_and_strip_punctuation", output_sequence_length=150 ) # Adapting the dataset vectorizer.adapt(     train_dataset.map(lambda x, y: x, num_parallel_calls=tf.data.AUTOTUNE).batch(256) )  def vectorize_text(text, label):     text = vectorizer(text)     return text, label  train_dataset = train_dataset.map(     vectorize_text, num_parallel_calls=tf.data.AUTOTUNE ).prefetch(tf.data.AUTOTUNE) pool_negatives = pool_negatives.map(vectorize_text, num_parallel_calls=tf.data.AUTOTUNE) pool_positives = pool_positives.map(vectorize_text, num_parallel_calls=tf.data.AUTOTUNE)  val_dataset = val_dataset.batch(256).map(     vectorize_text, num_parallel_calls=tf.data.AUTOTUNE ) test_dataset = test_dataset.batch(256).map(     vectorize_text, num_parallel_calls=tf.data.AUTOTUNE )`

* * *

Creating Helper Functions
-------------------------

Copied!

`# Helper function for merging new history objects with older ones def append_history(losses, val_losses, accuracy, val_accuracy, history):     losses = losses + history.history["loss"]     val_losses = val_losses + history.history["val_loss"]     accuracy = accuracy + history.history["binary_accuracy"]     val_accuracy = val_accuracy + history.history["val_binary_accuracy"]     return losses, val_losses, accuracy, val_accuracy  # Plotter function def plot_history(losses, val_losses, accuracies, val_accuracies):     plt.plot(losses)     plt.plot(val_losses)     plt.legend(["train_loss", "val_loss"])     plt.xlabel("Epochs")     plt.ylabel("Loss")     plt.show()      plt.plot(accuracies)     plt.plot(val_accuracies)     plt.legend(["train_accuracy", "val_accuracy"])     plt.xlabel("Epochs")     plt.ylabel("Accuracy")     plt.show()`

* * *

Creating the Model
------------------

We create a small bidirectional LSTM model. When using Active Learning, you should make sure that the model architecture is capable of overfitting to the initial data. Overfitting gives a strong hint that the model will have enough capacity for future, unseen data.

Copied!

`def create_model():     model = keras.models.Sequential(         [             layers.Input(shape=(150,)),             layers.Embedding(input_dim=3000, output_dim=128),             layers.Bidirectional(layers.LSTM(32, return_sequences=True)),             layers.GlobalMaxPool1D(),             layers.Dense(20, activation="relu"),             layers.Dropout(0.5),             layers.Dense(1, activation="sigmoid"),         ]     )     model.summary()     return model`

* * *

Training on the entire dataset
------------------------------

To show the effectiveness of Active Learning, we will first train the model on the entire dataset containing 40,000 labeled samples. This model will be used for comparison later.

Copied!

`def train_full_model(full_train_dataset, val_dataset, test_dataset):     model = create_model()     model.compile(         loss="binary_crossentropy",         optimizer="rmsprop",         metrics=[             keras.metrics.BinaryAccuracy(),             keras.metrics.FalseNegatives(),             keras.metrics.FalsePositives(),         ],     )      # We will save the best model at every epoch and load the best one for evaluation on the test set     history = model.fit(         full_train_dataset.batch(256),         epochs=20,         validation_data=val_dataset,         callbacks=[             keras.callbacks.EarlyStopping(patience=4, verbose=1),             keras.callbacks.ModelCheckpoint(                 "FullModelCheckpoint.keras", verbose=1, save_best_only=True             ),         ],     )      # Plot history     plot_history(         history.history["loss"],         history.history["val_loss"],         history.history["binary_accuracy"],         history.history["val_binary_accuracy"],     )      # Loading the best checkpoint     model = keras.models.load_model("FullModelCheckpoint.keras")      print("-" * 100)     print(         "Test set evaluation: ",         model.evaluate(test_dataset, verbose=0, return_dict=True),     )     print("-" * 100)     return model  # Sampling the full train dataset to train on full_train_dataset = (     train_dataset.concatenate(pool_positives)     .concatenate(pool_negatives)     .cache()     .shuffle(20000) )  # Training the full model full_dataset_model = train_full_model(full_train_dataset, val_dataset, test_dataset)`

Model: "sequential"

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ embedding (Embedding)           │ (None, 150, 128)       │       384,000 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ bidirectional (Bidirectional)   │ (None, 150, 64)        │        41,216 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ global\_max\_pooling1d            │ (None, 64)             │             0 │
│ (GlobalMaxPooling1D)            │                        │               │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense (Dense)                   │ (None, 20)             │         1,300 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dropout (Dropout)               │ (None, 20)             │             0 │
├─────────────────────────────────┼────────────────────────┼───────────────┤
│ dense\_1 (Dense)                 │ (None, 1)              │            21 │
└─────────────────────────────────┴────────────────────────┴───────────────┘

 Total params: 426,537 (1.63 MB)

 Trainable params: 426,537 (1.63 MB)

 Non-trainable params: 0 (0.00 B)

`Epoch 1/20`

156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 73ms/step - binary\_accuracy: 0.6412 - false\_negatives: 2084.3333 - false\_positives: 5252.1924 - loss: 0.6507\
\
`Epoch 1: val_loss improved from inf to 0.57198, saving model to FullModelCheckpoint.keras  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 15s 79ms/step - binary\_accuracy: 0.6411 - false\_negatives: 2135.1772 - false\_positives: 5292.4053 - loss: 0.6506 - val\_binary\_accuracy: 0.7356 - val\_false\_negatives: 898.0000 - val\_false\_positives: 424.0000 - val\_loss: 0.5720\
\
`Epoch 2/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.7448 - false\_negatives: 1756.2756 - false\_positives: 3249.1411 - loss: 0.5416\
\
`Epoch 2: val_loss improved from 0.57198 to 0.41756, saving model to FullModelCheckpoint.keras  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.7450 - false\_negatives: 1783.8925 - false\_positives: 3279.8101 - loss: 0.5412 - val\_binary\_accuracy: 0.8156 - val\_false\_negatives: 531.0000 - val\_false\_positives: 391.0000 - val\_loss: 0.4176\
\
`Epoch 3/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8162 - false\_negatives: 1539.7693 - false\_positives: 2197.1475 - loss: 0.4254\
\
`Epoch 3: val_loss improved from 0.41756 to 0.38233, saving model to FullModelCheckpoint.keras  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.8161 - false\_negatives: 1562.6962 - false\_positives: 2221.5886 - loss: 0.4254 - val\_binary\_accuracy: 0.8340 - val\_false\_negatives: 496.0000 - val\_false\_positives: 334.0000 - val\_loss: 0.3823\
\
`Epoch 4/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8413 - false\_negatives: 1400.6538 - false\_positives: 1818.7372 - loss: 0.3837\
\
`Epoch 4: val_loss improved from 0.38233 to 0.36235, saving model to FullModelCheckpoint.keras  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.8412 - false\_negatives: 1421.5063 - false\_positives: 1839.3102 - loss: 0.3838 - val\_binary\_accuracy: 0.8396 - val\_false\_negatives: 548.0000 - val\_false\_positives: 254.0000 - val\_loss: 0.3623\
\
`Epoch 5/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8611 - false\_negatives: 1264.5256 - false\_positives: 1573.5962 - loss: 0.3468\
\
`Epoch 5: val_loss did not improve from 0.36235  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 75ms/step - binary\_accuracy: 0.8611 - false\_negatives: 1283.0632 - false\_positives: 1592.3228 - loss: 0.3468 - val\_binary\_accuracy: 0.8222 - val\_false\_negatives: 734.0000 - val\_false\_positives: 155.0000 - val\_loss: 0.4081\
\
`Epoch 6/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8706 - false\_negatives: 1186.9166 - false\_positives: 1427.9487 - loss: 0.3301\
\
`Epoch 6: val_loss improved from 0.36235 to 0.35041, saving model to FullModelCheckpoint.keras  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.8705 - false\_negatives: 1204.8038 - false\_positives: 1444.9368 - loss: 0.3302 - val\_binary\_accuracy: 0.8412 - val\_false\_negatives: 569.0000 - val\_false\_positives: 225.0000 - val\_loss: 0.3504\
\
`Epoch 7/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8768 - false\_negatives: 1162.4423 - false\_positives: 1342.4807 - loss: 0.3084\
\
`Epoch 7: val_loss improved from 0.35041 to 0.32680, saving model to FullModelCheckpoint.keras  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.8768 - false\_negatives: 1179.5253 - false\_positives: 1358.4114 - loss: 0.3085 - val\_binary\_accuracy: 0.8590 - val\_false\_negatives: 364.0000 - val\_false\_positives: 341.0000 - val\_loss: 0.3268\
\
`Epoch 8/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 73ms/step - binary\_accuracy: 0.8865 - false\_negatives: 1079.3206 - false\_positives: 1250.2693 - loss: 0.2924\
\
`Epoch 8: val_loss did not improve from 0.32680  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.8864 - false\_negatives: 1094.9873 - false\_positives: 1265.0632 - loss: 0.2926 - val\_binary\_accuracy: 0.8460 - val\_false\_negatives: 548.0000 - val\_false\_positives: 222.0000 - val\_loss: 0.3432\
\
`Epoch 9/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 73ms/step - binary\_accuracy: 0.8912 - false\_negatives: 1019.1987 - false\_positives: 1189.4551 - loss: 0.2807\
\
`Epoch 9: val_loss did not improve from 0.32680  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 77ms/step - binary\_accuracy: 0.8912 - false\_negatives: 1033.9684 - false\_positives: 1203.5632 - loss: 0.2808 - val\_binary\_accuracy: 0.8588 - val\_false\_negatives: 330.0000 - val\_false\_positives: 376.0000 - val\_loss: 0.3302\
\
`Epoch 10/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8997 - false\_negatives: 968.6346 - false\_positives: 1109.9103 - loss: 0.2669\
\
`Epoch 10: val_loss did not improve from 0.32680  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.8996 - false\_negatives: 983.1202 - false\_positives: 1123.3418 - loss: 0.2671 - val\_binary\_accuracy: 0.8558 - val\_false\_negatives: 445.0000 - val\_false\_positives: 276.0000 - val\_loss: 0.3413\
\
`Epoch 11/20`\
\
156/157 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.9055 - false\_negatives: 937.0320 - false\_positives: 1000.8589 - loss: 0.2520\
\
`Epoch 11: val_loss did not improve from 0.32680  `\
\
157/157 ━━━━━━━━━━━━━━━━━━━━ 12s 76ms/step - binary\_accuracy: 0.9055 - false\_negatives: 950.3608 - false\_positives: 1013.6456 - loss: 0.2521 - val\_binary\_accuracy: 0.8602 - val\_false\_negatives: 402.0000 - val\_false\_positives: 297.0000 - val\_loss: 0.3281\
\
`Epoch 11: early stopping`\
\
![png](https://keras.io/img/examples/nlp/active_learning_review_classification/active_learning_review_classification_15_1755.png)\
\
![png](https://keras.io/img/examples/nlp/active_learning_review_classification/active_learning_review_classification_15_1756.png)\
\
`----------------------------------------------------------------------------------------------------  Test set evaluation:  {'binary_accuracy': 0.8507999777793884, 'false_negatives': 397.0, 'false_positives': 349.0, 'loss': 0.3372706174850464} ----------------------------------------------------------------------------------------------------`\
\
* * *\
\
Training via Active Learning\
----------------------------\
\
The general process we follow when performing Active Learning is demonstrated below:\
\
![Active Learning](https://i.imgur.com/dmNKusp.png)\
\
The pipeline can be summarized in five parts:\
\
1.  Sample and annotate a small, balanced training dataset\
2.  Train the model on this small subset\
3.  Evaluate the model on a balanced testing set\
4.  If the model satisfies the business criteria, deploy it in a real time setting\
5.  If it doesn't pass the criteria, sample a few more samples according to the ratio of false positives and negatives, add them to the training set and repeat from step 2 till the model passes the tests or till all available data is exhausted.\
\
For the code below, we will perform sampling using the following formula:  \
\
![Ratio Sampling](https://i.imgur.com/LyZEiZL.png)\
\
Active Learning techniques use callbacks extensively for progress tracking. We will be using model checkpointing and early stopping for this example. The `patience` parameter for Early Stopping can help minimize overfitting and the time required. We have set it `patience=4` for now but since the model is robust, we can increase the patience level if desired.\
\
Note: We are not loading the checkpoint after the first training iteration. In my experience working on Active Learning techniques, this helps the model probe the newly formed loss landscape. Even if the model fails to improve in the second iteration, we will still gain insight about the possible future false positive and negative rates. This will help us sample a better set in the next iteration where the model will have a greater chance to improve.\
\
Copied!\
\
`def train_active_learning_models(     train_dataset,     pool_negatives,     pool_positives,     val_dataset,     test_dataset,     num_iterations=3,     sampling_size=5000, ):      # Creating lists for storing metrics     losses, val_losses, accuracies, val_accuracies = [], [], [], []      model = create_model()     # We will monitor the false positives and false negatives predicted by our model     # These will decide the subsequent sampling ratio for every Active Learning loop     model.compile(         loss="binary_crossentropy",         optimizer="rmsprop",         metrics=[             keras.metrics.BinaryAccuracy(),             keras.metrics.FalseNegatives(),             keras.metrics.FalsePositives(),         ],     )      # Defining checkpoints.     # The checkpoint callback is reused throughout the training since it only saves the best overall model.     checkpoint = keras.callbacks.ModelCheckpoint(         "AL_Model.keras", save_best_only=True, verbose=1     )     # Here, patience is set to 4. This can be set higher if desired.     early_stopping = keras.callbacks.EarlyStopping(patience=4, verbose=1)      print(f"Starting to train with {len(train_dataset)} samples")     # Initial fit with a small subset of the training set     history = model.fit(         train_dataset.cache().shuffle(20000).batch(256),         epochs=20,         validation_data=val_dataset,         callbacks=[checkpoint, early_stopping],     )      # Appending history     losses, val_losses, accuracies, val_accuracies = append_history(         losses, val_losses, accuracies, val_accuracies, history     )      for iteration in range(num_iterations):         # Getting predictions from previously trained model         predictions = model.predict(test_dataset)          # Generating labels from the output probabilities         rounded = ops.where(ops.greater(predictions, 0.5), 1, 0)          # Evaluating the number of zeros and ones incorrrectly classified         _, _, false_negatives, false_positives = model.evaluate(test_dataset, verbose=0)          print("-" * 100)         print(             f"Number of zeros incorrectly classified: {false_negatives}, Number of ones incorrectly classified: {false_positives}"         )          # This technique of Active Learning demonstrates ratio based sampling where         # Number of ones/zeros to sample = Number of ones/zeros incorrectly classified / Total incorrectly classified         if false_negatives != 0 and false_positives != 0:             total = false_negatives + false_positives             sample_ratio_ones, sample_ratio_zeros = (                 false_positives / total,                 false_negatives / total,             )         # In the case where all samples are correctly predicted, we can sample both classes equally         else:             sample_ratio_ones, sample_ratio_zeros = 0.5, 0.5          print(             f"Sample ratio for positives: {sample_ratio_ones}, Sample ratio for negatives:{sample_ratio_zeros}"         )          # Sample the required number of ones and zeros         sampled_dataset = pool_negatives.take(             int(sample_ratio_zeros * sampling_size)         ).concatenate(pool_positives.take(int(sample_ratio_ones * sampling_size)))          # Skip the sampled data points to avoid repetition of sample         pool_negatives = pool_negatives.skip(int(sample_ratio_zeros * sampling_size))         pool_positives = pool_positives.skip(int(sample_ratio_ones * sampling_size))          # Concatenating the train_dataset with the sampled_dataset         train_dataset = train_dataset.concatenate(sampled_dataset).prefetch(             tf.data.AUTOTUNE         )          print(f"Starting training with {len(train_dataset)} samples")         print("-" * 100)          # We recompile the model to reset the optimizer states and retrain the model         model.compile(             loss="binary_crossentropy",             optimizer="rmsprop",             metrics=[                 keras.metrics.BinaryAccuracy(),                 keras.metrics.FalseNegatives(),                 keras.metrics.FalsePositives(),             ],         )         history = model.fit(             train_dataset.cache().shuffle(20000).batch(256),             validation_data=val_dataset,             epochs=20,             callbacks=[                 checkpoint,                 keras.callbacks.EarlyStopping(patience=4, verbose=1),             ],         )          # Appending the history         losses, val_losses, accuracies, val_accuracies = append_history(             losses, val_losses, accuracies, val_accuracies, history         )          # Loading the best model from this training loop         model = keras.models.load_model("AL_Model.keras")      # Plotting the overall history and evaluating the final model     plot_history(losses, val_losses, accuracies, val_accuracies)     print("-" * 100)     print(         "Test set evaluation: ",         model.evaluate(test_dataset, verbose=0, return_dict=True),     )     print("-" * 100)      return model  active_learning_model = train_active_learning_models(     train_dataset, pool_negatives, pool_positives, val_dataset, test_dataset )`\
\
Model: "sequential\_1"\
\
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓\
┃ Layer (type)                    ┃ Output Shape           ┃       Param # ┃\
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩\
│ embedding\_1 (Embedding)         │ (None, 150, 128)       │       384,000 │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ bidirectional\_1 (Bidirectional) │ (None, 150, 64)        │        41,216 │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ global\_max\_pooling1d\_1          │ (None, 64)             │             0 │\
│ (GlobalMaxPooling1D)            │                        │               │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ dense\_2 (Dense)                 │ (None, 20)             │         1,300 │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ dropout\_1 (Dropout)             │ (None, 20)             │             0 │\
├─────────────────────────────────┼────────────────────────┼───────────────┤\
│ dense\_3 (Dense)                 │ (None, 1)              │            21 │\
└─────────────────────────────────┴────────────────────────┴───────────────┘\
\
 Total params: 426,537 (1.63 MB)\
\
 Trainable params: 426,537 (1.63 MB)\
\
 Non-trainable params: 0 (0.00 B)\
\
`Starting to train with 15000 samples Epoch 1/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.5197 - false\_negatives\_1: 1686.7457 - false\_positives\_1: 1938.3051 - loss: 0.6918\
\
`Epoch 1: val_loss improved from inf to 0.67428, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 8s 89ms/step - binary\_accuracy: 0.5202 - false\_negatives\_1: 1716.9833 - false\_positives\_1: 1961.4667 - loss: 0.6917 - val\_binary\_accuracy: 0.6464 - val\_false\_negatives\_1: 279.0000 - val\_false\_positives\_1: 1489.0000 - val\_loss: 0.6743\
\
`Epoch 2/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.6505 - false\_negatives\_1: 1216.0170 - false\_positives\_1: 1434.2373 - loss: 0.6561\
\
`Epoch 2: val_loss improved from 0.67428 to 0.59133, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.6507 - false\_negatives\_1: 1234.9833 - false\_positives\_1: 1455.7667 - loss: 0.6558 - val\_binary\_accuracy: 0.7032 - val\_false\_negatives\_1: 235.0000 - val\_false\_positives\_1: 1249.0000 - val\_loss: 0.5913\
\
`Epoch 3/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.7103 - false\_negatives\_1: 939.5255 - false\_positives\_1: 1235.8983 - loss: 0.5829\
\
`Epoch 3: val_loss improved from 0.59133 to 0.51602, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.7106 - false\_negatives\_1: 953.0500 - false\_positives\_1: 1255.3167 - loss: 0.5827 - val\_binary\_accuracy: 0.7686 - val\_false\_negatives\_1: 812.0000 - val\_false\_positives\_1: 345.0000 - val\_loss: 0.5160\
\
`Epoch 4/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.7545 - false\_negatives\_1: 787.4237 - false\_positives\_1: 1070.0339 - loss: 0.5214\
\
`Epoch 4: val_loss improved from 0.51602 to 0.43948, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.7547 - false\_negatives\_1: 799.2667 - false\_positives\_1: 1085.8833 - loss: 0.5212 - val\_binary\_accuracy: 0.8028 - val\_false\_negatives\_1: 342.0000 - val\_false\_positives\_1: 644.0000 - val\_loss: 0.4395\
\
`Epoch 5/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.7919 - false\_negatives\_1: 676.7458 - false\_positives\_1: 907.4915 - loss: 0.4657\
\
`Epoch 5: val_loss improved from 0.43948 to 0.41679, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.7920 - false\_negatives\_1: 687.3834 - false\_positives\_1: 921.1667 - loss: 0.4655 - val\_binary\_accuracy: 0.8158 - val\_false\_negatives\_1: 598.0000 - val\_false\_positives\_1: 323.0000 - val\_loss: 0.4168\
\
`Epoch 6/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.7994 - false\_negatives\_1: 661.3560 - false\_positives\_1: 828.0847 - loss: 0.4498\
\
`Epoch 6: val_loss improved from 0.41679 to 0.39680, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.7997 - false\_negatives\_1: 671.3666 - false\_positives\_1: 840.2500 - loss: 0.4495 - val\_binary\_accuracy: 0.8260 - val\_false\_negatives\_1: 382.0000 - val\_false\_positives\_1: 488.0000 - val\_loss: 0.3968\
\
`Epoch 7/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8311 - false\_negatives\_1: 589.1187 - false\_positives\_1: 707.0170 - loss: 0.4017\
\
`Epoch 7: val_loss did not improve from 0.39680  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8312 - false\_negatives\_1: 598.3500 - false\_positives\_1: 717.8167 - loss: 0.4016 - val\_binary\_accuracy: 0.7706 - val\_false\_negatives\_1: 1004.0000 - val\_false\_positives\_1: 143.0000 - val\_loss: 0.4884\
\
`Epoch 8/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8365 - false\_negatives\_1: 566.7288 - false\_positives\_1: 649.9322 - loss: 0.3896\
\
`Epoch 8: val_loss did not improve from 0.39680  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8366 - false\_negatives\_1: 575.2833 - false\_positives\_1: 660.2167 - loss: 0.3895 - val\_binary\_accuracy: 0.8216 - val\_false\_negatives\_1: 623.0000 - val\_false\_positives\_1: 269.0000 - val\_loss: 0.4043\
\
`Epoch 9/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8531 - false\_negatives\_1: 519.0170 - false\_positives\_1: 591.6440 - loss: 0.3631\
\
`Epoch 9: val_loss improved from 0.39680 to 0.37727, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8531 - false\_negatives\_1: 527.2667 - false\_positives\_1: 601.2500 - loss: 0.3631 - val\_binary\_accuracy: 0.8348 - val\_false\_negatives\_1: 296.0000 - val\_false\_positives\_1: 530.0000 - val\_loss: 0.3773\
\
`Epoch 10/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8686 - false\_negatives\_1: 475.7966 - false\_positives\_1: 569.0508 - loss: 0.3387\
\
`Epoch 10: val_loss improved from 0.37727 to 0.37354, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8685 - false\_negatives\_1: 483.5000 - false\_positives\_1: 577.9667 - loss: 0.3387 - val\_binary\_accuracy: 0.8400 - val\_false\_negatives\_1: 327.0000 - val\_false\_positives\_1: 473.0000 - val\_loss: 0.3735\
\
`Epoch 11/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8716 - false\_negatives\_1: 452.1356 - false\_positives\_1: 522.1187 - loss: 0.3303\
\
`Epoch 11: val_loss improved from 0.37354 to 0.37074, saving model to AL_Model.keras  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8716 - false\_negatives\_1: 459.3833 - false\_positives\_1: 530.6667 - loss: 0.3303 - val\_binary\_accuracy: 0.8390 - val\_false\_negatives\_1: 362.0000 - val\_false\_positives\_1: 443.0000 - val\_loss: 0.3707\
\
`Epoch 12/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8833 - false\_negatives\_1: 433.0678 - false\_positives\_1: 481.1864 - loss: 0.3065\
\
`Epoch 12: val_loss did not improve from 0.37074  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8833 - false\_negatives\_1: 439.8333 - false\_positives\_1: 488.9667 - loss: 0.3066 - val\_binary\_accuracy: 0.8236 - val\_false\_negatives\_1: 208.0000 - val\_false\_positives\_1: 674.0000 - val\_loss: 0.4046\
\
`Epoch 13/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8876 - false\_negatives\_1: 384.8305 - false\_positives\_1: 476.5254 - loss: 0.2978\
\
`Epoch 13: val_loss did not improve from 0.37074  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 82ms/step - binary\_accuracy: 0.8876 - false\_negatives\_1: 391.2667 - false\_positives\_1: 484.2500 - loss: 0.2978 - val\_binary\_accuracy: 0.8380 - val\_false\_negatives\_1: 364.0000 - val\_false\_positives\_1: 446.0000 - val\_loss: 0.3783\
\
`Epoch 14/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8976 - false\_negatives\_1: 378.0169 - false\_positives\_1: 433.9831 - loss: 0.2754\
\
`Epoch 14: val_loss did not improve from 0.37074  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.8975 - false\_negatives\_1: 384.2333 - false\_positives\_1: 441.3833 - loss: 0.2757 - val\_binary\_accuracy: 0.8310 - val\_false\_negatives\_1: 525.0000 - val\_false\_positives\_1: 320.0000 - val\_loss: 0.3957\
\
`Epoch 15/20`\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.9013 - false\_negatives\_1: 354.9322 - false\_positives\_1: 403.1695 - loss: 0.2709\
\
`Epoch 15: val_loss did not improve from 0.37074  `\
\
59/59 ━━━━━━━━━━━━━━━━━━━━ 5s 83ms/step - binary\_accuracy: 0.9013 - false\_negatives\_1: 360.4000 - false\_positives\_1: 409.5833 - loss: 0.2709 - val\_binary\_accuracy: 0.8298 - val\_false\_negatives\_1: 302.0000 - val\_false\_positives\_1: 549.0000 - val\_loss: 0.4015\
\
`Epoch 15: early stopping`\
\
20/20 ━━━━━━━━━━━━━━━━━━━━ 1s 39ms/step\
\
`---------------------------------------------------------------------------------------------------- Number of zeros incorrectly classified: 290.0, Number of ones incorrectly classified: 538.0 Sample ratio for positives: 0.6497584541062802, Sample ratio for negatives:0.3502415458937198 Starting training with 19999 samples ---------------------------------------------------------------------------------------------------- Epoch 1/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8735 - false\_negatives\_2: 547.2436 - false\_positives\_2: 650.2436 - loss: 0.3527\
\
`Epoch 1: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 9s 84ms/step - binary\_accuracy: 0.8738 - false\_negatives\_2: 559.2125 - false\_positives\_2: 665.3375 - loss: 0.3518 - val\_binary\_accuracy: 0.7932 - val\_false\_negatives\_2: 119.0000 - val\_false\_positives\_2: 915.0000 - val\_loss: 0.4949\
\
`Epoch 2/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.8961 - false\_negatives\_2: 470.2436 - false\_positives\_2: 576.1539 - loss: 0.2824\
\
`Epoch 2: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 6s 80ms/step - binary\_accuracy: 0.8962 - false\_negatives\_2: 481.4125 - false\_positives\_2: 589.6750 - loss: 0.2823 - val\_binary\_accuracy: 0.8014 - val\_false\_negatives\_2: 809.0000 - val\_false\_positives\_2: 184.0000 - val\_loss: 0.4580\
\
`Epoch 3/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.9059 - false\_negatives\_2: 442.2051 - false\_positives\_2: 500.5385 - loss: 0.2628\
\
`Epoch 3: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 6s 80ms/step - binary\_accuracy: 0.9059 - false\_negatives\_2: 452.6750 - false\_positives\_2: 513.5250 - loss: 0.2629 - val\_binary\_accuracy: 0.8294 - val\_false\_negatives\_2: 302.0000 - val\_false\_positives\_2: 551.0000 - val\_loss: 0.3868\
\
`Epoch 4/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.9188 - false\_negatives\_2: 394.5513 - false\_positives\_2: 462.4359 - loss: 0.2391\
\
`Epoch 4: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 6s 80ms/step - binary\_accuracy: 0.9187 - false\_negatives\_2: 405.0625 - false\_positives\_2: 474.1250 - loss: 0.2393 - val\_binary\_accuracy: 0.8268 - val\_false\_negatives\_2: 225.0000 - val\_false\_positives\_2: 641.0000 - val\_loss: 0.4197\
\
`Epoch 5/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.9255 - false\_negatives\_2: 349.8718 - false\_positives\_2: 413.0898 - loss: 0.2270\
\
`Epoch 5: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 6s 79ms/step - binary\_accuracy: 0.9254 - false\_negatives\_2: 358.6500 - false\_positives\_2: 423.5625 - loss: 0.2270 - val\_binary\_accuracy: 0.8228 - val\_false\_negatives\_2: 611.0000 - val\_false\_positives\_2: 275.0000 - val\_loss: 0.4233\
\
`Epoch 6/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 73ms/step - binary\_accuracy: 0.9265 - false\_negatives\_2: 349.8590 - false\_positives\_2: 389.9359 - loss: 0.2147\
\
`Epoch 6: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 6s 80ms/step - binary\_accuracy: 0.9265 - false\_negatives\_2: 358.8375 - false\_positives\_2: 399.9875 - loss: 0.2148 - val\_binary\_accuracy: 0.8272 - val\_false\_negatives\_2: 581.0000 - val\_false\_positives\_2: 283.0000 - val\_loss: 0.4415\
\
`Epoch 7/20`\
\
78/79 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 72ms/step - binary\_accuracy: 0.9409 - false\_negatives\_2: 286.7820 - false\_positives\_2: 322.7949 - loss: 0.1877\
\
`Epoch 7: val_loss did not improve from 0.37074  `\
\
79/79 ━━━━━━━━━━━━━━━━━━━━ 6s 79ms/step - binary\_accuracy: 0.9408 - false\_negatives\_2: 294.4375 - false\_positives\_2: 331.4000 - loss: 0.1880 - val\_binary\_accuracy: 0.8266 - val\_false\_negatives\_2: 528.0000 - val\_false\_positives\_2: 339.0000 - val\_loss: 0.4419\
\
`Epoch 7: early stopping`\
\
20/20 ━━━━━━━━━━━━━━━━━━━━ 1s 39ms/step\
\
`---------------------------------------------------------------------------------------------------- Number of zeros incorrectly classified: 376.0, Number of ones incorrectly classified: 442.0 Sample ratio for positives: 0.5403422982885085, Sample ratio for negatives:0.45965770171149145 Starting training with 24998 samples ---------------------------------------------------------------------------------------------------- Epoch 1/20`\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 0s 73ms/step - binary\_accuracy: 0.8509 - false\_negatives\_3: 809.9184 - false\_positives\_3: 1018.9286 - loss: 0.3732\
\
`Epoch 1: val_loss improved from 0.37074 to 0.36196, saving model to AL_Model.keras  `\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 11s 83ms/step - binary\_accuracy: 0.8509 - false\_negatives\_3: 817.5757 - false\_positives\_3: 1028.7980 - loss: 0.3731 - val\_binary\_accuracy: 0.8424 - val\_false\_negatives\_3: 368.0000 - val\_false\_positives\_3: 420.0000 - val\_loss: 0.3620\
\
`Epoch 2/20`\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8744 - false\_negatives\_3: 734.7449 - false\_positives\_3: 884.7755 - loss: 0.3185\
\
`Epoch 2: val_loss did not improve from 0.36196  `\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 8s 79ms/step - binary\_accuracy: 0.8744 - false\_negatives\_3: 741.9697 - false\_positives\_3: 893.7172 - loss: 0.3186 - val\_binary\_accuracy: 0.8316 - val\_false\_negatives\_3: 202.0000 - val\_false\_positives\_3: 640.0000 - val\_loss: 0.3792\
\
`Epoch 3/20`\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8830 - false\_negatives\_3: 684.1326 - false\_positives\_3: 807.8878 - loss: 0.3090\
\
`Epoch 3: val_loss did not improve from 0.36196  `\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 8s 79ms/step - binary\_accuracy: 0.8830 - false\_negatives\_3: 691.0707 - false\_positives\_3: 816.2222 - loss: 0.3090 - val\_binary\_accuracy: 0.8118 - val\_false\_negatives\_3: 738.0000 - val\_false\_positives\_3: 203.0000 - val\_loss: 0.4112\
\
`Epoch 4/20`\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8892 - false\_negatives\_3: 651.9898 - false\_positives\_3: 776.4388 - loss: 0.2928\
\
`Epoch 4: val_loss did not improve from 0.36196  `\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 8s 79ms/step - binary\_accuracy: 0.8892 - false\_negatives\_3: 658.4041 - false\_positives\_3: 784.3839 - loss: 0.2928 - val\_binary\_accuracy: 0.8344 - val\_false\_negatives\_3: 557.0000 - val\_false\_positives\_3: 271.0000 - val\_loss: 0.3734\
\
`Epoch 5/20`\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 0s 72ms/step - binary\_accuracy: 0.8975 - false\_negatives\_3: 612.0714 - false\_positives\_3: 688.9184 - loss: 0.2806\
\
`Epoch 5: val_loss did not improve from 0.36196  `\
\
98/98 ━━━━━━━━━━━━━━━━━━━━ 8s 79ms/step - binary\_accuracy: 0.8974 - false\_negatives\_3: 618.4343 - false\_positives\_3: 696.1313 - loss: 0.2807 - val\_binary\_accuracy: 0.8456 - val\_false\_negatives\_3: 446.0000 - val\_false\_positives\_3: 326.0000 - val\_loss: 0.3658\
\
`Epoch 5: early stopping`\
\
20/20 ━━━━━━━━━━━━━━━━━━━━ 1s 40ms/step\
\
`---------------------------------------------------------------------------------------------------- Number of zeros incorrectly classified: 407.0, Number of ones incorrectly classified: 410.0 Sample ratio for positives: 0.5018359853121175, Sample ratio for negatives:0.4981640146878825 Starting training with 29997 samples ---------------------------------------------------------------------------------------------------- Epoch 1/20`\
\
117/118 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 76ms/step - binary\_accuracy: 0.8621 - false\_negatives\_4: 916.2393 - false\_positives\_4: 1130.9744 - loss: 0.3527\
\
`Epoch 1: val_loss did not improve from 0.36196  `\
\
118/118 ━━━━━━━━━━━━━━━━━━━━ 13s 85ms/step - binary\_accuracy: 0.8621 - false\_negatives\_4: 931.0924 - false\_positives\_4: 1149.7479 - loss: 0.3525 - val\_binary\_accuracy: 0.8266 - val\_false\_negatives\_4: 627.0000 - val\_false\_positives\_4: 240.0000 - val\_loss: 0.3802\
\
`Epoch 2/20`\
\
117/118 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 76ms/step - binary\_accuracy: 0.8761 - false\_negatives\_4: 876.4872 - false\_positives\_4: 1005.5726 - loss: 0.3195\
\
`Epoch 2: val_loss improved from 0.36196 to 0.35707, saving model to AL_Model.keras  `\
\
118/118 ━━━━━━━━━━━━━━━━━━━━ 10s 82ms/step - binary\_accuracy: 0.8760 - false\_negatives\_4: 891.0504 - false\_positives\_4: 1022.9412 - loss: 0.3196 - val\_binary\_accuracy: 0.8404 - val\_false\_negatives\_4: 479.0000 - val\_false\_positives\_4: 319.0000 - val\_loss: 0.3571\
\
`Epoch 3/20`\
\
117/118 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 74ms/step - binary\_accuracy: 0.8874 - false\_negatives\_4: 801.1710 - false\_positives\_4: 941.4786 - loss: 0.2965\
\
`Epoch 3: val_loss did not improve from 0.35707  `\
\
118/118 ━━━━━━━━━━━━━━━━━━━━ 9s 79ms/step - binary\_accuracy: 0.8873 - false\_negatives\_4: 814.8319 - false\_positives\_4: 957.8571 - loss: 0.2966 - val\_binary\_accuracy: 0.8226 - val\_false\_negatives\_4: 677.0000 - val\_false\_positives\_4: 210.0000 - val\_loss: 0.3948\
\
`Epoch 4/20`\
\
117/118 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 76ms/step - binary\_accuracy: 0.8977 - false\_negatives\_4: 740.5385 - false\_positives\_4: 837.1710 - loss: 0.2768\
\
`Epoch 4: val_loss did not improve from 0.35707  `\
\
118/118 ━━━━━━━━━━━━━━━━━━━━ 10s 81ms/step - binary\_accuracy: 0.8976 - false\_negatives\_4: 753.5378 - false\_positives\_4: 852.2437 - loss: 0.2770 - val\_binary\_accuracy: 0.8406 - val\_false\_negatives\_4: 530.0000 - val\_false\_positives\_4: 267.0000 - val\_loss: 0.3630\
\
`Epoch 5/20`\
\
117/118 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 76ms/step - binary\_accuracy: 0.9020 - false\_negatives\_4: 722.5214 - false\_positives\_4: 808.2308 - loss: 0.2674\
\
`Epoch 5: val_loss did not improve from 0.35707  `\
\
118/118 ━━━━━━━━━━━━━━━━━━━━ 10s 82ms/step - binary\_accuracy: 0.9019 - false\_negatives\_4: 734.8655 - false\_positives\_4: 822.4117 - loss: 0.2676 - val\_binary\_accuracy: 0.8330 - val\_false\_negatives\_4: 592.0000 - val\_false\_positives\_4: 243.0000 - val\_loss: 0.3805\
\
`Epoch 6/20`\
\
117/118 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 76ms/step - binary\_accuracy: 0.9059 - false\_negatives\_4: 682.1453 - false\_positives\_4: 737.0513 - loss: 0.2525\
\
`Epoch 6: val_loss did not improve from 0.35707  `\
\
118/118 ━━━━━━━━━━━━━━━━━━━━ 10s 82ms/step - binary\_accuracy: 0.9059 - false\_negatives\_4: 693.6387 - false\_positives\_4: 749.9412 - loss: 0.2526 - val\_binary\_accuracy: 0.8454 - val\_false\_negatives\_4: 391.0000 - val\_false\_positives\_4: 382.0000 - val\_loss: 0.3620\
\
`Epoch 6: early stopping`\
\
![png](https://keras.io/img/examples/nlp/active_learning_review_classification/active_learning_review_classification_17_2767.png)\
\
![png](https://keras.io/img/examples/nlp/active_learning_review_classification/active_learning_review_classification_17_2768.png)\
\
`----------------------------------------------------------------------------------------------------  Test set evaluation:  {'binary_accuracy': 0.8424000144004822, 'false_negatives_4': 491.0, 'false_positives_4': 297.0, 'loss': 0.3661557137966156} ----------------------------------------------------------------------------------------------------`\
\
* * *\
\
Conclusion\
----------\
\
Active Learning is a growing area of research. This example demonstrates the cost-efficiency benefits of using Active Learning, as it eliminates the need to annotate large amounts of data, saving resources.\
\
The following are some noteworthy observations from this example:\
\
1.  We only require 30,000 samples to reach the same (if not better) scores as the model trained on the full dataset. This means that in a real life setting, we save the effort required for annotating 10,000 images!\
2.  The number of false negatives and false positives are well balanced at the end of the training as compared to the skewed ratio obtained from the full training. This makes the model slightly more useful in real life scenarios where both the labels hold equal importance.\
\
For further reading about the types of sampling ratios, training techniques or available open source libraries/implementations, you can refer to the resources below:\
\
1.  [Active Learning Literature Survey](http://burrsettles.com/pub/settles.activelearning.pdf)\
     (Burr Settles, 2010).\
2.  [modAL](https://github.com/modAL-python/modAL)\
    : A Modular Active Learning framework.\
3.  Google's unofficial [Active Learning playground](https://github.com/google/active-learning)\
    .\
\
* * *\
\
Relevant Chapters from Deep Learning with Python\
------------------------------------------------\
\
*   [Chapter 14: Text classification](https://deeplearningwithpython.io/chapters/chapter14_text-classification)\
    \
\
[Review Classification using Active Learning](https://keras.io/examples/nlp/active_learning_review_classification/#review-classification-using-active-learning)\
\
[Introduction](https://keras.io/examples/nlp/active_learning_review_classification/#introduction)\
\
[Importing required libraries](https://keras.io/examples/nlp/active_learning_review_classification/#importing-required-libraries)\
\
[Loading and preprocessing the data](https://keras.io/examples/nlp/active_learning_review_classification/#loading-and-preprocessing-the-data)\
\
[Fitting the `TextVectorization` layer](https://keras.io/examples/nlp/active_learning_review_classification/#fitting-the-textvectorization-layer)\
\
[Creating Helper Functions](https://keras.io/examples/nlp/active_learning_review_classification/#creating-helper-functions)\
\
[Creating the Model](https://keras.io/examples/nlp/active_learning_review_classification/#creating-the-model)\
\
[Training on the entire dataset](https://keras.io/examples/nlp/active_learning_review_classification/#training-on-the-entire-dataset)\
\
[Training via Active Learning](https://keras.io/examples/nlp/active_learning_review_classification/#training-via-active-learning)\
\
[Conclusion](https://keras.io/examples/nlp/active_learning_review_classification/#conclusion)\
\
[Relevant Chapters from Deep Learning with Python](https://keras.io/examples/nlp/active_learning_review_classification/#relevant-chapters-from-deep-learning-with-python)