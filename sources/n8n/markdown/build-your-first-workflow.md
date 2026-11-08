For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build-your-first-workflow.md)
.

In this quick start, you’ll build a workflow that fetches the weather for Berlin every morning and turns it into a short report anyone can read at a glance. The workflow saves each report to a data table, so you build up a weather log over time.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-a4ded6e98c65464468ab6d5de15287ad4ba5daab%252Fbuild-your-first-workflow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=93750980b96879b4ac3362dea65734c5&sv=3)

8 AM schedule trigger connected to Get Berlin weather, Add weather report, and Save weather log

When it runs, your workflow produces a report like this:

Copy

    The temperature in Berlin is 6.8 degrees C and it's currently cloudy.

You’ll build it with n8n Assistant, which turns a prompt into a working workflow. That takes less than five minutes. If you’d rather build it node by node, an optional section at the end walks you through the same workflow by hand.

You can also follow along with this video:

Apart from n8n, you don’t need any coding experience. The weather data comes from Mockingbird, a sample-data service n8n provides for tutorials, so you’ll get similar results to this guide.

Before you start[](https://docs.n8n.io/build-your-first-workflow#before-you-start)

-----------------------------------------------------------------------------------

You need an n8n instance. Either:

*   **n8n Cloud**: [sign up for a free trial](https://go.n8n.io/ekXKXJ)
    , or
    
*   **Self-hosted**: follow the [host n8n](https://docs.n8n.io/deploy/host-n8n)
     guide, then [set up n8n Assistant](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-n8n-assistant)
     with your own AI provider account
    

Build the workflow with n8n Assistant[](https://docs.n8n.io/build-your-first-workflow#build-the-workflow-with-n8n-assistant)

-----------------------------------------------------------------------------------------------------------------------------

**Feature availability**

n8n Assistant is available on:

*   **n8n Cloud:** Starter, Pro
    
*   **Self-hosted:** Community, Registered Community, Business
    

On n8n Cloud Enterprise and self-hosted Enterprise, contact your Customer Success Manager about preview access.

Your results may differ from the screenshots in this guide.

n8n Assistant builds workflows from prompts. You describe what you want, approve each step, and end up with a workflow you can open, edit, and publish.

1.  Log in to your n8n instance and select **New chat** in the left menu to talk to the n8n Assistant.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-e93e6e4805142aca5ebd44f1f296f8678bbca267%252Fbuild-your-first-workflow-assistant-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3a917d2afdfdeab7538af4ad3b1f81e6&sv=3)
    
    New chat selected in the left menu, with the n8n Assistant chat box open
    
2.  Enter this prompt, or dictate it, and select the send arrow:
    
    Copy
    
        Build a workflow called Weather Log that runs every day at 8 AM:
        - Get the weather for Berlin from https://mockingbird.n8n.io/v1/weather/berlin
        - Add a report field that contains the city, temperature, and conditions e.g. The temperature in Berlin is 10°C. It's currently overcast.
        - Save the report to a new data table
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-992ad780653bb1319d5f2664a9c2514d22140ee0%252Fbuild-your-first-workflow-assistant-02.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=98d54b58ab24dec9e975b754296dff83&sv=3)
    
    The weather workflow prompt entered in the n8n Assistant chat box
    
    Mockingbird is a sample API with weather for about 40 European cities. Other cities return an error.
    
3.  Approve any prompts from n8n Assistant with **Allow once**. As it builds the workflow, you'll see the progress on the canvas to the right of the chat.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-f301c104b5cd3724a94e85a7535d9e3d00523cb4%252Fbuild-your-first-workflow-assistant-03.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6a4652f0971f2d140aa2f92ade84ae5d&sv=3)
    
    n8n Assistant asking the user for permission
    
4.  Approve a run if prompted by n8n Assistant. Otherwise, ask n8n Assistant to run a test for you.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-586d76136370c83ea062c40743c45236cfcca9ae%252Fbuild-your-first-workflow-assistant-04.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2c1a0007888a0b0e9bc3241f719eeb0c&sv=3)
    
    n8n Assistant asking to run a live test, with the finished workflow on the canvas
    
5.  Select **Publish and enable the schedule** if prompted by n8n Assistant, as the workflow only runs at 8 AM every day once you publish it. Otherwise, ask n8n Assistant to publish it for you.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-e92833c9556ded8de6476082106adfc26376ec1d%252Fbuild-your-first-workflow-assistant-05.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9329cbda05e5ff710d27335d9de53d49&sv=3)
    
    User asking assistant to publish workflow
    
