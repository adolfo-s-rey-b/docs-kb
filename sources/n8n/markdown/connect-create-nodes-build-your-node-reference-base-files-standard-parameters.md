For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters.md)
.

These are the standard parameters for the [node base file](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
. They're the same for all node types.

`displayName`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#displayname)

-------------------------------------------------------------------------------------------------------------------------------

_String_ | _Required_

This is the name users see in the n8n GUI.

`name`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#name)

-----------------------------------------------------------------------------------------------------------------

_String_ | _Required_

The internal name of the object. Used to reference it from other places in the node.

`icon`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#icon)

-----------------------------------------------------------------------------------------------------------------

_String_ or _Object_ | _Required_

Specifies an icon for a particular node. n8n recommends uploading your own image file.

You can provide the icon file name as a string, or as an object to handle different icons for light and dark modes. If the icon works in both light and dark modes, use a string that starts with `file:`, indicating the path to the icon file. For example:

Copy

    icon: 'file:exampleNodeIcon.svg'

To provide different icons for light and dark modes, use an object with `light` and `dark` properties. For example:

Copy

    icon: { 
      light: 'file:exampleNodeIcon.svg', 
      dark: 'file:exampleNodeIcon.dark.svg' 
    }

n8n recommends using an SVG for your node icon, but you can also use PNG. If using PNG, the icon resolution should be 60x60px. Node icons should have a square or near-square aspect ratio.

**Don't reference Font Awesome**

If you want to use a Font Awesome icon in your node, download and embed the image. Don't set `defaults.color`: it only tints Font Awesome icons, and n8n 3.0 removes it.

`group`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#group)

-------------------------------------------------------------------------------------------------------------------

_Array of strings_ | _Required_

Tells n8n how the node behaves when the workflow runs. Options are:

*   `trigger`: node waits for a trigger.
    
*   `schedule`: node waits for a timer to expire.
    
*   `input`, `output`, `transform`: these currently have no effect.
    
*   An empty array, `[]`. Use this as the default option if you don't need `trigger` or `schedule`.
    

`description`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#description)

-------------------------------------------------------------------------------------------------------------------------------

_String_ | _Required_

A short description of the node. n8n uses this in the GUI.

`defaults`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#defaults)

-------------------------------------------------------------------------------------------------------------------------

_Object_ | _Required_

Contains essential brand and name settings.

The object can include:

*   `name`: String. Used as the node name on the canvas if the `displayName` is too long.
    
*   `color`: String. Deprecated since n8n 1.52.0 and removed in n8n 3.0. It only tinted Font Awesome icons. Use a file [icon](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#icon)
     instead.
    

`forceInputNodeExecution`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#forceinputnodeexecution)

-------------------------------------------------------------------------------------------------------------------------------------------------------

_Boolean_ | _Optional_

When building a multi-input node, you can choose to force all preceding nodes on all branches to execute before the node runs. The default is `false` (requiring only one input branch to run).

`inputs`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#inputs)

---------------------------------------------------------------------------------------------------------------------

_Array of strings_ | _Required_

Names the input connectors. Controls the number of connectors the node has on the input side. If you need only one connector, use `inputs: [NodeConnectionTypes.Main]`.

`outputs`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#outputs)

-----------------------------------------------------------------------------------------------------------------------

_Array of strings_ | _Required_

Names the output connectors. Controls the number of connectors the node has on the output side. If you need only one connector, use `outputs: [NodeConnectionTypes.Main]`.

`requiredInputs`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#requiredinputs)

-------------------------------------------------------------------------------------------------------------------------------------

_Integer_ or _Array_ | _Optional_

Used for multi-input nodes. Specify inputs by number that must have data (their branches must run) before the node can execute.

`credentials`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#credentials)

-------------------------------------------------------------------------------------------------------------------------------

_Array of objects_ | _Required_

This parameter tells n8n the credential options. Each object defines an authentication type.

The object must include:

*   `name`: the credential name. Must match the `name` property in the credential file. For example, `name: 'asanaApi'` in [`Asana.node.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Asana/Asana.node.ts)
     links to `name = 'asanaApi'` in [`AsanaApi.credential.ts`](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/credentials/AsanaApi.credentials.ts)
    .
    
*   `required`: Boolean. Specify whether authentication is required to use this node.
    

`requestDefaults`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#requestdefaults)

---------------------------------------------------------------------------------------------------------------------------------------

_Object_ | _Required_

Set up the basic information for the API calls the node makes.

This object must include:

*   `baseURL`: The API base URL.
    

You can also add:

*   `headers`: an object describing the API call headers, such as content type.
    
*   `url`: string. Appended to the `baseURL`. You can usually leave this out. It's more common to provide this in the `operations`.
    

`properties`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#properties)

-----------------------------------------------------------------------------------------------------------------------------

_Array of objects_ | _Required_

This contains the resource and operations objects that define node behaviors, as well as objects to set up mandatory and optional fields that can receive user input.

### Resource objects[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#resource-objects)

A resource object includes the following parameters:

*   `displayName`: String. This should always be `Resource`.
    
*   `name`: String. This should always be `resource`.
    
*   `type`: String. Tells n8n which UI element to use, and what input type to expect. For example, `options` results in n8n adding a dropdown that allows users to choose one option. Refer to [Node UI elements](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements)
     for more information.
    
*   `noDataExpression`: Boolean. Prevents using an expression for the parameter. Must always be `true` for `resource`.
    

### Operations objects[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#operations-objects)

The operations object defines the available operations on a resource.

*   `displayName`: String. This should always be `Options`.
    
*   `name`: String. This should always be `option`.
    
*   `type`: String. Tells n8n which UI element to use, and what input type to expect. For example, `dateTime` results in n8n adding a date picker. Refer to [Node UI elements](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements)
     for more information.
    
*   `noDataExpression`: Boolean. Prevents using an expression for the parameter. Must always be `true` for `operation`.
    
*   `options`: Array of objects. Each objects describes an operation's behavior, such as its routing, the REST verb it uses, and so on. An `options` object includes:
    
    *   `name`. String.
        
    *   `value`. String.
        
    *   `action`: String. This parameter combines the resource and operation. You should always include it, as n8n will use it in future versions. For example, given a resource called `"Card"` and an operation `"Get all"`, your action is `"Get all cards"`.
        
    *   `description`: String.
        
    *   `routing`: Object containing request details.
        
    

### Additional fields objects[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#additional-fields-objects)

These objects define optional parameters. n8n displays them under **Additional Fields** in the GUI. Users can choose which parameters to set.

The objects must include:

Copy

    displayName: 'Additional Fields',
    name: 'additionalFields',
    // The UI element type
    type: ''
    placeholder: 'Add Field',
    default: {},
    displayOptions: {
      // Set which resources and operations this field is available for
      show: {
        resource: [\
          // Resource names\
        ],
        operation: [\
          // Operation names\
        ]
      },
    }

For more information about UI element types, refer to [UI elements](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements)
.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------

*   [Base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
    
*   [Structure](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure)
    
*   [Declarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)
    
*   [Programmatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)
    
*   [Programmatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)
    

[PreviousStructure](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure)
[NextDeclarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)

Last updated 10 days ago

Was this helpful?