# Mentoring manager platform # 

Dependencies:

* Django V.?
* Python2.7
* VirtualEnv

##How to install##

### Ubuntu ###
**Setup virtualenv**
It is used for creating an isolated environment of programming. 
More info in [Python.org](https://pypi.python.org/pypi/virtualenv).

```$
sudo easy_install virtualenv
```

```$
cd ~/.virtualenvs
```

```$
virtualenv --no-site-packages -p python2.7 mentoring_manager
```

```$
source ~/.virtualenvs/mentoring_manager/bin/activate
```

```$
pip install Django
```

```$
pip install south
```

```$
pip install pil
```

##How to run##

Load the virtualenv if haven't done it yet with: 

```$
source ~/.virtualenvs/mentoring_manager/bin/activate
```

You are then ready for running the project.

```$
cd mentoring_manager
``` 

```$
python manage.py runserver
```
