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
 / Abstractive Text Summarization with BART

Abstractive Text Summarization with BART
========================================

**Author:** [Abheesht Sharma](https://github.com/abheesht17/)
  
**Date created:** 2023/07/08  
**Last modified:** 2024/03/20  
**Description:** Use KerasHub to fine-tune BART on the abstractive summarization task.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/nlp/ipynb/abstractive_summarization_with_bart.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/nlp/abstractive_summarization_with_bart.py)

* * *

Introduction
------------

In the era of information overload, it has become crucial to extract the crux of a long document or a conversation and express it in a few sentences. Owing to the fact that summarization has widespread applications in different domains, it has become a key, well-studied NLP task in recent years.

[Bidirectional Autoregressive Transformer (BART)](https://arxiv.org/abs/1910.13461)
 is a Transformer-based encoder-decoder model, often used for sequence-to-sequence tasks like summarization and neural machine translation. BART is pre-trained in a self-supervised fashion on a large text corpus. During pre-training, the text is corrupted and BART is trained to reconstruct the original text (hence called a "denoising autoencoder"). Some pre-training tasks include token masking, token deletion, sentence permutation (shuffle sentences and train BART to fix the order), etc.

In this example, we will demonstrate how to fine-tune BART on the abstractive summarization task (on conversations!) using KerasHub, and generate summaries using the fine-tuned model.

* * *

Setup
-----

Before we start implementing the pipeline, let's install and import all the libraries we need. We'll be using the KerasHub library. We will also need a couple of utility libraries.

Copied!

`!pip install git+https://github.com/keras-team/keras-hub.git py7zr -q`

  `Installing build dependencies ... [?25l[?25hdone   Getting requirements to build wheel ... [?25l[?25hdone   Preparing metadata (pyproject.toml) ... [?25l[?25hdone [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.4/66.4 kB [31m1.4 MB/s eta [36m0:00:00 [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB [31m34.8 MB/s eta [36m0:00:00 [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 412.3/412.3 kB [31m30.4 MB/s eta [36m0:00:00 [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 138.8/138.8 kB [31m15.1 MB/s eta [36m0:00:00 [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.8/49.8 kB [31m5.8 MB/s eta [36m0:00:00 [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB [31m61.4 MB/s eta [36m0:00:00 [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.1/93.1 kB [31m10.1 MB/s eta [36m0:00:00 [?25h  Building wheel for keras-hub (pyproject.toml) ... [?25l[?25hdone`\
\
This examples uses [Keras 3](https://keras.io/keras_3)\
 to work in any of `"tensorflow"`, `"jax"` or `"torch"`. Support for Keras 3 is baked into KerasHub, simply change the `"KERAS_BACKEND"` environment variable to select the backend of your choice. We select the JAX backend below.\
\
Copied!\
\
`import os  os.environ["KERAS_BACKEND"] = "jax"`\
\
Import all necessary libraries.\
\
Copied!\
\
`import py7zr import time  import keras_hub import keras import tensorflow as tf import tensorflow_datasets as tfds`\
\
`Using JAX backend.`\
\
Let's also define our hyperparameters.\
\
Copied!\
\
`BATCH_SIZE = 8 NUM_BATCHES = 600 EPOCHS = 1  # Can be set to a higher value for better results MAX_ENCODER_SEQUENCE_LENGTH = 512 MAX_DECODER_SEQUENCE_LENGTH = 128 MAX_GENERATION_LENGTH = 40`\
\
* * *\
\
Dataset\
-------\
\
Let's load the [SAMSum dataset](https://arxiv.org/abs/1911.12237)\
. This dataset contains around 15,000 pairs of conversations/dialogues and summaries.\
\
Copied!\
\
``# Download the dataset. filename = keras.utils.get_file(     "corpus.7z",     origin="https://huggingface.co/datasets/samsum/resolve/main/data/corpus.7z", )  # Extract the `.7z` file. with py7zr.SevenZipFile(filename, mode="r") as z:     z.extractall(path="/root/tensorflow_datasets/downloads/manual")  # Load data using TFDS. samsum_ds = tfds.load("samsum", split="train", as_supervised=True)``\
\
`Downloading data from https://huggingface.co/datasets/samsum/resolve/main/data/corpus.7z  2944100/2944100 ━━━━━━━━━━━━━━━━━━━━ 1s 0us/step Downloading and preparing dataset Unknown size (download: Unknown size, generated: 10.71 MiB, total: 10.71 MiB) to /root/tensorflow_datasets/samsum/1.0.0...  Generating splits...:   0%|          | 0/3 [00:00<?, ? splits/s]  Generating train examples...:   0%|          | 0/14732 [00:00<?, ? examples/s]  Shuffling /root/tensorflow_datasets/samsum/1.0.0.incompleteYA9MAV/samsum-train.tfrecord*...:   0%|          | …  Generating validation examples...:   0%|          | 0/818 [00:00<?, ? examples/s]  Shuffling /root/tensorflow_datasets/samsum/1.0.0.incompleteYA9MAV/samsum-validation.tfrecord*...:   0%|       …  Generating test examples...:   0%|          | 0/819 [00:00<?, ? examples/s]  Shuffling /root/tensorflow_datasets/samsum/1.0.0.incompleteYA9MAV/samsum-test.tfrecord*...:   0%|          | 0…  Dataset samsum downloaded and prepared to /root/tensorflow_datasets/samsum/1.0.0. Subsequent calls will reuse this data.`\
\
The dataset has two fields: `dialogue` and `summary`. Let's see a sample.\
\
Copied!\
\
`for dialogue, summary in samsum_ds:     print(dialogue.numpy())     print(summary.numpy())     break`\
\
`b"Carter: Hey Alexis, I just wanted to let you know that I had a really nice time with you tonight. \r\nAlexis: Thanks Carter. Yeah, I really enjoyed myself as well. \r\nCarter: If you are up for it, I would really like to see you again soon.\r\nAlexis: Thanks Carter, I'm flattered. But I have a really busy week coming up.\r\nCarter: Yeah, no worries. I totally understand. But if you ever want to go grab dinner again, just let me know. \r\nAlexis: Yeah of course. Thanks again for tonight. \r\nCarter: Sure. Have a great night. " b'Alexis and Carter met tonight. Carter would like to meet again, but Alexis is busy.'`\
\
We'll now batch the dataset and retain only a subset of the dataset for the purpose of this example. The dialogue is fed to the encoder, and the corresponding summary serves as input to the decoder. We will, therefore, change the format of the dataset to a dictionary having two keys: `"encoder_text"` and `"decoder_text"`.This is how [`keras_hub.models.BartSeq2SeqLMPreprocessor`](https://keras.io/keras_hub/api/models/bart/bart_seq_2_seq_lm_preprocessor#bartseq2seqlmpreprocessor-class)\
 expects the input format to be.\
\
Copied!\
\
`train_ds = (     samsum_ds.map(         lambda dialogue, summary: {"encoder_text": dialogue, "decoder_text": summary}     )     .batch(BATCH_SIZE)     .cache() ) train_ds = train_ds.take(NUM_BATCHES)`\
\
* * *\
\
Fine-tune BART\
--------------\
\
Let's load the model and preprocessor first. We use sequence lengths of 512 and 128 for the encoder and decoder, respectively, instead of 1024 (which is the default sequence length). This will allow us to run this example quickly on Colab.\
\
If you observe carefully, the preprocessor is attached to the model. What this means is that we don't have to worry about preprocessing the text inputs; everything will be done internally. The preprocessor tokenizes the encoder text and the decoder text, adds special tokens and pads them. To generate labels for auto-regressive training, the preprocessor shifts the decoder text one position to the right. This is done because at every timestep, the model is trained to predict the next token.\
\
Copied!\
\
`preprocessor = keras_hub.models.BartSeq2SeqLMPreprocessor.from_preset(     "bart_base_en",     encoder_sequence_length=MAX_ENCODER_SEQUENCE_LENGTH,     decoder_sequence_length=MAX_DECODER_SEQUENCE_LENGTH, ) bart_lm = keras_hub.models.BartSeq2SeqLM.from_preset(     "bart_base_en", preprocessor=preprocessor )  bart_lm.summary()`\
\
`Downloading data from https://storage.googleapis.com/keras-hub/models/bart_base_en/v1/vocab.json  898823/898823 ━━━━━━━━━━━━━━━━━━━━ 1s 1us/step Downloading data from https://storage.googleapis.com/keras-hub/models/bart_base_en/v1/merges.txt  456318/456318 ━━━━━━━━━━━━━━━━━━━━ 1s 1us/step Downloading data from https://storage.googleapis.com/keras-hub/models/bart_base_en/v1/model.h5  557969120/557969120 ━━━━━━━━━━━━━━━━━━━━ 29s 0us/step`\
\
Preprocessor: "bart\_seq2\_seq\_lm\_preprocessor"\
\
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\
┃ Tokenizer (type)                                   ┃                                             Vocab # ┃\
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩\
│ bart\_tokenizer (BartTokenizer)                     │                                              50,265 │\
└────────────────────────────────────────────────────┴─────────────────────────────────────────────────────┘\
\
Model: "bart\_seq2\_seq\_lm"\
\
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\
┃ Layer (type)                  ┃ Output Shape              ┃     Param # ┃ Connected to                   ┃\
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩\
│ decoder\_padding\_mask          │ (None, None)              │           0 │ -                              │\
│ (InputLayer)                  │                           │             │                                │\
├───────────────────────────────┼───────────────────────────┼─────────────┼────────────────────────────────┤\
│ decoder\_token\_ids             │ (None, None)              │           0 │ -                              │\
│ (InputLayer)                  │                           │             │                                │\
├───────────────────────────────┼───────────────────────────┼─────────────┼────────────────────────────────┤\
│ encoder\_padding\_mask          │ (None, None)              │           0 │ -                              │\
│ (InputLayer)                  │                           │             │                                │\
├───────────────────────────────┼───────────────────────────┼─────────────┼────────────────────────────────┤\
│ encoder\_token\_ids             │ (None, None)              │           0 │ -                              │\
│ (InputLayer)                  │                           │             │                                │\
├───────────────────────────────┼───────────────────────────┼─────────────┼────────────────────────────────┤\
│ bart\_backbone (BartBackbone)  │ \[(None, None, 768),       │ 139,417,344 │ decoder\_padding\_mask\[0\]\[0\],    │\
│                               │ (None, None, 768)\]        │             │ decoder\_token\_ids\[0\]\[0\],       │\
│                               │                           │             │ encoder\_padding\_mask\[0\]\[0\],    │\
│                               │                           │             │ encoder\_token\_ids\[0\]\[0\]        │\
├───────────────────────────────┼───────────────────────────┼─────────────┼────────────────────────────────┤\
│ reverse\_embedding             │ (None, 50265)             │  38,603,520 │ bart\_backbone\[0\]\[0\]            │\
│ (ReverseEmbedding)            │                           │             │                                │\
└───────────────────────────────┴───────────────────────────┴─────────────┴────────────────────────────────┘\
\
 Total params: 139,417,344 (4.15 GB)\
\
 Trainable params: 139,417,344 (4.15 GB)\
\
 Non-trainable params: 0 (0.00 B)\
\
Define the optimizer and loss. We use the Adam optimizer with a linearly decaying learning rate. Compile the model.\
\
Copied!\
\
`optimizer = keras.optimizers.AdamW(     learning_rate=5e-5,     weight_decay=0.01,     epsilon=1e-6,     global_clipnorm=1.0,  # Gradient clipping. ) # Exclude layernorm and bias terms from weight decay. optimizer.exclude_from_weight_decay(var_names=["bias"]) optimizer.exclude_from_weight_decay(var_names=["gamma"]) optimizer.exclude_from_weight_decay(var_names=["beta"])  loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)  bart_lm.compile(     optimizer=optimizer,     loss=loss,     weighted_metrics=["accuracy"], )`\
\
Let's train the model!\
\
Copied!\
\
`bart_lm.fit(train_ds, epochs=EPOCHS)`\
\
 `600/600 ━━━━━━━━━━━━━━━━━━━━ 398s 586ms/step - loss: 0.4330  <keras_core.src.callbacks.history.History at 0x7ae2faf3e110>`\
\
* * *\
\
Generate summaries and evaluate them!\
-------------------------------------\
\
Now that the model has been trained, let's get to the fun part - actually generating summaries! Let's pick the first 100 samples from the validation set and generate summaries for them. We will use the default decoding strategy, i.e., greedy search.\
\
Generation in KerasHub is highly optimized. It is backed by the power of XLA. Secondly, key/value tensors in the self-attention layer and cross-attention layer in the decoder are cached to avoid recomputation at every timestep.\
\
Copied!\
\
`def generate_text(model, input_text, max_length=200, print_time_taken=False):     start = time.time()     output = model.generate(input_text, max_length=max_length)     end = time.time()     print(f"Total Time Elapsed: {end - start:.2f}s")     return output  # Load the dataset. val_ds = tfds.load("samsum", split="validation", as_supervised=True) val_ds = val_ds.take(100)  dialogues = [] ground_truth_summaries = [] for dialogue, summary in val_ds:     dialogues.append(dialogue.numpy())     ground_truth_summaries.append(summary.numpy())  # Let's make a dummy call - the first call to XLA generally takes a bit longer. _ = generate_text(bart_lm, "sample text", max_length=MAX_GENERATION_LENGTH)  # Generate summaries. generated_summaries = generate_text(     bart_lm,     val_ds.map(lambda dialogue, _: dialogue).batch(8),     max_length=MAX_GENERATION_LENGTH,     print_time_taken=True, )`\
\
`Total Time Elapsed: 21.22s Total Time Elapsed: 49.00s`\
\
Let's see some of the summaries.\
\
Copied!\
\
`for dialogue, generated_summary, ground_truth_summary in zip(     dialogues[:5], generated_summaries[:5], ground_truth_summaries[:5] ):     print("Dialogue:", dialogue)     print("Generated Summary:", generated_summary)     print("Ground Truth Summary:", ground_truth_summary)     print("=============================")`\
\
`Dialogue: b'Tony: Is the boss in?\r\nClaire: Not yet.\r\nTony: Could let me know when he comes, please? \r\nClaire: Of course.\r\nTony: Thank you.' Generated Summary: Tony will let Claire know when her boss comes. Ground Truth Summary: b"The boss isn't in yet. Claire will let Tony know when he comes." ============================= Dialogue: b"James: What shouldl I get her?\r\nTim: who?\r\nJames: gees Mary my girlfirend\r\nTim: Am I really the person you should be asking?\r\nJames: oh come on it's her birthday on Sat\r\nTim: ask Sandy\r\nTim: I honestly am not the right person to ask this\r\nJames: ugh fine!" Generated Summary: Mary's girlfriend is birthday. James and Tim are going to ask Sandy to buy her. Ground Truth Summary: b"Mary's birthday is on Saturday. Her boyfriend, James, is looking for gift ideas. Tim suggests that he ask Sandy." ============================= Dialogue: b"Mary: So, how's Israel? Have you been on the beach?\r\nKate: It's so expensive! But they say, it's Tel Aviv... Tomorrow we are going to Jerusalem.\r\nMary: I've heard Israel is expensive, Monica was there on vacation last year, she complained about how pricey it is. Are you going to the Dead Sea before it dies? ahahahha\r\nKate: ahahhaha yup, in few days." Generated Summary: Kate is on vacation in Tel Aviv. Mary will visit the Dead Sea in a few days. Ground Truth Summary: b'Mary and Kate discuss how expensive Israel is. Kate is in Tel Aviv now, planning to travel to Jerusalem tomorrow, and to the Dead Sea few days later.' ============================= Dialogue: b"Giny: do we have rice?\r\nRiley: nope, it's finished\r\nGiny: fuck!\r\nGiny: ok, I'll buy" Generated Summary: Giny wants to buy rice from Riley. Ground Truth Summary: b"Giny and Riley don't have any rice left. Giny will buy some." ============================= Dialogue: b"Jude: i'll be in warsaw at the beginning of december so we could meet again\r\nLeon: !!!\r\nLeon: at the beginning means...?\r\nLeon: cuz I won't be here during the first weekend\r\nJude: 10\r\nJude: but i think it's a monday, so never mind i guess :D\r\nLeon: yeah monday doesn't really work for me :D\r\nLeon: :<\r\nJude: oh well next time :d\r\nLeon: yeah...!" Generated Summary: Jude and Leon will meet again this weekend at 10 am. Ground Truth Summary: b'Jude is coming to Warsaw on the 10th of December and wants to see Leon. Leon has no time.' =============================`\
\
The generated summaries look awesome! Not bad for a model trained only for 1 epoch and on 5000 examples :) \`\`\`\
\
* * *\
\
Relevant Chapters from Deep Learning with Python\
------------------------------------------------\
\
*   [Chapter 15: Language models and the Transformer](https://deeplearningwithpython.io/chapters/chapter15_language-models-and-the-transformer)\
    \
*   [Chapter 16: Text generation](https://deeplearningwithpython.io/chapters/chapter16_text-generation)\
    \
\
[Abstractive Text Summarization with BART](https://keras.io/examples/nlp/abstractive_summarization_with_bart/#abstractive-text-summarization-with-bart)\
\
[Introduction](https://keras.io/examples/nlp/abstractive_summarization_with_bart/#introduction)\
\
[Setup](https://keras.io/examples/nlp/abstractive_summarization_with_bart/#setup)\
\
[Dataset](https://keras.io/examples/nlp/abstractive_summarization_with_bart/#dataset)\
\
[Fine-tune BART](https://keras.io/examples/nlp/abstractive_summarization_with_bart/#finetune-bart)\
\
[Generate summaries and evaluate them!](https://keras.io/examples/nlp/abstractive_summarization_with_bart/#generate-summaries-and-evaluate-them)