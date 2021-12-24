# Git & GitHub Tutorial  
**Content of table** 
- [Linux commands](#linux-commands)
- [Literature review](#literature-review)
- [Local repository](#local-repository)
- [Remote repository](#remote-repository)
- [Git checkout](#git-checkout)
- [Undoing](#)




# Linux commands
- [Current directory](#current-directory)
- [Change directory](#change-directory)
  - [Navigate back folder](#navigate-back-folder)
  - [Navigate forward folder](#navigate-forward-folder)
- [Make new folder](#make-new-folder)
- [List current folder contents](#list-current-folder-contents)
- [Make new file](#make-new-file)
- [Clear terminal](#clear-terminal)
## Current directory
```bash
pwd
```
> /d/GitHub/
## Change directory
`cd <desired directory>`
```bash
cd /d/GitHub/
```
### Navigate back folder
`cd ..`
```bash
cd ..
```
>cd /d/
### Navigate forward folder
`cd <desired folder name>`
```bash
cd GitHub
```
>cd /d/GitHub/
## Make new folder
`mkdir <desired new folder name>`
```bash
mkdir gittutorial
```
## List current folder contents
`ls`
## Make new file
`touch <file name>`
```bash
touch index.py
```
## Clear terminal
`clear`




# Literature review
- [Working tree](#working-tree)
- [Commit](#commit)
- [Stage](#stage)
- [Tracked/Untracked file](#trackeduntracked-file)
- [Modifed file](#modifed-file)
- [Nothing added to commit](#nothing-added-to-commit)
- [Changes not staged for commit](#changes-not-staged-for-commit)
- [HEAD](#head)
- [Local](#local)
- [Origin](#origin)
- [Remote](#remote)
- [Both modified](#both-modified)
- [Clone](#clone)
- [Ahead of origin/master](#ahead-of-originmaster)
- [Behind of origin/master](#behind-of-originmaster)
- [Your branch is up to date](#your-branch-is-up-to-date)
- [Origin/master & master](#originmaster--master)
- [Tag](#tag)


## Working tree
* The working tree, or working directory, consists of files that 
you are currently working on.  
* You can think of a working tree as a file system where you can
view and modify files.
## Commit
* save your file/files that put in stage, and after commit, 
git consider this file/files as a HEAD file. You will be 
availble call every commit in future.
* Git considers each commit change point or "save point". 
It is a point in the project you can go back to if you find 
a bug, or want to make a change.
## Stage
* stage is a place that, 1. untracked files put in stage in 
order to in commit phase, tracked by git. or 2. 
modified/deleted/... files that already tracked by git, 
put in stage in order to save changed in commit phase.
## Tracked/Untracked file
* you have NEW file/files that if contents modified, git can't 
sense alterations.
* Untracked basically means that Git sees a file you didn't have 
in the previous snapshot (commit), and which hasn't yet been 
staged.
* Untracked files are most of the time files you don't want to
be controlled, because for example they are generated by your 
compiler.
* Tracked - files that Git knows about and are added to the 
local repository.
* Untracked - files that are in your working directory, but 
not added to the local repository.
## Modifed file
* git always check tracked file/files,when file/files contents has 
been changed, git label it/these to modified file.
## Nothing added to commit
* no file/files are in stage to commit.
## Changes not staged for commit
* your tracked file/files has been modified, and NOT yet put in 
stage to commit.
## HEAD
* HEAD is last/final commit (last saved alterations).
## Local
* local meaning is in your personal computer.
* EX:  
local commit : a written commit that has been write in your computer and has
not yet push in remote repository.
## Origin
* origin" is the name of the remote repository where you want to 
publish you commits. By convention, the default remote repository 
is called "origin", but you can work with several remotes 
(with different names) as the same time. More information here.
## Remote
* A remote repository in Git, also called a remote, is a Git 
repository that's hosted on the Internet or another network.
## Both modified
* recommend you : commit and merege early early!
* recomend you : pull repository, and edited it and commit and 
push it.
## Clone
* duplicate and download everything of remote repository
when you use command clone in git, git create new folder with 
name as same as name of remote repo in github and copy and 
download everything and put it them on this folder.
## Ahead of origin/master
## Behind of origin/master
* when you fetch remote repo on your local repo, this guide say 
you, remote repo have new commits so that you have not these 
commits in your local repository. and you "behind of 
origin/master" this meaning that, you are NOT update rather to 
origin remote on master branch.
## Your branch is up to date
* when pull (fetch and merge) remote branch with your local branch
this guide showed.
## Origin/master & master
* "remote name"/"remote branch name" & "local branch name"
## Tag
* Git has the ability to tag specific points in a repository’s 
history as being important.







# Local repository
- [Initialize git](#initialize-git)
- [Display status](#display-status)
- [Track / Stage](#track--stage)
- [Save alterations](#save-alterations)
- [Display commits](#display-commits)
- [Display differences](#display-differences)
- [Branches](#branches)
  - [Checkout in branch](#checkout-in-branch)
- [Merging](#merging)

## Initialize git
Count current directory to git and git folder create in 
current directory:
```bash
git init
```
## Display status
Summery alterations in some frequent phrases:
```bash
git status
```
> **Frequent phrases:**   
> Tracked file/files   
> Untracked file/files   
> Staged file/files   
> Unstaged file/files  

## Track / Stage
This command has two performance:
  * Track new file/files that not yet added to git.
  * Stage file/files that has been tracked by git.
```bash
git add [options]
```
Options:
  * `<file name>` :
  * `<*.py>` :
  * `<--all>` / `-A` :
  * `<modules*>` :

## Save alterations
Save(Commit) your staged/tracked file(files) with message:
```bash
git commit -m "<your message>"
```
**NOTE:** Message is require.

## Display commits
Show all commits:
```bash
git log
```
**NOTE:** If list of commit is long, you can press `q` to exit.

## Display differences
Write about it.
```bash
git diff [options]
```
Options:
  * `<nothing>`:
  * `HEAD`:
  * `--staged`:
  
## Branches
Write about branches.
```bash
git branch [options]
```
Options:
  * `nothing`: Show current branch
  * `<branch_name>`: Create new branch
  * `-d <branch_name>`: Delete branch

### Checkout in branch
Write about checkout
```bash
git checkout <branch_name>
```

## Merging
Write about merging
```bash
git merge <branch_name>
```
**NOTE:** Sure that when you merge, your current branch in 
main branch.


# Remote repository








# Git checkout
- [Switch branch](#)
- [Ignore file/files chanes](#)
- [Switch tag](#)

# Undoing
- [git reset](#)