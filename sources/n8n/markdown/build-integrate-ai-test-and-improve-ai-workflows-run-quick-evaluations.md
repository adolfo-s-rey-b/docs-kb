For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations.md)
.

**Feature availability**

Light evaluations are available on:

*   **n8n Cloud:** All plans
    
*   **Self-hosted:** Registered Community, Business, Enterprise
    

What are light evaluations?[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#what-are-light-evaluations)

-----------------------------------------------------------------------------------------------------------------------------------------------------

When building your workflow, you often want to test it with a handful of examples to get a sense of how it performs and make improvements. At this stage of workflow development, looking over workflow outputs for each example is often enough. The benefits of setting up more [formal scoring or metrics](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality)
 don't yet justify the effort.

Light evaluation allows you to run the examples in a test dataset through your workflow one-by-one, writing the outputs back to your dataset. You can then examine those outputs next to each other, and visually compare them to the expected outputs (if you have them).

How it works[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#how-it-works)

------------------------------------------------------------------------------------------------------------------------

**Credentials for Google Sheets**

Evaluations use data tables or Google Sheets to store the test dataset. To use Google Sheets as a dataset source, configure a [Google Sheets credential](https://docs.n8n.io/integrations/builtin/credentials/google)
.

Light evaluations take place in the 'Editor' tab of your workflow, although you’ll find instructions on how to set it up in the 'Evaluations' tab.

Steps:

1.  Create a dataset
    
2.  Wire the dataset up to the workflow
    
3.  Write workflow outputs back to dataset
    
4.  Run evaluation
    

The following explanation will use a sample workflow that assigns a category and priority to incoming support tickets.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-9a3af200bc5a5df4ed433a52f90dc0ec108afb61%252Fexample-ai-workflow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7698c887a7174ef44231a67e27369f0c&sv=3)

Example AI workflow

### 1\. Create a dataset[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#id-1-create-a-dataset)

Create a data table or Google Sheet with a handful of examples for your workflow. Your dataset should contain columns for:

*   The workflow input
    
*   (Optional) The expected or correct workflow output
    
*   The actual output
    

Leave the actual output column or columns blank, since you'll be filling them during the evaluation.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-a1efdbb68a9a7e5fdca79aaee38539d9b6728a23%252Fsample-dataset.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=791d7dc52936db27df5c793a11893333&sv=3)

A [sample dataset](https://docs.google.com/spreadsheets/d/1uuPS5cHtSNZ6HNLOi75A2m8nVWZrdBZ_Ivf58osDAS8/edit?gid=294497137#gid=294497137)
 for the support ticket classification workflow.

### 2\. Wire the dataset up to your workflow[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#id-2-wire-the-dataset-up-to-your-workflow)

#### Insert an evaluation trigger to pull in your dataset[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#insert-an-evaluation-trigger-to-pull-in-your-dataset)

Each time the [evaluation trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger)
 runs, it will output a single item representing one row of your dataset.

Clicking the 'Evaluate all' button to the left of the evaluation trigger will run your workflow multiple times in sequence, once for each row in your dataset. This is a special behavior of the evaluation trigger.

While wiring the trigger up, you often only want to run it once. You can do this by either:

*   Setting the trigger's 'Max rows to process' to 1
    
*   Clicking on the 'Execute node' button on the trigger (rather than the 'Evaluate all' button)
    

#### Wire the trigger up to your workflow[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#wire-the-trigger-up-to-your-workflow)

You can now connect the evaluation trigger to the rest of your workflow and reference the data that it outputs. At a minimum, you need to use the dataset’s input column(s) later in the workflow.

If you have multiple triggers in your workflow you will need to [merge their branches together](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues#combining-multiple-triggers)
.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-f5fc41085c2d911bec0617baa039840101305ebd%252Fconnecting-evaluation-trigger.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ef0cb3014aa9e931e5fbba49fe5215b0&sv=3)

The support ticket classification workflow with the evaluation trigger added in and wired up.

### 3\. Write workflow outputs back to dataset[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#id-3-write-workflow-outputs-back-to-dataset)

To populate the output column(s) of your dataset when the evaluation runs:

*   Insert the 'Set outputs' action of the [evaluation node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation)
    
*   Wire it up to your workflow at a point after it has produced the outputs you're evaluating
    
*   In the node's parameters, map the workflow outputs into the correct dataset column
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-2ae99c409511c742d6c91f79995e683388730753%252Fconnecting-set-outputs-node.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0d46006563bd7ece30c2f80050282f2f&sv=3)

The support ticket classification workflow with the 'set outputs' node added in and wired up.

### 4\. Run evaluation[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#id-4-run-evaluation)

Click on the **Execute workflow** button to the left of the evaluation trigger. The workflow will execute multiple times, once for each row of the dataset:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-35886534efb1e6a7995f7cb08ea89a6736999238%252Fexecute-workflow-button.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7a8e1926349589e2cad17aa74bb8ba06&sv=3)

Execute workflow button

Review the outputs of each execution in the data table or Google Sheet, and examine the execution details using the workflow's 'executions' tab if you need to.

Once your dataset grows past a handful of examples, consider [metric-based evaluation](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality)
 to get a numerical view of performance. See also [tips and common issues](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues)
.

Related resources[](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations#related-resources)

----------------------------------------------------------------------------------------------------------------------------------

*   [Test and improve AI workflows](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows)
    
*   [Understand why to test](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test)
    
*   [Use metrics to measure quality](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality)
    
*   [Fix common issues](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues)
    

[PreviousUnderstand why to test](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/understand-why-to-test)
[NextUse metrics to measure quality](https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality)

Last updated 10 days ago

Was this helpful?