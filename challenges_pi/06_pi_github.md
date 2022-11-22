# Introduction to GitHub

Later on, we are going to focus on the topics _DevOps_ and _Continuous Integration & Continuous Deployment_. A tool for this is GitHub, which ist why we will now take a closer look at GitHub and its components.

In this chapter, you will learn about these topics:

- [GitHub organization](#github-organization)
- [GitHub repository](#github-repository)
- [Fork](#fork)
- [Clone](#clone)
- [GitHub Actions](#github-actions)

## GitHub organization

A [GitHub organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations) is a shared account where team members of businesses and open-source projects can collaborate across many projects. Owners and Administrators can manage member access to the organization's data and projects with security and administrative features.

During the setup prework, you already created your own GitHub organization. This is the place, where you would invite team members and manage access to projects and repositories. For this hackathon, you aren't working in teams and therefore, do not need to add team members.

## GitHub repository

A [GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) contains all of your project's files and each file's revision history.

During the day you are going to work with Git branches, commits and pull requests.

**Optional**: To learn more about version control with Git, follow this [free and simple learning path](https://docs.microsoft.com/en-us/learn/modules/intro-to-git/).

## Fork

A [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) is a copy of a repository that you manage. Forks let you make changes to a project without affecting the original repository. You can fetch updates from or submit changes to the original repository with pull requests.

If this sounds familiar, you already forked this repo during the setup prework. In fact, you have already been working on your own fork.

## Cloning a repository

When you create a repository on GitHub.com, it exists as a remote repository. You can [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) your repository to create a local copy on your computer and sync between the two locations.

Cloning this repository to your local machine was the same as forking it already part of your prework. Therefore, this should sound familiar to you.

## GitHub Actions

[GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

GitHub Actions are comprised of several components. Today you will dive into GitHub Actions **Workflows** and learn how to build and deploy each Azure service (the ones you created previously) in an automated way.

### GitHub Actions Workflows

A GitHub Actions workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

You can find GitHub Actions in your repository. Click on _Actions_ There you can see all workflows which have been triggered. None should be in there so far.
</br>
![Screenshot of where to find GitHub Actions in a GitHub repository](/images/06actions.png)

During the next challenges, we will introduce you to Continuous Integration and Continuous Development (CI/CD). GitHub Actions is a great tool to work with to automate your processes. You will learn more about it in [next steps](./07_pi_cicd.md).