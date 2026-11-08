[Skip to main content](https://scikit-learn.org/stable/machine_learning_map.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/machine_learning_map.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/machine_learning_map.html)
[1.8.0](https://scikit-learn.org/1.8/machine_learning_map.html)
[1.7.2](https://scikit-learn.org/1.7/machine_learning_map.html)
[1.6.1](https://scikit-learn.org/1.6/machine_learning_map.html)
[1.5.2](https://scikit-learn.org/1.5/machine_learning_map.html)
[1.4.2](https://scikit-learn.org/1.4/machine_learning_map.html)

Collapse Sidebar Expand Sidebar

14\. Choosing the right estimator[#](https://scikit-learn.org/stable/machine_learning_map.html#choosing-the-right-estimator "Link to this heading")

====================================================================================================================================================

Often the hardest part of solving a machine learning problem can be finding the right estimator for the job. Different estimators are better suited for different types of data and different problems.

The flowchart below is designed to give users a bit of a rough guide on how to approach problems with regard to which estimators to try on your data. Click on any estimator in the chart below to see its documentation. The **Try next** orange arrows are to be read as “if this estimator does not achieve the desired outcome, then follow the arrow and try the next one”. Use scroll wheel to zoom in and out, and click and drag to pan around. You can also download the chart: [`ml_map.svg`](https://scikit-learn.org/stable/_downloads/b82bf6cd7438a351f19fac60fbc0d927/ml_map.svg)
.

**START**

START

\>50

samples

\>50...

get

more

data

get...

NO

NO

predicting a

category

predicting...

YES

YES

do you have

labeled

data

do you hav...

YES

YES

predicting a

quantity

predicting...

NO

NO

just

looking

just...

NO

NO

predicting

structure

predicting...

NO

NO

tough  

luck

tough...

<100K

samples

<100K...

YES

YES

SGD

Classifier

SGD...

NO

NO

Linear

SVC

Linear...

YES

YES

text  

data

text...

Kernel

Approximation

Kernel...

KNeighbors

Classifier

KNeighbors...

NO

NO

SVC

SVC

Ensemble

Classifiers

Ensemble...

Naive

Bayes

Naive...

YES

YES

classification

classification

number of  

categories

known

number of...

NO

NO

<10K

samples

<10K...

<10K

samples

<10K...

NO

NO

NO

NO

YES

YES

MeanShift

MeanShift

VBGMM

VBGMM

YES

YES

MiniBatch

KMeans

MiniBatch...

NO

NO

clustering

clustering

KMeans

KMeans

YES

YES

Spectral

Clustering

Spectral...

GMM

GMM

<100K

samples

<100K...

YES

YES

few features

should be

important

few features...

YES

YES

SGD

Regressor

SGD...

NO

NO

Lasso

Lasso

ElasticNet

ElasticNet

YES

YES

RidgeRegression

RidgeRegression

SVR(kernel="linear")

SVR(kernel="linea...

NO

NO

SVR(kernel="rbf")

SVR(kernel="rbf...

Ensemble

Regressors

Ensemble...

regression

regression

Randomized  

PCA

Randomized...

YES

YES

<10K

samples

<10K...

Kernel

Approximation

Kernel...

NO

NO

IsoMap

IsoMap

Spectral

Embedding

Spectral...

YES

YES

LLE

LLE

dimensionality

reduction

dimensionality...

scikit-learn

algorithm cheat sheet

scikit-learn...

TRY

NEXT  

TRY...

TRY

NEXT  

TRY...

TRY

NEXT  

TRY...

TRY

NEXT  

TRY...

TRY

NEXT  

TRY...

TRY

NEXT  

TRY...

TRY

NEXT  

TRY...Text is not SVG - cannot display