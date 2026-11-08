For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/pin-and-mock-data.md)
.

When developing workflows, you might want to test your logic without repeatedly calling external systems or working with live data. n8n provides two related features to help with this:

*   **Data mocking**: Create or simulate test data without connecting to real data sources
    
*   **Data pinning**: Save test data (mocked or real) and reuse it in future workflow executions instead of fetching fresh data
    

Both approaches save time and resources during development, help you work with consistent datasets, and protect live systems from repeated test calls.

**For development only**

Data pinning and mocking are features to help test workflows during development. Data pinning isn't available for production workflow executions.

Data mocking approaches[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#data-mocking-approaches)

--------------------------------------------------------------------------------------------------------------

Create test data to work with during development. You can create mock data in several ways:

### Generate custom data using the Code or Edit Fields nodes[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#generate-custom-data-using-the-code-or-edit-fields-nodes)

You can create a custom dataset in your workflow using either the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
 or the [Edit Fields (Set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
.

In the Code node, you can create any data set you want, and return it as the node output. In the Edit Fields node, select **Add fields** to add your custom data.

The Edit Fields node is a good choice for small tests. To create more complex datasets, use the Code node.

**Use this approach when**: You need complete control over your test data structure and values, or when you want to test edge cases with specific data patterns.

### Output a sample data set from the Customer Datastore node[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#output-a-sample-data-set-from-the-customer-datastore-node)

The Customer Datastore node provides a fake dataset to work with. Add and execute the node to explore the data.

**Use this approach when**: You need some test data when exploring n8n, and you don't have a real use-case to work with.

Once you've created or obtained test data you want to reuse across multiple workflow executions, use [Data pinning](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#data-pinning)
 to save it for consistent testing.

Data pinning[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#data-pinning)

----------------------------------------------------------------------------------------

You can 'pin' data during workflow development. Data pinning means saving the output data of a node and using the saved data instead of fetching fresh data in future workflow executions.

You can use this when working with data from external sources to avoid having to repeat requests to the external system. This can save time and resources:

*   If your workflow relies on an external system to trigger it, such as a webhook call, being able to pin data means you don't need to use the external system every time you test the workflow.
    
*   If the external resource has data or usage limits, pinning data during tests avoids consuming your resource limits.
    
*   You can fetch and pin the data you want to test, then have confidence that the data is consistent in all your workflow tests.
    
*   You can mock test data (using the approaches above), then pin it for reuse across executions.
    

You can only pin data for nodes that have a single main output ("error" outputs don't count for this purpose).

### Pin data[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#pin-data)

To pin data in a node:

1.  Run the node to load data.
    
2.  In the **OUTPUT** view, select **Pin data** ![Pin data icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-1e9a0da133d9a87ac1852470172937152b8a6cc5%252Fdata-pinning-button.png%3Falt%3Dmedia&width=38&dpr=3&quality=100&sign=48fb29d21fac503641cdca4d8c2ad068&sv=3). When data pinning is active, the button is disabled and a "This data is pinned" banner is displayed in the **OUTPUT** view.
    

**Nodes that output binary data**

You can't pin data if the output data includes binary data.

### Unpin data[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#unpin-data)

When data pinning is active, a banner appears at the top of the node's output panel indicating that n8n has pinned the data. To unpin data and fetch fresh data on the next execution, select the **Unpin** link in the banner.

### Edit pinned data[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#edit-pinned-data)

n8n allows you to edit pinned data. This means you can check different scenarios without setting up each scenario and sending the relevant data from your external system. It makes it easier to test edge cases.

**For development only**

Data editing isn't available for production workflow executions. It's a feature to help test workflows during development.

#### Edit output data[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#edit-output-data)

To edit output data:

1.  Run the node to load data.
    
2.  In the **OUTPUT** view, select **JSON** to switch to JSON view.
    
3.  Select **Edit** ![Edit data icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-1fc23d50fc8c3d15511ec8ad33c7f19c15c79d05%252Fedit-data.png%3Falt%3Dmedia&width=43&dpr=3&quality=100&sign=82077052590471e1afbc9e878a61076e&sv=3).
    
4.  Edit your data.
    
5.  Select **Save**. n8n saves your data changes and pins your data.
    

#### Use data from previous executions[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#use-data-from-previous-executions)

You can copy data from nodes in previous workflow executions:

1.  Open the left menu.
    
2.  Select **Executions**.
    
3.  Browse the workflow executions list to find the one with the data you want to copy.
    
4.  Select **Open Past Execution** ![Open past execution icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-7d048c973725bf412e5d55e1ebafa42a4baa7ba6%252Fopen-execution.png%3Falt%3Dmedia&width=41&dpr=3&quality=100&sign=dfd1349b52dd613402961e2b71a90ffa&sv=3).
    
5.  Double click the node whose data you want to copy.
    
6.  If it's table layout, select **JSON** to switch to JSON view.
    
7.  There are two ways to copy the JSON:
    
8.  Select the JSON you want by highlighting it, like selecting text. Then use `ctrl` + `c` to copy it.
    
9.  Select the JSON you want to copy by clicking on a parameter. Then: 1. Hover over the JSON. n8n displays the **Copy** ![Copy data icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-0278483a67a130c22c6173f5e835e40045b5cd78%252Fcopy-data.png%3Falt%3Dmedia&width=38&dpr=3&quality=100&sign=b3b99bf5803421b2c0b50ba65b23b2f7&sv=3) button. 2. Select **Copy** ![Copy data icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-0278483a67a130c22c6173f5e835e40045b5cd78%252Fcopy-data.png%3Falt%3Dmedia&width=38&dpr=3&quality=100&sign=b3b99bf5803421b2c0b50ba65b23b2f7&sv=3). 3. You can choose what to copy:
    
    *   **Copy Item Path** and **Copy Parameter Path** give you expressions that access parts of the JSON.
        
    *   **Copy Value**: copies the entire selected JSON.
        
    
10.  Return to the workflow you're working on:
    
    1.  Open the left menu.
        
    2.  Select **Workflows**.
        
    3.  Select **Open**.
        
    4.  Select the workflow you want to open.
        
    
11.  Open the node where you want to use the copied data.
    
12.  If there is no data, run the node to load data.
    
13.  In the **OUTPUT** view, select **JSON** to switch to JSON view.
    
14.  Select **Edit** ![Edit data icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-1fc23d50fc8c3d15511ec8ad33c7f19c15c79d05%252Fedit-data.png%3Falt%3Dmedia&width=43&dpr=3&quality=100&sign=82077052590471e1afbc9e878a61076e&sv=3).
    
15.  Paste in the data from the previous execution.
    
16.  Select **Save**. n8n saves your data changes and pins your data.
    

### Combine mocking with pinning[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#combine-mocking-with-pinning)

For the most realistic testing experience, you can combine mocking and pinning approaches:

1.  Create test data using one of the mocking approaches (Code node, Edit Fields node, or Customer Datastore)
    
2.  Edit the test data to create specific test scenarios or edge cases
    
3.  Pin the edited data for reuse across multiple workflow executions
    
4.  Continue developing with this edited, pinned dataset
    

This approach gives you complete control over your test data while ensuring consistent testing across multiple runs.

Related resources[](https://docs.n8n.io/build/work-with-data/pin-and-mock-data#related-resources)

--------------------------------------------------------------------------------------------------

*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Understand n8n's data structure](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure)
    
*   [Expressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    
*   [Reference data](https://docs.n8n.io/build/work-with-data/reference-data)
    
*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    
*   [Filter out unwanted data](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data)
    
*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    
*   [Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
    

[PreviousFilter out unwanted data](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data)
[NextHandle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)

Last updated 10 days ago

Was this helpful?