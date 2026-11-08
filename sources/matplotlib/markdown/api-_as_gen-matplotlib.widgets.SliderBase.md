[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#main-content)

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
    

matplotlib.widgets.SliderBase[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib-widgets-sliderbase "Link to this heading")

====================================================================================================================================================================

class matplotlib.widgets.SliderBase(_ax_, _orientation_, _closedmin_, _closedmax_, _valmin_, _valmax_, _valfmt_, _dragging_, _valstep_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L304-L379)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase "Link to this definition")

Bases: [`AxesWidget`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.AxesWidget.html#matplotlib.widgets.AxesWidget "matplotlib.widgets.AxesWidget")

The base class for constructing Slider widgets. Not intended for direct usage.

For the slider to remain responsive you must maintain a reference to it.

disconnect(_cid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L365-L374)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase.disconnect "Link to this definition")

Remove the observer with connection id _cid_.

Parameters:

**cid**int

Connection id of the observer to be removed.

reset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/widgets.py#L376-L379)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#matplotlib.widgets.SliderBase.reset "Link to this definition")

Reset the slider to the initial value.

Examples using `matplotlib.widgets.SliderBase`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SliderBase.html#examples-using-matplotlib-widgets-sliderbase "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_range_slider_thumb.png)

[Image scaling using a RangeSlider](https://matplotlib.org/stable/gallery/widgets/range_slider.html)

Image scaling using a RangeSlider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_demo_thumb.png)

[Slider](https://matplotlib.org/stable/gallery/widgets/slider_demo.html)

Slider

![](https://matplotlib.org/stable/_images/sphx_glr_slider_snap_demo_thumb.png)

[Snap sliders to discrete values](https://matplotlib.org/stable/gallery/widgets/slider_snap_demo.html)

Snap sliders to discrete values

On this page