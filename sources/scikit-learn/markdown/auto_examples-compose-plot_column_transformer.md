[Skip to main content](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/compose/plot_column_transformer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/compose/plot_column_transformer.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/compose/plot_column_transformer.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/compose/plot_column_transformer.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/compose/plot_column_transformer.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/compose/plot_column_transformer.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#sphx-glr-download-auto-examples-compose-plot-column-transformer-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Column Transformer with Heterogeneous Data Sources[#](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#column-transformer-with-heterogeneous-data-sources "Link to this heading")

====================================================================================================================================================================================================================

Datasets can often contain components that require different feature extraction and processing pipelines. This scenario might occur when:

1.  your dataset consists of heterogeneous data types (e.g. raster images and text captions),
    
2.  your dataset is stored in a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame "(in pandas v3.0.5)")
     and different columns require different processing pipelines.
    

This example demonstrates how to use [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
 on a dataset containing different types of features. The choice of features is not particularly helpful, but serves to illustrate the technique.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import numpy as np

from sklearn.compose import [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")
from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.feature\_extraction import [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")
from sklearn.feature\_extraction.text import [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")
from sklearn.metrics import [classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.preprocessing import [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
from sklearn.svm import [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")

Copy to clipboard

20 newsgroups dataset[#](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#newsgroups-dataset "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

We will use the [20 newsgroups dataset](https://scikit-learn.org/stable/datasets/real_world.html#newsgroups-dataset)
, which comprises posts from newsgroups on 20 topics. This dataset is split into train and test subsets based on messages posted before and after a specific date. We will only use posts from 2 categories to speed up running time.

categories \= \["sci.med", "sci.space"\]
X\_train, y\_train \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    random\_state\=1,
    subset\="train",
    categories\=categories,
    remove\=("footers", "quotes"),
    return\_X\_y\=True,
)
X\_test, y\_test \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    random\_state\=1,
    subset\="test",
    categories\=categories,
    remove\=("footers", "quotes"),
    return\_X\_y\=True,
)

Copy to clipboard

Each feature comprises meta information about that post, such as the subject, and the body of the news post.

print(X\_train\[0\])

Copy to clipboard

From: mccall@mksol.dseg.ti.com (fred j mccall 575-3539)
Subject: Re: Metric vs English
Article-I.D.: mksol.1993Apr6.131900.8407
Organization: Texas Instruments Inc
Lines: 31




American, perhaps, but nothing military about it.  I learned (mostly)
slugs when we talked English units in high school physics and while
the teacher was an ex-Navy fighter jock the book certainly wasn't
produced by the military.

\[Poundals were just too flinking small and made the math come out\
funny; sort of the same reason proponents of SI give for using that.\]

--
"Insisting on perfect safety is for people who don't have the balls to live
 in the real world."   -- Mary Shafer, NASA Ames Dryden

Copy to clipboard

Creating transformers[#](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#creating-transformers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

First, we would like a transformer that extracts the subject and body of each post. Since this is a stateless transformation (does not require state information from training data), we can define a function that performs the data transformation then use [`FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
 to create a scikit-learn transformer.

def subject\_body\_extractor(posts):
    \# construct object dtype array with two columns
    \# first column = 'subject' and second column = 'body'
    features \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
(shape\=(len(posts), 2), dtype\=object)
    for i, text in enumerate(posts):
        \# temporary variable \`\_\` stores '\\n\\n'
        headers, \_, body \= text.partition("\\n\\n")
        \# store body text in second column
        features\[i, 1\] \= body

        prefix \= "Subject:"
        sub \= ""
        \# save text after 'Subject:' in first column
        for line in headers.split("\\n"):
            if line.startswith(prefix):
                sub \= line\[len(prefix) :\]
                break
        features\[i, 0\] \= sub

    return features

subject\_body\_transformer \= [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
(subject\_body\_extractor)

Copy to clipboard

We will also create a transformer that extracts the length of the text and the number of sentences.

def text\_stats(posts):
    return \[{"length": len(text), "num\_sentences": text.count(".")} for text in posts\]

text\_stats\_transformer \= [FunctionTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer")
(text\_stats)

Copy to clipboard

Classification pipeline[#](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer.html#classification-pipeline "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

The pipeline below extracts the subject and body from each post using `SubjectBodyExtractor`, producing a (n\_samples, 2) array. This array is then used to compute standard bag-of-words features for the subject and body as well as text length and number of sentences on the body, using `ColumnTransformer`. We combine them, with weights, then train a classifier on the combined set of features.

pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        \# Extract subject & body\
        ("subjectbody", subject\_body\_transformer),\
        \# Use ColumnTransformer to combine the subject and body features\
        (\
            "union",\
            [ColumnTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")\
(\
                \[\
                    \# bag-of-words for subject (col 0)\
                    ("subject", [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")\
(min\_df\=50), 0),\
                    \# bag-of-words with decomposition for body (col 1)\
                    (\
                        "body\_bow",\
                        [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
                            \[\
                                ("tfidf", [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")\
()),\
                                ("best", [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")\
(n\_components\=50, svd\_solver\="arpack")),\
                            \]\
                        ),\
                        1,\
                    ),\
                    \# Pipeline for pulling text stats from post's body\
                    (\
                        "body\_stats",\
                        [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")\
(\
                            \[\
                                (\
                                    "stats",\
                                    text\_stats\_transformer,\
                                ),  \# returns a list of dicts\
                                (\
                                    "vect",\
                                    [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer")\
(),\
                                ),  \# list of dicts -> feature matrix\
                            \]\
                        ),\
                        1,\
                    ),\
                \],\
                \# weight above ColumnTransformer features\
                transformer\_weights\={\
                    "subject": 0.8,\
                    "body\_bow": 0.5,\
                    "body\_stats": 1.0,\
                },\
            ),\
        ),\
        \# Use an SVC classifier on the combined features\
        ("svc", [LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(dual\=False)),\
    \],
    verbose\=True,
)

Copy to clipboard

Finally, we fit our pipeline on the training data and use it to predict topics for `X_test`. Performance metrics of our pipeline are then printed.

pipeline.fit(X\_train, y\_train)
y\_pred \= pipeline.predict(X\_test)
print("Classification report:\\n\\n{}".format([classification\_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")
(y\_test, y\_pred)))

Copy to clipboard

\[Pipeline\] ....... (step 1 of 3) Processing subjectbody, total=   0.0s
\[Pipeline\] ............. (step 2 of 3) Processing union, total=   0.4s
\[Pipeline\] ............... (step 3 of 3) Processing svc, total=   0.0s
Classification report:

              precision    recall  f1-score   support

           0       0.84      0.87      0.86       396
           1       0.87      0.84      0.85       394

    accuracy                           0.86       790
   macro avg       0.86      0.86      0.86       790
weighted avg       0.86      0.86      0.86       790

Copy to clipboard

**Total running time of the script:** (0 minutes 2.511 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_column_transformer.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_column_transformer.ipynb)

[`Download Jupyter notebook: plot_column_transformer.ipynb`](https://scikit-learn.org/stable/_downloads/15dc6d7a809edf988a7328336a25faec/plot_column_transformer.ipynb)

[`Download Python source code: plot_column_transformer.py`](https://scikit-learn.org/stable/_downloads/3e8abcbcde21489054beb05cb87da525/plot_column_transformer.py)

[`Download zipped: plot_column_transformer.zip`](https://scikit-learn.org/stable/_downloads/2f1e361eb1d2ca997cf5da2e2651b7bb/plot_column_transformer.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bicluster_newsgroups_thumb.png)

[Biclustering documents with the Spectral Co-clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_bicluster_newsgroups.html)

Biclustering documents with the Spectral Co-clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hashing_vs_dict_vectorizer_thumb.png)

[FeatureHasher and DictVectorizer Comparison](https://scikit-learn.org/stable/auto_examples/text/plot_hashing_vs_dict_vectorizer.html)

FeatureHasher and DictVectorizer Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_column_transformer_mixed_types_thumb.png)

[Column Transformer with Mixed Types](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)

Column Transformer with Mixed Types

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/3e8abcbcde21489054beb05cb87da525/plot_column_transformer.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/15dc6d7a809edf988a7328336a25faec/plot_column_transformer.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/2f1e361eb1d2ca997cf5da2e2651b7bb/plot_column_transformer.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo6.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/compose/plot_column_transformer.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo6.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/compose/plot_column_transformer.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)