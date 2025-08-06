## [LEGAL DISCLAIMER]
The usage of this keylogger project for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. The developers behind the project assume no liability and are not responsible for any misuse or damage caused by this program.

## Requirements for Infected Client
- a computer running Windows 10+
- Python 3+ with requests/pynput/datetime modules installed
- 1MB+ space

## How to Use
1. Set up a credential server with valid Pastebin credentials so clients can post logs to Pastebin
2. Set up a keylogger update server so clients can update
3. Set up a KMS (Keylogger Metadata Server), changing device IDs and/or settings if needed
4. Plug in the URLs into the source code and upload the code to the keylogger update server.
5. Wait for the "servers" to be moderated, if needed.
6. Install the keylogger to %AppData%\Microsoft\Windows\Start Menu\Programs\Startup\startup.pyw!
That's it! Manipulate the KMS to take over your client's keystroke data, *fully*.

## What are the directories for?
./installer/ has defunct examples of how to inject the keylogger into a user's startup folder.</br>
./kms/ has documentation on how to operate a Keylogger Metadata Server.</br>
./releases/ has previous versions of the keylogger. The Pastebin links present in these releases are defunct and will not work anymore.</br>
./tools/ has tools which can supplement the use of the keylogger.
- For example, logDownloader can download logs directly from Pastebin and logReader can read those logs.