import requests


def check_server_status(url):
    """Function for checking server status."""
    request_response = requests.head(url)
    status_code = request_response.status_code
    if status_code == 200:
        return True
    else:
        return False


print(check_server_status("https://www.example.com"))
