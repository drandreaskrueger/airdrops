## BTX balance check
If you want to check your hundreds of BTC addresses for an inital BTX balance (snapshot April 2017), then this little Python script helps you a lot: It automates the bitcore.cc query.  Published 20/10/2017 in [bitcointalk](https://bitcointalk.org/index.php?topic=1883902.msg23260682#msg23260682).

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
python3 BTXsnapshotCheck.py
python3 BTXsnapshotCheck.py --file addresses.txt
python3 BTXsnapshotCheck.py --address 149YssZJ63isQTG13qrv6TAD9FqMxh8KT2
python3 BTXsnapshotCheck.py --help
```

### output example
```
./BTXsnapshotCheck.py 
13EFsVvaFa61BKUZAd5Me8XZFZNpeV3L5M 0.0
149YssZJ63isQTG13qrv6TAD9FqMxh8KT2 0.05
```

### how to create such an addresses.txt inputfile from your wallet?
e.g. in electrum, open the console, then:

    print("\n".join(  listaddresses()  ))


## donationware
```
BTC  13EFsVvaFa61BKUZAd5Me8XZFZNpeV3L5M 
BTX  1JBFG6W71NzKZgDmqM7kcHUjqghcRxjQ5n
```

Thank you.
