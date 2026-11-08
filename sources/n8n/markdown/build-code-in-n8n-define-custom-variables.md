For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/define-custom-variables.md)
.

**Feature availability**

Custom variables are available on:

*   **n8n Cloud:** Pro, Enterprise
    
*   **Self-hosted:** Business, Enterprise
    

Only instance owners and admins can create variables.

Custom variables are read-only variables that you can use to store and reuse values in n8n workflows.

**Variable scope and availability**

*   **Global variables** are available to everyone on your n8n instance, across all projects.
    
*   **Project-scoped variables** are available only within the specific project they're created in.
    
*   Project-scoped variables are available from n8n 1.118.0. Previous versions only support global variables accessible from the left side menu.
    

Create variables[](https://docs.n8n.io/build/code-in-n8n/define-custom-variables#create-variables)

---------------------------------------------------------------------------------------------------

You can access the **Variables** tab from either the overview page or a specific project.

To create a new variable:

1.  On the **Variables** tab, select **Add Variable**.
    
2.  Enter a **Key** and **Value**. The maximum key length is 50 characters, and the maximum value length is 1000 characters. n8n limits the characters you can use in the key and value to lowercase and uppercase letters, numbers, and underscores (`A-Z`, `a-z`, `0-9`, `_`).
    
3.  Select the **Scope** (only available when creating from the overview page):
    
    *   **Global**: The variable is available across all projects in the n8n instance.
        
    *   **Project**: The variable is available only within a specific project (you can select which project).
        
    *   When creating from a project page, the scope is automatically set to that project.
        
    
4.  Select **Save**. The variable is now available for use in workflows according to its scope.
    

Edit and delete variables[](https://docs.n8n.io/build/code-in-n8n/define-custom-variables#edit-and-delete-variables)

---------------------------------------------------------------------------------------------------------------------

To edit or delete a variable:

1.  On the **Variables** tab, hover over the variable you want to change.
    
2.  Select **Edit** or **Delete**.
    

Use variables in workflows[](https://docs.n8n.io/build/code-in-n8n/define-custom-variables#use-variables-in-workflows)

-----------------------------------------------------------------------------------------------------------------------

You can access variables in the Code node and in expressions:

Copy

    // Access a variable
    $vars.<variable-name>

All variables are strings.

During workflow execution, n8n replaces the variables with the variable value. If the variable has no value, n8n treats its value as `undefined`. Workflows don't automatically fail in this case.

**Variable precedence**

When a project-scoped variable has the same key as a global variable, the project-scoped variable value takes precedence and overrides the global variable value within that project's workflows.

Variables are read-only. You must use the UI to change the values. If you need to set and access custom data within your workflow, use [Workflow static data](https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata)
.

Related resources[](https://docs.n8n.io/build/code-in-n8n/define-custom-variables#related-resources)

-----------------------------------------------------------------------------------------------------

*   [Code in n8n](https://docs.n8n.io/build/code-in-n8n)
    
*   [Using the Code node](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)
    
*   [Get coding help from AI](https://docs.n8n.io/build/code-in-n8n/get-coding-help-from-ai)
    
*   [Use built-in shortcuts](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts)
    
*   [Cookbook](https://docs.n8n.io/build/code-in-n8n/cookbook)
    

[Previousn8n metadata](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata)
[NextCookbook](https://docs.n8n.io/build/code-in-n8n/cookbook)

Last updated 10 days ago

Was this helpful?