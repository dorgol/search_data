# Empty Project template

  * [Template Goal](#template-goal)
  * [Folder structure](#folder-structure)
  * [Quick Run](#quick-run)
    + [Run on your local machine](#run-on-your-local-machine)
    + [Run Remotely](#run-remotely)
  * [Customization](#customization)
    + [How to customize this template to your own non-segmentation model](#how-to-customize-this-template-to-your-own-non-segmentation-model)
    + [Step A: Dataset customization](#step-a--dataset-customization)
∂    + [Step B: Model customization](#step-b--model-customization)
    + [Inference](#inference)
- [Contribution](#contribution)
## Template Goal
This template has a similar base as the Lightning-template. It has the same github workflows, pre-commits and
configuration files for an easy start.
## Folder structure
- [README.md](README.md) this file
- [prerun.sh](prerun.sh) script used in Cnvrg to setup environment
- [pyproject.toml](pyproject.toml)  project configurations (used for externals tool like black and isort)
- [requirements.txt](requirements.txt)  packages needed to install to use project
- [my_project_name](my_project_name)  all your src files
- [tests](tests) pytest files to test your code
- [notebooks](notebooks) a folder for Jupyter notebooks, see the [guidelines](notebooks/README.md)


## Quick Run
First of all, Click on [<kbd>Use this template</kbd>](https://github.com/LightricksResearch/empty-project-template/generate)
to create a repository from this template. Choose a name that explains your project.

### Run on your local machine
#### Clone
Make sure you have a version of python 3.6-3.8
1. Setup Lightricks Pypi:
* Add the following to `~/.pip/pip.conf` (you probably need to create the file and .pip dir):

```
[global]
extra-index-url = https://artifactory.lightricks.com/artifactory/api/pypi/pypi-local/simple
trusted-host = artifactory.lightricks.com
index = https://artifactory.lightricks.com/artifactory/api/pypi/pypi-local/simple
```

* Append to `~/.netrc` (a file with no extension, also may be new). Replace the password in the end with the one found in `artifactory-pypi-reader` in the 1pass shared vault `R&D-Research`:

```
machine artifactory.lightricks.com
   login pypi-reader
   password {secret-password}
```

You can use this command to do it :

 `printf "\nmachine artifactory.lightricks.com login pypi-reader password {secret-password}\n" >> $HOME/.netrc`

Make sure to replace the {secret-password} with the password from 1pass.

2. If you don't have `git-lfs` then install it first by running:
```bash
brew install git-lfs
git lfs install
```
- Note: In this repo git-lfs is set by default for many large files you might want to use such as `*.hdf5`, `*.mlmodel`, `*.nnmodel`, `*.zip` [see .gitattributes](.gitattributes)

3. Clone the project
```bash
git clone https://github.com/LightricksResearch/{your_project}

```
4. Rename the package "my_project_name" to the name of your project/package.
#### Venv

Create a new virtual environment for your project:
```bash
cd {your-project}
pip install virtualenv
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
```


#### Wandb
If you haven't signed up to Wandb, please ask your TL to sign you up

You will need to [setup W&B](https://docs.wandb.ai/quickstart) (if you haven't already):
```bash
pip install wandb
wandb login
```
and enter an API key from https://wandb.ai/settings.

Then run `wandb init`, this will ask you for the name of the project and the owner, but we will set those in the `config.yaml` (so just type something).

You'll also need to add the API key as a secret in your cnvrg Project->Secrets. If you're using remote debugging with PyCharm, add the API key as an environment variable also to the run configuration in PyCharm.



#### Black
LT research uses [Black](https://github.com/psf/black) as the code formatter. Your project should use black as well.
your code should be formatted by black at all times. There are a few easy ways to do so:
1. using a pre-commit hook. Run `pre-commit install` to setup black to run before every commit (you should have `pre-commit` installed from the requirements).
1. [integrate with IDE](https://github.com/psf/black/blob/master/docs/editor_integration.md)
1. run `black .` manually.

 All options will use the [pyproject.toml](pyproject.toml) configuration file so that black will use the correct configuration.

# Contribution
If you are planning to contribute back bug-fixes, please do so without any further discussion.
If you plan to contribute new features, utility functions, please first open an issue and discuss the feature with us.

* Please read the [PR Guidelines](https://docs.google.com/document/d/1Zjt65yk1DtSJoAymA8sDZpWJmUCFAAjwgDpZ2UdNxYw/edit#)
before opening a PR.
* Make sure you added inline documentation where required, have pytests, updates CHANGELOG.md (unreleased), updated README.md if needed
* Please run the pre-commit hooks before committing `pre-commit run --all-files`
* If it is not a fix then the PR should normally be into the next version dev branch
