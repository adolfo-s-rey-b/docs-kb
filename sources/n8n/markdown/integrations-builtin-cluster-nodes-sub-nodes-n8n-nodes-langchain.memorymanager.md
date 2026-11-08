For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md)
.

The Chat Memory Manager node manages chat message memories within your workflows. Use this node to load, insert, and delete chat messages in an in-memory vector store.

This node is useful when you:

*   Can't add a memory node directly.
    
*   Need to do more complex memory management, beyond what the memory nodes offer. For example, you can add this node to check the memory size of the Agent node's response, and reduce it if needed.
    
*   Want to inject messages to the AI that look like user messages, to give the AI more context.
    

On this page, you'll find a list of operations that the Chat Memory Manager node supports, along with links to more resources.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager#node-parameters)

--------------------------------------------------------------------------------------------------------------------------------------

*   **Operation Mode**: Choose between **Get Many Messages**, **Insert Messages**, and **Delete Messages** operations.
    
*   **Insert Mode**: Available in **Insert Messages** mode. Choose from:
    
    *   **Insert Messages**: Insert messages alongside existing messages.
        
    *   **Override All Messages**: Replace current memory.
        
    
*   **Delete Mode**: available in **Delete Messages** mode. Choose from:
    
    *   **Last N**: Delete the last N messages.
        
    *   **All Messages**: Delete messages from memory.
        
    
*   **Chat Messages**: available in **Insert Messages** mode. Define the chat messages to insert into the memory, including:
    
    *   **Type Name or ID**: Set the message type. Select one of:
        
        *   **AI**: Use this for messages from the AI.
            
        *   **System**: Add a message containing instructions for the AI.
            
        *   **User**: Use this for messages from the user. This message type is sometimes called the 'human' message in other AI tools and guides.
            
        
    *   **Message**: Enter the message contents.
        
    *   **Hide Message in Chat**: Select whether n8n should display the message to the user in the chat UI (turned off) or not (turned on).
        
    
*   **Messages Count**: Available in **Delete Messages** mode when you select **Last N**. Enter the number of latest messages to delete.
    
*   **Simplify Output**: Available in **Get Many Messages** mode. Turn on to simplify the output to include only the sender (AI, user, or system) and the text.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Chat Memory Manager node documentation integration templates](https://n8n.io/integrations/chat-memory-manager)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Memory documentation](https://langchain-ai.github.io/langgraphjs/concepts/memory/)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousHugging Face Inference Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference)
[NextSimple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)

Last updated 10 days ago

Was this helpful?