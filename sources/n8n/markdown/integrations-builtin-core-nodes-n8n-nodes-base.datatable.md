For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable.md)
.

Use the Data Table node to create and manage internal data tables. Data tables allow you to store structured data directly inside n8n and use it across workflows.

You can use the Data Table node to:

*   Create, list, and manage data tables
    
*   Insert, update, delete, and upsert rows in data tables
    
*   Query and retrieve rows using matching conditions
    

**Working with data tables**

As well as using the Data Tables node in a workflow, you can view and manage data tables manually from the **Data Tables** tab in your project **Overview**.

For information about working with data tables in this tab, and guidance on when to use data tables and their limitations, see [Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
.

Resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable#resources)

----------------------------------------------------------------------------------------------------

The Data Table node supports the following resources:

*   **Data Table:** Create, list, update, and delete tables.
    
*   **Row:** Insert, retrieve, update, delete, and upsert rows within a table.
    

### Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable#operations)

See available operations below. For detailed information on parameters for different operation types, refer to the [Table operations](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables)
 and [Row operations](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows)
 pages.

*   **Rows**
    
    *   [**Delete:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#delete-row)
         Delete one or more rows.
        
    *   [**Get:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#get-row)
         Get one or more rows from your table based on defined filters.
        
    *   [**If Row Exists:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#if-row-exists)
         Specify a set of conditions to match input items that exist in the data table.
        
    *   [**If Row Does Not Exist:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#if-row-does-not-exist)
         Specify a set of conditions to match input items that don't exist in the data table.
        
    *   [**Insert:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#insert-row)
         Insert rows into an existing table.
        
    *   [**Update:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#update-row)
         Update one or more rows.
        
    *   [**Upsert:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows#upsert-row)
         Upsert one or more rows. If the row exists, it's updated; otherwise, a new row is created.
        
    
*   **Tables**
    
    *   [**Create:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables#create-a-data-table)
         Create a new data table.
        
    *   [**Delete:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables#delete-a-data-table)
         Delete an existing data table.
        
    *   [**List:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables#list-data-tables)
         List existing data tables.
        
    *   [**Update:**](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/tables#update-a-data-table)
         Update an existing data table.
        
    

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable#related-resources)

--------------------------------------------------------------------------------------------------------------------

[Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
 explains how to create and manage data tables.

[PreviousCrypto](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto)
[NextRow operations](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows)

Last updated 10 days ago

Was this helpful?