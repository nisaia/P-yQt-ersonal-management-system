# Personal book library

A simple CRUD desktop application for managing books. It'developed with PyQt, a set of Python bindings for [The Qt Company's](https://www.qt.io/) Qt application framework and runs on all platforms supported by Qt including Windows, macOS, Linux, iOS and Android.

For more informations, check the link -> [here](https://riverbankcomputing.com/software/pyqt)

## Installation

1. Clone the repo:

```bash
git clone https://github.com/nisaia/Personal-library.git your-project-name
```
2. Enter into project folder and create a virtual enviroment:

```bash
python3 -m venv virtual_enviroment
```

3. Once the virtual enviroment is created, activate it:

```bash
. virtual_enviroment/bin/activate
```

4. Now the dependencies must be installed from **requirements.txt**:

```bash
pip install -r requirements.txt
```

5. Enter into python console and create the database engine:

```bash
>>> from database.db import create_database
>>> create_database()
```

## Usage

```bash
python run.py
```

Enjoy

## License
[MIT](https://choosealicense.com/licenses/mit/)