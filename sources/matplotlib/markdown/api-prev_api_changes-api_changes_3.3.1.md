[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.1.html#main-content)

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
    

API Changes for 3.3.1[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.1.html#api-changes-for-3-3-1 "Link to this heading")

=================================================================================================================================================

Deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.1.html#deprecations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### Reverted deprecation of `num2epoch` and `epoch2num`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.1.html#reverted-deprecation-of-num2epoch-and-epoch2num "Link to this heading")

These two functions were deprecated in 3.3.0, and did not return an accurate Matplotlib datenum relative to the new Matplotlib epoch handling ([`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
 and `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`)). This version reverts the deprecation.

### Functions `epoch2num` and `dates.julian2num` use `date.epoch` rcParam[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.3.1.html#functions-epoch2num-and-dates-julian2num-use-date-epoch-rcparam "Link to this heading")

Now `epoch2num` and (undocumented) `julian2num` return floating point days since [`get_epoch`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.get_epoch "matplotlib.dates.get_epoch")
 as set by `[rcParams["date.epoch"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.epoch#rcparam-date-epoch) ` (default: `'1970-01-01T00:00:00'`), instead of floating point days since the old epoch of "0000-12-31T00:00:00". If needed, you can translate from the new to old values as `old = new + mdates.date2num(np.datetime64('0000-12-31'))`

On this page