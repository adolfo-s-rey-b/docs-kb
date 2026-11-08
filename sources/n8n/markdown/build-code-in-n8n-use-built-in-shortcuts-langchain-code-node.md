For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node.md)
.

n8n provides these methods to make it easier to perform common tasks in the [LangChain Code node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code)
.

**LangChain Code node only**

The built-in methods and variables on this page are for use in expressions in the LangChain Code node. You can't use them in other nodes.

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

Related resources[](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node#related-resources)

------------------------------------------------------------------------------------------------------------------------

*   [Use built-in shortcuts](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts)
    
*   [JMESPath](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath)
    
*   [HTTP node](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node)
    
*   [n8n metadata](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata)
    

[PreviousHTTP node](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node)
[Nextn8n metadata](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata)

Last updated 10 days ago

Was this helpful?