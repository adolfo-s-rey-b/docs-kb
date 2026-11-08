For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters.md)
.

These are the parameters available for [node base file](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
 of declarative-style nodes.

This document gives short code snippets to help understand the code structure and concepts. For a full walk-through of building a node, including real-world code examples, refer to [Build a declarative-style node](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node)
.

Refer to [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
 for parameters available to all nodes.

`methods` and `loadOptions`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters#methods-and-loadoptions)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

_Object_ | _Optional_

`methods` contains the `loadOptions` object. You can use `loadOptions` to query the service to get user-specific settings, then return them and render them in the GUI so the user can include them in subsequent queries. The object must include routing information for how to query the service, and output settings that define how to handle the returned options. For example:

Copy

    methods : {
    	loadOptions: {
    		routing: {
    			request: {
    				url: '/webhook/example-option-parameters',
    				method: 'GET',
    			},
    			output: {
    				postReceive: [\
    					{\
    						// When the returned data is nested under another property\
    						// Specify that property key\
    						type: 'rootProperty',\
    						properties: {\
    							property: 'responseData',\
    						},\
    					},\
    					{\
    						type: 'setKeyValue',\
    						properties: {\
    							name: '={{$responseItem.key}} ({{$responseItem.value}})',\
    							value: '={{$responseItem.value}}',\
    						},\
    					},\
    					{\
    						// If incoming data is an array of objects, sort alphabetically by key\
    						type: 'sort',\
    						properties: {\
    							key: 'name',\
    						},\
    					},\
    				],
    			},
    		},
    	}
    },

`routing`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters#routing)

--------------------------------------------------------------------------------------------------------------------------------

_Object_ | _Required_

`routing` is an object used within an `options` array in operations and input field objects. It contains the details of an API call.

The code example below comes from the [Declarative-style tutorial](https://docs.n8n.io/connect/create-nodes/build-your-node/tutorial-build-a-declarative-style-node)
. It sets up an integration with a NASA API. It shows how to use `requestDefaults` to set up the basic API call details, and `routing` to add information for each operation.

Copy

    description: INodeTypeDescription = {
      // Other node info here
      requestDefaults: {
    			baseURL: 'https://api.nasa.gov',
    			url: '',
    			headers: {
    				Accept: 'application/json',
    				'Content-Type': 'application/json',
    			},
    		},
        properties: [\
          // Resources here\
          {\
            displayName: 'Operation'\
            // Other operation details\
            options: [\
              {\
                name: 'Get'\
                value: 'get',\
                description: '',\
                routing: {\
                  request: {\
                    method: 'GET',\
                    url: '/planetary/apod'\
                  }\
                }\
              }\
            ]\
          }\
        ]
    }

`version`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters#version)

--------------------------------------------------------------------------------------------------------------------------------

_Number_ or _Array_ | _Optional_

If you have one version of your node, this can be a number. If you want to support more than one version, turn this into an array, containing numbers for each node version.

n8n supports two methods of node versioning, but declarative-style nodes must use the light versioning approach. Refer to [Node versioning](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning)
 for more information.

`features`[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters#features)

----------------------------------------------------------------------------------------------------------------------------------

_Object_ | _Optional_

Define named feature flags evaluated against the node version. Use features to control parameter visibility with `@feature` in `displayOptions`.

Refer to [Feature-based versioning](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/versioning#feature-based-versioning)
 for more information.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------------

*   [Base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
    
*   [Structure](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure)
    
*   [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
    
*   [Programmatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)
    
*   [Programmatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)
    

[PreviousStandard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
[NextProgrammatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)

Last updated 10 days ago

Was this helpful?