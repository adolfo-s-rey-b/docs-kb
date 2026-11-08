For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md)
.

**Feature availability**

The Zep node is deprecated from n8n 1.108.0. Refer to [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
 for more information.

Use the Zep node to use Zep as a memory server.

On this page, you'll find a list of operations the Zep node supports, and links to more resources.

**Credentials**

Refer to the [Zep credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/zep)
 for authentication information for this node.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------

*   **Session ID**: Enter the ID to use to store the memory in the workflow data.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Zep node documentation integration templates](https://n8n.io/integrations/zep)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Single memory instance[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep#single-memory-instance)

------------------------------------------------------------------------------------------------------------------------------------------------

If you add more than one Zep node to your workflow, all nodes access the same memory instance by default. Be careful when doing destructive actions that override existing memory contents, such as the override all messages operation in the [Chat Memory Manager](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager)
 node. If you want more than one memory instance in your workflow, set different session IDs in different memory nodes.

[PreviousXata](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata)
[NextAuto-fixing Output Parser](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserautofixing)

Last updated 10 days ago

Was this helpful?