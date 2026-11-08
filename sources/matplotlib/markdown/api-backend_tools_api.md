[Skip to main content](https://matplotlib.org/stable/api/backend_tools_api.html#main-content)

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
    

`matplotlib.backend_tools`[#](https://matplotlib.org/stable/api/backend_tools_api.html#module-matplotlib.backend_tools "Link to this heading")

===============================================================================================================================================

Abstract base classes define the primitives for Tools. These tools are used by [`matplotlib.backend_managers.ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")

[`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Simple stateless tool

[`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")

Tool that has two states, only one Toggle tool can be active at any given time for the same [`matplotlib.backend_managers.ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")

class matplotlib.backend\_tools.AxisScaleBase(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L415-L429)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase "Link to this definition")

Bases: [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")

Base Tool to toggle between linear and logarithmic.

disable(_event\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L427-L429)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.disable "Link to this definition")

Disable the toggle tool.

[`trigger`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.trigger "matplotlib.backend_tools.AxisScaleBase.trigger")
 call this method when [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 is True.

This can happen in different circumstances.

*   Click on the toolbar tool button.
    
*   Call to [`matplotlib.backend_managers.ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
    .
    
*   Another [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")
     derived tool is triggered (from the same [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
    ).
    

enable(_event\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L423-L425)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.enable "Link to this definition")

Enable the toggle tool.

[`trigger`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.trigger "matplotlib.backend_tools.AxisScaleBase.trigger")
 calls this method when [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 is False.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L418-L421)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.trigger "Link to this definition")

Calls [`enable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.enable "matplotlib.backend_tools.AxisScaleBase.enable")
 or [`disable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase.disable "matplotlib.backend_tools.AxisScaleBase.disable")
 based on [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 value.

class matplotlib.backend\_tools.ConfigureSubplotsBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L622-L626)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ConfigureSubplotsBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Base tool for the configuration of subplots.

description \= 'Configure subplots'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ConfigureSubplotsBase.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/subplots'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ConfigureSubplotsBase.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

class matplotlib.backend\_tools.Cursors(_\*values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L29-L37)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "Link to this definition")

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python v3.14)")

Backend-independent cursor types.

HAND \= 2[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.HAND "Link to this definition")

MOVE \= 4[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.MOVE "Link to this definition")

POINTER \= 1[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.POINTER "Link to this definition")

RESIZE\_HORIZONTAL \= 6[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.RESIZE_HORIZONTAL "Link to this definition")

RESIZE\_VERTICAL \= 7[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.RESIZE_VERTICAL "Link to this definition")

SELECT\_REGION \= 3[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.SELECT_REGION "Link to this definition")

WAIT \= 5[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors.WAIT "Link to this definition")

class matplotlib.backend\_tools.RubberbandBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L327-L352)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.RubberbandBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Draw and remove a rubberband.

draw\_rubberband(_\*data_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L338-L344)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.RubberbandBase.draw_rubberband "Link to this definition")

Draw rubberband.

This method must get implemented per backend.

remove\_rubberband()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L346-L352)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.RubberbandBase.remove_rubberband "Link to this definition")

Remove rubberband.

This method should get implemented per backend.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L329-L336)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.RubberbandBase.trigger "Link to this definition")

Call [`draw_rubberband`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.RubberbandBase.draw_rubberband "matplotlib.backend_tools.RubberbandBase.draw_rubberband")
 or [`remove_rubberband`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.RubberbandBase.remove_rubberband "matplotlib.backend_tools.RubberbandBase.remove_rubberband")
 based on data.

class matplotlib.backend\_tools.SaveFigureBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L629-L634)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.SaveFigureBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Base tool for figure saving.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.SaveFigureBase.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Save the figure'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.SaveFigureBase.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/filesave'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.SaveFigureBase.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

class matplotlib.backend\_tools.ToolBack(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L604-L610)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBack "Link to this definition")

Bases: [`ViewsPositionsBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ViewsPositionsBase "matplotlib.backend_tools.ViewsPositionsBase")

Move back up the view limits stack.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBack.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Back to previous view'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBack.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/back'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBack.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

class matplotlib.backend\_tools.ToolBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L73-L159)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Base tool class.

A base tool, only implements [`trigger`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.trigger "matplotlib.backend_tools.ToolBase.trigger")
 method or no method at all. The tool is instantiated by [`matplotlib.backend_managers.ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
.

property canvas[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.canvas "Link to this definition")

The canvas of the figure affected by this tool, or None.

default\_keymap \= None[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.default_keymap "Link to this definition")

Keymap to associate with this tool.

`list[str]`: List of keys that will trigger this tool when a keypress event is emitted on `self.figure.canvas`. Note that this attribute is looked up on the instance, and can therefore be a property (this is used e.g. by the built-in tools to load the rcParams at instantiation time).

description \= None[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

property figure[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.figure "Link to this definition")

The Figure affected by this tool, or None.

image \= None[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

property name[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.name "Link to this definition")

The tool id (str, must be unique among tools of a tool manager).

set\_figure(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L125-L126)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.set_figure "Link to this definition")

property toolmanager[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.toolmanager "Link to this definition")

The [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 that controls this tool.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L144-L159)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolCopyToClipboardBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L926-L934)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCopyToClipboardBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Tool to copy the figure to the clipboard.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCopyToClipboardBase.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Copy the canvas figure to clipboard'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCopyToClipboardBase.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

trigger(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L932-L934)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCopyToClipboardBase.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolCursorPosition(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L299-L324)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCursorPosition "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Send message with the current pointer position.

This tool runs in the background reporting the position of the cursor.

send\_message(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L317-L324)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCursorPosition.send_message "Link to this definition")

Call [`matplotlib.backend_managers.ToolManager.message_event`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.message_event "matplotlib.backend_managers.ToolManager.message_event")
.

set\_figure(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L309-L315)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolCursorPosition.set_figure "Link to this definition")

class matplotlib.backend\_tools.ToolForward(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L613-L619)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolForward "Link to this definition")

Bases: [`ViewsPositionsBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ViewsPositionsBase "matplotlib.backend_tools.ViewsPositionsBase")

Move forward in the view lim stack.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolForward.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Forward to next view'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolForward.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/forward'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolForward.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

class matplotlib.backend\_tools.ToolFullScreen(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L405-L412)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolFullScreen "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Tool to toggle full screen.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolFullScreen.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Toggle fullscreen mode'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolFullScreen.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L411-L412)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolFullScreen.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolGrid(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L375-L387)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolGrid "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Tool to toggle the major grids of the figure.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolGrid.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Toggle major grids'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolGrid.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L381-L387)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolGrid.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolHelpBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L888-L923)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHelpBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHelpBase.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Print tool list, shortcuts and description'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHelpBase.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

static format\_shortcut(_key\_sequence_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L893-L900)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHelpBase.format_shortcut "Link to this definition")

Convert a shortcut string from the notation used in rc config to the standard notation for displaying shortcuts, e.g. 'ctrl+a' -> 'Ctrl+A'.

image \= 'mpl-data/images/help'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHelpBase.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

class matplotlib.backend\_tools.ToolHome(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L595-L601)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHome "Link to this definition")

Bases: [`ViewsPositionsBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ViewsPositionsBase "matplotlib.backend_tools.ViewsPositionsBase")

Restore the original view limits.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHome.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Reset original view'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHome.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/home'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHome.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

class matplotlib.backend\_tools.ToolMinorGrid(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L390-L402)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolMinorGrid "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Tool to toggle the major and minor grids of the figure.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolMinorGrid.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Toggle major and minor grids'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolMinorGrid.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L396-L402)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolMinorGrid.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolPan(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L822-L885)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan "Link to this definition")

Bases: [`ZoomPanBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase "matplotlib.backend_tools.ZoomPanBase")

Pan Axes with left mouse, zoom with right.

cursor \= 4[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan.cursor "Link to this definition")

Cursor to use when the tool is active.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Pan axes with left mouse, zoom with right'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/move'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

radio\_group \= 'default'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan.radio_group "Link to this definition")

