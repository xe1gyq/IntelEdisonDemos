echo
echo "Welcome to Somos Bimbo Playground"
echo

sleep 4

wget https://launchpad.net/python-weather-api/trunk/0.3.8/+download/pywapi-0.3.8.tar.gz
tar zxvf pywapi-0.3.8.tar.gz
cd pywapi-0.3.8
python setup.py build
python setup.py install
cd ..
rm -rf pywapi-0.3.8*

git clone https://github.com/xe1gyq/IntelEdisonDemos.git
cd IntelEdisonDemos/SomosBimbo

pip install pip --upgrade
sh requirements.opkg
pip install -r requirements.pip

echo
echo "Now go to IntelEdisonDemos/SomosBimbo directory to get started!"
echo
echo "Work on having your credentials ready!"
echo "credentials.config"
echo
echo "Happy SomosBimbo'ing!"
echo
