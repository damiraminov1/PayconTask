sudo apt-get install -y libgirepository1.0-dev build-essential \
  libbz2-dev libreadline-dev libssl-dev zlib1g-dev libsqlite3-dev wget \
  curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libcairo2-dev \
  libffi-dev python3.11-dev
sudo apt install python3.11-venv
python3.11 -m venv venv
source venv/bin/activate
pip install poetry == 1.5.0
poetry install
poetry run python run