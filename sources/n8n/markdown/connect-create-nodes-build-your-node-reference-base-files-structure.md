For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure.md)
.

The node base file follows this basic structure:

1.  Add import statements.
    
2.  Create a class for the node.
    
3.  Within the node class, create a `description` object, which defines the node.
    

A programmatic-style node also has an `execute()` method, which reads incoming data and parameters, then builds a request. The declarative style handles this using the `routing` key in the `properties` object, within `descriptions`.

Outline structure for a declarative-style node[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure#outline-structure-for-a-declarative-style-node)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This code snippet gives an outline of the node structure.

Copy

    import { INodeType, INodeTypeDescription } from 'n8n-workflow';
    
    export class ExampleNode implements INodeType {
    	description: INodeTypeDescription = {
    		// Basic node details here
    		properties: [\
    			// Resources and operations here\
    		]
    	};
    }

Refer to [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
 for information on parameters available to all node types. Refer to [Declarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)
 for the parameters available for declarative-style nodes.

Outline structure for a programmatic-style node[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure#outline-structure-for-a-programmatic-style-node)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This code snippet gives an outline of the node structure.

Copy

    import { IExecuteFunctions, INodeExecutionData, INodeType, INodeTypeDescription } from 'n8n-workflow';
    
    export class ExampleNode implements INodeType {
    	description: INodeTypeDescription = {
        // Basic node details here
        properties: [\
          // Resources and operations here\
        ]
      };
    
      async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
        // Process data and return
      }
    };

Refer to [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
 for information on parameters available to all node types. Refer to [Programmatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)
 and [Programmatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)
 for more information on working with programmatic-style nodes.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure#related-resources)

-------------------------------------------------------------------------------------------------------------------------------

*   [Base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
    
*   [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
    
*   [Declarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)
    
*   [Programmatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)
    
*   [Programmatic-style execute method](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method)
    

[PreviousBase files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
[NextStandard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)

Last updated 10 days ago

Was this helpful?