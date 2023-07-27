
from flask import Flask, jsonify, request
from gptbot.chatgptconfig import ChatGPTBotAPI


app = Flask("ChatBOTAPI")


@app.get('/')
def run():
    return jsonify('Running Flask App!')

@app.route('/create', methods=['POST'])
def create_prompt():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = ChatGPTBotAPI().create_prompt(prompt)
    return jsonify(response)

@app.route('/fetch/<string:prompt_id>', methods = ['GET'])
def get_response(prompt_id):
    response = ChatGPTBotAPI().get_response(prompt_id)
    return response

@app.route('/update', methods=['PUT'])
def update_response():
    body = request.get_json()
    prompt_id = body.get("prompt_id")
    updated_prompt = body.get("new_prompt", "")
    response = ChatGPTBotAPI().update_prompt(prompt_id, updated_prompt)
    return jsonify(response)

@app.route('/remove/<string:prompt_id>', methods = ['DELETE'])
def delete_response(prompt_id):
    response = ChatGPTBotAPI().delete_prompt(prompt_id)
    return jsonify(response)
    

if __name__ == "__main__":
    app.run()