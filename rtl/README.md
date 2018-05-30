# RTL helpers

## rtlswitch
script for switching between original DVB-T drivers and the osmo-sdr. Basically just loading and unloading driver modules. Supports classic RTL2382U and RTL2382P (Astrometa DVB-T2) for which it renames frontends to use built-in Panasonic DVB-T2 demodulator as default in VLC
### Enabling DVB-T:
- UNPLUG device!
- run rtlswitch -o
- PLUG IN device
- If your device is Astrometa DVB-T2 or clone, you have to rename your frontends to use it in vlc - run rtlswitch -o

### Enabling osmo-sdr:
- UNPLUG device!
- run rtlswitch -r
- PLUG in device!
