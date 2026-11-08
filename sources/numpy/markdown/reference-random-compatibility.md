[Skip to main content](https://numpy.org/doc/stable/reference/random/compatibility.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/compatibility.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/compatibility.html)
[2.4](https://numpy.org/doc/2.4/reference/random/compatibility.html)
[2.3](https://numpy.org/doc/2.3/reference/random/compatibility.html)
[2.2](https://numpy.org/doc/2.2/reference/random/compatibility.html)
[2.1](https://numpy.org/doc/2.1/reference/random/compatibility.html)
[2.0](https://numpy.org/doc/2.0/reference/random/compatibility.html)
[1.26](https://numpy.org/doc/1.26/reference/random/compatibility.html)
[1.25](https://numpy.org/doc/1.25/reference/random/compatibility.html)
[1.24](https://numpy.org/doc/1.24/reference/random/compatibility.html)
[1.23](https://numpy.org/doc/1.23/reference/random/compatibility.html)
[1.22](https://numpy.org/doc/1.22/reference/random/compatibility.html)
[1.21](https://numpy.org/doc/1.21/reference/random/compatibility.html)
[1.20](https://numpy.org/doc/1.20/reference/random/compatibility.html)
[1.19](https://numpy.org/doc/1.19/reference/random/compatibility.html)
[1.18](https://numpy.org/doc/1.18/reference/random/compatibility.html)
[1.17](https://numpy.org/doc/1.17/reference/random/compatibility.html)
[1.16](https://numpy.org/doc/1.16/reference/random/compatibility.html)
[1.15](https://numpy.org/doc/1.15/reference/random/compatibility.html)
[1.14](https://numpy.org/doc/1.14/reference/random/compatibility.html)
[1.13](https://numpy.org/doc/1.13/reference/random/compatibility.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Compatibility policy[#](https://numpy.org/doc/stable/reference/random/compatibility.html#compatibility-policy "Link to this heading")

======================================================================================================================================

[`numpy.random`](https://numpy.org/doc/stable/reference/random/index.html#module-numpy.random "numpy.random")
 has a somewhat stricter compatibility policy than the rest of NumPy. Users of pseudorandomness often have use cases for being able to reproduce runs in fine detail given the same seed (so-called “stream compatibility”), and so we try to balance those needs with the flexibility to enhance our algorithms. [NEP 19](https://numpy.org/neps/nep-0019-rng-policy.html#nep19 "(in NumPy Enhancement Proposals)")
 describes the evolution of this policy.

The main kind of compatibility that we enforce is stream-compatibility from run to run under certain conditions. If you create a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 with the same [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
, with the same seed, perform the same sequence of method calls with the same arguments, on the same build of `numpy`, in the same environment, on the same machine, you should get the same stream of numbers. Note that these conditions are very strict. There are a number of factors outside of NumPy’s control that limit our ability to guarantee much more than this. For example, different CPUs implement floating point arithmetic differently, and this can cause differences in certain edge cases that cascade to the rest of the stream. [`Generator.multivariate_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html#numpy.random.Generator.multivariate_normal "numpy.random.Generator.multivariate_normal")
, for another example, uses a matrix decomposition from [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
. Even on the same platform, a different build of `numpy` may use a different version of this matrix decomposition algorithm from the LAPACK that it links to, causing [`Generator.multivariate_normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multivariate_normal.html#numpy.random.Generator.multivariate_normal "numpy.random.Generator.multivariate_normal")
 to return completely different (but equally valid!) results. We strive to prefer algorithms that are more resistant to these effects, but this is always imperfect.

Note

Most of the [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 methods allow you to draw multiple values from a distribution as arrays. The requested size of this array is a parameter, for the purposes of the above policy. Calling `rng.random()` 5 times is not _guaranteed_ to give the same numbers as `rng.random(5)`. We reserve the ability to decide to use different algorithms for different-sized blocks. In practice, this happens rarely.

Like the rest of NumPy, we generally maintain API source compatibility from version to version. If we _must_ make an API-breaking change, then we will only do so with an appropriate deprecation period and warnings, according to [general NumPy policy](https://numpy.org/neps/nep-0023-backwards-compatibility.html#nep23 "(in NumPy Enhancement Proposals)")
.

Breaking stream-compatibility in order to introduce new features or improve performance in [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 or [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 will be _allowed_ with _caution_. Such changes will be considered features, and as such will be no faster than the standard release cadence of features (i.e. on `X.Y` releases, never `X.Y.Z`). Slowness will not be considered a bug for this purpose. Correctness bug fixes that break stream-compatibility can happen on bugfix releases, per usual, but developers should consider if they can wait until the next feature release. We encourage developers to strongly weight user’s pain from the break in stream-compatibility against the improvements. One example of a worthwhile improvement would be to change algorithms for a significant increase in performance, for example, moving from the [Box-Muller transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform)
 method of Gaussian variate generation to the faster [Ziggurat algorithm](https://en.wikipedia.org/wiki/Ziggurat_algorithm)
. An example of a discouraged improvement would be tweaking the Ziggurat tables just a little bit for a small performance improvement.

Note

In particular, [`default_rng`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
 is allowed to change the default [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 that it uses (again, with _caution_ and plenty of advance warning).

In general, [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 classes have stronger guarantees of version-to-version stream compatibility. This allows them to be a firmer building block for downstream users that need it. Their limited API surface makes it easier for them to maintain this compatibility from version to version. See the docstrings of each [`BitGenerator`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.html#numpy.random.BitGenerator "numpy.random.BitGenerator")
 class for their individual compatibility guarantees.

The legacy [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 and the [associated convenience functions](https://numpy.org/doc/stable/reference/random/legacy.html#functions-in-numpy-random)
 have a stricter version-to-version compatibility guarantee. For reasons outlined in [NEP 19](https://numpy.org/neps/nep-0019-rng-policy.html#nep19 "(in NumPy Enhancement Proposals)")
, we had made stronger promises about their version-to-version stability early in NumPy’s development. There are still some limited use cases for this kind of compatibility (like generating data for tests), so we maintain as much compatibility as we can. There will be no more modifications to [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
, not even to fix correctness bugs. There are a few gray areas where we can make minor fixes to keep [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 working without segfaulting as NumPy’s internals change, and some docstring fixes. However, the previously-mentioned caveats about the variability from machine to machine and build to build still apply to [`RandomState`](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 just as much as it does to [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
.