For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md)
.

Use the Microsoft Entra ID node to automate work in Microsoft Entra ID and integrate Microsoft Entra ID with other applications. n8n has built-in support for a wide range of Microsoft Entra ID features, which includes creating, getting, updating, and deleting users and groups, as well as adding users to and removing them from groups.

On this page, you'll find a list of operations the Microsoft Entra ID node supports, and links to more resources.

**Credentials**

Refer to the [Microsoft Entra ID credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/microsoftentra)
 for authentication information for this node.

**Government Cloud Support**

If you're using a government cloud tenant (US Government, US Government DOD, or China), make sure to select the appropriate **Microsoft Graph API Base URL** in your Microsoft Entra ID credentials configuration.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra#operations)

----------------------------------------------------------------------------------------------------------

*   **Group**
    
    *   **Create**: Create a new group
        
    *   **Delete**: Delete an existing group
        
    *   **Get**: Retrieve data for a specific group
        
    *   **Get Many**: Retrieve a list of groups
        
    *   **Update**: Update a group
        
    
*   **User**
    
    *   **Create**: Create a new user
        
    *   **Delete**: Delete an existing user
        
    *   **Get**: Retrieve data for a specific user
        
    *   **Get Many**: Retrieve a list of users
        
    *   **Update**: Update a user
        
    *   **Add to Group**: Add user to a group
        
    *   **Remove from Group**: Remove user from a group
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra#templates-and-examples)

----------------------------------------------------------------------------------------------------------------------------------

[Browse Microsoft Entra ID node documentation integration templates](https://n8n.io/integrations/microsoft-entra-id-azure-active-directory)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra#related-resources)

------------------------------------------------------------------------------------------------------------------------

Refer to [Microsoft Entra ID's documentation](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0)
 for more information about the service.

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra#common-issues)

----------------------------------------------------------------------------------------------------------------

Here are some common errors and issues with the Microsoft Entra ID node and steps to resolve or troubleshoot them.

### Updating the Allow External Senders and Auto Subscribe New Members options fails[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra#updating-the-allow-external-senders-and-auto-subscribe-new-members-options-fails)

You can't update the **Allow External Senders** and **Auto Subscribe New Members** options directly after creating a new group. You must wait after creating a group before you can change the values of these options.

When designing workflows that use multiple Microsoft Entra ID nodes to first create groups and then update these options, add a [Wait](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.wait)
 node between the two operations. A Wait node configured to pause for at least two seconds allows time for the group to fully initialize. After the wait, the update operation can complete without erroring.

[PreviousMicrosoft Dynamics CRM](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftdynamicscrm)
[NextMicrosoft Excel (OneDrive)](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel)

Last updated 10 days ago

Was this helpful?