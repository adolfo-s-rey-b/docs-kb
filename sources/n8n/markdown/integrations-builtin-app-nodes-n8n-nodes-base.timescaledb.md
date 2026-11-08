For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md)
.

Use the TimescaleDB node to automate work in TimescaleDB, and integrate TimescaleDB with other applications. n8n has built-in support for a wide range of TimescaleDB features, including executing an SQL query, as well as inserting and updating rows in a database.

On this page, you'll find a list of operations the TimescaleDB node supports and links to more resources.

**Credentials**

Refer to [TimescaleDB credentials](https://docs.n8n.io/integrations/builtin/credentials/timescaledb)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb#operations)

-------------------------------------------------------------------------------------------------------

*   Execute an SQL query
    
*   Insert rows in database
    
*   Update rows in database
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------

[Browse TimescaleDB node documentation integration templates](https://n8n.io/integrations/timescaledb)
 or [search all templates](https://n8n.io/workflows/)

Specify a column's data type[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb#specify-a-columns-data-type)

------------------------------------------------------------------------------------------------------------------------------------------

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for the column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.

[PreviousTheHive 5](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5)
[NextTodoist](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.todoist)

Last updated 10 days ago

Was this helpful?