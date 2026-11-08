For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/halopsa.md)
.

You can use these credentials to authenticate the following nodes:

*   [HaloPSA](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.halopsa)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/halopsa#prerequisites)

--------------------------------------------------------------------------------------------

Create a [HaloPSA](https://halopsa.com/)
 account.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/halopsa#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/halopsa#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [HaloPSA's API documentation](https://usehalo.com/halopsa/guides/1823/)
 for more information about the service.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/halopsa#using-api-key)

--------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   To select your **Hosting Type**:
    
    *   **On Premise Solution**: Choose this option if you're hosting the Halo application on your own server
        
    *   **Hosted Solution Of Halo**: Choose this option if your application is hosted by Halo. If this option is selected, you'll need to provide your **Tenant**.
        
    
*   The **HaloPSA Authorisation Server URL**: Your Authorisation Server URL is displayed within HaloPSA in **Configuration > Integrations > Halo API** in [API Details](https://halopsa.com/guides/article/?kbid=1737)
    .
    
*   The **Resource Server** URL: Your Resource Server is displayed within HaloPSA in **Configuration > Integrations > Halo API** in [API Details](https://halopsa.com/guides/article/?kbid=1737)
    .
    
*   A **Client ID**: Obtained by registering the application in the Halo API settings. Refer to [HaloPSA's Authorisation documentation](https://usehalo.com/halopsa/guides/1823/)
     for detailed instructions. n8n recommends using these settings:
    
    *   Choose `Client Credentials` as your **Authentication Method**.
        
    *   Use the `all` permission.
        
    
*   A **Client Secret**: Obtained by registering the application in the Halo API settings.
    
*   Your **Tenant** name: If **Hosted Solution of Halo** is selected as the **Hosting Type**, you must provide your tenant name. Your tenant name is displayed within HaloPSA in **Configuration > Integrations > Halo API** in [API Details](https://halopsa.com/guides/article/?kbid=1737)
    .
    

HaloPSA uses both the application permissions and the agent's permissions to determine API access.

[PreviousGumroad credentials](https://docs.n8n.io/integrations/builtin/credentials/gumroad)
[NextHarvest credentials](https://docs.n8n.io/integrations/builtin/credentials/harvest)

Last updated 10 days ago

Was this helpful?