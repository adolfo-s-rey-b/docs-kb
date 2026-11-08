For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md)
.

Use the Salesforce node to automate work in Salesforce, and integrate Salesforce with other applications. n8n has built-in support for a wide range of Salesforce features, including creating, updating, deleting, and getting accounts, attachments, cases, and leads, as well as uploading documents.

On this page, you'll find a list of operations the Salesforce node supports and links to more resources.

**Credentials**

Refer to [Salesforce credentials](https://docs.n8n.io/integrations/builtin/credentials/salesforce)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce#operations)

------------------------------------------------------------------------------------------------------

*   Account
    
    *   Add note to an account
        
    *   Create an account
        
    *   Create a new account, or update the current one if it already exists (upsert)
        
    *   Get an account
        
    *   Get all accounts
        
    *   Returns an overview of account's metadata.
        
    *   Delete an account
        
    *   Update an account
        
    
*   Attachment
    
    *   Create a attachment
        
    *   Delete a attachment
        
    *   Get a attachment
        
    *   Get all attachments
        
    *   Returns an overview of attachment's metadata.
        
    *   Update a attachment
        
    
*   Case
    
    *   Add a comment to a case
        
    *   Create a case
        
    *   Get a case
        
    *   Get all cases
        
    *   Returns an overview of case's metadata
        
    *   Delete a case
        
    *   Update a case
        
    
*   Contact
    
    *   Add lead to a campaign
        
    *   Add note to a contact
        
    *   Create a contact
        
    *   Create a new contact, or update the current one if it already exists (upsert)
        
    *   Delete a contact
        
    *   Get a contact
        
    *   Returns an overview of contact's metadata
        
    *   Get all contacts
        
    *   Update a contact
        
    
*   Custom Object
    
    *   Create a custom object record
        
    *   Create a new record, or update the current one if it already exists (upsert)
        
    *   Get a custom object record
        
    *   Get all custom object records
        
    *   Delete a custom object record
        
    *   Update a custom object record
        
    
*   Document
    
    *   Upload a document
        
    
*   Flow
    
    *   Get all flows
        
    *   Invoke a flow
        
    
*   Lead
    
    *   Add lead to a campaign
        
    *   Add note to a lead
        
    *   Create a lead
        
    *   Create a new lead, or update the current one if it already exists (upsert)
        
    *   Delete a lead
        
    *   Get a lead
        
    *   Get all leads
        
    *   Returns an overview of Lead's metadata
        
    *   Update a lead
        
    
*   Opportunity
    
    *   Add note to an opportunity
        
    *   Create an opportunity
        
    *   Create a new opportunity, or update the current one if it already exists (upsert)
        
    *   Delete an opportunity
        
    *   Get an opportunity
        
    *   Get all opportunities
        
    *   Returns an overview of opportunity's metadata
        
    *   Update an opportunity
        
    
*   Search
    
    *   Execute a SOQL query that returns all the results in a single response
        
    
*   Task
    
    *   Create a task
        
    *   Delete a task
        
    *   Get a task
        
    *   Get all tasks
        
    *   Returns an overview of task's metadata
        
    *   Update a task
        
    
*   User
    
    *   Get a user
        
    *   Get all users
        
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------------

[Browse Salesforce node documentation integration templates](https://n8n.io/integrations/salesforce)
 or [search all templates](https://n8n.io/workflows/)

### What to do if your operation isn't supported[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce#what-to-do-if-your-operation-isnt-supported)

If this node doesn't support the operation you want to do, you can use the [HTTP Request node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 to call the service's API.

You can use the credential you created for this service in the HTTP Request node:

1.  In the HTTP Request node, select **Authentication** > **Predefined Credential Type**.
    
2.  Select the service you want to connect to.
    
3.  Select your credential.
    

Refer to [Custom API operations](https://docs.n8n.io/integrations/builtin/custom-api-actions-for-existing-nodes)
 for more information.

Working with Salesforce custom fields[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce#working-with-salesforce-custom-fields)

------------------------------------------------------------------------------------------------------------------------------------------------------------

To add custom fields to your request:

1.  Select **Additional Fields** > **Add Field**.
    
2.  In the dropdown, select **Custom Fields**.
    

You can then find and add your custom fields.

[PreviousS3](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3)
[NextSalesmate](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesmate)

Last updated 10 days ago

Was this helpful?