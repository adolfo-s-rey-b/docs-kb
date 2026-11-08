For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method.md)
.

The main difference between the declarative and programmatic styles is how they handle incoming data and build API requests. The programmatic style requires an `execute()` method, which reads incoming data and parameters, then builds a request. The declarative style handles requests using the `routing` key in the `operations` object.

The `execute()` method creates and returns an instance of `INodeExecutionData`.

**Paired items**

You must include input and output item pairing information in the data you return. For more information, refer to [Paired items](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/item-linking)
.

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-execute-method#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
    
*   [Structure](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/structure)
    
*   [Standard parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/standard-parameters)
    
*   [Declarative-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/declarative-style-parameters)
    
*   [Programmatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)
    

[PreviousProgrammatic-style parameters](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files/programmatic-style-parameters)
[NextCodex files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/codex-files)

Last updated 10 days ago

Was this helpful?