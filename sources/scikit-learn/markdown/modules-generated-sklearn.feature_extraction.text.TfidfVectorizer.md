[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

Collapse Sidebar Expand Sidebar

TfidfVectorizer[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#tfidfvectorizer "Link to this heading")

==================================================================================================================================================================

class sklearn.feature\_extraction.text.TfidfVectorizer(_\*_, _input\='content'_, _encoding\='utf-8'_, _decode\_error\='strict'_, _strip\_accents\=None_, _lowercase\=True_, _preprocessor\=None_, _tokenizer\=None_, _analyzer\='word'_, _stop\_words\=None_, _token\_pattern\='(?u)\\\\b\\\\w\\\\w+\\\\b'_, _ngram\_range\=(1_, _1)_, _max\_df\=1.0_, _min\_df\=1_, _max\_features\=None_, _vocabulary\=None_, _binary\=False_, _dtype\=<class 'numpy.float64'>_, _norm\='l2'_, _use\_idf\=True_, _smooth\_idf\=True_, _sublinear\_tf\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L1750)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "Link to this definition")

Convert a collection of raw documents to a matrix of TF-IDF features.

Equivalent to [`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
 followed by [`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf)
.

Parameters:

**input**{‘filename’, ‘file’, ‘content’}, default=’content’

*   If `'filename'`, the sequence passed as an argument to fit is expected to be a list of filenames that need reading to fetch the raw content to analyze.
    
*   If `'file'`, the sequence items must have a ‘read’ method (file-like object) that is called to fetch the bytes in memory.
    
*   If `'content'`, the input is expected to be a sequence of items that can be of type string or byte.
    

**encoding**str, default=’utf-8’

If bytes or files are given to analyze, this encoding is used to decode.

**decode\_error**{‘strict’, ‘ignore’, ‘replace’}, default=’strict’

Instruction on what to do if a byte sequence is given to analyze that contains characters not of the given `encoding`. By default, it is ‘strict’, meaning that a UnicodeDecodeError will be raised. Other values are ‘ignore’ and ‘replace’.

**strip\_accents**{‘ascii’, ‘unicode’} or callable, default=None

Remove accents and perform other character normalization during the preprocessing step. ‘ascii’ is a fast method that only works on characters that have a direct ASCII mapping. ‘unicode’ is a slightly slower method that works on any characters. None (default) means no character normalization is performed.

Both ‘ascii’ and ‘unicode’ use NFKD normalization from [`unicodedata.normalize`](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize "(in Python v3.14)")
.

**lowercase**bool, default=True

Convert all characters to lowercase before tokenizing.

**preprocessor**callable, default=None

Override the preprocessing (string transformation) stage while preserving the tokenizing and n-grams generation steps. Only applies if `analyzer` is not callable.

**tokenizer**callable, default=None

Override the string tokenization step while preserving the preprocessing and n-grams generation steps. Only applies if `analyzer == 'word'`.

**analyzer**{‘word’, ‘char’, ‘char\_wb’} or callable, default=’word’

Whether the feature should be made of word or character n-grams. Option ‘char\_wb’ creates character n-grams only from text inside word boundaries; n-grams at the edges of words are padded with space.

If a callable is passed it is used to extract the sequence of features out of the raw, unprocessed input.

Changed in version 0.21: Since v0.21, if `input` is `'filename'` or `'file'`, the data is first read from the file and then passed to the given callable analyzer.

**stop\_words**{‘english’}, list, default=None

If a string, it is passed to \_check\_stop\_list and the appropriate stop list is returned. ‘english’ is currently the only supported string value. There are several known issues with ‘english’ and you should consider an alternative (see [Using stop words](https://scikit-learn.org/stable/modules/feature_extraction.html#stop-words)
).

If a list, that list is assumed to contain stop words, all of which will be removed from the resulting tokens. Only applies if `analyzer == 'word'`.

If None, no stop words will be used. In this case, setting `max_df` to a higher value, such as in the range (0.7, 1.0), can automatically detect and filter stop words based on intra corpus document frequency of terms.

**token\_pattern**str, default=r”(?u)\\b\\w\\w+\\b”

Regular expression denoting what constitutes a “token”, only used if `analyzer == 'word'`. The default regexp selects tokens of 2 or more alphanumeric characters (punctuation is completely ignored and always treated as a token separator).

If there is a capturing group in token\_pattern then the captured group content, not the entire match, becomes the token. At most one capturing group is permitted.

**ngram\_range**tuple (min\_n, max\_n), default=(1, 1)

The lower and upper boundary of the range of n-values for different n-grams to be extracted. All values of n such that min\_n <= n <= max\_n will be used. For example an `ngram_range` of `(1, 1)` means only unigrams, `(1, 2)` means unigrams and bigrams, and `(2, 2)` means only bigrams. Only applies if `analyzer` is not callable.

**max\_df**float or int, default=1.0

When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). If float in range \[0.0, 1.0\], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.

**min\_df**float or int, default=1

When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature. If float in range of \[0.0, 1.0\], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.

**max\_features**int, default=None

If not None, build a vocabulary that only consider the top `max_features` ordered by term frequency across the corpus. Otherwise, all features are used.

This parameter is ignored if vocabulary is not None.

**vocabulary**Mapping or iterable, default=None

Either a Mapping (e.g., a dict) where keys are terms and values are indices in the feature matrix, or an iterable over terms. If not given, a vocabulary is determined from the input documents.

**binary**bool, default=False

If True, all non-zero term counts are set to 1. This does not mean outputs will have only 0/1 values, only that the tf term in tf-idf is binary. (Set `binary` to True, `use_idf` to False and `norm` to None to get 0/1 outputs).

**dtype**dtype, default=float64

Type of the matrix returned by fit\_transform() or transform().

**norm**{‘l1’, ‘l2’} or None, default=’l2’

Each output row will have unit norm, either:

*   ‘l2’: Sum of squares of vector elements is 1. The cosine similarity between two vectors is their dot product when l2 norm has been applied.
    
*   ‘l1’: Sum of absolute values of vector elements is 1. See [`normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")
    .
    
*   None: No normalization.
    

**use\_idf**bool, default=True

Enable inverse-document-frequency reweighting. If False, idf(t) = 1.

**smooth\_idf**bool, default=True

Smooth idf weights by adding one to document frequencies, as if an extra document was seen containing every term in the collection exactly once. Prevents zero divisions.

**sublinear\_tf**bool, default=False

Apply sublinear tf scaling, i.e. replace tf with 1 + log(tf).

Attributes:

**vocabulary\_**dict

A mapping of terms to feature indices.

**fixed\_vocabulary\_**bool

True if a fixed vocabulary of term to indices mapping is provided by the user.

`idf_`array of shape (n\_features,)

Inverse document frequency vector, only defined if `use_idf=True`.

See also

[`CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")

Transforms text into a sparse matrix of n-gram counts.

[`TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")

Performs the TF-IDF transformation from a provided matrix of counts.

Examples

\>>> from sklearn.feature\_extraction.text import TfidfVectorizer
\>>> corpus \= \[\
...     'This is the first document.',\
...     'This document is the second document.',\
...     'And this is the third one.',\
...     'Is this the first document?',\
... \]
\>>> vectorizer \= TfidfVectorizer()
\>>> X \= vectorizer.fit\_transform(corpus)
\>>> vectorizer.get\_feature\_names\_out()
array(\['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third',\
       'this'\], ...)
\>>> print(X.shape)
(4, 9)

Copy to clipboard

build\_analyzer()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L425)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_analyzer "Link to this definition")

Return a callable to process input data.

The callable handles preprocessing, tokenization, and n-grams generation.

Returns:

analyzer: callable

A function to handle preprocessing, tokenization and n-grams generation.

build\_preprocessor()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L329)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_preprocessor "Link to this definition")

Return a function to preprocess the text before tokenization.

Returns:

preprocessor: callable

A function to preprocess the text before tokenization.

build\_tokenizer()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L356)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.build_tokenizer "Link to this definition")

Return a function that splits a string into a sequence of tokens.

Returns:

tokenizer: callable

A function to split a string into a sequence of tokens.

decode(_doc_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L216)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.decode "Link to this definition")

Decode the input into a string of unicode symbols.

The decoding strategy depends on the vectorizer parameters.

Parameters:

**doc**bytes or str

The string to decode.

Returns:

doc: str

A string of unicode symbols.

fit(_raw\_documents_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L2055)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.fit "Link to this definition")

Learn vocabulary and idf from training set.

Parameters:

**raw\_documents**iterable

An iterable which generates either str, unicode or file objects.

**y**None

This parameter is not needed to compute tfidf.

Returns:

**self**object

Fitted vectorizer.

fit\_transform(_raw\_documents_, _y\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L2084)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.fit_transform "Link to this definition")

Learn vocabulary and idf, return document-term matrix.

This is equivalent to fit followed by transform, but more efficiently implemented.

Parameters:

**raw\_documents**iterable

An iterable which generates either str, unicode or file objects.

**y**None

This parameter is ignored.

Returns:

**X**sparse matrix of (n\_samples, n\_features)

Tf-idf-weighted document-term matrix.

get\_feature\_names\_out(_input\_features\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L1475)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.get_feature_names_out "Link to this definition")

Get output feature names for transformation.

Parameters:

**input\_features**array-like of str or None, default=None

Not used, present here for API consistency by convention.

Returns:

**feature\_names\_out**ndarray of str objects

Transformed feature names.

get\_metadata\_routing()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_metadata_requests.py#L1743)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.get_metadata_routing "Link to this definition")

Get metadata routing of this object.

Please check [User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing)
 on how the routing mechanism works.

Returns:

**routing**MetadataRequest

A [`MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")
 encapsulating routing information.

get\_params(_deep\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L248)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.get_params "Link to this definition")

Get parameters for this estimator.

Parameters:

**deep**bool, default=True

If True, will return the parameters for this estimator and contained subobjects that are estimators.

Returns:

**params**dict

Parameter names mapped to their values.

get\_stop\_words()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L376)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.get_stop_words "Link to this definition")

