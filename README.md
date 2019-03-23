# pibooth
My own implementation of a photo booth with a raspberry-pi

## What does it do?
* Trigger on a button press
* Countdown
* Flash
* Taking a picture
* Print it with a small thermal printer
* Upload to an FTP server


## How to install?
```
# Clone this repo
git clone https://github.com/antoinehng/pibooth

# Make it the active directory
cd pibooth

# Install the dependencies
make install
```

_Warning: use python 2.7: adafruit library not compatible in 3.5_


## How to run?
```
make start
```

_More details on the hardware setup soon_