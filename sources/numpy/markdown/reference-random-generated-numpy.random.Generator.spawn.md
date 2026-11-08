[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.spawn.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.spawn.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.spawn.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.spawn.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.spawn.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.spawn.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.spawn.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.spawn.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.spawn.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.spawn.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.spawn.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.spawn.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.spawn.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.spawn.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.spawn.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.spawn.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.spawn.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.spawn.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.spawn.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.spawn.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.spawn[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#numpy-random-generator-spawn "Link to this heading")

===============================================================================================================================================================================

method

random.Generator.spawn(_n\_children_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.spawn.html#numpy.random.Generator.spawn "Link to this definition")

Create new independent child generators.

See [SeedSequence spawning](https://numpy.org/doc/stable/reference/random/parallel.html#seedsequence-spawn)
 for additional notes on spawning children.

New in version 1.25.0.

Parameters:

**n\_children**int

Returns:

**child\_generators**list of Generators

Raises:

TypeError

When the underlying SeedSequence does not implement spawning.

See also

[`random.BitGenerator.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.BitGenerator.spawn.html#numpy.random.BitGenerator.spawn "numpy.random.BitGenerator.spawn")
, [`random.SeedSequence.spawn`](https://numpy.org/doc/stable/reference/random/bit_generators/generated/numpy.random.SeedSequence.spawn.html#numpy.random.SeedSequence.spawn "numpy.random.SeedSequence.spawn")

Equivalent method on the bit generator and seed sequence.

[`bit_generator`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.bit_generator.html#numpy.random.Generator.bit_generator "numpy.random.Generator.bit_generator")

The bit generator instance used by the generator.

Examples

Try it in your browser!

Starting from a seeded default generator:

\>>> \# High quality entropy created with: f"0x{secrets.randbits(128):x}"
\>>> entropy \= 0x3034c61a9ae04ff8cb62ab8ec2c4b501
\>>> rng \= np.random.default\_rng(entropy)

Copy to clipboard

Create two new generators for example for parallel execution:

\>>> child\_rng1, child\_rng2 \= rng.spawn(2)

Copy to clipboard

Drawn numbers from each are independent but derived from the initial seeding entropy:

\>>> rng.uniform(), child\_rng1.uniform(), child\_rng2.uniform()
(0.19029263503854454, 0.9475673279178444, 0.4702687338396767)

Copy to clipboard

It is safe to spawn additional children from the original `rng` or the children:

\>>> more\_child\_rngs \= rng.spawn(20)
\>>> nested\_spawn \= child\_rng1.spawn(20)

Copy to clipboard

Go BackOpen In Tab

On this page