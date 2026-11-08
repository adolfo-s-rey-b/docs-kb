[Skip to main content](https://matplotlib.org/stable/api/backend_managers_api.html#main-content)

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
    

`matplotlib.backend_managers`[#](https://matplotlib.org/stable/api/backend_managers_api.html#module-matplotlib.backend_managers "Link to this heading")

========================================================================================================================================================

class matplotlib.backend\_managers.ToolEvent(_name_, _sender_, _tool_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L4-L10)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolEvent "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Event for tool manipulation (add/remove).

class matplotlib.backend\_managers.ToolManager(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L32-L387)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Manager for actions triggered by user interactions (key press, toolbar clicks, ...) on a Figure.

Attributes:

[`figure`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.figure "matplotlib.backend_managers.ToolManager.figure")
[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

Figure that holds the canvas.

**keypresslock**[`LockDraw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw "matplotlib.widgets.LockDraw")

[`LockDraw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw "matplotlib.widgets.LockDraw")
 object to know if the [`canvas`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.canvas "matplotlib.backend_managers.ToolManager.canvas")
 key\_press\_event is locked.

**messagelock**[`LockDraw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw "matplotlib.widgets.LockDraw")

[`LockDraw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LockDraw.html#matplotlib.widgets.LockDraw "matplotlib.widgets.LockDraw")
 object to know if the message is available to write.

property active\_toggle[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.active_toggle "Link to this definition")

Currently toggled tools.

add\_tool(_name_, _tool_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L215-L270)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.add_tool "Link to this definition")

Add _tool_ to [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
.

If successful, adds a new event `tool_trigger_{name}` where `{name}` is the _name_ of the tool; the event is fired every time the tool is triggered.

Parameters:

**name**str

Name of the tool, treated as the ID, has to be unique.

**tool**type

Class of the tool to be added. A subclass will be used instead if one was registered for the current canvas class.

**\*args, \*\*kwargs**

Passed to the _tool_'s constructor.

See also

[`matplotlib.backend_tools.ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

The base class for tools.

property canvas[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.canvas "Link to this definition")

Canvas managed by FigureManager.

property figure[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.figure "Link to this definition")

Figure that holds the canvas.

get\_tool(_name_, _warn\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L360-L387)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.get_tool "Link to this definition")

Return the tool object with the given name.

For convenience, this passes tool objects through.

Parameters:

**name**str or [`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")

Name of the tool, or the tool itself.

**warn**bool, default: True

Whether a warning should be emitted it no tool with the given name exists.

Returns:

[`ToolBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolBase "matplotlib.backend_tools.ToolBase")
 or None

The tool or None if no tool with the given name exists.

get\_tool\_keymap(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L154-L170)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.get_tool_keymap "Link to this definition")

Return the keymap associated with the specified tool.

Parameters:

**name**str

Name of the Tool.

Returns:

list of str

List of keys associated with the tool.

message\_event(_message_, _sender\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L140-L147)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.message_event "Link to this definition")

Emit a [`ToolManagerMessageEvent`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManagerMessageEvent "matplotlib.backend_managers.ToolManagerMessageEvent")
.

remove\_tool(_name_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L198-L213)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.remove_tool "Link to this definition")

Remove tool named _name_.

Parameters:

**name**str

Name of the tool.

set\_figure(_figure_, _update\_tools\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L78-L96)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.set_figure "Link to this definition")

Bind the given figure to the tools.

Parameters:

**figure**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

**update\_tools**bool, default: True

Force tools to update figure.

toolmanager\_connect(_s_, _func_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L98-L126)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.toolmanager_connect "Link to this definition")

Connect event with string _s_ to _func_.

Parameters:

**s**str

The name of the event. The following events are recognized:

*   'tool\_message\_event'
    
*   'tool\_removed\_event'
    
*   'tool\_added\_event'
    

For every tool added a new event is created

*   'tool\_trigger\_TOOLNAME', where TOOLNAME is the id of the tool.
    

**func**callable

Callback function for the toolmanager event with signature:

def func(event: ToolEvent) \-> Any

Returns:

cid

The callback id for the connection. This can be used in [`toolmanager_disconnect`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.toolmanager_disconnect "matplotlib.backend_managers.ToolManager.toolmanager_disconnect")
.

toolmanager\_disconnect(_cid_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L128-L138)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.toolmanager_disconnect "Link to this definition")

Disconnect callback id _cid_.

Example usage:

cid \= toolmanager.toolmanager\_connect('tool\_trigger\_zoom', onpress)
#...later
toolmanager.toolmanager\_disconnect(cid)

property tools[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.tools "Link to this definition")

A dict mapping tool name -> controlled tool.

trigger\_tool(_name_, _sender\=None_, _canvasevent\=None_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L315-L344)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.trigger_tool "Link to this definition")

Trigger a tool and emit the `tool_trigger_{name}` event.

Parameters:

**name**str

Name of the tool.

**sender**object

Object that wishes to trigger the tool.

**canvasevent**Event

Original Canvas event or None.

**data**object

Extra data to pass to the tool when triggering.

update\_keymap(_name_, _key_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L176-L196)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.update_keymap "Link to this definition")

Set the keymap to associate with the specified tool.

Parameters:

**name**str

Name of the Tool.

**key**str or list of str

Keys to associate with the tool.

class matplotlib.backend\_managers.ToolManagerMessageEvent(_name_, _sender_, _message_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L20-L29)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManagerMessageEvent "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Event carrying messages from toolmanager.

Messages usually get displayed to the user by the toolbar.

class matplotlib.backend\_managers.ToolTriggerEvent(_name_, _sender_, _tool_, _canvasevent\=None_, _data\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/backend_managers.py#L13-L17)
[#](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolTriggerEvent "Link to this definition")

Bases: [`ToolEvent`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolEvent "matplotlib.backend_managers.ToolEvent")

Event to inform that a tool has been triggered.

On this page