Attribute to group 'radio' like tools (mutually exclusive).

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 that identifies the group or **None** if not belonging to a group.

class matplotlib.backend\_tools.ToolQuit(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L355-L362)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuit "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Tool to call the figure manager destroy method.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuit.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Quit the figure'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuit.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L361-L362)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuit.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolQuitAll(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L365-L372)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuitAll "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Tool to call the figure manager destroy method.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuitAll.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Quit all figures'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuitAll.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L371-L372)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolQuitAll.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ToolSetCursor(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L249-L296)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolSetCursor "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Change to the current cursor while inaxes.

This tool, keeps track of all [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")
 derived tools, and updates the cursor when a tool gets triggered.

set\_figure(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L268-L274)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolSetCursor.set_figure "Link to this definition")

class matplotlib.backend\_tools.ToolToggleBase(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L162-L246)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Toggleable tool.

Every time it is triggered, it switches between enable and disable.

Parameters:

**\`\`\*args\`\`**

Variable length argument to be used by the Tool.

**\`\`\*\*kwargs\`\`**

[`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 if present and True, sets the initial state of the Tool Arbitrary keyword arguments to be consumed by the Tool

cursor \= None[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.cursor "Link to this definition")

Cursor to use when the tool is active.

default\_toggled \= False[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.default_toggled "Link to this definition")

