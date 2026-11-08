For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/baserow.md)
.

You can use these credentials to authenticate the following node:

*   [Baserow](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.baserow)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/baserow#prerequisites)

--------------------------------------------------------------------------------------------

Create a [Baserow](https://baserow.io/)
 account on any hosted Baserow instance or a self-hosted instance.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/baserow#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   Basic auth
    
*   Token
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/baserow#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [Baserow's documentation](https://baserow.io/docs/index)
 for more information about the service.

Refer to [Baserow's auto-generated API documentation](https://baserow.io/api-docs)
 for more information about the API specifically.

Using basic auth[](https://docs.n8n.io/integrations/builtin/credentials/baserow#using-basic-auth)

--------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   Your Baserow **Host**
    
*   A **Username** and **Password** to log in with
    

Follow these steps:

1.  Enter the **Host** for the Baserow instance:
    
    *   For a Baserow-hosted instance: leave as `https://api.baserow.io`.
        
    *   For a self-hosted instance: set to your self-hosted instance API URL.
        
    
2.  Enter the **Username** for the user account n8n should use.
    
3.  Enter the **Password** for that user account.
    

Refer to [Baserow's API Authentication documentation](https://baserow.io/docs/apis/rest-api#authentication)
 for information on creating user accounts.

Using a token[](https://docs.n8n.io/integrations/builtin/credentials/baserow#using-a-token)

--------------------------------------------------------------------------------------------

To configure the database token credential, you'll need:

*   Your Baserow **Host**
    
*   A **Database token** created on Baserow.io, which requires a **Username** and **Password** for login.
    

### Creating the database token[](https://docs.n8n.io/integrations/builtin/credentials/baserow#creating-the-database-token)

1.  In [Baserow](https://baserow.io/login)
    , log in with your username and password.
    
2.  Click on your workspace in the top left corner and select **My Settings**.
    
3.  In the screen that opens, click **Database tokens**.
    
4.  Click **Create token**.
    
5.  Enter a **Name** and **Workspace** for the token.
    
6.  Click **Create token** to finish.
    

To create the credential in n8n, follow these steps:

1.  Enter the **Host** for the Baserow instance:
    
    *   For a Baserow-hosted instance: leave as `https://api.baserow.io`.
        
    *   For a self-hosted instance: set to your self-hosted instance API URL.
        
    
2.  Enter the **Database Token** you created.
    

[PreviousBannerbear credentials](https://docs.n8n.io/integrations/builtin/credentials/bannerbear)
[NextBeeminder credentials](https://docs.n8n.io/integrations/builtin/credentials/beeminder)

Last updated 10 days ago

Was this helpful?