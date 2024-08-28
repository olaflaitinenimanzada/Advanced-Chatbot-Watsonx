from flask import Flask, request, jsonify
from src.assistant.assistant_integration import integrate_assistant
from src.nlu.nlu_integration import integrate_nlu
from src.tone_analyzer.tone_analyzer_integration import integrate_tone_analyzer
from src.discovery.discovery_integration import integrate_discovery

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Integrate with Watson services
    response = integrate_assistant(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
