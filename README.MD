# Music Related

#Precomplie project dependencies
Python 3.5 >
Pip3 (should be installed with python)
virtualenv (a pip package) (to install on windows http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)

# Set up dev environment on local machine on Linux/Mac OS X
Clone the project and cd into project
```bash
unizip package
open terminal
cd into directory
```
Set up your python virtual environment
```bash
virtualenv -p python3 [name_of_virtualenv]
source [name_of_virtualenv]/bin/activate

# go into project directory
cd music_related
pip3 -R install requirements.txt
python3 manage.py runserver

# create a new microservice 
python manage.py startapp [app_name]