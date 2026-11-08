For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/qdrant.md)
.

You can use these credentials to authenticate the following nodes:

*   [Qdrant Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/qdrant#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/qdrant#related-resources)

---------------------------------------------------------------------------------------------------

Refer to [Qdrant's documentation](https://qdrant.tech/documentation/)
 for more information.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/qdrant#using-api-key)

-------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Qdrant cluster](https://qdrant.tech/documentation/cloud/create-cluster/)
 and:

*   An **API Key**
    
*   Your **Qdrant URL**
    

To set it up:

1.  Go to the [Cloud Dashboard](https://qdrant.to/cloud)
    .
    
2.  Select **Access Management** to display available API keys (or go to the **API Keys** section of the **Cluster detail** page).
    
3.  Select **Create**.
    
4.  Select the cluster you want the key to have access to in the dropdown.
    
5.  Select **OK**.
    
6.  Copy the API Key and enter it in your n8n credential.
    
7.  Enter the URL for your Qdrant cluster in the **Qdrant URL**. Refer to [Qdrant Web UI](https://qdrant.tech/documentation/interfaces/web-ui/)
     for more information.
    

Refer to [Qdrant's authentication documentation](https://qdrant.tech/documentation/cloud/authentication/)
 for more information on creating and using API keys.

[PreviousQRadar credentials](https://docs.n8n.io/integrations/builtin/credentials/qradar)
[NextQualys credentials](https://docs.n8n.io/integrations/builtin/credentials/qualys)

Last updated 10 days ago

Was this helpful?