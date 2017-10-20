# how (and why) to compile `bitcore-qt` on Debian stretch

# folder & download & unpack
mkdir BitCore; cd BitCore
wget https://github.com/LIMXTEC/BitCore/releases/download/0.14.1.6/Linux-0-14-1-6.tar.gz
tar xzvf Linux-0-14-1-6.tar.gz
rm Linux-0-14-1-6.tar.gz

# now you try the binaries in `./bin`. but in my case, sadly, I get an error 
# (libboost_system.so.1.58.0: cannot open shared object file)
# so let's compile it ourselves:
  
unzip source/BitCore-master\(1\).zip
rm source/BitCore-master\(1\).zip
cd BitCore-master

sudo apt-get install libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev libboost-all-dev
sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools libprotobuf-dev protobuf-compiler

sudo apt install libdb5.3++ libdb5.3++-dev libevent-dev

./autogen.sh 
./configure --with-incompatible-bdb

make
sudo make install

bitcore-qt --version
bitcore-qt --help
bitcore-qt