6.  Select the `weather log` data table at the top of the right-hand pane to check the workflow ran as intended. Otherwise, ask n8n Assistant to show you the data table.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-b2143070c5eb31e3ac4b7b7cbdac4bf64e34d3ed%252Fbuild-your-first-workflow-assistant-06.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=858d720c0a290c0d51e428c1d26b6da7&sv=3)
    
    weather log tab selected at the top of the right-hand pane
    
7.  Select **Personal** in the left menu to see the workflow. n8n Assistant saves all workflows under **Personal**.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-e717e2dcfbfb1838ad2e85d35e2c611c97a41ae2%252Fbuild-your-first-workflow-assistant-07.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0af36980ea5c5cc1090b338b53afcaff&sv=3)
    
    weather log listed under Personal, marked as Published
    

What your workflow does[](https://docs.n8n.io/build-your-first-workflow#what-your-workflow-does)

-------------------------------------------------------------------------------------------------

Open **weather log** on the canvas and you'll see four [nodes](https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes)
, each doing one job and passing its result to the next:

Node

What it does

**Every day at 8 AM**

A [Schedule Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger)
 that starts the workflow at 8 AM every day.

**Get Berlin weather**

An [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 node that fetches the weather from the Mockingbird API.

**Add weather report**

An [Edit Fields (Set)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set)
 node that builds the `report` text, using an [expression](https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation)
 to pull in the live weather values.

**Save weather log**

A [Data table](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable)
 node that inserts the report as a new row in the table.

n8n Assistant chooses the node names itself, so yours may differ from the ones above.

Optional: Build the workflow yourself[](https://docs.n8n.io/build-your-first-workflow#optional-build-the-workflow-yourself)

----------------------------------------------------------------------------------------------------------------------------

This section builds the weather log workflow by hand, one node at a time, without n8n Assistant.

You'll end up with a second workflow built from the same four nodes: **Every day at 8 AM**, **Get Berlin weather**, **Add weather report**, and **Save weather log**. You'll also create a new data table in the process.

### 1\. Create the workflow[](https://docs.n8n.io/build-your-first-workflow#id-1.-create-the-workflow)

1.  Select **Personal** in the left menu followed by **Create workflow**. This opens the canvas, where you’ll build your workflow and spend most of this section.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-25137bf3072eaff3007f357a95edde2f41b4f25e%252Fbuild-your-first-workflow-optional-01-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6a9384e10e92d309d09dee8c116fbfab&sv=3)
    
    Personal in the left menu and the create workflow button
    
2.  Select the workflow’s name and change it to `Weather Log 2` (or something more creative). Select anywhere on the canvas to save the name.
    

### 2\. Run it at 8 AM every day[](https://docs.n8n.io/build-your-first-workflow#id-2.-run-it-at-8-am-every-day)

You’ll use: **Schedule Trigger**

When building a workflow, the first question to answer is: “How should this workflow start?” On a schedule, for example 8 AM every day? When a user submits a form? When an application like Telegram sends a message?

For this build, you'll set it to run at 8 AM every day. While you build, you’ll run the workflow yourself to test it. Once you publish it at the end, the schedule runs it for you:

1.  Select **Add first step**, then select **On a schedule**.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-cc72b41fb23a0fa86e4ded75b5c3ce3772e02299%252Fbuild-your-first-workflow-optional-02-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9594af12026d8ba53ba5e34ddcb8291a&sv=3)
    
    On a schedule option
    
2.  Select `8am` from the **Trigger at Hour** field in the Node details view. Select the close button in the top right to close the window.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-c06ced8528a912bde326efa09e6e3861e104c89c%252Fbuild-your-first-workflow-optional-02-02.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a83078e5dd112c197815aa0609f85425&sv=3)
    
    Trigger at Hour set to 8 AM
    
3.  Select the **Schedule Trigger** node and press space bar to open up the rename dialog box. Rename it to `Every day at 8 AM`.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-d930e170605d957fcbd17ebc150c18889a8cacba%252Fbuild-your-first-workflow-optional-02-03.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=79cba98c33dcad90f9eece748104e53e&sv=3)
    
    Renamed Schedule Trigger
    

