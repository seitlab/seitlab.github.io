# Introduction
This is the source code of the MSU SEIT Lab website. Please read this document before making changes to the website.

# Important notes
* This is the the development version of seit.egr.msu.edu website, it is not published yet.
* Please do not synchronize the local Git repository via automated cloud file storage solutions, such as Tresorit, MEGA, pCloud, Dropbox, Google Drive, etc. If you work on the website from several computers, synchronize this repository only via Git. If you do want to put it into your cloud storage, create a separate local repositories for each computer you are working from.
* Unless you have solid experience merging Git branches/changesets, please avoid simultaneous website editing by multiple users. Having a dedicated person responsible for website updates is the best strategy.
* **Do not** push a commit (by running `go.sh` or doing `git push`) if you have not tested the changes---all changes are immediately published on the website.
* **Do not** push a commit if Git spits out errors or warnings.
* **Do not** include any private or sensitive information (including in comments) in the repository. Once pushed, everything is published and available to 7+ billion of people immediately.


# Preparational steps
1. Use Linux or macOS to update the website.
2. Seriously, don't use Windows for that.
3. Install the latest stable version of Node.js.
4. Install this small HTTP server: https://www.npmjs.com/package/http-server following the instructions on the website.
5. Install your favorite HTML/JS/CSS editor; we recommend VS Code: https://code.visualstudio.com/ or WebStorm: https://www.jetbrains.com/webstorm/ (student promotional license is free as of March 2020).
6. Install Git following the instruction for your OS: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
7. Clone this repository (it will ask for login/password because it is a private repo):
```
git clone https://github.com/nick-ivanov/seitlab-site-draft.git
```
8. Make `go.sh` executable:
```
chmod +x go.sh
```

# How to make changes
1. Enter the Git repository:
```
cd seitlab-site-draft
```

2. Download latest changes (**always do it before editing the website**):
```
git pull
```

3. Make desired changes. If you do not have HTML/CSS/JS experience, use these trusted free resources:
  
  * https://www.w3schools.com/
  * https://developer.mozilla.org/en-US/docs/Learn
  
It is not a rocket science, but like all skills, it may need some diligent reading.

4. **VERY IMPORTANT**: Test changes locally:
  
  * While in the root of the current repository (i.e., the `seitlab-site-draft` directory), run the mini HTTP server:
  ```
  http-server
  ```
  * Open your favorite web-browser and go to `http://127.0.0.1:8080`;
  * Make sure that your changes are correct;
  * Make sure that the changes look good **both on desktop and mobile devices**.
 
 5. Upload your changes by running the following script (you will be asked for login/password):
 ```
 ./go.sh
```

6. Go to the website and make sure that the changes have been made correctly.

# Troubleshooting

If you are experiencing troubles, that is normal. The following tips can help resolve the problem.

1. If Git throwing at you error messages you don't understand, it may be prudent just to remove the local repo and clone a clean-slate version.

2. Try to solve the problem yourself. If you are *really* stuck or at risk of breaking something, ask for help.

Good luck!
