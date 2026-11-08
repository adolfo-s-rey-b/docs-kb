[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

matplotlib.pyplot.imread[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib-pyplot-imread "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.imread(_fname_, _format\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2759-L2763)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "Link to this definition")

Read an image from a file into an array.

Note

This function exists for historical reasons. It is recommended to use [`PIL.Image.open`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "(in Pillow (PIL Fork) v12.3.0)")
 instead for loading images.

Parameters:

**fname**str or file-like

The image file to read: a filename, a URL or a file-like object opened in read-binary mode.

Passing a URL is deprecated. Please open the URL for reading and pass the result to Pillow, e.g. with `np.array(PIL.Image.open(urllib.request.urlopen(url)))`.

**format**str, optional

The image file format assumed for reading the data. The image is loaded as a PNG file if _format_ is set to "png", if _fname_ is a path or opened file with a ".png" extension, or if it is a URL. In all other cases, _format_ is ignored and the format is auto-detected by [`PIL.Image.open`](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "(in Pillow (PIL Fork) v12.3.0)")
.

Returns:

[`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")

The image data. The returned array has shape

*   (M, N) for grayscale images.
    
*   (M, N, 3) for RGB images.
    
*   (M, N, 4) for RGBA images.
    

PNG images are returned as float arrays (0-1). All other formats are returned as int arrays, with a bit depth determined by the file's contents.

Notes

Note

This is equivalent to [`matplotlib.image.imread`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.imread "matplotlib.image.imread")
.

Examples using `matplotlib.pyplot.imread`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#examples-using-matplotlib-pyplot-imread "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_watermark_image_thumb.png)

[Watermark image](https://matplotlib.org/stable/gallery/images_contours_and_fields/watermark_image.html)

Watermark image

On this page