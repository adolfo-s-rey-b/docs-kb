[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.spawn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.BitGenerator.spawn[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.spawn.html#numpy-random-bitgenerator-spawn "Link to this heading")

=======================================================================================================================================================================================================

method

random.BitGenerator.spawn(_n\_children_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.spawn.html#numpy.random.BitGenerator.spawn "Link to this definition")

Create new independent child bit generators.

See [SeedSequence spawning](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawn)
 for additional notes on spawning children. Some bit generators also implement `jumped` as a different approach for creating independent streams.

New in version 1.25.0.

Parameters:

**n\_children**int

Returns:

**child\_bit\_generators**list of BitGenerators

Raises:

TypeError

When the underlying SeedSequence does not implement spawning.

See also

[`random.Generator.spawn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#numpy.random.Generator.spawn "numpy.random.Generator.spawn")
, [`random.SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")

Equivalent method on the generator and seed sequence.

On this page