### 3\. Get the weather for Berlin[](https://docs.n8n.io/build-your-first-workflow#id-3.-get-the-weather-for-berlin)

You’ll use: **HTTP Request**

You’ve got your trigger, so it’s time to fetch the weather. The **HTTP Request** node sends a request to a web address, called an endpoint, and returns the data that address provides. Services that share data this way are APIs.

1.  Select **+** after the trigger, type `http` in the **Search nodes** box, and select **HTTP Request**.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-57f66f24a74bae5c39727fae3b95068af1492590%252Fbuild-your-first-workflow-optional-03-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=06a2e258907b6311706ffd48425930e3&sv=3)
    
    HTTP Request in the search results
    
2.  Paste `https://mockingbird.n8n.io/v1/weather/berlin` into the **URL** field in the Node details view.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-003dea0a8037113910cb3e0652992498b2d44701%252Fbuild-your-first-workflow-optional-03-02.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=76ab6489ff3fb2036941f12b5aa601c4&sv=3)
    
    Mockingbird URL in the URL field
    
    Mockingbird is a sample API with weather for about 40 European cities. Other cities return an error.
    
3.  Press **Execute step**. You should see the weather for Berlin in the output, including the `city`, `temp_c`, and `condition` fields you’ll use in the next step.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-f7f7a69a8d0612a1825e7ce0cbfc6d5d1a3f766c%252Fbuild-your-first-workflow-optional-03-03.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d43ba23eda415b2e18c8c7f4cac91d20&sv=3)
    
    Berlin weather output
    
4.  Rename the node to be `Get Berlin weather`.
    

### 4\. Turn the weather into a report[](https://docs.n8n.io/build-your-first-workflow#id-4.-turn-the-weather-into-a-report)

You’ll use: **Edit Fields (Set)**

Next, you’ll turn the weather data into a short report that anyone can read at a glance.

1.  Select **+** after **Get Berlin weather**, select **Data transformation**, then select **Edit Fields (Set)**.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-5462d028a677b26be79dd0169cfb496785602620%252Fbuild-your-first-workflow-optional-04-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=aef51e06c1f7cb7c4d41d1cb130797da&sv=3)
    
    Edit Fields (Set) under Data transformation
    
2.  Select **Add Field** in the middle of the Node details view. For **Name**, enter `report`.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-191e07b87920ea786cf3cf858b458f9bdd17f271%252Fbuild-your-first-workflow-optional-04-02-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4c1090c69e420fe04ea116c02c991949&sv=3)
    
    Add Field button
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-141c12de2737f40150f2c8fe4cb4673bea00999b%252Fbuild-your-first-workflow-optional-04-02-02.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d0f47f140b39d54b015c3445f0fff910&sv=3)
    
    Field named report
    
3.  Enter `The temperature in` for **Value**, then drag `city` from the input panel on the left. When you drop a field in, n8n switches **Value** to **Expression** mode, and you see:
    
    Copy
    
        The temperature in {{ $json.city }}
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-db39374ab2fedbb37cf9d2878a495b96ce840a6b%252Fbuild-your-first-workflow-optional-04-03.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=51ccc990db2821ea100d585c7b4499c5&sv=3)
    
    city dragged into the Value field
    
    **What's an expression?**
    
    `{{ $json.city }}` is a placeholder, called an expression. When the workflow runs, n8n swaps it for the real value. The input panel shows the output from **Get Berlin weather**, which becomes the input to this node. You drag fields in rather than typing them, and the preview under the field shows you the finished sentence. To learn more, see [Expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes#expressions)
    .
    
4.  Drag `temp_c` in and update the wording to:
    
    Copy
    
        The temperature in {{ $json.city }} is {{ $json.temp_c }}°C.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-05d6b75efbb015408530e3f01aa1803e7f9280a4%252Fbuild-your-first-workflow-optional-04-04-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=61e9c36f9bfcd38fd70e6ddab02ec816&sv=3)
    
    Value with city and temperature
    
    Add `It's currently` to the end, then drag `condition` in:
    
    Copy
    
        The temperature in {{ $json.city }} is {{ $json.temp_c }}°C. It's currently {{ $json.condition }}.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-5f3deb81adbff4aaf4c7ba628a9d53d9fe61a408%252Fbuild-your-first-workflow-optional-04-04-02.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=983cb075d8854ca6918d7d4d2bf30cbb&sv=3)
    
    Value with city, temperature, and condition
    
