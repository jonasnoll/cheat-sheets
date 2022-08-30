 # Just Pyton Things to reuse

# Venv ##################################################################################

# creates a virtualenv
python3 -m venv myVenvName


# activates the virtualenv
source myVenvName/bin/activate

# CONDA
conda create --name myVenvName python=3.7
    
conda activate myVenvName


# Venv to Jupyter Notebooks
pip install jupyter
pip install ipykernel

python -m ipykernel install --user --name=myVenvName


# pip
# "I installed a package, but I can't import it!?"
# Best fix: don't use the "pip" command, instead use "python -m pip"
# ensures package is installed into same Python you'll be running.

# Init ##################################################################################
def main():
    let_the_script_roll()

if __name__ == "__main__":
    log.info("Starting Script...")
    main()

# Class with documentation #########################################################################
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

# Logging with catching errors (COPY THIS ONE)
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
###################


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
a = random.randint(0,5)
print(a)

a = random.sample(range(795), 20)
a.sort()
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


# Plotting #############################################################################

print("https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html")

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
    # I was 100    in this case.
    # I was 1000   in this case.


########################################################################################






























