# insulin-tracker
QR insulin bottle tracker, to start a 28-day timer when removed from refrigeration and then warn if trying to use after expiry.

The user process is:
1.  Register a user to get a unique application user handle (so users don't step on each other)
2.  Print or order a set of unique custom printed QR codes, one per insulin bottle.
3.  On insulin receipt, as putting into refrigeration, affix a sticker on each bottle.
4.  When removing from refrigeration, navigate to website via camera on QR code, starting the 28 day timer
5.  When using a bottle outside of refrigeration, navigate to website via camera on QR code to see how long it's been outside of refrigeration
6.  Once expired, dispose of insulin and sticker
