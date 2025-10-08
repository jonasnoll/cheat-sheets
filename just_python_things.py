 # Just Pyton Things to reuse

# Venv #########################################################################################

# Show Available Python Versions 
pyenv versions

# Install new version
pyenv install 3.12.0

# Create venv at root of the project
pyenv virtualenv 3.12.0 myprojectvenv

# Activate 
pyenv local myprojectvenv

# Delete Venv
pyenv virtualenv-delete myprojectvenv




###### My Legacy Way ######
# creates a virtualenv
python3.10 -m venv myVenvName


# activates the virtualenv
source webapp-demo-pip/bin/activate

# CONDA
conda create --name myVenvName python=3.8
conda create --name asdf python=3.12

# Remove Conda Env
conda remove --name ENV_NAME --all

# Freeze Conda Environment for pip without weird references
pip list --format=freeze > requirements.txt


# Venv to Jupyter Notebooks
pip install ipykernel 
# pip install jupyter ipykernel

python -m ipykernel install --user --name=myVenvName


# pip
pip install -r requirements.txt

# "I installed a package, but I can't import it!?"
# Best fix: don't use the "pip" command, instead use 
python -m pip install PACKAGE
# ensures package is installed into same Python you'll be running.
# -m steht für module (also das python in dem venv)


# Ad folder to github project ##################################################################

git init

# eg. git@github.com:jonasnoll/funneldemo.git
git remote add origin <Repository_Location>

# Checkout on the branch 
git branch -M main

# Add gitignore 
touch .gitignore

# Add files 
git add . 

# Initial commit 
git commit -m "Initial commit"

# Push to main for github (should be master with gitlab)
git push -u origin main



# Init #########################################################################################
def main():
    let_the_script_roll()

if __name__ == "__main__":
    # print("Starting...\n")
    log.info("Starting Script...")
    main()

# Hot-Releoad Notebook #########################################################################

import sys 

sys.path.append('/Users/jonasnoll/Devprojects/analysis/bp-prod-data-analysis')
%load_ext autoreload
%autoreload 2


# Class with documentation ######################################################################
class Dog():
	"""
    A class used to represent a Dog.

    Attributes
    ----------
    name : str
        the name of the dog
    breed : str
        the breed of the dog

    Methods 
    -------
    bark_name()
        Prints the dog's name with a sound indicator
    """

	species = 'mammal' # Class Object Attributes (regardless)

	def __init__(self, name, breed='Default Value'):
		self.name = name
		self.breed = breed

	def bark_name(self, sound=None):
		"""Prints the dog's name with a sound indicator.

        If the argument `name` isn't passed in, the default dog name is used.

        Parameters
        ----------
        sound : str, optional
            The sound the dog makes (default is None). Usually, "Angry Barking", ...
        """
		return f"{sound}: Wuff {self.name} wuff!"

dog1 = Dog('Rektus', 'Ridgeback')

print(dog1.name)
print(dog1.breed)
print(dog1.bark_name())

# Class Inheritance #####################################################################
class Puppy(Dog):

	def __init__(self, name):
		Dog.__init__(self, name)
		print("Puppy Created")

puppy1 = Puppy('Rex')


# Pydantic Data Model #####################################################################
from pydantic import BaseModel

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


# Timing things #########################################################################
import time

t0 = time.time()
#code_block
t1 = time.time()

total = t1-t0

# Current Date ##########################################################################
import datetime as dt

# time now
date = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
# today
date = dt.date.today().strftime("%d.%m.%Y")
# tomorrow
date = dt.date.today() + dt.timedelta(days=1)
date = date.strftime("%d.%m.%Y") 
# or just (dt.date.today() + dt.timedelta(days=1)).strftime("%d.%m.%Y")

# Format Date in f-String

f'The date is {date:%A, %B %d, %Y}.'


# Get datetime from unix timestamp (s or ms) ############################################

from datetime import datetime

ts = int('1671023926000')

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


# Logging ###############################################################################

import logging

log = logging.getLogger(__name__)
logging.basicConfig( 
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log.info("This is a logging message")

# Loggin to file
logname = "./log"
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG) # level is minimum message level it will accept

# Logging with catching errors 
###### Logging #####
import sys
import logging
log_filename = "myLog"
logger = logging.getLogger(__name__)
logging.basicConfig(filename=f"./logs/log_{log_filename}.log",
                                    filemode='a',
                                    format="%(asctime)s.%(msecs)03d - %(filename)s - %(levelname)s: %(message)s",
                                    datefmt="%Y-%m-%d %H:%M:%S",
                                    level=logging.DEBUG)
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception

################### (COPY THIS ONE !!!)

import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# from utils.utils import create_directory

LOG_FILE_NAME = 'debug_logs.log'

