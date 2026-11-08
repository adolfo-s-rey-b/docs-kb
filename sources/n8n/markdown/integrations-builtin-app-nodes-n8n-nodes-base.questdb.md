For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb.md)
.

Use the QuestDB node to automate work in QuestDB, and integrate QuestDB with other applications. n8n supports executing an SQL query and inserting rows in a database with QuestDB.

On this page, you'll find a list of operations the QuestDB node supports and links to more resources.

**Credentials**

Refer to [QuestDB credentials](https://docs.n8n.io/integrations/builtin/credentials/questdb)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb#operations)

---------------------------------------------------------------------------------------------------

*   Executes a SQL query.
    
*   Insert rows in database.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse QuestDB node documentation integration templates](https://n8n.io/integrations/questdb)
 or [search all templates](https://n8n.io/workflows/)

Node reference[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb#node-reference)

-----------------------------------------------------------------------------------------------------------

### Specify a column's data type[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb#specify-a-columns-data-type)

To specify a column's data type, append the column name with `:type`, where `type` is the data type you want for column. For example, if you want to specify the type `int` for the column **id** and type `text` for the column **name**, you can use the following snippet in the **Columns** field: `id:int,name:text`.

[PreviousPushover](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.pushover)
[NextQuick Base](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.quickbase)

Last updated 10 days ago

Was this helpful?