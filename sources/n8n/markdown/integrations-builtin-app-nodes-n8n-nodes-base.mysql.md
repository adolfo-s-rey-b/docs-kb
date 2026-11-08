For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql.md)
.

Use the MySQL node to automate work in MySQL, and integrate MySQL with other applications. n8n has built-in support for a wide range of MySQL features, including executing an SQL query, as well as inserting, and updating rows in a database.

On this page, you'll find a list of operations the MySQL node supports and links to more resources.

**Credentials**

Refer to [MySQL credentials](https://docs.n8n.io/integrations/builtin/credentials/mysql)
 for guidance on setting up authentication.

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql#operations)

-------------------------------------------------------------------------------------------------

*   Delete
    
*   Execute SQL
    
*   Insert
    
*   Insert or Update
    
*   Select
    
*   Update
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-base.mysql integration templates](https://n8n.io/integrations/mysql)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql#related-resources)

---------------------------------------------------------------------------------------------------------------

Refer to [MySQL's Connectors and APIs documentation](https://dev.mysql.com/doc/index-connectors.html)
 for more information about the service.

Refer to MySQL's [SELECT statement documentation](https://dev.mysql.com/doc/refman/8.4/en/select.html)
 for more information on writing SQL queries.

Use query parameters[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql#use-query-parameters)

---------------------------------------------------------------------------------------------------------------------

When creating a query to run on a MySQL database, you can use the **Query Parameters** field in the **Options** section to load data into the query. n8n sanitizes data in query parameters, which prevents SQL injection.

For example, you want to find a person by their email address. Given the following input data:

Copy

    [\
        {\
            "email": "alex@example.com",\
            "name": "Alex",\
            "age": 21 \
        },\
        {\
            "email": "jamie@example.com",\
            "name": "Jamie",\
            "age": 33 \
        }\
    ]

You can write a query like:

Copy

    SELECT * FROM $1:name WHERE email = $2;

Then in **Query Parameters**, provide the field values to use. You can provide fixed values or expressions. For this example, use expressions so the node can pull the email address from each input item in turn:

Copy

    // users is an example table name
    users, {{ $json.email }} 

Common issues[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql#common-issues)

-------------------------------------------------------------------------------------------------------

For common errors or issues and suggested resolution steps, refer to [Common issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues)
.

[PreviousMSG91](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.msg91)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues)

Last updated 10 days ago

Was this helpful?