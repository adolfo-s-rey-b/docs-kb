For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)
.

**Feature availability**

The Motorhead project is no longer maintained. The Motorhead node is deprecated from n8n 2.8.0. Refer to [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
 for more information.

Use the Motorhead node to use Motorhead as a memory server.

On this page, you'll find a list of operations the Motorhead node supports, and links to more resources.

**Credentials**

Refer to the [Motorhead credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/motorhead)
 for authentication information for this node.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------------

*   **Session ID**: Enter the ID to use to store the memory in the workflow data.
    

Node reference[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead#node-reference)

--------------------------------------------------------------------------------------------------------------------------------------

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Motorhead node documentation integration templates](https://n8n.io/integrations/motorhead)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Single memory instance[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead#single-memory-instance)

------------------------------------------------------------------------------------------------------------------------------------------------------

If you add more than one Motorhead node to your workflow, all nodes access the same memory instance by default. Be careful when doing destructive actions that override existing memory contents, such as the override all messages operation in the [Chat Memory Manager](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager)
 node. If you want more than one memory instance in your workflow, set different session IDs in different memory nodes.

[PreviousCommon issues](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)
[NextMongoDB Chat Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat)

Last updated 10 days ago

Was this helpful?