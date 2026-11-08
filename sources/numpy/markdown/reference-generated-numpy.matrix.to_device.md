[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.to_device.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matrix.to\_device[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.to_device.html#numpy-matrix-to-device "Link to this heading")

=======================================================================================================================================================

method

matrix.to\_device(_device_, _/_, _\*_, _stream\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.to_device.html#numpy.matrix.to_device "Link to this definition")

For Array API compatibility. Since NumPy only supports CPU arrays, this method is a no-op that returns the same array.

Parameters:

**device**“cpu”

Must be `"cpu"`.

**stream**None, optional

Currently unsupported.

Returns:

**out**Self

Returns the same array.

On this page