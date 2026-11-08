None

[Code examples](https://keras.io/examples/)

[Computer Vision](https://keras.io/examples/vision/)
 [Natural Language Processing](https://keras.io/examples/nlp/)
 [Structured Data](https://keras.io/examples/structured_data/)
 [Structured data classification with FeatureSpace](https://keras.io/examples/structured_data/structured_data_classification_with_feature_space/)
 [FeatureSpace advanced use cases](https://keras.io/examples/structured_data/feature_space_advanced/)
 [Imbalanced classification: credit card fraud detection](https://keras.io/examples/structured_data/imbalanced_classification/)
 [Structured data classification from scratch](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/)
 [Structured data learning with Wide, Deep, and Cross networks](https://keras.io/examples/structured_data/wide_deep_cross_networks/)
 [Deep Learning for Customer Lifetime Value](https://keras.io/examples/structured_data/customer_lifetime_value/)
 [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)
 [Classification with TensorFlow Decision Forests](https://keras.io/examples/structured_data/classification_with_tfdf/)
 [Classification with Neural Decision Forests](https://keras.io/examples/structured_data/deep_neural_decision_forests/)
 [Structured data learning with TabTransformer](https://keras.io/examples/structured_data/tabtransformer/)
 [Classification with Gated Residual and Variable Selection Networks with HyperParameters tuning](https://keras.io/examples/structured_data/class_with_grn_and_vsn_with_hyperparameters_tuning/)
 [Collaborative Filtering for Movie Recommendations](https://keras.io/examples/structured_data/collaborative_filtering_movielens/)
 [A Transformer-based recommendation system](https://keras.io/examples/structured_data/movielens_recommendations_transformers/)
 [Timeseries](https://keras.io/examples/timeseries/)
 [Generative Deep Learning](https://keras.io/examples/generative/)
 [Audio Data](https://keras.io/examples/audio/)
 [Reinforcement Learning](https://keras.io/examples/rl/)
 [Graph Data](https://keras.io/examples/graph/)
 [Quick Keras Recipes](https://keras.io/examples/keras_recipes/)

► [Code examples](https://keras.io/examples/)
 / [Structured Data](https://keras.io/examples/structured_data/)
 / A Transformer-based recommendation system

A Transformer-based recommendation system
=========================================

**Author:** [Khalid Salama](https://www.linkedin.com/in/khalid-salama-24403144/)
  
**Date created:** 2020/12/30  
**Last modified:** 2025/01/27  
**Description:** Rating rate prediction using the Behavior Sequence Transformer (BST) model on the Movielens.

ⓘ This example uses Keras 3

![](https://colab.research.google.com/img/colab_favicon.ico) [**View in Colab**](https://colab.research.google.com/github/keras-team/keras-io/blob/master/examples/structured_data/ipynb/movielens_recommendations_transformers.ipynb)
 •![](https://github.com/favicon.ico) [**GitHub source**](https://github.com/keras-team/keras-io/blob/master/examples/structured_data/movielens_recommendations_transformers.py)

* * *

Introduction
------------

This example demonstrates the [Behavior Sequence Transformer (BST)](https://arxiv.org/abs/1905.06874)
 model, by Qiwei Chen et al., using the [Movielens dataset](https://grouplens.org/datasets/movielens/)
. The BST model leverages the sequential behaviour of the users in watching and rating movies, as well as user profile and movie features, to predict the rating of the user to a target movie.

More precisely, the BST model aims to predict the rating of a target movie by accepting the following inputs:

1.  A fixed-length _sequence_ of `movie_ids` watched by a user.
2.  A fixed-length _sequence_ of the `ratings` for the movies watched by a user.
3.  A _set_ of user features, including `user_id`, `sex`, `occupation`, and `age_group`.
4.  A _set_ of `genres` for each movie in the input sequence and the target movie.
5.  A `target_movie_id` for which to predict the rating.

This example modifies the original BST model in the following ways:

1.  We incorporate the movie features (genres) into the processing of the embedding of each movie of the input sequence and the target movie, rather than treating them as "other features" outside the transformer layer.
2.  We utilize the ratings of movies in the input sequence, along with the their positions in the sequence, to update them before feeding them into the self-attention layer.

Note that this example should be run with TensorFlow 2.4 or higher.

* * *

The dataset
-----------

We use the [1M version of the Movielens dataset](https://grouplens.org/datasets/movielens/1m/)
. The dataset includes around 1 million ratings from 6000 users on 4000 movies, along with some user features, movie genres. In addition, the timestamp of each user-movie rating is provided, which allows creating sequences of movie ratings for each user, as expected by the BST model.

* * *

Setup
-----

Copied!

`import os  os.environ["KERAS_BACKEND"] = "jax"  # or torch, or tensorflow  import math from zipfile import ZipFile from urllib.request import urlretrieve import numpy as np import pandas as pd  import keras from keras import layers, ops from keras.layers import StringLookup`

* * *

Prepare the data
----------------

### Download and prepare the DataFrames

First, let's download the movielens data.

The downloaded folder will contain three data files: `users.dat`, `movies.dat`, and `ratings.dat`.

Copied!

`urlretrieve("http://files.grouplens.org/datasets/movielens/ml-1m.zip", "movielens.zip") ZipFile("movielens.zip", "r").extractall()`

Then, we load the data into pandas DataFrames with their proper column names.

Copied!

`users = pd.read_csv(     "ml-1m/users.dat",     sep="::",     names=["user_id", "sex", "age_group", "occupation", "zip_code"],     encoding="ISO-8859-1",     engine="python", )  ratings = pd.read_csv(     "ml-1m/ratings.dat",     sep="::",     names=["user_id", "movie_id", "rating", "unix_timestamp"],     encoding="ISO-8859-1",     engine="python", )  movies = pd.read_csv(     "ml-1m/movies.dat",     sep="::",     names=["movie_id", "title", "genres"],     encoding="ISO-8859-1",     engine="python", )`

Here, we do some simple data processing to fix the data types of the columns.

Copied!

`users["user_id"] = users["user_id"].apply(lambda x: f"user_{x}") users["age_group"] = users["age_group"].apply(lambda x: f"group_{x}") users["occupation"] = users["occupation"].apply(lambda x: f"occupation_{x}")  movies["movie_id"] = movies["movie_id"].apply(lambda x: f"movie_{x}")  ratings["movie_id"] = ratings["movie_id"].apply(lambda x: f"movie_{x}") ratings["user_id"] = ratings["user_id"].apply(lambda x: f"user_{x}") ratings["rating"] = ratings["rating"].apply(lambda x: float(x))`

Each movie has multiple genres. We split them into separate columns in the `movies` DataFrame.

Copied!

`genres = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime"] genres += ["Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical"] genres += ["Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]  for genre in genres:     movies[genre] = movies["genres"].apply(         lambda values: int(genre in values.split("|"))     )`

### Transform the movie ratings data into sequences

First, let's sort the the ratings data using the `unix_timestamp`, and then group the `movie_id` values and the `rating` values by `user_id`.

The output DataFrame will have a record for each `user_id`, with two ordered lists (sorted by rating datetime): the movies they have rated, and their ratings of these movies.

Copied!

`ratings_group = ratings.sort_values(by=["unix_timestamp"]).groupby("user_id")  ratings_data = pd.DataFrame(     data={         "user_id": list(ratings_group.groups.keys()),         "movie_ids": list(ratings_group.movie_id.apply(list)),         "ratings": list(ratings_group.rating.apply(list)),         "timestamps": list(ratings_group.unix_timestamp.apply(list)),     } )`

Now, let's split the `movie_ids` list into a set of sequences of a fixed length. We do the same for the `ratings`. Set the `sequence_length` variable to change the length of the input sequence to the model. You can also change the `step_size` to control the number of sequences to generate for each user.

Copied!

`sequence_length = 4 step_size = 2  def create_sequences(values, window_size, step_size):     sequences = []     start_index = 0     while True:         end_index = start_index + window_size         seq = values[start_index:end_index]         if len(seq) < window_size:             seq = values[-window_size:]             if len(seq) == window_size:                 sequences.append(seq)             break         sequences.append(seq)         start_index += step_size     return sequences  ratings_data.movie_ids = ratings_data.movie_ids.apply(     lambda ids: create_sequences(ids, sequence_length, step_size) )  ratings_data.ratings = ratings_data.ratings.apply(     lambda ids: create_sequences(ids, sequence_length, step_size) )  del ratings_data["timestamps"]`

After that, we process the output to have each sequence in a separate records in the DataFrame. In addition, we join the user features with the ratings data.

Copied!

`ratings_data_movies = ratings_data[["user_id", "movie_ids"]].explode(     "movie_ids", ignore_index=True ) ratings_data_rating = ratings_data[["ratings"]].explode("ratings", ignore_index=True) ratings_data_transformed = pd.concat([ratings_data_movies, ratings_data_rating], axis=1) ratings_data_transformed = ratings_data_transformed.join(     users.set_index("user_id"), on="user_id" ) ratings_data_transformed.movie_ids = ratings_data_transformed.movie_ids.apply(     lambda x: ",".join(x) ) ratings_data_transformed.ratings = ratings_data_transformed.ratings.apply(     lambda x: ",".join([str(v) for v in x]) )  del ratings_data_transformed["zip_code"]  ratings_data_transformed.rename(     columns={"movie_ids": "sequence_movie_ids", "ratings": "sequence_ratings"},     inplace=True, )`

With `sequence_length` of 4 and `step_size` of 2, we end up with 498,623 sequences.

Finally, we split the data into training and testing splits, with 85% and 15% of the instances, respectively, and store them to CSV files.

Copied!

`random_selection = np.random.rand(len(ratings_data_transformed.index)) <= 0.85 train_data = ratings_data_transformed[random_selection] test_data = ratings_data_transformed[~random_selection]  train_data.to_csv("train_data.csv", index=False, sep="|", header=False) test_data.to_csv("test_data.csv", index=False, sep="|", header=False)`

* * *

Define metadata
---------------

Copied!

`CSV_HEADER = list(ratings_data_transformed.columns)  CATEGORICAL_FEATURES_WITH_VOCABULARY = {     "user_id": list(users.user_id.unique()),     "movie_id": list(movies.movie_id.unique()),     "sex": list(users.sex.unique()),     "age_group": list(users.age_group.unique()),     "occupation": list(users.occupation.unique()), }  USER_FEATURES = ["sex", "age_group", "occupation"]  MOVIE_FEATURES = ["genres"]`

* * *

Encode input features
---------------------

The `encode_input_features` function works as follows:

1.  Each categorical user feature is encoded using `layers.Embedding`, with embedding dimension equals to the square root of the vocabulary size of the feature. The embeddings of these features are concatenated to form a single input tensor.
    
2.  Each movie in the movie sequence and the target movie is encoded `layers.Embedding`, where the dimension size is the square root of the number of movies.
    
3.  A multi-hot genres vector for each movie is concatenated with its embedding vector, and processed using a non-linear `layers.Dense` to output a vector of the same movie embedding dimensions.
    
4.  A positional embedding is added to each movie embedding in the sequence, and then multiplied by its rating from the ratings sequence.
    
5.  The target movie embedding is concatenated to the sequence movie embeddings, producing a tensor with the shape of `[batch size, sequence length, embedding size]`, as expected by the attention layer for the transformer architecture.
    
6.  The method returns a tuple of two elements: `encoded_transformer_features` and `encoded_other_features`.
    

Copied!

`# Required for tf.data.Dataset import tensorflow as tf  def get_dataset_from_csv(csv_file_path, batch_size, shuffle=True):      def process(features):         movie_ids_string = features["sequence_movie_ids"]         sequence_movie_ids = tf.strings.split(movie_ids_string, ",").to_tensor()         # The last movie id in the sequence is the target movie.         features["target_movie_id"] = sequence_movie_ids[:, -1]         features["sequence_movie_ids"] = sequence_movie_ids[:, :-1]         # Sequence ratings         ratings_string = features["sequence_ratings"]         sequence_ratings = tf.strings.to_number(             tf.strings.split(ratings_string, ","), tf.dtypes.float32         ).to_tensor()         # The last rating in the sequence is the target for the model to predict.         target = sequence_ratings[:, -1]         features["sequence_ratings"] = sequence_ratings[:, :-1]          def encoding_helper(feature_name):              # This are target_movie_id and sequence_movie_ids and they have the same             # vocabulary as movie_id.             if feature_name not in CATEGORICAL_FEATURES_WITH_VOCABULARY:                 vocabulary = CATEGORICAL_FEATURES_WITH_VOCABULARY["movie_id"]                 index_lookup = StringLookup(                     vocabulary=vocabulary, mask_token=None, num_oov_indices=0                 )                 # Convert the string input values into integer indices.                 value_index = index_lookup(features[feature_name])                 features[feature_name] = value_index             else:                 # movie_id is not part of the features, hence not processed. It was mainly required                 # for its vocabulary above.                 if feature_name == "movie_id":                     pass                 else:                     vocabulary = CATEGORICAL_FEATURES_WITH_VOCABULARY[feature_name]                     index_lookup = StringLookup(                         vocabulary=vocabulary, mask_token=None, num_oov_indices=0                     )                     # Convert the string input values into integer indices.                     value_index = index_lookup(features[feature_name])                     features[feature_name] = value_index          # Encode the user features         for feature_name in CATEGORICAL_FEATURES_WITH_VOCABULARY:             encoding_helper(feature_name)         # Encoding target_movie_id and returning it as the target variable         encoding_helper("target_movie_id")         # Encoding sequence movie_ids.         encoding_helper("sequence_movie_ids")         return dict(features), target      dataset = tf.data.experimental.make_csv_dataset(         csv_file_path,         batch_size=batch_size,         column_names=CSV_HEADER,         num_epochs=1,         header=False,         field_delim="|",         shuffle=shuffle,     ).map(process)     return dataset  def encode_input_features(     inputs,     include_user_id,     include_user_features,     include_movie_features, ):     encoded_transformer_features = []     encoded_other_features = []      other_feature_names = []     if include_user_id:         other_feature_names.append("user_id")     if include_user_features:         other_feature_names.extend(USER_FEATURES)      ## Encode user features     for feature_name in other_feature_names:         vocabulary = CATEGORICAL_FEATURES_WITH_VOCABULARY[feature_name]         # Compute embedding dimensions         embedding_dims = int(math.sqrt(len(vocabulary)))         # Create an embedding layer with the specified dimensions.         embedding_encoder = layers.Embedding(             input_dim=len(vocabulary),             output_dim=embedding_dims,             name=f"{feature_name}_embedding",         )         # Convert the index values to embedding representations.         encoded_other_features.append(embedding_encoder(inputs[feature_name]))      ## Create a single embedding vector for the user features     if len(encoded_other_features) > 1:         encoded_other_features = layers.concatenate(encoded_other_features)     elif len(encoded_other_features) == 1:         encoded_other_features = encoded_other_features[0]     else:         encoded_other_features = None      ## Create a movie embedding encoder     movie_vocabulary = CATEGORICAL_FEATURES_WITH_VOCABULARY["movie_id"]     movie_embedding_dims = int(math.sqrt(len(movie_vocabulary)))     # Create an embedding layer with the specified dimensions.     movie_embedding_encoder = layers.Embedding(         input_dim=len(movie_vocabulary),         output_dim=movie_embedding_dims,         name=f"movie_embedding",     )     # Create a vector lookup for movie genres.     genre_vectors = movies[genres].to_numpy()     movie_genres_lookup = layers.Embedding(         input_dim=genre_vectors.shape[0],         output_dim=genre_vectors.shape[1],         embeddings_initializer=keras.initializers.Constant(genre_vectors),         trainable=False,         name="genres_vector",     )     # Create a processing layer for genres.     movie_embedding_processor = layers.Dense(         units=movie_embedding_dims,         activation="relu",         name="process_movie_embedding_with_genres",     )      ## Define a function to encode a given movie id.     def encode_movie(movie_id):         # Convert the string input values into integer indices.         movie_embedding = movie_embedding_encoder(movie_id)         encoded_movie = movie_embedding         if include_movie_features:             movie_genres_vector = movie_genres_lookup(movie_id)             encoded_movie = movie_embedding_processor(                 layers.concatenate([movie_embedding, movie_genres_vector])             )         return encoded_movie      ## Encoding target_movie_id     target_movie_id = inputs["target_movie_id"]     encoded_target_movie = encode_movie(target_movie_id)      ## Encoding sequence movie_ids.     sequence_movies_ids = inputs["sequence_movie_ids"]     encoded_sequence_movies = encode_movie(sequence_movies_ids)     # Create positional embedding.     position_embedding_encoder = layers.Embedding(         input_dim=sequence_length,         output_dim=movie_embedding_dims,         name="position_embedding",     )     positions = ops.arange(start=0, stop=sequence_length - 1, step=1)     encodded_positions = position_embedding_encoder(positions)     # Retrieve sequence ratings to incorporate them into the encoding of the movie.     sequence_ratings = inputs["sequence_ratings"]     sequence_ratings = ops.expand_dims(sequence_ratings, -1)     # Add the positional encoding to the movie encodings and multiply them by rating.     encoded_sequence_movies_with_poistion_and_rating = layers.Multiply()(         [(encoded_sequence_movies + encodded_positions), sequence_ratings]     )      # Construct the transformer inputs.     for i in range(sequence_length - 1):         feature = encoded_sequence_movies_with_poistion_and_rating[:, i, ...]         feature = ops.expand_dims(feature, 1)         encoded_transformer_features.append(feature)     encoded_transformer_features.append(encoded_target_movie)     encoded_transformer_features = layers.concatenate(         encoded_transformer_features, axis=1     )     return encoded_transformer_features, encoded_other_features`

* * *

Create model inputs
-------------------

Copied!

`def create_model_inputs():     return {         "user_id": keras.Input(name="user_id", shape=(1,), dtype="int32"),         "sequence_movie_ids": keras.Input(             name="sequence_movie_ids", shape=(sequence_length - 1,), dtype="int32"         ),         "target_movie_id": keras.Input(             name="target_movie_id", shape=(1,), dtype="int32"         ),         "sequence_ratings": keras.Input(             name="sequence_ratings", shape=(sequence_length - 1,), dtype="float32"         ),         "sex": keras.Input(name="sex", shape=(1,), dtype="int32"),         "age_group": keras.Input(name="age_group", shape=(1,), dtype="int32"),         "occupation": keras.Input(name="occupation", shape=(1,), dtype="int32"),     }`

* * *

Create a BST model
------------------

Copied!

`include_user_id = False include_user_features = False include_movie_features = False  hidden_units = [256, 128] dropout_rate = 0.1 num_heads = 3  def create_model():      inputs = create_model_inputs()     transformer_features, other_features = encode_input_features(         inputs, include_user_id, include_user_features, include_movie_features     )     # Create a multi-headed attention layer.     attention_output = layers.MultiHeadAttention(         num_heads=num_heads, key_dim=transformer_features.shape[2], dropout=dropout_rate     )(transformer_features, transformer_features)      # Transformer block.     attention_output = layers.Dropout(dropout_rate)(attention_output)     x1 = layers.Add()([transformer_features, attention_output])     x1 = layers.LayerNormalization()(x1)     x2 = layers.LeakyReLU()(x1)     x2 = layers.Dense(units=x2.shape[-1])(x2)     x2 = layers.Dropout(dropout_rate)(x2)     transformer_features = layers.Add()([x1, x2])     transformer_features = layers.LayerNormalization()(transformer_features)     features = layers.Flatten()(transformer_features)      # Included the other_features.     if other_features is not None:         features = layers.concatenate(             [features, layers.Reshape([other_features.shape[-1]])(other_features)]         )      # Fully-connected layers.     for num_units in hidden_units:         features = layers.Dense(num_units)(features)         features = layers.BatchNormalization()(features)         features = layers.LeakyReLU()(features)         features = layers.Dropout(dropout_rate)(features)     outputs = layers.Dense(units=1)(features)     model = keras.Model(inputs=inputs, outputs=outputs)     return model  model = create_model()`

`An NVIDIA GPU may be present on this machine, but a CUDA-enabled jaxlib is not installed. Falling back to cpu.`

* * *

Run training and evaluation experiment
--------------------------------------

Copied!

`# Compile the model. model.compile(     optimizer=keras.optimizers.Adagrad(learning_rate=0.01),     loss=keras.losses.MeanSquaredError(),     metrics=[keras.metrics.MeanAbsoluteError()], )  # Read the training data.  train_dataset = get_dataset_from_csv("train_data.csv", batch_size=265, shuffle=True)  # Fit the model with the training data. model.fit(train_dataset, epochs=2)  # Read the test data. test_dataset = get_dataset_from_csv("test_data.csv", batch_size=265)  # Evaluate the model on the test data. _, rmse = model.evaluate(test_dataset, verbose=0) print(f"Test MAE: {round(rmse, 3)}")`

`Epoch 1/2`

  `1/Unknown  7s 7s/step - loss: 12.6790 - mean_absolute_error: 3.2470     2/Unknown  7s 175ms/step - loss: 11.8442 - mean_absolute_error: 3.1216     3/Unknown  7s 169ms/step - loss: 11.2701 - mean_absolute_error: 3.0387     4/Unknown  7s 162ms/step - loss: 10.7890 - mean_absolute_error: 2.9640     5/Unknown  8s 160ms/step - loss: 10.3522 - mean_absolute_error: 2.8934     6/Unknown  8s 173ms/step - loss: 9.9734 - mean_absolute_error: 2.8301      7/Unknown  8s 181ms/step - loss: 9.6343 - mean_absolute_error: 2.7711     8/Unknown  8s 176ms/step - loss: 9.3284 - mean_absolute_error: 2.7167     9/Unknown  8s 174ms/step - loss: 9.0492 - mean_absolute_error: 2.6662    10/Unknown  8s 172ms/step - loss: 8.7926 - mean_absolute_error: 2.6188    11/Unknown  9s 171ms/step - loss: 8.5587 - mean_absolute_error: 2.5750    12/Unknown  9s 169ms/step - loss: 8.3417 - mean_absolute_error: 2.5337    13/Unknown  9s 169ms/step - loss: 8.1379 - mean_absolute_error: 2.4944    14/Unknown  9s 169ms/step - loss: 7.9466 - mean_absolute_error: 2.4568    15/Unknown  9s 168ms/step - loss: 7.7681 - mean_absolute_error: 2.4216    16/Unknown  9s 168ms/step - loss: 7.6015 - mean_absolute_error: 2.3885    17/Unknown  10s 168ms/step - loss: 7.4451 - mean_absolute_error: 2.3571    18/Unknown  10s 168ms/step - loss: 7.2978 - mean_absolute_error: 2.3273    19/Unknown  10s 167ms/step - loss: 7.1582 - mean_absolute_error: 2.2988    20/Unknown  10s 167ms/step - loss: 7.0262 - mean_absolute_error: 2.2716    21/Unknown  10s 167ms/step - loss: 6.9011 - mean_absolute_error: 2.2458    22/Unknown  10s 166ms/step - loss: 6.7823 - mean_absolute_error: 2.2211    23/Unknown  11s 166ms/step - loss: 6.6689 - mean_absolute_error: 2.1972    24/Unknown  11s 167ms/step - loss: 6.5609 - mean_absolute_error: 2.1744    25/Unknown  11s 166ms/step - loss: 6.4579 - mean_absolute_error: 2.1524    26/Unknown  11s 166ms/step - loss: 6.3597 - mean_absolute_error: 2.1315    27/Unknown  11s 166ms/step - loss: 6.2656 - mean_absolute_error: 2.1112    28/Unknown  11s 166ms/step - loss: 6.1754 - mean_absolute_error: 2.0917    29/Unknown  12s 166ms/step - loss: 6.0891 - mean_absolute_error: 2.0730    30/Unknown  12s 166ms/step - loss: 6.0059 - mean_absolute_error: 2.0548    31/Unknown  12s 166ms/step - loss: 5.9260 - mean_absolute_error: 2.0372    32/Unknown  12s 166ms/step - loss: 5.8491 - mean_absolute_error: 2.0203    33/Unknown  12s 167ms/step - loss: 5.7751 - mean_absolute_error: 2.0039    34/Unknown  12s 167ms/step - loss: 5.7038 - mean_absolute_error: 1.9880    35/Unknown  13s 167ms/step - loss: 5.6349 - mean_absolute_error: 1.9727    36/Unknown  13s 168ms/step - loss: 5.5687 - mean_absolute_error: 1.9579    37/Unknown  13s 168ms/step - loss: 5.5050 - mean_absolute_error: 1.9435    38/Unknown  13s 169ms/step - loss: 5.4435 - mean_absolute_error: 1.9297    39/Unknown  13s 170ms/step - loss: 5.3839 - mean_absolute_error: 1.9163    40/Unknown  13s 170ms/step - loss: 5.3267 - mean_absolute_error: 1.9033    41/Unknown  14s 170ms/step - loss: 5.2712 - mean_absolute_error: 1.8908    42/Unknown  14s 171ms/step - loss: 5.2175 - mean_absolute_error: 1.8786    43/Unknown  14s 171ms/step - loss: 5.1653 - mean_absolute_error: 1.8667    44/Unknown  14s 171ms/step - loss: 5.1147 - mean_absolute_error: 1.8551    45/Unknown  14s 170ms/step - loss: 5.0658 - mean_absolute_error: 1.8439    46/Unknown  15s 170ms/step - loss: 5.0183 - mean_absolute_error: 1.8330    47/Unknown  15s 171ms/step - loss: 4.9722 - mean_absolute_error: 1.8224    48/Unknown  15s 171ms/step - loss: 4.9275 - mean_absolute_error: 1.8121    49/Unknown  15s 171ms/step - loss: 4.8840 - mean_absolute_error: 1.8021    50/Unknown  15s 170ms/step - loss: 4.8417 - mean_absolute_error: 1.7923    51/Unknown  15s 170ms/step - loss: 4.8005 - mean_absolute_error: 1.7828    52/Unknown  16s 170ms/step - loss: 4.7605 - mean_absolute_error: 1.7735    53/Unknown  16s 170ms/step - loss: 4.7216 - mean_absolute_error: 1.7645    54/Unknown  16s 169ms/step - loss: 4.6837 - mean_absolute_error: 1.7557    55/Unknown  16s 169ms/step - loss: 4.6468 - mean_absolute_error: 1.7471    56/Unknown  16s 169ms/step - loss: 4.6108 - mean_absolute_error: 1.7387    57/Unknown  16s 169ms/step - loss: 4.5756 - mean_absolute_error: 1.7305    58/Unknown  16s 169ms/step - loss: 4.5413 - mean_absolute_error: 1.7224    59/Unknown  17s 169ms/step - loss: 4.5078 - mean_absolute_error: 1.7146    60/Unknown  17s 169ms/step - loss: 4.4751 - mean_absolute_error: 1.7069    61/Unknown  17s 169ms/step - loss: 4.4432 - mean_absolute_error: 1.6994    62/Unknown  17s 169ms/step - loss: 4.4120 - mean_absolute_error: 1.6921    63/Unknown  17s 169ms/step - loss: 4.3815 - mean_absolute_error: 1.6849    64/Unknown  18s 169ms/step - loss: 4.3517 - mean_absolute_error: 1.6778    65/Unknown  18s 169ms/step - loss: 4.3225 - mean_absolute_error: 1.6709    66/Unknown  18s 169ms/step - loss: 4.2940 - mean_absolute_error: 1.6642    67/Unknown  18s 169ms/step - loss: 4.2660 - mean_absolute_error: 1.6576    68/Unknown  18s 169ms/step - loss: 4.2387 - mean_absolute_error: 1.6511    69/Unknown  18s 169ms/step - loss: 4.2120 - mean_absolute_error: 1.6447    70/Unknown  19s 169ms/step - loss: 4.1859 - mean_absolute_error: 1.6385    71/Unknown  19s 169ms/step - loss: 4.1602 - mean_absolute_error: 1.6324    72/Unknown  19s 169ms/step - loss: 4.1352 - mean_absolute_error: 1.6265    73/Unknown  19s 169ms/step - loss: 4.1106 - mean_absolute_error: 1.6206    74/Unknown  19s 169ms/step - loss: 4.0865 - mean_absolute_error: 1.6149    75/Unknown  19s 169ms/step - loss: 4.0629 - mean_absolute_error: 1.6093    76/Unknown  20s 169ms/step - loss: 4.0398 - mean_absolute_error: 1.6038    77/Unknown  20s 169ms/step - loss: 4.0172 - mean_absolute_error: 1.5984    78/Unknown  20s 169ms/step - loss: 3.9950 - mean_absolute_error: 1.5931    79/Unknown  20s 169ms/step - loss: 3.9733 - mean_absolute_error: 1.5880    80/Unknown  20s 169ms/step - loss: 3.9519 - mean_absolute_error: 1.5829    81/Unknown  20s 170ms/step - loss: 3.9309 - mean_absolute_error: 1.5779    82/Unknown  21s 170ms/step - loss: 3.9104 - mean_absolute_error: 1.5730    83/Unknown  21s 170ms/step - loss: 3.8903 - mean_absolute_error: 1.5682    84/Unknown  21s 170ms/step - loss: 3.8705 - mean_absolute_error: 1.5634    85/Unknown  21s 170ms/step - loss: 3.8511 - mean_absolute_error: 1.5588    86/Unknown  21s 170ms/step - loss: 3.8320 - mean_absolute_error: 1.5543    87/Unknown  22s 170ms/step - loss: 3.8133 - mean_absolute_error: 1.5498    88/Unknown  22s 170ms/step - loss: 3.7949 - mean_absolute_error: 1.5454    89/Unknown  22s 170ms/step - loss: 3.7769 - mean_absolute_error: 1.5411    90/Unknown  22s 171ms/step - loss: 3.7592 - mean_absolute_error: 1.5369    91/Unknown  22s 171ms/step - loss: 3.7419 - mean_absolute_error: 1.5327    92/Unknown  22s 171ms/step - loss: 3.7248 - mean_absolute_error: 1.5286    93/Unknown  23s 172ms/step - loss: 3.7080 - mean_absolute_error: 1.5246    94/Unknown  23s 172ms/step - loss: 3.6914 - mean_absolute_error: 1.5206    95/Unknown  23s 172ms/step - loss: 3.6751 - mean_absolute_error: 1.5167    96/Unknown  23s 173ms/step - loss: 3.6591 - mean_absolute_error: 1.5129    97/Unknown  24s 174ms/step - loss: 3.6433 - mean_absolute_error: 1.5091    98/Unknown  24s 175ms/step - loss: 3.6278 - mean_absolute_error: 1.5053    99/Unknown  24s 175ms/step - loss: 3.6125 - mean_absolute_error: 1.5017   100/Unknown  24s 175ms/step - loss: 3.5975 - mean_absolute_error: 1.4980   101/Unknown  24s 175ms/step - loss: 3.5827 - mean_absolute_error: 1.4945   102/Unknown  25s 176ms/step - loss: 3.5682 - mean_absolute_error: 1.4910   103/Unknown  25s 176ms/step - loss: 3.5539 - mean_absolute_error: 1.4875   104/Unknown  25s 176ms/step - loss: 3.5397 - mean_absolute_error: 1.4841   105/Unknown  25s 176ms/step - loss: 3.5259 - mean_absolute_error: 1.4808   106/Unknown  26s 179ms/step - loss: 3.5122 - mean_absolute_error: 1.4775   107/Unknown  26s 179ms/step - loss: 3.4987 - mean_absolute_error: 1.4742   108/Unknown  26s 179ms/step - loss: 3.4854 - mean_absolute_error: 1.4710   109/Unknown  26s 179ms/step - loss: 3.4723 - mean_absolute_error: 1.4679   110/Unknown  26s 179ms/step - loss: 3.4594 - mean_absolute_error: 1.4648   111/Unknown  27s 179ms/step - loss: 3.4466 - mean_absolute_error: 1.4617   112/Unknown  27s 179ms/step - loss: 3.4341 - mean_absolute_error: 1.4587   113/Unknown  27s 179ms/step - loss: 3.4217 - mean_absolute_error: 1.4557   114/Unknown  27s 179ms/step - loss: 3.4095 - mean_absolute_error: 1.4527   115/Unknown  27s 178ms/step - loss: 3.3974 - mean_absolute_error: 1.4498   116/Unknown  27s 178ms/step - loss: 3.3856 - mean_absolute_error: 1.4470   117/Unknown  28s 178ms/step - loss: 3.3738 - mean_absolute_error: 1.4441   118/Unknown  28s 178ms/step - loss: 3.3623 - mean_absolute_error: 1.4413   119/Unknown  28s 178ms/step - loss: 3.3509 - mean_absolute_error: 1.4386   120/Unknown  28s 178ms/step - loss: 3.3396 - mean_absolute_error: 1.4358   121/Unknown  28s 178ms/step - loss: 3.3285 - mean_absolute_error: 1.4331   122/Unknown  28s 178ms/step - loss: 3.3175 - mean_absolute_error: 1.4305   123/Unknown  29s 178ms/step - loss: 3.3067 - mean_absolute_error: 1.4279   124/Unknown  29s 177ms/step - loss: 3.2960 - mean_absolute_error: 1.4253   125/Unknown  29s 177ms/step - loss: 3.2855 - mean_absolute_error: 1.4227   126/Unknown  29s 177ms/step - loss: 3.2751 - mean_absolute_error: 1.4202   127/Unknown  29s 177ms/step - loss: 3.2648 - mean_absolute_error: 1.4177   128/Unknown  29s 177ms/step - loss: 3.2546 - mean_absolute_error: 1.4152   129/Unknown  30s 177ms/step - loss: 3.2446 - mean_absolute_error: 1.4128   130/Unknown  30s 177ms/step - loss: 3.2347 - mean_absolute_error: 1.4104   131/Unknown  30s 177ms/step - loss: 3.2249 - mean_absolute_error: 1.4080   132/Unknown  30s 177ms/step - loss: 3.2152 - mean_absolute_error: 1.4056   133/Unknown  30s 177ms/step - loss: 3.2057 - mean_absolute_error: 1.4033   134/Unknown  30s 177ms/step - loss: 3.1962 - mean_absolute_error: 1.4010   135/Unknown  31s 177ms/step - loss: 3.1869 - mean_absolute_error: 1.3988   136/Unknown  31s 177ms/step - loss: 3.1777 - mean_absolute_error: 1.3965   137/Unknown  31s 177ms/step - loss: 3.1686 - mean_absolute_error: 1.3943   138/Unknown  31s 177ms/step - loss: 3.1596 - mean_absolute_error: 1.3921   139/Unknown  31s 177ms/step - loss: 3.1507 - mean_absolute_error: 1.3899   140/Unknown  32s 177ms/step - loss: 3.1419 - mean_absolute_error: 1.3878   141/Unknown  32s 177ms/step - loss: 3.1331 - mean_absolute_error: 1.3856   142/Unknown  32s 178ms/step - loss: 3.1245 - mean_absolute_error: 1.3835   143/Unknown  32s 178ms/step - loss: 3.1160 - mean_absolute_error: 1.3815   144/Unknown  32s 178ms/step - loss: 3.1076 - mean_absolute_error: 1.3794   145/Unknown  32s 178ms/step - loss: 3.0993 - mean_absolute_error: 1.3774   146/Unknown  33s 178ms/step - loss: 3.0910 - mean_absolute_error: 1.3754   147/Unknown  33s 178ms/step - loss: 3.0829 - mean_absolute_error: 1.3734   148/Unknown  33s 178ms/step - loss: 3.0748 - mean_absolute_error: 1.3714   149/Unknown  33s 178ms/step - loss: 3.0668 - mean_absolute_error: 1.3694   150/Unknown  33s 178ms/step - loss: 3.0589 - mean_absolute_error: 1.3675   151/Unknown  34s 178ms/step - loss: 3.0510 - mean_absolute_error: 1.3656   152/Unknown  34s 178ms/step - loss: 3.0433 - mean_absolute_error: 1.3637   153/Unknown  34s 178ms/step - loss: 3.0356 - mean_absolute_error: 1.3618   154/Unknown  34s 178ms/step - loss: 3.0280 - mean_absolute_error: 1.3599   155/Unknown  34s 178ms/step - loss: 3.0204 - mean_absolute_error: 1.3581   156/Unknown  34s 178ms/step - loss: 3.0130 - mean_absolute_error: 1.3562   157/Unknown  35s 178ms/step - loss: 3.0056 - mean_absolute_error: 1.3544   158/Unknown  35s 178ms/step - loss: 2.9982 - mean_absolute_error: 1.3526   159/Unknown  35s 178ms/step - loss: 2.9910 - mean_absolute_error: 1.3508   160/Unknown  35s 178ms/step - loss: 2.9838 - mean_absolute_error: 1.3491   161/Unknown  35s 178ms/step - loss: 2.9767 - mean_absolute_error: 1.3473   162/Unknown  35s 178ms/step - loss: 2.9696 - mean_absolute_error: 1.3456   163/Unknown  36s 178ms/step - loss: 2.9626 - mean_absolute_error: 1.3439   164/Unknown  36s 178ms/step - loss: 2.9557 - mean_absolute_error: 1.3422   165/Unknown  36s 178ms/step - loss: 2.9489 - mean_absolute_error: 1.3405   166/Unknown  36s 178ms/step - loss: 2.9421 - mean_absolute_error: 1.3388   167/Unknown  36s 178ms/step - loss: 2.9353 - mean_absolute_error: 1.3371   168/Unknown  37s 178ms/step - loss: 2.9287 - mean_absolute_error: 1.3355   169/Unknown  37s 178ms/step - loss: 2.9221 - mean_absolute_error: 1.3339   170/Unknown  37s 178ms/step - loss: 2.9155 - mean_absolute_error: 1.3323   171/Unknown  37s 178ms/step - loss: 2.9091 - mean_absolute_error: 1.3307   172/Unknown  37s 178ms/step - loss: 2.9026 - mean_absolute_error: 1.3291   173/Unknown  37s 178ms/step - loss: 2.8963 - mean_absolute_error: 1.3275   174/Unknown  38s 178ms/step - loss: 2.8900 - mean_absolute_error: 1.3259   175/Unknown  38s 178ms/step - loss: 2.8837 - mean_absolute_error: 1.3244   176/Unknown  38s 178ms/step - loss: 2.8775 - mean_absolute_error: 1.3228   177/Unknown  38s 178ms/step - loss: 2.8714 - mean_absolute_error: 1.3213   178/Unknown  38s 178ms/step - loss: 2.8653 - mean_absolute_error: 1.3198   179/Unknown  39s 178ms/step - loss: 2.8592 - mean_absolute_error: 1.3183   180/Unknown  39s 178ms/step - loss: 2.8533 - mean_absolute_error: 1.3168   181/Unknown  39s 178ms/step - loss: 2.8473 - mean_absolute_error: 1.3154   182/Unknown  39s 178ms/step - loss: 2.8414 - mean_absolute_error: 1.3139   183/Unknown  39s 178ms/step - loss: 2.8356 - mean_absolute_error: 1.3125   184/Unknown  39s 178ms/step - loss: 2.8298 - mean_absolute_error: 1.3110   185/Unknown  40s 178ms/step - loss: 2.8241 - mean_absolute_error: 1.3096   186/Unknown  40s 178ms/step - loss: 2.8184 - mean_absolute_error: 1.3082   187/Unknown  40s 178ms/step - loss: 2.8128 - mean_absolute_error: 1.3068   188/Unknown  40s 178ms/step - loss: 2.8072 - mean_absolute_error: 1.3054   189/Unknown  40s 178ms/step - loss: 2.8017 - mean_absolute_error: 1.3040   190/Unknown  40s 178ms/step - loss: 2.7962 - mean_absolute_error: 1.3027   191/Unknown  41s 178ms/step - loss: 2.7907 - mean_absolute_error: 1.3013   192/Unknown  41s 178ms/step - loss: 2.7853 - mean_absolute_error: 1.3000   193/Unknown  41s 178ms/step - loss: 2.7800 - mean_absolute_error: 1.2986   194/Unknown  41s 178ms/step - loss: 2.7746 - mean_absolute_error: 1.2973   195/Unknown  41s 178ms/step - loss: 2.7694 - mean_absolute_error: 1.2960   196/Unknown  42s 178ms/step - loss: 2.7641 - mean_absolute_error: 1.2947   197/Unknown  42s 178ms/step - loss: 2.7590 - mean_absolute_error: 1.2934   198/Unknown  42s 178ms/step - loss: 2.7538 - mean_absolute_error: 1.2921   199/Unknown  42s 178ms/step - loss: 2.7487 - mean_absolute_error: 1.2909   200/Unknown  42s 178ms/step - loss: 2.7436 - mean_absolute_error: 1.2896   201/Unknown  42s 178ms/step - loss: 2.7386 - mean_absolute_error: 1.2884   202/Unknown  43s 178ms/step - loss: 2.7336 - mean_absolute_error: 1.2871   203/Unknown  43s 178ms/step - loss: 2.7287 - mean_absolute_error: 1.2859   204/Unknown  43s 178ms/step - loss: 2.7238 - mean_absolute_error: 1.2846   205/Unknown  43s 178ms/step - loss: 2.7189 - mean_absolute_error: 1.2834   206/Unknown  43s 178ms/step - loss: 2.7140 - mean_absolute_error: 1.2822   207/Unknown  44s 178ms/step - loss: 2.7092 - mean_absolute_error: 1.2810   208/Unknown  44s 178ms/step - loss: 2.7045 - mean_absolute_error: 1.2798   209/Unknown  44s 178ms/step - loss: 2.6997 - mean_absolute_error: 1.2786   210/Unknown  44s 178ms/step - loss: 2.6950 - mean_absolute_error: 1.2775   211/Unknown  44s 178ms/step - loss: 2.6904 - mean_absolute_error: 1.2763   212/Unknown  44s 178ms/step - loss: 2.6857 - mean_absolute_error: 1.2751   213/Unknown  45s 178ms/step - loss: 2.6812 - mean_absolute_error: 1.2740   214/Unknown  45s 178ms/step - loss: 2.6766 - mean_absolute_error: 1.2729   215/Unknown  45s 178ms/step - loss: 2.6721 - mean_absolute_error: 1.2717   216/Unknown  45s 178ms/step - loss: 2.6676 - mean_absolute_error: 1.2706   217/Unknown  45s 178ms/step - loss: 2.6631 - mean_absolute_error: 1.2695   218/Unknown  45s 178ms/step - loss: 2.6587 - mean_absolute_error: 1.2684   219/Unknown  46s 178ms/step - loss: 2.6543 - mean_absolute_error: 1.2673   220/Unknown  46s 177ms/step - loss: 2.6499 - mean_absolute_error: 1.2662   221/Unknown  46s 177ms/step - loss: 2.6456 - mean_absolute_error: 1.2651   222/Unknown  46s 177ms/step - loss: 2.6413 - mean_absolute_error: 1.2640   223/Unknown  46s 177ms/step - loss: 2.6370 - mean_absolute_error: 1.2629   224/Unknown  46s 177ms/step - loss: 2.6328 - mean_absolute_error: 1.2619   225/Unknown  47s 177ms/step - loss: 2.6286 - mean_absolute_error: 1.2608   226/Unknown  47s 177ms/step - loss: 2.6244 - mean_absolute_error: 1.2598   227/Unknown  47s 177ms/step - loss: 2.6202 - mean_absolute_error: 1.2587   228/Unknown  47s 177ms/step - loss: 2.6161 - mean_absolute_error: 1.2577   229/Unknown  47s 177ms/step - loss: 2.6120 - mean_absolute_error: 1.2567   230/Unknown  47s 177ms/step - loss: 2.6079 - mean_absolute_error: 1.2556   231/Unknown  48s 177ms/step - loss: 2.6039 - mean_absolute_error: 1.2546   232/Unknown  48s 177ms/step - loss: 2.5999 - mean_absolute_error: 1.2536   233/Unknown  48s 177ms/step - loss: 2.5959 - mean_absolute_error: 1.2526   234/Unknown  48s 177ms/step - loss: 2.5920 - mean_absolute_error: 1.2516   235/Unknown  48s 177ms/step - loss: 2.5880 - mean_absolute_error: 1.2506   236/Unknown  48s 177ms/step - loss: 2.5841 - mean_absolute_error: 1.2496   237/Unknown  49s 177ms/step - loss: 2.5803 - mean_absolute_error: 1.2487   238/Unknown  49s 177ms/step - loss: 2.5764 - mean_absolute_error: 1.2477   239/Unknown  49s 177ms/step - loss: 2.5726 - mean_absolute_error: 1.2467   240/Unknown  49s 177ms/step - loss: 2.5688 - mean_absolute_error: 1.2458   241/Unknown  49s 177ms/step - loss: 2.5650 - mean_absolute_error: 1.2448   242/Unknown  49s 177ms/step - loss: 2.5613 - mean_absolute_error: 1.2439   243/Unknown  50s 177ms/step - loss: 2.5576 - mean_absolute_error: 1.2429   244/Unknown  50s 177ms/step - loss: 2.5539 - mean_absolute_error: 1.2420   245/Unknown  50s 177ms/step - loss: 2.5502 - mean_absolute_error: 1.2411   246/Unknown  50s 177ms/step - loss: 2.5465 - mean_absolute_error: 1.2402   247/Unknown  50s 177ms/step - loss: 2.5429 - mean_absolute_error: 1.2393   248/Unknown  51s 177ms/step - loss: 2.5393 - mean_absolute_error: 1.2383   249/Unknown  51s 177ms/step - loss: 2.5357 - mean_absolute_error: 1.2374   250/Unknown  51s 177ms/step - loss: 2.5322 - mean_absolute_error: 1.2365   251/Unknown  51s 177ms/step - loss: 2.5286 - mean_absolute_error: 1.2356   252/Unknown  51s 177ms/step - loss: 2.5251 - mean_absolute_error: 1.2347   253/Unknown  52s 178ms/step - loss: 2.5216 - mean_absolute_error: 1.2339   254/Unknown  52s 178ms/step - loss: 2.5181 - mean_absolute_error: 1.2330   255/Unknown  52s 178ms/step - loss: 2.5146 - mean_absolute_error: 1.2321   256/Unknown  52s 178ms/step - loss: 2.5112 - mean_absolute_error: 1.2312   257/Unknown  52s 178ms/step - loss: 2.5078 - mean_absolute_error: 1.2304   258/Unknown  53s 178ms/step - loss: 2.5044 - mean_absolute_error: 1.2295   259/Unknown  53s 178ms/step - loss: 2.5010 - mean_absolute_error: 1.2286   260/Unknown  53s 178ms/step - loss: 2.4976 - mean_absolute_error: 1.2278   261/Unknown  53s 179ms/step - loss: 2.4943 - mean_absolute_error: 1.2269   262/Unknown  53s 179ms/step - loss: 2.4910 - mean_absolute_error: 1.2261   263/Unknown  54s 179ms/step - loss: 2.4877 - mean_absolute_error: 1.2253   264/Unknown  54s 179ms/step - loss: 2.4844 - mean_absolute_error: 1.2244   265/Unknown  54s 179ms/step - loss: 2.4812 - mean_absolute_error: 1.2236   266/Unknown  54s 179ms/step - loss: 2.4779 - mean_absolute_error: 1.2228   267/Unknown  54s 179ms/step - loss: 2.4747 - mean_absolute_error: 1.2220   268/Unknown  55s 179ms/step - loss: 2.4715 - mean_absolute_error: 1.2211   269/Unknown  55s 179ms/step - loss: 2.4683 - mean_absolute_error: 1.2203   270/Unknown  55s 179ms/step - loss: 2.4652 - mean_absolute_error: 1.2195   271/Unknown  55s 179ms/step - loss: 2.4620 - mean_absolute_error: 1.2187   272/Unknown  55s 179ms/step - loss: 2.4589 - mean_absolute_error: 1.2179   273/Unknown  56s 179ms/step - loss: 2.4558 - mean_absolute_error: 1.2172   274/Unknown  56s 179ms/step - loss: 2.4527 - mean_absolute_error: 1.2164   275/Unknown  56s 179ms/step - loss: 2.4496 - mean_absolute_error: 1.2156   276/Unknown  56s 179ms/step - loss: 2.4465 - mean_absolute_error: 1.2148   277/Unknown  56s 179ms/step - loss: 2.4435 - mean_absolute_error: 1.2140   278/Unknown  57s 179ms/step - loss: 2.4405 - mean_absolute_error: 1.2133   279/Unknown  57s 179ms/step - loss: 2.4375 - mean_absolute_error: 1.2125   280/Unknown  57s 179ms/step - loss: 2.4345 - mean_absolute_error: 1.2117   281/Unknown  57s 179ms/step - loss: 2.4315 - mean_absolute_error: 1.2110   282/Unknown  57s 179ms/step - loss: 2.4286 - mean_absolute_error: 1.2102   283/Unknown  57s 179ms/step - loss: 2.4256 - mean_absolute_error: 1.2095   284/Unknown  58s 179ms/step - loss: 2.4227 - mean_absolute_error: 1.2087   285/Unknown  58s 179ms/step - loss: 2.4198 - mean_absolute_error: 1.2080   286/Unknown  58s 179ms/step - loss: 2.4169 - mean_absolute_error: 1.2072   287/Unknown  58s 179ms/step - loss: 2.4140 - mean_absolute_error: 1.2065   288/Unknown  58s 179ms/step - loss: 2.4111 - mean_absolute_error: 1.2058   289/Unknown  59s 179ms/step - loss: 2.4083 - mean_absolute_error: 1.2050   290/Unknown  59s 179ms/step - loss: 2.4054 - mean_absolute_error: 1.2043   291/Unknown  59s 179ms/step - loss: 2.4026 - mean_absolute_error: 1.2036   292/Unknown  59s 179ms/step - loss: 2.3998 - mean_absolute_error: 1.2029   293/Unknown  59s 179ms/step - loss: 2.3970 - mean_absolute_error: 1.2021   294/Unknown  59s 179ms/step - loss: 2.3943 - mean_absolute_error: 1.2014   295/Unknown  60s 179ms/step - loss: 2.3915 - mean_absolute_error: 1.2007   296/Unknown  60s 179ms/step - loss: 2.3887 - mean_absolute_error: 1.2000   297/Unknown  60s 179ms/step - loss: 2.3860 - mean_absolute_error: 1.1993   298/Unknown  60s 179ms/step - loss: 2.3833 - mean_absolute_error: 1.1986   299/Unknown  60s 179ms/step - loss: 2.3806 - mean_absolute_error: 1.1979   300/Unknown  61s 179ms/step - loss: 2.3779 - mean_absolute_error: 1.1972   301/Unknown  61s 179ms/step - loss: 2.3752 - mean_absolute_error: 1.1966   302/Unknown  61s 179ms/step - loss: 2.3726 - mean_absolute_error: 1.1959   303/Unknown  61s 179ms/step - loss: 2.3699 - mean_absolute_error: 1.1952   304/Unknown  61s 180ms/step - loss: 2.3673 - mean_absolute_error: 1.1945   305/Unknown  61s 180ms/step - loss: 2.3647 - mean_absolute_error: 1.1938   306/Unknown  62s 180ms/step - loss: 2.3621 - mean_absolute_error: 1.1932   307/Unknown  62s 180ms/step - loss: 2.3595 - mean_absolute_error: 1.1925   308/Unknown  62s 180ms/step - loss: 2.3569 - mean_absolute_error: 1.1918   309/Unknown  62s 180ms/step - loss: 2.3543 - mean_absolute_error: 1.1912   310/Unknown  62s 180ms/step - loss: 2.3518 - mean_absolute_error: 1.1905   311/Unknown  63s 180ms/step - loss: 2.3492 - mean_absolute_error: 1.1899   312/Unknown  63s 180ms/step - loss: 2.3467 - mean_absolute_error: 1.1892   313/Unknown  63s 180ms/step - loss: 2.3442 - mean_absolute_error: 1.1886   314/Unknown  63s 180ms/step - loss: 2.3417 - mean_absolute_error: 1.1879   315/Unknown  63s 180ms/step - loss: 2.3392 - mean_absolute_error: 1.1873   316/Unknown  64s 180ms/step - loss: 2.3367 - mean_absolute_error: 1.1867   317/Unknown  64s 180ms/step - loss: 2.3343 - mean_absolute_error: 1.1860   318/Unknown  64s 180ms/step - loss: 2.3318 - mean_absolute_error: 1.1854   319/Unknown  64s 180ms/step - loss: 2.3294 - mean_absolute_error: 1.1848   320/Unknown  64s 180ms/step - loss: 2.3270 - mean_absolute_error: 1.1841   321/Unknown  65s 180ms/step - loss: 2.3245 - mean_absolute_error: 1.1835   322/Unknown  65s 180ms/step - loss: 2.3221 - mean_absolute_error: 1.1829   323/Unknown  65s 180ms/step - loss: 2.3197 - mean_absolute_error: 1.1823   324/Unknown  65s 180ms/step - loss: 2.3174 - mean_absolute_error: 1.1817   325/Unknown  65s 180ms/step - loss: 2.3150 - mean_absolute_error: 1.1811   326/Unknown  66s 180ms/step - loss: 2.3127 - mean_absolute_error: 1.1805   327/Unknown  66s 180ms/step - loss: 2.3103 - mean_absolute_error: 1.1799   328/Unknown  66s 180ms/step - loss: 2.3080 - mean_absolute_error: 1.1793   329/Unknown  66s 181ms/step - loss: 2.3057 - mean_absolute_error: 1.1787   330/Unknown  66s 181ms/step - loss: 2.3034 - mean_absolute_error: 1.1781   331/Unknown  66s 181ms/step - loss: 2.3011 - mean_absolute_error: 1.1775   332/Unknown  67s 181ms/step - loss: 2.2988 - mean_absolute_error: 1.1769   333/Unknown  67s 181ms/step - loss: 2.2965 - mean_absolute_error: 1.1763   334/Unknown  67s 181ms/step - loss: 2.2943 - mean_absolute_error: 1.1757   335/Unknown  67s 181ms/step - loss: 2.2920 - mean_absolute_error: 1.1751   336/Unknown  67s 181ms/step - loss: 2.2898 - mean_absolute_error: 1.1745   337/Unknown  68s 181ms/step - loss: 2.2875 - mean_absolute_error: 1.1740   338/Unknown  68s 181ms/step - loss: 2.2853 - mean_absolute_error: 1.1734   339/Unknown  68s 181ms/step - loss: 2.2831 - mean_absolute_error: 1.1728   340/Unknown  68s 181ms/step - loss: 2.2809 - mean_absolute_error: 1.1723   341/Unknown  68s 181ms/step - loss: 2.2787 - mean_absolute_error: 1.1717   342/Unknown  69s 181ms/step - loss: 2.2765 - mean_absolute_error: 1.1711   343/Unknown  69s 181ms/step - loss: 2.2744 - mean_absolute_error: 1.1706   344/Unknown  69s 181ms/step - loss: 2.2722 - mean_absolute_error: 1.1700   345/Unknown  69s 181ms/step - loss: 2.2701 - mean_absolute_error: 1.1695   346/Unknown  69s 181ms/step - loss: 2.2679 - mean_absolute_error: 1.1689   347/Unknown  70s 181ms/step - loss: 2.2658 - mean_absolute_error: 1.1684   348/Unknown  70s 181ms/step - loss: 2.2637 - mean_absolute_error: 1.1678   349/Unknown  70s 181ms/step - loss: 2.2616 - mean_absolute_error: 1.1673   350/Unknown  70s 181ms/step - loss: 2.2595 - mean_absolute_error: 1.1667   351/Unknown  70s 181ms/step - loss: 2.2574 - mean_absolute_error: 1.1662   352/Unknown  71s 181ms/step - loss: 2.2553 - mean_absolute_error: 1.1657   353/Unknown  71s 181ms/step - loss: 2.2533 - mean_absolute_error: 1.1651   354/Unknown  71s 181ms/step - loss: 2.2512 - mean_absolute_error: 1.1646   355/Unknown  71s 181ms/step - loss: 2.2492 - mean_absolute_error: 1.1641   356/Unknown  71s 181ms/step - loss: 2.2471 - mean_absolute_error: 1.1635   357/Unknown  71s 181ms/step - loss: 2.2451 - mean_absolute_error: 1.1630   358/Unknown  72s 182ms/step - loss: 2.2431 - mean_absolute_error: 1.1625   359/Unknown  72s 182ms/step - loss: 2.2411 - mean_absolute_error: 1.1620   360/Unknown  72s 182ms/step - loss: 2.2391 - mean_absolute_error: 1.1614   361/Unknown  72s 182ms/step - loss: 2.2371 - mean_absolute_error: 1.1609   362/Unknown  72s 182ms/step - loss: 2.2351 - mean_absolute_error: 1.1604   363/Unknown  73s 182ms/step - loss: 2.2331 - mean_absolute_error: 1.1599   364/Unknown  73s 182ms/step - loss: 2.2311 - mean_absolute_error: 1.1594   365/Unknown  73s 182ms/step - loss: 2.2292 - mean_absolute_error: 1.1589   366/Unknown  73s 182ms/step - loss: 2.2272 - mean_absolute_error: 1.1584   367/Unknown  74s 182ms/step - loss: 2.2253 - mean_absolute_error: 1.1579   368/Unknown  74s 182ms/step - loss: 2.2234 - mean_absolute_error: 1.1574   369/Unknown  74s 182ms/step - loss: 2.2214 - mean_absolute_error: 1.1569   370/Unknown  74s 183ms/step - loss: 2.2195 - mean_absolute_error: 1.1564   371/Unknown  74s 183ms/step - loss: 2.2176 - mean_absolute_error: 1.1559   372/Unknown  75s 183ms/step - loss: 2.2157 - mean_absolute_error: 1.1554   373/Unknown  75s 183ms/step - loss: 2.2138 - mean_absolute_error: 1.1549   374/Unknown  75s 183ms/step - loss: 2.2119 - mean_absolute_error: 1.1544   375/Unknown  75s 183ms/step - loss: 2.2101 - mean_absolute_error: 1.1539   376/Unknown  75s 183ms/step - loss: 2.2082 - mean_absolute_error: 1.1535   377/Unknown  76s 183ms/step - loss: 2.2064 - mean_absolute_error: 1.1530   378/Unknown  76s 183ms/step - loss: 2.2045 - mean_absolute_error: 1.1525   379/Unknown  76s 183ms/step - loss: 2.2027 - mean_absolute_error: 1.1520   380/Unknown  76s 183ms/step - loss: 2.2008 - mean_absolute_error: 1.1515   381/Unknown  76s 183ms/step - loss: 2.1990 - mean_absolute_error: 1.1511   382/Unknown  77s 183ms/step - loss: 2.1972 - mean_absolute_error: 1.1506   383/Unknown  77s 183ms/step - loss: 2.1954 - mean_absolute_error: 1.1501   384/Unknown  77s 183ms/step - loss: 2.1936 - mean_absolute_error: 1.1497   385/Unknown  77s 183ms/step - loss: 2.1918 - mean_absolute_error: 1.1492   386/Unknown  77s 183ms/step - loss: 2.1900 - mean_absolute_error: 1.1487   387/Unknown  78s 183ms/step - loss: 2.1882 - mean_absolute_error: 1.1483   388/Unknown  78s 183ms/step - loss: 2.1865 - mean_absolute_error: 1.1478   389/Unknown  78s 183ms/step - loss: 2.1847 - mean_absolute_error: 1.1474   390/Unknown  78s 183ms/step - loss: 2.1829 - mean_absolute_error: 1.1469   391/Unknown  78s 183ms/step - loss: 2.1812 - mean_absolute_error: 1.1464   392/Unknown  79s 183ms/step - loss: 2.1794 - mean_absolute_error: 1.1460   393/Unknown  79s 183ms/step - loss: 2.1777 - mean_absolute_error: 1.1455   394/Unknown  79s 183ms/step - loss: 2.1760 - mean_absolute_error: 1.1451   395/Unknown  79s 183ms/step - loss: 2.1743 - mean_absolute_error: 1.1446   396/Unknown  79s 183ms/step - loss: 2.1725 - mean_absolute_error: 1.1442   397/Unknown  79s 183ms/step - loss: 2.1708 - mean_absolute_error: 1.1438   398/Unknown  80s 183ms/step - loss: 2.1691 - mean_absolute_error: 1.1433   399/Unknown  80s 183ms/step - loss: 2.1674 - mean_absolute_error: 1.1429   400/Unknown  80s 183ms/step - loss: 2.1657 - mean_absolute_error: 1.1424   401/Unknown  80s 184ms/step - loss: 2.1641 - mean_absolute_error: 1.1420   402/Unknown  80s 184ms/step - loss: 2.1624 - mean_absolute_error: 1.1416   403/Unknown  81s 184ms/step - loss: 2.1607 - mean_absolute_error: 1.1411   404/Unknown  81s 184ms/step - loss: 2.1590 - mean_absolute_error: 1.1407   405/Unknown  81s 184ms/step - loss: 2.1574 - mean_absolute_error: 1.1403   406/Unknown  81s 184ms/step - loss: 2.1557 - mean_absolute_error: 1.1398   407/Unknown  81s 184ms/step - loss: 2.1541 - mean_absolute_error: 1.1394   408/Unknown  82s 184ms/step - loss: 2.1525 - mean_absolute_error: 1.1390   409/Unknown  82s 184ms/step - loss: 2.1508 - mean_absolute_error: 1.1385   410/Unknown  82s 184ms/step - loss: 2.1492 - mean_absolute_error: 1.1381   411/Unknown  82s 184ms/step - loss: 2.1476 - mean_absolute_error: 1.1377   412/Unknown  82s 184ms/step - loss: 2.1460 - mean_absolute_error: 1.1373   413/Unknown  83s 184ms/step - loss: 2.1444 - mean_absolute_error: 1.1369   414/Unknown  83s 184ms/step - loss: 2.1428 - mean_absolute_error: 1.1364   415/Unknown  83s 184ms/step - loss: 2.1412 - mean_absolute_error: 1.1360   416/Unknown  83s 184ms/step - loss: 2.1396 - mean_absolute_error: 1.1356   417/Unknown  83s 184ms/step - loss: 2.1380 - mean_absolute_error: 1.1352   418/Unknown  84s 184ms/step - loss: 2.1364 - mean_absolute_error: 1.1348   419/Unknown  84s 184ms/step - loss: 2.1349 - mean_absolute_error: 1.1344   420/Unknown  84s 184ms/step - loss: 2.1333 - mean_absolute_error: 1.1340   421/Unknown  84s 184ms/step - loss: 2.1317 - mean_absolute_error: 1.1336   422/Unknown  84s 184ms/step - loss: 2.1302 - mean_absolute_error: 1.1332   423/Unknown  85s 184ms/step - loss: 2.1286 - mean_absolute_error: 1.1328   424/Unknown  85s 184ms/step - loss: 2.1271 - mean_absolute_error: 1.1324   425/Unknown  85s 184ms/step - loss: 2.1256 - mean_absolute_error: 1.1320   426/Unknown  85s 184ms/step - loss: 2.1240 - mean_absolute_error: 1.1316   427/Unknown  85s 184ms/step - loss: 2.1225 - mean_absolute_error: 1.1312   428/Unknown  86s 184ms/step - loss: 2.1210 - mean_absolute_error: 1.1308   429/Unknown  86s 184ms/step - loss: 2.1195 - mean_absolute_error: 1.1304   430/Unknown  86s 184ms/step - loss: 2.1180 - mean_absolute_error: 1.1300   431/Unknown  86s 184ms/step - loss: 2.1165 - mean_absolute_error: 1.1296   432/Unknown  86s 185ms/step - loss: 2.1150 - mean_absolute_error: 1.1292   433/Unknown  87s 185ms/step - loss: 2.1135 - mean_absolute_error: 1.1288   434/Unknown  87s 185ms/step - loss: 2.1120 - mean_absolute_error: 1.1284   435/Unknown  87s 185ms/step - loss: 2.1105 - mean_absolute_error: 1.1280   436/Unknown  87s 185ms/step - loss: 2.1090 - mean_absolute_error: 1.1276   437/Unknown  87s 185ms/step - loss: 2.1076 - mean_absolute_error: 1.1272   438/Unknown  88s 185ms/step - loss: 2.1061 - mean_absolute_error: 1.1269   439/Unknown  88s 185ms/step - loss: 2.1046 - mean_absolute_error: 1.1265   440/Unknown  88s 185ms/step - loss: 2.1032 - mean_absolute_error: 1.1261   441/Unknown  89s 186ms/step - loss: 2.1017 - mean_absolute_error: 1.1257   442/Unknown  89s 186ms/step - loss: 2.1003 - mean_absolute_error: 1.1253   443/Unknown  89s 186ms/step - loss: 2.0988 - mean_absolute_error: 1.1250   444/Unknown  89s 186ms/step - loss: 2.0974 - mean_absolute_error: 1.1246   445/Unknown  89s 186ms/step - loss: 2.0960 - mean_absolute_error: 1.1242   446/Unknown  90s 186ms/step - loss: 2.0945 - mean_absolute_error: 1.1238   447/Unknown  90s 186ms/step - loss: 2.0931 - mean_absolute_error: 1.1235   448/Unknown  90s 186ms/step - loss: 2.0917 - mean_absolute_error: 1.1231   449/Unknown  90s 186ms/step - loss: 2.0903 - mean_absolute_error: 1.1227   450/Unknown  90s 186ms/step - loss: 2.0889 - mean_absolute_error: 1.1223   451/Unknown  91s 186ms/step - loss: 2.0875 - mean_absolute_error: 1.1220   452/Unknown  91s 186ms/step - loss: 2.0861 - mean_absolute_error: 1.1216   453/Unknown  91s 186ms/step - loss: 2.0847 - mean_absolute_error: 1.1212   454/Unknown  91s 186ms/step - loss: 2.0833 - mean_absolute_error: 1.1209   455/Unknown  91s 186ms/step - loss: 2.0820 - mean_absolute_error: 1.1205   456/Unknown  92s 186ms/step - loss: 2.0806 - mean_absolute_error: 1.1202   457/Unknown  92s 186ms/step - loss: 2.0792 - mean_absolute_error: 1.1198   458/Unknown  92s 186ms/step - loss: 2.0778 - mean_absolute_error: 1.1194   459/Unknown  92s 186ms/step - loss: 2.0765 - mean_absolute_error: 1.1191   460/Unknown  92s 186ms/step - loss: 2.0751 - mean_absolute_error: 1.1187   461/Unknown  93s 186ms/step - loss: 2.0738 - mean_absolute_error: 1.1184   462/Unknown  93s 186ms/step - loss: 2.0724 - mean_absolute_error: 1.1180   463/Unknown  93s 187ms/step - loss: 2.0711 - mean_absolute_error: 1.1177   464/Unknown  93s 187ms/step - loss: 2.0697 - mean_absolute_error: 1.1173   465/Unknown  94s 187ms/step - loss: 2.0684 - mean_absolute_error: 1.1169   466/Unknown  94s 187ms/step - loss: 2.0671 - mean_absolute_error: 1.1166   467/Unknown  94s 187ms/step - loss: 2.0658 - mean_absolute_error: 1.1163   468/Unknown  94s 187ms/step - loss: 2.0644 - mean_absolute_error: 1.1159   469/Unknown  94s 187ms/step - loss: 2.0631 - mean_absolute_error: 1.1156   470/Unknown  95s 187ms/step - loss: 2.0618 - mean_absolute_error: 1.1152   471/Unknown  95s 187ms/step - loss: 2.0605 - mean_absolute_error: 1.1149   472/Unknown  95s 187ms/step - loss: 2.0592 - mean_absolute_error: 1.1145   473/Unknown  95s 187ms/step - loss: 2.0579 - mean_absolute_error: 1.1142   474/Unknown  96s 188ms/step - loss: 2.0566 - mean_absolute_error: 1.1138   475/Unknown  96s 188ms/step - loss: 2.0554 - mean_absolute_error: 1.1135   476/Unknown  96s 188ms/step - loss: 2.0541 - mean_absolute_error: 1.1132   477/Unknown  96s 188ms/step - loss: 2.0528 - mean_absolute_error: 1.1128   478/Unknown  96s 188ms/step - loss: 2.0515 - mean_absolute_error: 1.1125   479/Unknown  97s 188ms/step - loss: 2.0502 - mean_absolute_error: 1.1122   480/Unknown  97s 188ms/step - loss: 2.0490 - mean_absolute_error: 1.1118   481/Unknown  97s 188ms/step - loss: 2.0477 - mean_absolute_error: 1.1115   482/Unknown  97s 188ms/step - loss: 2.0465 - mean_absolute_error: 1.1112   483/Unknown  97s 188ms/step - loss: 2.0452 - mean_absolute_error: 1.1108   484/Unknown  98s 188ms/step - loss: 2.0440 - mean_absolute_error: 1.1105   485/Unknown  98s 188ms/step - loss: 2.0427 - mean_absolute_error: 1.1102   486/Unknown  98s 188ms/step - loss: 2.0415 - mean_absolute_error: 1.1098   487/Unknown  98s 188ms/step - loss: 2.0402 - mean_absolute_error: 1.1095   488/Unknown  99s 188ms/step - loss: 2.0390 - mean_absolute_error: 1.1092   489/Unknown  99s 188ms/step - loss: 2.0378 - mean_absolute_error: 1.1089   490/Unknown  99s 188ms/step - loss: 2.0365 - mean_absolute_error: 1.1085   491/Unknown  99s 188ms/step - loss: 2.0353 - mean_absolute_error: 1.1082   492/Unknown  99s 188ms/step - loss: 2.0341 - mean_absolute_error: 1.1079   493/Unknown  100s 188ms/step - loss: 2.0329 - mean_absolute_error: 1.1076   494/Unknown  100s 188ms/step - loss: 2.0317 - mean_absolute_error: 1.1073   495/Unknown  100s 188ms/step - loss: 2.0305 - mean_absolute_error: 1.1069   496/Unknown  100s 188ms/step - loss: 2.0293 - mean_absolute_error: 1.1066   497/Unknown  100s 188ms/step - loss: 2.0281 - mean_absolute_error: 1.1063   498/Unknown  101s 189ms/step - loss: 2.0269 - mean_absolute_error: 1.1060   499/Unknown  101s 189ms/step - loss: 2.0257 - mean_absolute_error: 1.1057   500/Unknown  101s 189ms/step - loss: 2.0245 - mean_absolute_error: 1.1054   501/Unknown  101s 189ms/step - loss: 2.0233 - mean_absolute_error: 1.1051   502/Unknown  101s 189ms/step - loss: 2.0222 - mean_absolute_error: 1.1047   503/Unknown  102s 189ms/step - loss: 2.0210 - mean_absolute_error: 1.1044   504/Unknown  102s 189ms/step - loss: 2.0198 - mean_absolute_error: 1.1041   505/Unknown  102s 189ms/step - loss: 2.0187 - mean_absolute_error: 1.1038   506/Unknown  102s 189ms/step - loss: 2.0175 - mean_absolute_error: 1.1035   507/Unknown  102s 189ms/step - loss: 2.0163 - mean_absolute_error: 1.1032   508/Unknown  103s 189ms/step - loss: 2.0152 - mean_absolute_error: 1.1029   509/Unknown  103s 189ms/step - loss: 2.0140 - mean_absolute_error: 1.1026   510/Unknown  103s 189ms/step - loss: 2.0129 - mean_absolute_error: 1.1023   511/Unknown  103s 189ms/step - loss: 2.0117 - mean_absolute_error: 1.1020   512/Unknown  104s 189ms/step - loss: 2.0106 - mean_absolute_error: 1.1017   513/Unknown  104s 189ms/step - loss: 2.0095 - mean_absolute_error: 1.1014   514/Unknown  104s 189ms/step - loss: 2.0083 - mean_absolute_error: 1.1011   515/Unknown  104s 189ms/step - loss: 2.0072 - mean_absolute_error: 1.1008   516/Unknown  104s 189ms/step - loss: 2.0061 - mean_absolute_error: 1.1005   517/Unknown  105s 189ms/step - loss: 2.0050 - mean_absolute_error: 1.1002   518/Unknown  105s 189ms/step - loss: 2.0038 - mean_absolute_error: 1.0999   519/Unknown  105s 189ms/step - loss: 2.0027 - mean_absolute_error: 1.0996   520/Unknown  105s 189ms/step - loss: 2.0016 - mean_absolute_error: 1.0993   521/Unknown  105s 190ms/step - loss: 2.0005 - mean_absolute_error: 1.0990   522/Unknown  106s 190ms/step - loss: 1.9994 - mean_absolute_error: 1.0987   523/Unknown  106s 190ms/step - loss: 1.9983 - mean_absolute_error: 1.0984   524/Unknown  106s 190ms/step - loss: 1.9972 - mean_absolute_error: 1.0981   525/Unknown  106s 190ms/step - loss: 1.9961 - mean_absolute_error: 1.0978   526/Unknown  106s 190ms/step - loss: 1.9950 - mean_absolute_error: 1.0975   527/Unknown  107s 190ms/step - loss: 1.9939 - mean_absolute_error: 1.0973   528/Unknown  107s 190ms/step - loss: 1.9928 - mean_absolute_error: 1.0970   529/Unknown  107s 190ms/step - loss: 1.9918 - mean_absolute_error: 1.0967   530/Unknown  107s 190ms/step - loss: 1.9907 - mean_absolute_error: 1.0964   531/Unknown  108s 190ms/step - loss: 1.9896 - mean_absolute_error: 1.0961   532/Unknown  108s 190ms/step - loss: 1.9885 - mean_absolute_error: 1.0958   533/Unknown  108s 190ms/step - loss: 1.9875 - mean_absolute_error: 1.0955   534/Unknown  108s 190ms/step - loss: 1.9864 - mean_absolute_error: 1.0953   535/Unknown  109s 190ms/step - loss: 1.9853 - mean_absolute_error: 1.0950   536/Unknown  109s 191ms/step - loss: 1.9843 - mean_absolute_error: 1.0947   537/Unknown  109s 191ms/step - loss: 1.9832 - mean_absolute_error: 1.0944   538/Unknown  109s 191ms/step - loss: 1.9822 - mean_absolute_error: 1.0941   539/Unknown  110s 191ms/step - loss: 1.9811 - mean_absolute_error: 1.0939   540/Unknown  110s 191ms/step - loss: 1.9801 - mean_absolute_error: 1.0936   541/Unknown  110s 191ms/step - loss: 1.9791 - mean_absolute_error: 1.0933   542/Unknown  110s 191ms/step - loss: 1.9780 - mean_absolute_error: 1.0930   543/Unknown  110s 191ms/step - loss: 1.9770 - mean_absolute_error: 1.0928   544/Unknown  111s 191ms/step - loss: 1.9759 - mean_absolute_error: 1.0925   545/Unknown  111s 191ms/step - loss: 1.9749 - mean_absolute_error: 1.0922   546/Unknown  111s 191ms/step - loss: 1.9739 - mean_absolute_error: 1.0919   547/Unknown  111s 191ms/step - loss: 1.9729 - mean_absolute_error: 1.0917   548/Unknown  112s 191ms/step - loss: 1.9718 - mean_absolute_error: 1.0914   549/Unknown  112s 191ms/step - loss: 1.9708 - mean_absolute_error: 1.0911   550/Unknown  112s 191ms/step - loss: 1.9698 - mean_absolute_error: 1.0909   551/Unknown  112s 191ms/step - loss: 1.9688 - mean_absolute_error: 1.0906   552/Unknown  112s 191ms/step - loss: 1.9678 - mean_absolute_error: 1.0903   553/Unknown  113s 192ms/step - loss: 1.9668 - mean_absolute_error: 1.0900   554/Unknown  113s 192ms/step - loss: 1.9658 - mean_absolute_error: 1.0898   555/Unknown  113s 192ms/step - loss: 1.9648 - mean_absolute_error: 1.0895   556/Unknown  113s 192ms/step - loss: 1.9638 - mean_absolute_error: 1.0892   557/Unknown  114s 192ms/step - loss: 1.9628 - mean_absolute_error: 1.0890   558/Unknown  114s 192ms/step - loss: 1.9618 - mean_absolute_error: 1.0887   559/Unknown  114s 192ms/step - loss: 1.9608 - mean_absolute_error: 1.0885   560/Unknown  114s 192ms/step - loss: 1.9598 - mean_absolute_error: 1.0882   561/Unknown  114s 192ms/step - loss: 1.9588 - mean_absolute_error: 1.0879   562/Unknown  115s 192ms/step - loss: 1.9579 - mean_absolute_error: 1.0877   563/Unknown  115s 192ms/step - loss: 1.9569 - mean_absolute_error: 1.0874   564/Unknown  115s 192ms/step - loss: 1.9559 - mean_absolute_error: 1.0872   565/Unknown  115s 192ms/step - loss: 1.9549 - mean_absolute_error: 1.0869   566/Unknown  116s 192ms/step - loss: 1.9540 - mean_absolute_error: 1.0866   567/Unknown  116s 192ms/step - loss: 1.9530 - mean_absolute_error: 1.0864   568/Unknown  116s 193ms/step - loss: 1.9520 - mean_absolute_error: 1.0861   569/Unknown  116s 193ms/step - loss: 1.9511 - mean_absolute_error: 1.0859   570/Unknown  117s 193ms/step - loss: 1.9501 - mean_absolute_error: 1.0856   571/Unknown  117s 193ms/step - loss: 1.9492 - mean_absolute_error: 1.0854   572/Unknown  117s 193ms/step - loss: 1.9482 - mean_absolute_error: 1.0851   573/Unknown  117s 193ms/step - loss: 1.9473 - mean_absolute_error: 1.0848   574/Unknown  118s 193ms/step - loss: 1.9463 - mean_absolute_error: 1.0846   575/Unknown  118s 193ms/step - loss: 1.9454 - mean_absolute_error: 1.0843   576/Unknown  118s 193ms/step - loss: 1.9444 - mean_absolute_error: 1.0841   577/Unknown  118s 193ms/step - loss: 1.9435 - mean_absolute_error: 1.0838   578/Unknown  118s 193ms/step - loss: 1.9426 - mean_absolute_error: 1.0836   579/Unknown  119s 193ms/step - loss: 1.9416 - mean_absolute_error: 1.0833   580/Unknown  119s 193ms/step - loss: 1.9407 - mean_absolute_error: 1.0831   581/Unknown  119s 193ms/step - loss: 1.9398 - mean_absolute_error: 1.0828   582/Unknown  119s 193ms/step - loss: 1.9388 - mean_absolute_error: 1.0826   583/Unknown  119s 193ms/step - loss: 1.9379 - mean_absolute_error: 1.0824   584/Unknown  120s 193ms/step - loss: 1.9370 - mean_absolute_error: 1.0821   585/Unknown  120s 193ms/step - loss: 1.9361 - mean_absolute_error: 1.0819   586/Unknown  120s 193ms/step - loss: 1.9352 - mean_absolute_error: 1.0816   587/Unknown  120s 193ms/step - loss: 1.9342 - mean_absolute_error: 1.0814   588/Unknown  120s 193ms/step - loss: 1.9333 - mean_absolute_error: 1.0811   589/Unknown  121s 193ms/step - loss: 1.9324 - mean_absolute_error: 1.0809   590/Unknown  121s 193ms/step - loss: 1.9315 - mean_absolute_error: 1.0806   591/Unknown  121s 193ms/step - loss: 1.9306 - mean_absolute_error: 1.0804   592/Unknown  121s 193ms/step - loss: 1.9297 - mean_absolute_error: 1.0802   593/Unknown  121s 194ms/step - loss: 1.9288 - mean_absolute_error: 1.0799   594/Unknown  122s 194ms/step - loss: 1.9279 - mean_absolute_error: 1.0797   595/Unknown  122s 194ms/step - loss: 1.9270 - mean_absolute_error: 1.0794   596/Unknown  122s 194ms/step - loss: 1.9261 - mean_absolute_error: 1.0792   597/Unknown  122s 194ms/step - loss: 1.9252 - mean_absolute_error: 1.0790   598/Unknown  122s 194ms/step - loss: 1.9243 - mean_absolute_error: 1.0787   599/Unknown  123s 194ms/step - loss: 1.9234 - mean_absolute_error: 1.0785   600/Unknown  123s 194ms/step - loss: 1.9226 - mean_absolute_error: 1.0782   601/Unknown  123s 194ms/step - loss: 1.9217 - mean_absolute_error: 1.0780   602/Unknown  124s 194ms/step - loss: 1.9208 - mean_absolute_error: 1.0778   603/Unknown  124s 194ms/step - loss: 1.9199 - mean_absolute_error: 1.0775   604/Unknown  124s 194ms/step - loss: 1.9190 - mean_absolute_error: 1.0773   605/Unknown  124s 194ms/step - loss: 1.9182 - mean_absolute_error: 1.0771   606/Unknown  125s 195ms/step - loss: 1.9173 - mean_absolute_error: 1.0768   607/Unknown  125s 195ms/step - loss: 1.9164 - mean_absolute_error: 1.0766   608/Unknown  125s 195ms/step - loss: 1.9156 - mean_absolute_error: 1.0764   609/Unknown  125s 195ms/step - loss: 1.9147 - mean_absolute_error: 1.0761   610/Unknown  125s 195ms/step - loss: 1.9139 - mean_absolute_error: 1.0759   611/Unknown  126s 195ms/step - loss: 1.9130 - mean_absolute_error: 1.0757   612/Unknown  126s 195ms/step - loss: 1.9121 - mean_absolute_error: 1.0754   613/Unknown  126s 195ms/step - loss: 1.9113 - mean_absolute_error: 1.0752   614/Unknown  126s 195ms/step - loss: 1.9104 - mean_absolute_error: 1.0750   615/Unknown  126s 195ms/step - loss: 1.9096 - mean_absolute_error: 1.0748   616/Unknown  127s 195ms/step - loss: 1.9087 - mean_absolute_error: 1.0745   617/Unknown  127s 195ms/step - loss: 1.9079 - mean_absolute_error: 1.0743   618/Unknown  127s 195ms/step - loss: 1.9070 - mean_absolute_error: 1.0741   619/Unknown  127s 195ms/step - loss: 1.9062 - mean_absolute_error: 1.0739   620/Unknown  128s 195ms/step - loss: 1.9054 - mean_absolute_error: 1.0736   621/Unknown  128s 195ms/step - loss: 1.9045 - mean_absolute_error: 1.0734   622/Unknown  128s 195ms/step - loss: 1.9037 - mean_absolute_error: 1.0732   623/Unknown  128s 195ms/step - loss: 1.9029 - mean_absolute_error: 1.0730   624/Unknown  128s 195ms/step - loss: 1.9020 - mean_absolute_error: 1.0727   625/Unknown  129s 195ms/step - loss: 1.9012 - mean_absolute_error: 1.0725   626/Unknown  129s 195ms/step - loss: 1.9004 - mean_absolute_error: 1.0723   627/Unknown  129s 195ms/step - loss: 1.8996 - mean_absolute_error: 1.0721   628/Unknown  129s 195ms/step - loss: 1.8987 - mean_absolute_error: 1.0718   629/Unknown  129s 195ms/step - loss: 1.8979 - mean_absolute_error: 1.0716   630/Unknown  130s 195ms/step - loss: 1.8971 - mean_absolute_error: 1.0714   631/Unknown  130s 195ms/step - loss: 1.8963 - mean_absolute_error: 1.0712   632/Unknown  130s 195ms/step - loss: 1.8955 - mean_absolute_error: 1.0710   633/Unknown  130s 195ms/step - loss: 1.8947 - mean_absolute_error: 1.0708   634/Unknown  131s 195ms/step - loss: 1.8939 - mean_absolute_error: 1.0705   635/Unknown  131s 195ms/step - loss: 1.8931 - mean_absolute_error: 1.0703   636/Unknown  131s 195ms/step - loss: 1.8923 - mean_absolute_error: 1.0701   637/Unknown  131s 195ms/step - loss: 1.8915 - mean_absolute_error: 1.0699   638/Unknown  131s 196ms/step - loss: 1.8907 - mean_absolute_error: 1.0697   639/Unknown  132s 196ms/step - loss: 1.8899 - mean_absolute_error: 1.0695   640/Unknown  132s 196ms/step - loss: 1.8891 - mean_absolute_error: 1.0692   641/Unknown  132s 196ms/step - loss: 1.8883 - mean_absolute_error: 1.0690   642/Unknown  132s 196ms/step - loss: 1.8875 - mean_absolute_error: 1.0688   643/Unknown  133s 196ms/step - loss: 1.8867 - mean_absolute_error: 1.0686   644/Unknown  133s 196ms/step - loss: 1.8859 - mean_absolute_error: 1.0684   645/Unknown  133s 196ms/step - loss: 1.8851 - mean_absolute_error: 1.0682   646/Unknown  133s 196ms/step - loss: 1.8843 - mean_absolute_error: 1.0680   647/Unknown  134s 196ms/step - loss: 1.8835 - mean_absolute_error: 1.0678   648/Unknown  134s 196ms/step - loss: 1.8828 - mean_absolute_error: 1.0675   649/Unknown  134s 196ms/step - loss: 1.8820 - mean_absolute_error: 1.0673   650/Unknown  134s 196ms/step - loss: 1.8812 - mean_absolute_error: 1.0671   651/Unknown  134s 196ms/step - loss: 1.8804 - mean_absolute_error: 1.0669   652/Unknown  135s 196ms/step - loss: 1.8796 - mean_absolute_error: 1.0667   653/Unknown  135s 196ms/step - loss: 1.8789 - mean_absolute_error: 1.0665   654/Unknown  135s 196ms/step - loss: 1.8781 - mean_absolute_error: 1.0663   655/Unknown  135s 196ms/step - loss: 1.8773 - mean_absolute_error: 1.0661   656/Unknown  135s 196ms/step - loss: 1.8766 - mean_absolute_error: 1.0659   657/Unknown  136s 196ms/step - loss: 1.8758 - mean_absolute_error: 1.0657   658/Unknown  136s 196ms/step - loss: 1.8750 - mean_absolute_error: 1.0655   659/Unknown  136s 196ms/step - loss: 1.8743 - mean_absolute_error: 1.0652   660/Unknown  136s 196ms/step - loss: 1.8735 - mean_absolute_error: 1.0650   661/Unknown  137s 197ms/step - loss: 1.8728 - mean_absolute_error: 1.0648   662/Unknown  137s 197ms/step - loss: 1.8720 - mean_absolute_error: 1.0646   663/Unknown  137s 197ms/step - loss: 1.8713 - mean_absolute_error: 1.0644   664/Unknown  137s 197ms/step - loss: 1.8705 - mean_absolute_error: 1.0642   665/Unknown  137s 197ms/step - loss: 1.8698 - mean_absolute_error: 1.0640   666/Unknown  138s 197ms/step - loss: 1.8690 - mean_absolute_error: 1.0638   667/Unknown  138s 197ms/step - loss: 1.8683 - mean_absolute_error: 1.0636   668/Unknown  138s 197ms/step - loss: 1.8675 - mean_absolute_error: 1.0634   669/Unknown  138s 197ms/step - loss: 1.8668 - mean_absolute_error: 1.0632   670/Unknown  139s 197ms/step - loss: 1.8660 - mean_absolute_error: 1.0630   671/Unknown  139s 197ms/step - loss: 1.8653 - mean_absolute_error: 1.0628   672/Unknown  139s 197ms/step - loss: 1.8646 - mean_absolute_error: 1.0626   673/Unknown  139s 197ms/step - loss: 1.8638 - mean_absolute_error: 1.0624   674/Unknown  140s 197ms/step - loss: 1.8631 - mean_absolute_error: 1.0622   675/Unknown  140s 198ms/step - loss: 1.8624 - mean_absolute_error: 1.0620   676/Unknown  140s 198ms/step - loss: 1.8616 - mean_absolute_error: 1.0618   677/Unknown  141s 198ms/step - loss: 1.8609 - mean_absolute_error: 1.0616   678/Unknown  141s 198ms/step - loss: 1.8602 - mean_absolute_error: 1.0614   679/Unknown  141s 198ms/step - loss: 1.8595 - mean_absolute_error: 1.0612   680/Unknown  141s 198ms/step - loss: 1.8587 - mean_absolute_error: 1.0610   681/Unknown  142s 198ms/step - loss: 1.8580 - mean_absolute_error: 1.0609   682/Unknown  142s 198ms/step - loss: 1.8573 - mean_absolute_error: 1.0607   683/Unknown  142s 198ms/step - loss: 1.8566 - mean_absolute_error: 1.0605   684/Unknown  143s 199ms/step - loss: 1.8559 - mean_absolute_error: 1.0603   685/Unknown  143s 199ms/step - loss: 1.8551 - mean_absolute_error: 1.0601   686/Unknown  143s 199ms/step - loss: 1.8544 - mean_absolute_error: 1.0599   687/Unknown  143s 199ms/step - loss: 1.8537 - mean_absolute_error: 1.0597   688/Unknown  144s 199ms/step - loss: 1.8530 - mean_absolute_error: 1.0595   689/Unknown  144s 199ms/step - loss: 1.8523 - mean_absolute_error: 1.0593   690/Unknown  144s 199ms/step - loss: 1.8516 - mean_absolute_error: 1.0591   691/Unknown  144s 199ms/step - loss: 1.8509 - mean_absolute_error: 1.0589   692/Unknown  145s 199ms/step - loss: 1.8502 - mean_absolute_error: 1.0587   693/Unknown  145s 199ms/step - loss: 1.8495 - mean_absolute_error: 1.0585   694/Unknown  145s 199ms/step - loss: 1.8488 - mean_absolute_error: 1.0584   695/Unknown  145s 200ms/step - loss: 1.8481 - mean_absolute_error: 1.0582   696/Unknown  146s 200ms/step - loss: 1.8474 - mean_absolute_error: 1.0580   697/Unknown  146s 200ms/step - loss: 1.8467 - mean_absolute_error: 1.0578   698/Unknown  146s 200ms/step - loss: 1.8460 - mean_absolute_error: 1.0576   699/Unknown  146s 200ms/step - loss: 1.8453 - mean_absolute_error: 1.0574   700/Unknown  147s 200ms/step - loss: 1.8446 - mean_absolute_error: 1.0572   701/Unknown  147s 200ms/step - loss: 1.8439 - mean_absolute_error: 1.0570   702/Unknown  147s 200ms/step - loss: 1.8432 - mean_absolute_error: 1.0569   703/Unknown  147s 200ms/step - loss: 1.8425 - mean_absolute_error: 1.0567   704/Unknown  147s 200ms/step - loss: 1.8419 - mean_absolute_error: 1.0565   705/Unknown  148s 200ms/step - loss: 1.8412 - mean_absolute_error: 1.0563   706/Unknown  148s 200ms/step - loss: 1.8405 - mean_absolute_error: 1.0561   707/Unknown  148s 200ms/step - loss: 1.8398 - mean_absolute_error: 1.0559   708/Unknown  149s 200ms/step - loss: 1.8391 - mean_absolute_error: 1.0557   709/Unknown  149s 200ms/step - loss: 1.8385 - mean_absolute_error: 1.0556   710/Unknown  149s 200ms/step - loss: 1.8378 - mean_absolute_error: 1.0554   711/Unknown  149s 201ms/step - loss: 1.8371 - mean_absolute_error: 1.0552   712/Unknown  150s 201ms/step - loss: 1.8364 - mean_absolute_error: 1.0550   713/Unknown  150s 201ms/step - loss: 1.8358 - mean_absolute_error: 1.0548   714/Unknown  150s 201ms/step - loss: 1.8351 - mean_absolute_error: 1.0547   715/Unknown  150s 201ms/step - loss: 1.8344 - mean_absolute_error: 1.0545   716/Unknown  151s 201ms/step - loss: 1.8338 - mean_absolute_error: 1.0543   717/Unknown  151s 201ms/step - loss: 1.8331 - mean_absolute_error: 1.0541   718/Unknown  151s 201ms/step - loss: 1.8324 - mean_absolute_error: 1.0539   719/Unknown  151s 201ms/step - loss: 1.8318 - mean_absolute_error: 1.0537   720/Unknown  152s 201ms/step - loss: 1.8311 - mean_absolute_error: 1.0536   721/Unknown  152s 201ms/step - loss: 1.8305 - mean_absolute_error: 1.0534   722/Unknown  152s 201ms/step - loss: 1.8298 - mean_absolute_error: 1.0532   723/Unknown  152s 201ms/step - loss: 1.8291 - mean_absolute_error: 1.0530   724/Unknown  152s 201ms/step - loss: 1.8285 - mean_absolute_error: 1.0529   725/Unknown  153s 201ms/step - loss: 1.8278 - mean_absolute_error: 1.0527   726/Unknown  153s 201ms/step - loss: 1.8272 - mean_absolute_error: 1.0525   727/Unknown  153s 201ms/step - loss: 1.8265 - mean_absolute_error: 1.0523   728/Unknown  153s 201ms/step - loss: 1.8259 - mean_absolute_error: 1.0522   729/Unknown  153s 201ms/step - loss: 1.8253 - mean_absolute_error: 1.0520   730/Unknown  154s 201ms/step - loss: 1.8246 - mean_absolute_error: 1.0518   731/Unknown  154s 201ms/step - loss: 1.8240 - mean_absolute_error: 1.0516   732/Unknown  154s 201ms/step - loss: 1.8233 - mean_absolute_error: 1.0515   733/Unknown  154s 201ms/step - loss: 1.8227 - mean_absolute_error: 1.0513   734/Unknown  154s 201ms/step - loss: 1.8220 - mean_absolute_error: 1.0511   735/Unknown  155s 201ms/step - loss: 1.8214 - mean_absolute_error: 1.0509   736/Unknown  155s 201ms/step - loss: 1.8208 - mean_absolute_error: 1.0508   737/Unknown  155s 201ms/step - loss: 1.8201 - mean_absolute_error: 1.0506   738/Unknown  155s 201ms/step - loss: 1.8195 - mean_absolute_error: 1.0504   739/Unknown  155s 201ms/step - loss: 1.8189 - mean_absolute_error: 1.0502   740/Unknown  156s 201ms/step - loss: 1.8182 - mean_absolute_error: 1.0501   741/Unknown  156s 201ms/step - loss: 1.8176 - mean_absolute_error: 1.0499   742/Unknown  156s 201ms/step - loss: 1.8170 - mean_absolute_error: 1.0497   743/Unknown  156s 201ms/step - loss: 1.8164 - mean_absolute_error: 1.0496   744/Unknown  157s 201ms/step - loss: 1.8157 - mean_absolute_error: 1.0494   745/Unknown  157s 201ms/step - loss: 1.8151 - mean_absolute_error: 1.0492   746/Unknown  157s 201ms/step - loss: 1.8145 - mean_absolute_error: 1.0491   747/Unknown  157s 201ms/step - loss: 1.8139 - mean_absolute_error: 1.0489   748/Unknown  157s 202ms/step - loss: 1.8133 - mean_absolute_error: 1.0487   749/Unknown  158s 202ms/step - loss: 1.8126 - mean_absolute_error: 1.0485   750/Unknown  158s 202ms/step - loss: 1.8120 - mean_absolute_error: 1.0484   751/Unknown  158s 202ms/step - loss: 1.8114 - mean_absolute_error: 1.0482   752/Unknown  159s 202ms/step - loss: 1.8108 - mean_absolute_error: 1.0480   753/Unknown  159s 202ms/step - loss: 1.8102 - mean_absolute_error: 1.0479   754/Unknown  159s 202ms/step - loss: 1.8096 - mean_absolute_error: 1.0477   755/Unknown  159s 202ms/step - loss: 1.8090 - mean_absolute_error: 1.0475   756/Unknown  159s 202ms/step - loss: 1.8083 - mean_absolute_error: 1.0474   757/Unknown  160s 202ms/step - loss: 1.8077 - mean_absolute_error: 1.0472   758/Unknown  160s 202ms/step - loss: 1.8071 - mean_absolute_error: 1.0470   759/Unknown  160s 202ms/step - loss: 1.8065 - mean_absolute_error: 1.0469   760/Unknown  160s 202ms/step - loss: 1.8059 - mean_absolute_error: 1.0467   761/Unknown  161s 202ms/step - loss: 1.8053 - mean_absolute_error: 1.0466   762/Unknown  161s 202ms/step - loss: 1.8047 - mean_absolute_error: 1.0464   763/Unknown  161s 202ms/step - loss: 1.8041 - mean_absolute_error: 1.0462   764/Unknown  161s 202ms/step - loss: 1.8035 - mean_absolute_error: 1.0461   765/Unknown  162s 202ms/step - loss: 1.8029 - mean_absolute_error: 1.0459   766/Unknown  162s 203ms/step - loss: 1.8023 - mean_absolute_error: 1.0457   767/Unknown  162s 203ms/step - loss: 1.8017 - mean_absolute_error: 1.0456   768/Unknown  162s 203ms/step - loss: 1.8011 - mean_absolute_error: 1.0454   769/Unknown  163s 203ms/step - loss: 1.8005 - mean_absolute_error: 1.0453   770/Unknown  163s 203ms/step - loss: 1.7999 - mean_absolute_error: 1.0451   771/Unknown  163s 203ms/step - loss: 1.7994 - mean_absolute_error: 1.0449   772/Unknown  163s 203ms/step - loss: 1.7988 - mean_absolute_error: 1.0448   773/Unknown  164s 203ms/step - loss: 1.7982 - mean_absolute_error: 1.0446   774/Unknown  164s 203ms/step - loss: 1.7976 - mean_absolute_error: 1.0444   775/Unknown  164s 203ms/step - loss: 1.7970 - mean_absolute_error: 1.0443   776/Unknown  164s 203ms/step - loss: 1.7964 - mean_absolute_error: 1.0441   777/Unknown  164s 203ms/step - loss: 1.7958 - mean_absolute_error: 1.0440   778/Unknown  165s 203ms/step - loss: 1.7953 - mean_absolute_error: 1.0438   779/Unknown  165s 203ms/step - loss: 1.7947 - mean_absolute_error: 1.0437   780/Unknown  165s 203ms/step - loss: 1.7941 - mean_absolute_error: 1.0435   781/Unknown  166s 203ms/step - loss: 1.7935 - mean_absolute_error: 1.0433   782/Unknown  166s 204ms/step - loss: 1.7929 - mean_absolute_error: 1.0432   783/Unknown  166s 204ms/step - loss: 1.7924 - mean_absolute_error: 1.0430   784/Unknown  166s 204ms/step - loss: 1.7918 - mean_absolute_error: 1.0429   785/Unknown  167s 204ms/step - loss: 1.7912 - mean_absolute_error: 1.0427   786/Unknown  167s 204ms/step - loss: 1.7907 - mean_absolute_error: 1.0426   787/Unknown  167s 204ms/step - loss: 1.7901 - mean_absolute_error: 1.0424   788/Unknown  167s 204ms/step - loss: 1.7895 - mean_absolute_error: 1.0422   789/Unknown  168s 204ms/step - loss: 1.7889 - mean_absolute_error: 1.0421   790/Unknown  168s 204ms/step - loss: 1.7884 - mean_absolute_error: 1.0419   791/Unknown  168s 204ms/step - loss: 1.7878 - mean_absolute_error: 1.0418   792/Unknown  168s 204ms/step - loss: 1.7872 - mean_absolute_error: 1.0416   793/Unknown  168s 204ms/step - loss: 1.7867 - mean_absolute_error: 1.0415   794/Unknown  169s 204ms/step - loss: 1.7861 - mean_absolute_error: 1.0413   795/Unknown  169s 204ms/step - loss: 1.7856 - mean_absolute_error: 1.0412   796/Unknown  169s 204ms/step - loss: 1.7850 - mean_absolute_error: 1.0410   797/Unknown  169s 204ms/step - loss: 1.7844 - mean_absolute_error: 1.0409   798/Unknown  170s 204ms/step - loss: 1.7839 - mean_absolute_error: 1.0407   799/Unknown  170s 204ms/step - loss: 1.7833 - mean_absolute_error: 1.0406   800/Unknown  170s 204ms/step - loss: 1.7828 - mean_absolute_error: 1.0404   801/Unknown  170s 204ms/step - loss: 1.7822 - mean_absolute_error: 1.0402   802/Unknown  170s 204ms/step - loss: 1.7817 - mean_absolute_error: 1.0401   803/Unknown  171s 204ms/step - loss: 1.7811 - mean_absolute_error: 1.0399   804/Unknown  171s 204ms/step - loss: 1.7806 - mean_absolute_error: 1.0398   805/Unknown  171s 204ms/step - loss: 1.7800 - mean_absolute_error: 1.0396   806/Unknown  171s 204ms/step - loss: 1.7794 - mean_absolute_error: 1.0395   807/Unknown  172s 205ms/step - loss: 1.7789 - mean_absolute_error: 1.0393   808/Unknown  172s 205ms/step - loss: 1.7784 - mean_absolute_error: 1.0392   809/Unknown  172s 205ms/step - loss: 1.7778 - mean_absolute_error: 1.0390   810/Unknown  172s 205ms/step - loss: 1.7773 - mean_absolute_error: 1.0389   811/Unknown  173s 205ms/step - loss: 1.7767 - mean_absolute_error: 1.0387   812/Unknown  173s 205ms/step - loss: 1.7762 - mean_absolute_error: 1.0386   813/Unknown  173s 205ms/step - loss: 1.7756 - mean_absolute_error: 1.0384   814/Unknown  173s 205ms/step - loss: 1.7751 - mean_absolute_error: 1.0383   815/Unknown  174s 205ms/step - loss: 1.7745 - mean_absolute_error: 1.0381   816/Unknown  174s 205ms/step - loss: 1.7740 - mean_absolute_error: 1.0380   817/Unknown  174s 205ms/step - loss: 1.7735 - mean_absolute_error: 1.0379   818/Unknown  174s 205ms/step - loss: 1.7729 - mean_absolute_error: 1.0377   819/Unknown  175s 205ms/step - loss: 1.7724 - mean_absolute_error: 1.0376   820/Unknown  175s 205ms/step - loss: 1.7719 - mean_absolute_error: 1.0374   821/Unknown  175s 205ms/step - loss: 1.7713 - mean_absolute_error: 1.0373   822/Unknown  175s 205ms/step - loss: 1.7708 - mean_absolute_error: 1.0371   823/Unknown  176s 205ms/step - loss: 1.7703 - mean_absolute_error: 1.0370   824/Unknown  176s 205ms/step - loss: 1.7697 - mean_absolute_error: 1.0368   825/Unknown  176s 205ms/step - loss: 1.7692 - mean_absolute_error: 1.0367   826/Unknown  176s 206ms/step - loss: 1.7687 - mean_absolute_error: 1.0365   827/Unknown  177s 206ms/step - loss: 1.7681 - mean_absolute_error: 1.0364   828/Unknown  177s 206ms/step - loss: 1.7676 - mean_absolute_error: 1.0362   829/Unknown  177s 206ms/step - loss: 1.7671 - mean_absolute_error: 1.0361   830/Unknown  178s 206ms/step - loss: 1.7666 - mean_absolute_error: 1.0360   831/Unknown  178s 206ms/step - loss: 1.7660 - mean_absolute_error: 1.0358   832/Unknown  178s 206ms/step - loss: 1.7655 - mean_absolute_error: 1.0357   833/Unknown  178s 206ms/step - loss: 1.7650 - mean_absolute_error: 1.0355   834/Unknown  179s 206ms/step - loss: 1.7645 - mean_absolute_error: 1.0354   835/Unknown  179s 206ms/step - loss: 1.7639 - mean_absolute_error: 1.0352   836/Unknown  179s 206ms/step - loss: 1.7634 - mean_absolute_error: 1.0351   837/Unknown  179s 206ms/step - loss: 1.7629 - mean_absolute_error: 1.0350   838/Unknown  179s 206ms/step - loss: 1.7624 - mean_absolute_error: 1.0348   839/Unknown  180s 206ms/step - loss: 1.7619 - mean_absolute_error: 1.0347   840/Unknown  180s 206ms/step - loss: 1.7614 - mean_absolute_error: 1.0345   841/Unknown  180s 206ms/step - loss: 1.7608 - mean_absolute_error: 1.0344   842/Unknown  180s 206ms/step - loss: 1.7603 - mean_absolute_error: 1.0343   843/Unknown  181s 206ms/step - loss: 1.7598 - mean_absolute_error: 1.0341   844/Unknown  181s 206ms/step - loss: 1.7593 - mean_absolute_error: 1.0340   845/Unknown  181s 206ms/step - loss: 1.7588 - mean_absolute_error: 1.0338   846/Unknown  181s 206ms/step - loss: 1.7583 - mean_absolute_error: 1.0337   847/Unknown  181s 206ms/step - loss: 1.7578 - mean_absolute_error: 1.0335   848/Unknown  182s 206ms/step - loss: 1.7573 - mean_absolute_error: 1.0334   849/Unknown  182s 206ms/step - loss: 1.7568 - mean_absolute_error: 1.0333   850/Unknown  182s 206ms/step - loss: 1.7563 - mean_absolute_error: 1.0331   851/Unknown  182s 206ms/step - loss: 1.7558 - mean_absolute_error: 1.0330   852/Unknown  183s 206ms/step - loss: 1.7553 - mean_absolute_error: 1.0329   853/Unknown  183s 207ms/step - loss: 1.7547 - mean_absolute_error: 1.0327   854/Unknown  183s 207ms/step - loss: 1.7542 - mean_absolute_error: 1.0326   855/Unknown  183s 207ms/step - loss: 1.7537 - mean_absolute_error: 1.0324   856/Unknown  183s 207ms/step - loss: 1.7532 - mean_absolute_error: 1.0323   857/Unknown  184s 207ms/step - loss: 1.7527 - mean_absolute_error: 1.0322   858/Unknown  184s 207ms/step - loss: 1.7522 - mean_absolute_error: 1.0320   859/Unknown  184s 207ms/step - loss: 1.7518 - mean_absolute_error: 1.0319   860/Unknown  184s 207ms/step - loss: 1.7513 - mean_absolute_error: 1.0318   861/Unknown  185s 207ms/step - loss: 1.7508 - mean_absolute_error: 1.0316   862/Unknown  185s 207ms/step - loss: 1.7503 - mean_absolute_error: 1.0315   863/Unknown  185s 207ms/step - loss: 1.7498 - mean_absolute_error: 1.0313   864/Unknown  185s 207ms/step - loss: 1.7493 - mean_absolute_error: 1.0312   865/Unknown  185s 207ms/step - loss: 1.7488 - mean_absolute_error: 1.0311   866/Unknown  186s 207ms/step - loss: 1.7483 - mean_absolute_error: 1.0309   867/Unknown  186s 207ms/step - loss: 1.7478 - mean_absolute_error: 1.0308   868/Unknown  186s 207ms/step - loss: 1.7473 - mean_absolute_error: 1.0307   869/Unknown  186s 207ms/step - loss: 1.7468 - mean_absolute_error: 1.0305   870/Unknown  187s 207ms/step - loss: 1.7463 - mean_absolute_error: 1.0304   871/Unknown  187s 207ms/step - loss: 1.7459 - mean_absolute_error: 1.0303   872/Unknown  187s 207ms/step - loss: 1.7454 - mean_absolute_error: 1.0301   873/Unknown  187s 207ms/step - loss: 1.7449 - mean_absolute_error: 1.0300   874/Unknown  188s 207ms/step - loss: 1.7444 - mean_absolute_error: 1.0299   875/Unknown  188s 207ms/step - loss: 1.7439 - mean_absolute_error: 1.0297   876/Unknown  188s 207ms/step - loss: 1.7434 - mean_absolute_error: 1.0296   877/Unknown  188s 207ms/step - loss: 1.7430 - mean_absolute_error: 1.0295   878/Unknown  189s 207ms/step - loss: 1.7425 - mean_absolute_error: 1.0293   879/Unknown  189s 207ms/step - loss: 1.7420 - mean_absolute_error: 1.0292   880/Unknown  189s 207ms/step - loss: 1.7415 - mean_absolute_error: 1.0291   881/Unknown  189s 207ms/step - loss: 1.7410 - mean_absolute_error: 1.0289   882/Unknown  190s 207ms/step - loss: 1.7406 - mean_absolute_error: 1.0288   883/Unknown  190s 207ms/step - loss: 1.7401 - mean_absolute_error: 1.0287   884/Unknown  190s 207ms/step - loss: 1.7396 - mean_absolute_error: 1.0286   885/Unknown  190s 207ms/step - loss: 1.7391 - mean_absolute_error: 1.0284   886/Unknown  191s 208ms/step - loss: 1.7387 - mean_absolute_error: 1.0283   887/Unknown  191s 208ms/step - loss: 1.7382 - mean_absolute_error: 1.0282   888/Unknown  191s 208ms/step - loss: 1.7377 - mean_absolute_error: 1.0280   889/Unknown  191s 208ms/step - loss: 1.7373 - mean_absolute_error: 1.0279   890/Unknown  192s 208ms/step - loss: 1.7368 - mean_absolute_error: 1.0278   891/Unknown  192s 208ms/step - loss: 1.7363 - mean_absolute_error: 1.0276   892/Unknown  192s 208ms/step - loss: 1.7359 - mean_absolute_error: 1.0275   893/Unknown  192s 208ms/step - loss: 1.7354 - mean_absolute_error: 1.0274   894/Unknown  193s 208ms/step - loss: 1.7349 - mean_absolute_error: 1.0273   895/Unknown  193s 208ms/step - loss: 1.7345 - mean_absolute_error: 1.0271   896/Unknown  193s 208ms/step - loss: 1.7340 - mean_absolute_error: 1.0270   897/Unknown  193s 208ms/step - loss: 1.7335 - mean_absolute_error: 1.0269   898/Unknown  194s 208ms/step - loss: 1.7331 - mean_absolute_error: 1.0267   899/Unknown  194s 208ms/step - loss: 1.7326 - mean_absolute_error: 1.0266   900/Unknown  194s 208ms/step - loss: 1.7322 - mean_absolute_error: 1.0265   901/Unknown  194s 208ms/step - loss: 1.7317 - mean_absolute_error: 1.0264   902/Unknown  195s 208ms/step - loss: 1.7312 - mean_absolute_error: 1.0262   903/Unknown  195s 209ms/step - loss: 1.7308 - mean_absolute_error: 1.0261   904/Unknown  195s 209ms/step - loss: 1.7303 - mean_absolute_error: 1.0260   905/Unknown  196s 209ms/step - loss: 1.7299 - mean_absolute_error: 1.0259   906/Unknown  196s 209ms/step - loss: 1.7294 - mean_absolute_error: 1.0257   907/Unknown  196s 209ms/step - loss: 1.7290 - mean_absolute_error: 1.0256   908/Unknown  196s 209ms/step - loss: 1.7285 - mean_absolute_error: 1.0255   909/Unknown  197s 209ms/step - loss: 1.7280 - mean_absolute_error: 1.0254   910/Unknown  197s 209ms/step - loss: 1.7276 - mean_absolute_error: 1.0252   911/Unknown  197s 209ms/step - loss: 1.7271 - mean_absolute_error: 1.0251   912/Unknown  197s 209ms/step - loss: 1.7267 - mean_absolute_error: 1.0250   913/Unknown  198s 209ms/step - loss: 1.7262 - mean_absolute_error: 1.0249   914/Unknown  198s 209ms/step - loss: 1.7258 - mean_absolute_error: 1.0247   915/Unknown  198s 209ms/step - loss: 1.7253 - mean_absolute_error: 1.0246   916/Unknown  198s 209ms/step - loss: 1.7249 - mean_absolute_error: 1.0245   917/Unknown  199s 209ms/step - loss: 1.7244 - mean_absolute_error: 1.0244   918/Unknown  199s 209ms/step - loss: 1.7240 - mean_absolute_error: 1.0242   919/Unknown  199s 209ms/step - loss: 1.7235 - mean_absolute_error: 1.0241   920/Unknown  199s 209ms/step - loss: 1.7231 - mean_absolute_error: 1.0240   921/Unknown  200s 209ms/step - loss: 1.7226 - mean_absolute_error: 1.0239   922/Unknown  200s 209ms/step - loss: 1.7222 - mean_absolute_error: 1.0237   923/Unknown  200s 209ms/step - loss: 1.7218 - mean_absolute_error: 1.0236   924/Unknown  200s 209ms/step - loss: 1.7213 - mean_absolute_error: 1.0235   925/Unknown  200s 209ms/step - loss: 1.7209 - mean_absolute_error: 1.0234   926/Unknown  201s 209ms/step - loss: 1.7204 - mean_absolute_error: 1.0233   927/Unknown  201s 209ms/step - loss: 1.7200 - mean_absolute_error: 1.0231   928/Unknown  201s 209ms/step - loss: 1.7196 - mean_absolute_error: 1.0230   929/Unknown  201s 209ms/step - loss: 1.7191 - mean_absolute_error: 1.0229   930/Unknown  201s 209ms/step - loss: 1.7187 - mean_absolute_error: 1.0228   931/Unknown  202s 209ms/step - loss: 1.7182 - mean_absolute_error: 1.0226   932/Unknown  202s 209ms/step - loss: 1.7178 - mean_absolute_error: 1.0225   933/Unknown  202s 210ms/step - loss: 1.7174 - mean_absolute_error: 1.0224   934/Unknown  202s 210ms/step - loss: 1.7169 - mean_absolute_error: 1.0223   935/Unknown  203s 210ms/step - loss: 1.7165 - mean_absolute_error: 1.0222   936/Unknown  203s 210ms/step - loss: 1.7160 - mean_absolute_error: 1.0220   937/Unknown  203s 210ms/step - loss: 1.7156 - mean_absolute_error: 1.0219   938/Unknown  203s 210ms/step - loss: 1.7152 - mean_absolute_error: 1.0218   939/Unknown  204s 210ms/step - loss: 1.7147 - mean_absolute_error: 1.0217   940/Unknown  204s 210ms/step - loss: 1.7143 - mean_absolute_error: 1.0216   941/Unknown  204s 210ms/step - loss: 1.7139 - mean_absolute_error: 1.0214   942/Unknown  204s 210ms/step - loss: 1.7134 - mean_absolute_error: 1.0213   943/Unknown  205s 210ms/step - loss: 1.7130 - mean_absolute_error: 1.0212   944/Unknown  205s 210ms/step - loss: 1.7126 - mean_absolute_error: 1.0211   945/Unknown  205s 210ms/step - loss: 1.7122 - mean_absolute_error: 1.0210   946/Unknown  205s 210ms/step - loss: 1.7117 - mean_absolute_error: 1.0208   947/Unknown  206s 210ms/step - loss: 1.7113 - mean_absolute_error: 1.0207   948/Unknown  206s 210ms/step - loss: 1.7109 - mean_absolute_error: 1.0206   949/Unknown  206s 210ms/step - loss: 1.7104 - mean_absolute_error: 1.0205   950/Unknown  206s 210ms/step - loss: 1.7100 - mean_absolute_error: 1.0204   951/Unknown  206s 210ms/step - loss: 1.7096 - mean_absolute_error: 1.0202   952/Unknown  207s 210ms/step - loss: 1.7092 - mean_absolute_error: 1.0201   953/Unknown  207s 210ms/step - loss: 1.7087 - mean_absolute_error: 1.0200   954/Unknown  207s 210ms/step - loss: 1.7083 - mean_absolute_error: 1.0199   955/Unknown  207s 210ms/step - loss: 1.7079 - mean_absolute_error: 1.0198   956/Unknown  207s 210ms/step - loss: 1.7075 - mean_absolute_error: 1.0197   957/Unknown  208s 210ms/step - loss: 1.7070 - mean_absolute_error: 1.0195   958/Unknown  208s 210ms/step - loss: 1.7066 - mean_absolute_error: 1.0194   959/Unknown  208s 210ms/step - loss: 1.7062 - mean_absolute_error: 1.0193   960/Unknown  208s 210ms/step - loss: 1.7058 - mean_absolute_error: 1.0192   961/Unknown  209s 210ms/step - loss: 1.7054 - mean_absolute_error: 1.0191   962/Unknown  209s 210ms/step - loss: 1.7049 - mean_absolute_error: 1.0190   963/Unknown  209s 210ms/step - loss: 1.7045 - mean_absolute_error: 1.0188   964/Unknown  209s 210ms/step - loss: 1.7041 - mean_absolute_error: 1.0187   965/Unknown  210s 210ms/step - loss: 1.7037 - mean_absolute_error: 1.0186   966/Unknown  210s 210ms/step - loss: 1.7033 - mean_absolute_error: 1.0185   967/Unknown  210s 210ms/step - loss: 1.7029 - mean_absolute_error: 1.0184   968/Unknown  210s 210ms/step - loss: 1.7025 - mean_absolute_error: 1.0183   969/Unknown  210s 210ms/step - loss: 1.7020 - mean_absolute_error: 1.0181   970/Unknown  211s 210ms/step - loss: 1.7016 - mean_absolute_error: 1.0180   971/Unknown  211s 210ms/step - loss: 1.7012 - mean_absolute_error: 1.0179   972/Unknown  211s 210ms/step - loss: 1.7008 - mean_absolute_error: 1.0178   973/Unknown  211s 210ms/step - loss: 1.7004 - mean_absolute_error: 1.0177   974/Unknown  212s 210ms/step - loss: 1.7000 - mean_absolute_error: 1.0176   975/Unknown  212s 210ms/step - loss: 1.6996 - mean_absolute_error: 1.0175   976/Unknown  212s 210ms/step - loss: 1.6992 - mean_absolute_error: 1.0173   977/Unknown  212s 210ms/step - loss: 1.6987 - mean_absolute_error: 1.0172   978/Unknown  212s 210ms/step - loss: 1.6983 - mean_absolute_error: 1.0171   979/Unknown  213s 210ms/step - loss: 1.6979 - mean_absolute_error: 1.0170   980/Unknown  213s 210ms/step - loss: 1.6975 - mean_absolute_error: 1.0169   981/Unknown  213s 210ms/step - loss: 1.6971 - mean_absolute_error: 1.0168   982/Unknown  213s 210ms/step - loss: 1.6967 - mean_absolute_error: 1.0167   983/Unknown  214s 211ms/step - loss: 1.6963 - mean_absolute_error: 1.0166   984/Unknown  214s 211ms/step - loss: 1.6959 - mean_absolute_error: 1.0164   985/Unknown  214s 211ms/step - loss: 1.6955 - mean_absolute_error: 1.0163   986/Unknown  214s 211ms/step - loss: 1.6951 - mean_absolute_error: 1.0162   987/Unknown  214s 211ms/step - loss: 1.6947 - mean_absolute_error: 1.0161   988/Unknown  215s 211ms/step - loss: 1.6943 - mean_absolute_error: 1.0160   989/Unknown  215s 211ms/step - loss: 1.6939 - mean_absolute_error: 1.0159   990/Unknown  215s 211ms/step - loss: 1.6935 - mean_absolute_error: 1.0158   991/Unknown  215s 211ms/step - loss: 1.6931 - mean_absolute_error: 1.0157   992/Unknown  216s 211ms/step - loss: 1.6927 - mean_absolute_error: 1.0155   993/Unknown  216s 211ms/step - loss: 1.6923 - mean_absolute_error: 1.0154   994/Unknown  216s 211ms/step - loss: 1.6919 - mean_absolute_error: 1.0153   995/Unknown  217s 211ms/step - loss: 1.6915 - mean_absolute_error: 1.0152   996/Unknown  217s 211ms/step - loss: 1.6911 - mean_absolute_error: 1.0151   997/Unknown  217s 211ms/step - loss: 1.6907 - mean_absolute_error: 1.0150   998/Unknown  217s 211ms/step - loss: 1.6903 - mean_absolute_error: 1.0149   999/Unknown  217s 211ms/step - loss: 1.6899 - mean_absolute_error: 1.0148  `

1000/Unknown 218s 211ms/step - loss: 1.6895 - mean\_absolute\_error: 1.0147

``

1001/Unknown 218s 211ms/step - loss: 1.6891 - mean\_absolute\_error: 1.0145

``

1002/Unknown 218s 211ms/step - loss: 1.6887 - mean\_absolute\_error: 1.0144

``

1003/Unknown 218s 211ms/step - loss: 1.6883 - mean\_absolute\_error: 1.0143

``

1004/Unknown 219s 211ms/step - loss: 1.6880 - mean\_absolute\_error: 1.0142

``

1005/Unknown 219s 211ms/step - loss: 1.6876 - mean\_absolute\_error: 1.0141

``

1006/Unknown 219s 211ms/step - loss: 1.6872 - mean\_absolute\_error: 1.0140

``

1007/Unknown 220s 211ms/step - loss: 1.6868 - mean\_absolute\_error: 1.0139

``

1008/Unknown 220s 211ms/step - loss: 1.6864 - mean\_absolute\_error: 1.0138

``

1009/Unknown 220s 212ms/step - loss: 1.6860 - mean\_absolute\_error: 1.0137

``

1010/Unknown 220s 212ms/step - loss: 1.6856 - mean\_absolute\_error: 1.0136

``

1011/Unknown 221s 212ms/step - loss: 1.6852 - mean\_absolute\_error: 1.0135

``

1012/Unknown 221s 212ms/step - loss: 1.6848 - mean\_absolute\_error: 1.0134

``

1013/Unknown 221s 212ms/step - loss: 1.6845 - mean\_absolute\_error: 1.0132

``

1014/Unknown 221s 212ms/step - loss: 1.6841 - mean\_absolute\_error: 1.0131

``

1015/Unknown 222s 212ms/step - loss: 1.6837 - mean\_absolute\_error: 1.0130

``

1016/Unknown 222s 212ms/step - loss: 1.6833 - mean\_absolute\_error: 1.0129

``

1017/Unknown 222s 212ms/step - loss: 1.6829 - mean\_absolute\_error: 1.0128

``

1018/Unknown 222s 212ms/step - loss: 1.6825 - mean\_absolute\_error: 1.0127

``

1019/Unknown 223s 212ms/step - loss: 1.6821 - mean\_absolute\_error: 1.0126

``

1020/Unknown 223s 212ms/step - loss: 1.6818 - mean\_absolute\_error: 1.0125

``

1021/Unknown 223s 212ms/step - loss: 1.6814 - mean\_absolute\_error: 1.0124

``

1022/Unknown 223s 212ms/step - loss: 1.6810 - mean\_absolute\_error: 1.0123

``

1023/Unknown 224s 212ms/step - loss: 1.6806 - mean\_absolute\_error: 1.0122

``

1024/Unknown 224s 212ms/step - loss: 1.6802 - mean\_absolute\_error: 1.0121

``

1025/Unknown 224s 212ms/step - loss: 1.6799 - mean\_absolute\_error: 1.0120

``

1026/Unknown 224s 212ms/step - loss: 1.6795 - mean\_absolute\_error: 1.0118

``

1027/Unknown 225s 212ms/step - loss: 1.6791 - mean\_absolute\_error: 1.0117

``

1028/Unknown 225s 212ms/step - loss: 1.6787 - mean\_absolute\_error: 1.0116

``

1029/Unknown 225s 212ms/step - loss: 1.6783 - mean\_absolute\_error: 1.0115

``

1030/Unknown 225s 212ms/step - loss: 1.6780 - mean\_absolute\_error: 1.0114

``

1031/Unknown 226s 212ms/step - loss: 1.6776 - mean\_absolute\_error: 1.0113

``

1032/Unknown 226s 212ms/step - loss: 1.6772 - mean\_absolute\_error: 1.0112

``

1033/Unknown 226s 212ms/step - loss: 1.6768 - mean\_absolute\_error: 1.0111

``

1034/Unknown 226s 212ms/step - loss: 1.6765 - mean\_absolute\_error: 1.0110

``

1035/Unknown 227s 212ms/step - loss: 1.6761 - mean\_absolute\_error: 1.0109

``

1036/Unknown 227s 212ms/step - loss: 1.6757 - mean\_absolute\_error: 1.0108

``

1037/Unknown 227s 213ms/step - loss: 1.6753 - mean\_absolute\_error: 1.0107

``

1038/Unknown 227s 213ms/step - loss: 1.6750 - mean\_absolute\_error: 1.0106

``

1039/Unknown 227s 213ms/step - loss: 1.6746 - mean\_absolute\_error: 1.0105

``

1040/Unknown 228s 213ms/step - loss: 1.6742 - mean\_absolute\_error: 1.0104

``

1041/Unknown 228s 213ms/step - loss: 1.6738 - mean\_absolute\_error: 1.0103

``

1042/Unknown 228s 213ms/step - loss: 1.6735 - mean\_absolute\_error: 1.0102

``

1043/Unknown 228s 213ms/step - loss: 1.6731 - mean\_absolute\_error: 1.0101

``

1044/Unknown 229s 213ms/step - loss: 1.6727 - mean\_absolute\_error: 1.0100

``

1045/Unknown 229s 213ms/step - loss: 1.6724 - mean\_absolute\_error: 1.0099

``

1046/Unknown 229s 213ms/step - loss: 1.6720 - mean\_absolute\_error: 1.0097

``

1047/Unknown 229s 213ms/step - loss: 1.6716 - mean\_absolute\_error: 1.0096

``

1048/Unknown 229s 213ms/step - loss: 1.6713 - mean\_absolute\_error: 1.0095

``

1049/Unknown 230s 213ms/step - loss: 1.6709 - mean\_absolute\_error: 1.0094

``

1050/Unknown 230s 213ms/step - loss: 1.6705 - mean\_absolute\_error: 1.0093

``

1051/Unknown 230s 213ms/step - loss: 1.6702 - mean\_absolute\_error: 1.0092

``

1052/Unknown 230s 213ms/step - loss: 1.6698 - mean\_absolute\_error: 1.0091

``

1053/Unknown 231s 213ms/step - loss: 1.6694 - mean\_absolute\_error: 1.0090

``

1054/Unknown 231s 213ms/step - loss: 1.6691 - mean\_absolute\_error: 1.0089

``

1055/Unknown 231s 213ms/step - loss: 1.6687 - mean\_absolute\_error: 1.0088

``

1056/Unknown 231s 213ms/step - loss: 1.6683 - mean\_absolute\_error: 1.0087

``

1057/Unknown 231s 213ms/step - loss: 1.6680 - mean\_absolute\_error: 1.0086

``

1058/Unknown 232s 213ms/step - loss: 1.6676 - mean\_absolute\_error: 1.0085

``

1059/Unknown 232s 213ms/step - loss: 1.6672 - mean\_absolute\_error: 1.0084

``

1060/Unknown 232s 213ms/step - loss: 1.6669 - mean\_absolute\_error: 1.0083

``

1061/Unknown 232s 213ms/step - loss: 1.6665 - mean\_absolute\_error: 1.0082

``

1062/Unknown 233s 213ms/step - loss: 1.6662 - mean\_absolute\_error: 1.0081

``

1063/Unknown 233s 213ms/step - loss: 1.6658 - mean\_absolute\_error: 1.0080

``

1064/Unknown 233s 213ms/step - loss: 1.6654 - mean\_absolute\_error: 1.0079

``

1065/Unknown 233s 213ms/step - loss: 1.6651 - mean\_absolute\_error: 1.0078

``

1066/Unknown 234s 213ms/step - loss: 1.6647 - mean\_absolute\_error: 1.0077

``

1067/Unknown 234s 213ms/step - loss: 1.6644 - mean\_absolute\_error: 1.0076

``

1068/Unknown 234s 213ms/step - loss: 1.6640 - mean\_absolute\_error: 1.0075

``

1069/Unknown 234s 213ms/step - loss: 1.6637 - mean\_absolute\_error: 1.0074

``

1070/Unknown 234s 213ms/step - loss: 1.6633 - mean\_absolute\_error: 1.0073

``

1071/Unknown 235s 213ms/step - loss: 1.6629 - mean\_absolute\_error: 1.0072

``

1072/Unknown 235s 213ms/step - loss: 1.6626 - mean\_absolute\_error: 1.0071

``

1073/Unknown 235s 213ms/step - loss: 1.6622 - mean\_absolute\_error: 1.0070

``

1074/Unknown 236s 213ms/step - loss: 1.6619 - mean\_absolute\_error: 1.0069

``

1075/Unknown 236s 213ms/step - loss: 1.6615 - mean\_absolute\_error: 1.0068

``

1076/Unknown 236s 213ms/step - loss: 1.6612 - mean\_absolute\_error: 1.0067

``

1077/Unknown 236s 213ms/step - loss: 1.6608 - mean\_absolute\_error: 1.0066

``

1078/Unknown 237s 213ms/step - loss: 1.6605 - mean\_absolute\_error: 1.0065

``

1079/Unknown 237s 213ms/step - loss: 1.6601 - mean\_absolute\_error: 1.0064

``

1080/Unknown 237s 213ms/step - loss: 1.6598 - mean\_absolute\_error: 1.0063

``

1081/Unknown 237s 214ms/step - loss: 1.6594 - mean\_absolute\_error: 1.0062

``

1082/Unknown 238s 214ms/step - loss: 1.6591 - mean\_absolute\_error: 1.0061

``

1083/Unknown 238s 214ms/step - loss: 1.6587 - mean\_absolute\_error: 1.0060

``

1084/Unknown 238s 214ms/step - loss: 1.6584 - mean\_absolute\_error: 1.0059

``

1085/Unknown 238s 214ms/step - loss: 1.6580 - mean\_absolute\_error: 1.0058

``

1086/Unknown 239s 214ms/step - loss: 1.6577 - mean\_absolute\_error: 1.0057

``

1087/Unknown 239s 214ms/step - loss: 1.6573 - mean\_absolute\_error: 1.0056

``

1088/Unknown 239s 214ms/step - loss: 1.6570 - mean\_absolute\_error: 1.0055

``

1089/Unknown 239s 214ms/step - loss: 1.6566 - mean\_absolute\_error: 1.0054

``

1090/Unknown 240s 214ms/step - loss: 1.6563 - mean\_absolute\_error: 1.0053

``

1091/Unknown 240s 214ms/step - loss: 1.6559 - mean\_absolute\_error: 1.0052

``

1092/Unknown 240s 214ms/step - loss: 1.6556 - mean\_absolute\_error: 1.0051

``

1093/Unknown 240s 214ms/step - loss: 1.6552 - mean\_absolute\_error: 1.0050

``

1094/Unknown 241s 214ms/step - loss: 1.6549 - mean\_absolute\_error: 1.0049

``

1095/Unknown 241s 214ms/step - loss: 1.6546 - mean\_absolute\_error: 1.0048

``

1096/Unknown 241s 214ms/step - loss: 1.6542 - mean\_absolute\_error: 1.0047

``

1097/Unknown 241s 214ms/step - loss: 1.6539 - mean\_absolute\_error: 1.0046

``

1098/Unknown 241s 214ms/step - loss: 1.6535 - mean\_absolute\_error: 1.0045

``

1099/Unknown 242s 214ms/step - loss: 1.6532 - mean\_absolute\_error: 1.0044

``

1100/Unknown 242s 214ms/step - loss: 1.6528 - mean\_absolute\_error: 1.0043

``

1101/Unknown 242s 214ms/step - loss: 1.6525 - mean\_absolute\_error: 1.0043

``

1102/Unknown 242s 214ms/step - loss: 1.6522 - mean\_absolute\_error: 1.0042

``

1103/Unknown 243s 214ms/step - loss: 1.6518 - mean\_absolute\_error: 1.0041

``

1104/Unknown 243s 214ms/step - loss: 1.6515 - mean\_absolute\_error: 1.0040

``

1105/Unknown 243s 214ms/step - loss: 1.6511 - mean\_absolute\_error: 1.0039

``

1106/Unknown 243s 214ms/step - loss: 1.6508 - mean\_absolute\_error: 1.0038

``

1107/Unknown 244s 214ms/step - loss: 1.6505 - mean\_absolute\_error: 1.0037

``

1108/Unknown 244s 214ms/step - loss: 1.6501 - mean\_absolute\_error: 1.0036

``

1109/Unknown 244s 214ms/step - loss: 1.6498 - mean\_absolute\_error: 1.0035

``

1110/Unknown 244s 214ms/step - loss: 1.6494 - mean\_absolute\_error: 1.0034

``

1111/Unknown 245s 214ms/step - loss: 1.6491 - mean\_absolute\_error: 1.0033

``

1112/Unknown 245s 214ms/step - loss: 1.6488 - mean\_absolute\_error: 1.0032

``

1113/Unknown 245s 214ms/step - loss: 1.6484 - mean\_absolute\_error: 1.0031

``

1114/Unknown 245s 214ms/step - loss: 1.6481 - mean\_absolute\_error: 1.0030

``

1115/Unknown 246s 214ms/step - loss: 1.6478 - mean\_absolute\_error: 1.0029

``

1116/Unknown 246s 214ms/step - loss: 1.6474 - mean\_absolute\_error: 1.0028

``

1117/Unknown 246s 215ms/step - loss: 1.6471 - mean\_absolute\_error: 1.0027

``

1118/Unknown 247s 215ms/step - loss: 1.6468 - mean\_absolute\_error: 1.0026

``

1119/Unknown 247s 215ms/step - loss: 1.6464 - mean\_absolute\_error: 1.0025

``

1120/Unknown 247s 215ms/step - loss: 1.6461 - mean\_absolute\_error: 1.0024

``

1121/Unknown 247s 215ms/step - loss: 1.6458 - mean\_absolute\_error: 1.0023

``

1122/Unknown 248s 215ms/step - loss: 1.6454 - mean\_absolute\_error: 1.0022

``

1123/Unknown 248s 215ms/step - loss: 1.6451 - mean\_absolute\_error: 1.0022

``

1124/Unknown 248s 215ms/step - loss: 1.6448 - mean\_absolute\_error: 1.0021

``

1125/Unknown 248s 215ms/step - loss: 1.6444 - mean\_absolute\_error: 1.0020

``

1126/Unknown 249s 215ms/step - loss: 1.6441 - mean\_absolute\_error: 1.0019

``

1127/Unknown 249s 215ms/step - loss: 1.6438 - mean\_absolute\_error: 1.0018

``

1128/Unknown 249s 215ms/step - loss: 1.6434 - mean\_absolute\_error: 1.0017

``

1129/Unknown 249s 215ms/step - loss: 1.6431 - mean\_absolute\_error: 1.0016

``

1130/Unknown 249s 215ms/step - loss: 1.6428 - mean\_absolute\_error: 1.0015

``

1131/Unknown 250s 215ms/step - loss: 1.6425 - mean\_absolute\_error: 1.0014

``

1132/Unknown 250s 215ms/step - loss: 1.6421 - mean\_absolute\_error: 1.0013

``

1133/Unknown 250s 215ms/step - loss: 1.6418 - mean\_absolute\_error: 1.0012

``

1134/Unknown 250s 215ms/step - loss: 1.6415 - mean\_absolute\_error: 1.0011

``

1135/Unknown 251s 215ms/step - loss: 1.6411 - mean\_absolute\_error: 1.0010

``

1136/Unknown 251s 215ms/step - loss: 1.6408 - mean\_absolute\_error: 1.0009

``

1137/Unknown 251s 215ms/step - loss: 1.6405 - mean\_absolute\_error: 1.0008

``

1138/Unknown 251s 215ms/step - loss: 1.6402 - mean\_absolute\_error: 1.0008

``

1139/Unknown 251s 215ms/step - loss: 1.6398 - mean\_absolute\_error: 1.0007

``

1140/Unknown 252s 215ms/step - loss: 1.6395 - mean\_absolute\_error: 1.0006

``

1141/Unknown 252s 215ms/step - loss: 1.6392 - mean\_absolute\_error: 1.0005

``

1142/Unknown 252s 215ms/step - loss: 1.6389 - mean\_absolute\_error: 1.0004

``

1143/Unknown 252s 215ms/step - loss: 1.6385 - mean\_absolute\_error: 1.0003

``

1144/Unknown 253s 215ms/step - loss: 1.6382 - mean\_absolute\_error: 1.0002

``

1145/Unknown 253s 215ms/step - loss: 1.6379 - mean\_absolute\_error: 1.0001

``

1146/Unknown 253s 215ms/step - loss: 1.6376 - mean\_absolute\_error: 1.0000

``

1147/Unknown 253s 215ms/step - loss: 1.6373 - mean\_absolute\_error: 0.9999

``

1148/Unknown 254s 215ms/step - loss: 1.6369 - mean\_absolute\_error: 0.9998

``

1149/Unknown 254s 215ms/step - loss: 1.6366 - mean\_absolute\_error: 0.9997

``

1150/Unknown 254s 215ms/step - loss: 1.6363 - mean\_absolute\_error: 0.9997

``

1151/Unknown 254s 215ms/step - loss: 1.6360 - mean\_absolute\_error: 0.9996

``

1152/Unknown 255s 215ms/step - loss: 1.6356 - mean\_absolute\_error: 0.9995

``

1153/Unknown 255s 215ms/step - loss: 1.6353 - mean\_absolute\_error: 0.9994

``

1154/Unknown 255s 215ms/step - loss: 1.6350 - mean\_absolute\_error: 0.9993

``

1155/Unknown 255s 215ms/step - loss: 1.6347 - mean\_absolute\_error: 0.9992

``

1156/Unknown 256s 215ms/step - loss: 1.6344 - mean\_absolute\_error: 0.9991

``

1157/Unknown 256s 215ms/step - loss: 1.6341 - mean\_absolute\_error: 0.9990

``

1158/Unknown 256s 215ms/step - loss: 1.6337 - mean\_absolute\_error: 0.9989

``

1159/Unknown 256s 215ms/step - loss: 1.6334 - mean\_absolute\_error: 0.9988

``

1160/Unknown 257s 215ms/step - loss: 1.6331 - mean\_absolute\_error: 0.9987

``

1161/Unknown 257s 215ms/step - loss: 1.6328 - mean\_absolute\_error: 0.9987

``

1162/Unknown 257s 215ms/step - loss: 1.6325 - mean\_absolute\_error: 0.9986

``

1163/Unknown 257s 216ms/step - loss: 1.6322 - mean\_absolute\_error: 0.9985

``

1164/Unknown 257s 216ms/step - loss: 1.6318 - mean\_absolute\_error: 0.9984

``

1165/Unknown 258s 215ms/step - loss: 1.6315 - mean\_absolute\_error: 0.9983

``

1166/Unknown 258s 215ms/step - loss: 1.6312 - mean\_absolute\_error: 0.9982

``

1167/Unknown 258s 215ms/step - loss: 1.6309 - mean\_absolute\_error: 0.9981

``

1168/Unknown 258s 215ms/step - loss: 1.6306 - mean\_absolute\_error: 0.9980

``

1169/Unknown 259s 215ms/step - loss: 1.6303 - mean\_absolute\_error: 0.9979

``

1170/Unknown 259s 215ms/step - loss: 1.6300 - mean\_absolute\_error: 0.9979

``

1171/Unknown 259s 216ms/step - loss: 1.6297 - mean\_absolute\_error: 0.9978

``

1172/Unknown 259s 216ms/step - loss: 1.6293 - mean\_absolute\_error: 0.9977

``

1173/Unknown 259s 216ms/step - loss: 1.6290 - mean\_absolute\_error: 0.9976

``

1174/Unknown 260s 216ms/step - loss: 1.6287 - mean\_absolute\_error: 0.9975

``

1175/Unknown 260s 216ms/step - loss: 1.6284 - mean\_absolute\_error: 0.9974

``

1176/Unknown 260s 216ms/step - loss: 1.6281 - mean\_absolute\_error: 0.9973

``

1177/Unknown 260s 216ms/step - loss: 1.6278 - mean\_absolute\_error: 0.9972

``

1178/Unknown 261s 216ms/step - loss: 1.6275 - mean\_absolute\_error: 0.9971

``

1179/Unknown 261s 216ms/step - loss: 1.6272 - mean\_absolute\_error: 0.9971

``

1180/Unknown 261s 216ms/step - loss: 1.6269 - mean\_absolute\_error: 0.9970

``

1181/Unknown 261s 216ms/step - loss: 1.6266 - mean\_absolute\_error: 0.9969

``

1182/Unknown 262s 216ms/step - loss: 1.6263 - mean\_absolute\_error: 0.9968

``

1183/Unknown 262s 216ms/step - loss: 1.6259 - mean\_absolute\_error: 0.9967

``

1184/Unknown 262s 216ms/step - loss: 1.6256 - mean\_absolute\_error: 0.9966

``

1185/Unknown 262s 216ms/step - loss: 1.6253 - mean\_absolute\_error: 0.9965

``

1186/Unknown 263s 216ms/step - loss: 1.6250 - mean\_absolute\_error: 0.9964

``

1187/Unknown 263s 216ms/step - loss: 1.6247 - mean\_absolute\_error: 0.9964

``

1188/Unknown 263s 216ms/step - loss: 1.6244 - mean\_absolute\_error: 0.9963

``

1189/Unknown 263s 216ms/step - loss: 1.6241 - mean\_absolute\_error: 0.9962

``

1190/Unknown 264s 216ms/step - loss: 1.6238 - mean\_absolute\_error: 0.9961

``

1191/Unknown 264s 216ms/step - loss: 1.6235 - mean\_absolute\_error: 0.9960

``

1192/Unknown 264s 216ms/step - loss: 1.6232 - mean\_absolute\_error: 0.9959

``

1193/Unknown 264s 216ms/step - loss: 1.6229 - mean\_absolute\_error: 0.9958

``

1194/Unknown 264s 216ms/step - loss: 1.6226 - mean\_absolute\_error: 0.9957

``

1195/Unknown 265s 216ms/step - loss: 1.6223 - mean\_absolute\_error: 0.9957

``

1196/Unknown 265s 216ms/step - loss: 1.6220 - mean\_absolute\_error: 0.9956

``

1197/Unknown 265s 216ms/step - loss: 1.6217 - mean\_absolute\_error: 0.9955

``

1198/Unknown 265s 216ms/step - loss: 1.6214 - mean\_absolute\_error: 0.9954

``

1199/Unknown 266s 216ms/step - loss: 1.6211 - mean\_absolute\_error: 0.9953

``

1200/Unknown 266s 216ms/step - loss: 1.6208 - mean\_absolute\_error: 0.9952

``

1201/Unknown 266s 216ms/step - loss: 1.6205 - mean\_absolute\_error: 0.9951

``

1202/Unknown 267s 216ms/step - loss: 1.6202 - mean\_absolute\_error: 0.9951

``

1203/Unknown 267s 216ms/step - loss: 1.6199 - mean\_absolute\_error: 0.9950

``

1204/Unknown 267s 216ms/step - loss: 1.6196 - mean\_absolute\_error: 0.9949

``

1205/Unknown 267s 216ms/step - loss: 1.6193 - mean\_absolute\_error: 0.9948

``

1206/Unknown 267s 216ms/step - loss: 1.6190 - mean\_absolute\_error: 0.9947

``

1207/Unknown 268s 216ms/step - loss: 1.6187 - mean\_absolute\_error: 0.9946

``

1208/Unknown 268s 216ms/step - loss: 1.6184 - mean\_absolute\_error: 0.9945

``

1209/Unknown 268s 216ms/step - loss: 1.6181 - mean\_absolute\_error: 0.9945

``

1210/Unknown 268s 216ms/step - loss: 1.6178 - mean\_absolute\_error: 0.9944

``

1211/Unknown 269s 216ms/step - loss: 1.6175 - mean\_absolute\_error: 0.9943

``

1212/Unknown 269s 216ms/step - loss: 1.6172 - mean\_absolute\_error: 0.9942

``

1213/Unknown 269s 216ms/step - loss: 1.6169 - mean\_absolute\_error: 0.9941

``

1214/Unknown 269s 216ms/step - loss: 1.6166 - mean\_absolute\_error: 0.9940

``

1215/Unknown 270s 216ms/step - loss: 1.6163 - mean\_absolute\_error: 0.9940

``

1216/Unknown 270s 216ms/step - loss: 1.6160 - mean\_absolute\_error: 0.9939

``

1217/Unknown 270s 216ms/step - loss: 1.6157 - mean\_absolute\_error: 0.9938

``

1218/Unknown 270s 216ms/step - loss: 1.6155 - mean\_absolute\_error: 0.9937

``

1219/Unknown 270s 216ms/step - loss: 1.6152 - mean\_absolute\_error: 0.9936

``

1220/Unknown 271s 216ms/step - loss: 1.6149 - mean\_absolute\_error: 0.9935

``

1221/Unknown 271s 216ms/step - loss: 1.6146 - mean\_absolute\_error: 0.9935

``

1222/Unknown 271s 217ms/step - loss: 1.6143 - mean\_absolute\_error: 0.9934

``

1223/Unknown 272s 217ms/step - loss: 1.6140 - mean\_absolute\_error: 0.9933

``

1224/Unknown 272s 217ms/step - loss: 1.6137 - mean\_absolute\_error: 0.9932

``

1225/Unknown 272s 217ms/step - loss: 1.6134 - mean\_absolute\_error: 0.9931

``

1226/Unknown 272s 217ms/step - loss: 1.6131 - mean\_absolute\_error: 0.9930

``

1227/Unknown 273s 217ms/step - loss: 1.6128 - mean\_absolute\_error: 0.9930

``

1228/Unknown 273s 217ms/step - loss: 1.6125 - mean\_absolute\_error: 0.9929

``

1229/Unknown 273s 217ms/step - loss: 1.6122 - mean\_absolute\_error: 0.9928

``

1230/Unknown 273s 217ms/step - loss: 1.6120 - mean\_absolute\_error: 0.9927

``

1231/Unknown 273s 217ms/step - loss: 1.6117 - mean\_absolute\_error: 0.9926

``

1232/Unknown 274s 217ms/step - loss: 1.6114 - mean\_absolute\_error: 0.9925

``

1233/Unknown 274s 217ms/step - loss: 1.6111 - mean\_absolute\_error: 0.9925

``

1234/Unknown 274s 217ms/step - loss: 1.6108 - mean\_absolute\_error: 0.9924

``

1235/Unknown 274s 217ms/step - loss: 1.6105 - mean\_absolute\_error: 0.9923

``

1236/Unknown 274s 217ms/step - loss: 1.6102 - mean\_absolute\_error: 0.9922

``

1237/Unknown 275s 217ms/step - loss: 1.6099 - mean\_absolute\_error: 0.9921

``

1238/Unknown 275s 217ms/step - loss: 1.6097 - mean\_absolute\_error: 0.9920

``

1239/Unknown 275s 217ms/step - loss: 1.6094 - mean\_absolute\_error: 0.9920

``

1240/Unknown 275s 217ms/step - loss: 1.6091 - mean\_absolute\_error: 0.9919

``

1241/Unknown 276s 217ms/step - loss: 1.6088 - mean\_absolute\_error: 0.9918

``

1242/Unknown 276s 217ms/step - loss: 1.6085 - mean\_absolute\_error: 0.9917

``

1243/Unknown 276s 217ms/step - loss: 1.6082 - mean\_absolute\_error: 0.9916

``

1244/Unknown 276s 217ms/step - loss: 1.6080 - mean\_absolute\_error: 0.9916

``

1245/Unknown 276s 217ms/step - loss: 1.6077 - mean\_absolute\_error: 0.9915

``

1246/Unknown 277s 217ms/step - loss: 1.6074 - mean\_absolute\_error: 0.9914

``

1247/Unknown 277s 217ms/step - loss: 1.6071 - mean\_absolute\_error: 0.9913

``

1248/Unknown 277s 217ms/step - loss: 1.6068 - mean\_absolute\_error: 0.9912

``

1249/Unknown 277s 217ms/step - loss: 1.6065 - mean\_absolute\_error: 0.9912

``

1250/Unknown 278s 217ms/step - loss: 1.6063 - mean\_absolute\_error: 0.9911

``

1251/Unknown 278s 217ms/step - loss: 1.6060 - mean\_absolute\_error: 0.9910

``

1252/Unknown 278s 217ms/step - loss: 1.6057 - mean\_absolute\_error: 0.9909

``

1253/Unknown 278s 217ms/step - loss: 1.6054 - mean\_absolute\_error: 0.9908

``

1254/Unknown 279s 217ms/step - loss: 1.6051 - mean\_absolute\_error: 0.9908

``

1255/Unknown 279s 217ms/step - loss: 1.6049 - mean\_absolute\_error: 0.9907

``

1256/Unknown 279s 217ms/step - loss: 1.6046 - mean\_absolute\_error: 0.9906

``

1257/Unknown 279s 217ms/step - loss: 1.6043 - mean\_absolute\_error: 0.9905

``

1258/Unknown 279s 217ms/step - loss: 1.6040 - mean\_absolute\_error: 0.9904

``

1259/Unknown 280s 217ms/step - loss: 1.6037 - mean\_absolute\_error: 0.9904

``

1260/Unknown 280s 217ms/step - loss: 1.6035 - mean\_absolute\_error: 0.9903

``

1261/Unknown 280s 217ms/step - loss: 1.6032 - mean\_absolute\_error: 0.9902

``

1262/Unknown 280s 217ms/step - loss: 1.6029 - mean\_absolute\_error: 0.9901

``

1263/Unknown 281s 217ms/step - loss: 1.6026 - mean\_absolute\_error: 0.9900

``

1264/Unknown 281s 217ms/step - loss: 1.6024 - mean\_absolute\_error: 0.9900

``

1265/Unknown 281s 217ms/step - loss: 1.6021 - mean\_absolute\_error: 0.9899

``

1266/Unknown 281s 217ms/step - loss: 1.6018 - mean\_absolute\_error: 0.9898

``

1267/Unknown 281s 217ms/step - loss: 1.6015 - mean\_absolute\_error: 0.9897

``

1268/Unknown 282s 217ms/step - loss: 1.6013 - mean\_absolute\_error: 0.9896

``

1269/Unknown 282s 217ms/step - loss: 1.6010 - mean\_absolute\_error: 0.9896

``

1270/Unknown 282s 217ms/step - loss: 1.6007 - mean\_absolute\_error: 0.9895

``

1271/Unknown 282s 217ms/step - loss: 1.6004 - mean\_absolute\_error: 0.9894

``

1272/Unknown 283s 217ms/step - loss: 1.6002 - mean\_absolute\_error: 0.9893

``

1273/Unknown 283s 217ms/step - loss: 1.5999 - mean\_absolute\_error: 0.9892

``

1274/Unknown 283s 217ms/step - loss: 1.5996 - mean\_absolute\_error: 0.9892

``

1275/Unknown 283s 217ms/step - loss: 1.5993 - mean\_absolute\_error: 0.9891

``

1276/Unknown 283s 217ms/step - loss: 1.5991 - mean\_absolute\_error: 0.9890

``

1277/Unknown 284s 217ms/step - loss: 1.5988 - mean\_absolute\_error: 0.9889

``

1278/Unknown 284s 217ms/step - loss: 1.5985 - mean\_absolute\_error: 0.9889

``

1279/Unknown 284s 217ms/step - loss: 1.5983 - mean\_absolute\_error: 0.9888

``

1280/Unknown 284s 217ms/step - loss: 1.5980 - mean\_absolute\_error: 0.9887

``

1281/Unknown 285s 217ms/step - loss: 1.5977 - mean\_absolute\_error: 0.9886

``

1282/Unknown 285s 217ms/step - loss: 1.5974 - mean\_absolute\_error: 0.9885

``

1283/Unknown 285s 217ms/step - loss: 1.5972 - mean\_absolute\_error: 0.9885

``

1284/Unknown 285s 217ms/step - loss: 1.5969 - mean\_absolute\_error: 0.9884

``

1285/Unknown 285s 217ms/step - loss: 1.5966 - mean\_absolute\_error: 0.9883

``

1286/Unknown 286s 217ms/step - loss: 1.5964 - mean\_absolute\_error: 0.9882

``

1287/Unknown 286s 217ms/step - loss: 1.5961 - mean\_absolute\_error: 0.9882

``

1288/Unknown 286s 217ms/step - loss: 1.5958 - mean\_absolute\_error: 0.9881

``

1289/Unknown 286s 217ms/step - loss: 1.5956 - mean\_absolute\_error: 0.9880

``

1290/Unknown 286s 217ms/step - loss: 1.5953 - mean\_absolute\_error: 0.9879

``

1291/Unknown 287s 217ms/step - loss: 1.5950 - mean\_absolute\_error: 0.9879

``

1292/Unknown 287s 217ms/step - loss: 1.5948 - mean\_absolute\_error: 0.9878

``

1293/Unknown 287s 217ms/step - loss: 1.5945 - mean\_absolute\_error: 0.9877

``

1294/Unknown 287s 217ms/step - loss: 1.5942 - mean\_absolute\_error: 0.9876

``

1295/Unknown 288s 217ms/step - loss: 1.5940 - mean\_absolute\_error: 0.9875

``

1296/Unknown 288s 217ms/step - loss: 1.5937 - mean\_absolute\_error: 0.9875

``

1297/Unknown 288s 217ms/step - loss: 1.5934 - mean\_absolute\_error: 0.9874

``

1298/Unknown 288s 217ms/step - loss: 1.5932 - mean\_absolute\_error: 0.9873

``

1299/Unknown 288s 217ms/step - loss: 1.5929 - mean\_absolute\_error: 0.9872

``

1300/Unknown 289s 217ms/step - loss: 1.5926 - mean\_absolute\_error: 0.9872

``

1301/Unknown 289s 217ms/step - loss: 1.5924 - mean\_absolute\_error: 0.9871

``

1302/Unknown 289s 217ms/step - loss: 1.5921 - mean\_absolute\_error: 0.9870

``

1303/Unknown 289s 217ms/step - loss: 1.5918 - mean\_absolute\_error: 0.9869

``

1304/Unknown 289s 217ms/step - loss: 1.5916 - mean\_absolute\_error: 0.9869

``

1305/Unknown 290s 217ms/step - loss: 1.5913 - mean\_absolute\_error: 0.9868

``

1306/Unknown 290s 217ms/step - loss: 1.5910 - mean\_absolute\_error: 0.9867

``

1307/Unknown 290s 217ms/step - loss: 1.5908 - mean\_absolute\_error: 0.9866

``

1308/Unknown 290s 217ms/step - loss: 1.5905 - mean\_absolute\_error: 0.9866

``

1309/Unknown 290s 217ms/step - loss: 1.5903 - mean\_absolute\_error: 0.9865

``

1310/Unknown 291s 217ms/step - loss: 1.5900 - mean\_absolute\_error: 0.9864

``

1311/Unknown 291s 217ms/step - loss: 1.5897 - mean\_absolute\_error: 0.9863

``

1312/Unknown 291s 217ms/step - loss: 1.5895 - mean\_absolute\_error: 0.9863

``

1313/Unknown 291s 217ms/step - loss: 1.5892 - mean\_absolute\_error: 0.9862

``

1314/Unknown 291s 217ms/step - loss: 1.5890 - mean\_absolute\_error: 0.9861

``

1315/Unknown 292s 217ms/step - loss: 1.5887 - mean\_absolute\_error: 0.9860

``

1316/Unknown 292s 217ms/step - loss: 1.5884 - mean\_absolute\_error: 0.9860

``

1317/Unknown 292s 217ms/step - loss: 1.5882 - mean\_absolute\_error: 0.9859

``

1318/Unknown 292s 217ms/step - loss: 1.5879 - mean\_absolute\_error: 0.9858

``

1319/Unknown 293s 217ms/step - loss: 1.5877 - mean\_absolute\_error: 0.9857

``

1320/Unknown 293s 217ms/step - loss: 1.5874 - mean\_absolute\_error: 0.9857

``

1321/Unknown 293s 217ms/step - loss: 1.5871 - mean\_absolute\_error: 0.9856

``

1322/Unknown 293s 217ms/step - loss: 1.5869 - mean\_absolute\_error: 0.9855

``

1323/Unknown 293s 217ms/step - loss: 1.5866 - mean\_absolute\_error: 0.9854

``

1324/Unknown 294s 217ms/step - loss: 1.5864 - mean\_absolute\_error: 0.9854

``

1325/Unknown 294s 217ms/step - loss: 1.5861 - mean\_absolute\_error: 0.9853

``

1326/Unknown 294s 217ms/step - loss: 1.5858 - mean\_absolute\_error: 0.9852

``

1327/Unknown 294s 217ms/step - loss: 1.5856 - mean\_absolute\_error: 0.9851

``

1328/Unknown 295s 217ms/step - loss: 1.5853 - mean\_absolute\_error: 0.9851

``

1329/Unknown 295s 217ms/step - loss: 1.5851 - mean\_absolute\_error: 0.9850

``

1330/Unknown 295s 217ms/step - loss: 1.5848 - mean\_absolute\_error: 0.9849

``

1331/Unknown 295s 217ms/step - loss: 1.5846 - mean\_absolute\_error: 0.9848

``

1332/Unknown 295s 217ms/step - loss: 1.5843 - mean\_absolute\_error: 0.9848

``

1333/Unknown 296s 217ms/step - loss: 1.5841 - mean\_absolute\_error: 0.9847

``

1334/Unknown 296s 217ms/step - loss: 1.5838 - mean\_absolute\_error: 0.9846

``

1335/Unknown 296s 217ms/step - loss: 1.5836 - mean\_absolute\_error: 0.9846

``

1336/Unknown 296s 217ms/step - loss: 1.5833 - mean\_absolute\_error: 0.9845

``

1337/Unknown 297s 217ms/step - loss: 1.5830 - mean\_absolute\_error: 0.9844

``

1338/Unknown 297s 217ms/step - loss: 1.5828 - mean\_absolute\_error: 0.9843

``

1339/Unknown 297s 217ms/step - loss: 1.5825 - mean\_absolute\_error: 0.9843

``

1340/Unknown 297s 217ms/step - loss: 1.5823 - mean\_absolute\_error: 0.9842

``

1341/Unknown 297s 217ms/step - loss: 1.5820 - mean\_absolute\_error: 0.9841

``

1342/Unknown 297s 217ms/step - loss: 1.5818 - mean\_absolute\_error: 0.9840

``

1343/Unknown 298s 217ms/step - loss: 1.5815 - mean\_absolute\_error: 0.9840

``

1344/Unknown 298s 217ms/step - loss: 1.5813 - mean\_absolute\_error: 0.9839

``

1345/Unknown 298s 217ms/step - loss: 1.5810 - mean\_absolute\_error: 0.9838

``

1346/Unknown 298s 217ms/step - loss: 1.5808 - mean\_absolute\_error: 0.9838

``

1347/Unknown 298s 217ms/step - loss: 1.5805 - mean\_absolute\_error: 0.9837

``

1348/Unknown 299s 217ms/step - loss: 1.5803 - mean\_absolute\_error: 0.9836

``

1349/Unknown 299s 217ms/step - loss: 1.5800 - mean\_absolute\_error: 0.9835

``

1350/Unknown 299s 217ms/step - loss: 1.5798 - mean\_absolute\_error: 0.9835

``

1351/Unknown 299s 217ms/step - loss: 1.5795 - mean\_absolute\_error: 0.9834

``

1352/Unknown 300s 217ms/step - loss: 1.5793 - mean\_absolute\_error: 0.9833

``

1353/Unknown 300s 217ms/step - loss: 1.5790 - mean\_absolute\_error: 0.9833

``

1354/Unknown 300s 217ms/step - loss: 1.5788 - mean\_absolute\_error: 0.9832

``

1355/Unknown 300s 217ms/step - loss: 1.5785 - mean\_absolute\_error: 0.9831

``

1356/Unknown 300s 217ms/step - loss: 1.5783 - mean\_absolute\_error: 0.9830

``

1357/Unknown 301s 217ms/step - loss: 1.5781 - mean\_absolute\_error: 0.9830

``

1358/Unknown 301s 217ms/step - loss: 1.5778 - mean\_absolute\_error: 0.9829

``

1359/Unknown 301s 217ms/step - loss: 1.5776 - mean\_absolute\_error: 0.9828

``

1360/Unknown 301s 217ms/step - loss: 1.5773 - mean\_absolute\_error: 0.9828

``

1361/Unknown 301s 217ms/step - loss: 1.5771 - mean\_absolute\_error: 0.9827

``

1362/Unknown 302s 217ms/step - loss: 1.5768 - mean\_absolute\_error: 0.9826

``

1363/Unknown 302s 217ms/step - loss: 1.5766 - mean\_absolute\_error: 0.9825

``

1364/Unknown 302s 217ms/step - loss: 1.5763 - mean\_absolute\_error: 0.9825

``

1365/Unknown 302s 217ms/step - loss: 1.5761 - mean\_absolute\_error: 0.9824

``

1366/Unknown 303s 217ms/step - loss: 1.5759 - mean\_absolute\_error: 0.9823

``

1367/Unknown 303s 217ms/step - loss: 1.5756 - mean\_absolute\_error: 0.9823

``

1368/Unknown 303s 217ms/step - loss: 1.5754 - mean\_absolute\_error: 0.9822

``

1369/Unknown 303s 217ms/step - loss: 1.5751 - mean\_absolute\_error: 0.9821

``

1370/Unknown 304s 217ms/step - loss: 1.5749 - mean\_absolute\_error: 0.9821

``

1371/Unknown 304s 217ms/step - loss: 1.5746 - mean\_absolute\_error: 0.9820

``

1372/Unknown 304s 217ms/step - loss: 1.5744 - mean\_absolute\_error: 0.9819

``

1373/Unknown 304s 217ms/step - loss: 1.5742 - mean\_absolute\_error: 0.9818

``

1374/Unknown 304s 217ms/step - loss: 1.5739 - mean\_absolute\_error: 0.9818

``

1375/Unknown 305s 217ms/step - loss: 1.5737 - mean\_absolute\_error: 0.9817

``

1376/Unknown 305s 217ms/step - loss: 1.5734 - mean\_absolute\_error: 0.9816

``

1377/Unknown 305s 217ms/step - loss: 1.5732 - mean\_absolute\_error: 0.9816

``

1378/Unknown 305s 217ms/step - loss: 1.5729 - mean\_absolute\_error: 0.9815

``

1379/Unknown 305s 217ms/step - loss: 1.5727 - mean\_absolute\_error: 0.9814

``

1380/Unknown 306s 217ms/step - loss: 1.5725 - mean\_absolute\_error: 0.9814

``

1381/Unknown 306s 217ms/step - loss: 1.5722 - mean\_absolute\_error: 0.9813

``

1382/Unknown 306s 217ms/step - loss: 1.5720 - mean\_absolute\_error: 0.9812

``

1383/Unknown 306s 217ms/step - loss: 1.5718 - mean\_absolute\_error: 0.9812

``

1384/Unknown 306s 217ms/step - loss: 1.5715 - mean\_absolute\_error: 0.9811

``

1385/Unknown 307s 217ms/step - loss: 1.5713 - mean\_absolute\_error: 0.9810

``

1386/Unknown 307s 217ms/step - loss: 1.5710 - mean\_absolute\_error: 0.9809

``

1387/Unknown 307s 217ms/step - loss: 1.5708 - mean\_absolute\_error: 0.9809

``

1388/Unknown 307s 217ms/step - loss: 1.5706 - mean\_absolute\_error: 0.9808

``

1389/Unknown 307s 217ms/step - loss: 1.5703 - mean\_absolute\_error: 0.9807

``

1390/Unknown 308s 217ms/step - loss: 1.5701 - mean\_absolute\_error: 0.9807

``

1391/Unknown 308s 217ms/step - loss: 1.5698 - mean\_absolute\_error: 0.9806

``

1392/Unknown 308s 217ms/step - loss: 1.5696 - mean\_absolute\_error: 0.9805

``

1393/Unknown 308s 217ms/step - loss: 1.5694 - mean\_absolute\_error: 0.9805

``

1394/Unknown 309s 217ms/step - loss: 1.5691 - mean\_absolute\_error: 0.9804

``

1395/Unknown 309s 217ms/step - loss: 1.5689 - mean\_absolute\_error: 0.9803

``

1396/Unknown 309s 217ms/step - loss: 1.5687 - mean\_absolute\_error: 0.9803

``

1397/Unknown 309s 217ms/step - loss: 1.5684 - mean\_absolute\_error: 0.9802

``

1398/Unknown 309s 217ms/step - loss: 1.5682 - mean\_absolute\_error: 0.9801

``

1399/Unknown 310s 217ms/step - loss: 1.5680 - mean\_absolute\_error: 0.9801

``

1400/Unknown 310s 217ms/step - loss: 1.5677 - mean\_absolute\_error: 0.9800

``

1401/Unknown 310s 217ms/step - loss: 1.5675 - mean\_absolute\_error: 0.9799

``

1402/Unknown 310s 217ms/step - loss: 1.5673 - mean\_absolute\_error: 0.9799

``

1403/Unknown 311s 217ms/step - loss: 1.5670 - mean\_absolute\_error: 0.9798

``

1404/Unknown 311s 217ms/step - loss: 1.5668 - mean\_absolute\_error: 0.9797

``

1405/Unknown 311s 217ms/step - loss: 1.5666 - mean\_absolute\_error: 0.9797

``

1406/Unknown 311s 217ms/step - loss: 1.5663 - mean\_absolute\_error: 0.9796

``

1407/Unknown 311s 217ms/step - loss: 1.5661 - mean\_absolute\_error: 0.9795

``

1408/Unknown 312s 217ms/step - loss: 1.5659 - mean\_absolute\_error: 0.9795

``

1409/Unknown 312s 217ms/step - loss: 1.5656 - mean\_absolute\_error: 0.9794

``

1410/Unknown 312s 217ms/step - loss: 1.5654 - mean\_absolute\_error: 0.9793

``

1411/Unknown 312s 217ms/step - loss: 1.5652 - mean\_absolute\_error: 0.9793

``

1412/Unknown 313s 217ms/step - loss: 1.5649 - mean\_absolute\_error: 0.9792

``

1413/Unknown 313s 217ms/step - loss: 1.5647 - mean\_absolute\_error: 0.9791

``

1414/Unknown 313s 217ms/step - loss: 1.5645 - mean\_absolute\_error: 0.9791

``

1415/Unknown 313s 217ms/step - loss: 1.5642 - mean\_absolute\_error: 0.9790

``

1416/Unknown 313s 217ms/step - loss: 1.5640 - mean\_absolute\_error: 0.9789

``

1417/Unknown 314s 217ms/step - loss: 1.5638 - mean\_absolute\_error: 0.9789

``

1418/Unknown 314s 217ms/step - loss: 1.5635 - mean\_absolute\_error: 0.9788

``

1419/Unknown 314s 217ms/step - loss: 1.5633 - mean\_absolute\_error: 0.9787

``

1420/Unknown 314s 217ms/step - loss: 1.5631 - mean\_absolute\_error: 0.9787

``

1421/Unknown 315s 217ms/step - loss: 1.5629 - mean\_absolute\_error: 0.9786

``

1422/Unknown 315s 217ms/step - loss: 1.5626 - mean\_absolute\_error: 0.9785

``

1423/Unknown 315s 217ms/step - loss: 1.5624 - mean\_absolute\_error: 0.9785

``

1424/Unknown 316s 217ms/step - loss: 1.5622 - mean\_absolute\_error: 0.9784

``

1425/Unknown 316s 217ms/step - loss: 1.5619 - mean\_absolute\_error: 0.9783

``

1426/Unknown 316s 217ms/step - loss: 1.5617 - mean\_absolute\_error: 0.9783

``

1427/Unknown 316s 217ms/step - loss: 1.5615 - mean\_absolute\_error: 0.9782

``

1428/Unknown 317s 217ms/step - loss: 1.5613 - mean\_absolute\_error: 0.9781

``

1429/Unknown 317s 217ms/step - loss: 1.5610 - mean\_absolute\_error: 0.9781

``

1430/Unknown 317s 217ms/step - loss: 1.5608 - mean\_absolute\_error: 0.9780

``

1431/Unknown 317s 217ms/step - loss: 1.5606 - mean\_absolute\_error: 0.9779

``

1432/Unknown 317s 217ms/step - loss: 1.5604 - mean\_absolute\_error: 0.9779

``

1433/Unknown 318s 217ms/step - loss: 1.5601 - mean\_absolute\_error: 0.9778

``

1434/Unknown 318s 217ms/step - loss: 1.5599 - mean\_absolute\_error: 0.9777

``

1435/Unknown 318s 217ms/step - loss: 1.5597 - mean\_absolute\_error: 0.9777

``

1436/Unknown 318s 217ms/step - loss: 1.5595 - mean\_absolute\_error: 0.9776

``

1437/Unknown 318s 217ms/step - loss: 1.5592 - mean\_absolute\_error: 0.9775

``

1438/Unknown 319s 217ms/step - loss: 1.5590 - mean\_absolute\_error: 0.9775

``

1439/Unknown 319s 217ms/step - loss: 1.5588 - mean\_absolute\_error: 0.9774

``

1440/Unknown 319s 217ms/step - loss: 1.5586 - mean\_absolute\_error: 0.9773

``

1441/Unknown 319s 217ms/step - loss: 1.5583 - mean\_absolute\_error: 0.9773

``

1442/Unknown 320s 217ms/step - loss: 1.5581 - mean\_absolute\_error: 0.9772

``

1443/Unknown 320s 217ms/step - loss: 1.5579 - mean\_absolute\_error: 0.9771

``

1444/Unknown 320s 217ms/step - loss: 1.5577 - mean\_absolute\_error: 0.9771

``

1445/Unknown 320s 217ms/step - loss: 1.5574 - mean\_absolute\_error: 0.9770

``

1446/Unknown 320s 217ms/step - loss: 1.5572 - mean\_absolute\_error: 0.9770

``

1447/Unknown 321s 217ms/step - loss: 1.5570 - mean\_absolute\_error: 0.9769

``

1448/Unknown 321s 217ms/step - loss: 1.5568 - mean\_absolute\_error: 0.9768

``

1449/Unknown 321s 217ms/step - loss: 1.5565 - mean\_absolute\_error: 0.9768

``

1450/Unknown 321s 217ms/step - loss: 1.5563 - mean\_absolute\_error: 0.9767

``

1451/Unknown 322s 217ms/step - loss: 1.5561 - mean\_absolute\_error: 0.9766

``

1452/Unknown 322s 217ms/step - loss: 1.5559 - mean\_absolute\_error: 0.9766

``

1453/Unknown 322s 217ms/step - loss: 1.5557 - mean\_absolute\_error: 0.9765

``

1454/Unknown 322s 217ms/step - loss: 1.5554 - mean\_absolute\_error: 0.9764

``

1455/Unknown 323s 217ms/step - loss: 1.5552 - mean\_absolute\_error: 0.9764

``

1456/Unknown 323s 217ms/step - loss: 1.5550 - mean\_absolute\_error: 0.9763

``

1457/Unknown 323s 217ms/step - loss: 1.5548 - mean\_absolute\_error: 0.9763

``

1458/Unknown 323s 217ms/step - loss: 1.5546 - mean\_absolute\_error: 0.9762

``

1459/Unknown 324s 217ms/step - loss: 1.5543 - mean\_absolute\_error: 0.9761

``

1460/Unknown 324s 217ms/step - loss: 1.5541 - mean\_absolute\_error: 0.9761

``

1461/Unknown 324s 217ms/step - loss: 1.5539 - mean\_absolute\_error: 0.9760

``

1462/Unknown 324s 217ms/step - loss: 1.5537 - mean\_absolute\_error: 0.9759

``

1463/Unknown 324s 217ms/step - loss: 1.5535 - mean\_absolute\_error: 0.9759

``

1464/Unknown 325s 217ms/step - loss: 1.5532 - mean\_absolute\_error: 0.9758

``

1465/Unknown 325s 217ms/step - loss: 1.5530 - mean\_absolute\_error: 0.9757

``

1466/Unknown 325s 217ms/step - loss: 1.5528 - mean\_absolute\_error: 0.9757

``

1467/Unknown 325s 217ms/step - loss: 1.5526 - mean\_absolute\_error: 0.9756

``

1468/Unknown 326s 217ms/step - loss: 1.5524 - mean\_absolute\_error: 0.9756

``

1469/Unknown 326s 217ms/step - loss: 1.5522 - mean\_absolute\_error: 0.9755

``

1470/Unknown 326s 217ms/step - loss: 1.5519 - mean\_absolute\_error: 0.9754

``

1471/Unknown 326s 217ms/step - loss: 1.5517 - mean\_absolute\_error: 0.9754

``

1472/Unknown 327s 217ms/step - loss: 1.5515 - mean\_absolute\_error: 0.9753

``

1473/Unknown 327s 217ms/step - loss: 1.5513 - mean\_absolute\_error: 0.9752

``

1474/Unknown 327s 217ms/step - loss: 1.5511 - mean\_absolute\_error: 0.9752

``

1475/Unknown 327s 217ms/step - loss: 1.5509 - mean\_absolute\_error: 0.9751

``

1476/Unknown 328s 218ms/step - loss: 1.5506 - mean\_absolute\_error: 0.9751

``

1477/Unknown 328s 218ms/step - loss: 1.5504 - mean\_absolute\_error: 0.9750

``

1478/Unknown 328s 218ms/step - loss: 1.5502 - mean\_absolute\_error: 0.9749

``

1479/Unknown 329s 218ms/step - loss: 1.5500 - mean\_absolute\_error: 0.9749

``

1480/Unknown 329s 218ms/step - loss: 1.5498 - mean\_absolute\_error: 0.9748

``

1481/Unknown 329s 218ms/step - loss: 1.5496 - mean\_absolute\_error: 0.9747

``

1482/Unknown 329s 218ms/step - loss: 1.5493 - mean\_absolute\_error: 0.9747

``

1483/Unknown 330s 218ms/step - loss: 1.5491 - mean\_absolute\_error: 0.9746

``

1484/Unknown 330s 218ms/step - loss: 1.5489 - mean\_absolute\_error: 0.9746

``

1485/Unknown 330s 218ms/step - loss: 1.5487 - mean\_absolute\_error: 0.9745

``

1486/Unknown 330s 218ms/step - loss: 1.5485 - mean\_absolute\_error: 0.9744

``

1487/Unknown 330s 218ms/step - loss: 1.5483 - mean\_absolute\_error: 0.9744

``

1488/Unknown 331s 218ms/step - loss: 1.5481 - mean\_absolute\_error: 0.9743

``

1489/Unknown 331s 218ms/step - loss: 1.5478 - mean\_absolute\_error: 0.9742

``

1490/Unknown 331s 218ms/step - loss: 1.5476 - mean\_absolute\_error: 0.9742

``

1491/Unknown 331s 218ms/step - loss: 1.5474 - mean\_absolute\_error: 0.9741

``

1492/Unknown 332s 218ms/step - loss: 1.5472 - mean\_absolute\_error: 0.9741

``

1493/Unknown 332s 218ms/step - loss: 1.5470 - mean\_absolute\_error: 0.9740

``

1494/Unknown 332s 218ms/step - loss: 1.5468 - mean\_absolute\_error: 0.9739

``

1495/Unknown 332s 218ms/step - loss: 1.5466 - mean\_absolute\_error: 0.9739

``

1496/Unknown 333s 218ms/step - loss: 1.5464 - mean\_absolute\_error: 0.9738

``

1497/Unknown 333s 218ms/step - loss: 1.5461 - mean\_absolute\_error: 0.9737

``

1498/Unknown 333s 218ms/step - loss: 1.5459 - mean\_absolute\_error: 0.9737

``

1499/Unknown 333s 218ms/step - loss: 1.5457 - mean\_absolute\_error: 0.9736

``

1500/Unknown 334s 218ms/step - loss: 1.5455 - mean\_absolute\_error: 0.9736

``

1501/Unknown 334s 218ms/step - loss: 1.5453 - mean\_absolute\_error: 0.9735

``

1502/Unknown 334s 218ms/step - loss: 1.5451 - mean\_absolute\_error: 0.9734

``

1503/Unknown 334s 218ms/step - loss: 1.5449 - mean\_absolute\_error: 0.9734

``

1504/Unknown 334s 218ms/step - loss: 1.5447 - mean\_absolute\_error: 0.9733

``

1505/Unknown 335s 218ms/step - loss: 1.5445 - mean\_absolute\_error: 0.9733

``

1506/Unknown 335s 218ms/step - loss: 1.5443 - mean\_absolute\_error: 0.9732

``

1507/Unknown 335s 218ms/step - loss: 1.5440 - mean\_absolute\_error: 0.9731

``

1508/Unknown 335s 218ms/step - loss: 1.5438 - mean\_absolute\_error: 0.9731

``

1509/Unknown 335s 218ms/step - loss: 1.5436 - mean\_absolute\_error: 0.9730

``

1510/Unknown 336s 218ms/step - loss: 1.5434 - mean\_absolute\_error: 0.9730

``

1511/Unknown 336s 218ms/step - loss: 1.5432 - mean\_absolute\_error: 0.9729

``

1512/Unknown 336s 218ms/step - loss: 1.5430 - mean\_absolute\_error: 0.9728

``

1513/Unknown 336s 218ms/step - loss: 1.5428 - mean\_absolute\_error: 0.9728

``

1514/Unknown 337s 218ms/step - loss: 1.5426 - mean\_absolute\_error: 0.9727

``

1515/Unknown 337s 218ms/step - loss: 1.5424 - mean\_absolute\_error: 0.9727

``

1516/Unknown 337s 218ms/step - loss: 1.5422 - mean\_absolute\_error: 0.9726

``

1517/Unknown 337s 218ms/step - loss: 1.5420 - mean\_absolute\_error: 0.9725

``

1518/Unknown 338s 218ms/step - loss: 1.5418 - mean\_absolute\_error: 0.9725

``

1519/Unknown 338s 218ms/step - loss: 1.5415 - mean\_absolute\_error: 0.9724

``

1520/Unknown 338s 218ms/step - loss: 1.5413 - mean\_absolute\_error: 0.9724

``

1521/Unknown 338s 218ms/step - loss: 1.5411 - mean\_absolute\_error: 0.9723

``

1522/Unknown 338s 218ms/step - loss: 1.5409 - mean\_absolute\_error: 0.9722

``

1523/Unknown 339s 218ms/step - loss: 1.5407 - mean\_absolute\_error: 0.9722

``

1524/Unknown 339s 218ms/step - loss: 1.5405 - mean\_absolute\_error: 0.9721

``

1525/Unknown 339s 218ms/step - loss: 1.5403 - mean\_absolute\_error: 0.9721

``

1526/Unknown 339s 218ms/step - loss: 1.5401 - mean\_absolute\_error: 0.9720

``

1527/Unknown 340s 218ms/step - loss: 1.5399 - mean\_absolute\_error: 0.9719

``

1528/Unknown 340s 218ms/step - loss: 1.5397 - mean\_absolute\_error: 0.9719

``

1529/Unknown 340s 218ms/step - loss: 1.5395 - mean\_absolute\_error: 0.9718

``

1530/Unknown 340s 218ms/step - loss: 1.5393 - mean\_absolute\_error: 0.9718

``

1531/Unknown 341s 218ms/step - loss: 1.5391 - mean\_absolute\_error: 0.9717

``

1532/Unknown 341s 218ms/step - loss: 1.5389 - mean\_absolute\_error: 0.9716

``

1533/Unknown 341s 218ms/step - loss: 1.5387 - mean\_absolute\_error: 0.9716

``

1534/Unknown 341s 218ms/step - loss: 1.5385 - mean\_absolute\_error: 0.9715

``

1535/Unknown 342s 218ms/step - loss: 1.5383 - mean\_absolute\_error: 0.9715

``

1536/Unknown 342s 218ms/step - loss: 1.5381 - mean\_absolute\_error: 0.9714

``

1537/Unknown 342s 218ms/step - loss: 1.5379 - mean\_absolute\_error: 0.9713

``

1538/Unknown 342s 218ms/step - loss: 1.5377 - mean\_absolute\_error: 0.9713

``

1539/Unknown 343s 218ms/step - loss: 1.5375 - mean\_absolute\_error: 0.9712

``

1540/Unknown 343s 218ms/step - loss: 1.5373 - mean\_absolute\_error: 0.9712

``

1541/Unknown 343s 218ms/step - loss: 1.5371 - mean\_absolute\_error: 0.9711

``

1542/Unknown 344s 218ms/step - loss: 1.5369 - mean\_absolute\_error: 0.9710

``

1543/Unknown 344s 218ms/step - loss: 1.5366 - mean\_absolute\_error: 0.9710

``

1544/Unknown 344s 219ms/step - loss: 1.5364 - mean\_absolute\_error: 0.9709

``

1545/Unknown 344s 219ms/step - loss: 1.5362 - mean\_absolute\_error: 0.9709

``

1546/Unknown 345s 219ms/step - loss: 1.5360 - mean\_absolute\_error: 0.9708

``

1547/Unknown 345s 219ms/step - loss: 1.5358 - mean\_absolute\_error: 0.9708

``

1548/Unknown 345s 219ms/step - loss: 1.5356 - mean\_absolute\_error: 0.9707

``

1549/Unknown 345s 219ms/step - loss: 1.5354 - mean\_absolute\_error: 0.9706

``

1550/Unknown 346s 219ms/step - loss: 1.5352 - mean\_absolute\_error: 0.9706

``

1551/Unknown 346s 219ms/step - loss: 1.5350 - mean\_absolute\_error: 0.9705

``

1552/Unknown 346s 219ms/step - loss: 1.5348 - mean\_absolute\_error: 0.9705

``

1553/Unknown 346s 219ms/step - loss: 1.5346 - mean\_absolute\_error: 0.9704

``

1554/Unknown 347s 219ms/step - loss: 1.5344 - mean\_absolute\_error: 0.9703

``

1555/Unknown 347s 219ms/step - loss: 1.5342 - mean\_absolute\_error: 0.9703

``

1556/Unknown 347s 219ms/step - loss: 1.5340 - mean\_absolute\_error: 0.9702

``

1557/Unknown 348s 219ms/step - loss: 1.5338 - mean\_absolute\_error: 0.9702

``

1558/Unknown 348s 219ms/step - loss: 1.5336 - mean\_absolute\_error: 0.9701

``

1559/Unknown 348s 219ms/step - loss: 1.5334 - mean\_absolute\_error: 0.9701

``

1560/Unknown 349s 219ms/step - loss: 1.5332 - mean\_absolute\_error: 0.9700

``

1561/Unknown 349s 219ms/step - loss: 1.5330 - mean\_absolute\_error: 0.9699

``

1562/Unknown 349s 219ms/step - loss: 1.5328 - mean\_absolute\_error: 0.9699

``

1563/Unknown 349s 219ms/step - loss: 1.5326 - mean\_absolute\_error: 0.9698

``

1564/Unknown 350s 219ms/step - loss: 1.5325 - mean\_absolute\_error: 0.9698

``

1565/Unknown 350s 219ms/step - loss: 1.5323 - mean\_absolute\_error: 0.9697

``

1566/Unknown 350s 219ms/step - loss: 1.5321 - mean\_absolute\_error: 0.9696

``

1567/Unknown 351s 219ms/step - loss: 1.5319 - mean\_absolute\_error: 0.9696

``

1568/Unknown 351s 219ms/step - loss: 1.5317 - mean\_absolute\_error: 0.9695

``

1569/Unknown 351s 219ms/step - loss: 1.5315 - mean\_absolute\_error: 0.9695

``

1570/Unknown 351s 219ms/step - loss: 1.5313 - mean\_absolute\_error: 0.9694

``

1571/Unknown 351s 219ms/step - loss: 1.5311 - mean\_absolute\_error: 0.9694

``

1572/Unknown 352s 219ms/step - loss: 1.5309 - mean\_absolute\_error: 0.9693

``

1573/Unknown 352s 219ms/step - loss: 1.5307 - mean\_absolute\_error: 0.9692

``

1574/Unknown 352s 220ms/step - loss: 1.5305 - mean\_absolute\_error: 0.9692

``

1575/Unknown 352s 220ms/step - loss: 1.5303 - mean\_absolute\_error: 0.9691

``

1576/Unknown 353s 220ms/step - loss: 1.5301 - mean\_absolute\_error: 0.9691

``

1577/Unknown 353s 220ms/step - loss: 1.5299 - mean\_absolute\_error: 0.9690

``

1578/Unknown 353s 220ms/step - loss: 1.5297 - mean\_absolute\_error: 0.9690

``

1579/Unknown 354s 220ms/step - loss: 1.5295 - mean\_absolute\_error: 0.9689

``

1580/Unknown 354s 220ms/step - loss: 1.5293 - mean\_absolute\_error: 0.9688

``

1581/Unknown 354s 220ms/step - loss: 1.5291 - mean\_absolute\_error: 0.9688

``

1582/Unknown 354s 220ms/step - loss: 1.5289 - mean\_absolute\_error: 0.9687

``

1583/Unknown 355s 220ms/step - loss: 1.5287 - mean\_absolute\_error: 0.9687

``

1584/Unknown 355s 220ms/step - loss: 1.5285 - mean\_absolute\_error: 0.9686

``

1585/Unknown 355s 220ms/step - loss: 1.5283 - mean\_absolute\_error: 0.9686

``

1586/Unknown 356s 220ms/step - loss: 1.5281 - mean\_absolute\_error: 0.9685

``

1587/Unknown 356s 220ms/step - loss: 1.5279 - mean\_absolute\_error: 0.9684

``

1588/Unknown 356s 220ms/step - loss: 1.5277 - mean\_absolute\_error: 0.9684

``

1589/Unknown 356s 220ms/step - loss: 1.5276 - mean\_absolute\_error: 0.9683

``

1590/Unknown 357s 220ms/step - loss: 1.5274 - mean\_absolute\_error: 0.9683

``

1591/Unknown 357s 220ms/step - loss: 1.5272 - mean\_absolute\_error: 0.9682

``

1592/Unknown 357s 220ms/step - loss: 1.5270 - mean\_absolute\_error: 0.9682

``

1593/Unknown 357s 220ms/step - loss: 1.5268 - mean\_absolute\_error: 0.9681

``

1594/Unknown 358s 220ms/step - loss: 1.5266 - mean\_absolute\_error: 0.9680

``

1595/Unknown 358s 220ms/step - loss: 1.5264 - mean\_absolute\_error: 0.9680

``

1596/Unknown 358s 220ms/step - loss: 1.5262 - mean\_absolute\_error: 0.9679

``

1597/Unknown 358s 220ms/step - loss: 1.5260 - mean\_absolute\_error: 0.9679

``

1598/Unknown 358s 220ms/step - loss: 1.5258 - mean\_absolute\_error: 0.9678

``

1599/Unknown 364s 224ms/step - loss: 1.5256 - mean\_absolute\_error: 0.9678

``

1599/1599 ━━━━━━━━━━━━━━━━━━━━ 364s 224ms/step - loss: 1.5254 - mean\_absolute\_error: 0.9677

``Epoch 2/2  /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/trainers/epoch_iterator.py:159: UserWarning: Your input ran out of data; interrupting training. Make sure that your dataset or generator can generate at least `steps_per_epoch * epochs` batches. You may need to use the `.repeat()` function when building your dataset.   self._interrupted_warning()``

Copied!

`1/1599 [37m━━━━━━━━━━━━━━━━━━━━  13:19 500ms/step - loss: 1.2442 - mean_absolute_error: 0.8669`\
\
``\
\
Copied!\
\
`2/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:39 250ms/step - loss: 1.1797 - mean_absolute_error: 0.8505`\
\
``\
\
Copied!\
\
`3/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:44 253ms/step - loss: 1.1448 - mean_absolute_error: 0.8407`\
\
``\
\
Copied!\
\
`4/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:38 250ms/step - loss: 1.1370 - mean_absolute_error: 0.8397`\
\
``\
\
Copied!\
\
`5/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:42 253ms/step - loss: 1.1311 - mean_absolute_error: 0.8382`\
\
``\
\
Copied!\
\
`6/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:40 252ms/step - loss: 1.1236 - mean_absolute_error: 0.8364`\
\
``\
\
Copied!\
\
`7/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:38 251ms/step - loss: 1.1174 - mean_absolute_error: 0.8353`\
\
``\
\
Copied!\
\
`8/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:37 250ms/step - loss: 1.1116 - mean_absolute_error: 0.8343`\
\
``\
\
Copied!\
\
`9/1599 [37m━━━━━━━━━━━━━━━━━━━━  6:37 250ms/step - loss: 1.1087 - mean_absolute_error: 0.8343`\
\
``\
\
10/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:36 249ms/step - loss: 1.1065 - mean\_absolute\_error: 0.8343\
\
``\
\
11/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:36 250ms/step - loss: 1.1047 - mean\_absolute\_error: 0.8344\
\
``\
\
12/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:35 249ms/step - loss: 1.1020 - mean\_absolute\_error: 0.8339\
\
``\
\
13/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:35 250ms/step - loss: 1.0994 - mean\_absolute\_error: 0.8331\
\
``\
\
14/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:34 249ms/step - loss: 1.0971 - mean\_absolute\_error: 0.8324\
\
``\
\
15/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:34 249ms/step - loss: 1.0957 - mean\_absolute\_error: 0.8320\
\
``\
\
16/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:33 249ms/step - loss: 1.0943 - mean\_absolute\_error: 0.8315\
\
``\
\
17/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:33 248ms/step - loss: 1.0928 - mean\_absolute\_error: 0.8310\
\
``\
\
18/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:33 249ms/step - loss: 1.0913 - mean\_absolute\_error: 0.8306\
\
``\
\
19/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:32 248ms/step - loss: 1.0899 - mean\_absolute\_error: 0.8301\
\
``\
\
20/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:32 249ms/step - loss: 1.0889 - mean\_absolute\_error: 0.8299\
\
``\
\
21/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:31 248ms/step - loss: 1.0878 - mean\_absolute\_error: 0.8296\
\
``\
\
22/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:29 247ms/step - loss: 1.0871 - mean\_absolute\_error: 0.8294\
\
``\
\
23/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:26 246ms/step - loss: 1.0865 - mean\_absolute\_error: 0.8293\
\
``\
\
24/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:24 244ms/step - loss: 1.0858 - mean\_absolute\_error: 0.8291\
\
``\
\
25/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:23 244ms/step - loss: 1.0849 - mean\_absolute\_error: 0.8290\
\
``\
\
26/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:22 243ms/step - loss: 1.0841 - mean\_absolute\_error: 0.8288\
\
``\
\
27/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:19 242ms/step - loss: 1.0833 - mean\_absolute\_error: 0.8286\
\
``\
\
28/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:17 241ms/step - loss: 1.0828 - mean\_absolute\_error: 0.8286\
\
``\
\
29/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:15 239ms/step - loss: 1.0822 - mean\_absolute\_error: 0.8284\
\
``\
\
30/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:14 239ms/step - loss: 1.0817 - mean\_absolute\_error: 0.8284\
\
``\
\
31/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:12 238ms/step - loss: 1.0811 - mean\_absolute\_error: 0.8283\
\
``\
\
32/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:11 237ms/step - loss: 1.0805 - mean\_absolute\_error: 0.8281\
\
``\
\
33/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:11 237ms/step - loss: 1.0799 - mean\_absolute\_error: 0.8280\
\
``\
\
34/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:10 237ms/step - loss: 1.0792 - mean\_absolute\_error: 0.8279\
\
``\
\
35/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:09 236ms/step - loss: 1.0787 - mean\_absolute\_error: 0.8278\
\
``\
\
36/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:08 236ms/step - loss: 1.0781 - mean\_absolute\_error: 0.8277\
\
``\
\
37/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:07 236ms/step - loss: 1.0776 - mean\_absolute\_error: 0.8276\
\
``\
\
38/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:07 235ms/step - loss: 1.0771 - mean\_absolute\_error: 0.8275\
\
``\
\
39/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:06 235ms/step - loss: 1.0766 - mean\_absolute\_error: 0.8274\
\
``\
\
40/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:06 235ms/step - loss: 1.0761 - mean\_absolute\_error: 0.8273\
\
``\
\
41/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 234ms/step - loss: 1.0757 - mean\_absolute\_error: 0.8272\
\
``\
\
42/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 234ms/step - loss: 1.0753 - mean\_absolute\_error: 0.8272\
\
``\
\
43/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 234ms/step - loss: 1.0748 - mean\_absolute\_error: 0.8270\
\
``\
\
44/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:03 234ms/step - loss: 1.0743 - mean\_absolute\_error: 0.8269\
\
``\
\
45/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 234ms/step - loss: 1.0738 - mean\_absolute\_error: 0.8268\
\
``\
\
46/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 235ms/step - loss: 1.0734 - mean\_absolute\_error: 0.8267\
\
``\
\
47/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:06 236ms/step - loss: 1.0730 - mean\_absolute\_error: 0.8266\
\
``\
\
48/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:07 237ms/step - loss: 1.0726 - mean\_absolute\_error: 0.8265\
\
``\
\
49/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:06 236ms/step - loss: 1.0724 - mean\_absolute\_error: 0.8265\
\
``\
\
50/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:06 237ms/step - loss: 1.0722 - mean\_absolute\_error: 0.8265\
\
``\
\
51/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:21 247ms/step - loss: 1.0721 - mean\_absolute\_error: 0.8265\
\
``\
\
52/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:21 246ms/step - loss: 1.0720 - mean\_absolute\_error: 0.8265\
\
``\
\
53/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:19 246ms/step - loss: 1.0719 - mean\_absolute\_error: 0.8265\
\
``\
\
54/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:19 245ms/step - loss: 1.0717 - mean\_absolute\_error: 0.8265\
\
``\
\
55/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:17 245ms/step - loss: 1.0716 - mean\_absolute\_error: 0.8265\
\
``\
\
56/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:16 244ms/step - loss: 1.0714 - mean\_absolute\_error: 0.8265\
\
``\
\
57/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:15 243ms/step - loss: 1.0712 - mean\_absolute\_error: 0.8265\
\
``\
\
58/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:13 243ms/step - loss: 1.0709 - mean\_absolute\_error: 0.8265\
\
``\
\
59/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:12 242ms/step - loss: 1.0707 - mean\_absolute\_error: 0.8264\
\
``\
\
60/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:11 242ms/step - loss: 1.0704 - mean\_absolute\_error: 0.8264\
\
``\
\
61/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:11 241ms/step - loss: 1.0701 - mean\_absolute\_error: 0.8263\
\
``\
\
62/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:10 241ms/step - loss: 1.0699 - mean\_absolute\_error: 0.8263\
\
``\
\
63/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:09 241ms/step - loss: 1.0696 - mean\_absolute\_error: 0.8262\
\
``\
\
64/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:09 240ms/step - loss: 1.0694 - mean\_absolute\_error: 0.8262\
\
``\
\
65/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:08 240ms/step - loss: 1.0691 - mean\_absolute\_error: 0.8261\
\
``\
\
66/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:07 240ms/step - loss: 1.0690 - mean\_absolute\_error: 0.8261\
\
``\
\
67/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:07 240ms/step - loss: 1.0688 - mean\_absolute\_error: 0.8261\
\
``\
\
68/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:06 239ms/step - loss: 1.0686 - mean\_absolute\_error: 0.8261\
\
``\
\
69/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 239ms/step - loss: 1.0684 - mean\_absolute\_error: 0.8260\
\
``\
\
70/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 239ms/step - loss: 1.0682 - mean\_absolute\_error: 0.8260\
\
``\
\
71/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 239ms/step - loss: 1.0680 - mean\_absolute\_error: 0.8260\
\
``\
\
72/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 239ms/step - loss: 1.0678 - mean\_absolute\_error: 0.8259\
\
``\
\
73/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:03 238ms/step - loss: 1.0676 - mean\_absolute\_error: 0.8259\
\
``\
\
74/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:03 239ms/step - loss: 1.0674 - mean\_absolute\_error: 0.8259\
\
``\
\
75/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 239ms/step - loss: 1.0672 - mean\_absolute\_error: 0.8258\
\
``\
\
76/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:04 240ms/step - loss: 1.0670 - mean\_absolute\_error: 0.8258\
\
``\
\
77/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 240ms/step - loss: 1.0668 - mean\_absolute\_error: 0.8258\
\
``\
\
78/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 240ms/step - loss: 1.0666 - mean\_absolute\_error: 0.8257\
\
``\
\
79/1599 \[37m━━━━━━━━━━━━━━━━━━━━ 6:05 241ms/step - loss: 1.0664 - mean\_absolute\_error: 0.8257\
\
``\
\
80/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:06 241ms/step - loss: 1.0662 - mean\_absolute\_error: 0.8257\
\
``\
\
81/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:06 241ms/step - loss: 1.0661 - mean\_absolute\_error: 0.8257\
\
``\
\
82/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:05 241ms/step - loss: 1.0659 - mean\_absolute\_error: 0.8256\
\
``\
\
83/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:05 241ms/step - loss: 1.0658 - mean\_absolute\_error: 0.8256\
\
``\
\
84/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:05 241ms/step - loss: 1.0657 - mean\_absolute\_error: 0.8256\
\
``\
\
85/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:05 241ms/step - loss: 1.0656 - mean\_absolute\_error: 0.8256\
\
``\
\
86/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:04 241ms/step - loss: 1.0655 - mean\_absolute\_error: 0.8256\
\
``\
\
87/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:04 241ms/step - loss: 1.0653 - mean\_absolute\_error: 0.8256\
\
``\
\
88/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 241ms/step - loss: 1.0652 - mean\_absolute\_error: 0.8256\
\
``\
\
89/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 241ms/step - loss: 1.0651 - mean\_absolute\_error: 0.8256\
\
``\
\
90/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 241ms/step - loss: 1.0651 - mean\_absolute\_error: 0.8256\
\
``\
\
91/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 241ms/step - loss: 1.0650 - mean\_absolute\_error: 0.8256\
\
``\
\
92/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 241ms/step - loss: 1.0649 - mean\_absolute\_error: 0.8256\
\
``\
\
93/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 241ms/step - loss: 1.0649 - mean\_absolute\_error: 0.8256\
\
``\
\
94/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 241ms/step - loss: 1.0648 - mean\_absolute\_error: 0.8256\
\
``\
\
95/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:01 241ms/step - loss: 1.0648 - mean\_absolute\_error: 0.8256\
\
``\
\
96/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 241ms/step - loss: 1.0647 - mean\_absolute\_error: 0.8256\
\
``\
\
97/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 241ms/step - loss: 1.0647 - mean\_absolute\_error: 0.8256\
\
``\
\
98/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 242ms/step - loss: 1.0646 - mean\_absolute\_error: 0.8256\
\
``\
\
99/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 242ms/step - loss: 1.0646 - mean\_absolute\_error: 0.8256\
\
``\
\
100/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 243ms/step - loss: 1.0645 - mean\_absolute\_error: 0.8256\
\
``\
\
101/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 243ms/step - loss: 1.0645 - mean\_absolute\_error: 0.8256\
\
``\
\
102/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 243ms/step - loss: 1.0645 - mean\_absolute\_error: 0.8256\
\
``\
\
103/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:03 243ms/step - loss: 1.0644 - mean\_absolute\_error: 0.8256\
\
``\
\
104/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 243ms/step - loss: 1.0644 - mean\_absolute\_error: 0.8256\
\
``\
\
105/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 243ms/step - loss: 1.0643 - mean\_absolute\_error: 0.8256\
\
``\
\
106/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 243ms/step - loss: 1.0643 - mean\_absolute\_error: 0.8256\
\
``\
\
107/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 243ms/step - loss: 1.0642 - mean\_absolute\_error: 0.8256\
\
``\
\
108/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:02 243ms/step - loss: 1.0642 - mean\_absolute\_error: 0.8256\
\
``\
\
109/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:01 243ms/step - loss: 1.0642 - mean\_absolute\_error: 0.8256\
\
``\
\
110/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:01 243ms/step - loss: 1.0642 - mean\_absolute\_error: 0.8256\
\
``\
\
111/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:01 243ms/step - loss: 1.0641 - mean\_absolute\_error: 0.8256\
\
``\
\
112/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0641 - mean\_absolute\_error: 0.8256\
\
``\
\
113/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0641 - mean\_absolute\_error: 0.8256\
\
``\
\
114/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0640 - mean\_absolute\_error: 0.8256\
\
``\
\
115/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0640 - mean\_absolute\_error: 0.8256\
\
``\
\
116/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0640 - mean\_absolute\_error: 0.8256\
\
``\
\
117/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0640 - mean\_absolute\_error: 0.8256\
\
``\
\
118/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 6:00 243ms/step - loss: 1.0639 - mean\_absolute\_error: 0.8256\
\
``\
\
119/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:59 243ms/step - loss: 1.0639 - mean\_absolute\_error: 0.8256\
\
``\
\
120/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:59 243ms/step - loss: 1.0639 - mean\_absolute\_error: 0.8256\
\
``\
\
121/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:59 243ms/step - loss: 1.0639 - mean\_absolute\_error: 0.8256\
\
``\
\
122/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:59 243ms/step - loss: 1.0639 - mean\_absolute\_error: 0.8256\
\
``\
\
123/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:59 243ms/step - loss: 1.0639 - mean\_absolute\_error: 0.8256\
\
``\
\
124/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:58 243ms/step - loss: 1.0638 - mean\_absolute\_error: 0.8256\
\
``\
\
125/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:58 243ms/step - loss: 1.0638 - mean\_absolute\_error: 0.8256\
\
``\
\
126/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:57 243ms/step - loss: 1.0638 - mean\_absolute\_error: 0.8256\
\
``\
\
127/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:57 243ms/step - loss: 1.0638 - mean\_absolute\_error: 0.8256\
\
``\
\
128/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:56 242ms/step - loss: 1.0638 - mean\_absolute\_error: 0.8256\
\
``\
\
129/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:56 242ms/step - loss: 1.0638 - mean\_absolute\_error: 0.8256\
\
``\
\
130/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:55 242ms/step - loss: 1.0637 - mean\_absolute\_error: 0.8256\
\
``\
\
131/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:54 242ms/step - loss: 1.0637 - mean\_absolute\_error: 0.8256\
\
``\
\
132/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:54 242ms/step - loss: 1.0637 - mean\_absolute\_error: 0.8256\
\
``\
\
133/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:54 242ms/step - loss: 1.0637 - mean\_absolute\_error: 0.8256\
\
``\
\
134/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:53 241ms/step - loss: 1.0636 - mean\_absolute\_error: 0.8255\
\
``\
\
135/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:53 241ms/step - loss: 1.0636 - mean\_absolute\_error: 0.8255\
\
``\
\
136/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:52 241ms/step - loss: 1.0636 - mean\_absolute\_error: 0.8255\
\
``\
\
137/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:52 241ms/step - loss: 1.0636 - mean\_absolute\_error: 0.8255\
\
``\
\
138/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:52 241ms/step - loss: 1.0635 - mean\_absolute\_error: 0.8255\
\
``\
\
139/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:51 241ms/step - loss: 1.0635 - mean\_absolute\_error: 0.8255\
\
``\
\
140/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:51 241ms/step - loss: 1.0635 - mean\_absolute\_error: 0.8255\
\
``\
\
141/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:51 241ms/step - loss: 1.0635 - mean\_absolute\_error: 0.8255\
\
``\
\
142/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:50 241ms/step - loss: 1.0634 - mean\_absolute\_error: 0.8255\
\
``\
\
143/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:50 241ms/step - loss: 1.0634 - mean\_absolute\_error: 0.8255\
\
``\
\
144/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 240ms/step - loss: 1.0634 - mean\_absolute\_error: 0.8255\
\
``\
\
145/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 240ms/step - loss: 1.0633 - mean\_absolute\_error: 0.8255\
\
``\
\
146/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 240ms/step - loss: 1.0633 - mean\_absolute\_error: 0.8255\
\
``\
\
147/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 241ms/step - loss: 1.0633 - mean\_absolute\_error: 0.8255\
\
``\
\
148/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 241ms/step - loss: 1.0632 - mean\_absolute\_error: 0.8254\
\
``\
\
149/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 241ms/step - loss: 1.0632 - mean\_absolute\_error: 0.8254\
\
``\
\
150/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 241ms/step - loss: 1.0632 - mean\_absolute\_error: 0.8254\
\
``\
\
151/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 241ms/step - loss: 1.0631 - mean\_absolute\_error: 0.8254\
\
``\
\
152/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 242ms/step - loss: 1.0631 - mean\_absolute\_error: 0.8254\
\
``\
\
153/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 242ms/step - loss: 1.0630 - mean\_absolute\_error: 0.8254\
\
``\
\
154/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 242ms/step - loss: 1.0630 - mean\_absolute\_error: 0.8254\
\
``\
\
155/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:49 242ms/step - loss: 1.0629 - mean\_absolute\_error: 0.8253\
\
``\
\
156/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:48 242ms/step - loss: 1.0629 - mean\_absolute\_error: 0.8253\
\
``\
\
157/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:48 242ms/step - loss: 1.0628 - mean\_absolute\_error: 0.8253\
\
``\
\
158/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:48 242ms/step - loss: 1.0627 - mean\_absolute\_error: 0.8253\
\
``\
\
159/1599 ━\[37m━━━━━━━━━━━━━━━━━━━ 5:47 242ms/step - loss: 1.0627 - mean\_absolute\_error: 0.8252\
\
``\
\
160/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:47 241ms/step - loss: 1.0626 - mean\_absolute\_error: 0.8252\
\
``\
\
161/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:46 241ms/step - loss: 1.0625 - mean\_absolute\_error: 0.8252\
\
``\
\
162/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:46 241ms/step - loss: 1.0625 - mean\_absolute\_error: 0.8252\
\
``\
\
163/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:46 241ms/step - loss: 1.0624 - mean\_absolute\_error: 0.8251\
\
``\
\
164/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:45 241ms/step - loss: 1.0623 - mean\_absolute\_error: 0.8251\
\
``\
\
165/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:45 241ms/step - loss: 1.0623 - mean\_absolute\_error: 0.8251\
\
``\
\
166/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:44 240ms/step - loss: 1.0622 - mean\_absolute\_error: 0.8251\
\
``\
\
167/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:43 240ms/step - loss: 1.0621 - mean\_absolute\_error: 0.8250\
\
``\
\
168/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:43 240ms/step - loss: 1.0621 - mean\_absolute\_error: 0.8250\
\
``\
\
169/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:43 240ms/step - loss: 1.0620 - mean\_absolute\_error: 0.8250\
\
``\
\
170/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:43 240ms/step - loss: 1.0619 - mean\_absolute\_error: 0.8250\
\
``\
\
171/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:42 240ms/step - loss: 1.0619 - mean\_absolute\_error: 0.8249\
\
``\
\
172/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:42 240ms/step - loss: 1.0618 - mean\_absolute\_error: 0.8249\
\
``\
\
173/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:42 240ms/step - loss: 1.0617 - mean\_absolute\_error: 0.8249\
\
``\
\
174/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:41 240ms/step - loss: 1.0617 - mean\_absolute\_error: 0.8249\
\
``\
\
175/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:41 240ms/step - loss: 1.0616 - mean\_absolute\_error: 0.8249\
\
``\
\
176/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:41 240ms/step - loss: 1.0616 - mean\_absolute\_error: 0.8248\
\
``\
\
177/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:40 240ms/step - loss: 1.0615 - mean\_absolute\_error: 0.8248\
\
``\
\
178/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:40 240ms/step - loss: 1.0614 - mean\_absolute\_error: 0.8248\
\
``\
\
179/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:40 239ms/step - loss: 1.0614 - mean\_absolute\_error: 0.8248\
\
``\
\
180/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 239ms/step - loss: 1.0613 - mean\_absolute\_error: 0.8247\
\
``\
\
181/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0612 - mean\_absolute\_error: 0.8247\
\
``\
\
182/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0612 - mean\_absolute\_error: 0.8247\
\
``\
\
183/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0611 - mean\_absolute\_error: 0.8247\
\
``\
\
184/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0611 - mean\_absolute\_error: 0.8247\
\
``\
\
185/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0611 - mean\_absolute\_error: 0.8246\
\
``\
\
186/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0610 - mean\_absolute\_error: 0.8246\
\
``\
\
187/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0610 - mean\_absolute\_error: 0.8246\
\
``\
\
188/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:39 240ms/step - loss: 1.0609 - mean\_absolute\_error: 0.8246\
\
``\
\
189/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:38 240ms/step - loss: 1.0609 - mean\_absolute\_error: 0.8246\
\
``\
\
190/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:38 240ms/step - loss: 1.0608 - mean\_absolute\_error: 0.8246\
\
``\
\
191/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:38 240ms/step - loss: 1.0608 - mean\_absolute\_error: 0.8245\
\
``\
\
192/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:37 240ms/step - loss: 1.0608 - mean\_absolute\_error: 0.8245\
\
``\
\
193/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:37 240ms/step - loss: 1.0607 - mean\_absolute\_error: 0.8245\
\
``\
\
194/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:36 240ms/step - loss: 1.0607 - mean\_absolute\_error: 0.8245\
\
``\
\
195/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:36 240ms/step - loss: 1.0606 - mean\_absolute\_error: 0.8245\
\
``\
\
196/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:35 239ms/step - loss: 1.0606 - mean\_absolute\_error: 0.8245\
\
``\
\
197/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:35 239ms/step - loss: 1.0605 - mean\_absolute\_error: 0.8245\
\
``\
\
198/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:35 239ms/step - loss: 1.0605 - mean\_absolute\_error: 0.8244\
\
``\
\
199/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:34 239ms/step - loss: 1.0605 - mean\_absolute\_error: 0.8244\
\
``\
\
200/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:34 239ms/step - loss: 1.0604 - mean\_absolute\_error: 0.8244\
\
``\
\
201/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:34 239ms/step - loss: 1.0604 - mean\_absolute\_error: 0.8244\
\
``\
\
202/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 239ms/step - loss: 1.0603 - mean\_absolute\_error: 0.8244\
\
``\
\
203/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 239ms/step - loss: 1.0603 - mean\_absolute\_error: 0.8244\
\
``\
\
204/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 239ms/step - loss: 1.0602 - mean\_absolute\_error: 0.8243\
\
``\
\
205/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 239ms/step - loss: 1.0602 - mean\_absolute\_error: 0.8243\
\
``\
\
206/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 239ms/step - loss: 1.0601 - mean\_absolute\_error: 0.8243\
\
``\
\
207/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 239ms/step - loss: 1.0601 - mean\_absolute\_error: 0.8243\
\
``\
\
208/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 239ms/step - loss: 1.0600 - mean\_absolute\_error: 0.8243\
\
``\
\
209/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 239ms/step - loss: 1.0600 - mean\_absolute\_error: 0.8243\
\
``\
\
210/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 239ms/step - loss: 1.0599 - mean\_absolute\_error: 0.8242\
\
``\
\
211/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 239ms/step - loss: 1.0599 - mean\_absolute\_error: 0.8242\
\
``\
\
212/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 239ms/step - loss: 1.0598 - mean\_absolute\_error: 0.8242\
\
``\
\
213/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 240ms/step - loss: 1.0598 - mean\_absolute\_error: 0.8242\
\
``\
\
214/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 240ms/step - loss: 1.0597 - mean\_absolute\_error: 0.8242\
\
``\
\
215/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 240ms/step - loss: 1.0597 - mean\_absolute\_error: 0.8241\
\
``\
\
216/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 241ms/step - loss: 1.0596 - mean\_absolute\_error: 0.8241\
\
``\
\
217/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 241ms/step - loss: 1.0596 - mean\_absolute\_error: 0.8241\
\
``\
\
218/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 241ms/step - loss: 1.0595 - mean\_absolute\_error: 0.8241\
\
``\
\
219/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 241ms/step - loss: 1.0595 - mean\_absolute\_error: 0.8241\
\
``\
\
220/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 241ms/step - loss: 1.0594 - mean\_absolute\_error: 0.8241\
\
``\
\
221/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 242ms/step - loss: 1.0594 - mean\_absolute\_error: 0.8240\
\
``\
\
222/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:33 242ms/step - loss: 1.0593 - mean\_absolute\_error: 0.8240\
\
``\
\
223/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 242ms/step - loss: 1.0593 - mean\_absolute\_error: 0.8240\
\
``\
\
224/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 242ms/step - loss: 1.0592 - mean\_absolute\_error: 0.8240\
\
``\
\
225/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 242ms/step - loss: 1.0592 - mean\_absolute\_error: 0.8240\
\
``\
\
226/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:32 242ms/step - loss: 1.0591 - mean\_absolute\_error: 0.8240\
\
``\
\
227/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:31 242ms/step - loss: 1.0590 - mean\_absolute\_error: 0.8239\
\
``\
\
228/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:31 242ms/step - loss: 1.0590 - mean\_absolute\_error: 0.8239\
\
``\
\
229/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:31 242ms/step - loss: 1.0589 - mean\_absolute\_error: 0.8239\
\
``\
\
230/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:30 242ms/step - loss: 1.0589 - mean\_absolute\_error: 0.8239\
\
``\
\
231/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:30 242ms/step - loss: 1.0589 - mean\_absolute\_error: 0.8239\
\
``\
\
232/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:30 241ms/step - loss: 1.0588 - mean\_absolute\_error: 0.8238\
\
``\
\
233/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:29 241ms/step - loss: 1.0588 - mean\_absolute\_error: 0.8238\
\
``\
\
234/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:29 241ms/step - loss: 1.0587 - mean\_absolute\_error: 0.8238\
\
``\
\
235/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:28 241ms/step - loss: 1.0587 - mean\_absolute\_error: 0.8238\
\
``\
\
236/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:28 241ms/step - loss: 1.0586 - mean\_absolute\_error: 0.8238\
\
``\
\
237/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:28 241ms/step - loss: 1.0586 - mean\_absolute\_error: 0.8238\
\
``\
\
238/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:27 241ms/step - loss: 1.0585 - mean\_absolute\_error: 0.8237\
\
``\
\
239/1599 ━━\[37m━━━━━━━━━━━━━━━━━━ 5:27 241ms/step - loss: 1.0585 - mean\_absolute\_error: 0.8237\
\
``\
\
240/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:27 241ms/step - loss: 1.0584 - mean\_absolute\_error: 0.8237\
\
``\
\
241/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:27 241ms/step - loss: 1.0584 - mean\_absolute\_error: 0.8237\
\
``\
\
242/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:26 241ms/step - loss: 1.0583 - mean\_absolute\_error: 0.8237\
\
``\
\
243/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:26 241ms/step - loss: 1.0583 - mean\_absolute\_error: 0.8237\
\
``\
\
244/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:26 241ms/step - loss: 1.0583 - mean\_absolute\_error: 0.8236\
\
``\
\
245/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:26 241ms/step - loss: 1.0582 - mean\_absolute\_error: 0.8236\
\
``\
\
246/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0582 - mean\_absolute\_error: 0.8236\
\
``\
\
247/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0581 - mean\_absolute\_error: 0.8236\
\
``\
\
248/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0581 - mean\_absolute\_error: 0.8236\
\
``\
\
249/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0580 - mean\_absolute\_error: 0.8236\
\
``\
\
250/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0580 - mean\_absolute\_error: 0.8235\
\
``\
\
251/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0579 - mean\_absolute\_error: 0.8235\
\
``\
\
252/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:25 241ms/step - loss: 1.0578 - mean\_absolute\_error: 0.8235\
\
``\
\
253/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:24 241ms/step - loss: 1.0578 - mean\_absolute\_error: 0.8235\
\
``\
\
254/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:24 242ms/step - loss: 1.0577 - mean\_absolute\_error: 0.8235\
\
``\
\
255/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:24 242ms/step - loss: 1.0577 - mean\_absolute\_error: 0.8234\
\
``\
\
256/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:24 242ms/step - loss: 1.0576 - mean\_absolute\_error: 0.8234\
\
``\
\
257/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:24 242ms/step - loss: 1.0575 - mean\_absolute\_error: 0.8234\
\
``\
\
258/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:24 242ms/step - loss: 1.0575 - mean\_absolute\_error: 0.8234\
\
``\
\
259/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:23 242ms/step - loss: 1.0574 - mean\_absolute\_error: 0.8233\
\
``\
\
260/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:23 242ms/step - loss: 1.0573 - mean\_absolute\_error: 0.8233\
\
``\
\
261/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:23 242ms/step - loss: 1.0573 - mean\_absolute\_error: 0.8233\
\
``\
\
262/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:22 242ms/step - loss: 1.0572 - mean\_absolute\_error: 0.8233\
\
``\
\
263/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:22 242ms/step - loss: 1.0572 - mean\_absolute\_error: 0.8232\
\
``\
\
264/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:22 241ms/step - loss: 1.0571 - mean\_absolute\_error: 0.8232\
\
``\
\
265/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:22 241ms/step - loss: 1.0570 - mean\_absolute\_error: 0.8232\
\
``\
\
266/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:21 241ms/step - loss: 1.0569 - mean\_absolute\_error: 0.8232\
\
``\
\
267/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:21 241ms/step - loss: 1.0569 - mean\_absolute\_error: 0.8231\
\
``\
\
268/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:21 241ms/step - loss: 1.0568 - mean\_absolute\_error: 0.8231\
\
``\
\
269/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:21 242ms/step - loss: 1.0567 - mean\_absolute\_error: 0.8231\
\
``\
\
270/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:20 242ms/step - loss: 1.0567 - mean\_absolute\_error: 0.8230\
\
``\
\
271/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:20 242ms/step - loss: 1.0566 - mean\_absolute\_error: 0.8230\
\
``\
\
272/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:20 242ms/step - loss: 1.0565 - mean\_absolute\_error: 0.8230\
\
``\
\
273/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:20 241ms/step - loss: 1.0565 - mean\_absolute\_error: 0.8230\
\
``\
\
274/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:19 241ms/step - loss: 1.0564 - mean\_absolute\_error: 0.8229\
\
``\
\
275/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:19 241ms/step - loss: 1.0563 - mean\_absolute\_error: 0.8229\
\
``\
\
276/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:19 241ms/step - loss: 1.0563 - mean\_absolute\_error: 0.8229\
\
``\
\
277/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:18 241ms/step - loss: 1.0562 - mean\_absolute\_error: 0.8228\
\
``\
\
278/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:18 241ms/step - loss: 1.0561 - mean\_absolute\_error: 0.8228\
\
``\
\
279/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:18 241ms/step - loss: 1.0560 - mean\_absolute\_error: 0.8228\
\
``\
\
280/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:18 241ms/step - loss: 1.0560 - mean\_absolute\_error: 0.8228\
\
``\
\
281/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:17 241ms/step - loss: 1.0559 - mean\_absolute\_error: 0.8227\
\
``\
\
282/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:17 241ms/step - loss: 1.0558 - mean\_absolute\_error: 0.8227\
\
``\
\
283/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:17 241ms/step - loss: 1.0558 - mean\_absolute\_error: 0.8227\
\
``\
\
284/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:17 241ms/step - loss: 1.0557 - mean\_absolute\_error: 0.8227\
\
``\
\
285/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:17 241ms/step - loss: 1.0556 - mean\_absolute\_error: 0.8226\
\
``\
\
286/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:16 241ms/step - loss: 1.0556 - mean\_absolute\_error: 0.8226\
\
``\
\
287/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:16 241ms/step - loss: 1.0555 - mean\_absolute\_error: 0.8226\
\
``\
\
288/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:16 241ms/step - loss: 1.0554 - mean\_absolute\_error: 0.8225\
\
``\
\
289/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:16 241ms/step - loss: 1.0554 - mean\_absolute\_error: 0.8225\
\
``\
\
290/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:16 241ms/step - loss: 1.0553 - mean\_absolute\_error: 0.8225\
\
``\
\
291/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:15 241ms/step - loss: 1.0552 - mean\_absolute\_error: 0.8225\
\
``\
\
292/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:15 241ms/step - loss: 1.0552 - mean\_absolute\_error: 0.8224\
\
``\
\
293/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:15 241ms/step - loss: 1.0551 - mean\_absolute\_error: 0.8224\
\
``\
\
294/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:14 241ms/step - loss: 1.0550 - mean\_absolute\_error: 0.8224\
\
``\
\
295/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:14 241ms/step - loss: 1.0550 - mean\_absolute\_error: 0.8224\
\
``\
\
296/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:13 241ms/step - loss: 1.0549 - mean\_absolute\_error: 0.8223\
\
``\
\
297/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:13 241ms/step - loss: 1.0548 - mean\_absolute\_error: 0.8223\
\
``\
\
298/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:13 241ms/step - loss: 1.0548 - mean\_absolute\_error: 0.8223\
\
``\
\
299/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:12 241ms/step - loss: 1.0547 - mean\_absolute\_error: 0.8222\
\
``\
\
300/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:12 241ms/step - loss: 1.0546 - mean\_absolute\_error: 0.8222\
\
``\
\
301/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:12 240ms/step - loss: 1.0545 - mean\_absolute\_error: 0.8222\
\
``\
\
302/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:11 240ms/step - loss: 1.0545 - mean\_absolute\_error: 0.8222\
\
``\
\
303/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:11 240ms/step - loss: 1.0544 - mean\_absolute\_error: 0.8221\
\
``\
\
304/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:11 240ms/step - loss: 1.0543 - mean\_absolute\_error: 0.8221\
\
``\
\
305/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:10 240ms/step - loss: 1.0543 - mean\_absolute\_error: 0.8221\
\
``\
\
306/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:10 240ms/step - loss: 1.0542 - mean\_absolute\_error: 0.8220\
\
``\
\
307/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:10 240ms/step - loss: 1.0541 - mean\_absolute\_error: 0.8220\
\
``\
\
308/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:09 240ms/step - loss: 1.0541 - mean\_absolute\_error: 0.8220\
\
``\
\
309/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:09 240ms/step - loss: 1.0540 - mean\_absolute\_error: 0.8220\
\
``\
\
310/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:09 240ms/step - loss: 1.0539 - mean\_absolute\_error: 0.8219\
\
``\
\
311/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:09 240ms/step - loss: 1.0539 - mean\_absolute\_error: 0.8219\
\
``\
\
312/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 240ms/step - loss: 1.0538 - mean\_absolute\_error: 0.8219\
\
``\
\
313/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 240ms/step - loss: 1.0537 - mean\_absolute\_error: 0.8219\
\
``\
\
314/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 240ms/step - loss: 1.0536 - mean\_absolute\_error: 0.8218\
\
``\
\
315/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 240ms/step - loss: 1.0536 - mean\_absolute\_error: 0.8218\
\
``\
\
316/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 240ms/step - loss: 1.0535 - mean\_absolute\_error: 0.8218\
\
``\
\
317/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 240ms/step - loss: 1.0534 - mean\_absolute\_error: 0.8217\
\
``\
\
318/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:08 241ms/step - loss: 1.0534 - mean\_absolute\_error: 0.8217\
\
``\
\
319/1599 ━━━\[37m━━━━━━━━━━━━━━━━━ 5:07 241ms/step - loss: 1.0533 - mean\_absolute\_error: 0.8217\
\
``\
\
320/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 241ms/step - loss: 1.0532 - mean\_absolute\_error: 0.8217\
\
``\
\
321/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 241ms/step - loss: 1.0532 - mean\_absolute\_error: 0.8216\
\
``\
\
322/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 241ms/step - loss: 1.0531 - mean\_absolute\_error: 0.8216\
\
``\
\
323/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 241ms/step - loss: 1.0531 - mean\_absolute\_error: 0.8216\
\
``\
\
324/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:08 242ms/step - loss: 1.0530 - mean\_absolute\_error: 0.8216\
\
``\
\
325/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:08 242ms/step - loss: 1.0529 - mean\_absolute\_error: 0.8215\
\
``\
\
326/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:08 242ms/step - loss: 1.0529 - mean\_absolute\_error: 0.8215\
\
``\
\
327/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 242ms/step - loss: 1.0528 - mean\_absolute\_error: 0.8215\
\
``\
\
328/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 242ms/step - loss: 1.0527 - mean\_absolute\_error: 0.8214\
\
``\
\
329/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:07 242ms/step - loss: 1.0527 - mean\_absolute\_error: 0.8214\
\
``\
\
330/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:06 242ms/step - loss: 1.0526 - mean\_absolute\_error: 0.8214\
\
``\
\
331/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:06 242ms/step - loss: 1.0525 - mean\_absolute\_error: 0.8214\
\
``\
\
332/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:05 241ms/step - loss: 1.0525 - mean\_absolute\_error: 0.8213\
\
``\
\
333/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:05 241ms/step - loss: 1.0524 - mean\_absolute\_error: 0.8213\
\
``\
\
334/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:05 241ms/step - loss: 1.0523 - mean\_absolute\_error: 0.8213\
\
``\
\
335/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:05 241ms/step - loss: 1.0523 - mean\_absolute\_error: 0.8213\
\
``\
\
336/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:04 241ms/step - loss: 1.0522 - mean\_absolute\_error: 0.8212\
\
``\
\
337/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:04 241ms/step - loss: 1.0522 - mean\_absolute\_error: 0.8212\
\
``\
\
338/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:04 241ms/step - loss: 1.0521 - mean\_absolute\_error: 0.8212\
\
``\
\
339/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:03 241ms/step - loss: 1.0520 - mean\_absolute\_error: 0.8212\
\
``\
\
340/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:03 241ms/step - loss: 1.0520 - mean\_absolute\_error: 0.8211\
\
``\
\
341/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:03 241ms/step - loss: 1.0519 - mean\_absolute\_error: 0.8211\
\
``\
\
342/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:02 241ms/step - loss: 1.0518 - mean\_absolute\_error: 0.8211\
\
``\
\
343/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:02 241ms/step - loss: 1.0518 - mean\_absolute\_error: 0.8211\
\
``\
\
344/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:02 241ms/step - loss: 1.0517 - mean\_absolute\_error: 0.8210\
\
``\
\
345/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:02 241ms/step - loss: 1.0517 - mean\_absolute\_error: 0.8210\
\
``\
\
346/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:01 241ms/step - loss: 1.0516 - mean\_absolute\_error: 0.8210\
\
``\
\
347/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:01 241ms/step - loss: 1.0515 - mean\_absolute\_error: 0.8210\
\
``\
\
348/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:01 241ms/step - loss: 1.0515 - mean\_absolute\_error: 0.8209\
\
``\
\
349/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:01 241ms/step - loss: 1.0514 - mean\_absolute\_error: 0.8209\
\
``\
\
350/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:01 241ms/step - loss: 1.0514 - mean\_absolute\_error: 0.8209\
\
``\
\
351/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:01 241ms/step - loss: 1.0513 - mean\_absolute\_error: 0.8209\
\
``\
\
352/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:00 241ms/step - loss: 1.0513 - mean\_absolute\_error: 0.8208\
\
``\
\
353/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:00 241ms/step - loss: 1.0512 - mean\_absolute\_error: 0.8208\
\
``\
\
354/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 5:00 241ms/step - loss: 1.0511 - mean\_absolute\_error: 0.8208\
\
``\
\
355/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:59 241ms/step - loss: 1.0511 - mean\_absolute\_error: 0.8208\
\
``\
\
356/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:59 241ms/step - loss: 1.0510 - mean\_absolute\_error: 0.8208\
\
``\
\
357/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:59 241ms/step - loss: 1.0510 - mean\_absolute\_error: 0.8207\
\
``\
\
358/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:58 241ms/step - loss: 1.0509 - mean\_absolute\_error: 0.8207\
\
``\
\
359/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:58 241ms/step - loss: 1.0509 - mean\_absolute\_error: 0.8207\
\
``\
\
360/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:58 241ms/step - loss: 1.0508 - mean\_absolute\_error: 0.8207\
\
``\
\
361/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:57 241ms/step - loss: 1.0508 - mean\_absolute\_error: 0.8206\
\
``\
\
362/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:57 241ms/step - loss: 1.0507 - mean\_absolute\_error: 0.8206\
\
``\
\
363/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:57 240ms/step - loss: 1.0506 - mean\_absolute\_error: 0.8206\
\
``\
\
364/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:56 240ms/step - loss: 1.0506 - mean\_absolute\_error: 0.8206\
\
``\
\
365/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:56 240ms/step - loss: 1.0505 - mean\_absolute\_error: 0.8206\
\
``\
\
366/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:56 240ms/step - loss: 1.0505 - mean\_absolute\_error: 0.8205\
\
``\
\
367/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:56 240ms/step - loss: 1.0504 - mean\_absolute\_error: 0.8205\
\
``\
\
368/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:55 240ms/step - loss: 1.0504 - mean\_absolute\_error: 0.8205\
\
``\
\
369/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:55 240ms/step - loss: 1.0503 - mean\_absolute\_error: 0.8205\
\
``\
\
370/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:55 240ms/step - loss: 1.0503 - mean\_absolute\_error: 0.8204\
\
``\
\
371/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:54 240ms/step - loss: 1.0502 - mean\_absolute\_error: 0.8204\
\
``\
\
372/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:54 240ms/step - loss: 1.0502 - mean\_absolute\_error: 0.8204\
\
``\
\
373/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:54 240ms/step - loss: 1.0501 - mean\_absolute\_error: 0.8204\
\
``\
\
374/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:54 240ms/step - loss: 1.0501 - mean\_absolute\_error: 0.8204\
\
``\
\
375/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 240ms/step - loss: 1.0500 - mean\_absolute\_error: 0.8203\
\
``\
\
376/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 240ms/step - loss: 1.0500 - mean\_absolute\_error: 0.8203\
\
``\
\
377/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 240ms/step - loss: 1.0499 - mean\_absolute\_error: 0.8203\
\
``\
\
378/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 240ms/step - loss: 1.0499 - mean\_absolute\_error: 0.8203\
\
``\
\
379/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 240ms/step - loss: 1.0498 - mean\_absolute\_error: 0.8203\
\
``\
\
380/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 241ms/step - loss: 1.0498 - mean\_absolute\_error: 0.8203\
\
``\
\
381/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:53 241ms/step - loss: 1.0497 - mean\_absolute\_error: 0.8202\
\
``\
\
382/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:52 241ms/step - loss: 1.0497 - mean\_absolute\_error: 0.8202\
\
``\
\
383/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:52 241ms/step - loss: 1.0497 - mean\_absolute\_error: 0.8202\
\
``\
\
384/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:52 241ms/step - loss: 1.0496 - mean\_absolute\_error: 0.8202\
\
``\
\
385/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:52 241ms/step - loss: 1.0496 - mean\_absolute\_error: 0.8202\
\
``\
\
386/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:51 241ms/step - loss: 1.0495 - mean\_absolute\_error: 0.8201\
\
``\
\
387/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:51 241ms/step - loss: 1.0495 - mean\_absolute\_error: 0.8201\
\
``\
\
388/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:51 240ms/step - loss: 1.0494 - mean\_absolute\_error: 0.8201\
\
``\
\
389/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:50 240ms/step - loss: 1.0494 - mean\_absolute\_error: 0.8201\
\
``\
\
390/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:50 240ms/step - loss: 1.0493 - mean\_absolute\_error: 0.8201\
\
``\
\
391/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:50 240ms/step - loss: 1.0493 - mean\_absolute\_error: 0.8200\
\
``\
\
392/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:49 240ms/step - loss: 1.0492 - mean\_absolute\_error: 0.8200\
\
``\
\
393/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:49 240ms/step - loss: 1.0492 - mean\_absolute\_error: 0.8200\
\
``\
\
394/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:49 240ms/step - loss: 1.0491 - mean\_absolute\_error: 0.8200\
\
``\
\
395/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:48 240ms/step - loss: 1.0491 - mean\_absolute\_error: 0.8200\
\
``\
\
396/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:48 240ms/step - loss: 1.0491 - mean\_absolute\_error: 0.8200\
\
``\
\
397/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:48 240ms/step - loss: 1.0490 - mean\_absolute\_error: 0.8199\
\
``\
\
398/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:48 240ms/step - loss: 1.0490 - mean\_absolute\_error: 0.8199\
\
``\
\
399/1599 ━━━━\[37m━━━━━━━━━━━━━━━━ 4:47 240ms/step - loss: 1.0489 - mean\_absolute\_error: 0.8199\
\
``\
\
400/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:47 240ms/step - loss: 1.0489 - mean\_absolute\_error: 0.8199\
\
``\
\
401/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:47 240ms/step - loss: 1.0488 - mean\_absolute\_error: 0.8199\
\
``\
\
402/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:47 240ms/step - loss: 1.0488 - mean\_absolute\_error: 0.8198\
\
``\
\
403/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:46 240ms/step - loss: 1.0487 - mean\_absolute\_error: 0.8198\
\
``\
\
404/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:46 240ms/step - loss: 1.0487 - mean\_absolute\_error: 0.8198\
\
``\
\
405/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:46 240ms/step - loss: 1.0486 - mean\_absolute\_error: 0.8198\
\
``\
\
406/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0486 - mean\_absolute\_error: 0.8198\
\
``\
\
407/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0485 - mean\_absolute\_error: 0.8198\
\
``\
\
408/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0485 - mean\_absolute\_error: 0.8197\
\
``\
\
409/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0485 - mean\_absolute\_error: 0.8197\
\
``\
\
410/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0484 - mean\_absolute\_error: 0.8197\
\
``\
\
411/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0484 - mean\_absolute\_error: 0.8197\
\
``\
\
412/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:45 240ms/step - loss: 1.0483 - mean\_absolute\_error: 0.8197\
\
``\
\
413/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:44 240ms/step - loss: 1.0483 - mean\_absolute\_error: 0.8196\
\
``\
\
414/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:44 240ms/step - loss: 1.0482 - mean\_absolute\_error: 0.8196\
\
``\
\
415/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:44 240ms/step - loss: 1.0482 - mean\_absolute\_error: 0.8196\
\
``\
\
416/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:44 240ms/step - loss: 1.0481 - mean\_absolute\_error: 0.8196\
\
``\
\
417/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:44 240ms/step - loss: 1.0481 - mean\_absolute\_error: 0.8196\
\
``\
\
418/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:43 240ms/step - loss: 1.0480 - mean\_absolute\_error: 0.8196\
\
``\
\
419/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:43 241ms/step - loss: 1.0480 - mean\_absolute\_error: 0.8195\
\
``\
\
420/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:43 241ms/step - loss: 1.0480 - mean\_absolute\_error: 0.8195\
\
``\
\
421/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:43 241ms/step - loss: 1.0479 - mean\_absolute\_error: 0.8195\
\
``\
\
422/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:43 241ms/step - loss: 1.0479 - mean\_absolute\_error: 0.8195\
\
``\
\
423/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:43 241ms/step - loss: 1.0478 - mean\_absolute\_error: 0.8195\
\
``\
\
424/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:42 241ms/step - loss: 1.0478 - mean\_absolute\_error: 0.8194\
\
``\
\
425/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:42 241ms/step - loss: 1.0477 - mean\_absolute\_error: 0.8194\
\
``\
\
426/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:42 241ms/step - loss: 1.0477 - mean\_absolute\_error: 0.8194\
\
``\
\
427/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:42 241ms/step - loss: 1.0476 - mean\_absolute\_error: 0.8194\
\
``\
\
428/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:41 241ms/step - loss: 1.0476 - mean\_absolute\_error: 0.8194\
\
``\
\
429/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:41 241ms/step - loss: 1.0476 - mean\_absolute\_error: 0.8194\
\
``\
\
430/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:41 241ms/step - loss: 1.0475 - mean\_absolute\_error: 0.8193\
\
``\
\
431/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:41 241ms/step - loss: 1.0475 - mean\_absolute\_error: 0.8193\
\
``\
\
432/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:41 241ms/step - loss: 1.0474 - mean\_absolute\_error: 0.8193\
\
``\
\
433/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:40 241ms/step - loss: 1.0474 - mean\_absolute\_error: 0.8193\
\
``\
\
434/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:40 241ms/step - loss: 1.0473 - mean\_absolute\_error: 0.8193\
\
``\
\
435/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:40 241ms/step - loss: 1.0473 - mean\_absolute\_error: 0.8192\
\
``\
\
436/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:40 241ms/step - loss: 1.0472 - mean\_absolute\_error: 0.8192\
\
``\
\
437/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:40 241ms/step - loss: 1.0472 - mean\_absolute\_error: 0.8192\
\
``\
\
438/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:39 241ms/step - loss: 1.0471 - mean\_absolute\_error: 0.8192\
\
``\
\
439/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:39 241ms/step - loss: 1.0471 - mean\_absolute\_error: 0.8192\
\
``\
\
440/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:39 241ms/step - loss: 1.0471 - mean\_absolute\_error: 0.8191\
\
``\
\
441/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:39 241ms/step - loss: 1.0470 - mean\_absolute\_error: 0.8191\
\
``\
\
442/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:39 241ms/step - loss: 1.0470 - mean\_absolute\_error: 0.8191\
\
``\
\
443/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:38 241ms/step - loss: 1.0469 - mean\_absolute\_error: 0.8191\
\
``\
\
444/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:38 241ms/step - loss: 1.0469 - mean\_absolute\_error: 0.8191\
\
``\
\
445/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:38 241ms/step - loss: 1.0468 - mean\_absolute\_error: 0.8191\
\
``\
\
446/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:38 241ms/step - loss: 1.0468 - mean\_absolute\_error: 0.8190\
\
``\
\
447/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:38 241ms/step - loss: 1.0467 - mean\_absolute\_error: 0.8190\
\
``\
\
448/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 241ms/step - loss: 1.0467 - mean\_absolute\_error: 0.8190\
\
``\
\
449/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 241ms/step - loss: 1.0466 - mean\_absolute\_error: 0.8190\
\
``\
\
450/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0466 - mean\_absolute\_error: 0.8190\
\
``\
\
451/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0465 - mean\_absolute\_error: 0.8189\
\
``\
\
452/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0465 - mean\_absolute\_error: 0.8189\
\
``\
\
453/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0464 - mean\_absolute\_error: 0.8189\
\
``\
\
454/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0464 - mean\_absolute\_error: 0.8189\
\
``\
\
455/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0464 - mean\_absolute\_error: 0.8189\
\
``\
\
456/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:37 242ms/step - loss: 1.0463 - mean\_absolute\_error: 0.8188\
\
``\
\
457/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:36 242ms/step - loss: 1.0463 - mean\_absolute\_error: 0.8188\
\
``\
\
458/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:36 243ms/step - loss: 1.0462 - mean\_absolute\_error: 0.8188\
\
``\
\
459/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:36 243ms/step - loss: 1.0462 - mean\_absolute\_error: 0.8188\
\
``\
\
460/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:36 243ms/step - loss: 1.0461 - mean\_absolute\_error: 0.8188\
\
``\
\
461/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:35 243ms/step - loss: 1.0461 - mean\_absolute\_error: 0.8187\
\
``\
\
462/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:35 243ms/step - loss: 1.0460 - mean\_absolute\_error: 0.8187\
\
``\
\
463/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:35 242ms/step - loss: 1.0460 - mean\_absolute\_error: 0.8187\
\
``\
\
464/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:35 242ms/step - loss: 1.0459 - mean\_absolute\_error: 0.8187\
\
``\
\
465/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:34 242ms/step - loss: 1.0459 - mean\_absolute\_error: 0.8187\
\
``\
\
466/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:34 242ms/step - loss: 1.0458 - mean\_absolute\_error: 0.8186\
\
``\
\
467/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:34 242ms/step - loss: 1.0458 - mean\_absolute\_error: 0.8186\
\
``\
\
468/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:33 242ms/step - loss: 1.0457 - mean\_absolute\_error: 0.8186\
\
``\
\
469/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:33 242ms/step - loss: 1.0457 - mean\_absolute\_error: 0.8186\
\
``\
\
470/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:33 242ms/step - loss: 1.0456 - mean\_absolute\_error: 0.8186\
\
``\
\
471/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:33 242ms/step - loss: 1.0456 - mean\_absolute\_error: 0.8185\
\
``\
\
472/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:32 242ms/step - loss: 1.0455 - mean\_absolute\_error: 0.8185\
\
``\
\
473/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:32 242ms/step - loss: 1.0455 - mean\_absolute\_error: 0.8185\
\
``\
\
474/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:32 242ms/step - loss: 1.0454 - mean\_absolute\_error: 0.8185\
\
``\
\
475/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:32 242ms/step - loss: 1.0454 - mean\_absolute\_error: 0.8185\
\
``\
\
476/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:31 242ms/step - loss: 1.0453 - mean\_absolute\_error: 0.8184\
\
``\
\
477/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:31 242ms/step - loss: 1.0453 - mean\_absolute\_error: 0.8184\
\
``\
\
478/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:31 242ms/step - loss: 1.0452 - mean\_absolute\_error: 0.8184\
\
``\
\
479/1599 ━━━━━\[37m━━━━━━━━━━━━━━━ 4:31 242ms/step - loss: 1.0452 - mean\_absolute\_error: 0.8184\
\
``\
\
480/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:30 242ms/step - loss: 1.0451 - mean\_absolute\_error: 0.8184\
\
``\
\
481/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:30 242ms/step - loss: 1.0451 - mean\_absolute\_error: 0.8183\
\
``\
\
482/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:30 242ms/step - loss: 1.0450 - mean\_absolute\_error: 0.8183\
\
``\
\
483/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:30 242ms/step - loss: 1.0450 - mean\_absolute\_error: 0.8183\
\
``\
\
484/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:29 242ms/step - loss: 1.0449 - mean\_absolute\_error: 0.8183\
\
``\
\
485/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:29 242ms/step - loss: 1.0449 - mean\_absolute\_error: 0.8183\
\
``\
\
486/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:29 242ms/step - loss: 1.0448 - mean\_absolute\_error: 0.8182\
\
``\
\
487/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:29 242ms/step - loss: 1.0448 - mean\_absolute\_error: 0.8182\
\
``\
\
488/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:29 242ms/step - loss: 1.0447 - mean\_absolute\_error: 0.8182\
\
``\
\
489/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:29 242ms/step - loss: 1.0447 - mean\_absolute\_error: 0.8182\
\
``\
\
490/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:28 242ms/step - loss: 1.0447 - mean\_absolute\_error: 0.8182\
\
``\
\
491/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:28 242ms/step - loss: 1.0446 - mean\_absolute\_error: 0.8181\
\
``\
\
492/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:28 242ms/step - loss: 1.0446 - mean\_absolute\_error: 0.8181\
\
``\
\
493/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:28 243ms/step - loss: 1.0445 - mean\_absolute\_error: 0.8181\
\
``\
\
494/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:28 243ms/step - loss: 1.0445 - mean\_absolute\_error: 0.8181\
\
``\
\
495/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:27 243ms/step - loss: 1.0444 - mean\_absolute\_error: 0.8181\
\
``\
\
496/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:27 243ms/step - loss: 1.0444 - mean\_absolute\_error: 0.8180\
\
``\
\
497/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:27 243ms/step - loss: 1.0443 - mean\_absolute\_error: 0.8180\
\
``\
\
498/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:27 243ms/step - loss: 1.0443 - mean\_absolute\_error: 0.8180\
\
``\
\
499/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:27 243ms/step - loss: 1.0443 - mean\_absolute\_error: 0.8180\
\
``\
\
500/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:27 243ms/step - loss: 1.0442 - mean\_absolute\_error: 0.8180\
\
``\
\
501/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 243ms/step - loss: 1.0442 - mean\_absolute\_error: 0.8180\
\
``\
\
502/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 243ms/step - loss: 1.0441 - mean\_absolute\_error: 0.8179\
\
``\
\
503/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 243ms/step - loss: 1.0441 - mean\_absolute\_error: 0.8179\
\
``\
\
504/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 243ms/step - loss: 1.0440 - mean\_absolute\_error: 0.8179\
\
``\
\
505/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 243ms/step - loss: 1.0440 - mean\_absolute\_error: 0.8179\
\
``\
\
506/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 244ms/step - loss: 1.0440 - mean\_absolute\_error: 0.8179\
\
``\
\
507/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:26 244ms/step - loss: 1.0439 - mean\_absolute\_error: 0.8178\
\
``\
\
508/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:25 244ms/step - loss: 1.0439 - mean\_absolute\_error: 0.8178\
\
``\
\
509/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:25 244ms/step - loss: 1.0438 - mean\_absolute\_error: 0.8178\
\
``\
\
510/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:25 244ms/step - loss: 1.0438 - mean\_absolute\_error: 0.8178\
\
``\
\
511/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:25 244ms/step - loss: 1.0437 - mean\_absolute\_error: 0.8178\
\
``\
\
512/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:25 244ms/step - loss: 1.0437 - mean\_absolute\_error: 0.8178\
\
``\
\
513/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:24 244ms/step - loss: 1.0437 - mean\_absolute\_error: 0.8177\
\
``\
\
514/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:24 244ms/step - loss: 1.0436 - mean\_absolute\_error: 0.8177\
\
``\
\
515/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:24 244ms/step - loss: 1.0436 - mean\_absolute\_error: 0.8177\
\
``\
\
516/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:24 244ms/step - loss: 1.0435 - mean\_absolute\_error: 0.8177\
\
``\
\
517/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:23 244ms/step - loss: 1.0435 - mean\_absolute\_error: 0.8177\
\
``\
\
518/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:23 244ms/step - loss: 1.0435 - mean\_absolute\_error: 0.8177\
\
``\
\
519/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:23 244ms/step - loss: 1.0434 - mean\_absolute\_error: 0.8176\
\
``\
\
520/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:23 244ms/step - loss: 1.0434 - mean\_absolute\_error: 0.8176\
\
``\
\
521/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:22 244ms/step - loss: 1.0433 - mean\_absolute\_error: 0.8176\
\
``\
\
522/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:22 244ms/step - loss: 1.0433 - mean\_absolute\_error: 0.8176\
\
``\
\
523/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:22 244ms/step - loss: 1.0433 - mean\_absolute\_error: 0.8176\
\
``\
\
524/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:22 244ms/step - loss: 1.0432 - mean\_absolute\_error: 0.8176\
\
``\
\
525/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:21 244ms/step - loss: 1.0432 - mean\_absolute\_error: 0.8175\
\
``\
\
526/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:21 244ms/step - loss: 1.0431 - mean\_absolute\_error: 0.8175\
\
``\
\
527/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:21 244ms/step - loss: 1.0431 - mean\_absolute\_error: 0.8175\
\
``\
\
528/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:21 244ms/step - loss: 1.0430 - mean\_absolute\_error: 0.8175\
\
``\
\
529/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:20 244ms/step - loss: 1.0430 - mean\_absolute\_error: 0.8175\
\
``\
\
530/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:20 244ms/step - loss: 1.0430 - mean\_absolute\_error: 0.8175\
\
``\
\
531/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:20 244ms/step - loss: 1.0429 - mean\_absolute\_error: 0.8174\
\
``\
\
532/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:20 244ms/step - loss: 1.0429 - mean\_absolute\_error: 0.8174\
\
``\
\
533/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:20 244ms/step - loss: 1.0428 - mean\_absolute\_error: 0.8174\
\
``\
\
534/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:19 244ms/step - loss: 1.0428 - mean\_absolute\_error: 0.8174\
\
``\
\
535/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:19 244ms/step - loss: 1.0428 - mean\_absolute\_error: 0.8174\
\
``\
\
536/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:19 244ms/step - loss: 1.0427 - mean\_absolute\_error: 0.8174\
\
``\
\
537/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:19 244ms/step - loss: 1.0427 - mean\_absolute\_error: 0.8173\
\
``\
\
538/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:18 244ms/step - loss: 1.0426 - mean\_absolute\_error: 0.8173\
\
``\
\
539/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:18 244ms/step - loss: 1.0426 - mean\_absolute\_error: 0.8173\
\
``\
\
540/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:18 244ms/step - loss: 1.0426 - mean\_absolute\_error: 0.8173\
\
``\
\
541/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:18 244ms/step - loss: 1.0425 - mean\_absolute\_error: 0.8173\
\
``\
\
542/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:17 244ms/step - loss: 1.0425 - mean\_absolute\_error: 0.8173\
\
``\
\
543/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:17 244ms/step - loss: 1.0425 - mean\_absolute\_error: 0.8172\
\
``\
\
544/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:17 244ms/step - loss: 1.0424 - mean\_absolute\_error: 0.8172\
\
``\
\
545/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:17 244ms/step - loss: 1.0424 - mean\_absolute\_error: 0.8172\
\
``\
\
546/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:17 244ms/step - loss: 1.0423 - mean\_absolute\_error: 0.8172\
\
``\
\
547/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:16 244ms/step - loss: 1.0423 - mean\_absolute\_error: 0.8172\
\
``\
\
548/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:16 244ms/step - loss: 1.0423 - mean\_absolute\_error: 0.8172\
\
``\
\
549/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:16 244ms/step - loss: 1.0422 - mean\_absolute\_error: 0.8171\
\
``\
\
550/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:16 244ms/step - loss: 1.0422 - mean\_absolute\_error: 0.8171\
\
``\
\
551/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:15 244ms/step - loss: 1.0422 - mean\_absolute\_error: 0.8171\
\
``\
\
552/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:15 244ms/step - loss: 1.0421 - mean\_absolute\_error: 0.8171\
\
``\
\
553/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:15 244ms/step - loss: 1.0421 - mean\_absolute\_error: 0.8171\
\
``\
\
554/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:15 244ms/step - loss: 1.0420 - mean\_absolute\_error: 0.8171\
\
``\
\
555/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:15 244ms/step - loss: 1.0420 - mean\_absolute\_error: 0.8171\
\
``\
\
556/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:14 244ms/step - loss: 1.0420 - mean\_absolute\_error: 0.8170\
\
``\
\
557/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:14 244ms/step - loss: 1.0419 - mean\_absolute\_error: 0.8170\
\
``\
\
558/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:14 244ms/step - loss: 1.0419 - mean\_absolute\_error: 0.8170\
\
``\
\
559/1599 ━━━━━━\[37m━━━━━━━━━━━━━━ 4:14 244ms/step - loss: 1.0419 - mean\_absolute\_error: 0.8170\
\
``\
\
560/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:14 245ms/step - loss: 1.0418 - mean\_absolute\_error: 0.8170\
\
``\
\
561/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0418 - mean\_absolute\_error: 0.8170\
\
``\
\
562/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0417 - mean\_absolute\_error: 0.8169\
\
``\
\
563/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0417 - mean\_absolute\_error: 0.8169\
\
``\
\
564/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0417 - mean\_absolute\_error: 0.8169\
\
``\
\
565/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0416 - mean\_absolute\_error: 0.8169\
\
``\
\
566/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0416 - mean\_absolute\_error: 0.8169\
\
``\
\
567/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0416 - mean\_absolute\_error: 0.8169\
\
``\
\
568/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:13 245ms/step - loss: 1.0415 - mean\_absolute\_error: 0.8169\
\
``\
\
569/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:12 245ms/step - loss: 1.0415 - mean\_absolute\_error: 0.8168\
\
``\
\
570/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:12 246ms/step - loss: 1.0415 - mean\_absolute\_error: 0.8168\
\
``\
\
571/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:12 246ms/step - loss: 1.0414 - mean\_absolute\_error: 0.8168\
\
``\
\
572/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:12 246ms/step - loss: 1.0414 - mean\_absolute\_error: 0.8168\
\
``\
\
573/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:11 246ms/step - loss: 1.0414 - mean\_absolute\_error: 0.8168\
\
``\
\
574/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:11 246ms/step - loss: 1.0413 - mean\_absolute\_error: 0.8168\
\
``\
\
575/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:11 246ms/step - loss: 1.0413 - mean\_absolute\_error: 0.8168\
\
``\
\
576/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:11 246ms/step - loss: 1.0413 - mean\_absolute\_error: 0.8167\
\
``\
\
577/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:11 246ms/step - loss: 1.0412 - mean\_absolute\_error: 0.8167\
\
``\
\
578/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:11 246ms/step - loss: 1.0412 - mean\_absolute\_error: 0.8167\
\
``\
\
579/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:10 246ms/step - loss: 1.0411 - mean\_absolute\_error: 0.8167\
\
``\
\
580/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:10 246ms/step - loss: 1.0411 - mean\_absolute\_error: 0.8167\
\
``\
\
581/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:10 246ms/step - loss: 1.0411 - mean\_absolute\_error: 0.8167\
\
``\
\
582/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:10 246ms/step - loss: 1.0410 - mean\_absolute\_error: 0.8167\
\
``\
\
583/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:10 246ms/step - loss: 1.0410 - mean\_absolute\_error: 0.8166\
\
``\
\
584/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:10 246ms/step - loss: 1.0410 - mean\_absolute\_error: 0.8166\
\
``\
\
585/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:09 247ms/step - loss: 1.0409 - mean\_absolute\_error: 0.8166\
\
``\
\
586/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:09 247ms/step - loss: 1.0409 - mean\_absolute\_error: 0.8166\
\
``\
\
587/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:09 247ms/step - loss: 1.0409 - mean\_absolute\_error: 0.8166\
\
``\
\
588/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:09 247ms/step - loss: 1.0408 - mean\_absolute\_error: 0.8166\
\
``\
\
589/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:09 247ms/step - loss: 1.0408 - mean\_absolute\_error: 0.8166\
\
``\
\
590/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:08 247ms/step - loss: 1.0408 - mean\_absolute\_error: 0.8165\
\
``\
\
591/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:08 247ms/step - loss: 1.0407 - mean\_absolute\_error: 0.8165\
\
``\
\
592/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:08 247ms/step - loss: 1.0407 - mean\_absolute\_error: 0.8165\
\
``\
\
593/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:08 247ms/step - loss: 1.0406 - mean\_absolute\_error: 0.8165\
\
``\
\
594/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:08 247ms/step - loss: 1.0406 - mean\_absolute\_error: 0.8165\
\
``\
\
595/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:07 247ms/step - loss: 1.0406 - mean\_absolute\_error: 0.8165\
\
``\
\
596/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:07 247ms/step - loss: 1.0405 - mean\_absolute\_error: 0.8165\
\
``\
\
597/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:07 247ms/step - loss: 1.0405 - mean\_absolute\_error: 0.8164\
\
``\
\
598/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:07 247ms/step - loss: 1.0405 - mean\_absolute\_error: 0.8164\
\
``\
\
599/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:06 247ms/step - loss: 1.0404 - mean\_absolute\_error: 0.8164\
\
``\
\
600/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:06 247ms/step - loss: 1.0404 - mean\_absolute\_error: 0.8164\
\
``\
\
601/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:06 247ms/step - loss: 1.0404 - mean\_absolute\_error: 0.8164\
\
``\
\
602/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:06 247ms/step - loss: 1.0403 - mean\_absolute\_error: 0.8164\
\
``\
\
603/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:05 247ms/step - loss: 1.0403 - mean\_absolute\_error: 0.8164\
\
``\
\
604/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:05 247ms/step - loss: 1.0403 - mean\_absolute\_error: 0.8163\
\
``\
\
605/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:05 247ms/step - loss: 1.0402 - mean\_absolute\_error: 0.8163\
\
``\
\
606/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:05 247ms/step - loss: 1.0402 - mean\_absolute\_error: 0.8163\
\
``\
\
607/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:04 247ms/step - loss: 1.0402 - mean\_absolute\_error: 0.8163\
\
``\
\
608/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:04 247ms/step - loss: 1.0401 - mean\_absolute\_error: 0.8163\
\
``\
\
609/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:04 247ms/step - loss: 1.0401 - mean\_absolute\_error: 0.8163\
\
``\
\
610/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:04 247ms/step - loss: 1.0400 - mean\_absolute\_error: 0.8163\
\
``\
\
611/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:03 247ms/step - loss: 1.0400 - mean\_absolute\_error: 0.8162\
\
``\
\
612/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:03 247ms/step - loss: 1.0400 - mean\_absolute\_error: 0.8162\
\
``\
\
613/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:03 247ms/step - loss: 1.0399 - mean\_absolute\_error: 0.8162\
\
``\
\
614/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:03 247ms/step - loss: 1.0399 - mean\_absolute\_error: 0.8162\
\
``\
\
615/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:03 247ms/step - loss: 1.0399 - mean\_absolute\_error: 0.8162\
\
``\
\
616/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:02 247ms/step - loss: 1.0398 - mean\_absolute\_error: 0.8162\
\
``\
\
617/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:02 247ms/step - loss: 1.0398 - mean\_absolute\_error: 0.8162\
\
``\
\
618/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:02 247ms/step - loss: 1.0398 - mean\_absolute\_error: 0.8161\
\
``\
\
619/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:02 247ms/step - loss: 1.0397 - mean\_absolute\_error: 0.8161\
\
``\
\
620/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:01 247ms/step - loss: 1.0397 - mean\_absolute\_error: 0.8161\
\
``\
\
621/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:01 247ms/step - loss: 1.0397 - mean\_absolute\_error: 0.8161\
\
``\
\
622/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:01 247ms/step - loss: 1.0396 - mean\_absolute\_error: 0.8161\
\
``\
\
623/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:01 247ms/step - loss: 1.0396 - mean\_absolute\_error: 0.8161\
\
``\
\
624/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:01 247ms/step - loss: 1.0396 - mean\_absolute\_error: 0.8161\
\
``\
\
625/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:01 248ms/step - loss: 1.0395 - mean\_absolute\_error: 0.8161\
\
``\
\
626/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:00 248ms/step - loss: 1.0395 - mean\_absolute\_error: 0.8160\
\
``\
\
627/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:00 248ms/step - loss: 1.0395 - mean\_absolute\_error: 0.8160\
\
``\
\
628/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:00 248ms/step - loss: 1.0394 - mean\_absolute\_error: 0.8160\
\
``\
\
629/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 4:00 248ms/step - loss: 1.0394 - mean\_absolute\_error: 0.8160\
\
``\
\
630/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:59 248ms/step - loss: 1.0394 - mean\_absolute\_error: 0.8160\
\
``\
\
631/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:59 248ms/step - loss: 1.0394 - mean\_absolute\_error: 0.8160\
\
``\
\
632/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:59 247ms/step - loss: 1.0393 - mean\_absolute\_error: 0.8160\
\
``\
\
633/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:59 247ms/step - loss: 1.0393 - mean\_absolute\_error: 0.8159\
\
``\
\
634/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:58 247ms/step - loss: 1.0393 - mean\_absolute\_error: 0.8159\
\
``\
\
635/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:58 247ms/step - loss: 1.0392 - mean\_absolute\_error: 0.8159\
\
``\
\
636/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:58 247ms/step - loss: 1.0392 - mean\_absolute\_error: 0.8159\
\
``\
\
637/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:58 247ms/step - loss: 1.0392 - mean\_absolute\_error: 0.8159\
\
``\
\
638/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:57 247ms/step - loss: 1.0391 - mean\_absolute\_error: 0.8159\
\
``\
\
639/1599 ━━━━━━━\[37m━━━━━━━━━━━━━ 3:57 247ms/step - loss: 1.0391 - mean\_absolute\_error: 0.8159\
\
``\
\
640/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:57 247ms/step - loss: 1.0391 - mean\_absolute\_error: 0.8159\
\
``\
\
641/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:57 247ms/step - loss: 1.0390 - mean\_absolute\_error: 0.8158\
\
``\
\
642/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:56 247ms/step - loss: 1.0390 - mean\_absolute\_error: 0.8158\
\
``\
\
643/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:56 247ms/step - loss: 1.0390 - mean\_absolute\_error: 0.8158\
\
``\
\
644/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:56 247ms/step - loss: 1.0389 - mean\_absolute\_error: 0.8158\
\
``\
\
645/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:56 247ms/step - loss: 1.0389 - mean\_absolute\_error: 0.8158\
\
``\
\
646/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:55 247ms/step - loss: 1.0389 - mean\_absolute\_error: 0.8158\
\
``\
\
647/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:55 248ms/step - loss: 1.0389 - mean\_absolute\_error: 0.8158\
\
``\
\
648/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:55 248ms/step - loss: 1.0388 - mean\_absolute\_error: 0.8158\
\
``\
\
649/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:55 248ms/step - loss: 1.0388 - mean\_absolute\_error: 0.8157\
\
``\
\
650/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:55 248ms/step - loss: 1.0388 - mean\_absolute\_error: 0.8157\
\
``\
\
651/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:54 248ms/step - loss: 1.0387 - mean\_absolute\_error: 0.8157\
\
``\
\
652/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:54 248ms/step - loss: 1.0387 - mean\_absolute\_error: 0.8157\
\
``\
\
653/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:54 248ms/step - loss: 1.0387 - mean\_absolute\_error: 0.8157\
\
``\
\
654/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:54 248ms/step - loss: 1.0386 - mean\_absolute\_error: 0.8157\
\
``\
\
655/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:54 248ms/step - loss: 1.0386 - mean\_absolute\_error: 0.8157\
\
``\
\
656/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:54 248ms/step - loss: 1.0386 - mean\_absolute\_error: 0.8157\
\
``\
\
657/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:53 248ms/step - loss: 1.0386 - mean\_absolute\_error: 0.8156\
\
``\
\
658/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:53 248ms/step - loss: 1.0385 - mean\_absolute\_error: 0.8156\
\
``\
\
659/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:53 248ms/step - loss: 1.0385 - mean\_absolute\_error: 0.8156\
\
``\
\
660/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:53 248ms/step - loss: 1.0385 - mean\_absolute\_error: 0.8156\
\
``\
\
661/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:52 248ms/step - loss: 1.0384 - mean\_absolute\_error: 0.8156\
\
``\
\
662/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:52 248ms/step - loss: 1.0384 - mean\_absolute\_error: 0.8156\
\
``\
\
663/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:52 248ms/step - loss: 1.0384 - mean\_absolute\_error: 0.8156\
\
``\
\
664/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:52 248ms/step - loss: 1.0384 - mean\_absolute\_error: 0.8156\
\
``\
\
665/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:51 248ms/step - loss: 1.0383 - mean\_absolute\_error: 0.8155\
\
``\
\
666/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:51 248ms/step - loss: 1.0383 - mean\_absolute\_error: 0.8155\
\
``\
\
667/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:51 248ms/step - loss: 1.0383 - mean\_absolute\_error: 0.8155\
\
``\
\
668/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:51 248ms/step - loss: 1.0382 - mean\_absolute\_error: 0.8155\
\
``\
\
669/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:50 248ms/step - loss: 1.0382 - mean\_absolute\_error: 0.8155\
\
``\
\
670/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:50 248ms/step - loss: 1.0382 - mean\_absolute\_error: 0.8155\
\
``\
\
671/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:50 248ms/step - loss: 1.0382 - mean\_absolute\_error: 0.8155\
\
``\
\
672/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:50 248ms/step - loss: 1.0381 - mean\_absolute\_error: 0.8155\
\
``\
\
673/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:49 248ms/step - loss: 1.0381 - mean\_absolute\_error: 0.8155\
\
``\
\
674/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:49 248ms/step - loss: 1.0381 - mean\_absolute\_error: 0.8154\
\
``\
\
675/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:49 248ms/step - loss: 1.0380 - mean\_absolute\_error: 0.8154\
\
``\
\
676/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:49 248ms/step - loss: 1.0380 - mean\_absolute\_error: 0.8154\
\
``\
\
677/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:48 248ms/step - loss: 1.0380 - mean\_absolute\_error: 0.8154\
\
``\
\
678/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:48 248ms/step - loss: 1.0380 - mean\_absolute\_error: 0.8154\
\
``\
\
679/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:48 248ms/step - loss: 1.0379 - mean\_absolute\_error: 0.8154\
\
``\
\
680/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:48 248ms/step - loss: 1.0379 - mean\_absolute\_error: 0.8154\
\
``\
\
681/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:48 248ms/step - loss: 1.0379 - mean\_absolute\_error: 0.8154\
\
``\
\
682/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:47 249ms/step - loss: 1.0379 - mean\_absolute\_error: 0.8154\
\
``\
\
683/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:47 249ms/step - loss: 1.0378 - mean\_absolute\_error: 0.8153\
\
``\
\
684/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:47 249ms/step - loss: 1.0378 - mean\_absolute\_error: 0.8153\
\
``\
\
685/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:47 249ms/step - loss: 1.0378 - mean\_absolute\_error: 0.8153\
\
``\
\
686/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:46 249ms/step - loss: 1.0378 - mean\_absolute\_error: 0.8153\
\
``\
\
687/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:46 249ms/step - loss: 1.0377 - mean\_absolute\_error: 0.8153\
\
``\
\
688/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:46 249ms/step - loss: 1.0377 - mean\_absolute\_error: 0.8153\
\
``\
\
689/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:46 249ms/step - loss: 1.0377 - mean\_absolute\_error: 0.8153\
\
``\
\
690/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:45 249ms/step - loss: 1.0376 - mean\_absolute\_error: 0.8153\
\
``\
\
691/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:45 249ms/step - loss: 1.0376 - mean\_absolute\_error: 0.8153\
\
``\
\
692/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:45 249ms/step - loss: 1.0376 - mean\_absolute\_error: 0.8152\
\
``\
\
693/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:45 249ms/step - loss: 1.0376 - mean\_absolute\_error: 0.8152\
\
``\
\
694/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:44 249ms/step - loss: 1.0375 - mean\_absolute\_error: 0.8152\
\
``\
\
695/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:44 249ms/step - loss: 1.0375 - mean\_absolute\_error: 0.8152\
\
``\
\
696/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:44 249ms/step - loss: 1.0375 - mean\_absolute\_error: 0.8152\
\
``\
\
697/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:44 249ms/step - loss: 1.0375 - mean\_absolute\_error: 0.8152\
\
``\
\
698/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:43 249ms/step - loss: 1.0374 - mean\_absolute\_error: 0.8152\
\
``\
\
699/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:43 249ms/step - loss: 1.0374 - mean\_absolute\_error: 0.8152\
\
``\
\
700/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:43 249ms/step - loss: 1.0374 - mean\_absolute\_error: 0.8152\
\
``\
\
701/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:43 249ms/step - loss: 1.0374 - mean\_absolute\_error: 0.8151\
\
``\
\
702/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:42 249ms/step - loss: 1.0373 - mean\_absolute\_error: 0.8151\
\
``\
\
703/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:42 249ms/step - loss: 1.0373 - mean\_absolute\_error: 0.8151\
\
``\
\
704/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:42 249ms/step - loss: 1.0373 - mean\_absolute\_error: 0.8151\
\
``\
\
705/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:42 249ms/step - loss: 1.0373 - mean\_absolute\_error: 0.8151\
\
``\
\
706/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:41 249ms/step - loss: 1.0372 - mean\_absolute\_error: 0.8151\
\
``\
\
707/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:41 249ms/step - loss: 1.0372 - mean\_absolute\_error: 0.8151\
\
``\
\
708/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:41 249ms/step - loss: 1.0372 - mean\_absolute\_error: 0.8151\
\
``\
\
709/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:41 249ms/step - loss: 1.0372 - mean\_absolute\_error: 0.8151\
\
``\
\
710/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:41 249ms/step - loss: 1.0371 - mean\_absolute\_error: 0.8150\
\
``\
\
711/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:41 249ms/step - loss: 1.0371 - mean\_absolute\_error: 0.8150\
\
``\
\
712/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:40 249ms/step - loss: 1.0371 - mean\_absolute\_error: 0.8150\
\
``\
\
713/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:40 249ms/step - loss: 1.0370 - mean\_absolute\_error: 0.8150\
\
``\
\
714/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:40 249ms/step - loss: 1.0370 - mean\_absolute\_error: 0.8150\
\
``\
\
715/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:40 249ms/step - loss: 1.0370 - mean\_absolute\_error: 0.8150\
\
``\
\
716/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:39 249ms/step - loss: 1.0370 - mean\_absolute\_error: 0.8150\
\
``\
\
717/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:39 249ms/step - loss: 1.0369 - mean\_absolute\_error: 0.8150\
\
``\
\
718/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:39 249ms/step - loss: 1.0369 - mean\_absolute\_error: 0.8150\
\
``\
\
719/1599 ━━━━━━━━\[37m━━━━━━━━━━━━ 3:38 249ms/step - loss: 1.0369 - mean\_absolute\_error: 0.8150\
\
``\
\
720/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:38 249ms/step - loss: 1.0369 - mean\_absolute\_error: 0.8149\
\
``\
\
721/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:38 249ms/step - loss: 1.0368 - mean\_absolute\_error: 0.8149\
\
``\
\
722/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:38 249ms/step - loss: 1.0368 - mean\_absolute\_error: 0.8149\
\
``\
\
723/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0368 - mean\_absolute\_error: 0.8149\
\
``\
\
724/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0368 - mean\_absolute\_error: 0.8149\
\
``\
\
725/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0368 - mean\_absolute\_error: 0.8149\
\
``\
\
726/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0367 - mean\_absolute\_error: 0.8149\
\
``\
\
727/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0367 - mean\_absolute\_error: 0.8149\
\
``\
\
728/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0367 - mean\_absolute\_error: 0.8149\
\
``\
\
729/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:37 249ms/step - loss: 1.0367 - mean\_absolute\_error: 0.8148\
\
``\
\
730/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:36 249ms/step - loss: 1.0366 - mean\_absolute\_error: 0.8148\
\
``\
\
731/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:36 249ms/step - loss: 1.0366 - mean\_absolute\_error: 0.8148\
\
``\
\
732/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:36 249ms/step - loss: 1.0366 - mean\_absolute\_error: 0.8148\
\
``\
\
733/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:35 249ms/step - loss: 1.0366 - mean\_absolute\_error: 0.8148\
\
``\
\
734/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:35 249ms/step - loss: 1.0365 - mean\_absolute\_error: 0.8148\
\
``\
\
735/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:35 249ms/step - loss: 1.0365 - mean\_absolute\_error: 0.8148\
\
``\
\
736/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:35 249ms/step - loss: 1.0365 - mean\_absolute\_error: 0.8148\
\
``\
\
737/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:34 249ms/step - loss: 1.0365 - mean\_absolute\_error: 0.8148\
\
``\
\
738/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:34 249ms/step - loss: 1.0364 - mean\_absolute\_error: 0.8148\
\
``\
\
739/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:34 249ms/step - loss: 1.0364 - mean\_absolute\_error: 0.8147\
\
``\
\
740/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:34 249ms/step - loss: 1.0364 - mean\_absolute\_error: 0.8147\
\
``\
\
741/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:33 249ms/step - loss: 1.0364 - mean\_absolute\_error: 0.8147\
\
``\
\
742/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:33 249ms/step - loss: 1.0363 - mean\_absolute\_error: 0.8147\
\
``\
\
743/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:33 249ms/step - loss: 1.0363 - mean\_absolute\_error: 0.8147\
\
``\
\
744/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:33 249ms/step - loss: 1.0363 - mean\_absolute\_error: 0.8147\
\
``\
\
745/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:32 249ms/step - loss: 1.0363 - mean\_absolute\_error: 0.8147\
\
``\
\
746/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:32 249ms/step - loss: 1.0363 - mean\_absolute\_error: 0.8147\
\
``\
\
747/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:32 249ms/step - loss: 1.0362 - mean\_absolute\_error: 0.8147\
\
``\
\
748/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:32 249ms/step - loss: 1.0362 - mean\_absolute\_error: 0.8147\
\
``\
\
749/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:32 249ms/step - loss: 1.0362 - mean\_absolute\_error: 0.8146\
\
``\
\
750/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:31 250ms/step - loss: 1.0362 - mean\_absolute\_error: 0.8146\
\
``\
\
751/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:31 250ms/step - loss: 1.0361 - mean\_absolute\_error: 0.8146\
\
``\
\
752/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:31 250ms/step - loss: 1.0361 - mean\_absolute\_error: 0.8146\
\
``\
\
753/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:31 250ms/step - loss: 1.0361 - mean\_absolute\_error: 0.8146\
\
``\
\
754/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:31 250ms/step - loss: 1.0361 - mean\_absolute\_error: 0.8146\
\
``\
\
755/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:30 250ms/step - loss: 1.0360 - mean\_absolute\_error: 0.8146\
\
``\
\
756/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:30 250ms/step - loss: 1.0360 - mean\_absolute\_error: 0.8146\
\
``\
\
757/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:30 250ms/step - loss: 1.0360 - mean\_absolute\_error: 0.8146\
\
``\
\
758/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:29 250ms/step - loss: 1.0360 - mean\_absolute\_error: 0.8146\
\
``\
\
759/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:29 250ms/step - loss: 1.0360 - mean\_absolute\_error: 0.8146\
\
``\
\
760/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:29 250ms/step - loss: 1.0359 - mean\_absolute\_error: 0.8145\
\
``\
\
761/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:29 250ms/step - loss: 1.0359 - mean\_absolute\_error: 0.8145\
\
``\
\
762/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:29 250ms/step - loss: 1.0359 - mean\_absolute\_error: 0.8145\
\
``\
\
763/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:28 250ms/step - loss: 1.0359 - mean\_absolute\_error: 0.8145\
\
``\
\
764/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:28 250ms/step - loss: 1.0358 - mean\_absolute\_error: 0.8145\
\
``\
\
765/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:28 250ms/step - loss: 1.0358 - mean\_absolute\_error: 0.8145\
\
``\
\
766/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:28 250ms/step - loss: 1.0358 - mean\_absolute\_error: 0.8145\
\
``\
\
767/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:27 250ms/step - loss: 1.0358 - mean\_absolute\_error: 0.8145\
\
``\
\
768/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:27 250ms/step - loss: 1.0358 - mean\_absolute\_error: 0.8145\
\
``\
\
769/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:27 250ms/step - loss: 1.0357 - mean\_absolute\_error: 0.8145\
\
``\
\
770/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:27 250ms/step - loss: 1.0357 - mean\_absolute\_error: 0.8145\
\
``\
\
771/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:26 250ms/step - loss: 1.0357 - mean\_absolute\_error: 0.8144\
\
``\
\
772/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:26 250ms/step - loss: 1.0357 - mean\_absolute\_error: 0.8144\
\
``\
\
773/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:26 250ms/step - loss: 1.0357 - mean\_absolute\_error: 0.8144\
\
``\
\
774/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:26 250ms/step - loss: 1.0356 - mean\_absolute\_error: 0.8144\
\
``\
\
775/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:25 250ms/step - loss: 1.0356 - mean\_absolute\_error: 0.8144\
\
``\
\
776/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:25 250ms/step - loss: 1.0356 - mean\_absolute\_error: 0.8144\
\
``\
\
777/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:25 250ms/step - loss: 1.0356 - mean\_absolute\_error: 0.8144\
\
``\
\
778/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:25 250ms/step - loss: 1.0356 - mean\_absolute\_error: 0.8144\
\
``\
\
779/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:24 250ms/step - loss: 1.0355 - mean\_absolute\_error: 0.8144\
\
``\
\
780/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:24 250ms/step - loss: 1.0355 - mean\_absolute\_error: 0.8144\
\
``\
\
781/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:24 250ms/step - loss: 1.0355 - mean\_absolute\_error: 0.8144\
\
``\
\
782/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:24 250ms/step - loss: 1.0355 - mean\_absolute\_error: 0.8143\
\
``\
\
783/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:24 250ms/step - loss: 1.0355 - mean\_absolute\_error: 0.8143\
\
``\
\
784/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 250ms/step - loss: 1.0354 - mean\_absolute\_error: 0.8143\
\
``\
\
785/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 250ms/step - loss: 1.0354 - mean\_absolute\_error: 0.8143\
\
``\
\
786/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 251ms/step - loss: 1.0354 - mean\_absolute\_error: 0.8143\
\
``\
\
787/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 251ms/step - loss: 1.0354 - mean\_absolute\_error: 0.8143\
\
``\
\
788/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 251ms/step - loss: 1.0354 - mean\_absolute\_error: 0.8143\
\
``\
\
789/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 251ms/step - loss: 1.0353 - mean\_absolute\_error: 0.8143\
\
``\
\
790/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:23 251ms/step - loss: 1.0353 - mean\_absolute\_error: 0.8143\
\
``\
\
791/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:22 251ms/step - loss: 1.0353 - mean\_absolute\_error: 0.8143\
\
``\
\
792/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:22 251ms/step - loss: 1.0353 - mean\_absolute\_error: 0.8143\
\
``\
\
793/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:22 251ms/step - loss: 1.0352 - mean\_absolute\_error: 0.8142\
\
``\
\
794/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:22 251ms/step - loss: 1.0352 - mean\_absolute\_error: 0.8142\
\
``\
\
795/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:22 251ms/step - loss: 1.0352 - mean\_absolute\_error: 0.8142\
\
``\
\
796/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:21 251ms/step - loss: 1.0352 - mean\_absolute\_error: 0.8142\
\
``\
\
797/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:21 251ms/step - loss: 1.0352 - mean\_absolute\_error: 0.8142\
\
``\
\
798/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:21 251ms/step - loss: 1.0351 - mean\_absolute\_error: 0.8142\
\
``\
\
799/1599 ━━━━━━━━━\[37m━━━━━━━━━━━ 3:21 251ms/step - loss: 1.0351 - mean\_absolute\_error: 0.8142\
\
``\
\
800/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:20 251ms/step - loss: 1.0351 - mean\_absolute\_error: 0.8142\
\
``\
\
801/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:20 251ms/step - loss: 1.0351 - mean\_absolute\_error: 0.8142\
\
``\
\
802/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:20 251ms/step - loss: 1.0351 - mean\_absolute\_error: 0.8142\
\
``\
\
803/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:20 251ms/step - loss: 1.0351 - mean\_absolute\_error: 0.8142\
\
``\
\
804/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:19 251ms/step - loss: 1.0350 - mean\_absolute\_error: 0.8141\
\
``\
\
805/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:19 252ms/step - loss: 1.0350 - mean\_absolute\_error: 0.8141\
\
``\
\
806/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:19 252ms/step - loss: 1.0350 - mean\_absolute\_error: 0.8141\
\
``\
\
807/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:19 252ms/step - loss: 1.0350 - mean\_absolute\_error: 0.8141\
\
``\
\
808/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:19 252ms/step - loss: 1.0350 - mean\_absolute\_error: 0.8141\
\
``\
\
809/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:18 252ms/step - loss: 1.0349 - mean\_absolute\_error: 0.8141\
\
``\
\
810/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:18 252ms/step - loss: 1.0349 - mean\_absolute\_error: 0.8141\
\
``\
\
811/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:18 252ms/step - loss: 1.0349 - mean\_absolute\_error: 0.8141\
\
``\
\
812/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:18 252ms/step - loss: 1.0349 - mean\_absolute\_error: 0.8141\
\
``\
\
813/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:17 252ms/step - loss: 1.0349 - mean\_absolute\_error: 0.8141\
\
``\
\
814/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:17 252ms/step - loss: 1.0348 - mean\_absolute\_error: 0.8141\
\
``\
\
815/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:17 252ms/step - loss: 1.0348 - mean\_absolute\_error: 0.8141\
\
``\
\
816/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:17 252ms/step - loss: 1.0348 - mean\_absolute\_error: 0.8140\
\
``\
\
817/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:17 252ms/step - loss: 1.0348 - mean\_absolute\_error: 0.8140\
\
``\
\
818/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:17 252ms/step - loss: 1.0348 - mean\_absolute\_error: 0.8140\
\
``\
\
819/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:16 252ms/step - loss: 1.0347 - mean\_absolute\_error: 0.8140\
\
``\
\
820/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:16 253ms/step - loss: 1.0347 - mean\_absolute\_error: 0.8140\
\
``\
\
821/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:16 253ms/step - loss: 1.0347 - mean\_absolute\_error: 0.8140\
\
``\
\
822/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:16 253ms/step - loss: 1.0347 - mean\_absolute\_error: 0.8140\
\
``\
\
823/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:16 253ms/step - loss: 1.0347 - mean\_absolute\_error: 0.8140\
\
``\
\
824/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:15 253ms/step - loss: 1.0346 - mean\_absolute\_error: 0.8140\
\
``\
\
825/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:15 253ms/step - loss: 1.0346 - mean\_absolute\_error: 0.8140\
\
``\
\
826/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:15 253ms/step - loss: 1.0346 - mean\_absolute\_error: 0.8140\
\
``\
\
827/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:15 253ms/step - loss: 1.0346 - mean\_absolute\_error: 0.8140\
\
``\
\
828/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:15 253ms/step - loss: 1.0346 - mean\_absolute\_error: 0.8139\
\
``\
\
829/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:14 253ms/step - loss: 1.0346 - mean\_absolute\_error: 0.8139\
\
``\
\
830/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:14 253ms/step - loss: 1.0345 - mean\_absolute\_error: 0.8139\
\
``\
\
831/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:14 253ms/step - loss: 1.0345 - mean\_absolute\_error: 0.8139\
\
``\
\
832/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:14 253ms/step - loss: 1.0345 - mean\_absolute\_error: 0.8139\
\
``\
\
833/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:13 253ms/step - loss: 1.0345 - mean\_absolute\_error: 0.8139\
\
``\
\
834/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:13 253ms/step - loss: 1.0345 - mean\_absolute\_error: 0.8139\
\
``\
\
835/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:13 253ms/step - loss: 1.0344 - mean\_absolute\_error: 0.8139\
\
``\
\
836/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:13 253ms/step - loss: 1.0344 - mean\_absolute\_error: 0.8139\
\
``\
\
837/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:12 253ms/step - loss: 1.0344 - mean\_absolute\_error: 0.8139\
\
``\
\
838/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:12 253ms/step - loss: 1.0344 - mean\_absolute\_error: 0.8139\
\
``\
\
839/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:12 253ms/step - loss: 1.0344 - mean\_absolute\_error: 0.8139\
\
``\
\
840/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:12 253ms/step - loss: 1.0344 - mean\_absolute\_error: 0.8138\
\
``\
\
841/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:11 253ms/step - loss: 1.0343 - mean\_absolute\_error: 0.8138\
\
``\
\
842/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:11 253ms/step - loss: 1.0343 - mean\_absolute\_error: 0.8138\
\
``\
\
843/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:11 253ms/step - loss: 1.0343 - mean\_absolute\_error: 0.8138\
\
``\
\
844/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:11 253ms/step - loss: 1.0343 - mean\_absolute\_error: 0.8138\
\
``\
\
845/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:10 253ms/step - loss: 1.0343 - mean\_absolute\_error: 0.8138\
\
``\
\
846/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:10 253ms/step - loss: 1.0343 - mean\_absolute\_error: 0.8138\
\
``\
\
847/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:10 253ms/step - loss: 1.0342 - mean\_absolute\_error: 0.8138\
\
``\
\
848/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:10 253ms/step - loss: 1.0342 - mean\_absolute\_error: 0.8138\
\
``\
\
849/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:09 253ms/step - loss: 1.0342 - mean\_absolute\_error: 0.8138\
\
``\
\
850/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:09 253ms/step - loss: 1.0342 - mean\_absolute\_error: 0.8138\
\
``\
\
851/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:09 253ms/step - loss: 1.0342 - mean\_absolute\_error: 0.8138\
\
``\
\
852/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:09 253ms/step - loss: 1.0341 - mean\_absolute\_error: 0.8138\
\
``\
\
853/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:08 253ms/step - loss: 1.0341 - mean\_absolute\_error: 0.8137\
\
``\
\
854/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:08 253ms/step - loss: 1.0341 - mean\_absolute\_error: 0.8137\
\
``\
\
855/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:08 253ms/step - loss: 1.0341 - mean\_absolute\_error: 0.8137\
\
``\
\
856/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:08 253ms/step - loss: 1.0341 - mean\_absolute\_error: 0.8137\
\
``\
\
857/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:07 253ms/step - loss: 1.0341 - mean\_absolute\_error: 0.8137\
\
``\
\
858/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:07 253ms/step - loss: 1.0340 - mean\_absolute\_error: 0.8137\
\
``\
\
859/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:07 253ms/step - loss: 1.0340 - mean\_absolute\_error: 0.8137\
\
``\
\
860/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:07 253ms/step - loss: 1.0340 - mean\_absolute\_error: 0.8137\
\
``\
\
861/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:06 253ms/step - loss: 1.0340 - mean\_absolute\_error: 0.8137\
\
``\
\
862/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:06 253ms/step - loss: 1.0340 - mean\_absolute\_error: 0.8137\
\
``\
\
863/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:06 253ms/step - loss: 1.0340 - mean\_absolute\_error: 0.8137\
\
``\
\
864/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:06 253ms/step - loss: 1.0339 - mean\_absolute\_error: 0.8137\
\
``\
\
865/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:05 253ms/step - loss: 1.0339 - mean\_absolute\_error: 0.8137\
\
``\
\
866/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:05 253ms/step - loss: 1.0339 - mean\_absolute\_error: 0.8136\
\
``\
\
867/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:05 253ms/step - loss: 1.0339 - mean\_absolute\_error: 0.8136\
\
``\
\
868/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:05 253ms/step - loss: 1.0339 - mean\_absolute\_error: 0.8136\
\
``\
\
869/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:04 253ms/step - loss: 1.0338 - mean\_absolute\_error: 0.8136\
\
``\
\
870/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:04 253ms/step - loss: 1.0338 - mean\_absolute\_error: 0.8136\
\
``\
\
871/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:04 253ms/step - loss: 1.0338 - mean\_absolute\_error: 0.8136\
\
``\
\
872/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:04 253ms/step - loss: 1.0338 - mean\_absolute\_error: 0.8136\
\
``\
\
873/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:03 253ms/step - loss: 1.0338 - mean\_absolute\_error: 0.8136\
\
``\
\
874/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:03 253ms/step - loss: 1.0338 - mean\_absolute\_error: 0.8136\
\
``\
\
875/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:03 253ms/step - loss: 1.0337 - mean\_absolute\_error: 0.8136\
\
``\
\
876/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:03 253ms/step - loss: 1.0337 - mean\_absolute\_error: 0.8136\
\
``\
\
877/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:02 253ms/step - loss: 1.0337 - mean\_absolute\_error: 0.8136\
\
``\
\
878/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:02 253ms/step - loss: 1.0337 - mean\_absolute\_error: 0.8136\
\
``\
\
879/1599 ━━━━━━━━━━\[37m━━━━━━━━━━ 3:02 253ms/step - loss: 1.0337 - mean\_absolute\_error: 0.8135\
\
``\
\
880/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:02 253ms/step - loss: 1.0337 - mean\_absolute\_error: 0.8135\
\
``\
\
881/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:01 253ms/step - loss: 1.0336 - mean\_absolute\_error: 0.8135\
\
``\
\
882/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:01 253ms/step - loss: 1.0336 - mean\_absolute\_error: 0.8135\
\
``\
\
883/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:01 253ms/step - loss: 1.0336 - mean\_absolute\_error: 0.8135\
\
``\
\
884/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:01 253ms/step - loss: 1.0336 - mean\_absolute\_error: 0.8135\
\
``\
\
885/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:00 253ms/step - loss: 1.0336 - mean\_absolute\_error: 0.8135\
\
``\
\
886/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:00 253ms/step - loss: 1.0336 - mean\_absolute\_error: 0.8135\
\
``\
\
887/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:00 253ms/step - loss: 1.0335 - mean\_absolute\_error: 0.8135\
\
``\
\
888/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 3:00 253ms/step - loss: 1.0335 - mean\_absolute\_error: 0.8135\
\
``\
\
889/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:59 253ms/step - loss: 1.0335 - mean\_absolute\_error: 0.8135\
\
``\
\
890/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:59 253ms/step - loss: 1.0335 - mean\_absolute\_error: 0.8135\
\
``\
\
891/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:59 253ms/step - loss: 1.0335 - mean\_absolute\_error: 0.8135\
\
``\
\
892/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:59 253ms/step - loss: 1.0335 - mean\_absolute\_error: 0.8135\
\
``\
\
893/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:58 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
894/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:58 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
895/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:58 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
896/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:58 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
897/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:57 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
898/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:57 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
899/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:57 253ms/step - loss: 1.0334 - mean\_absolute\_error: 0.8134\
\
``\
\
900/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:57 253ms/step - loss: 1.0333 - mean\_absolute\_error: 0.8134\
\
``\
\
901/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:56 253ms/step - loss: 1.0333 - mean\_absolute\_error: 0.8134\
\
``\
\
902/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:56 253ms/step - loss: 1.0333 - mean\_absolute\_error: 0.8134\
\
``\
\
903/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:56 253ms/step - loss: 1.0333 - mean\_absolute\_error: 0.8134\
\
``\
\
904/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:56 253ms/step - loss: 1.0333 - mean\_absolute\_error: 0.8134\
\
``\
\
905/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:55 253ms/step - loss: 1.0333 - mean\_absolute\_error: 0.8134\
\
``\
\
906/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:55 253ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8134\
\
``\
\
907/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:55 253ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8134\
\
``\
\
908/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:55 253ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8133\
\
``\
\
909/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:54 254ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8133\
\
``\
\
910/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:54 254ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8133\
\
``\
\
911/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:54 254ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8133\
\
``\
\
912/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:54 253ms/step - loss: 1.0332 - mean\_absolute\_error: 0.8133\
\
``\
\
913/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:53 253ms/step - loss: 1.0331 - mean\_absolute\_error: 0.8133\
\
``\
\
914/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:53 254ms/step - loss: 1.0331 - mean\_absolute\_error: 0.8133\
\
``\
\
915/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:53 254ms/step - loss: 1.0331 - mean\_absolute\_error: 0.8133\
\
``\
\
916/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:53 254ms/step - loss: 1.0331 - mean\_absolute\_error: 0.8133\
\
``\
\
917/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:52 254ms/step - loss: 1.0331 - mean\_absolute\_error: 0.8133\
\
``\
\
918/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:52 254ms/step - loss: 1.0331 - mean\_absolute\_error: 0.8133\
\
``\
\
919/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:52 254ms/step - loss: 1.0330 - mean\_absolute\_error: 0.8133\
\
``\
\
920/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:52 254ms/step - loss: 1.0330 - mean\_absolute\_error: 0.8133\
\
``\
\
921/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:51 254ms/step - loss: 1.0330 - mean\_absolute\_error: 0.8133\
\
``\
\
922/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:51 254ms/step - loss: 1.0330 - mean\_absolute\_error: 0.8132\
\
``\
\
923/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:51 254ms/step - loss: 1.0330 - mean\_absolute\_error: 0.8132\
\
``\
\
924/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:51 254ms/step - loss: 1.0330 - mean\_absolute\_error: 0.8132\
\
``\
\
925/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:50 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
926/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:50 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
927/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:50 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
928/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:50 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
929/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:50 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
930/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:49 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
931/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:49 254ms/step - loss: 1.0329 - mean\_absolute\_error: 0.8132\
\
``\
\
932/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:49 254ms/step - loss: 1.0328 - mean\_absolute\_error: 0.8132\
\
``\
\
933/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:49 254ms/step - loss: 1.0328 - mean\_absolute\_error: 0.8132\
\
``\
\
934/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:48 254ms/step - loss: 1.0328 - mean\_absolute\_error: 0.8132\
\
``\
\
935/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:48 254ms/step - loss: 1.0328 - mean\_absolute\_error: 0.8131\
\
``\
\
936/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:48 254ms/step - loss: 1.0328 - mean\_absolute\_error: 0.8131\
\
``\
\
937/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:48 254ms/step - loss: 1.0327 - mean\_absolute\_error: 0.8131\
\
``\
\
938/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:47 254ms/step - loss: 1.0327 - mean\_absolute\_error: 0.8131\
\
``\
\
939/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:47 254ms/step - loss: 1.0327 - mean\_absolute\_error: 0.8131\
\
``\
\
940/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:47 254ms/step - loss: 1.0327 - mean\_absolute\_error: 0.8131\
\
``\
\
941/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:46 254ms/step - loss: 1.0327 - mean\_absolute\_error: 0.8131\
\
``\
\
942/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:46 254ms/step - loss: 1.0327 - mean\_absolute\_error: 0.8131\
\
``\
\
943/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:46 254ms/step - loss: 1.0326 - mean\_absolute\_error: 0.8131\
\
``\
\
944/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:46 254ms/step - loss: 1.0326 - mean\_absolute\_error: 0.8131\
\
``\
\
945/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:45 254ms/step - loss: 1.0326 - mean\_absolute\_error: 0.8131\
\
``\
\
946/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:45 254ms/step - loss: 1.0326 - mean\_absolute\_error: 0.8131\
\
``\
\
947/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:45 254ms/step - loss: 1.0326 - mean\_absolute\_error: 0.8131\
\
``\
\
948/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:45 254ms/step - loss: 1.0326 - mean\_absolute\_error: 0.8131\
\
``\
\
949/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:44 254ms/step - loss: 1.0325 - mean\_absolute\_error: 0.8130\
\
``\
\
950/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:44 254ms/step - loss: 1.0325 - mean\_absolute\_error: 0.8130\
\
``\
\
951/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:44 254ms/step - loss: 1.0325 - mean\_absolute\_error: 0.8130\
\
``\
\
952/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:44 254ms/step - loss: 1.0325 - mean\_absolute\_error: 0.8130\
\
``\
\
953/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:43 254ms/step - loss: 1.0325 - mean\_absolute\_error: 0.8130\
\
``\
\
954/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:43 254ms/step - loss: 1.0325 - mean\_absolute\_error: 0.8130\
\
``\
\
955/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:43 254ms/step - loss: 1.0324 - mean\_absolute\_error: 0.8130\
\
``\
\
956/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:43 254ms/step - loss: 1.0324 - mean\_absolute\_error: 0.8130\
\
``\
\
957/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:42 254ms/step - loss: 1.0324 - mean\_absolute\_error: 0.8130\
\
``\
\
958/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:42 254ms/step - loss: 1.0324 - mean\_absolute\_error: 0.8130\
\
``\
\
959/1599 ━━━━━━━━━━━\[37m━━━━━━━━━ 2:42 254ms/step - loss: 1.0324 - mean\_absolute\_error: 0.8130\
\
``\
\
960/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:42 254ms/step - loss: 1.0323 - mean\_absolute\_error: 0.8130\
\
``\
\
961/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:41 254ms/step - loss: 1.0323 - mean\_absolute\_error: 0.8129\
\
``\
\
962/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:41 254ms/step - loss: 1.0323 - mean\_absolute\_error: 0.8129\
\
``\
\
963/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:41 254ms/step - loss: 1.0323 - mean\_absolute\_error: 0.8129\
\
``\
\
964/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:41 254ms/step - loss: 1.0323 - mean\_absolute\_error: 0.8129\
\
``\
\
965/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:40 254ms/step - loss: 1.0322 - mean\_absolute\_error: 0.8129\
\
``\
\
966/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:40 254ms/step - loss: 1.0322 - mean\_absolute\_error: 0.8129\
\
``\
\
967/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:40 254ms/step - loss: 1.0322 - mean\_absolute\_error: 0.8129\
\
``\
\
968/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:40 254ms/step - loss: 1.0322 - mean\_absolute\_error: 0.8129\
\
``\
\
969/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:39 254ms/step - loss: 1.0322 - mean\_absolute\_error: 0.8129\
\
``\
\
970/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:39 254ms/step - loss: 1.0322 - mean\_absolute\_error: 0.8129\
\
``\
\
971/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:39 254ms/step - loss: 1.0321 - mean\_absolute\_error: 0.8129\
\
``\
\
972/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:39 254ms/step - loss: 1.0321 - mean\_absolute\_error: 0.8129\
\
``\
\
973/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:38 254ms/step - loss: 1.0321 - mean\_absolute\_error: 0.8128\
\
``\
\
974/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:38 254ms/step - loss: 1.0321 - mean\_absolute\_error: 0.8128\
\
``\
\
975/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:38 254ms/step - loss: 1.0321 - mean\_absolute\_error: 0.8128\
\
``\
\
976/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:38 254ms/step - loss: 1.0320 - mean\_absolute\_error: 0.8128\
\
``\
\
977/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:37 254ms/step - loss: 1.0320 - mean\_absolute\_error: 0.8128\
\
``\
\
978/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:37 254ms/step - loss: 1.0320 - mean\_absolute\_error: 0.8128\
\
``\
\
979/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:37 254ms/step - loss: 1.0320 - mean\_absolute\_error: 0.8128\
\
``\
\
980/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:37 254ms/step - loss: 1.0320 - mean\_absolute\_error: 0.8128\
\
``\
\
981/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:36 254ms/step - loss: 1.0319 - mean\_absolute\_error: 0.8128\
\
``\
\
982/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:36 254ms/step - loss: 1.0319 - mean\_absolute\_error: 0.8128\
\
``\
\
983/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:36 254ms/step - loss: 1.0319 - mean\_absolute\_error: 0.8128\
\
``\
\
984/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:36 254ms/step - loss: 1.0319 - mean\_absolute\_error: 0.8128\
\
``\
\
985/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:35 254ms/step - loss: 1.0319 - mean\_absolute\_error: 0.8127\
\
``\
\
986/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:35 254ms/step - loss: 1.0319 - mean\_absolute\_error: 0.8127\
\
``\
\
987/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:35 254ms/step - loss: 1.0318 - mean\_absolute\_error: 0.8127\
\
``\
\
988/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:35 254ms/step - loss: 1.0318 - mean\_absolute\_error: 0.8127\
\
``\
\
989/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:35 254ms/step - loss: 1.0318 - mean\_absolute\_error: 0.8127\
\
``\
\
990/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:34 254ms/step - loss: 1.0318 - mean\_absolute\_error: 0.8127\
\
``\
\
991/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:34 254ms/step - loss: 1.0318 - mean\_absolute\_error: 0.8127\
\
``\
\
992/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:34 254ms/step - loss: 1.0317 - mean\_absolute\_error: 0.8127\
\
``\
\
993/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:34 254ms/step - loss: 1.0317 - mean\_absolute\_error: 0.8127\
\
``\
\
994/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:33 254ms/step - loss: 1.0317 - mean\_absolute\_error: 0.8127\
\
``\
\
995/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:33 254ms/step - loss: 1.0317 - mean\_absolute\_error: 0.8127\
\
``\
\
996/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:33 254ms/step - loss: 1.0317 - mean\_absolute\_error: 0.8126\
\
``\
\
997/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:33 254ms/step - loss: 1.0316 - mean\_absolute\_error: 0.8126\
\
``\
\
998/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:32 254ms/step - loss: 1.0316 - mean\_absolute\_error: 0.8126\
\
``\
\
999/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:32 254ms/step - loss: 1.0316 - mean\_absolute\_error: 0.8126\
\
``\
\
1000/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:32 254ms/step - loss: 1.0316 - mean\_absolute\_error: 0.8126\
\
``\
\
1001/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:32 255ms/step - loss: 1.0316 - mean\_absolute\_error: 0.8126\
\
``\
\
1002/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:31 255ms/step - loss: 1.0316 - mean\_absolute\_error: 0.8126\
\
``\
\
1003/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:31 255ms/step - loss: 1.0315 - mean\_absolute\_error: 0.8126\
\
``\
\
1004/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:31 255ms/step - loss: 1.0315 - mean\_absolute\_error: 0.8126\
\
``\
\
1005/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:31 255ms/step - loss: 1.0315 - mean\_absolute\_error: 0.8126\
\
``\
\
1006/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:30 255ms/step - loss: 1.0315 - mean\_absolute\_error: 0.8126\
\
``\
\
1007/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:30 255ms/step - loss: 1.0315 - mean\_absolute\_error: 0.8126\
\
``\
\
1008/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:30 255ms/step - loss: 1.0315 - mean\_absolute\_error: 0.8126\
\
``\
\
1009/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:30 255ms/step - loss: 1.0314 - mean\_absolute\_error: 0.8125\
\
``\
\
1010/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:30 255ms/step - loss: 1.0314 - mean\_absolute\_error: 0.8125\
\
``\
\
1011/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:29 255ms/step - loss: 1.0314 - mean\_absolute\_error: 0.8125\
\
``\
\
1012/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:29 255ms/step - loss: 1.0314 - mean\_absolute\_error: 0.8125\
\
``\
\
1013/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:29 255ms/step - loss: 1.0314 - mean\_absolute\_error: 0.8125\
\
``\
\
1014/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:29 255ms/step - loss: 1.0313 - mean\_absolute\_error: 0.8125\
\
``\
\
1015/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:28 255ms/step - loss: 1.0313 - mean\_absolute\_error: 0.8125\
\
``\
\
1016/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:28 255ms/step - loss: 1.0313 - mean\_absolute\_error: 0.8125\
\
``\
\
1017/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:28 255ms/step - loss: 1.0313 - mean\_absolute\_error: 0.8125\
\
``\
\
1018/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:28 255ms/step - loss: 1.0313 - mean\_absolute\_error: 0.8125\
\
``\
\
1019/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:27 255ms/step - loss: 1.0313 - mean\_absolute\_error: 0.8125\
\
``\
\
1020/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:27 255ms/step - loss: 1.0312 - mean\_absolute\_error: 0.8125\
\
``\
\
1021/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:27 255ms/step - loss: 1.0312 - mean\_absolute\_error: 0.8124\
\
``\
\
1022/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:27 255ms/step - loss: 1.0312 - mean\_absolute\_error: 0.8124\
\
``\
\
1023/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:27 255ms/step - loss: 1.0312 - mean\_absolute\_error: 0.8124\
\
``\
\
1024/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:26 255ms/step - loss: 1.0312 - mean\_absolute\_error: 0.8124\
\
``\
\
1025/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:26 255ms/step - loss: 1.0311 - mean\_absolute\_error: 0.8124\
\
``\
\
1026/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:26 255ms/step - loss: 1.0311 - mean\_absolute\_error: 0.8124\
\
``\
\
1027/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:26 256ms/step - loss: 1.0311 - mean\_absolute\_error: 0.8124\
\
``\
\
1028/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:25 256ms/step - loss: 1.0311 - mean\_absolute\_error: 0.8124\
\
``\
\
1029/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:25 256ms/step - loss: 1.0311 - mean\_absolute\_error: 0.8124\
\
``\
\
1030/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:25 256ms/step - loss: 1.0310 - mean\_absolute\_error: 0.8124\
\
``\
\
1031/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:25 256ms/step - loss: 1.0310 - mean\_absolute\_error: 0.8124\
\
``\
\
1032/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:25 256ms/step - loss: 1.0310 - mean\_absolute\_error: 0.8124\
\
``\
\
1033/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:24 256ms/step - loss: 1.0310 - mean\_absolute\_error: 0.8123\
\
``\
\
1034/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:24 256ms/step - loss: 1.0310 - mean\_absolute\_error: 0.8123\
\
``\
\
1035/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:24 256ms/step - loss: 1.0310 - mean\_absolute\_error: 0.8123\
\
``\
\
1036/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:24 256ms/step - loss: 1.0309 - mean\_absolute\_error: 0.8123\
\
``\
\
1037/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:23 256ms/step - loss: 1.0309 - mean\_absolute\_error: 0.8123\
\
``\
\
1038/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:23 256ms/step - loss: 1.0309 - mean\_absolute\_error: 0.8123\
\
``\
\
1039/1599 ━━━━━━━━━━━━\[37m━━━━━━━━ 2:23 256ms/step - loss: 1.0309 - mean\_absolute\_error: 0.8123\
\
``\
\
1040/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:23 256ms/step - loss: 1.0309 - mean\_absolute\_error: 0.8123\
\
``\
\
1041/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:22 256ms/step - loss: 1.0308 - mean\_absolute\_error: 0.8123\
\
``\
\
1042/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:22 256ms/step - loss: 1.0308 - mean\_absolute\_error: 0.8123\
\
``\
\
1043/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:22 256ms/step - loss: 1.0308 - mean\_absolute\_error: 0.8123\
\
``\
\
1044/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:22 256ms/step - loss: 1.0308 - mean\_absolute\_error: 0.8122\
\
``\
\
1045/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:21 256ms/step - loss: 1.0308 - mean\_absolute\_error: 0.8122\
\
``\
\
1046/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:21 256ms/step - loss: 1.0308 - mean\_absolute\_error: 0.8122\
\
``\
\
1047/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:21 256ms/step - loss: 1.0307 - mean\_absolute\_error: 0.8122\
\
``\
\
1048/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:21 256ms/step - loss: 1.0307 - mean\_absolute\_error: 0.8122\
\
``\
\
1049/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:20 256ms/step - loss: 1.0307 - mean\_absolute\_error: 0.8122\
\
``\
\
1050/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:20 256ms/step - loss: 1.0307 - mean\_absolute\_error: 0.8122\
\
``\
\
1051/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:20 256ms/step - loss: 1.0307 - mean\_absolute\_error: 0.8122\
\
``\
\
1052/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:20 256ms/step - loss: 1.0306 - mean\_absolute\_error: 0.8122\
\
``\
\
1053/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:20 257ms/step - loss: 1.0306 - mean\_absolute\_error: 0.8122\
\
``\
\
1054/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:19 257ms/step - loss: 1.0306 - mean\_absolute\_error: 0.8122\
\
``\
\
1055/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:19 257ms/step - loss: 1.0306 - mean\_absolute\_error: 0.8122\
\
``\
\
1056/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:19 257ms/step - loss: 1.0306 - mean\_absolute\_error: 0.8121\
\
``\
\
1057/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:19 257ms/step - loss: 1.0306 - mean\_absolute\_error: 0.8121\
\
``\
\
1058/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:19 257ms/step - loss: 1.0305 - mean\_absolute\_error: 0.8121\
\
``\
\
1059/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:18 257ms/step - loss: 1.0305 - mean\_absolute\_error: 0.8121\
\
``\
\
1060/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:18 257ms/step - loss: 1.0305 - mean\_absolute\_error: 0.8121\
\
``\
\
1061/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:18 257ms/step - loss: 1.0305 - mean\_absolute\_error: 0.8121\
\
``\
\
1062/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:18 257ms/step - loss: 1.0305 - mean\_absolute\_error: 0.8121\
\
``\
\
1063/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:17 257ms/step - loss: 1.0304 - mean\_absolute\_error: 0.8121\
\
``\
\
1064/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:17 257ms/step - loss: 1.0304 - mean\_absolute\_error: 0.8121\
\
``\
\
1065/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:17 257ms/step - loss: 1.0304 - mean\_absolute\_error: 0.8121\
\
``\
\
1066/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:17 258ms/step - loss: 1.0304 - mean\_absolute\_error: 0.8121\
\
``\
\
1067/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:17 258ms/step - loss: 1.0304 - mean\_absolute\_error: 0.8121\
\
``\
\
1068/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:16 258ms/step - loss: 1.0304 - mean\_absolute\_error: 0.8120\
\
``\
\
1069/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:16 258ms/step - loss: 1.0303 - mean\_absolute\_error: 0.8120\
\
``\
\
1070/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:16 258ms/step - loss: 1.0303 - mean\_absolute\_error: 0.8120\
\
``\
\
1071/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:16 258ms/step - loss: 1.0303 - mean\_absolute\_error: 0.8120\
\
``\
\
1072/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:15 258ms/step - loss: 1.0303 - mean\_absolute\_error: 0.8120\
\
``\
\
1073/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:15 258ms/step - loss: 1.0303 - mean\_absolute\_error: 0.8120\
\
``\
\
1074/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:15 258ms/step - loss: 1.0302 - mean\_absolute\_error: 0.8120\
\
``\
\
1075/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:15 258ms/step - loss: 1.0302 - mean\_absolute\_error: 0.8120\
\
``\
\
1076/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:14 258ms/step - loss: 1.0302 - mean\_absolute\_error: 0.8120\
\
``\
\
1077/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:14 258ms/step - loss: 1.0302 - mean\_absolute\_error: 0.8120\
\
``\
\
1078/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:14 258ms/step - loss: 1.0302 - mean\_absolute\_error: 0.8120\
\
``\
\
1079/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:14 258ms/step - loss: 1.0302 - mean\_absolute\_error: 0.8120\
\
``\
\
1080/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:13 258ms/step - loss: 1.0301 - mean\_absolute\_error: 0.8120\
\
``\
\
1081/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:13 258ms/step - loss: 1.0301 - mean\_absolute\_error: 0.8119\
\
``\
\
1082/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:13 258ms/step - loss: 1.0301 - mean\_absolute\_error: 0.8119\
\
``\
\
1083/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:13 258ms/step - loss: 1.0301 - mean\_absolute\_error: 0.8119\
\
``\
\
1084/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:13 258ms/step - loss: 1.0301 - mean\_absolute\_error: 0.8119\
\
``\
\
1085/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:12 258ms/step - loss: 1.0301 - mean\_absolute\_error: 0.8119\
\
``\
\
1086/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:12 258ms/step - loss: 1.0300 - mean\_absolute\_error: 0.8119\
\
``\
\
1087/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:12 258ms/step - loss: 1.0300 - mean\_absolute\_error: 0.8119\
\
``\
\
1088/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:12 258ms/step - loss: 1.0300 - mean\_absolute\_error: 0.8119\
\
``\
\
1089/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:11 258ms/step - loss: 1.0300 - mean\_absolute\_error: 0.8119\
\
``\
\
1090/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:11 259ms/step - loss: 1.0300 - mean\_absolute\_error: 0.8119\
\
``\
\
1091/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:11 259ms/step - loss: 1.0299 - mean\_absolute\_error: 0.8119\
\
``\
\
1092/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:11 259ms/step - loss: 1.0299 - mean\_absolute\_error: 0.8119\
\
``\
\
1093/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:10 259ms/step - loss: 1.0299 - mean\_absolute\_error: 0.8118\
\
``\
\
1094/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:10 259ms/step - loss: 1.0299 - mean\_absolute\_error: 0.8118\
\
``\
\
1095/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:10 259ms/step - loss: 1.0299 - mean\_absolute\_error: 0.8118\
\
``\
\
1096/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:10 259ms/step - loss: 1.0299 - mean\_absolute\_error: 0.8118\
\
``\
\
1097/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:09 259ms/step - loss: 1.0298 - mean\_absolute\_error: 0.8118\
\
``\
\
1098/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:09 259ms/step - loss: 1.0298 - mean\_absolute\_error: 0.8118\
\
``\
\
1099/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:09 259ms/step - loss: 1.0298 - mean\_absolute\_error: 0.8118\
\
``\
\
1100/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:09 259ms/step - loss: 1.0298 - mean\_absolute\_error: 0.8118\
\
``\
\
1101/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:08 259ms/step - loss: 1.0298 - mean\_absolute\_error: 0.8118\
\
``\
\
1102/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:08 259ms/step - loss: 1.0298 - mean\_absolute\_error: 0.8118\
\
``\
\
1103/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:08 259ms/step - loss: 1.0297 - mean\_absolute\_error: 0.8118\
\
``\
\
1104/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:08 259ms/step - loss: 1.0297 - mean\_absolute\_error: 0.8118\
\
``\
\
1105/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:07 259ms/step - loss: 1.0297 - mean\_absolute\_error: 0.8117\
\
``\
\
1106/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:07 259ms/step - loss: 1.0297 - mean\_absolute\_error: 0.8117\
\
``\
\
1107/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:07 259ms/step - loss: 1.0297 - mean\_absolute\_error: 0.8117\
\
``\
\
1108/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:07 259ms/step - loss: 1.0297 - mean\_absolute\_error: 0.8117\
\
``\
\
1109/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:06 259ms/step - loss: 1.0296 - mean\_absolute\_error: 0.8117\
\
``\
\
1110/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:06 259ms/step - loss: 1.0296 - mean\_absolute\_error: 0.8117\
\
``\
\
1111/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:06 259ms/step - loss: 1.0296 - mean\_absolute\_error: 0.8117\
\
``\
\
1112/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:06 259ms/step - loss: 1.0296 - mean\_absolute\_error: 0.8117\
\
``\
\
1113/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:05 259ms/step - loss: 1.0296 - mean\_absolute\_error: 0.8117\
\
``\
\
1114/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:05 259ms/step - loss: 1.0295 - mean\_absolute\_error: 0.8117\
\
``\
\
1115/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:05 259ms/step - loss: 1.0295 - mean\_absolute\_error: 0.8117\
\
``\
\
1116/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:05 259ms/step - loss: 1.0295 - mean\_absolute\_error: 0.8117\
\
``\
\
1117/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:04 259ms/step - loss: 1.0295 - mean\_absolute\_error: 0.8117\
\
``\
\
1118/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:04 259ms/step - loss: 1.0295 - mean\_absolute\_error: 0.8116\
\
``\
\
1119/1599 ━━━━━━━━━━━━━\[37m━━━━━━━ 2:04 259ms/step - loss: 1.0295 - mean\_absolute\_error: 0.8116\
\
``\
\
1120/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:04 259ms/step - loss: 1.0294 - mean\_absolute\_error: 0.8116\
\
``\
\
1121/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:04 259ms/step - loss: 1.0294 - mean\_absolute\_error: 0.8116\
\
``\
\
1122/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:03 259ms/step - loss: 1.0294 - mean\_absolute\_error: 0.8116\
\
``\
\
1123/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:03 260ms/step - loss: 1.0294 - mean\_absolute\_error: 0.8116\
\
``\
\
1124/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:03 260ms/step - loss: 1.0294 - mean\_absolute\_error: 0.8116\
\
``\
\
1125/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:03 260ms/step - loss: 1.0293 - mean\_absolute\_error: 0.8116\
\
``\
\
1126/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:02 260ms/step - loss: 1.0293 - mean\_absolute\_error: 0.8116\
\
``\
\
1127/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:02 260ms/step - loss: 1.0293 - mean\_absolute\_error: 0.8116\
\
``\
\
1128/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:02 260ms/step - loss: 1.0293 - mean\_absolute\_error: 0.8116\
\
``\
\
1129/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:02 260ms/step - loss: 1.0293 - mean\_absolute\_error: 0.8115\
\
``\
\
1130/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:01 260ms/step - loss: 1.0292 - mean\_absolute\_error: 0.8115\
\
``\
\
1131/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:01 260ms/step - loss: 1.0292 - mean\_absolute\_error: 0.8115\
\
``\
\
1132/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:01 260ms/step - loss: 1.0292 - mean\_absolute\_error: 0.8115\
\
``\
\
1133/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:00 260ms/step - loss: 1.0292 - mean\_absolute\_error: 0.8115\
\
``\
\
1134/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:00 260ms/step - loss: 1.0292 - mean\_absolute\_error: 0.8115\
\
``\
\
1135/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:00 260ms/step - loss: 1.0292 - mean\_absolute\_error: 0.8115\
\
``\
\
1136/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 2:00 260ms/step - loss: 1.0291 - mean\_absolute\_error: 0.8115\
\
``\
\
1137/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:59 260ms/step - loss: 1.0291 - mean\_absolute\_error: 0.8115\
\
``\
\
1138/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:59 260ms/step - loss: 1.0291 - mean\_absolute\_error: 0.8115\
\
``\
\
1139/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:59 260ms/step - loss: 1.0291 - mean\_absolute\_error: 0.8115\
\
``\
\
1140/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:59 260ms/step - loss: 1.0291 - mean\_absolute\_error: 0.8115\
\
``\
\
1141/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:58 260ms/step - loss: 1.0291 - mean\_absolute\_error: 0.8114\
\
``\
\
1142/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:58 260ms/step - loss: 1.0290 - mean\_absolute\_error: 0.8114\
\
``\
\
1143/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:58 260ms/step - loss: 1.0290 - mean\_absolute\_error: 0.8114\
\
``\
\
1144/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:58 260ms/step - loss: 1.0290 - mean\_absolute\_error: 0.8114\
\
``\
\
1145/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:57 260ms/step - loss: 1.0290 - mean\_absolute\_error: 0.8114\
\
``\
\
1146/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:57 260ms/step - loss: 1.0290 - mean\_absolute\_error: 0.8114\
\
``\
\
1147/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:57 260ms/step - loss: 1.0289 - mean\_absolute\_error: 0.8114\
\
``\
\
1148/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:57 260ms/step - loss: 1.0289 - mean\_absolute\_error: 0.8114\
\
``\
\
1149/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:56 260ms/step - loss: 1.0289 - mean\_absolute\_error: 0.8114\
\
``\
\
1150/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:56 260ms/step - loss: 1.0289 - mean\_absolute\_error: 0.8114\
\
``\
\
1151/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:56 260ms/step - loss: 1.0289 - mean\_absolute\_error: 0.8114\
\
``\
\
1152/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:56 260ms/step - loss: 1.0288 - mean\_absolute\_error: 0.8114\
\
``\
\
1153/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:55 260ms/step - loss: 1.0288 - mean\_absolute\_error: 0.8113\
\
``\
\
1154/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:55 260ms/step - loss: 1.0288 - mean\_absolute\_error: 0.8113\
\
``\
\
1155/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:55 260ms/step - loss: 1.0288 - mean\_absolute\_error: 0.8113\
\
``\
\
1156/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:55 260ms/step - loss: 1.0288 - mean\_absolute\_error: 0.8113\
\
``\
\
1157/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:54 260ms/step - loss: 1.0288 - mean\_absolute\_error: 0.8113\
\
``\
\
1158/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:54 260ms/step - loss: 1.0287 - mean\_absolute\_error: 0.8113\
\
``\
\
1159/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:54 260ms/step - loss: 1.0287 - mean\_absolute\_error: 0.8113\
\
``\
\
1160/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:54 260ms/step - loss: 1.0287 - mean\_absolute\_error: 0.8113\
\
``\
\
1161/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:53 260ms/step - loss: 1.0287 - mean\_absolute\_error: 0.8113\
\
``\
\
1162/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:53 260ms/step - loss: 1.0287 - mean\_absolute\_error: 0.8113\
\
``\
\
1163/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:53 260ms/step - loss: 1.0286 - mean\_absolute\_error: 0.8113\
\
``\
\
1164/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:53 260ms/step - loss: 1.0286 - mean\_absolute\_error: 0.8113\
\
``\
\
1165/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:52 260ms/step - loss: 1.0286 - mean\_absolute\_error: 0.8112\
\
``\
\
1166/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:52 260ms/step - loss: 1.0286 - mean\_absolute\_error: 0.8112\
\
``\
\
1167/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:52 260ms/step - loss: 1.0286 - mean\_absolute\_error: 0.8112\
\
``\
\
1168/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:52 260ms/step - loss: 1.0286 - mean\_absolute\_error: 0.8112\
\
``\
\
1169/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:51 260ms/step - loss: 1.0285 - mean\_absolute\_error: 0.8112\
\
``\
\
1170/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:51 260ms/step - loss: 1.0285 - mean\_absolute\_error: 0.8112\
\
``\
\
1171/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:51 260ms/step - loss: 1.0285 - mean\_absolute\_error: 0.8112\
\
``\
\
1172/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:51 260ms/step - loss: 1.0285 - mean\_absolute\_error: 0.8112\
\
``\
\
1173/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:50 260ms/step - loss: 1.0285 - mean\_absolute\_error: 0.8112\
\
``\
\
1174/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:50 260ms/step - loss: 1.0285 - mean\_absolute\_error: 0.8112\
\
``\
\
1175/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:50 260ms/step - loss: 1.0284 - mean\_absolute\_error: 0.8112\
\
``\
\
1176/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:50 260ms/step - loss: 1.0284 - mean\_absolute\_error: 0.8112\
\
``\
\
1177/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:49 260ms/step - loss: 1.0284 - mean\_absolute\_error: 0.8111\
\
``\
\
1178/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:49 260ms/step - loss: 1.0284 - mean\_absolute\_error: 0.8111\
\
``\
\
1179/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:49 260ms/step - loss: 1.0284 - mean\_absolute\_error: 0.8111\
\
``\
\
1180/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:49 260ms/step - loss: 1.0283 - mean\_absolute\_error: 0.8111\
\
``\
\
1181/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:48 260ms/step - loss: 1.0283 - mean\_absolute\_error: 0.8111\
\
``\
\
1182/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:48 260ms/step - loss: 1.0283 - mean\_absolute\_error: 0.8111\
\
``\
\
1183/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:48 260ms/step - loss: 1.0283 - mean\_absolute\_error: 0.8111\
\
``\
\
1184/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:48 260ms/step - loss: 1.0283 - mean\_absolute\_error: 0.8111\
\
``\
\
1185/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:47 260ms/step - loss: 1.0283 - mean\_absolute\_error: 0.8111\
\
``\
\
1186/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:47 260ms/step - loss: 1.0282 - mean\_absolute\_error: 0.8111\
\
``\
\
1187/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:47 260ms/step - loss: 1.0282 - mean\_absolute\_error: 0.8111\
\
``\
\
1188/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:46 260ms/step - loss: 1.0282 - mean\_absolute\_error: 0.8111\
\
``\
\
1189/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:46 260ms/step - loss: 1.0282 - mean\_absolute\_error: 0.8110\
\
``\
\
1190/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:46 260ms/step - loss: 1.0282 - mean\_absolute\_error: 0.8110\
\
``\
\
1191/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:46 260ms/step - loss: 1.0281 - mean\_absolute\_error: 0.8110\
\
``\
\
1192/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:45 260ms/step - loss: 1.0281 - mean\_absolute\_error: 0.8110\
\
``\
\
1193/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:45 260ms/step - loss: 1.0281 - mean\_absolute\_error: 0.8110\
\
``\
\
1194/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:45 260ms/step - loss: 1.0281 - mean\_absolute\_error: 0.8110\
\
``\
\
1195/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:45 260ms/step - loss: 1.0281 - mean\_absolute\_error: 0.8110\
\
``\
\
1196/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:44 260ms/step - loss: 1.0281 - mean\_absolute\_error: 0.8110\
\
``\
\
1197/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:44 260ms/step - loss: 1.0280 - mean\_absolute\_error: 0.8110\
\
``\
\
1198/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:44 260ms/step - loss: 1.0280 - mean\_absolute\_error: 0.8110\
\
``\
\
1199/1599 ━━━━━━━━━━━━━━\[37m━━━━━━ 1:44 260ms/step - loss: 1.0280 - mean\_absolute\_error: 0.8110\
\
``\
\
1200/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:43 260ms/step - loss: 1.0280 - mean\_absolute\_error: 0.8110\
\
``\
\
1201/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:43 260ms/step - loss: 1.0280 - mean\_absolute\_error: 0.8110\
\
``\
\
1202/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:43 261ms/step - loss: 1.0280 - mean\_absolute\_error: 0.8109\
\
``\
\
1203/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:43 261ms/step - loss: 1.0279 - mean\_absolute\_error: 0.8109\
\
``\
\
1204/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:42 261ms/step - loss: 1.0279 - mean\_absolute\_error: 0.8109\
\
``\
\
1205/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:42 261ms/step - loss: 1.0279 - mean\_absolute\_error: 0.8109\
\
``\
\
1206/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:42 261ms/step - loss: 1.0279 - mean\_absolute\_error: 0.8109\
\
``\
\
1207/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:42 261ms/step - loss: 1.0279 - mean\_absolute\_error: 0.8109\
\
``\
\
1208/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:41 261ms/step - loss: 1.0279 - mean\_absolute\_error: 0.8109\
\
``\
\
1209/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:41 261ms/step - loss: 1.0278 - mean\_absolute\_error: 0.8109\
\
``\
\
1210/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:41 261ms/step - loss: 1.0278 - mean\_absolute\_error: 0.8109\
\
``\
\
1211/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:41 261ms/step - loss: 1.0278 - mean\_absolute\_error: 0.8109\
\
``\
\
1212/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:40 261ms/step - loss: 1.0278 - mean\_absolute\_error: 0.8109\
\
``\
\
1213/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:40 261ms/step - loss: 1.0278 - mean\_absolute\_error: 0.8109\
\
``\
\
1214/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:40 261ms/step - loss: 1.0278 - mean\_absolute\_error: 0.8108\
\
``\
\
1215/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:40 261ms/step - loss: 1.0277 - mean\_absolute\_error: 0.8108\
\
``\
\
1216/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:39 261ms/step - loss: 1.0277 - mean\_absolute\_error: 0.8108\
\
``\
\
1217/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:39 261ms/step - loss: 1.0277 - mean\_absolute\_error: 0.8108\
\
``\
\
1218/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:39 261ms/step - loss: 1.0277 - mean\_absolute\_error: 0.8108\
\
``\
\
1219/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:39 261ms/step - loss: 1.0277 - mean\_absolute\_error: 0.8108\
\
``\
\
1220/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:38 261ms/step - loss: 1.0276 - mean\_absolute\_error: 0.8108\
\
``\
\
1221/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:38 261ms/step - loss: 1.0276 - mean\_absolute\_error: 0.8108\
\
``\
\
1222/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:38 261ms/step - loss: 1.0276 - mean\_absolute\_error: 0.8108\
\
``\
\
1223/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:38 261ms/step - loss: 1.0276 - mean\_absolute\_error: 0.8108\
\
``\
\
1224/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:37 261ms/step - loss: 1.0276 - mean\_absolute\_error: 0.8108\
\
``\
\
1225/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:37 261ms/step - loss: 1.0276 - mean\_absolute\_error: 0.8108\
\
``\
\
1226/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:37 261ms/step - loss: 1.0275 - mean\_absolute\_error: 0.8108\
\
``\
\
1227/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:36 261ms/step - loss: 1.0275 - mean\_absolute\_error: 0.8107\
\
``\
\
1228/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:36 261ms/step - loss: 1.0275 - mean\_absolute\_error: 0.8107\
\
``\
\
1229/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:36 261ms/step - loss: 1.0275 - mean\_absolute\_error: 0.8107\
\
``\
\
1230/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:36 261ms/step - loss: 1.0275 - mean\_absolute\_error: 0.8107\
\
``\
\
1231/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:35 261ms/step - loss: 1.0275 - mean\_absolute\_error: 0.8107\
\
``\
\
1232/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:35 261ms/step - loss: 1.0274 - mean\_absolute\_error: 0.8107\
\
``\
\
1233/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:35 261ms/step - loss: 1.0274 - mean\_absolute\_error: 0.8107\
\
``\
\
1234/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:35 261ms/step - loss: 1.0274 - mean\_absolute\_error: 0.8107\
\
``\
\
1235/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:34 261ms/step - loss: 1.0274 - mean\_absolute\_error: 0.8107\
\
``\
\
1236/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:34 261ms/step - loss: 1.0274 - mean\_absolute\_error: 0.8107\
\
``\
\
1237/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:34 261ms/step - loss: 1.0274 - mean\_absolute\_error: 0.8107\
\
``\
\
1238/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:34 261ms/step - loss: 1.0273 - mean\_absolute\_error: 0.8107\
\
``\
\
1239/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:33 261ms/step - loss: 1.0273 - mean\_absolute\_error: 0.8107\
\
``\
\
1240/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:33 261ms/step - loss: 1.0273 - mean\_absolute\_error: 0.8106\
\
``\
\
1241/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:33 261ms/step - loss: 1.0273 - mean\_absolute\_error: 0.8106\
\
``\
\
1242/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:33 261ms/step - loss: 1.0273 - mean\_absolute\_error: 0.8106\
\
``\
\
1243/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:33 261ms/step - loss: 1.0273 - mean\_absolute\_error: 0.8106\
\
``\
\
1244/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:32 261ms/step - loss: 1.0272 - mean\_absolute\_error: 0.8106\
\
``\
\
1245/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:32 261ms/step - loss: 1.0272 - mean\_absolute\_error: 0.8106\
\
``\
\
1246/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:32 261ms/step - loss: 1.0272 - mean\_absolute\_error: 0.8106\
\
``\
\
1247/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:31 261ms/step - loss: 1.0272 - mean\_absolute\_error: 0.8106\
\
``\
\
1248/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:31 261ms/step - loss: 1.0272 - mean\_absolute\_error: 0.8106\
\
``\
\
1249/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:31 261ms/step - loss: 1.0272 - mean\_absolute\_error: 0.8106\
\
``\
\
1250/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:31 261ms/step - loss: 1.0271 - mean\_absolute\_error: 0.8106\
\
``\
\
1251/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:30 261ms/step - loss: 1.0271 - mean\_absolute\_error: 0.8106\
\
``\
\
1252/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:30 261ms/step - loss: 1.0271 - mean\_absolute\_error: 0.8106\
\
``\
\
1253/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:30 261ms/step - loss: 1.0271 - mean\_absolute\_error: 0.8105\
\
``\
\
1254/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:30 261ms/step - loss: 1.0271 - mean\_absolute\_error: 0.8105\
\
``\
\
1255/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:29 261ms/step - loss: 1.0271 - mean\_absolute\_error: 0.8105\
\
``\
\
1256/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:29 261ms/step - loss: 1.0270 - mean\_absolute\_error: 0.8105\
\
``\
\
1257/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:29 261ms/step - loss: 1.0270 - mean\_absolute\_error: 0.8105\
\
``\
\
1258/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:29 261ms/step - loss: 1.0270 - mean\_absolute\_error: 0.8105\
\
``\
\
1259/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:28 261ms/step - loss: 1.0270 - mean\_absolute\_error: 0.8105\
\
``\
\
1260/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:28 261ms/step - loss: 1.0270 - mean\_absolute\_error: 0.8105\
\
``\
\
1261/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:28 261ms/step - loss: 1.0270 - mean\_absolute\_error: 0.8105\
\
``\
\
1262/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:28 261ms/step - loss: 1.0269 - mean\_absolute\_error: 0.8105\
\
``\
\
1263/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:27 261ms/step - loss: 1.0269 - mean\_absolute\_error: 0.8105\
\
``\
\
1264/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:27 261ms/step - loss: 1.0269 - mean\_absolute\_error: 0.8105\
\
``\
\
1265/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:27 261ms/step - loss: 1.0269 - mean\_absolute\_error: 0.8105\
\
``\
\
1266/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:27 261ms/step - loss: 1.0269 - mean\_absolute\_error: 0.8104\
\
``\
\
1267/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:26 261ms/step - loss: 1.0269 - mean\_absolute\_error: 0.8104\
\
``\
\
1268/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:26 261ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1269/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:26 261ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1270/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:26 261ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1271/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:25 262ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1272/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:25 262ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1273/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:25 262ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1274/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:25 262ms/step - loss: 1.0268 - mean\_absolute\_error: 0.8104\
\
``\
\
1275/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:24 262ms/step - loss: 1.0267 - mean\_absolute\_error: 0.8104\
\
``\
\
1276/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:24 262ms/step - loss: 1.0267 - mean\_absolute\_error: 0.8104\
\
``\
\
1277/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:24 262ms/step - loss: 1.0267 - mean\_absolute\_error: 0.8104\
\
``\
\
1278/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:24 262ms/step - loss: 1.0267 - mean\_absolute\_error: 0.8104\
\
``\
\
1279/1599 ━━━━━━━━━━━━━━━\[37m━━━━━ 1:23 262ms/step - loss: 1.0267 - mean\_absolute\_error: 0.8103\
\
``\
\
1280/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:23 262ms/step - loss: 1.0267 - mean\_absolute\_error: 0.8103\
\
``\
\
1281/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:23 262ms/step - loss: 1.0266 - mean\_absolute\_error: 0.8103\
\
``\
\
1282/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:23 262ms/step - loss: 1.0266 - mean\_absolute\_error: 0.8103\
\
``\
\
1283/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:22 262ms/step - loss: 1.0266 - mean\_absolute\_error: 0.8103\
\
``\
\
1284/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:22 262ms/step - loss: 1.0266 - mean\_absolute\_error: 0.8103\
\
``\
\
1285/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:22 262ms/step - loss: 1.0266 - mean\_absolute\_error: 0.8103\
\
``\
\
1286/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:22 262ms/step - loss: 1.0266 - mean\_absolute\_error: 0.8103\
\
``\
\
1287/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:21 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8103\
\
``\
\
1288/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:21 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8103\
\
``\
\
1289/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:21 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8103\
\
``\
\
1290/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:20 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8103\
\
``\
\
1291/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:20 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8103\
\
``\
\
1292/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:20 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8103\
\
``\
\
1293/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:20 262ms/step - loss: 1.0265 - mean\_absolute\_error: 0.8102\
\
``\
\
1294/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:19 262ms/step - loss: 1.0264 - mean\_absolute\_error: 0.8102\
\
``\
\
1295/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:19 262ms/step - loss: 1.0264 - mean\_absolute\_error: 0.8102\
\
``\
\
1296/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:19 262ms/step - loss: 1.0264 - mean\_absolute\_error: 0.8102\
\
``\
\
1297/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:19 262ms/step - loss: 1.0264 - mean\_absolute\_error: 0.8102\
\
``\
\
1298/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:18 262ms/step - loss: 1.0264 - mean\_absolute\_error: 0.8102\
\
``\
\
1299/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:18 262ms/step - loss: 1.0264 - mean\_absolute\_error: 0.8102\
\
``\
\
1300/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:18 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1301/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:18 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1302/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:17 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1303/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:17 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1304/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:17 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1305/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:17 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1306/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:16 262ms/step - loss: 1.0263 - mean\_absolute\_error: 0.8102\
\
``\
\
1307/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:16 262ms/step - loss: 1.0262 - mean\_absolute\_error: 0.8101\
\
``\
\
1308/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:16 262ms/step - loss: 1.0262 - mean\_absolute\_error: 0.8101\
\
``\
\
1309/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:16 262ms/step - loss: 1.0262 - mean\_absolute\_error: 0.8101\
\
``\
\
1310/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:15 262ms/step - loss: 1.0262 - mean\_absolute\_error: 0.8101\
\
``\
\
1311/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:15 262ms/step - loss: 1.0262 - mean\_absolute\_error: 0.8101\
\
``\
\
1312/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:15 262ms/step - loss: 1.0262 - mean\_absolute\_error: 0.8101\
\
``\
\
1313/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:14 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1314/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:14 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1315/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:14 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1316/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:14 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1317/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:14 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1318/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:13 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1319/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:13 262ms/step - loss: 1.0261 - mean\_absolute\_error: 0.8101\
\
``\
\
1320/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:13 263ms/step - loss: 1.0260 - mean\_absolute\_error: 0.8101\
\
``\
\
1321/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:12 263ms/step - loss: 1.0260 - mean\_absolute\_error: 0.8100\
\
``\
\
1322/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:12 263ms/step - loss: 1.0260 - mean\_absolute\_error: 0.8100\
\
``\
\
1323/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:12 263ms/step - loss: 1.0260 - mean\_absolute\_error: 0.8100\
\
``\
\
1324/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:12 263ms/step - loss: 1.0260 - mean\_absolute\_error: 0.8100\
\
``\
\
1325/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:11 262ms/step - loss: 1.0260 - mean\_absolute\_error: 0.8100\
\
``\
\
1326/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:11 262ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1327/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:11 262ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1328/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:11 263ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1329/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:10 263ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1330/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:10 263ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1331/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:10 263ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1332/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:10 263ms/step - loss: 1.0259 - mean\_absolute\_error: 0.8100\
\
``\
\
1333/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:09 263ms/step - loss: 1.0258 - mean\_absolute\_error: 0.8100\
\
``\
\
1334/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:09 263ms/step - loss: 1.0258 - mean\_absolute\_error: 0.8100\
\
``\
\
1335/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:09 263ms/step - loss: 1.0258 - mean\_absolute\_error: 0.8100\
\
``\
\
1336/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:09 263ms/step - loss: 1.0258 - mean\_absolute\_error: 0.8099\
\
``\
\
1337/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:08 263ms/step - loss: 1.0258 - mean\_absolute\_error: 0.8099\
\
``\
\
1338/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:08 263ms/step - loss: 1.0258 - mean\_absolute\_error: 0.8099\
\
``\
\
1339/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:08 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1340/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:08 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1341/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:07 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1342/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:07 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1343/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:07 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1344/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:06 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1345/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:06 263ms/step - loss: 1.0257 - mean\_absolute\_error: 0.8099\
\
``\
\
1346/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:06 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8099\
\
``\
\
1347/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:06 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8099\
\
``\
\
1348/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:05 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8099\
\
``\
\
1349/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:05 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8099\
\
``\
\
1350/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:05 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8099\
\
``\
\
1351/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:05 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8098\
\
``\
\
1352/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:04 263ms/step - loss: 1.0256 - mean\_absolute\_error: 0.8098\
\
``\
\
1353/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:04 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1354/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:04 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1355/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:04 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1356/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:03 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1357/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:03 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1358/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:03 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1359/1599 ━━━━━━━━━━━━━━━━\[37m━━━━ 1:03 263ms/step - loss: 1.0255 - mean\_absolute\_error: 0.8098\
\
``\
\
1360/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:02 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8098\
\
``\
\
1361/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:02 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8098\
\
``\
\
1362/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:02 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8098\
\
``\
\
1363/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:02 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8098\
\
``\
\
1364/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:01 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8098\
\
``\
\
1365/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:01 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8098\
\
``\
\
1366/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:01 263ms/step - loss: 1.0254 - mean\_absolute\_error: 0.8097\
\
``\
\
1367/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:01 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1368/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:00 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1369/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:00 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1370/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:00 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1371/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 1:00 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1372/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 59s 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1373/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 59s 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1374/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 59s 263ms/step - loss: 1.0253 - mean\_absolute\_error: 0.8097\
\
``\
\
1375/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 58s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1376/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 58s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1377/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 58s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1378/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 58s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1379/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 57s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1380/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 57s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1381/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 57s 263ms/step - loss: 1.0252 - mean\_absolute\_error: 0.8097\
\
``\
\
1382/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 57s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1383/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 56s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1384/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 56s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1385/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 56s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1386/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 56s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1387/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 55s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1388/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 55s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1389/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 55s 263ms/step - loss: 1.0251 - mean\_absolute\_error: 0.8096\
\
``\
\
1390/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 55s 263ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1391/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 54s 263ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1392/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 54s 263ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1393/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 54s 264ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1394/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 54s 264ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1395/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 53s 264ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1396/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 53s 264ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1397/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 53s 264ms/step - loss: 1.0250 - mean\_absolute\_error: 0.8096\
\
``\
\
1398/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 52s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1399/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 52s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1400/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 52s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1401/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 52s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1402/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 51s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1403/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 51s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1404/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 51s 264ms/step - loss: 1.0249 - mean\_absolute\_error: 0.8095\
\
``\
\
1405/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 51s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1406/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 50s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1407/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 50s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1408/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 50s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1409/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 50s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1410/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 49s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1411/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 49s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1412/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 49s 264ms/step - loss: 1.0248 - mean\_absolute\_error: 0.8095\
\
``\
\
1413/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 49s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8095\
\
``\
\
1414/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 48s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1415/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 48s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1416/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 48s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1417/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 47s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1418/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 47s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1419/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 47s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1420/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 47s 264ms/step - loss: 1.0247 - mean\_absolute\_error: 0.8094\
\
``\
\
1421/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 46s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1422/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 46s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1423/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 46s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1424/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 46s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1425/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 45s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1426/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 45s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1427/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 45s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1428/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 45s 264ms/step - loss: 1.0246 - mean\_absolute\_error: 0.8094\
\
``\
\
1429/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 44s 264ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8094\
\
``\
\
1430/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 44s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8094\
\
``\
\
1431/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 44s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8093\
\
``\
\
1432/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 43s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8093\
\
``\
\
1433/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 43s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8093\
\
``\
\
1434/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 43s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8093\
\
``\
\
1435/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 43s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8093\
\
``\
\
1436/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 42s 263ms/step - loss: 1.0245 - mean\_absolute\_error: 0.8093\
\
``\
\
1437/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 42s 263ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1438/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 42s 263ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1439/1599 ━━━━━━━━━━━━━━━━━\[37m━━━ 42s 263ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1440/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 41s 263ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1441/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 41s 264ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1442/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 41s 264ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1443/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 41s 264ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1444/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 40s 264ms/step - loss: 1.0244 - mean\_absolute\_error: 0.8093\
\
``\
\
1445/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 40s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8093\
\
``\
\
1446/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 40s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8093\
\
``\
\
1447/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 40s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8093\
\
``\
\
1448/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 39s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8092\
\
``\
\
1449/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 39s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8092\
\
``\
\
1450/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 39s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8092\
\
``\
\
1451/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 39s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8092\
\
``\
\
1452/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 38s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8092\
\
``\
\
1453/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 38s 264ms/step - loss: 1.0243 - mean\_absolute\_error: 0.8092\
\
``\
\
1454/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 38s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1455/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 37s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1456/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 37s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1457/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 37s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1458/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 37s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1459/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 36s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1460/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 36s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1461/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 36s 264ms/step - loss: 1.0242 - mean\_absolute\_error: 0.8092\
\
``\
\
1462/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 36s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8092\
\
``\
\
1463/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 35s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8092\
\
``\
\
1464/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 35s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8092\
\
``\
\
1465/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 35s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8092\
\
``\
\
1466/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 35s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8091\
\
``\
\
1467/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 34s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8091\
\
``\
\
1468/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 34s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8091\
\
``\
\
1469/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 34s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8091\
\
``\
\
1470/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 34s 264ms/step - loss: 1.0241 - mean\_absolute\_error: 0.8091\
\
``\
\
1471/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 33s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1472/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 33s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1473/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 33s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1474/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 32s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1475/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 32s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1476/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 32s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1477/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 32s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1478/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 31s 264ms/step - loss: 1.0240 - mean\_absolute\_error: 0.8091\
\
``\
\
1479/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 31s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8091\
\
``\
\
1480/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 31s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8091\
\
``\
\
1481/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 31s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8091\
\
``\
\
1482/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 30s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8091\
\
``\
\
1483/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 30s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8091\
\
``\
\
1484/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 30s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8090\
\
``\
\
1485/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 30s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8090\
\
``\
\
1486/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 29s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8090\
\
``\
\
1487/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 29s 264ms/step - loss: 1.0239 - mean\_absolute\_error: 0.8090\
\
``\
\
1488/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 29s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1489/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 29s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1490/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 28s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1491/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 28s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1492/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 28s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1493/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 27s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1494/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 27s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1495/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 27s 264ms/step - loss: 1.0238 - mean\_absolute\_error: 0.8090\
\
``\
\
1496/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 27s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8090\
\
``\
\
1497/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 26s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8090\
\
``\
\
1498/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 26s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8090\
\
``\
\
1499/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 26s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8090\
\
``\
\
1500/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 26s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8090\
\
``\
\
1501/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 25s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8090\
\
``\
\
1502/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 25s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8089\
\
``\
\
1503/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 25s 264ms/step - loss: 1.0237 - mean\_absolute\_error: 0.8089\
\
``\
\
1504/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 25s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1505/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 24s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1506/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 24s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1507/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 24s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1508/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 24s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1509/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 23s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1510/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 23s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1511/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 23s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1512/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 22s 264ms/step - loss: 1.0236 - mean\_absolute\_error: 0.8089\
\
``\
\
1513/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 22s 264ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1514/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 22s 264ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1515/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 22s 264ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1516/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 21s 264ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1517/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 21s 264ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1518/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 21s 264ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1519/1599 ━━━━━━━━━━━━━━━━━━\[37m━━ 21s 265ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8089\
\
``\
\
1520/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 20s 265ms/step - loss: 1.0235 - mean\_absolute\_error: 0.8088\
\
``\
\
1521/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 20s 265ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1522/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 20s 265ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1523/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 20s 265ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1524/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 19s 264ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1525/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 19s 264ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1526/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 19s 264ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1527/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 19s 264ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1528/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 18s 264ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1529/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 18s 264ms/step - loss: 1.0234 - mean\_absolute\_error: 0.8088\
\
``\
\
1530/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 18s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1531/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 17s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1532/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 17s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1533/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 17s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1534/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 17s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1535/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 16s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1536/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 16s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1537/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 16s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8088\
\
``\
\
1538/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 16s 264ms/step - loss: 1.0233 - mean\_absolute\_error: 0.8087\
\
``\
\
1539/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 15s 264ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1540/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 15s 264ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1541/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 15s 264ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1542/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 15s 264ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1543/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 14s 265ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1544/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 14s 265ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1545/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 14s 265ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1546/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 14s 265ms/step - loss: 1.0232 - mean\_absolute\_error: 0.8087\
\
``\
\
1547/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 13s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1548/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 13s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1549/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 13s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1550/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 12s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1551/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 12s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1552/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 12s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1553/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 12s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1554/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 11s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1555/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 11s 265ms/step - loss: 1.0231 - mean\_absolute\_error: 0.8087\
\
``\
\
1556/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 11s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8087\
\
``\
\
1557/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 11s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1558/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 10s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1559/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 10s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1560/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 10s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1561/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 10s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1562/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 9s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1563/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 9s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1564/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 9s 265ms/step - loss: 1.0230 - mean\_absolute\_error: 0.8086\
\
``\
\
1565/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 8s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1566/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 8s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1567/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 8s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1568/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 8s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1569/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 7s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1570/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 7s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1571/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 7s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1572/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 7s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1573/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 6s 265ms/step - loss: 1.0229 - mean\_absolute\_error: 0.8086\
\
``\
\
1574/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 6s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8086\
\
``\
\
1575/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 6s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8086\
\
``\
\
1576/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 6s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1577/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 5s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1578/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 5s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1579/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 5s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1580/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 5s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1581/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 4s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1582/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 4s 265ms/step - loss: 1.0228 - mean\_absolute\_error: 0.8085\
\
``\
\
1583/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 4s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1584/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 3s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1585/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 3s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1586/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 3s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1587/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 3s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1588/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 2s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1589/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 2s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1590/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 2s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1591/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 2s 265ms/step - loss: 1.0227 - mean\_absolute\_error: 0.8085\
\
``\
\
1592/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 1s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8085\
\
``\
\
1593/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 1s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8085\
\
``\
\
1594/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 1s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``\
\
1595/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 1s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``\
\
1596/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``\
\
1597/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``\
\
1598/1599 ━━━━━━━━━━━━━━━━━━━\[37m━ 0s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``\
\
1599/1599 ━━━━━━━━━━━━━━━━━━━━ 0s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``\
\
1599/1599 ━━━━━━━━━━━━━━━━━━━━ 424s 265ms/step - loss: 1.0226 - mean\_absolute\_error: 0.8084\
\
``Test MAE: 0.779  /home/humbulani/tensorflow-env/env/lib/python3.11/site-packages/keras/src/trainers/epoch_iterator.py:159: UserWarning: Your input ran out of data; interrupting training. Make sure that your dataset or generator can generate at least `steps_per_epoch * epochs` batches. You may need to use the `.repeat()` function when building your dataset.   self._interrupted_warning()``\
\
You should achieve a Mean Absolute Error (MAE) at or around 0.7 on the test data.\
\
* * *\
\
Conclusion\
----------\
\
The BST model uses the Transformer layer in its architecture to capture the sequential signals underlying users’ behavior sequences for recommendation.\
\
You can try training this model with different configurations, for example, by increasing the input sequence length and training the model for a larger number of epochs. In addition, you can try including other features like movie release year and customer zipcode, and including cross features like sex X genre.\
\
[A Transformer-based recommendation system](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#a-transformerbased-recommendation-system)\
\
[Introduction](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#introduction)\
\
[The dataset](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#the-dataset)\
\
[Setup](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#setup)\
\
[Prepare the data](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#prepare-the-data)\
\
[Download and prepare the DataFrames](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#download-and-prepare-the-dataframes)\
\
[Transform the movie ratings data into sequences](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#transform-the-movie-ratings-data-into-sequences)\
\
[Define metadata](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#define-metadata)\
\
[Encode input features](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#encode-input-features)\
\
[Create model inputs](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#create-model-inputs)\
\
[Create a BST model](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#create-a-bst-model)\
\
[Run training and evaluation experiment](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#run-training-and-evaluation-experiment)\
\
[Conclusion](https://keras.io/examples/structured_data/movielens_recommendations_transformers/#conclusion)