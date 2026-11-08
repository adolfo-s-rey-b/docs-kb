For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake.md)
.

Use the Snowflake node to automate work in Snowflake, and integrate Snowflake with other applications. n8n has built-in support for a wide range of Snowflake features, including executing SQL queries, and inserting rows in a database.

On this page, you'll find a list of operations the Snowflake node supports and links to more resources.

**Credentials**

Refer to [Snowflake credentials](https://docs.n8n.io/integrations/builtin/credentials/snowflake)
 for guidance on setting up authentication.

Operations[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake#operations)

-----------------------------------------------------------------------------------------------------

*   Execute an SQL query.
    
*   Insert rows in database.
    
*   Update rows in database.
    

### Execute an SQL query[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake#execute-an-sql-query)

When executing SQL queries on Snowflake, you can use parameterized queries to safely pass values into your SQL statements.

#### Use query parameters[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake#use-query-parameters)

Use the **Query Parameters** field in the **Options** section to bind values to your query. n8n sanitizes data in query parameters, which prevents SQL injection.

In your SQL query, use placeholders `$1`, `$2`, `$3`, and so on to indicate where parameter values should be inserted. For example:

Copy

    SELECT * FROM users WHERE email = $1 AND status = $2;

Then in **Query Parameters**, provide the values to bind. You can provide fixed values or expressions. Use expressions to pull data from input items:

Copy

    {{ $json.email }}, {{ $json.status }}

Each parameter value should be separated by a comma. The first value binds to `$1`, the second to `$2`, and so on.

**Security recommendation**

When your query includes any external or untrusted input, use query parameters instead of interpolating `{{ }}` expressions directly into the query string. This prevents SQL injection attacks by ensuring values are properly sanitized.

Templates and examples[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.snowflake#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------

[Browse Snowflake node documentation integration templates](https://n8n.io/integrations/snowflake)
 or [search all templates](https://n8n.io/workflows/)

[PreviousApprovals](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/approvals)
[NextSplunk](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.splunk)

Last updated 10 days ago

Was this helpful?