<p align="center">
    <img width="400px" src="https://penseemti.com.br/wp-content/uploads/2019/01/python-logo.png" alt="Python logo"/>
</p>

# Introduction to programming 
 Final project regarding the Introduction to Programming course, taught by Professor Dr. Fernando Neto at the Computer Center at the Federal University of Pernambuco - Brazil.

### Project brief
This system was created with the purpose of optimizing communication within hospitals, including reception staff, doctors and the director. All are interconnected, one depending on the other. In the reception system we have several functionalities, such as creating a patient's record, reading this record, updating and also deleting, within the reception program, you also have the option of placing a patient on the waiting list to be seen. In the doctor's system, he can know the number of people who are on the waiting list waiting for care, he can also start seeing patients, knowing in advance what they are feeling and ending the consultation. In the director's system he has all the control of the hospital, he can create a register for the employees, he can know the number of patients and employees registered, he can read all the information of the patients and employees, he can change the level of access of the employees and also you can delete an employee's registration. The system database is made in txt files. The system also has features like login, access levels and also has a log file, to generate a history of what was done and who did it, the database of the log file is in a csv file.

### First Steps

Initially, clone the repository:

```
git clone https://github.com/viniciuslima-99/introduction-to-programming.git
```

## Technology

* **[Python](https://docs.python.org/3/)** - Python is a high-level, interpreted, scripting, imperative, object-oriented, functional, efficient and strong typing language. 

## GitHub

### Branches
They can be:
+ master
+ feature
+ bugfix
+ hotfix

Their names must follow this template: `feature/branch-name`

### Commits
Must begin with the name of the branch you developed on, following the model: _“Feature(name-of-feature) : What was done…”._

Must be simple and show briefly what you just did.

- Ex: `git commit -m “Feature(issue_name) : Added ...”`
- Ex: `git commit -m “Bugfix(issue_name) : Changed ...”`
- Ex: `git commit -m “Hotfix(issue_name) : Fix ...”`

### Pull Requests
First, proceed with _rebase_:
1. _commit_ the changes on your branch
2. Go to the original branch (master) with `git checkout master`
3. Run `git pull`
4. Go back to your branch with `git checkout "your-branch"`
5. Run `git rebase master`
6. Follow the steps to conclude the _rebase_, solving conflicts and running `git add .` and then `git rebase --continue`
7. When finished rebasing, run `git push -f origin "your-branch"`. Now your Pull Request can be opened on GitHub.

Use this template for the pull request body:
```
### Issue Name
**What I did:**

- First thing I did...

- Second thing I did...

**How to test:**

- First step to execute the project...

- Second step to execute the project...

```

```markdown
Made with `markdown` and love by Vinícius Lima
```