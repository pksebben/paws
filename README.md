#Paws Your Game

##Users
Why are you even here?  *How* are you even here?  This is a closed repo.  Go on, get.  Vamoose.  There's nothing for you here.

##Developers

###Running a development server
Before doing either of these, you gotta pull the repo.


####Via Python (Recommended; more straightforward)
This runs app.py through Python3

1. [Install Python3](https://www.python.org/downloads/)
2. Open a terminal and [create a venv](https://docs.python.org/3/library/venv.html)
3. [Start that venv](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments)
4. cd to pyg/python/pyg/web/
5. do this: `python3 app.py`
6. It will bitch about some stuff missing. `pip install` whatever it says is missing.
7. `python3 app.py` again.  If it bitches, see #6, if not, the site should be live at [localhost:8080](localhost:8080)

####Via Pantsbuild (fewer things to install, **way** more to mess with while developing)
This will generate an executable .pex file that can be run from anywhere without installing dependencies.
Note: you will have to run  `./pants binary python/pyg/web:app` *every time* you make changes to the code, so this route is fairly slow.  Also; if you make a new file or use a new package, you'll have to add it to the BUILD file.  

1. Open a terminal (like bash) and cd into the project root
2. Do [this](https://www.pantsbuild.org/install.html)
3. do this: `./pants binary python/pyg/web:app`
4. do this: `./dist/app.pex`
5. The site should be live at [localhost:8080](localhost:8080)
