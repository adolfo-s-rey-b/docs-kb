[Skip to main content](https://numpy.org/doc/stable/user/byteswapping.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/byteswapping.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/byteswapping.html)
[2.4](https://numpy.org/doc/2.4/user/byteswapping.html)
[2.3](https://numpy.org/doc/2.3/user/byteswapping.html)
[2.2](https://numpy.org/doc/2.2/user/byteswapping.html)
[2.1](https://numpy.org/doc/2.1/user/byteswapping.html)
[2.0](https://numpy.org/doc/2.0/user/byteswapping.html)
[1.26](https://numpy.org/doc/1.26/user/byteswapping.html)
[1.25](https://numpy.org/doc/1.25/user/byteswapping.html)
[1.24](https://numpy.org/doc/1.24/user/byteswapping.html)
[1.23](https://numpy.org/doc/1.23/user/byteswapping.html)
[1.22](https://numpy.org/doc/1.22/user/byteswapping.html)
[1.21](https://numpy.org/doc/1.21/user/byteswapping.html)
[1.20](https://numpy.org/doc/1.20/user/byteswapping.html)
[1.19](https://numpy.org/doc/1.19/user/byteswapping.html)
[1.18](https://numpy.org/doc/1.18/user/byteswapping.html)
[1.17](https://numpy.org/doc/1.17/user/byteswapping.html)
[1.16](https://numpy.org/doc/1.16/user/byteswapping.html)
[1.15](https://numpy.org/doc/1.15/user/byteswapping.html)
[1.14](https://numpy.org/doc/1.14/user/byteswapping.html)
[1.13](https://numpy.org/doc/1.13/user/byteswapping.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Byte-swapping[#](https://numpy.org/doc/stable/user/byteswapping.html#byte-swapping "Link to this heading")

===========================================================================================================

Introduction to byte ordering and ndarrays[#](https://numpy.org/doc/stable/user/byteswapping.html#introduction-to-byte-ordering-and-ndarrays "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `ndarray` is an object that provides a python array interface to data in memory.

It often happens that the memory that you want to view with an array is not of the same byte ordering as the computer on which you are running Python.

For example, I might be working on a computer with a little-endian CPU - such as an Intel Pentium, but I have loaded some data from a file written by a computer that is big-endian. Let’s say I have loaded 4 bytes from a file written by a Sun (big-endian) computer. I know that these 4 bytes represent two 16-bit integers. On a big-endian machine, a two-byte integer is stored with the Most Significant Byte (MSB) first, and then the Least Significant Byte (LSB). Thus the bytes are, in memory order:

1.  MSB integer 1
    
2.  LSB integer 1
    
3.  MSB integer 2
    
4.  LSB integer 2
    

Let’s say the two integers were in fact 1 and 770. Because 770 = 256 \* 3 + 2, the 4 bytes in memory would contain respectively: 0, 1, 3, 2. The bytes I have loaded from the file would have these contents:

\>>> big\_end\_buffer \= bytearray(\[0,1,3,2\])
\>>> big\_end\_buffer
bytearray(b'\\x00\\x01\\x03\\x02')

Copy to clipboard

We might want to use an `ndarray` to access these integers. In that case, we can create an array around this memory, and tell numpy that there are two integers, and that they are 16 bit and big-endian:

\>>> import numpy as np
\>>> big\_end\_arr \= np.ndarray(shape\=(2,),dtype\='>i2', buffer\=big\_end\_buffer)
\>>> big\_end\_arr\[0\]
np.int16(1)
\>>> big\_end\_arr\[1\]
np.int16(770)

Copy to clipboard

Note the array `dtype` above of `>i2`. The `>` means ‘big-endian’ (`<` is little-endian) and `i2` means ‘signed 2-byte integer’. For example, if our data represented a single unsigned 4-byte little-endian integer, the dtype string would be `<u4`.

In fact, why don’t we try that?

\>>> little\_end\_u4 \= np.ndarray(shape\=(1,),dtype\='<u4', buffer\=big\_end\_buffer)
\>>> little\_end\_u4\[0\] \== 1 \* 256\*\*1 + 3 \* 256\*\*2 + 2 \* 256\*\*3
True

Copy to clipboard

Returning to our `big_end_arr` - in this case our underlying data is big-endian (data endianness) and we’ve set the dtype to match (the dtype is also big-endian). However, sometimes you need to flip these around.

Warning

Scalars do not include byte order information, so extracting a scalar from an array will return an integer in native byte order. Hence:

\>>> big\_end\_arr\[0\].dtype.byteorder \== little\_end\_u4\[0\].dtype.byteorder
True

Copy to clipboard

NumPy intentionally does not attempt to always preserve byte-order and for example converts to native byte-order in [`numpy.concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
.

Changing byte ordering[#](https://numpy.org/doc/stable/user/byteswapping.html#changing-byte-ordering "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

As you can imagine from the introduction, there are two ways you can affect the relationship between the byte ordering of the array and the underlying memory it is looking at:

*   Change the byte-ordering information in the array dtype so that it interprets the underlying data as being in a different byte order. This is the role of `arr.view(arr.dtype.newbyteorder())`
    
*   Change the byte-ordering of the underlying data, leaving the dtype interpretation as it was. This is what `arr.byteswap()` does.
    

The common situations in which you need to change byte ordering are:

1.  Your data and dtype endianness don’t match, and you want to change the dtype so that it matches the data.
    
2.  Your data and dtype endianness don’t match, and you want to swap the data so that they match the dtype
    
3.  Your data and dtype endianness match, but you want the data swapped and the dtype to reflect this
    

### Data and dtype endianness don’t match, change dtype to match data[#](https://numpy.org/doc/stable/user/byteswapping.html#data-and-dtype-endianness-don-t-match-change-dtype-to-match-data "Link to this heading")

We make something where they don’t match:

\>>> wrong\_end\_dtype\_arr \= np.ndarray(shape\=(2,),dtype\='<i2', buffer\=big\_end\_buffer)
\>>> wrong\_end\_dtype\_arr\[0\]
np.int16(256)

Copy to clipboard

The obvious fix for this situation is to change the dtype so it gives the correct endianness:

\>>> fixed\_end\_dtype\_arr \= wrong\_end\_dtype\_arr.view(np.dtype('<i2').newbyteorder())
\>>> fixed\_end\_dtype\_arr\[0\]
np.int16(1)

Copy to clipboard

Note the array has not changed in memory:

\>>> fixed\_end\_dtype\_arr.tobytes() \== big\_end\_buffer
True

Copy to clipboard

### Data and type endianness don’t match, change data to match dtype[#](https://numpy.org/doc/stable/user/byteswapping.html#data-and-type-endianness-don-t-match-change-data-to-match-dtype "Link to this heading")

You might want to do this if you need the data in memory to be a certain ordering. For example you might be writing the memory out to a file that needs a certain byte ordering.

\>>> fixed\_end\_mem\_arr \= wrong\_end\_dtype\_arr.byteswap()
\>>> fixed\_end\_mem\_arr\[0\]
np.int16(1)

Copy to clipboard

Now the array _has_ changed in memory:

\>>> fixed\_end\_mem\_arr.tobytes() \== big\_end\_buffer
False

Copy to clipboard

### Data and dtype endianness match, swap data and dtype[#](https://numpy.org/doc/stable/user/byteswapping.html#data-and-dtype-endianness-match-swap-data-and-dtype "Link to this heading")

You may have a correctly specified array dtype, but you need the array to have the opposite byte order in memory, and you want the dtype to match so the array values make sense. In this case you just do both of the previous operations:

\>>> swapped\_end\_arr \= big\_end\_arr.byteswap()
\>>> swapped\_end\_arr \= swapped\_end\_arr.view(swapped\_end\_arr.dtype.newbyteorder())
\>>> swapped\_end\_arr\[0\]
np.int16(1)
\>>> swapped\_end\_arr.tobytes() \== big\_end\_buffer
False

Copy to clipboard

An easier way of casting the data to a specific dtype and byte ordering can be achieved with the ndarray astype method:

\>>> swapped\_end\_arr \= big\_end\_arr.astype('<i2')
\>>> swapped\_end\_arr\[0\]
np.int16(1)
\>>> swapped\_end\_arr.tobytes() \== big\_end\_buffer
False

Copy to clipboard

On this page