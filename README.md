# Paycon Task [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

### 1. Install system dependencies:
```shell
sudo apt-get install -y python3-venv python3-wheel python3-dev
sudo apt-get install -y libgirepository1.0-dev build-essential \
  libbz2-dev libreadline-dev libssl-dev zlib1g-dev libsqlite3-dev wget \
  curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libcairo2-dev
```

[//]: # (### 1. Create .env file with variables below:)

[//]: # (```dotenv)

[//]: # (BASE_URL=https://www.rusal.ru/suppliers/selection/)

[//]: # (PARAMS=?q=&selection%5B%5D=current&section=ALL&region%5B%5D=ALL&region%5B%5D=50948&region%5B%5D=50924&region%5B%5D=50920&region%5B%5D=50917&region%5B%5D=50919&region%5B%5D=50952&region%5B%5D=50943&region%5B%5D=50947&region%5B%5D=50937&region%5B%5D=50938&region%5B%5D=50934&region%5B%5D=50936&region%5B%5D=50944&region%5B%5D=50921&region%5B%5D=50916&region%5B%5D=50922&region%5B%5D=50929&region%5B%5D=50931&region%5B%5D=50942&region%5B%5D=111342&region%5B%5D=50918&region%5B%5D=111889&region%5B%5D=50950&region%5B%5D=50923&region%5B%5D=50927&region%5B%5D=50925&region%5B%5D=50932&region%5B%5D=51296&region%5B%5D=50928&region%5B%5D=50946&region%5B%5D=50945&region%5B%5D=50951&region%5B%5D=50926&region%5B%5D=50930&region%5B%5D=50933&region%5B%5D=50940&region%5B%5D=50935&region%5B%5D=50939&region%5B%5D=111686&region%5B%5D=50941&region%5B%5D=50915&region%5B%5D=50949&client%5B%5D=ALL&client%5B%5D=50968&client%5B%5D=50959&client%5B%5D=50967&client%5B%5D=50972&client%5B%5D=50965&client%5B%5D=50980&client%5B%5D=50981&client%5B%5D=50986&client%5B%5D=50996&client%5B%5D=50997&client%5B%5D=106661&client%5B%5D=50987&client%5B%5D=50991&client%5B%5D=77338&client%5B%5D=50969&client%5B%5D=50995&client%5B%5D=51001&client%5B%5D=111343&client%5B%5D=50955&client%5B%5D=50957&client%5B%5D=51002&client%5B%5D=50974&client%5B%5D=50999&client%5B%5D=50979&client%5B%5D=50982&client%5B%5D=50984&client%5B%5D=50985&client%5B%5D=51003&client%5B%5D=111685&client%5B%5D=50976&client%5B%5D=50975&client%5B%5D=54174&client%5B%5D=50954&client%5B%5D=50970&client%5B%5D=50992&client%5B%5D=50956&client%5B%5D=50964&client%5B%5D=50961&client%5B%5D=50966&client%5B%5D=50978&client%5B%5D=51000&client%5B%5D=51004&client%5B%5D=94520&client%5B%5D=56088&client%5B%5D=51459&client%5B%5D=55917&client%5B%5D=70759&client%5B%5D=56992&client%5B%5D=107874&client%5B%5D=111367&client%5B%5D=94450&client%5B%5D=111890&client%5B%5D=50962&client%5B%5D=50989&client%5B%5D=61931&client%5B%5D=51534&client%5B%5D=51549&client%5B%5D=51005&client%5B%5D=51006&client%5B%5D=50988&client%5B%5D=50963&client%5B%5D=51201&client%5B%5D=53184&client%5B%5D=94521&client%5B%5D=93536&client%5B%5D=51007&client%5B%5D=53239&client%5B%5D=92708&client%5B%5D=94283&client%5B%5D=111687&client%5B%5D=68021&client%5B%5D=50994&client%5B%5D=111688&client%5B%5D=51008&client%5B%5D=94818&client%5B%5D=61940&client%5B%5D=51297&client%5B%5D=94519&client%5B%5D=50958&client%5B%5D=50971&client%5B%5D=50998&client%5B%5D=50977&client%5B%5D=51010&client%5B%5D=51009&client%5B%5D=50983&apply_filter=Y)

[//]: # (ACCEPT=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7)

[//]: # (USER_AGENT=Mozilla/5.0 &#40;iPhone; CPU iPhone OS 13_2_3 like Mac OS X&#41; AppleWebKit/605.1.15 &#40;KHTML, like Gecko&#41; Version/13.0.3 Mobile/15E148 Safari/604.1)

[//]: # (```)

[//]: # ()
[//]: # (### 2. Install [Poetry]&#40;https://python-poetry.org&#41;)

[//]: # ()
[//]: # (### 3. Install dependencies:)

[//]: # (```shell)

[//]: # (poetry install)

[//]: # (```)

[//]: # ()
[//]: # (### 4. Run:)

[//]: # (```shell)

[//]: # (poetry run python main.py)

[//]: # (```)

[//]: # ()
[//]: # ()
[//]: # (## Development [![Python 3.11]&#40;https://img.shields.io/badge/python-3.11-blue.svg&#41;]&#40;https://www.python.org/downloads/release/python-311/&#41;)

[//]: # ()
[//]: # (### 1. Create .env file with variables below:)

[//]: # (```dotenv)

[//]: # (BASE_URL=https://www.rusal.ru/suppliers/selection/)

[//]: # (PARAMS=?q=&selection%5B%5D=current&section=ALL&region%5B%5D=ALL&region%5B%5D=50948&region%5B%5D=50924&region%5B%5D=50920&region%5B%5D=50917&region%5B%5D=50919&region%5B%5D=50952&region%5B%5D=50943&region%5B%5D=50947&region%5B%5D=50937&region%5B%5D=50938&region%5B%5D=50934&region%5B%5D=50936&region%5B%5D=50944&region%5B%5D=50921&region%5B%5D=50916&region%5B%5D=50922&region%5B%5D=50929&region%5B%5D=50931&region%5B%5D=50942&region%5B%5D=111342&region%5B%5D=50918&region%5B%5D=111889&region%5B%5D=50950&region%5B%5D=50923&region%5B%5D=50927&region%5B%5D=50925&region%5B%5D=50932&region%5B%5D=51296&region%5B%5D=50928&region%5B%5D=50946&region%5B%5D=50945&region%5B%5D=50951&region%5B%5D=50926&region%5B%5D=50930&region%5B%5D=50933&region%5B%5D=50940&region%5B%5D=50935&region%5B%5D=50939&region%5B%5D=111686&region%5B%5D=50941&region%5B%5D=50915&region%5B%5D=50949&client%5B%5D=ALL&client%5B%5D=50968&client%5B%5D=50959&client%5B%5D=50967&client%5B%5D=50972&client%5B%5D=50965&client%5B%5D=50980&client%5B%5D=50981&client%5B%5D=50986&client%5B%5D=50996&client%5B%5D=50997&client%5B%5D=106661&client%5B%5D=50987&client%5B%5D=50991&client%5B%5D=77338&client%5B%5D=50969&client%5B%5D=50995&client%5B%5D=51001&client%5B%5D=111343&client%5B%5D=50955&client%5B%5D=50957&client%5B%5D=51002&client%5B%5D=50974&client%5B%5D=50999&client%5B%5D=50979&client%5B%5D=50982&client%5B%5D=50984&client%5B%5D=50985&client%5B%5D=51003&client%5B%5D=111685&client%5B%5D=50976&client%5B%5D=50975&client%5B%5D=54174&client%5B%5D=50954&client%5B%5D=50970&client%5B%5D=50992&client%5B%5D=50956&client%5B%5D=50964&client%5B%5D=50961&client%5B%5D=50966&client%5B%5D=50978&client%5B%5D=51000&client%5B%5D=51004&client%5B%5D=94520&client%5B%5D=56088&client%5B%5D=51459&client%5B%5D=55917&client%5B%5D=70759&client%5B%5D=56992&client%5B%5D=107874&client%5B%5D=111367&client%5B%5D=94450&client%5B%5D=111890&client%5B%5D=50962&client%5B%5D=50989&client%5B%5D=61931&client%5B%5D=51534&client%5B%5D=51549&client%5B%5D=51005&client%5B%5D=51006&client%5B%5D=50988&client%5B%5D=50963&client%5B%5D=51201&client%5B%5D=53184&client%5B%5D=94521&client%5B%5D=93536&client%5B%5D=51007&client%5B%5D=53239&client%5B%5D=92708&client%5B%5D=94283&client%5B%5D=111687&client%5B%5D=68021&client%5B%5D=50994&client%5B%5D=111688&client%5B%5D=51008&client%5B%5D=94818&client%5B%5D=61940&client%5B%5D=51297&client%5B%5D=94519&client%5B%5D=50958&client%5B%5D=50971&client%5B%5D=50998&client%5B%5D=50977&client%5B%5D=51010&client%5B%5D=51009&client%5B%5D=50983&apply_filter=Y)

[//]: # (ACCEPT=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7)

[//]: # (USER_AGENT=Mozilla/5.0 &#40;iPhone; CPU iPhone OS 13_2_3 like Mac OS X&#41; AppleWebKit/605.1.15 &#40;KHTML, like Gecko&#41; Version/13.0.3 Mobile/15E148 Safari/604.1)

[//]: # (```)

[//]: # ()
[//]: # (### 2. Install [Poetry]&#40;https://python-poetry.org&#41;)

[//]: # ()
[//]: # (### 3. Install dependencies:)

[//]: # (```shell)

[//]: # (poetry install --with development)

[//]: # (```)

[//]: # ()
[//]: # (### 5. Run:)

[//]: # (```shell)

[//]: # (poetry run python main.py)

[//]: # (```)

[//]: # ()
[//]: # (## Additions)

[//]: # (### 1. Create database schema:)

[//]: # (```shell)

[//]: # (poetry run alembic upgrade head)

[//]: # (```)
