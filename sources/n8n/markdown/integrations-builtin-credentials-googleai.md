For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/googleai.md)
.

On n8n Cloud, you can skip setting up Google Gemini credentials by selecting **Use Gateway credits** in the credential field of nodes that support it. Refer to [Gateway credits](https://docs.n8n.io/deploy/use-n8n-cloud/gateway-credits)
 for details.

You can use these credentials to authenticate the following nodes:

*   [Embeddings Google Gemini](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini)
    
*   [Google Gemini](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini)
    
*   [Google Gemini Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini)
    
*   [Embeddings Google PaLM](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/googleai#prerequisites)

---------------------------------------------------------------------------------------------

*   Create a [Google Cloud](https://cloud.google.com/)
     account.
    
*   Create a [Google Cloud Platform project](https://developers.google.com/workspace/marketplace/create-gcp-project)
    .
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/googleai#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   Gemini(PaLM) API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/googleai#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [Google's Gemini API documentation](https://ai.google.dev/gemini-api/docs)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using Gemini(PaLM) API key[](https://docs.n8n.io/integrations/builtin/credentials/googleai#using-geminipalm-api-key)

---------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   The API **Host** URL: Both PaLM and Gemini use the default `https://generativelanguage.googleapis.com`.
    
*   An **API Key**: Create a key in [Google AI Studio](https://aistudio.google.com/apikey)
    .
    

**Custom hosts not supported**

The related nodes don't yet support custom hosts or proxies for the API host and must use `https://generativelanguage.googleapis.com`.

To create an API key:

1.  Go to the API Key page in Google AI Studio: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
    .
    
2.  Select **Create API Key**.
    
3.  You can choose whether to **Create API key in new project** or search for an existing Google Cloud project to **Create API key in existing project**.
    
4.  Copy the generated API key and add it to your n8n credential.
    

[PreviousGoogle Service Account](https://docs.n8n.io/integrations/builtin/credentials/google/service-account)
[NextGoogle Vertex AI credentials](https://docs.n8n.io/integrations/builtin/credentials/googlevertexai)

Last updated 10 days ago

Was this helpful?