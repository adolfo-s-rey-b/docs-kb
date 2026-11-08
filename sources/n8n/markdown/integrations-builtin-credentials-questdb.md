For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/questdb.md)
.

You can use these credentials to authenticate the following nodes:

*   [QuestDB](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb)
    

Prerequisites[](https://docs.n8n.io/integrations/builtin/credentials/questdb#prerequisites)

--------------------------------------------------------------------------------------------

Create a user account on an instance of [QuestDB](https://questdb.io/)
.

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/questdb#supported-authentication-methods)

----------------------------------------------------------------------------------------------------------------------------------

*   Database connection
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/questdb#related-resources)

----------------------------------------------------------------------------------------------------

Refer to [QuestDB's documentation](https://questdb.io/docs)
 for more information about the service.

Using database connection[](https://docs.n8n.io/integrations/builtin/credentials/questdb#using-database-connection)

--------------------------------------------------------------------------------------------------------------------

To configure this credential, you'll need:

*   The **Host**: Enter the host name or IP address for the server.
    
*   The **Database**: Enter the database name, for example `qdb`.
    
*   A **User**: Enter the username for the user account as configured in `pg.user` or `pg.readonly.user` property in `server.conf`. Default value is `admin`.
    
*   A **Password**: Enter the password for the user account as configured in `pg.password` or `pg.readonly.password` property in `server.conf`. Default value is `quest`.
    
*   **SSL**: Select whether the connection should use SSL, which sets the `sslmode` parameter. Options include:
    
    *   **Allow**
        
    *   **Disable**
        
    *   **Require**
        
    
*   The **Port**: Enter the port number to use for the connection. Default is `8812`.
    

Refer to [List of supported connection properties](https://questdb.io/docs/reference/api/postgres/#list-of-supported-connection-properties)
 for more information.

[PreviousQualys credentials](https://docs.n8n.io/integrations/builtin/credentials/qualys)
[NextQuick Base credentials](https://docs.n8n.io/integrations/builtin/credentials/quickbase)

Last updated 10 days ago

Was this helpful?