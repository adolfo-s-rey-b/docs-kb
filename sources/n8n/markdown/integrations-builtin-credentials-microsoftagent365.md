For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365.md)
.

You can use these credentials to authenticate the following nodes:

*   [Microsoft Agent 365 Trigger](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger)
    

**Preview status**

Microsoft Agent 365 is an early preview feature. You need to be part of the [Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)
 to get early access.

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365#prerequisites)

------------------------------------------------------------------------------------------------------

*   Enrollment in the [Microsoft Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/)
    
*   A [Microsoft Azure](https://azure.microsoft.com/)
     account
    
*   An Agent 365 blueprint created using the Agent 365 CLI
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365#supported-authentication-methods)

--------------------------------------------------------------------------------------------------------------------------------------------

*   OAuth2 (App Registration)
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365#related-resources)

--------------------------------------------------------------------------------------------------------------

Refer to [Microsoft Agent 365 developer documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)
 for more information about the service.

Using OAuth2[](https://docs.n8n.io/integrations/builtin/credentials/microsoftagent365#using-oauth2)

----------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   **Tenant ID**: Your Microsoft Entra tenant ID
    
*   **Client ID**: The Application (client) ID from your Azure app registration
    
*   **Client Secret**: The secret generated for your app registration
    

To set up the credential:

1.  Find your Tenant ID in [Microsoft Entra ID](https://entra.microsoft.com/#home)
     and copy it into n8n as the **Tenant ID**.
    
2.  Open the [Microsoft Application Registration Portal](https://aka.ms/appregistrations)
     and follow the [custom client app registration guide](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/custom-client-app-registration)
     for Microsoft Agent 365. Once your custom client app is created, copy the Application (client) ID into n8n as the **Client ID**.
    
3.  Follow the [credentials guide](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret)
     to generate a client secret and copy the **Secret** in the **Value** column and paste it into n8n as the **Client Secret**.
    

**Incoming request validation**

The Microsoft Agent 365 Trigger node also uses your **Client ID** to validate incoming webhook requests, so it must match the application (client) ID of your agent's app registration. Refer to [Webhook authentication](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger#webhook-authentication)
.

We recommend using [Agent 365 CLI](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/agent-365-cli)
 to create your agent blueprint and manifest.

[PreviousMicrosoft SQL credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoftsql)
[NextMilvus credentials](https://docs.n8n.io/integrations/builtin/credentials/milvus)

Last updated 10 days ago

Was this helpful?