Build or fetch the effective stop words list.

Returns:

stop\_words: list or None

A list of stop words.

inverse\_transform(_X_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L1437)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.inverse_transform "Link to this definition")

Return terms per document with nonzero entries in X.

Parameters:

**X**{array-like, sparse matrix} of shape (n\_samples, n\_features)

Document-term matrix.

Returns:

**X\_original**list of arrays of shape (n\_samples,)

List of arrays of terms.

set\_params(_\*\*params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L400)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.set_params "Link to this definition")

Set the parameters of this estimator.

The method works on simple estimators as well as on nested objects (such as [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.

Parameters:

**\*\*params**dict

Estimator parameters.

Returns:

**self**estimator instance

Estimator instance.

transform(_raw\_documents_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/text.py#L2116)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer.transform "Link to this definition")

Transform documents to document-term matrix.

Uses the vocabulary and document frequencies (df) learned by fit (or fit\_transform).

Parameters:

**raw\_documents**iterable

An iterable which generates either str, unicode or file objects.

Returns:

**X**sparse matrix of (n\_samples, n\_features)

Tf-idf-weighted document-term matrix.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_topics_extraction_with_nmf_lda_thumb.png)

[Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation](https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html)

Topic extraction with Non-negative Matrix Factorization and Latent Dirichlet Allocation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_thumb.png)

[Column Transformer with Heterogeneous Data Sources](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)

Column Transformer with Heterogeneous Data Sources

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_text_feature_extraction_thumb.png)

[Sample pipeline for text feature extraction and evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_text_feature_extraction.html)

Sample pipeline for text feature extraction and evaluation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_clustering_thumb.png)

[Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html)

Clustering text documents using k-means

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)