Default of toggled state.

disable(_event\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L210-L223)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.disable "Link to this definition")

Disable the toggle tool.

[`trigger`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.trigger "matplotlib.backend_tools.ToolToggleBase.trigger")
 call this method when [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 is True.

This can happen in different circumstances.

*   Click on the toolbar tool button.
    
*   Call to [`matplotlib.backend_managers.ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
    .
    
*   Another [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")
     derived tool is triggered (from the same [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
    ).
    

enable(_event\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L202-L208)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.enable "Link to this definition")

Enable the toggle tool.

[`trigger`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.trigger "matplotlib.backend_tools.ToolToggleBase.trigger")
 calls this method when [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 is False.

radio\_group \= None[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.radio_group "Link to this definition")

Attribute to group 'radio' like tools (mutually exclusive).

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 that identifies the group or **None** if not belonging to a group.

set\_figure(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L230-L246)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.set_figure "Link to this definition")

property toggled[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "Link to this definition")

State of the toggled tool.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L194-L200)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.trigger "Link to this definition")

Calls [`enable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.enable "matplotlib.backend_tools.ToolToggleBase.enable")
 or [`disable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.disable "matplotlib.backend_tools.ToolToggleBase.disable")
 based on [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 value.

class matplotlib.backend\_tools.ToolViewsPositions(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L452-L580)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Auxiliary Tool to handle changes in views and positions.

Runs in the background and should get used by all the tools that need to access the figure's history of views and positions, e.g.

*   [`ToolZoom`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom "matplotlib.backend_tools.ToolZoom")
    
*   [`ToolPan`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan "matplotlib.backend_tools.ToolPan")
    
*   [`ToolHome`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHome "matplotlib.backend_tools.ToolHome")
    
*   [`ToolBack`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBack "matplotlib.backend_tools.ToolBack")
    
*   [`ToolForward`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolForward "matplotlib.backend_tools.ToolForward")
    

add\_figure(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L472-L482)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.add_figure "Link to this definition")

Add the current figure to the stack of views and positions.

back()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L572-L575)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.back "Link to this definition")

Back one step in the stack of views and positions.

clear(_figure_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L484-L490)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.clear "Link to this definition")

Reset the Axes stack.

forward()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L577-L580)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.forward "Link to this definition")

Forward one step in the stack of views and positions.

home()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L567-L570)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.home "Link to this definition")

Recall the first view and position from the stack.

push\_current(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L523-L535)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.push_current "Link to this definition")

Push the current view limits and position onto their respective stacks.

update\_home\_views(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L555-L565)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.update_home_views "Link to this definition")

Make sure that `self.home_views` has an entry for all Axes present in the figure.

update\_view()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L492-L521)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolViewsPositions.update_view "Link to this definition")

Update the view limits and position for each Axes from the current stack position. If any Axes are present in the figure that aren't in the current stack position, use the home view limits for those Axes and don't update _any_ positions.

class matplotlib.backend\_tools.ToolXScale(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L442-L449)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolXScale "Link to this definition")

Bases: [`AxisScaleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase "matplotlib.backend_tools.AxisScaleBase")

Tool to toggle between linear and logarithmic scales on the X axis.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolXScale.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Toggle scale X axis'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolXScale.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

set\_scale(_ax_, _scale_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L448-L449)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolXScale.set_scale "Link to this definition")

