For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md)
.

Use the CrateDB node to automate work in CrateDB, and integrate CrateDB with other applications. n8n has built-in support for a wide range of CrateDB features, including executing, inserting, and updating rows in the database.

On this page, you'll find a list of operations the CrateDB node supports and links to more resources.

**Credentials**

Refer to [CrateDB credentials](https://docs.n8n.io/integrations/builtin/credentials/cratedb)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb#operations)

---------------------------------------------------------------------------------------------------

*   Execute an SQL query
    
*   Insert rows in database
    
*   Update rows in database
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse CrateDB node documentation integration templates](https://n8n.io/integrations/cratedb)
 or [search all templates](https://n8n.io/workflows/)

Node reference[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb#node-reference)

-----------------------------------------------------------------------------------------------------------

### Specify a column's data type[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb#specify-a-columns-data-type)

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for the column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.

[PreviousCortex](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cortex)
[NextCustomer.io](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.customerio)

Last updated 10 days ago

Was this helpful?