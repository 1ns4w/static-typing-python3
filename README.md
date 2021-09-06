# static-typing-python

Run the following instructions in your terminal to ensure the examples run as expected.

## 1. Create a virtual enviroment 
On windows:
```
python -m venv my-first-venv
```

On Unix, GNU/Linux and MacOS:
```
python3 -m venv my-first-venv
```

## 2. Create a .gitignore file and add your virtual enviroment to it

```
echo /venv > .gitignore
```   

## 3. Activate your virtual enviroment

On Windows run:
```
.\venv\Scripts\activate
```

On Unix or MacOS run:
```
source ./my-first-venv/bin/activate
```

## 4. Install the required dependencies

```
pip install -r requirements.txt
```

## 5. Try mypy

Run any of the samples and make sure to use static typing from now on!
```

mypy first_example.py
```

```
mypy second_example.py
```
