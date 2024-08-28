from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import WATSON_NLU_API_KEY, WATSON_NLU_URL

def setup_nlu():
    authenticator = IAMAuthenticator(WATSON_NLU_API_KEY)
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
    nlu.set_service_url(WATSON_NLU_URL)
    return nlu

if __name__ == "__main__":
    nlu = setup_nlu()
    print("NLU setup complete.")
