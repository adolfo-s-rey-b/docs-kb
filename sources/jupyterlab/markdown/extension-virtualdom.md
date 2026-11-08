[Skip to main content](https://jupyterlab.readthedocs.io/en/stable/extension/virtualdom.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [![jupyter.org](https://jupyterlab.readthedocs.io/en/stable/_static/jupyter_logo.svg)](https://jupyter.org/)
    
*   [GitHub](https://github.com/jupyterlab/jupyterlab)
    
*   [Discourse](https://discourse.jupyter.org/c/jupyterlab/17)
    
*   [Zulip](https://jupyter.zulipchat.com/#narrow/channel/469762-jupyterlab)
    

React[#](https://jupyterlab.readthedocs.io/en/stable/extension/virtualdom.html#react "Link to this heading")

=============================================================================================================

Many JupyterLab APIs require `Lumino` [Widgets](https://lumino.readthedocs.io/en/latest/api/modules/widgets.Widget.html)
 which have some additional features over native DOM elements, including:

*   Resize events that propagate down the Widget hierarchy.
    
*   Lifecycle events (`onBeforeDetach`, `onAfterAttach`, etc.).
    
*   Both CSS-based and absolutely positioned layouts.
    

We support wrapping React components to turn them into Lumino widgets using the [`ReactWidget`](https://jupyterlab.readthedocs.io/en/stable/api/classes/apputils.ReactWidget.html)
 class from `@jupyterlab/ui-components`:

/\*
 \* Copyright (c) Jupyter Development Team.
 \* Distributed under the terms of the Modified BSD License.
 \*/

import \* as React from 'react';

import { Widget } from '@lumino/widgets';
import { ReactWidget } from '@jupyterlab/ui-components';

function MyComponent() {
  return <div\>My Widget</div\>;
}

const myWidget: Widget \= ReactWidget.create(<MyComponent />);
Widget.attach(myWidget, document.body);

Copy to clipboard

Here we use the `create` static method to transform a React element into a Lumino widget. Whenever the widget is mounted, the React element will be rendered on the page.

If you need to handle other life cycle events on the Lumino widget or add other methods to it, you can subclass `ReactWidget` and override the `render` method to return a React element:

/\*
 \* Copyright (c) Jupyter Development Team.
 \* Distributed under the terms of the Modified BSD License.
 \*/

import \* as React from 'react';

import { Widget } from '@lumino/widgets';
import { ReactWidget } from '@jupyterlab/ui-components';

function MyComponent() {
  return <div\>My Widget</div\>;
}
class MyWidget extends ReactWidget {
  render() {
    return <MyComponent />;
  }
}
const myWidget: Widget \= new MyWidget();
Widget.attach(myWidget, document.body);

Copy to clipboard

We use Lumino [Signals](https://lumino.readthedocs.io/en/latest/api/interfaces/signaling.ISignal.html)
 to represent data that changes over time in JupyterLab. To have your React element change in response to a signal event, use the `UseSignal` component from `@jupyterlab/ui-components`, which implements the [“render props”](https://reactjs.org/docs/render-props.html)
:

/\*
 \* Copyright (c) Jupyter Development Team.
 \* Distributed under the terms of the Modified BSD License.
 \*/

import \* as React from 'react';

import { ReactWidget, UseSignal } from '@jupyterlab/ui-components';

import type { ISignal } from '@lumino/signaling';
import { Signal } from '@lumino/signaling';

import { Widget } from '@lumino/widgets';

function MyComponent() {
  return <div\>My Widget</div\>;
}

function UseSignalComponent(props: { signal: ISignal<MyWidget, void\> }) {
  return <UseSignal signal\={props.signal}\>{() \=> <MyComponent />}</UseSignal\>;
}

class MyWidget extends ReactWidget {
  render() {
    return <UseSignalComponent signal\={this.\_signal} />;
  }

  private \_signal \= new Signal<this, void\>(this);
}

const myWidget: Widget \= new MyWidget();
Widget.attach(myWidget, document.body);

Copy to clipboard

The [running component](https://github.com/jupyterlab/jupyterlab/blob/f2e0cde0e7c960dc82fd9b010fcd3dbd9e9b43d0/packages/running/src/index.tsx#L157-L159)
 and the `createSearchOverlay` function in the [search overlay](https://github.com/jupyterlab/jupyterlab/blob/f2e0cde0e7c960dc82fd9b010fcd3dbd9e9b43d0/packages/documentsearch/src/searchoverlay.tsx#L440-L457)
 use both of these features and serve as a good reference for best practices.

There is also a [simple example](https://github.com/jupyterlab/extension-examples/tree/71486d7b891175fb3883a8b136b8edd2cd560385/react/react-widget)
 making a Lumino react widget in the JupyterLab [extension examples repository](https://github.com/jupyterlab/extension-examples)
.

We currently do not have a way of embedding Lumino widgets inside of React components. If you find yourself trying to do this, we would recommend either converting the Lumino widget to a React component or using a Lumino widget for the outer layer component.

We follow the [React documentation](https://reactjs.org/docs/thinking-in-react.html)
 and [“React & Redux in TypeScript - Static Typing Guide”](https://github.com/piotrwitek/react-redux-typescript-guide#readme)
 for best practices on using React in TypeScript.

[Edit on GitHub](https://github.com/jupyterlab/jupyterlab/edit/4.6.x/docs/source/extension/virtualdom.md)

[Show Source](https://jupyterlab.readthedocs.io/en/stable/_sources/extension/virtualdom.md.txt)