class matplotlib.backend\_tools.ToolYScale(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L432-L439)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolYScale "Link to this definition")

Bases: [`AxisScaleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.AxisScaleBase "matplotlib.backend_tools.AxisScaleBase")

Tool to toggle between linear and logarithmic scales on the Y axis.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolYScale.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Toggle scale Y axis'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolYScale.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

set\_scale(_ax_, _scale_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L438-L439)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolYScale.set_scale "Link to this definition")

class matplotlib.backend\_tools.ToolZoom(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L701-L819)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom "Link to this definition")

Bases: [`ZoomPanBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase "matplotlib.backend_tools.ZoomPanBase")

A Tool for zooming using a rectangle selector.

cursor \= 3[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom.cursor "Link to this definition")

Cursor to use when the tool is active.

property default\_keymap[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom.default_keymap "Link to this definition")

The type of the None singleton.

description \= 'Zoom to rectangle'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom.description "Link to this definition")

Description of the Tool.

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
: Tooltip used if the Tool is included in a Toolbar.

image \= 'mpl-data/images/zoom\_to\_rect'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom.image "Link to this definition")

Icon filename.

`str | None`: Filename of the Toolbar icon; either absolute, or relative to the directory containing the Python source file where the `Tool.image` class attribute is defined (in the latter case, this cannot be defined as an instance attribute). In either case, the extension is optional; leaving it off lets individual backends select the icon format they prefer. If None, the _name_ is used as a label in the toolbar button.

radio\_group \= 'default'[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom.radio_group "Link to this definition")

Attribute to group 'radio' like tools (mutually exclusive).

[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 that identifies the group or **None** if not belonging to a group.

class matplotlib.backend\_tools.ViewsPositionsBase(_toolmanager_, _name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L583-L592)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ViewsPositionsBase "Link to this definition")

Bases: [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Base class for [`ToolHome`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolHome "matplotlib.backend_tools.ToolHome")
, [`ToolBack`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBack "matplotlib.backend_tools.ToolBack")
 and [`ToolForward`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolForward "matplotlib.backend_tools.ToolForward")
.

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L588-L592)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ViewsPositionsBase.trigger "Link to this definition")

Called when this tool gets used.

This method is called by [`ToolManager.trigger_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "matplotlib.backend_managers.ToolManager.trigger_tool")
.

Parameters:

**event**[`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")

The canvas event that caused this tool to be called.

**sender**object

Object that requested the tool to be triggered.

**data**object

Extra data.

class matplotlib.backend\_tools.ZoomPanBase(_\*args_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L637-L698)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase "Link to this definition")

Bases: [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")

Base class for [`ToolZoom`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolZoom "matplotlib.backend_tools.ToolZoom")
 and [`ToolPan`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolPan "matplotlib.backend_tools.ToolPan")
.

disable(_event\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L660-L666)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase.disable "Link to this definition")

Release the canvas and disconnect press/release events.

enable(_event\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L650-L658)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase.enable "Link to this definition")

Connect press/release events and lock the canvas.

scroll\_zoom(_event_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L672-L698)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase.scroll_zoom "Link to this definition")

trigger(_sender_, _event_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L668-L670)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase.trigger "Link to this definition")

