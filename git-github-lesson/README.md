# Git & Github

Lesson |  Information
--- | --- |
**Duration** | 1 hour
**Creator** | Kristyn Bryan 
**Competencies** | Git & Github

## Lesson Objectives
1. What is Git?
2. What is Github?
3. How do they work together?
4. How do you make a repository?
5. How do you interact with a repo that is not yours (forking, cloning, pull requests)?

<hr>

## What is git?

A version control system - a way to track changes in your computer.

![version control](https://i.imgur.com/sXyZ6nK.png)

Git does this for you "behind the scenes"!

## What is Github?

Github is a company that offers storage for your files. It offers a way for people to easily share their files through forking & cloning. In addition, collaboration is made possible by allowing multiple people to become collaborators on repositories.

## Who Uses It?

Companies who share their code: https://octoverse.github.com/

- Nasa: 
  - https://www.nasa.gov/mission_pages/apollo/missions/apollo11.html
  - https://github.com/chrislgarry/Apollo-11
- Spotify:
  - https://github.com/zmb3/spotify
- YOU!

## How Do Git and Github Interact?

### Git

You work with **git** for your local tracking.

![git](https://i.imgur.com/JI8rNwP.png)

### Github

Github is a company that will store your documents "in the cloud". You can have access to your code from any machine from their company website: www.github.com or their enterprise site: https://enterprise.github.com.

![github](https://i.imgur.com/c92z3Wx.png)


### Your Part in Their Relationship

You play the most important part in this relationship. You have to tell **git** whether to track files. In addition, you can also tell **git** to send your work to **Github**. 

You do all of this with **git** commands on your command line / terminal.


## Practice Making a Github Repo

### 2 Ways :octocat:

#### 1. Making a repo on Github first and cloning it locally

1. Go to your Github account and log in to your account.

2. Click on the plus sign next to your profile photo at the top-right corner of your page:

    ![new repo](https://i.imgur.com/u21yY3L.png)

3. Click on `New repository`

    ![new repo click](https://i.imgur.com/w9tkj8J.png)

4. Create a new repo by entering a name in the `Repository Name` field. Note that this name has to be *unique* to your repository. Let's use the random name that they suggested for me: `repo-practice`

    ![repo name](https://i.imgur.com/j8Ex7hX.png)

5. This will be a **public** repo. Private repos required a paid account. 

6. Click on the "Initialize this repository with a README". A README file is just a blank document that is the default page that your repository displays. It is a markdown file and normally includes information that you provide about your application.

    ![readme](https://i.imgur.com/OMX3sah.png)
    
7. Click `Create repository`. You should be redirected to the newly made repo.

8. Click on the `Clone or download` button.

9. Copy the link (this is the direct link that is created by Github to your repo).

    ![clone and download](https://i.imgur.com/eQAy4O3.png)

10. Open your terminal / Git Bash - it's time to make a local copy of this Github repo!

11. In your terminal / Git Bash, navigate to the folder where you would like to keep the folder for this repo. 

12. Type the git command `git clone` followed by the link to your repo.

    ![clone](https://i.imgur.com/SaOFuio.png)
    
13. That's it! Type `ls` to see your files. Your new repo should be there. Navigate inside the folder, type `ls` and confirm that you have a `README.md` file.

<hr>

#### 2. Making a local folder, turning it into a git repo, pushing it up to Github

1. Navigate to the folder where you're going to keep the files for this lesson.

2. Create a new folder called `git-repo-practice`.

3. Navigate inside `git-repo-practice` and type `git status` (you should get an error). We need to ask git to track this folder, so let's tell it to do so.

4. Inside this folder, run the command `git init` (this tells git to track this folder). Type `git status` to see that there is no longer an error.

5. We now have a local git repo, we have to create a repo on Github and connect it. Navigate to Github and log in if you're not logged in already.

6. Create a new Github repo. Let's give it the name `git-repo-practice` (note that this is the same as our local file, but it does not have to be for it to work).

7. **Do not** initialize a README (we'll make it on our own in our local repo).

8. Copy the repo address (it will look like: git@github.com:username/new_repo).

9. Go back to your terminal / Git Bash. We will create a remote called `origin` by running the command `git remote add origin git@github.com:username/new_repo` (replace the last part with your specific repo address).

10. Confirm that you have the remote created by running the command `git remote -v`

11. Let's create a README and push it up to our Github repo. From inside our local `git-repo-practice` folder, create a file called `README.md`.

12. Type `git status` to see that we have a new file that needs to be committed.

13. `git add .`, `git commit -m"adding initial README file"`, `git push origin master` 

14. Go back to Github and refresh your page. Your README file should now be pushed up from your local repo to your Github repo.


<hr>

## Interacting with Other People's Repos

Sometimes we want to interact with another user's repo. We can safely do this by **forking** it.

**Forking** is the equivalent of making a copy to keep for ourselves.

![mona lisa](img/mona_lisa.png) ![mona lisa cat](img/mona_lisa_cat.png)

<hr>

## Let's Practice Together

### Part 1

1. Navigate to: https://github.com/teaching-materials/git-github-practice/blob/master/README.md

2. Fork this repo and add it to your personal repo.

    <details><summary>What it looks like on Github</summary>

    ![fork](https://i.imgur.com/cmP8Hnd.png)

    </details>

3. On Github, navigate to your personal repo.

    <details><summary>What it looks like on Github</summary>

    ![main page](https://i.imgur.com/Ay1re5i.png)

    ![repos](https://i.imgur.com/8KGEA99.png)

    </details>

4. On Github, navigate to your forked version of this repo (your username should be in the top left corner of the page followed by a slash and the name of the repo. Ex: `harrypotter/git-github-practice`).

### Step 2

5. Click on the `clone or download` button: 

    <details><summary>What it looks like on Github</summary>

    ![clone or download](https://i.imgur.com/6fFU7zd.png)

    </details>


5. Copy the web address:

    <details><summary>What it looks like on Github</summary>

    ![clone](https://i.imgur.com/VXcjHf9.png)

    </details>


6. Open your git bash (terminal / Git Bash).

7. Navigate to the folder where you would keep your work for today (if your class does not have a specific file structure for you to follow, possibly make an external folder by the topic that you're learning).

8. Make a clone of your github forked repository by running the command `git clone` followed by the address of your fork (the web address that you copied in **step 5**):

    <details><summary>What it looks like in your terminal / Git Bash </summary>

    ![clone](https://i.imgur.com/IUCw6YD.png)

    </details>

NOTE: This will create a folder named the same as the repo. It should contain all of the files and folders that were located in the repo.

## Step 3

9. Check it out! Type `ls` to see the files that you cloned from Github. These files are now **local**. 

10. Navigate inside the repo.

11. Type `git remote -v` to confirm that git has created a remote link for you. The default name is `origin` and to confirm that you're inside the right file, check the name of the repo in the remote link. 

## Step 4

12. Open the `hello.py` file in your text editor.

13. Adjust the code according to the activity

1. Save your file in your text editor.

## Step 5

2. In your terminal / Git Bash, run the command `git status` to see that there is a file that has changes that need to be added and committed.

3. In your terminal, run the command `git add .` to add all of the files that need to be tracked.

    <details><summary>What it looks like in your terminal</summary>

    ![add](https://i.imgur.com/jd0lwWe.png)

    </details>
    
4. In your terminal / Git Bash, run the command `git commit -m" add a message here about what you did"` to commit the files.


    <details><summary>What it looks like in your terminal</summary>

    ![commit](https://i.imgur.com/nhHoBan.png)

    </details>

5. In your terminal / Git Bash, run the command `git push origin master` to push your work from your local machine to your repository on Github.

   <details><summary>What it looks like in your terminal</summary>

   ![push](https://i.imgur.com/STKsEoF.png)

   </details>
   
   NOTE: `origin` here refers to the default variable name that git has assigned to your repository. `master` refers to the default branch that Github creates for you when you make a new repository.

6. Go to Github, look at your forked repo, refresh the page. Your changes (your favorite ice cream flavor or `banana`) should now appear in the `README.md` file.

## Step 6

1. From your fork in Github, click on `New pull request`.

   <details><summary>What it looks like in your terminal</summary>

   ![pull request](https://i.imgur.com/S7EpxXH.png)

   </details>
   
2. The base fork should automatically be set to the **original** repo and the head fork will be **your** fork of the repo. If it's not, then you're probably trying to submit a pull request from somewhere other than your forked repo.

   <details><summary>What it looks like in your terminal / Git Bash</summary>

   ![pull request view](https://i.imgur.com/iFqLqnW.png)

   </details>
   
3. Click `Create pull request`.


   <details><summary>What it looks like in your terminal / Git Bash</summary>

   ![pull request submit](https://i.imgur.com/UwMhKgR.png)

   </details>
   
That's it! :clap:

Oh wait... let's change something...

## Step 7

1. In your text editor, open the `hello.py` file and change the name in the string from `hello, you!" to `Grumpy Cat`. Save your file.

2. In your terinal / Git Bash, run `git status` to see that there is a change that has been tracked.

3. Go through the process of adding, committing, and pushing your code.

4. Go back to Github and look at the pull request that you submitted. It should have our newly updated code!

![grumpy cat](https://i.imgur.com/tqifmk9.png)

<hr>

## Practice on Your Own

1. Navigate to this lab and follow the directions in the markdown: https://github.com/teaching-materials/git-lab/blob/master/README.md

## Final Questions?

