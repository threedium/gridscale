
## To get the Virtual Environment
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper

## virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

## Create Working Virtual Environment
mkvirtualenv gridscale -p python3

## Export Virtual Environment to .bashrc
`env -i bash -c 'export WORKON_HOME=~/.virtualenvs && source /usr/local/bin/virtualenvwrapper.sh`

## Start the Virtual Environment
workon gridscale

## Install Python Modules from File
pip install -r requirements.txt

## Start the Development/Production Server
python run.py
