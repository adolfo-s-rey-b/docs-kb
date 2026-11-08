For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md)
.

Use the Google Vertex AI Chat Model node to use Google's Vertex AI chat models with conversational agents.

On this page, you'll find the node parameters for the Google Vertex AI Chat Model node, and links to more resources.

**Credentials**

Use [Google Vertex AI credentials](https://docs.n8n.io/integrations/builtin/credentials/googlevertexai)
 to store the project and region with your service account details. This node also supports [Google Service Account credentials](https://docs.n8n.io/integrations/builtin/credentials/google/service-account)
.

**Parameter resolution in sub-nodes**

Sub-nodes behave differently to other nodes when processing multiple items using an expression.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five `name` values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five `name` values, the expression `{{ $json.name }}` always resolves to the first name.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex#node-parameters)

-------------------------------------------------------------------------------------------------------------------------------------------

*   **Authentication**: Select **Google Service Account** (the default) or **Google Vertex AI**.
    
*   **Project ID**: For **Google Service Account** authentication, n8n loads the project list using the service account's access. Select a listed project, or enter the project ID manually. For **Google Vertex AI** authentication, configure the project in the credential.
    
*   **Model Name**: Enter the name of the model to use for completions, for example `gemini-2.5-flash`. Refer to [Google models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
     for a list of available models.
    
*   **Region**: Select **Default (Use Credential Region)** to use the region set in the credential. To override it, select **Global**, **EU (Multi-Region)**, or **US (Multi-Region)**.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex#node-options)

-------------------------------------------------------------------------------------------------------------------------------------

*   **Maximum Number of Tokens**: Enter the maximum number of tokens used, which sets the completion length.
    
*   **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
    
*   **Thinking Budget**: Controls reasoning tokens for thinking models. Set to `0` to disable automatic thinking. Set to `-1` for dynamic thinking. Leave empty for auto mode.
    
*   **Top K**: Enter the number of token choices the model uses to generate the next token.
    
*   **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.
    
*   **Safety Settings**: Gemini supports adjustable safety settings. Refer to Google's [Gemini API safety settings](https://ai.google.dev/docs/safety_setting_gemini)
     for information on the available filters and levels.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[Browse Google Vertex Chat Model node documentation integration templates](https://n8n.io/integrations/google-vertex-chat-model)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------------

Refer to [LangChain's Google Vertex AI documentation](https://docs.langchain.com/oss/javascript/integrations/chat/google_vertex_ai)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousGoogle Gemini Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini)
[NextGroq Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq)

Last updated 10 days ago

Was this helpful?