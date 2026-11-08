For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns.md)
.

The relationship between n8n instances and Git branches is flexible. You can create different setups depending on your needs.

**Recommendation: don't push and pull to the same n8n instance**

You can push work from an instance to a branch, and pull to the same instance. n8n doesn't recommend this. To reduce the risk of merge conflicts and overwriting work, try to create a process where work goes in one direction: either to Git, or from Git, but not both.

Multiple instances, multiple branches[](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns#multiple-instances-multiple-branches)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This pattern involves having multiple n8n instances, each one linked to its own branch.

You can use this pattern for environments. For example, create two n8n instances, development and production. Link them to their own branches. Push work from your development instance to its branch, do a pull request to move work to the production branch, then pull to the production instance.

The advantages of this pattern are:

*   An added safety layer to prevent changes getting into your production environment by mistake. You have to do a pull request in GitHub to copy work between environments.
    
*   It supports more than two instances.
    

The disadvantage is more manual steps to copy work between environments.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-b0be1ee24a05de272adff8770233c8a91cfe1b52%252Fvc-multi-multi.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a0d5bd3498b5e693ebfd46f35bcb4dce&sv=3)

Development and production n8n instances, each connected to its own Git branch, with a pull request moving work between the branches

Multiple instances, one branch[](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns#multiple-instances-one-branch)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Use this pattern if you want the same workflows, tags, and variables everywhere, but want to use them in different n8n instances.

You can use this pattern for environments. For example, create two n8n instances, development and production. Link them both to the same branch. Push work from development, and pull it into production.

This pattern is also useful when testing a new version of n8n: you can create a new n8n instance with the new version, connect it to the Git branch and test it, while your production instance remains on the older version until you're confident it's safe to upgrade.

The advantage of this pattern is that work is instantly available to other environments when you push from one instance.

The disadvantages are:

*   If you push by mistake, there is a risk the work will make it into your production instance. If you [use a GitHub Action to automate pulls](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control#optional-use-a-github-action-to-automate-pulls)
     to production, you must either use the multi-instance, multi-branch pattern, or be careful to never push work that you don't want in production.
    
*   Pushing and pulling to the same instance can cause data loss as changes are overridden when performing these actions. You should set up processes to ensure content flows in one direction.
    

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-a2abf427fa5e3de60185ae69fcbd0e3c8031848b%252Fvc-multi-one.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d7bbd49ae378e486c5edbcfd54d48e1a&sv=3)

Development and production n8n instances both connected to the same single Git branch

One instance, multiple branches[](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns#one-instance-multiple-branches)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The instance owner can change which Git branch connects to the instance. The full setup in this case is likely to be a [Multiple instances, multiple branches](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns#multiple-instances-multiple-branches)
 pattern, but with one instance switching between branches.

This is useful to review work. For example, different users could work on their own instance and push to their own branch. The reviewer could work in a review instance, and switch between branches to load work from different users.

**No cleanup**

n8n doesn't clean up the existing contents of an instance when changing branches. Switching branches in this pattern results in all the workflows from each branch being in your instance.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-9eb450b2aca5aad75df2245dc97e0680c27ea1c7%252Fvc-one-multi.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2caf68cce729203a638718a03680aec2&sv=3)

One n8n instance switching between several Git branches to review work pushed by different users

One instance, one branch[](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns#one-instance-one-branch)

-------------------------------------------------------------------------------------------------------------------------------------------------

This is the simplest pattern.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-1c9e77fe8e64ca3e0ae57e111e94e89670b31062%252Fvc-one-one.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=56ab7b1f204d345d688614f2a6708ffe&sv=3)

Single n8n instance connected to a single Git branch

Related resources[](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns#related-resources)

------------------------------------------------------------------------------------------------------------------------------------

*   [Use source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [Understand source control](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control)
    
*   [Work with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
    
*   [Use Git in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
    
*   [Set up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
    
*   [Push and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
    
*   [Compare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)
    
*   [Move work between environments](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments)
    
*   [Use environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)
    
*   [Tutorial: Create environments with source control](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control)
    

[PreviousUse Git in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
[NextSet up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)

Last updated 10 days ago

Was this helpful?