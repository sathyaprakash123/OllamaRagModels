import base64

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

def describe_image(query, question):
    print(f'About to call Deepseek with the query:{query}')
    with open(query, 'rb') as img_file:
        img_data = img_file.read()

    # Convert image to base64 for Ollama
    img_base64 = base64.b64encode(img_data).decode('utf-8')

    # Use the correct approach as per Ollama 3 documentation - images at top level
    response = ollama.generate(
        model='llava:latest',
        prompt=question,
        images=[img_base64],  # Pass base64 encoded image data at top level
        options={"temperature": 0.9}  # Lower temperature for more consistent output
    )

    # Extract the caption from the response
    return response['response'].strip()
    # return response["message"]["content"]


if(__name__ == "__main__"):
    ollama_app.run(port=8010)
    print("Running Ollama Deepseek Agent")