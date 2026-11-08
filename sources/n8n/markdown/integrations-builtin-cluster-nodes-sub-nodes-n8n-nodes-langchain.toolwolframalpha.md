For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md)
.

Use the Wolfram|Alpha tool node to connect your agents and chains to Wolfram|Alpha's computational intelligence engine.

**Credentials**

Refer to the [Wolfram|Alpha credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/wolframalpha)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Wolfram|Alpha tool node documentation integration templates](https://n8n.io/integrations/wolframoralpha)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

Refer to [Wolfram|Alpha's documentation](https://products.wolframalpha.com/api)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousWikipedia](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia)
[NextCall n8n Workflow Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow)

Last updated 10 days ago

Was this helpful?