5.  Rename the node to `Add weather report` and select **Execute step**.
    

### 5\. Save the data[](https://docs.n8n.io/build-your-first-workflow#id-5.-save-the-data)

You’ll use: **Data table**

You’ve fetched the data and formatted it, so now it’s time to store it. You'll create a data table in the process.

1.  Add a **Data table** node after **Add weather report** and select **Insert row** as the action.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-8ed395442c2b6b202c1f2efce676c7bdcead39e0%252Fbuild-your-first-workflow-optional-05-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dde2e5ef9f00480eedf76ca54c90a8b0&sv=3)
    
    Insert row action
    
2.  Open the node, select the drop down under **Data table**, then select **Create new data table**:
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-3dfb64c5396a6220ad9ede3e7cd4090e8d54f4af%252Fbuild-your-first-workflow-optional-05-02.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c5ef34542cb83ab2e50d3132b198d254&sv=3)
    
    Create a new data table
    
    A new browser tab will open.
    
3.  Enter `weather log 2` for the name of your data table (or something creative!), and select **Create**:
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-d316e744709e8b7e1af3a32d954cc73709ee6c4f%252Fbuild-your-first-workflow-optional-05-03.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f7de38798360c507c240d145b2d28a76&sv=3)
    
    Name the new data table
    
4.  Select **Add Column** on the top right and enter `report` before selecting **Add Column**. This will be the column the data from the `Add weather report` node gets saved to.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-0bf66180682f05f0ecfdd49de8a3df80aa02d601%252Fbuild-your-first-workflow-optional-05-04.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0b38b48bb1223c5fa6bdc3bf8b156234&sv=3)
    
    Add a column to the new data table
    
    Navigate back to the workflow tab.
    
5.  Select the data table you just created from the **Data table** list and change **Mapping Column Mode** to **Map Automatically**. The `report` field from **Add weather report** has the same name as the column in the data table, so n8n maps them for you.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-3b4cd2cd6b9fda2db4dd37735b2c72f75380822b%252Fbuild-your-first-workflow-optional-05-05.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c1d1664d62ff9405d93e3d4ecd0bf705&sv=3)
    
    Data table node with the data table selected and Map Automatically set
    
6.  Rename the node to `Save weather log`.
    

### 6\. Test and publish the workflow[](https://docs.n8n.io/build-your-first-workflow#id-6.-test-and-publish-the-workflow)

Your workflow is complete. Test it, then publish it so it runs every day at 8 AM.

1.  Select **Execute** under the canvas to test it. You should see green check marks on all four nodes:
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-10479180cc9280bc28e3632dc8af29610a544a71%252Fbuild-your-first-workflow-optional-06-01.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=841718abb7e5e1229789e9669a7a9773&sv=3)
    
    Successful workflow run after execution
    
2.  Navigate to **Personal** > **Data tables** to see the new row.
    
3.  Select **Publish** in the Canvas header and follow the prompts to publish the workflow.
    
    ![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2446198290-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCxSeOtVxqqhfxMSac0AV%252Fuploads%252Fgit-blob-d969f80e0d19f877a0c3ebfaf06b4242a4aa65d8%252Fbuild-your-first-workflow-optional-06-03.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=60e246fd9f785fe40c9121cf8eb96264&sv=3)
    
    Publish the workflow
    

Next steps[](https://docs.n8n.io/build-your-first-workflow#next-steps)

-----------------------------------------------------------------------

*   Take [courses at n8n Academy](https://go.n8n.io/gfzWgF)
    .
    
*   Explore more examples in [workflow templates](https://n8n.io/workflows/)
    .
    

Related resources[](https://docs.n8n.io/build-your-first-workflow#related-resources)

-------------------------------------------------------------------------------------

*   [n8n Docs](https://docs.n8n.io/)
    
*   [Choose how to use n8n](https://docs.n8n.io/choose-how-to-use-n8n)
    
*   [Use n8n Assistant](https://docs.n8n.io/build/ways-of-building-workflows/n8n-assistant)
    
*   [Learning paths](https://docs.n8n.io/learning-paths)
    
*   [Key concept glossary](https://docs.n8n.io/key-concept-glossary)
    

[PreviousChoose how to use n8n](https://docs.n8n.io/choose-how-to-use-n8n)
[NextLearning paths](https://docs.n8n.io/learning-paths)

Last updated 5 days ago

Was this helpful?