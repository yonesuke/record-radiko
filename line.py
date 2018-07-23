import requests
import Lconfig

def main():
    url = "https://notify-api.line.me/api/notify"
    token = Lconfig.APItoken
    headers = {"Authorization" : "Bearer "+ token}

    message =  'ここにメッセージを入れます'
    payload = {"message" :  message}
    files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。

    r = requests.post(url ,headers = headers ,params=payload, files=files)
    
if __name__ == '__main__':
    main()