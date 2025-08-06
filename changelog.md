[CHANGELOG]
patch 0.1: new beginnings
patch 0.2: stores keylogger and logs in a hidden folder
patch 0.3: saves logs in tiny files

patch 1: uploads logs to Pastebin (enter credentials in %userprofile%/.config/roblox/PBIN_CREDS.bin)
         uses zlib compression to shorten log filesizes
         erases most spaces in logs, therefore halving the filesize of original logs

patch 2: keylog pastes are private

patch 3: you can use a customizable fake program data path!
           format: "ExistingDir/Name1/Name2" or ExistingDirVar+"/Name1/Name2"
           Pastebin credentials should be uploaded to this new path

patch V: restored KMS functionality
         the keylogger has a less chance of crashing on the first run (import fixes)
         sending the keylog is now a function
         NOTE: THE UPDATER CODE IS BROKEN ON THIS VERSION.
               YOU WILL HAVE TO MANUALLY UPDATE THE KEYLOGGER TO THE LATEST VERSION.

2024.3.29: newly created device IDs are much shorter

2024.4.1: pastebin credentials are stored online for easier deployment
          device IDs can be changed through the KMS
          text can be sent to pastebin through the keylogger
          fixed the keylogger crashing on the KMS if an error was in the code
          keylogger updates execute on the spot instead of waiting for a restart
          keylogger updates are smarter, only updating if the code is different
          removed unused module 'sys'

2024.4.4: fixed a glitch where the keylogger would be stuck in an "update loop"

2024.4.10: fixed the updater code by making the keylogger path a definite path
           keylogger pastes are no longer privated so the reader can save logs

2024.4.11: only the autoupdate and one operating state can be chosen in the KMS
           store the keylogger server URLs to variables to change them easily

2024.4.14: added functions that allow for the change the credential and update servers
             syntax: change_credserver(ids [list], url [string]) | change_updateserver(ids [list], url [string])
             use ["*"] for the ids parameter to apply this change to all devices connected to the KMS.
             a pastebin RAW link must be used for the url parameter.

2024.4.18: if "*" is included in the autoupdate or status lists, EVERY client will have their status set to that one.
             this will replace using update() at the beginning of KMS code.
           changed function names with change_... to set...
             ex: change_credserver() -> setcredserver()

2024.4.20: version is now displayed when sending logs

2024.4.28: MANY functions are renamed to make them simpler.
             change_devid() -> changeid()
             setcredserver() -> loadcreds()
             setupdateserver() -> upd()
           the data path can now be set to ANY PATH
             the keylogger will create ANY missing paths much more efficiently
           if the internet is down, the keylogger will not crash when fetching KMS/credentials
           removed the autoupdate list in the KMS
             use update() to update all clients
             use upd([ids],update_server_url) to update specific clients/use a different update server

2024.5.9: instead of pre-setting a keylogger file, the keylogger file location is determined using __file__
            even if the keylogger isn't named a certain way, it will still be updated

2024.6.15: modules are installed with the "--upgrade" flag by default

2024.7.3: most strings with + in them have been converted to f-strings
          credential variables are deleted from memory after the keylogger starts

          ===FUNCTION UPDATES===
          some functions have arguments that already have a default value
           -> send(privacyLevel='1',title=None,text=None) sends plain text or logs
              if only privacyLevel='1' is included, a log will be sent with the 'unlisted' status.
              if only title="example",text="example" is included, plain text will be sent.
              if either title or text are not provided, a log will be sent instead.

           -> update(ids=["*"],url=update_server) updates all IDs and/or uses a different update server.
              if only url="https://updateserver.com/" is included, all IDs will be updated using the given URL.
              if only ids=["id1","id2"] is included, specific IDs will be updated using the fallback server.
              if both arguments are given, specific IDs will be updated using the given URL.
              if no arguments are given, all IDs will be updated using the default update server.

          send_text() still works as before, however the 'private' status can be overrided
          upd() has been merged into update()
          ===FUNCTION UPDATES===

          you can now paste keylogs at any Pastebin privacy level with the variable 'privacyLvl'
              privacyLvl = '0' means that logs are pasted publicly
              privacyLvl = '1' means that logs are unlisted (DEFAULT)
              privacyLvl = '2' means that logs are pasted privately
              this should be changed through the KMS

          public log pasting is now allowed
          subprocess and sys modules are added
          when downloading modules, no console window is shown
          keylogger version is no longer stored as a dictionary
          creation of data directory and device ID is optimized
          keylogging single keys is optimized
          saving/loading data from files is optimized
          request.ok is used instead of request.status_code == requests.codes.ok

DOWNLOAD the latest update from [this repo]!
Keyloggers on version v2024.4.10+ should be used for working auto-update.