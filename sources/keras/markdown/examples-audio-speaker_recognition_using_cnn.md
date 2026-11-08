None

[Code examples](https://keras.io/examples/)

[Computer Vision](https://keras.io/examples/vision/)
 [Natural Language Processing](https://keras.io/examples/nlp/)
 [Structured Data](https://keras.io/examples/structured_data/)
 [Timeseries](https://keras.io/examples/timeseries/)
 [Generative Deep Learning](https://keras.io/examples/generative/)
 [Audio Data](https://keras.io/examples/audio/)
 [Vocal Track Separation with Encoder-Decoder Architecture](https://keras.io/examples/audio/vocal_track_separation/)
 [Automatic Speech Recognition with Transformer](https://keras.io/examples/audio/transformer_asr/)
 [Automatic Speech Recognition using CTC](https://keras.io/examples/audio/ctc_asr/)
 [Audio Classification with the STFTSpectrogram layer](https://keras.io/examples/audio/stft/)
 [Speaker Recognition](https://keras.io/examples/audio/speaker_recognition_using_cnn/)
 [English speaker accent recognition using Transfer Learning](https://keras.io/examples/audio/uk_ireland_accent_recognition/)
 [MelGAN-based spectrogram inversion using feature matching](https://keras.io/examples/audio/melgan_spectrogram_inversion/)
 [Reinforcement Learning](https://keras.io/examples/rl/)
 [Graph Data](https://keras.io/examples/graph/)
 [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)

► [Code examples](https://keras.io/examples/)
 / [Audio Data](https://keras.io/examples/audio/)
 / Speaker Recognition

Speaker Recognition
===================

**Author:** [Fadi Badine](https://twitter.com/fadibadine)
  
**Date created:** 14/06/2020  
**Last modified:** 19/07/2023  
**Description:** Classify speakers using Fast Fourier Transform (FFT) and a 1D Convnet.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/audio/ipynb/speaker_recognition_using_cnn.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/audio/speaker_recognition_using_cnn.py)

* * *

Introduction
------------

This example demonstrates how to create a model to classify speakers from the frequency domain representation of speech recordings, obtained via Fast Fourier Transform (FFT).

It shows the following:

*   How to use [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
     to load, preprocess and feed audio streams into a model
*   How to create a 1D convolutional network with residual connections for audio classification.

Our process:

*   We prepare a dataset of speech samples from different speakers, with the speaker as label.
*   We add background noise to these samples to augment our data.
*   We take the FFT of these samples.
*   We train a 1D convnet to predict the correct speaker given a noisy FFT speech sample.

Note:

*   This example should be run with TensorFlow 2.3 or higher, or `tf-nightly`.
*   The noise samples in the dataset need to be resampled to a sampling rate of 16000 Hz before using the code in this example. In order to do this, you will need to have installed `ffmpg`.

* * *

Setup
-----

Copied!

`import os  os.environ["KERAS_BACKEND"] = "tensorflow"  import shutil import numpy as np  import tensorflow as tf import keras  from pathlib import Path from IPython.display import display, Audio  # Get the data from https://www.kaggle.com/kongaevans/speaker-recognition-dataset/ # and save it to ./speaker-recognition-dataset.zip # then unzip it to ./16000_pcm_speeches`

Copied!

`!kaggle datasets download -d kongaevans/speaker-recognition-dataset !unzip -qq speaker-recognition-dataset.zip`

Copied!

`DATASET_ROOT = "16000_pcm_speeches"  # The folders in which we will put the audio samples and the noise samples AUDIO_SUBFOLDER = "audio" NOISE_SUBFOLDER = "noise"  DATASET_AUDIO_PATH = os.path.join(DATASET_ROOT, AUDIO_SUBFOLDER) DATASET_NOISE_PATH = os.path.join(DATASET_ROOT, NOISE_SUBFOLDER)  # Percentage of samples to use for validation VALID_SPLIT = 0.1  # Seed to use when shuffling the dataset and the noise SHUFFLE_SEED = 43  # The sampling rate to use. # This is the one used in all the audio samples. # We will resample all the noise to this sampling rate. # This will also be the output size of the audio wave samples # (since all samples are of 1 second long) SAMPLING_RATE = 16000  # The factor to multiply the noise with according to: #   noisy_sample = sample + noise * prop * scale #      where prop = sample_amplitude / noise_amplitude SCALE = 0.5  BATCH_SIZE = 128 EPOCHS = 1`

`Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 /home/fchollet/.kaggle/kaggle.json' Downloading speaker-recognition-dataset.zip to /home/fchollet/keras-io/scripts/tmp_5022915  90%|████████████████████████████████████▉    | 208M/231M [00:00<00:00, 217MB/s] 100%|█████████████████████████████████████████| 231M/231M [00:01<00:00, 227MB/s]`

* * *

Data preparation
----------------

The dataset is composed of 7 folders, divided into 2 groups:

*   Speech samples, with 5 folders for 5 different speakers. Each folder contains 1500 audio files, each 1 second long and sampled at 16000 Hz.
*   Background noise samples, with 2 folders and a total of 6 files. These files are longer than 1 second (and originally not sampled at 16000 Hz, but we will resample them to 16000 Hz). We will use those 6 files to create 354 1-second-long noise samples to be used for training.

Let's sort these 2 categories into 2 folders:

*   An `audio` folder which will contain all the per-speaker speech sample folders
*   A `noise` folder which will contain all the noise samples

Before sorting the audio and noise categories into 2 folders, we have the following directory structure:

Copied!

`main_directory/ ...speaker_a/ ...speaker_b/ ...speaker_c/ ...speaker_d/ ...speaker_e/ ...other/ ..._background_noise_/`

After sorting, we end up with the following structure:

Copied!

`main_directory/ ...audio/ ......speaker_a/ ......speaker_b/ ......speaker_c/ ......speaker_d/ ......speaker_e/ ...noise/ ......other/ ......_background_noise_/`

Copied!

``for folder in os.listdir(DATASET_ROOT):     if os.path.isdir(os.path.join(DATASET_ROOT, folder)):         if folder in [AUDIO_SUBFOLDER, NOISE_SUBFOLDER]:             # If folder is `audio` or `noise`, do nothing             continue         elif folder in ["other", "_background_noise_"]:             # If folder is one of the folders that contains noise samples,             # move it to the `noise` folder             shutil.move(                 os.path.join(DATASET_ROOT, folder),                 os.path.join(DATASET_NOISE_PATH, folder),             )         else:             # Otherwise, it should be a speaker folder, then move it to             # `audio` folder             shutil.move(                 os.path.join(DATASET_ROOT, folder),                 os.path.join(DATASET_AUDIO_PATH, folder),             )``

* * *

Noise preparation
-----------------

In this section:

*   We load all noise samples (which should have been resampled to 16000)
*   We split those noise samples to chunks of 16000 samples which correspond to 1 second duration each

Copied!

`# Get the list of all noise files noise_paths = [] for subdir in os.listdir(DATASET_NOISE_PATH):     subdir_path = Path(DATASET_NOISE_PATH) / subdir     if os.path.isdir(subdir_path):         noise_paths += [             os.path.join(subdir_path, filepath)             for filepath in os.listdir(subdir_path)             if filepath.endswith(".wav")         ] if not noise_paths:     raise RuntimeError(f"Could not find any files at {DATASET_NOISE_PATH}") print(     "Found {} files belonging to {} directories".format(         len(noise_paths), len(os.listdir(DATASET_NOISE_PATH))     ) )`

`Found 6 files belonging to 2 directories`

Resample all noise samples to 16000 Hz

Copied!

``command = (     "for dir in `ls -1 " + DATASET_NOISE_PATH + "`; do "     "for file in `ls -1 " + DATASET_NOISE_PATH + "/$dir/*.wav`; do "     "sample_rate=`ffprobe -hide_banner -loglevel panic -show_streams "     "$file | grep sample_rate | cut -f2 -d=`; "     "if [ $sample_rate -ne 16000 ]; then "     "ffmpeg -hide_banner -loglevel panic -y "     "-i $file -ar 16000 temp.wav; "     "mv temp.wav $file; "     "fi; done; done" ) os.system(command)  # Split noise into chunks of 16,000 steps each def load_noise_sample(path):     sample, sampling_rate = tf.audio.decode_wav(         tf.io.read_file(path), desired_channels=1     )     if sampling_rate == SAMPLING_RATE:         # Number of slices of 16000 each that can be generated from the noise sample         slices = int(sample.shape[0] / SAMPLING_RATE)         sample = tf.split(sample[: slices * SAMPLING_RATE], slices)         return sample     else:         print("Sampling rate for {} is incorrect. Ignoring it".format(path))         return None  noises = [] for path in noise_paths:     sample = load_noise_sample(path)     if sample:         noises.extend(sample) noises = tf.stack(noises)  print(     "{} noise files were split into {} noise samples where each is {} sec. long".format(         len(noise_paths), noises.shape[0], noises.shape[1] // SAMPLING_RATE     ) )``

`6 noise files were split into 354 noise samples where each is 1 sec. long`

* * *

Dataset generation
------------------

Copied!

``def paths_and_labels_to_dataset(audio_paths, labels):     """Constructs a dataset of audios and labels."""     path_ds = tf.data.Dataset.from_tensor_slices(audio_paths)     audio_ds = path_ds.map(         lambda x: path_to_audio(x), num_parallel_calls=tf.data.AUTOTUNE     )     label_ds = tf.data.Dataset.from_tensor_slices(labels)     return tf.data.Dataset.zip((audio_ds, label_ds))  def path_to_audio(path):     """Reads and decodes an audio file."""     audio = tf.io.read_file(path)     audio, _ = tf.audio.decode_wav(audio, 1, SAMPLING_RATE)     return audio  def add_noise(audio, noises=None, scale=0.5):     if noises is not None:         # Create a random tensor of the same size as audio ranging from         # 0 to the number of noise stream samples that we have.         tf_rnd = tf.random.uniform(             (tf.shape(audio)[0],), 0, noises.shape[0], dtype=tf.int32         )         noise = tf.gather(noises, tf_rnd, axis=0)          # Get the amplitude proportion between the audio and the noise         prop = tf.math.reduce_max(audio, axis=1) / tf.math.reduce_max(noise, axis=1)         prop = tf.repeat(tf.expand_dims(prop, axis=1), tf.shape(audio)[1], axis=1)          # Adding the rescaled noise to audio         audio = audio + noise * prop * scale      return audio  def audio_to_fft(audio):     # Since tf.signal.fft applies FFT on the innermost dimension,     # we need to squeeze the dimensions and then expand them again     # after FFT     audio = tf.squeeze(audio, axis=-1)     fft = tf.signal.fft(         tf.cast(tf.complex(real=audio, imag=tf.zeros_like(audio)), tf.complex64)     )     fft = tf.expand_dims(fft, axis=-1)      # Return the absolute value of the first half of the FFT     # which represents the positive frequencies     return tf.math.abs(fft[:, : (audio.shape[1] // 2), :])  # Get the list of audio file paths along with their corresponding labels  class_names = os.listdir(DATASET_AUDIO_PATH) print(     "Our class names: {}".format(         class_names,     ) )  audio_paths = [] labels = [] for label, name in enumerate(class_names):     print(         "Processing speaker {}".format(             name,         )     )     dir_path = Path(DATASET_AUDIO_PATH) / name     speaker_sample_paths = [         os.path.join(dir_path, filepath)         for filepath in os.listdir(dir_path)         if filepath.endswith(".wav")     ]     audio_paths += speaker_sample_paths     labels += [label] * len(speaker_sample_paths)  print(     "Found {} files belonging to {} classes.".format(len(audio_paths), len(class_names)) )  # Shuffle rng = np.random.RandomState(SHUFFLE_SEED) rng.shuffle(audio_paths) rng = np.random.RandomState(SHUFFLE_SEED) rng.shuffle(labels)  # Split into training and validation num_val_samples = int(VALID_SPLIT * len(audio_paths)) print("Using {} files for training.".format(len(audio_paths) - num_val_samples)) train_audio_paths = audio_paths[:-num_val_samples] train_labels = labels[:-num_val_samples]  print("Using {} files for validation.".format(num_val_samples)) valid_audio_paths = audio_paths[-num_val_samples:] valid_labels = labels[-num_val_samples:]  # Create 2 datasets, one for training and the other for validation train_ds = paths_and_labels_to_dataset(train_audio_paths, train_labels) train_ds = train_ds.shuffle(buffer_size=BATCH_SIZE * 8, seed=SHUFFLE_SEED).batch(     BATCH_SIZE )  valid_ds = paths_and_labels_to_dataset(valid_audio_paths, valid_labels) valid_ds = valid_ds.shuffle(buffer_size=32 * 8, seed=SHUFFLE_SEED).batch(32)  # Add noise to the training set train_ds = train_ds.map(     lambda x, y: (add_noise(x, noises, scale=SCALE), y),     num_parallel_calls=tf.data.AUTOTUNE, )  # Transform audio wave to the frequency domain using `audio_to_fft` train_ds = train_ds.map(     lambda x, y: (audio_to_fft(x), y), num_parallel_calls=tf.data.AUTOTUNE ) train_ds = train_ds.prefetch(tf.data.AUTOTUNE)  valid_ds = valid_ds.map(     lambda x, y: (audio_to_fft(x), y), num_parallel_calls=tf.data.AUTOTUNE ) valid_ds = valid_ds.prefetch(tf.data.AUTOTUNE)``

`Our class names: ['Nelson_Mandela', 'Jens_Stoltenberg', 'Benjamin_Netanyau', 'Julia_Gillard', 'Magaret_Tarcher'] Processing speaker Nelson_Mandela Processing speaker Jens_Stoltenberg Processing speaker Benjamin_Netanyau Processing speaker Julia_Gillard Processing speaker Magaret_Tarcher Found 7501 files belonging to 5 classes. Using 6751 files for training. Using 750 files for validation.`

* * *

Model Definition
----------------

Copied!

`def residual_block(x, filters, conv_num=3, activation="relu"):     # Shortcut     s = keras.layers.Conv1D(filters, 1, padding="same")(x)     for i in range(conv_num - 1):         x = keras.layers.Conv1D(filters, 3, padding="same")(x)         x = keras.layers.Activation(activation)(x)     x = keras.layers.Conv1D(filters, 3, padding="same")(x)     x = keras.layers.Add()([x, s])     x = keras.layers.Activation(activation)(x)     return keras.layers.MaxPool1D(pool_size=2, strides=2)(x)  def build_model(input_shape, num_classes):     inputs = keras.layers.Input(shape=input_shape, name="input")      x = residual_block(inputs, 16, 2)     x = residual_block(x, 32, 2)     x = residual_block(x, 64, 3)     x = residual_block(x, 128, 3)     x = residual_block(x, 128, 3)      x = keras.layers.AveragePooling1D(pool_size=3, strides=3)(x)     x = keras.layers.Flatten()(x)     x = keras.layers.Dense(256, activation="relu")(x)     x = keras.layers.Dense(128, activation="relu")(x)      outputs = keras.layers.Dense(num_classes, activation="softmax", name="output")(x)      return keras.models.Model(inputs=inputs, outputs=outputs)  model = build_model((SAMPLING_RATE // 2, 1), len(class_names))  model.summary()  # Compile the model using Adam's default learning rate model.compile(     optimizer="Adam",     loss="sparse_categorical_crossentropy",     metrics=["accuracy"], )  # Add callbacks: # 'EarlyStopping' to stop training when the model is not enhancing anymore # 'ModelCheckPoint' to always keep the model that has the best val_accuracy model_save_filename = "model.keras"  earlystopping_cb = keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True) mdlcheckpoint_cb = keras.callbacks.ModelCheckpoint(     model_save_filename, monitor="val_accuracy", save_best_only=True )`

Model: "functional\_1"

┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Layer (type)        ┃ Output Shape      ┃ Param # ┃ Connected to         ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ input (InputLayer)  │ (None, 8000, 1)   │       0 │ -                    │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d\_1 (Conv1D)   │ (None, 8000, 16)  │      64 │ input\[0\]\[0\]          │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ activation          │ (None, 8000, 16)  │       0 │ conv1d\_1\[0\]\[0\]       │
│ (Activation)        │                   │         │                      │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d\_2 (Conv1D)   │ (None, 8000, 16)  │     784 │ activation\[0\]\[0\]     │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d (Conv1D)     │ (None, 8000, 16)  │      32 │ input\[0\]\[0\]          │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ add (Add)           │ (None, 8000, 16)  │       0 │ conv1d\_2\[0\]\[0\],      │
│                     │                   │         │ conv1d\[0\]\[0\]         │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ activation\_1        │ (None, 8000, 16)  │       0 │ add\[0\]\[0\]            │
│ (Activation)        │                   │         │                      │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ max\_pooling1d       │ (None, 4000, 16)  │       0 │ activation\_1\[0\]\[0\]   │
│ (MaxPooling1D)      │                   │         │                      │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d\_4 (Conv1D)   │ (None, 4000, 32)  │   1,568 │ max\_pooling1d\[0\]\[0\]  │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ activation\_2        │ (None, 4000, 32)  │       0 │ conv1d\_4\[0\]\[0\]       │
│ (Activation)        │                   │         │                      │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d\_5 (Conv1D)   │ (None, 4000, 32)  │   3,104 │ activation\_2\[0\]\[0\]   │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d\_3 (Conv1D)   │ (None, 4000, 32)  │     544 │ max\_pooling1d\[0\]\[0\]  │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ add\_1 (Add)         │ (None, 4000, 32)  │       0 │ conv1d\_5\[0\]\[0\],      │
│                     │                   │         │ conv1d\_3\[0\]\[0\]       │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ activation\_3        │ (None, 4000, 32)  │       0 │ add\_1\[0\]\[0\]          │
│ (Activation)        │                   │         │                      │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ max\_pooling1d\_1     │ (None, 2000, 32)  │       0 │ activation\_3\[0\]\[0\]   │
│ (MaxPooling1D)      │                   │         │                      │
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤
│ conv1d\_7 (Conv1D)   │ (None, 2000, 64)  │   6,208 │ max\_pooling1d\_1\[0\]\[… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_4        │ (None, 2000, 64)  │       0 │ conv1d\_7\[0\]\[0\]       │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_8 (Conv1D)   │ (None, 2000, 64)  │  12,352 │ activation\_4\[0\]\[0\]   │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_5        │ (None, 2000, 64)  │       0 │ conv1d\_8\[0\]\[0\]       │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_9 (Conv1D)   │ (None, 2000, 64)  │  12,352 │ activation\_5\[0\]\[0\]   │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_6 (Conv1D)   │ (None, 2000, 64)  │   2,112 │ max\_pooling1d\_1\[0\]\[… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ add\_2 (Add)         │ (None, 2000, 64)  │       0 │ conv1d\_9\[0\]\[0\],      │\
│                     │                   │         │ conv1d\_6\[0\]\[0\]       │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_6        │ (None, 2000, 64)  │       0 │ add\_2\[0\]\[0\]          │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ max\_pooling1d\_2     │ (None, 1000, 64)  │       0 │ activation\_6\[0\]\[0\]   │\
│ (MaxPooling1D)      │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_11 (Conv1D)  │ (None, 1000, 128) │  24,704 │ max\_pooling1d\_2\[0\]\[… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_7        │ (None, 1000, 128) │       0 │ conv1d\_11\[0\]\[0\]      │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_12 (Conv1D)  │ (None, 1000, 128) │  49,280 │ activation\_7\[0\]\[0\]   │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_8        │ (None, 1000, 128) │       0 │ conv1d\_12\[0\]\[0\]      │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_13 (Conv1D)  │ (None, 1000, 128) │  49,280 │ activation\_8\[0\]\[0\]   │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_10 (Conv1D)  │ (None, 1000, 128) │   8,320 │ max\_pooling1d\_2\[0\]\[… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ add\_3 (Add)         │ (None, 1000, 128) │       0 │ conv1d\_13\[0\]\[0\],     │\
│                     │                   │         │ conv1d\_10\[0\]\[0\]      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_9        │ (None, 1000, 128) │       0 │ add\_3\[0\]\[0\]          │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ max\_pooling1d\_3     │ (None, 500, 128)  │       0 │ activation\_9\[0\]\[0\]   │\
│ (MaxPooling1D)      │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_15 (Conv1D)  │ (None, 500, 128)  │  49,280 │ max\_pooling1d\_3\[0\]\[… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_10       │ (None, 500, 128)  │       0 │ conv1d\_15\[0\]\[0\]      │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_16 (Conv1D)  │ (None, 500, 128)  │  49,280 │ activation\_10\[0\]\[0\]  │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_11       │ (None, 500, 128)  │       0 │ conv1d\_16\[0\]\[0\]      │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_17 (Conv1D)  │ (None, 500, 128)  │  49,280 │ activation\_11\[0\]\[0\]  │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ conv1d\_14 (Conv1D)  │ (None, 500, 128)  │  16,512 │ max\_pooling1d\_3\[0\]\[… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ add\_4 (Add)         │ (None, 500, 128)  │       0 │ conv1d\_17\[0\]\[0\],     │\
│                     │                   │         │ conv1d\_14\[0\]\[0\]      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ activation\_12       │ (None, 500, 128)  │       0 │ add\_4\[0\]\[0\]          │\
│ (Activation)        │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ max\_pooling1d\_4     │ (None, 250, 128)  │       0 │ activation\_12\[0\]\[0\]  │\
│ (MaxPooling1D)      │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ average\_pooling1d   │ (None, 83, 128)   │       0 │ max\_pooling1d\_4\[0\]\[… │\
│ (AveragePooling1D)  │                   │         │                      │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ flatten (Flatten)   │ (None, 10624)     │       0 │ average\_pooling1d\[0… │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ dense (Dense)       │ (None, 256)       │ 2,720,… │ flatten\[0\]\[0\]        │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ dense\_1 (Dense)     │ (None, 128)       │  32,896 │ dense\[0\]\[0\]          │\
├─────────────────────┼───────────────────┼─────────┼──────────────────────┤\
│ output (Dense)      │ (None, 5)         │     645 │ dense\_1\[0\]\[0\]        │\
└─────────────────────┴───────────────────┴─────────┴──────────────────────┘\
\
 Total params: 3,088,597 (11.78 MB)\
\
 Trainable params: 3,088,597 (11.78 MB)\
\
 Non-trainable params: 0 (0.00 B)\
\
* * *\
\
Training\
--------\
\
Copied!\
\
`history = model.fit(     train_ds,     epochs=EPOCHS,     validation_data=valid_ds,     callbacks=[earlystopping_cb, mdlcheckpoint_cb], )`\
\
`WARNING: All log messages before absl::InitializeLog() is called are written to STDERR I0000 00:00:1699469571.349760  302130 device_compiler.h:186] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process. W0000 00:00:1699469571.377393  302130 graph_launch.cc:671] Fallback to op-by-op mode because memset node breaks graph update   52/53 ━━━━━━━━━━━━━━━━━━━[37m━  0s 396ms/step - accuracy: 0.4496 - loss: 5.2439  W0000 00:00:1699469622.140353  302129 graph_launch.cc:671] Fallback to op-by-op mode because memset node breaks graph update   53/53 ━━━━━━━━━━━━━━━━━━━━ 0s 974ms/step - accuracy: 0.4531 - loss: 5.1842  W0000 00:00:1699469625.456199  302130 graph_launch.cc:671] Fallback to op-by-op mode because memset node breaks graph update W0000 00:00:1699469627.405341  302129 graph_launch.cc:671] Fallback to op-by-op mode because memset node breaks graph update   53/53 ━━━━━━━━━━━━━━━━━━━━ 101s 1s/step - accuracy: 0.4564 - loss: 5.1267 - val_accuracy: 0.8720 - val_loss: 0.3273`\
\
* * *\
\
Evaluation\
----------\
\
Copied!\
\
`print(model.evaluate(valid_ds))`\
\
 `24/24 ━━━━━━━━━━━━━━━━━━━━ 0s 5ms/step - accuracy: 0.8641 - loss: 0.3521 [0.32171541452407837, 0.871999979019165]`\
\
We get ~ 98% validation accuracy.\
\
* * *\
\
Demonstration\
-------------\
\
Let's take some samples and:\
\
*   Predict the speaker\
*   Compare the prediction with the real speaker\
*   Listen to the audio to see that despite the samples being noisy, the model is still pretty accurate\
\
Copied!\
\
`SAMPLES_TO_DISPLAY = 10  test_ds = paths_and_labels_to_dataset(valid_audio_paths, valid_labels) test_ds = test_ds.shuffle(buffer_size=BATCH_SIZE * 8, seed=SHUFFLE_SEED).batch(     BATCH_SIZE )  test_ds = test_ds.map(     lambda x, y: (add_noise(x, noises, scale=SCALE), y),     num_parallel_calls=tf.data.AUTOTUNE, )  for audios, labels in test_ds.take(1):     # Get the signal FFT     ffts = audio_to_fft(audios)     # Predict     y_pred = model.predict(ffts)     # Take random samples     rnd = np.random.randint(0, BATCH_SIZE, SAMPLES_TO_DISPLAY)     audios = audios.numpy()[rnd, :, :]     labels = labels.numpy()[rnd]     y_pred = np.argmax(y_pred, axis=-1)[rnd]      for index in range(SAMPLES_TO_DISPLAY):         # For every sample, print the true and predicted label         # as well as run the voice with the noise         print(             "Speaker:\33{} {}\33[0m\tPredicted:\33{} {}\33[0m".format(                 "[92m" if labels[index] == y_pred[index] else "[91m",                 class_names[labels[index]],                 "[92m" if labels[index] == y_pred[index] else "[91m",                 class_names[y_pred[index]],             )         )         display(Audio(audios[index, :, :].squeeze(), rate=SAMPLING_RATE))`\
\
 `4/4 ━━━━━━━━━━━━━━━━━━━━ 1s 3ms/step   Speaker:[91m Magaret_Tarcher   Predicted:[91m Benjamin_Netanyau  W0000 00:00:1699469629.002282  302130 graph_launch.cc:671] Fallback to op-by-op mode because memset node breaks graph update`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Julia_Gillard Predicted:[92m Julia_Gillard`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Nelson_Mandela    Predicted:[92m Nelson_Mandela`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Magaret_Tarcher   Predicted:[92m Magaret_Tarcher`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Julia_Gillard Predicted:[92m Julia_Gillard`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Julia_Gillard Predicted:[92m Julia_Gillard`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Jens_Stoltenberg  Predicted:[92m Jens_Stoltenberg`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Benjamin_Netanyau Predicted:[92m Benjamin_Netanyau`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Nelson_Mandela    Predicted:[92m Nelson_Mandela`\
\
 Your browser does not support the audio element.\
\
`Speaker:[92m Nelson_Mandela    Predicted:[92m Nelson_Mandela`\
\
 Your browser does not support the audio element.\
\
[Speaker Recognition](https://keras.io/examples/audio/speaker_recognition_using_cnn/#speaker-recognition)\
\
[Introduction](https://keras.io/examples/audio/speaker_recognition_using_cnn/#introduction)\
\
[Setup](https://keras.io/examples/audio/speaker_recognition_using_cnn/#setup)\
\
[Data preparation](https://keras.io/examples/audio/speaker_recognition_using_cnn/#data-preparation)\
\
[Noise preparation](https://keras.io/examples/audio/speaker_recognition_using_cnn/#noise-preparation)\
\
[Dataset generation](https://keras.io/examples/audio/speaker_recognition_using_cnn/#dataset-generation)\
\
[Model Definition](https://keras.io/examples/audio/speaker_recognition_using_cnn/#model-definition)\
\
[Training](https://keras.io/examples/audio/speaker_recognition_using_cnn/#training)\
\
[Evaluation](https://keras.io/examples/audio/speaker_recognition_using_cnn/#evaluation)\
\
[Demonstration](https://keras.io/examples/audio/speaker_recognition_using_cnn/#demonstration)