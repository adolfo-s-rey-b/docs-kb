[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.murmurhash3_32.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.murmurhash3_32.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.murmurhash3_32.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.murmurhash3_32.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.murmurhash3_32.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.murmurhash3_32.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.murmurhash3_32.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.murmurhash3_32.html)

Collapse Sidebar Expand Sidebar

murmurhash3\_32[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.murmurhash3_32.html#murmurhash3-32 "Link to this heading")

==============================================================================================================================================

sklearn.utils.murmurhash3\_32(_key_, _seed\=0_, _positive\=False_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.murmurhash3_32.html#sklearn.utils.murmurhash3_32 "Link to this definition")

Compute the 32bit murmurhash3 of key at seed.

The underlying implementation is MurmurHash3\_x86\_32 generating low latency 32bits hash suitable for implementing lookup tables, Bloom filters, count min sketch or feature hashing.

Parameters:

**key**np.int32, bytes, unicode or ndarray of dtype=np.int32

The physical object to hash.

**seed**int, default=0

Integer seed for the hashing algorithm.

**positive**bool, default=False

True: the results is casted to an unsigned int

from 0 to 2 \*\* 32 - 1

False: the results is casted to a signed int

from -(2 \*\* 31) to 2 \*\* 31 - 1

Examples

\>>> from sklearn.utils import murmurhash3\_32
\>>> murmurhash3\_32(b"Hello World!", seed\=42)
3565178

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)