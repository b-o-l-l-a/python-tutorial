# Python Tutorial 1 - CSV to DataFrame
This tutorial covers step-by-step code snippets (and associated explanations) for: 

- Bringing data into a pandas DataFrame through a CSV
- Creating new columns in the DataFrame to make it appropriate for analysis

### In order to use this repo, you must do the following beforehand
At some point, we'll get more detailed, step-by-step instructions on each of the following. In the meantime, this provides a list of tasks needed to get started. Below this list, you'll find definitions to each of the required tools.

- Create a [github](https://github.com/) account
- If on Windows, download [Git Bash](https://gitforwindows.org/)
- Download and install [Python](https://www.python.org/downloads/). Make sure it is version 3.7 or greater
- Install [`pip`](https://pip.pypa.io/en/stable/installing/) onto your machine.
- Install [`pipenv`](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv) 
- Run the following commands (in order) on your Terminal (on a Mac) or Git Bash (on Windows)

```
git clone https://github.com/b-o-l-l-a/python-tutorial.git
cd python-tutorial
pipenv install
```

**github**: Used for _version control_ of software development projects. Sometimes, multiple people are developing different pieces of functionality in the _same_ project. Github allows all developers to "push" changes they've created into the project, and "pull" changes that others have made, among other things
<br/>**Git Bash / Terminal**: An interface that you can use to run commands on your computer
<br/>**pip**: A "package management system" to install and manage software packages (aka libraries) written in Python. The Python you install from [this page](https://www.python.org/downloads/) doesn't have _all_ the functionality you may want as a developer. People have developed _third-party packages_ (or _libraries_) which focus on a particular function; these packages can be installed through `pip`
<br/>**pipenv**: Manages all the needed packages for a particular project/environment. There are a few other options that perform the same task (e.g., [`virtualenv`](https://virtualenv.pypa.io/en/latest/)), but my personal fave is pipenv. It keeps all needed libraries and their versions in an easy-to-use `Pipfile` 

## Click on the [`tutorial-1-read_csv_to_df_operations.ipynb`](https://github.com/b-o-l-l-a/python-tutorial/blob/step-1-csv/tutorial-1-read_csv_to_df_operations.ipynb) to get started
