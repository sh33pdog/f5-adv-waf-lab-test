import requests
from requests.auth import HTTPBasicAuth

# Replace these with your actual F5 BIG-IP details
BIGIP_HOST = 'IP/DOMAIN'
BIGIP_USER = 'USERNAME'
BIGIP_PASSWORD = 'PASSWORD'

# Set the base URL for the iControlREST API
BASE_URL = 'https://{}/mgmt/tm/asm/policies'.format(BIGIP_HOST)

# Define a function to get the policies
def get_policies():
    response = requests.get(
        BASE_URL,
        auth=HTTPBasicAuth(BIGIP_USER, BIGIP_PASSWORD),
        verify=False  # Set to True if you have a valid SSL certificate
    )
    response.raise_for_status()  # Raise an error for bad HTTP responses
    return response.json()

# Define a function to extract names and virtualServers from the policies
def extract_policy_info(policies):
    for policy in policies.get('items', []):
        name = policy.get('name')
        virtual_servers = policy.get('virtualServers', [])
        virtual_servers_str = ', '.join(virtual_servers) if virtual_servers else 'N/A'
        print("WAF Policy Name = : {}, This is assigned to Virtual Servers = : {}".format(name, virtual_servers_str))

# Main function
def main():
    try:
        policies = get_policies()
        extract_policy_info(policies)
    except requests.RequestException as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
