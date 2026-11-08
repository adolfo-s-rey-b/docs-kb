For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md)
.

Use the LangChain Code node to import LangChain. This means if there is functionality you need that n8n hasn't created a node for, you can still use it. By configuring the LangChain Code node connectors you can use it as a normal node, root node or sub-node.

On this page, you'll find the node parameters, guidance on configuring the node, and links to more resources.

**Feature availability**

The LangChain Code node has critical security issues and isn't safe to use. It's deprecated from n8n 2.35.0 and hidden from the nodes panel. Avoid using it in your workflows.

**Not available on Cloud**

This node is only available on self-hosted n8n.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#node-parameters)

------------------------------------------------------------------------------------------------------------------------------

### Add Code[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#add-code)

Add your custom code. Choose either **Execute** or **Supply Data** mode. You can only use one mode.

Unlike the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
, the LangChain Code node doesn't support Python.

*   **Execute**: use the LangChain Code node like n8n's own Code node. This takes input data from the workflow, processes it, and returns it as the node output. This mode requires a main input and output. You must create these connections in **Inputs** and **Outputs**.
    
*   **Supply Data**: use the LangChain Code node as a sub-node, sending data to a root node. This uses an output other than main.
    

By default, you can't load built-in or external modules in this node. Self-hosted users can [enable built-in and external modules](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration)
.

### Inputs[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#inputs)

Choose the input types.

The main input is the normal connector found in all n8n workflows. If you have a main input and output set in the node, **Execute** code is required.

### Outputs[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#outputs)

Choose the output types.

The main output is the normal connector found in all n8n workflows. If you have a main input and output set in the node, **Execute** code is required.

Node inputs and outputs configuration[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#node-inputs-and-outputs-configuration)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By configuring the LangChain Code node connectors (inputs and outputs) you can use it as an app node, root node or sub-node.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-f9f03fac4e19190cc8e9361616ad666462fc0006%252Fcreate-node-types.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=561e754c98e1bc7c970d8175d963cfa4&sv=3)

Four LangChain Code nodes in one workflow, each set up as a different node type: app, root, sub-node, and sub-node with sub-nodes

Node type

Inputs

Outputs

Code mode

App node. Similar to the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
.

Main

Main

Execute

Root node

Main; at least one other type

Main

Execute

Sub-node

\-

A type other than main. Must match the input type you want to connect to.

Supply Data

Sub-node with sub-nodes

A type other than main

A type other than main. Must match the input type you want to connect to.

Supply Data

Built-in methods[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#built-in-methods)

--------------------------------------------------------------------------------------------------------------------------------

n8n provides these methods to make it easier to perform common tasks in the LangChain Code node.

Method

Description

`this.addInputData(inputName, data)`

Populate the data of a specified non-main input. Useful for mocking data.

*   `inputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`
    
*   `data` contains the data you want to add. Refer to [Data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
     for information on the data structure expected by n8n.
    

`this.addOutputData(outputName, data)`

Populate the data of a specified non-main output. Useful for mocking data.

*   `outputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`
    
*   `data` contains the data you want to add. Refer to [Data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
     for information on the data structure expected by n8n.
    

`this.getInputConnectionData(inputName, itemIndex, inputIndex?)`

Get data from a specified non-main input.

*   `inputName` is the input connection type, and must be one of: `ai_agent`, `ai_chain`, `ai_document`, `ai_embedding`, `ai_languageModel`, `ai_memory`, `ai_outputParser`, `ai_retriever`, `ai_textSplitter`, `ai_tool`, `ai_vectorRetriever`, `ai_vectorStore`
    
*   `itemIndex` should always be `0` (this parameter will be used in upcoming functionality)
    
*   Use `inputIndex` if there is more than one node connected to the specified input.
    

`this.getInputData(inputIndex?, inputName?)`

Get data from the main input.

`this.getNode()`

Get the current node.

`this.getNodeOutputs()`

Get the outputs of the current node.

`this.getExecutionCancelSignal()`

Use this to stop the execution of a function when the workflow stops. n8n handles this in most workflows, but you may need it if you build your own chains or agents.

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------------------------

[Browse LangChain Code node documentation integration templates](https://n8n.io/integrations/langchain-code)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code#related-resources)

----------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousSentiment Analysis](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis)
[NextMicrosoft Agent 365 Trigger](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger)

Last updated 10 days ago

Was this helpful?