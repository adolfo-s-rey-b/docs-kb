For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md)
.

Use the Custom Code Tool node to write code that an agent can run.

On this page, you'll find the node parameters for the Custom Code Tool node and links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode#node-parameters)

---------------------------------------------------------------------------------------------------------------------------------

### Description[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode#description)

Give your custom code a description. This tells the agent when to use this tool. For example:

> Call this tool to get a random color. The input should be a string with comma separated names of colors to exclude.

### Language[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode#language)

You can use JavaScript or Python.

### JavaScript / Python box[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode#javascript-python-box)

Write the code here.

You can access the tool input using `query`. For example, to take the input string and lowercase it:

Copy

    let myString = query;
    return myString.toLowerCase();

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------------------

[Browse Custom Code Tool node documentation integration templates](https://n8n.io/integrations/code-tool)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's documentation on tools](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
 for more information about tools in LangChain.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousCalculator](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcalculator)
[NextDatabricks Genie One MCP server](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-mcp-registry.databricksgenie)

Last updated 10 days ago

Was this helpful?