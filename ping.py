import socket
import requests


def check_server_status(url):
    """Function for checking server status."""
    ip = socket.gethostbyname(url)
    a = requests.get(ip)
    if a == 200:
        return True
    else:
        return False


print(check_server_status("www.google.com"))
