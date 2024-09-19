import requests
import json


def check_http_https(domain_or_ip, port=80, https_port=443):
    try:
        response = requests.get(f"http://{domain_or_ip}:{port}", timeout=5)
        if response.status_code == 200:
            print(f"{domain_or_ip} accepts HTTP requests on port {port}"
                  f"\nstatus code: {response.status_code}")
        else:
            print(f"{domain_or_ip} does not accept HTTP requests on port {port}"
                  f"\n status code: {response.status_code}"
                  f"\n error: {response.text} {response.raise_for_status()}")
    except requests.ConnectionError:
        print(f"{domain_or_ip} does not accept HTTP requests on port {port}")

    try:
        response = requests.get(f"https://{domain_or_ip}:{https_port}", timeout=5, verify=False)
        if response.status_code == 200:
            print(f"{domain_or_ip} accepts HTTPS requests on port {https_port}"
                  f"\nstatus code: {response.status_code}")
        else:
            print(f"{domain_or_ip} does not accept HTTPS requests on port {https_port}"
                  f"\n status code: {response.status_code}"
                  f"\n error: {response.text} {response.raise_for_status()}")
    except requests.ConnectionError:
        print(f"{domain_or_ip} does not accept HTTPS requests on port {https_port}")


def get_from_api(api):
    try:
        response = requests.get(api, timeout=5)
        if response.status_code == 200:
            print(f"Successful GET Request! \nStatus code: {response.status_code}")
        else:
            print(f"Error getting response.")
    except requests.ConnectionError:
        print(f"Error getting response.")


def post_to_api(api, data, headers):
    try:
        json_data = json.dumps(data)
        response = requests.post(url=api, data=json_data, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"Successful Post Request! \nStatus code: {response.status_code}")
        else:
            print(f"Error getting response. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Error getting response: Connection Error.")


get_from_api('http://localhost:5000/')
post_to_api('http://localhost:5000/',{"message": "YOO!!!!"}, {"Content-Type": "application/json"})
