For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/motorhead.md)
.

**Feature availability**

The Motorhead project is no longer maintained. The [Motorhead node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead)
 is deprecated from n8n 2.8.0, and will be removed in a future version. See [Deprecated and versioned nodes](https://docs.n8n.io/integrations/builtin/deprecated-nodes)
 for details.

You can use these credentials to authenticate the following nodes:

*   [Motorhead](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/motorhead#supported-authentication-methods)

------------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/motorhead#related-resources)

------------------------------------------------------------------------------------------------------

Refer to [Motorhead's API documentation](https://docs.getmetal.io/rest-api/introduction)
 for more information about the service.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/motorhead#using-api-key)

----------------------------------------------------------------------------------------------

To configure this credential, you'll need a [Motorhead](https://www.metal.ai/)
 account and:

*   Your **Host** URL
    
*   An **API Key**
    
*   A **Client ID**
    

To set it up, you'll generate an API key:

1.  If you're self-hosting Motorhead, update the **Host** URL to match your Motorhead URL.
    
2.  In Motorhead, go to **Settings > Organization**.
    
3.  In the **API Keys** section, select **Create**.
    
4.  Enter a **Name** for your API Key, like `n8n integration`.
    
5.  Select **Generate**.
    
6.  Copy the **apiKey** and enter it in your n8n credential.
    
7.  Return to the API key list.
    
8.  Copy the **clientID** for the key and enter it as the **Client ID** in your n8n credential.
    

Refer to [Generate an API key](https://docs.getmetal.io/guides/misc-get-keys)
 for more information.

[PreviousMoonshot credentials](https://docs.n8n.io/integrations/builtin/credentials/moonshot)
[NextMQTT credentials](https://docs.n8n.io/integrations/builtin/credentials/mqtt)

Last updated 10 days ago

Was this helpful?