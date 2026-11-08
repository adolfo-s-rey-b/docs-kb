For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/erpnext.md)
.

You can use these credentials to authenticate the following nodes:

*   [ERPNext](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.erpnext)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/erpnext#prerequisites)

--------------------------------------------------------------------------------------------

*   Create an [ERPNext](https://erpnext.com/)
     account.
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/erpnext#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/erpnext#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [ERPNext's documentation](https://docs.erpnext.com/docs/user/manual/en/introduction)
 for more information about the service.

Refer to [ERPNext's developer documentation](https://frappeframework.com/docs/user/en/introduction)
 for more information about working with the framework.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/erpnext#using-api-key)

--------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   An **API Key**: Generate this from your own ERPNext user account in **Settings > My Settings > API Access**.
    
*   An **API Secret**: Generated with the API key.
    
*   Your ERPNext **Environment**:
    
    *   For **Cloud-hosted**:
        
        *   Your ERPNext **Subdomain**: Refer to the [FAQs](https://docs.n8n.io/integrations/builtin/credentials/erpnext#how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account)
            
        *   Your **Domain**: Choose between `erpnext.com` and `frappe.cloud`.
            
        
    *   For **Self-hosted**:
        
        *   The fully qualified **Domain** where you host ERPNext
            
        
    
*   Choose whether to **Ignore SSL Issues**: When selected, n8n will connect even if SSL certificate validation is unavailable.
    

If you are an ERPNext System Manager, you can also generate API keys and secrets for other users. Refer to the [ERPNext Adding Users documentation](https://docs.erpnext.com/docs/user/manual/en/adding-users)
 for more information.

How to find the subdomain of an ERPNext cloud-hosted account[](https://docs.n8n.io/integrations/builtin/credentials/erpnext#how-to-find-the-subdomain-of-an-erpnext-cloud-hosted-account)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can find your ERPNext subdomain by reviewing the address bar of your browser. The string between `https://` and either `.erpnext.com` or `frappe.cloud` is your subdomain.

For example, if the URL in the address bar is `https://n8n.erpnext.com`, the subdomain is `n8n`.

[PreviousEmelia credentials](https://docs.n8n.io/integrations/builtin/credentials/emelia)
[NextEventbrite credentials](https://docs.n8n.io/integrations/builtin/credentials/eventbrite)

Last updated 10 days ago

Was this helpful?