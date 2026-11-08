[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.SeedSequence[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy-random-seedsequence "Link to this heading")

=====================================================================================================================================================================================

_class_ numpy.random.SeedSequence(_entropy\=None_, _\*_, _spawn\_key\=()_, _pool\_size\=4_, _n\_children\_spawned\=0_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "Link to this definition")

SeedSequence mixes sources of entropy in a reproducible way to set the initial state for independent and very probably non-overlapping BitGenerators.

Once the SeedSequence is instantiated, you can call the [`generate_state`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html#numpy.random.SeedSequence.generate_state "numpy.random.SeedSequence.generate_state")
 method to get an appropriately sized seed. Calling [`spawn(n)`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
 will create `n` SeedSequences that can be used to seed independent BitGenerators, i.e. for different threads.

Parameters:

**entropy**{None, int, sequence\[int\]}, optional

The entropy for creating a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
. All integer values must be non-negative.

**spawn\_key**{(), sequence\[int\]}, optional

An additional source of entropy based on the position of this [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 in the tree of such objects created with the [`SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
 method. Typically, only [`SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")
 will set this, and users will not.

**pool\_size**{int}, optional

Size of the pooled entropy to store. Default is 4 to give a 128-bit entropy pool. 8 (for 256 bits) is another reasonable choice if working with larger PRNGs, but there is very little to be gained by selecting another value.

**n\_children\_spawned**{int}, optional

The number of children already spawned. Only pass this if reconstructing a [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")
 from a serialized form.

Attributes:

**entropy**

**n\_children\_spawned**

**pool**

**pool\_size**

**spawn\_key**

**state**

Methods

|     |     |
| --- | --- |
| [`generate_state`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.generate_state.html#numpy.random.SeedSequence.generate_state "numpy.random.SeedSequence.generate_state")<br>(n\_words\[, dtype\]) | Return the requested number of words for PRNG seeding. |
| [`spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")<br>(n\_children) | Spawn a number of child [`SeedSequence`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.html#numpy.random.SeedSequence "numpy.random.SeedSequence")<br> s by extending the [`spawn_key`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn_key.html#numpy.random.SeedSequence.spawn_key "numpy.random.SeedSequence.spawn_key")<br>. |

Notes

Best practice for achieving reproducible bit streams is to use the default `None` for the initial entropy, and then use [`SeedSequence.entropy`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.entropy.html#numpy.random.SeedSequence.entropy "numpy.random.SeedSequence.entropy")
 to log/pickle the [`entropy`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.entropy.html#numpy.random.SeedSequence.entropy "numpy.random.SeedSequence.entropy")
 for reproducibility:

\>>> sq1 \= np.random.SeedSequence()
\>>> sq1.entropy
243799254704924441050048792905230269161  # random
\>>> sq2 \= np.random.SeedSequence(sq1.entropy)
\>>> np.all(sq1.generate\_state(10) \== sq2.generate\_state(10))
True

Copy to clipboard

On this page