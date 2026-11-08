For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments.md)
.

The steps to send work from one n8n instance to another are different depending on whether you use a single Git branch or multiple branches.

Single branch[](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments#single-branch)

---------------------------------------------------------------------------------------------------------------------------------

If you have a single Git branch the steps to copy work are:

1.  Push work from one instance to the Git branch.
    
2.  Log in to the other instance to pull the work from Git. You can [automate pulls](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments#automatically-send-changes-to-n8n)
    .
    

Multiple branches[](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments#multiple-branches)

-----------------------------------------------------------------------------------------------------------------------------------------

If you have more than one Git branch, you need to merge the branches in your Git provider to copy work between environments. You can't copy work directly between environments in n8n.

A common pattern is:

1.  Do work in your developments instance.
    
2.  Push the work to the development branch in Git.
    
3.  Merge your development branch into your production branch. Refer to the documentation for your Git provider for guidance on doing this:
    
    *   [GitHub: Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
        
    *   [GitLab: Creating merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
        
    *   [Git: Basic branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
        
    
4.  In your production n8n instance, pull the changes. You can [automate pulls](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments#automatically-send-changes-to-n8n)
    .
    

Automatically send changes to n8n[](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments#automatically-send-changes-to-n8n)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can automate parts of the process of copying work, using the `/source-control/pull` API endpoint. Call the API after merging the changes:

Copy

    curl --request POST \
    	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/pull' \
    	--header 'Content-Type: application/json' \
    	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
    	--data '{"force": true}'

This means you can use a GitHub Action or GitLab CI/CD to automatically pull changes to the production instance on merge.

A GitHub Action example:

Copy

    name: CI
    on:
      # Trigger the workflow on push or pull request events for the "production" branch
      push:
        branches: [ "production" ]
      # Allows you to run this workflow manually from the Actions tab
      workflow_dispatch:
    jobs:
      run-pull:
        runs-on: ubuntu-latest
        steps:
          - name: PULL
    				# Use GitHub secrets to protect sensitive information
            run: >
              curl --location '${{ secrets.INSTANCE_URL }}/version-control/pull' --header
              'Content-Type: application/json' --header 'X-N8N-API-KEY: ${{ secrets.INSTANCE_API_KEY }}'

Related resources[](https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments#related-resources)

-----------------------------------------------------------------------------------------------------------------------------------------

*   [Use source control and environments](https://docs.n8n.io/administer/use-source-control-and-environments)
    
*   [Understand source control](https://docs.n8n.io/administer/use-source-control-and-environments/understand-source-control)
    
*   [Work with environments](https://docs.n8n.io/administer/use-source-control-and-environments/work-with-environments)
    
*   [Use Git in n8n](https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n)
    
*   [Choose branching patterns](https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns)
    
*   [Set up source control](https://docs.n8n.io/administer/use-source-control-and-environments/set-up-source-control)
    
*   [Push and pull changes](https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes)
    
*   [Compare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)
    
*   [Use environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)
    
*   [Tutorial: Create environments with source control](https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control)
    

[PreviousCompare versions](https://docs.n8n.io/administer/use-source-control-and-environments/compare-versions)
[NextUse environments programmatically with the public API](https://docs.n8n.io/administer/use-source-control-and-environments/use-environments-via-api)

Last updated 10 days ago

Was this helpful?