[Skip to main content](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[2.4](https://numpy.org/doc/2.4/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[2.3](https://numpy.org/doc/2.3/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[2.2](https://numpy.org/doc/2.2/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[2.1](https://numpy.org/doc/2.1/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[2.0](https://numpy.org/doc/2.0/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.26](https://numpy.org/doc/1.26/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.25](https://numpy.org/doc/1.25/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.24](https://numpy.org/doc/1.24/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.23](https://numpy.org/doc/1.23/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.22](https://numpy.org/doc/1.22/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.21](https://numpy.org/doc/1.21/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.20](https://numpy.org/doc/1.20/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.19](https://numpy.org/doc/1.19/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.18](https://numpy.org/doc/1.18/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.17](https://numpy.org/doc/1.17/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.16](https://numpy.org/doc/1.16/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.15](https://numpy.org/doc/1.15/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.14](https://numpy.org/doc/1.14/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)
[1.13](https://numpy.org/doc/1.13/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.SeedSequence.spawn[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy-random-seedsequence-spawn "Link to this heading")

=======================================================================================================================================================================================================

method

random.SeedSequence.spawn(_n\_children_)[#](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "Link to this definition")

Spawn a number of child _SeedSequence_ s by extending the [`spawn_key`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn_key.html#numpy.random.SeedSequence.spawn_key "numpy.random.SeedSequence.spawn_key")
.

See [SeedSequence spawning](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawn)
 for additional notes on spawning children.

Parameters:

**n\_children**int

Returns:

**seqs**list of _SeedSequence_ s

See also

[`random.Generator.spawn`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#numpy.random.Generator.spawn "numpy.random.Generator.spawn")
, [`random.BitGenerator.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.spawn.html#numpy.random.BitGenerator.spawn "numpy.random.BitGenerator.spawn")

Equivalent method on the generator and bit generator.

On this page