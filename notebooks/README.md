# Recommended Practices For Jupiter Notebooks
When using jupiter notebooks it is recommended to pair them using a [jupytext](https://github.com/mwouts/jupytext) to a python or md files, so that any change in them will happen also in the paired files.
This will allow tracking changes/versions in git and formatting the code(black, isort). Jupytext supports 2 way syncing both in jupiter-lab and notebook, see:
* https://jupytext.readthedocs.io/en/latest/paired-notebooks.html

Use a pre-commit hook to make sure it happens before every commit, see:
* https://jupytext.readthedocs.io/en/latest/using-pre-commit.html

To install:
```bash
pip install jupytext --upgrade
```
To export a specific notebook to python you could run:
```bash
jupytext --to py:percent notebook.ipynb
```
To run black formatter on a Notebook:
```bash
jupytext --sync --pipe black notebook.ipynb
```
To add a pre-commit hook and pipe output to black for formatting:
```yaml
-   repo: https://github.com/mwouts/jupytext
    rev: v1.11.0  # CURRENT_TAG/COMMIT_HASH
    hooks:
    - id: jupytext
      args: [--from, ipynb, --to, "py:percent",--sync, --pipe, black]
      additional_dependencies:
        - black==20.8b1 # Matches hook
```
Currently, the hook only works if you have a paired notebook and add the notebook to the commit.
if you want to save the notebook with the outputs it might be quite large, and it's probably best to use git-lfs,
otherwise you can remove the ipynb file from the commit and only commit the paired file.
