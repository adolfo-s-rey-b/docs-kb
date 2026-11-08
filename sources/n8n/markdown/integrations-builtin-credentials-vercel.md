For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/vercel.md)
.

You can use these credentials to authenticate the following nodes:

*   [Chat Vercel AI Gateway](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatvercel)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/vercel#prerequisites)

-------------------------------------------------------------------------------------------

Create a [Vercel](https://vercel.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/vercel#supported-authentication-methods)

---------------------------------------------------------------------------------------------------------------------------------

*   API key
    
*   OIDC token
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/vercel#related-resources)

---------------------------------------------------------------------------------------------------

Refer to the [Vercel AI Gateway documentation](https://vercel.com/docs/ai-gateway)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/vercel#using-api-key)

-------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**
    

To generate your API Key:

1.  [Login to Vercel](https://vercel.com/login)
     or [create an account](https://vercel.com/signup)
    .
    
2.  Go to the Vercel dashboard and select the **AI Gateway** tab.
    
3.  Select **API keys** on the left side bar.
    
4.  Select **Add key** and proceed with **Create key** from the Dialog.
    
5.  Copy your key and add it as the **API Key** in n8n.
    

Using OIDC token[](https://docs.n8n.io/integrations/builtin/credentials/vercel#using-oidc-token)

-------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **OIDC token**
    

To generate your OIDC token:

1.  In local development, link your application to a Vercel project with the `vc link` command.
    
2.  Run the `vercel env pull` command to pull the environment variables from Vercel.
    
3.  Copy your token and add it as the **OIDC TOKEN** in n8n.
    

[PreviousVenafi TLS Protect Datacenter credentials](https://docs.n8n.io/integrations/builtin/credentials/venafitlsprotectdatacenter)
[NextVero credentials](https://docs.n8n.io/integrations/builtin/credentials/vero)

Last updated 10 days ago

Was this helpful?