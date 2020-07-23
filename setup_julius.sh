curl -LO https://github.com/julius-speech/julius/archive/v4.5.zip
tar zxvf v4.5.zip
cd julius-4.5
./configure
make
make install
cd julius-kit
curl -LO https://osdn.net/dl/julius/dictation-kit-4.5.zip
unzip dictation-kit-4.5.zip
cd dictation-kit-4.5
