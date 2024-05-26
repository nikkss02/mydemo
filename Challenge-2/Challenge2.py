import requests
import json

def get_aws_metadata():
    metadata_url = "http://169.254.169.254/latest/meta-data/"
    metadata = {}

    def get_metadata_recursively(url, key):
        response = requests.get(url)
        if response.status_code == 200:
            if response.text.endswith('/'):
                sub_keys = response.text.splitlines()
                for sub_key in sub_keys:
                    get_metadata_recursively(url + sub_key, key + sub_key + '/')
            else:
                metadata[key.rstrip('/')] = response.text

    get_metadata_recursively(metadata_url, "")
    return metadata

if __name__ == "__main__":
    metadata = get_aws_metadata()
    print(json.dumps(metadata, indent=4))