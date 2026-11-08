For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md)
.

The Vector Store Question Answer node is a tool that allows an agent to summarize results and answer questions based on chunks from a vector store.

On this page, you'll find the node parameters for the Vector Store Question Answer node, and links to more resources.

**Examples and templates**

For usage examples and templates to help you get started, refer to n8n's [Vector Store Question Answer Tool integrations](https://n8n.io/integrations/vector-store-tool/)
 page.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore#node-parameters)

----------------------------------------------------------------------------------------------------------------------------------------

### Description of Data[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore#description-of-data)

Enter a description of the data in the vector store.

### Limit[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore#limit)

The maximum number of results to return.

How n8n populates the tool description[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore#how-n8n-populates-the-tool-description)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

n8n uses the node name (select the name to edit) and **Description of Data** parameter to populate the tool description for AI agents using the following format:

> Useful for when you need to answer questions about \[node name\]. Whenever you need information about \[Description of Data\], you should ALWAYS use this. Input should be a fully formed question.

Spaces in the node name are converted to underscores in the tool description.

**Avoid special characters in node names**

Using special characters in the node name will cause errors when the agent runs, for example:

Copy

    Error in sub-node 'OpenAI Chat Model'
    
    Invalid 'tools[0].function.name': string does not match pattern. Expected a string that matches the pattern '^[a-zA-Z0-9_-]+$'.

![Error message shown when a tool name contains special characters](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F139179334-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FBKcbOzIWja8NfqKDcqHc%252Fuploads%252Fgit-blob-37dcc8139d2ff55670cf27fcaf01df216af71898%252Fname-characters-error.png%3Falt%3Dmedia&width=300&dpr=3&quality=100&sign=4be0b9d6592175b983bf31c4bebe6f69&sv=3)

Use only alphanumeric characters, spaces, dashes, and underscores in node names.

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------------

View [example workflows and related content](https://n8n.io/integrations/vector-store-tool/)
 on n8n's website.

Refer to [LangChain's documentation on tools](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)
 for more information about tools in LangChain.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousThink Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink)
[NextWikipedia](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia)

Last updated 10 days ago

Was this helpful?