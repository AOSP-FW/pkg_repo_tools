import requests

class MyRequest:

    PROXY_SOCKET = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
    ANDROID_GOOGLESOURCE = "https://android.googlesource.com"

    @classmethod
    def get(cls, url):
        return requests.get(f"{cls.ANDROID_GOOGLESOURCE}/{url}", proxies=cls.PROXY_SOCKET)