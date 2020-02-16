from ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('https://github.com/peoplesdriver/ledlights.git')
    ota_updater.download_and_install_update_if_available(ssid, password)

def start():
    # code goes here ...
    import wifimgr

    wlan = wifimgr.get_connection()

    if wlan is None:
        while True:
            pass  # you shall not pass :D

    import RazLedRoom



def boot():
    download_and_install_update_if_available()
    start()


boot()
