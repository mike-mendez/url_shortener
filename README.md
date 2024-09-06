# URL Shortening Service

A URL Shortener API that helps shorten long URLs. Using Python & FastAPI.

## Requirements

### Install Python & SQLite

#### macOS (using Homebreww)

Use the following command: ```brew install python sqlite```.
Verify with:

```bash
python3 --version
sqlite3 --version
```

#### Windows (using winget)

Use the following command: ```winget install Python.Python.3```. Verify with ```python --version```

#### Linux

##### Ubuntu/Debian

Use the following command: ```sudo apt update && sudo apt install python3 sqlite3```.

##### Fedora

Use the following command: ```sudo dnf check-update && sudo dnf install python3 sqlite```.

##### Arch Linux

Use the following command: ```sudo pacman -Syu python sqlite```.

Verify all with:

```bash
python --version
sqlite3 --version
```

## Clone Repository & Setup venv

Clone the repository with:

```bash
git@github.com:mike-mendez/url_shortener.git
```

OR

```bash
https://github.com/mike-mendez/url_shortener.git
```

```cd``` into the url_shortener directory then create and activate a virtual environment:

### macOS & Linux

```bash
cd url_shortener
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
cd url_shortener
python -m venv venv
venv/Scripts/activate
```

## Install Necessary Packages

Install all packages with the following:

### macOS & Linux

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Alembic Migration

Use the following commands to setup an initial alembic migration:

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Start Server

Run server with: ```fastapi dev app.py```

Root: <http://127.0.0.1:8000>
Documentation: <http://127.0.0.1:8000/docs> or <http://127.0.0.1:8000/redoc>
