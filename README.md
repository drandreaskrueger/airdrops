## BTX balance check

### clone repo
```
git clone https://github.com/drandreaskrueger/airdrops
cd airdrops
```

### virtualenv, dependencies
Using `virtualenv` to keep package installations `requests lxml click` local, not to change your host system much (Can be easily undone by simply deleting the `env` folder). `pip` is the python package manager:
```
sudo apt-get install python-pip
sudo pip install virtualenv

virtualenv -p python3 env/py3
source ./env/py3/bin/activate

pip install lxml requests click
```

### run
when no parameter given, it falls back to reading in file `addresses.txt` in current folder.  Try these:
```
python3 BTXbalanceCheck.py
python3 BTXbalanceCheck.py --file addresses.txt
python3 BTXbalanceCheck.py --address 1NiNja1bUmhSoTXozBRBEtR8LeF9TGbZBN
python3 BTXbalanceCheck.py --help
```

## donationware
```
BTC  13EFsVvaFa61BKUZAd5Me8XZFZNpeV3L5M
BTX  
```