Calls [`enable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase.enable "matplotlib.backend_tools.ZoomPanBase.enable")
 or [`disable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ZoomPanBase.disable "matplotlib.backend_tools.ZoomPanBase.disable")
 based on [`toggled`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.toggled "matplotlib.backend_tools.ToolToggleBase.toggled")
 value.

matplotlib.backend\_tools.add\_tools\_to\_container(_container_, _tools\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L982-L1001)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.add_tools_to_container "Link to this definition")

Add multiple tools to the container.

Parameters:

**container**Container

[`backend_bases.ToolContainerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "matplotlib.backend_bases.ToolContainerBase")
 object that will get the tools added.

**tools**list, optional

List in the form `[[group1, [tool1, tool2 ...]], [group2, [...]]]` where the tools `[tool1, tool2, ...]` will display in group1. See [`backend_bases.ToolContainerBase.add_tool`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase.add_tool "matplotlib.backend_bases.ToolContainerBase.add_tool")
 for details. If not specified, then defaults to [`default_toolbar_tools`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.default_toolbar_tools "matplotlib.backend_tools.default_toolbar_tools")
.

matplotlib.backend\_tools.add\_tools\_to\_manager(_toolmanager_, _tools\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L963-L979)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.add_tools_to_manager "Link to this definition")

Add multiple tools to a [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
.

Parameters:

**toolmanager**[`backend_managers.ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")

Manager to which the tools are added.

**tools**{str: class\_like}, optional

The tools to add in a {name: tool} dict, see [`backend_managers.ToolManager.add_tool`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.add_tool "matplotlib.backend_managers.ToolManager.add_tool")
 for more info. If not specified, then defaults to [`default_tools`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.default_tools "matplotlib.backend_tools.default_tools")
.

matplotlib.backend\_tools.cursors[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_tools.py#L29-L37)
[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.cursors "Link to this definition")

alias of [`Cursors`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.Cursors "matplotlib.backend_tools.Cursors")

matplotlib.backend\_tools.default\_toolbar\_tools \= \[\['navigation', \['home', 'back', 'forward'\]\], \['zoompan', \['pan', 'zoom', 'subplots'\]\], \['io', \['save', 'help'\]\]\][#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.default_toolbar_tools "Link to this definition")

The default tools to add to a container.

matplotlib.backend\_tools.default\_tools \= {'back': <class 'matplotlib.backend\_tools.ToolBack'>, 'copy': <class 'matplotlib.backend\_tools.ToolCopyToClipboardBase'>, 'cursor': <class 'matplotlib.backend\_tools.ToolSetCursor'>, 'forward': <class 'matplotlib.backend\_tools.ToolForward'>, 'fullscreen': <class 'matplotlib.backend\_tools.ToolFullScreen'>, 'grid': <class 'matplotlib.backend\_tools.ToolGrid'>, 'grid\_minor': <class 'matplotlib.backend\_tools.ToolMinorGrid'>, 'help': <class 'matplotlib.backend\_tools.ToolHelpBase'>, 'home': <class 'matplotlib.backend\_tools.ToolHome'>, 'pan': <class 'matplotlib.backend\_tools.ToolPan'>, 'position': <class 'matplotlib.backend\_tools.ToolCursorPosition'>, 'quit': <class 'matplotlib.backend\_tools.ToolQuit'>, 'quit\_all': <class 'matplotlib.backend\_tools.ToolQuitAll'>, 'rubberband': <class 'matplotlib.backend\_tools.RubberbandBase'>, 'save': <class 'matplotlib.backend\_tools.SaveFigureBase'>, 'subplots': <class 'matplotlib.backend\_tools.ConfigureSubplotsBase'>, 'viewpos': <class 'matplotlib.backend\_tools.ToolViewsPositions'>, 'xscale': <class 'matplotlib.backend\_tools.ToolXScale'>, 'yscale': <class 'matplotlib.backend\_tools.ToolYScale'>, 'zoom': <class 'matplotlib.backend\_tools.ToolZoom'>}[#](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.default_tools "Link to this definition")

The default tools to add to a tool manager.

On this page