class Log():
    def __init__(self, name, logfile="mylog.log", stdout=True):
        """Custom Logging Class for Logging in a log file"""
        assert logfile.split('.')[-1] == 'log', "Ivalid log-file extension. Must be .log"

        name = __name__ if name == 'module' else name

        # Get logfile path
        current_directory = os.path.dirname(os.path.abspath(sys.argv[0])) 
        logfile = os.path.join(current_directory, 'logs/', logfile)
        
        self.logfile = logfile
        self.logger = logging.getLogger(name)

        # Create directory for placing the files
        self.create_log_directory(logfile)

        # Set Logginf Format
        log_format = logging.Formatter(
            "%(asctime)s.%(msecs)03d - %(filename)s (%(name)s) - %(levelname)s: %(message)s"
        )

        # Log to Std Out Handler
        stdoutHandler = logging.StreamHandler(stream=sys.stdout)
        stdoutHandler.setLevel(logging.INFO)
        stdoutHandler.setFormatter(log_format)

        # Log to File Handler
        # fileHandler = logging.FileHandler(self.logfile)
        fileHandler = RotatingFileHandler(self.logfile, backupCount=10, maxBytes=5000000) # Handles to large
        fileHandler.setLevel(logging.INFO)
        fileHandler. setFormatter(log_format)

        # Add handlers
        if stdout:
            self.logger.addHandler(stdoutHandler)
        self.logger.addHandler(fileHandler)

        # Set level of logger again because the levels of the handlers dont propagate
        self.logger.setLevel(logging.INFO)

        sys.excepthook = self.handle_exception


    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        self.logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


    def create_log_directory(self, logfile):
        # Get parent directory of the logfile
        parent_dir = os.path.dirname(logfile)
        # Resolve the relative path to an absolute path
        # Check if the directory exists, and create it if it does not
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
            self.logger.info(f"Directory '{parent_dir}' created.")
        else:
            self.logger.info(f"Directory '{parent_dir}' already exists.")



# dash_logger = Log(name="dash.dash", logfile=LOG_FILE_NAME, stdout=False).logger
logger = Log(name="module", logfile=LOG_FILE_NAME).logger

###################3
    
# Make a request ########################################################################

# get request / post request
import requests
 
url = "https://httpbin.org/get"
 
headers = {"Content-Type": "application/json; charset=utf-8"}
# headers = {"Authorization": f"Bearer xxxxxxxx"}
 
params = {
    "id": 1001,
    "name": "geek",
    "passion": "coding",
}

# OR
# params = dict(
#     id=1001,
#     name="geek",
#     passion="coding",
# )
 
response = requests.get(url, headers=headers, params=params)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())




# Check for Type / is type or Check for Attr / is attr ################################

# Type
if isinstance(o, str):
    print(True)

# Attr
if hasattr(a, 'property'):
    a.property


# Try Except ###########################################################################

try:
  print(x)
except:
  print("An exception occurred")
finally:
	print("I'm saying this regardless")
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Random Numbers / within Range #########################################################

import random

random.seed(10)

a = random.randint(0,5)
print(a)

a = random.sample(range(795), 20)
a.sort()
print(a)


# taking random samples from list
mylist = [2, 2, 4, 6, 6, 8]
 n = 4
 a = random.sample(mylist, n)
 print(a)

# Inline Expression / Variable Assignment ###############################################

expression_if_true if condition else expression_if_false
a = 1 if condition else 2

# Inline List / List Comprehension ######################################################

inline_list = [f(x) for x in full_list if condition] 

# Double Loop
seq_x = [1, 2, 3, 4]
seq_y = 'abc'
[(x,y) for x in seq_x for y in seq_y] # [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), ...]

# Flatten / Given a list of list ll
flat_list = [item for sublist in ll for item in sublist]

# Inline Dict / Dict Comprehension ######################################################

square_dict = {num: f(num) for num in range(1, 11)}

# List files with glob ##################################################################
import glob

dirs = glob.glob("/home/azureuser/ml-sandbox/**/", recursive=True)
file_paths = glob.glob("/path/to/dir/*.png", recursive=True)
for path in dirs:
    print(path)

# Alternative 
yaml_files = glob.glob(os.path.join(os.path.abspath('app_configs/'), '*.yaml'))



# Plotting #############################################################################

s = "see just ds things"


# Matplot make custom axis labels #######################################################

# Eg for spectrograms

def get_plt_time_axis_labels(axis_size, n_places, t_start, t_end, timeline):
    axis_range = [i for i in range(axis_size)]
    # Get Axis array
    timeline = timeline[::axis_size]
    time_axis = timeline[t_start:t_end]

    ax_places = [int(axis_size/n_places*i) for i in range(n_places)] + [axis_size-1]
    locator_axis = [f"{time_axis[i]:.9f}" if i in ax_places else None for i in range(axis_size)]

    # print(ax_labels)

    return axis_range, locator_axis

x_range, labels = get_plt_freq_axis_labels(axis_size=num_pix, n_places=4, axis_limit=signal_obj.bandwidth_in_MHz, ax_centered=True)
plt.xticks(x_range, labels, rotation='horizontal')


# tmux #################################################################################

"""
# Create new session
$ tmux new -s MySessionName

# Rename session
$ tmux rename-session -t 0 git

# List all running session (detached or not)
$ tmux ls

# Kill a session
$ tmux kill-session -t MySessionName

# Detach a session
ctrl + b --> d

# Attach a session
$ tmux attach -t MySessionName

"""

# Print f-strings with spacing #########################################################

# Cut Decimals
n = 96.902234234234
print(f"{a:.2f}")
# '96.90'
print(f"{a:.3f}")
# '96.902'


# Padding string from left
for i in [1, 10, 100, 1000]:
    print(f"I was {i:>6} in this case.")
    # prints
    # I was      1 in this case.
    # I was     10 in this case.
    # I was    100 in this case.
    # I was   1000 in this case.

    print(f"I was {i:<6} in this case.")
    # I was 1      in this case.
    # I was 10     in this case.
    # I was 100    in this case.3
    # I was 1000   in this case.


# Fill with zeros for numbering 
txt = "50"
x = txt.zfill(3)

print(x) # 050


# Pyinstaller ######################################################################

# https://realpython.com/pyinstaller-python/

# 1. Create main file on top level to run app







########################################################################################































