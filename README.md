# Paycon Task [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

## Installation guide

### 1. Install system dependencies:
```shell
sudo apt-get install -y libgirepository1.0-dev build-essential \
  libbz2-dev libreadline-dev libssl-dev zlib1g-dev libsqlite3-dev wget \
  curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libcairo2-dev \
  libffi-dev python3.11-dev
```
### 2. Install Python dependencies (Poetry 1.5.0 and higher):
```shell
poetry install
```
### 3. Run:
```shell
poetry run python main.py
```

## The easiest way to run
```shell
sudo bash easy_run.sh
```
