# Mypy demonstration

Run the following instructions in your terminal to ensure the provided [examples](https://github.com/ins4w/static-typing-python3/tree/main/samples) run as expected.

## 1. Create a Python virtual enviroment 
On windows:
```
python -m venv my-first-venv
```

On Unix, GNU/Linux and MacOS:
```
python3 -m venv my-first-venv
```

## 2. Activate your virtual enviroment

On Windows run:
```
.\venv\Scripts\activate
```

On Unix, GNU/Linux and MacOS:
```
source ./my-first-venv/bin/activate
```

## 3. Install the required dependencies

```
pip install -r requirements.txt
```

## 4. Use Mypy

Look for errors in the [file](https://github.com/ins4w/static-typing-python3/blob/main/samples/second_example.py) where we used data types without executing it:

```
mypy ./samples/second_example.py
```

## 5. More information
For further research, make sure to read [Mypy documentation](https://mypy.readthedocs.io/en/stable/introduction.html).
