For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n.md)
.

n8n uses Git to provide source control. To use this feature, it helps to have some knowledge of basic Git concepts. n8n doesn't implement all Git functionality: you shouldn't view n8n's source control as full version control.

**New to Git and source control?**

If you're new to Git, don't panic. You don't need to learn Git to use n8n. This document explains the concepts you need. You do need some Git knowledge to set up the source control, as this involves work in your Git provider.

**Familiar with Git and source control?**

If you're familiar with Git, don't rely on behaviors matching exactly. In particular, be aware that source control in n8n doesn't support a pull request-style review and merge process, unless you do this outside n8n in your Git provider.

This page introduces the Git concepts and terminology used in n8n. It doesn't cover everything you need to set up and manage a repository. The person doing the [Setup](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
 should have some familiarity with Git and with their Git hosting provider.

**This is a brief introduction**

Git is a complex topic. This section provides a brief introduction to the key terms you need when using environments in n8n. If you want to learn about Git in depth, refer to [GitHub | Git and GitHub learning resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources)
.

Git overview[](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n#git-overview)

---------------------------------------------------------------------------------------------------------------

[Git](https://git-scm.com/)
 is a tool for managing, tracking, and collaborating on multiple versions of documents. It's the basis for widely used platforms such as [GitHub](https://github.com/)
 and [GitLab](https://about.gitlab.com/)
.

Branches: Multiple copies of a project[](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n#branches-multiple-copies-of-a-project)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Git uses branches to maintain multiple copies of a document alongside each other. Every branch has its own version. A common pattern is to have a main branch, and then everyone who wants to contribute to the project works on their own branch (copy). When they finish their work, their branch is merged back into the main branch.

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1614847662-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FwMJrGrimpx3PxCJpUswm%252Fuploads%252Fgit-blob-29b711181b0f9d5a6385dd0674d55b32529d69b6%252Fsimple-git-branch.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d4b4e4c922f8c827cbc1e5b82d4fe1b4&sv=3)

Main branch with two separate branches forked from it, each merged back into main at a different point

Local and remote: Moving work between your machine and a Git provider[](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n#local-and-remote-moving-work-between-your-machine-and-a-git-provider)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A common pattern when using Git is to install Git on your own computer, and use a Git provider such as GitHub to work with Git in the cloud. In effect, you have a Git repository (project) on GitHub, and work with copies of it on your local machine.

n8n uses this pattern for source control: you'll work with your workflows on your n8n instance, but send them to your Git provider to store them.

Push, pull, and commit[](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n#push-pull-and-commit)

---------------------------------------------------------------------------------------------------------------------------------

n8n uses three key Git processes:

*   **Push**: send work from your instance to Git. This saves a copy of your workflows and tags, as well as credential and variable stubs, to Git. You can choose which workflows you want to save.
    
*   **Pull**: get the workflows, tags, and variables from Git and load it into n8n. You will need to populate any credentials or variable stubs included in the refreshed items.
    
    **Pulling overwrites your work**
    
    If you have made changes to a workflow in n8n, you must push the changes to Git before pulling. When you pull, it overwrites any changes you've made if they aren't stored in Git.
    
*   **Commit**: a commit in n8n is a single occurrence of pushing work to Git. In n8n, commit and push happen at the same time.
    

Refer to [Push and pull](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
 for detailed information about how n8n interacts with Git.

Related resources[](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n#related-resources)

-------------------------------------------------------------------------------------------------------------------------

*   [Use source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [Understand source control](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control)
    
*   [Work with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
    
*   [Choose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
    
*   [Set up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
    
*   [Push and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
    
*   [Compare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)
    
*   [Move work between environments](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments)
    
*   [Use environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)
    
*   [Tutorial: Create environments with source control](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control)
    

[PreviousWork with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
[NextChoose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)

Last updated 10 days ago

Was this helpful?