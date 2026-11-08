For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/zep.md)
.

You can use these credentials to authenticate the following nodes:

*   [Zep](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep)
    
*   [Zep Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorezep)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/zep#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/zep#related-resources)

------------------------------------------------------------------------------------------------

Refer to [Zep's Cloud SDK documentation](https://help.getzep.com/install-sdks)
 for more information about the service. Refer to [Zep's REST API documentation](https://getzep.github.io/zep/)
 for information about the API.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/zep#using-api-key)

----------------------------------------------------------------------------------------

To configure this credential, you'll need a [Zep server](https://www.getzep.com/)
 with at least one project and:

*   An **API URL**
    
*   An **API Key**
    

Setup depends on whether you're using Zep Cloud or self-hosted Zep Open Source.

### Zep Cloud setup[](https://docs.n8n.io/integrations/builtin/credentials/zep#zep-cloud-setup)

Follow these instructions if you're using [Zep Cloud](https://app.getzep.com/)
:

1.  In Zep, open the **Project Settings**.
    
2.  In the **Project Keys** section, select **Add Key**.
    
3.  Enter a **Key Name**, like `n8n integration`.
    
4.  Select **Create**.
    
5.  Copy the key and enter it in your n8n integration as the **API Key**.
    
6.  Turn on the **Cloud** toggle.
    

### Self-hosted Zep Open Source setup[](https://docs.n8n.io/integrations/builtin/credentials/zep#self-hosted-zep-open-source-setup)

**Feature availability**

The Zep team [deprecated the open source Zep Community Edition](https://blog.getzep.com/announcing-a-new-direction-for-zeps-open-source-strategy/)
 in April 2025. These instructions may not work after that date.

Follow these instructions if you're self-hosting Zep Open Source:

1.  Enter the JWT token for your Zep server as the **API Key** in n8n.
    
2.  Make sure the **Cloud** toggle is off.
    
3.  Enter the URL for your Zep server as the **API URL**.
    

[PreviousZendesk credentials](https://docs.n8n.io/integrations/builtin/credentials/zendesk)
[NextZoho credentials](https://docs.n8n.io/integrations/builtin/credentials/zoho)

Last updated 10 days ago

Was this helpful?