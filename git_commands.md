# Git Commands Used in FreshCart Project

| Command | Where the change happens | What exactly happens? |
|---|---|---|
| `git init` | Working folder → Local Git | Initializes a new Git repository in the current folder. |
| `git add train.py` | Working folder → Local Git staging area | Stages `train.py` so it can be included in the next commit. |
| `git commit -m "msg"` | Local Git | Saves the staged changes as a new commit in the local repository. |
| `git remote add origin URL` | Local Git → Remote Git connection | Links the local repository to the specified GitHub repository. |
| `git push -u origin main` | Local Git → Remote Git | Uploads local commits from the main branch to GitHub and sets the upstream branch. |
| `git pull origin main` | Remote Git → Local Git | Fetches changes from GitHub and merges them into the current local branch. |

## Question

**After running `git commit`, can your teammate see your code on GitHub? Why or why not?**

No. A commit saves changes only in the local Git repository. The teammate can see the changes on GitHub only after the commits are pushed to the remote repository using `git push`.
