# Python Programming Language

#### [PEP8](00_pep8.py)
#### [Basics](01_basics.py)
#### [Strings](02_strings.py)
#### [Control Flow](03_control_flow.py)
#### [Try Except](04_try_except.py)
#### [Lists](05_lists.py)
#### [List Comprehension](06_list_comprehension.py)
#### [Sets](07_sets.py)
#### [Tuples](08_tuples.py)
#### [Dictionary](09_dictionary.py)
#### [Namespaces](10_namespaces.py)
#### [Functions](11_functions.py)
#### [Type Hinting](12_type_hinting.py)
#### [Lambda Functions](13_lambda_functions.py)
#### [User Input](14_user_input.py)
#### [Files](15_files.py)
#### [Parsing Data](16_parsing_data.py)
#### [Decorators](17_decorators.py)
#### [Generators](18_generators.py)
#### [Class](19_classes.py)
#### [Modules](20_modules.py)
#### [Name_Main 1](name_main_1.py)
#### [Name_Main 2](name_main_2.py)


### *venv naming convention:* 
`my_project_venv`

### *create venv with python 3:*
`python3 -m venv <NAME_OF_ENVIRONMENT>`

### *activate venv:*
`source <VENV_DIR>/bin/activate`

# check correct python is being used
which python or pip

# In venv use python and pip without the 3
python and pip

# deactivate venv
deactivate

# create requirements.txt
pip freeze > requirements.txt

# install requirements.txt
pip install -r requirements.txt

# pip uninstall all packages(make requirements.txt file first)
pip uninstall -y -r <(pip freeze)  # doesn't make file just removes

# show installed and not their dependencies
pip list --not-required

# show package dependencies
pip show package_name

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
sys.path.append(dir_path)

######################################
# ~~~~~~~~~~~~~ Python ~~~~~~~~~~~~~ #
######################################


####################################
# ~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~ #
####################################

# set app name in terminal
set FLASK_APP=app_name.py # Windows
export FLASK_APP=app_name.py # Mac/Linux

# set debug
set FLASK_DEBUG=1 # Windows
export FLASK_DEBUG=1 # Mac/Linux

# run Flask
flask run

# run app with debug in "if name main"
python app.py

####################################
# ~~~~~~~~~~~~ Flask ~~~~~~~~~~~~~ #
####################################
