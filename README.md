# Mypy demonstration

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

## 2. Activate your virtual enviroment

On Windows run:
```
.\venv\Scripts\activate
```

On Unix or MacOS run:
```
source ./my-first-venv/bin/activate
```

## 3. Install the required dependencies

```
pip install -r requirements.txt
```

## 4. Run mypy

Look for errors in the second example without executing it:

```
mypy ./samples/second_example.py
```

## 5. More information
For further research, make sure to read [Mypy documentation](https://mypy.readthedocs.io/en/stable/introduction.html).
