For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured.md)
.

Use the Structured Output Parser node to return fields based on a JSON Schema.

On this page, you'll find the node parameters for the Structured Output Parser node, and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------------

*   **Schema Type**: Define the output structure and validation. You have two options to provide the schema:
    

1.  **Generate from JSON Example**: Input an example JSON object to automatically generate the schema. The node uses the object property types and names. It ignores the actual values. n8n treats every field as mandatory when generating schemas from JSON examples.
    
2.  **Define using JSON Schema**: Manually input the JSON schema. Read the JSON Schema [guides and examples](https://json-schema.org/learn/miscellaneous-examples)
     for help creating a valid JSON schema. Please note that we don't support references (using `$ref`) in JSON schemas.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-langchain.outputparserstructured integration templates](https://n8n.io/integrations/structured-output-parser)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's structured output documentation](https://docs.langchain.com/oss/javascript/langchain/structured-output)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Common issues[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured#common-issues)

-------------------------------------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues)
.

[PreviousItem List Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparseritemlist)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues)

Last updated 10 days ago

Was this helpful?