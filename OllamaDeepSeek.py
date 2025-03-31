import ollama
from flask import Flask, jsonify, request

ollama_app = Flask('__name__')


@ollama_app.route("/query", methods=['GET'])
def query_service():
    query = request.args.get("query")
    print(f'Query Received: {query}')
    return jsonify(call_deepseek(query))


def call_deepseek(query):
    print(f'About to call Deepseek with the query:{query}')
    response = ollama.chat(

        model="deepseek-r1:1.5b",
        messages=[
            {"role": "user", "content": query},
        ],
    )
    return response["message"]["content"]

if(__name__ == "__main__"):
    ollama_app.run(port=8010)
    print("Running Ollama Deepseek Agent")