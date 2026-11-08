[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#main-content)

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
    

mpl\_toolkits.axisartist.angle\_helper[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#module-mpl_toolkits.axisartist.angle_helper "Link to this heading")

==================================================================================================================================================================================================

Classes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#classes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ExtremeFinderCycle`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle.html#mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle "mpl_toolkits.axisartist.angle_helper.ExtremeFinderCycle")<br>(nx, ny\[, lon\_cycle, ...\]) | This subclass handles the case where one or both coordinates should be taken modulo 360, or be restricted to not exceed a specific range. |
| [`FormatterDMS`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.FormatterDMS.html#mpl_toolkits.axisartist.angle_helper.FormatterDMS "mpl_toolkits.axisartist.angle_helper.FormatterDMS")<br>() |     |
| [`FormatterHMS`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.FormatterHMS.html#mpl_toolkits.axisartist.angle_helper.FormatterHMS "mpl_toolkits.axisartist.angle_helper.FormatterHMS")<br>() |     |
| [`LocatorBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorBase.html#mpl_toolkits.axisartist.angle_helper.LocatorBase "mpl_toolkits.axisartist.angle_helper.LocatorBase")<br>(nbins\[, include\_last\]) |     |
| [`LocatorD`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorD.html#mpl_toolkits.axisartist.angle_helper.LocatorD "mpl_toolkits.axisartist.angle_helper.LocatorD")<br>(nbins\[, include\_last\]) |     |
| [`LocatorDM`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorDM.html#mpl_toolkits.axisartist.angle_helper.LocatorDM "mpl_toolkits.axisartist.angle_helper.LocatorDM")<br>(nbins\[, include\_last\]) |     |
| [`LocatorDMS`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorDMS.html#mpl_toolkits.axisartist.angle_helper.LocatorDMS "mpl_toolkits.axisartist.angle_helper.LocatorDMS")<br>(nbins\[, include\_last\]) |     |
| [`LocatorH`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorH.html#mpl_toolkits.axisartist.angle_helper.LocatorH "mpl_toolkits.axisartist.angle_helper.LocatorH")<br>(nbins\[, include\_last\]) |     |
| [`LocatorHM`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorHM.html#mpl_toolkits.axisartist.angle_helper.LocatorHM "mpl_toolkits.axisartist.angle_helper.LocatorHM")<br>(nbins\[, include\_last\]) |     |
| [`LocatorHMS`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.LocatorHMS.html#mpl_toolkits.axisartist.angle_helper.LocatorHMS "mpl_toolkits.axisartist.angle_helper.LocatorHMS")<br>(nbins\[, include\_last\]) |     |

Functions[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.html#functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`select_step`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.select_step.html#mpl_toolkits.axisartist.angle_helper.select_step "mpl_toolkits.axisartist.angle_helper.select_step")<br>(v1, v2, nv\[, hour, ...\]) |     |
| [`select_step24`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.select_step24.html#mpl_toolkits.axisartist.angle_helper.select_step24 "mpl_toolkits.axisartist.angle_helper.select_step24")<br>(v1, v2, nv\[, include\_last, ...\]) |     |
| [`select_step360`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.select_step360.html#mpl_toolkits.axisartist.angle_helper.select_step360 "mpl_toolkits.axisartist.angle_helper.select_step360")<br>(v1, v2, nv\[, include\_last, ...\]) |     |
| [`select_step_degree`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.select_step_degree.html#mpl_toolkits.axisartist.angle_helper.select_step_degree "mpl_toolkits.axisartist.angle_helper.select_step_degree")<br>(dv) |     |
| [`select_step_hour`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.select_step_hour.html#mpl_toolkits.axisartist.angle_helper.select_step_hour "mpl_toolkits.axisartist.angle_helper.select_step_hour")<br>(dv) |     |
| [`select_step_sub`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.angle_helper.select_step_sub.html#mpl_toolkits.axisartist.angle_helper.select_step_sub "mpl_toolkits.axisartist.angle_helper.select_step_sub")<br>(dv) |     |

On this page