from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import WATSON_DISCOVERY_API_KEY, WATSON_DISCOVERY_URL

def setup_discovery():
    authenticator = IAMAuthenticator(WATSON_DISCOVERY_API_KEY)
    discovery = DiscoveryV1(
        version='2019-04-30',
        authenticator=authenticator
    )
    discovery.set_service_url(WATSON_DISCOVERY_URL)
    return discovery

if __name__ == "__main__":
    discovery = setup_discovery()
    print("Discovery setup complete.")
