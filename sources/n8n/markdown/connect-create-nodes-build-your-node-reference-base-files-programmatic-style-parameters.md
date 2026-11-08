For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters.md)
.

These are the parameters available for [node base file](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
 of programmatic-style nodes.

This document gives short code snippets to help understand the code structure and concepts. For a full walk-through of building a node, including real-world code examples, refer to [Build a programmatic-style node](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-programmatic-style-node)
.

Programmatic-style nodes also use the `execute()` method. Refer to [Programmatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)
 for more information.

Refer to [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
 for parameters available to all nodes.

`defaultVersion`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters#defaultversion)

-----------------------------------------------------------------------------------------------------------------------------------------------

_Number_ | _Optional_

Use `defaultVersion` when using the full versioning approach.

n8n support two methods of node versioning. Refer to [Node versioning](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning)
 for more information.

`methods` and `loadOptions`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters#methods-and-loadoptions)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

_Object_ | _Optional_

Contains the `loadOptions` method for programmatic-style nodes. You can use this method to query the service to get user-specific settings (such as getting a user's email labels from Gmail), then return them and render them in the GUI so the user can include them in subsequent queries.

For example, n8n's [Gmail node](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Google/Gmail/Gmail.node.ts)
 uses `loadOptions` to get all email labels:

Copy

    	methods = {
    		loadOptions: {
    			// Get all the labels and display them
    			async getLabels(
    				this: ILoadOptionsFunctions,
    			): Promise<INodePropertyOptions[]> {
    				const returnData: INodePropertyOptions[] = [];
    				const labels = await googleApiRequestAllItems.call(
    					this,
    					'labels',
    					'GET',
    					'/gmail/v1/users/me/labels',
    				);
    				for (const label of labels) {
    					const labelName = label.name;
    					const labelId = label.id;
    					returnData.push({
    						name: labelName,
    						value: labelId,
    					});
    				}
    				return returnData;
    			},
    		},
    	};

`version`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters#version)

---------------------------------------------------------------------------------------------------------------------------------

_Number_ or _Array_ | _Optional_

Use `version` when using the light versioning approach.

If you have one version of your node, this can be a number. If you want to support multiple versions, turn this into an array, containing numbers for each node version.

n8n support two methods of node versioning. Programmatic-style nodes can use either. Refer to [Node versioning](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning)
 for more information.

`features`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters#features)

-----------------------------------------------------------------------------------------------------------------------------------

_Object_ | _Optional_

Define named feature flags evaluated against the node version. Use features to control parameter visibility with `@feature` in `displayOptions`, or check them in code with `this.isNodeFeatureEnabled()`.

Refer to [Feature-based versioning](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning#feature-based-versioning)
 for more information.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------------

*   [Base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
    
*   [Structure](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure)
    
*   [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
    
*   [Declarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)
    
*   [Programmatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)
    

[PreviousDeclarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)
[NextProgrammatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)

Last updated 10 days ago

Was this helpful?