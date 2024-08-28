from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import WATSON_TONE_ANALYZER_API_KEY, WATSON_TONE_ANALYZER_URL

def setup_tone_analyzer():
    authenticator = IAMAuthenticator(WATSON_TONE_ANALYZER_API_KEY)
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )
    tone_analyzer.set_service_url(WATSON_TONE_ANALYZER_URL)
    return tone_analyzer

if __name__ == "__main__":
    tone_analyzer = setup_tone_analyzer()
    print("Tone Analyzer setup complete.")
