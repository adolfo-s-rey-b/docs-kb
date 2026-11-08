For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint.md)
.

This page takes a fresh Microsoft 365 tenant to an app registration the [Microsoft SharePoint node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint)
 can sign in with, using the [Microsoft Entra Service Principal credential](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal)
. It gives you a permission manifest fragment to paste, a script to run, and the per-site grant that most setups miss.

It's written for the administrator who approves and creates the app registration. If your security team reviews permission requests, the manifest fragment and the permission table are what they need to see.

The Microsoft SharePoint node supports app-only access from version 2 of the node.

Before you start[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#before-you-start)

------------------------------------------------------------------------------------------------------------------------------------

You need:

*   The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
     installed, signed in with `az login --tenant <your-tenant-id>`.
    
*   An account that can create app registrations and grant admin consent. Admin consent needs the Global Administrator or Privileged Role Administrator role.
    
*   The address of each SharePoint site the workflows will use, for example `https://contoso.sharepoint.com/sites/mysite`.
    

Choose a permission level[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#choose-a-permission-level)

------------------------------------------------------------------------------------------------------------------------------------------------------

All three options are Microsoft Graph **Application** permissions. Delegated permissions with the same names are different permissions and don't apply to app-only access.

Permission

What the app can reach

Choose it when

`Sites.Selected`

Only the sites you grant it, with the role you give each one

Default. The app starts with access to nothing, so a security team can approve it without approving the whole tenant.

`Sites.Read.All`

Every site in the tenant, read only

Workflows read from many sites, or you need the node's site search

`Sites.ReadWrite.All`

Every site in the tenant, read and write

Workflows write to many sites, or you need the node's site search

With `Sites.Selected`, read and write isn't a manifest choice. The app registration asks for one permission, and you decide read or write per site when you [grant the app access to a site](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#grant-the-app-access-to-a-site)
.

Site search (the node's **From List** option on the **Site** field) needs a tenant-wide read permission. With `Sites.Selected`, set the **Site** field to **By URL** or **By ID** instead. Neither needs search.

The permission manifest fragment[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#the-permission-manifest-fragment)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Save this as `n8n-sharepoint-permissions.json`. It requests `Sites.Selected` from Microsoft Graph and nothing else:

n8n-sharepoint-permissions.json

Copy

    [\
    	{\
    		"resourceAppId": "00000003-0000-0000-c000-000000000000",\
    		"resourceAccess": [\
    			{\
    				"id": "883ea226-0bf2-4a8f-9f9d-92c9162a727d",\
    				"type": "Role"\
    			}\
    		]\
    	}\
    ]

For a tenant-wide permission instead, replace the one `id` value:

Application permission

`id` value

`type`

`Sites.Selected`

`883ea226-0bf2-4a8f-9f9d-92c9162a727d`

`Role`

`Sites.Read.All`

`332a536c-c7ef-4017-ab91-336970924f0d`

`Role`

`Sites.ReadWrite.All`

`9492366f-7969-46a4-8d15-ed1a20078fff`

`Role`

`resourceAppId` is Microsoft Graph. The SharePoint node calls Microsoft Graph, so a fragment that targets the older SharePoint Online API (`00000003-0000-0ff1-ce00-000000000000`) grants the app nothing the node can use. `type` is always `Role`: `Role` means an application permission, `Scope` means a delegated one.

Use the file in two ways:

*   **Azure CLI**: pass it as `--required-resource-accesses @n8n-sharepoint-permissions.json`, as the script below does.
    
*   **Microsoft Entra admin center**: open your app registration, select **Manifest**, and paste the array as the value of `requiredResourceAccess`.
    

Provision the app registration with the Azure CLI[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#provision-the-app-registration-with-the-azure-cli)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Run these commands from the folder holding `n8n-sharepoint-permissions.json`. They create the app registration and a client secret, then grant admin consent, which also creates the app's service principal:

Copy

    # Create the app registration for this tenant only, with the permission already requested
    APP_ID=$(az ad app create \
    	--display-name "n8n SharePoint" \
    	--sign-in-audience AzureADMyOrg \
    	--required-resource-accesses @n8n-sharepoint-permissions.json \
    	--query appId --output tsv)
    
    # Create a client secret valid for one year, and print it once
    az ad app credential reset \
    	--id "$APP_ID" \
    	--display-name "n8n credential" \
    	--years 1 \
    	--query password --output tsv
    
    # Grant admin consent. This also creates the app's service principal in the tenant
    az ad app permission admin-consent --id "$APP_ID"
    
    # Print the two IDs you enter in n8n
    echo "Application (client) ID: $APP_ID"
    echo "Directory (tenant) ID: $(az account show --query tenantId --output tsv)"

Copy the secret from the output of the second command. Microsoft only shows it once.

A few things to watch:

*   **On an existing app registration, add** `**--append**` **to** `**az ad app credential reset**`**.** Without it, the command removes the secrets and certificates already on the app, and any service using them stops working.
    
*   **Don't run** `**az ad sp create**` **before granting consent.** `az ad app permission admin-consent` creates the service principal itself. If one already exists, consent fails with `Request_BadRequest` and the message "The `<application-client-id>` service principal name is already present for the tenant".
    
*   **Admin consent can fail the first time you run it.** Microsoft Entra needs a few seconds to replicate the new app registration. The command reports `Directory_ObjectNotFound` with "Unable to read the company information from the directory". Wait and run it again.
    
*   **If admin consent keeps failing, grant it in the portal instead.** `az ad app permission admin-consent` calls a legacy Azure endpoint that doesn't work for every account. Open the app registration's **API permissions** page in the Microsoft Entra admin center and select **Grant admin consent for** `**<your-tenant>**`.
    

Grant the app access to a site[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#grant-the-app-access-to-a-site)

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Skip this section if you chose a tenant-wide permission. An app with only `Sites.Selected` can't reach any site until an administrator grants it access, one site at a time. This step has no page in the Microsoft Entra admin center or the SharePoint admin center, which is why setups miss it. Until you complete it, every operation fails with a 403 error.

Grant `read` for read-only workflows, or `write` for workflows that upload files or change list items.

You need the site's ID. Request it by address:

Copy

    GET https://graph.microsoft.com/v1.0/sites/contoso.sharepoint.com:/sites/mysite

### PnP PowerShell[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#pnp-powershell)

SharePoint administrators can use [PnP PowerShell](https://pnp.github.io/powershell/)
. Connect to the site, then grant the app access to it:

Copy

    Connect-PnPOnline -Url "https://contoso.sharepoint.com/sites/mysite" -Interactive -ClientId <pnp-app-client-id>
    
    Grant-PnPEntraIDAppSitePermission -AppId <application-client-id> -DisplayName "n8n SharePoint" -Permissions Write

`-Permissions` takes `Read`, `Write`, `Manage`, or `FullControl`. The node needs `Read` or `Write`.

Interactive sign-in needs its own app registration for PnP PowerShell, which `Register-PnPEntraIDAppForInteractiveLogin` creates. Pass that app's client ID as `-ClientId`.

### Microsoft Graph[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#microsoft-graph)

Send one request per site, as an administrator with the `Sites.FullControl.All` permission:

Copy

    POST https://graph.microsoft.com/v1.0/sites/<site-id>/permissions
    Content-Type: application/json
    
    {
    	"roles": ["write"],
    	"grantedToIdentities": [\
    		{\
    			"application": {\
    				"id": "<application-client-id>",\
    				"displayName": "n8n SharePoint"\
    			}\
    		}\
    	]
    }

[Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
 can send it. Open **Modify permissions** and consent to `Sites.FullControl.All` first. Refer to [Grant access per site](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal#grant-access-per-site)
 for what a 403 on this request means.

### Why the Azure CLI can't do this step[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#why-the-azure-cli-cant-do-this-step)

`az rest --method POST` against the same endpoint returns 403, even for a Global Administrator. The Azure CLI signs in as its own Microsoft-owned application, and that application doesn't hold `Sites.FullControl.All`. Consenting to the permission in your own app registration doesn't change what the Azure CLI's token carries. Use PnP PowerShell or Graph Explorer instead.

Finish the setup in n8n[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#finish-the-setup-in-n8n)

--------------------------------------------------------------------------------------------------------------------------------------------------

1.  Create a **Microsoft Entra Service Principal** credential. Enter the Directory (tenant) ID, the Application (client) ID, and the client secret the script printed. Refer to [Microsoft Entra Service Principal credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal)
     for the certificate option and for sovereign clouds.
    
2.  In the Microsoft SharePoint node, set **Authentication** to **Microsoft Entra Service Principal (App-Only)** and select the credential.
    
3.  Set the **Site** field to **By URL** and paste a site address you granted the app access to.
    
4.  Run the node.
    

From n8n 2.40.0, the credential's connection test only checks that the app can sign in. A missing permission, missing admin consent, or a missing per-site grant passes the test and fails when the node runs, with a 403 error naming the permission the operation needs.

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal-sharepoint#related-resources)

--------------------------------------------------------------------------------------------------------------------------------------

*   [Microsoft Entra Service Principal credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal)
    
*   [Microsoft SharePoint node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint)
    
*   [Microsoft credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoft)
    
*   [Overview of Sites.Selected](https://learn.microsoft.com/en-us/graph/permissions-selected-overview)
    
*   [Create a permission on a site](https://learn.microsoft.com/en-us/graph/api/site-post-permissions)
    
*   [Grant-PnPEntraIDAppSitePermission](https://pnp.github.io/powershell/cmdlets/Grant-PnPEntraIDAppSitePermission.html)
    

[PreviousMicrosoft Entra Service Principal credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoftentraserviceprincipal)
[NextMicrosoft SQL credentials](https://docs.n8n.io/integrations/builtin/credentials/microsoftsql)

Last updated 10 days ago

Was this helpful?