[Skip to main content](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html#sphx-glr-download-auto-examples-semi-supervised-plot-semi-supervised-newsgroups-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Semi-supervised Classification on a Text Dataset[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html#semi-supervised-classification-on-a-text-dataset "Link to this heading")

================================================================================================================================================================================================================================

This example demonstrates the effectiveness of semi-supervised learning for text classification on [`TF-IDF`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
 features when labeled data is scarce. For such purpose we compare four different approaches:

1.  Supervised learning using 100% of labels in the training set (best-case scenario)
    
    *   Uses [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
         with full supervision
        
    *   Represents the best possible performance when labeled data is abundant
        
2.  Supervised learning using 20% of labels in the training set (baseline)
    
    *   Same model as the best-case scenario but trained on a random 20% subset of the labeled training data
        
    *   Shows the performance degradation of a fully supervised model due to limited labeled data
        
3.  [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")
     (semi-supervised)
    
    *   Uses 20% labeled data + 80% unlabeled data for training
        
    *   Iteratively predicts labels for unlabeled data
        
    *   Demonstrates how self-training can improve performance
        
4.  [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
     (semi-supervised)
    
    *   Uses 20% labeled data + 80% unlabeled data for training
        
    *   Propagates labels through the data manifold
        
    *   Shows how graph-based methods can leverage unlabeled data
        

The example uses the 20 newsgroups dataset, focusing on five categories. The results demonstrate how semi-supervised methods can achieve better performance than supervised learning with limited labeled data by effectively utilizing unlabeled samples.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

from sklearn.datasets import [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
from sklearn.feature\_extraction.text import [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")
, [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")
from sklearn.linear\_model import [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
from sklearn.metrics import [f1\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.pipeline import [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
from sklearn.semi\_supervised import [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
, [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")

\# Loading dataset containing first five categories
data \= [fetch\_20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")
(
    subset\="train",
    categories\=\[\
        "alt.atheism",\
        "comp.graphics",\
        "comp.os.ms-windows.misc",\
        "comp.sys.ibm.pc.hardware",\
        "comp.sys.mac.hardware",\
    \],
)

\# Parameters
sdg\_params \= dict(alpha\=1e-5, penalty\="l2", loss\="log\_loss")
vectorizer\_params \= dict(ngram\_range\=(1, 2), min\_df\=5, max\_df\=0.8)

\# Supervised Pipeline
pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("vect", [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")\
(\*\*vectorizer\_params)),\
        ("tfidf", [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")\
()),\
        ("clf", [SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")\
(\*\*sdg\_params)),\
    \]
)
\# SelfTraining Pipeline
st\_pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("vect", [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")\
(\*\*vectorizer\_params)),\
        ("tfidf", [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")\
()),\
        ("clf", [SelfTrainingClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier")\
([SGDClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")\
(\*\*sdg\_params))),\
    \]
)
\# LabelSpreading Pipeline
ls\_pipeline \= [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("vect", [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")\
(\*\*vectorizer\_params)),\
        ("tfidf", [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")\
()),\
        ("clf", [LabelSpreading](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")\
()),\
    \]
)

def eval\_and\_get\_f1(clf, X\_train, y\_train, X\_test, y\_test):
    """Evaluate model performance and return F1 score"""
    print(f"   Number of training samples: {len(X\_train)}")
    print(f"   Unlabeled samples in training set: {sum(1 for x in y\_train if x \== \-1)}")
    clf.fit(X\_train, y\_train)
    y\_pred \= clf.predict(X\_test)
    f1 \= [f1\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
(y\_test, y\_pred, average\="micro")
    print(f"   Micro-averaged F1 score on test set: {f1:.3f}")
    print("\\n")
    return f1

X, y \= data.data, data.target
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y)

Copy to clipboard

1\. Evaluate a supervised SGDClassifier using 100% of the (labeled) training set. This represents the best-case performance when the model has full access to all labeled examples.

f1\_scores \= {}
print("1. Supervised SGDClassifier on 100% of the data:")
f1\_scores\["Supervised (100%)"\] \= eval\_and\_get\_f1(
    pipeline, X\_train, y\_train, X\_test, y\_test
)

Copy to clipboard

1\. Supervised SGDClassifier on 100% of the data:
   Number of training samples: 2117
   Unlabeled samples in training set: 0
   Micro-averaged F1 score on test set: 0.901

Copy to clipboard

2\. Evaluate a supervised SGDClassifier trained on only 20% of the data. This serves as a baseline to illustrate the performance drop caused by limiting the training samples.

import numpy as np

print("2. Supervised SGDClassifier on 20% of the training data:")
rng \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(42)
y\_mask \= rng.random(len(y\_train)) < 0.2
\# X\_20 and y\_20 are the subset of the train dataset indicated by the mask
X\_20, y\_20 \= map(list, zip(\*((x, y) for x, y, m in zip(X\_train, y\_train, y\_mask) if m)))
f1\_scores\["Supervised (20%)"\] \= eval\_and\_get\_f1(pipeline, X\_20, y\_20, X\_test, y\_test)

Copy to clipboard

2\. Supervised SGDClassifier on 20% of the training data:
   Number of training samples: 434
   Unlabeled samples in training set: 0
   Micro-averaged F1 score on test set: 0.775

Copy to clipboard

3\. Evaluate a semi-supervised SelfTrainingClassifier using 20% labeled and 80% unlabeled data. The remaining 80% of the training labels are masked as unlabeled (-1), allowing the model to iteratively label and learn from them.

print(
    "3. SelfTrainingClassifier (semi-supervised) using 20% labeled "
    "+ 80% unlabeled data):"
)
y\_train\_semi \= y\_train.copy()
y\_train\_semi\[~y\_mask\] \= \-1
f1\_scores\["SelfTraining"\] \= eval\_and\_get\_f1(
    st\_pipeline, X\_train, y\_train\_semi, X\_test, y\_test
)

Copy to clipboard

3\. SelfTrainingClassifier (semi-supervised) using 20% labeled + 80% unlabeled data):
   Number of training samples: 2117
   Unlabeled samples in training set: 1683
   Micro-averaged F1 score on test set: 0.829

Copy to clipboard

4\. Evaluate a semi-supervised LabelSpreading model using 20% labeled and 80% unlabeled data. Like SelfTraining, the model infers labels for the unlabeled portion of the data to enhance performance.

print("4. LabelSpreading (semi-supervised) using 20% labeled + 80% unlabeled data:")
f1\_scores\["LabelSpreading"\] \= eval\_and\_get\_f1(
    ls\_pipeline, X\_train, y\_train\_semi, X\_test, y\_test
)

Copy to clipboard

4\. LabelSpreading (semi-supervised) using 20% labeled + 80% unlabeled data:
   Number of training samples: 2117
   Unlabeled samples in training set: 1683
   Micro-averaged F1 score on test set: 0.647

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.html#plot-results "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Visualize the performance of different classification approaches using a bar chart. This helps to compare how each method performs based on the micro-averaged [`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")
. Micro-averaging computes metrics globally across all classes, which gives a single overall measure of performance and allows fair comparison between the different approaches, even in the presence of class imbalance.

import matplotlib.pyplot as plt

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 6))

models \= list(f1\_scores.keys())
scores \= list(f1\_scores.values())

colors \= \["royalblue", "royalblue", "forestgreen", "royalblue"\]
bars \= [plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(models, scores, color\=colors)

[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Comparison of Classification Approaches")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("Micro-averaged F1 Score on test set")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
()

for bar in bars:
    height \= bar.get\_height()
    [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(
        bar.get\_x() + bar.get\_width() / 2.0,
        height,
        f"{height:.2f}",
        ha\="center",
        va\="bottom",
    )

[plt.figtext](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figtext.html#matplotlib.pyplot.figtext "matplotlib.pyplot.figtext")
(
    0.5,
    0.02,
    "SelfTraining classifier shows improved performance over "
    "supervised learning with limited data",
    ha\="center",
    va\="bottom",
    fontsize\=10,
    style\="italic",
)

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(bottom\=0.15)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Comparison of Classification Approaches](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_newsgroups_001.png)

**Total running time of the script:** (0 minutes 5.123 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_semi_supervised_newsgroups.ipynb)

[`Download Jupyter notebook: plot_semi_supervised_newsgroups.ipynb`](https://scikit-learn.org/stable/_downloads/ebb639877592982f79ada0c577699e8d/plot_semi_supervised_newsgroups.ipynb)

[`Download Python source code: plot_semi_supervised_newsgroups.py`](https://scikit-learn.org/stable/_downloads/7f9c06d88a8d544a3815452dacaa0548/plot_semi_supervised_newsgroups.py)

[`Download zipped: plot_semi_supervised_newsgroups.zip`](https://scikit-learn.org/stable/_downloads/a9b380a057ec6333fd7e96273331a9b8/plot_semi_supervised_newsgroups.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_semi_supervised_versus_svm_iris_thumb.png)

[Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_semi_supervised_versus_svm_iris.html)

Decision boundary of semi-supervised classifiers versus SVM on the Iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_thumb.png)

[Label Propagation digits: Demonstrating performance](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits.html)

Label Propagation digits: Demonstrating performance

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_label_propagation_digits_active_learning_thumb.png)

[Label Propagation digits: Active learning](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_label_propagation_digits_active_learning.html)

Label Propagation digits: Active learning

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/7f9c06d88a8d544a3815452dacaa0548/plot_semi_supervised_newsgroups.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/ebb639877592982f79ada0c577699e8d/plot_semi_supervised_newsgroups.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a9b380a057ec6333fd7e96273331a9b8/plot_semi_supervised_newsgroups.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo30.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/semi_supervised/plot_semi_supervised_newsgroups.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo30.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/semi_supervised/plot_semi_supervised_newsgroups.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)