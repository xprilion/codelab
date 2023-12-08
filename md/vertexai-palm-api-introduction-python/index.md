summary: Introduction to Building Solutions with PaLM2 API via Vertex AI on GCP
id: vertexai-palm-api-introduction-python
categories: python
tags: beginner
status: Published 
authors: Anubhav Singh
feedback Link: https://xprilion.com/codelabs/
analytics account: G-NKJL65V2YL


# Introduction to Building Solutions with PaLM2 API via VertexAI on GCP
<!-- ------------------------ -->
## Overview 
Duration: 1

Hey there!

In this Codelab, we'll walk through creating a simple chatbot based game using Google Cloud's Vertex AI and Flask, a popular web framework in Python. Our application will ask you to 


<!-- ------------------------ -->
## Requirements
Duration: 2

In order to follow this codelab, you'll need the following:

1. A Google Cloud Platform account with active billing.
2. A development environment with Python 3.7 or above installed.
3. Access to terminal/shell for executing commands.


<!-- ------------------------ -->
## Setting Up Your Google Cloud Environment
Duration: 10

1. Log in to your [Google Cloud Platform](https://console.cloud.google.com/) account.
2. Create a new project, let's name it `project-x`.
3. Enable [billing for the project](https://cloud.google.com/billing/docs/how-to/modify-project).
4. Navigate to the [APIs & Services dashboard](https://console.cloud.google.com/apis/dashboard) and enable the Vertex AI API.
5. [Create a service account and download the JSON key file](https://cloud.google.com/iam/docs/keys-create-delete) (`key.json`). Store this file safely.


<!-- ------------------------ -->
## Setting Up Your Local Environment
Duration: 5

1. Install Flask:
   ```bash
   pip install Flask
   ```
2. Install other required libraries:
   ```bash
   pip install marko google-cloud-aiplatform
   ```


<!-- ------------------------ -->
## Write the driving code
Duration: 10

1. **Importing Libraries**: We start by importing necessary Python libraries. Flask for our web framework, Vertex AI for AI model interaction, and others for various functionalities.

```python
import os
from flask import Flask, request, Response, g, render_template, jsonify
import marko
import vertexai
from vertexai.language_models import TextGenerationModel
from google.oauth2 import service_account
```

2. **Initializing the App and Vertex AI**: We initialize our Flask app and configure Vertex AI with our GCP project details.

```python
credentials = service_account.Credentials.from_service_account_file('./key.json')

app = Flask(__name__)
app.debug = True

vertexai.init(project="gcp-adventure-x", location="us-central1", credentials=credentials)
parameters = {
    "temperature": 1,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}

model = TextGenerationModel.from_pretrained("text-bison@001")
```

3. **Defining Routes**: We define two routes - one for the home page and another for handling chat messages.

```python
@app.route('/', methods=['GET'])
def hello_world():
    return render_template("chat.html")

@app.route('/chat/<message>', methods=['GET'])
def chat(message):
    response = model.predict(
        "generate a poem with the message that follows, make it sound like shakespeare, make it funny, no longer than 12 lines: " + message,
        **parameters
    )

    print(response)

    return jsonify({
        "response": marko.convert(response.text)
    })


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
```

4. **Chat Function**: This function takes a message, sends it to the AI model, and returns a poem based on the message.

```jinja
{% extends "base.html" %}

{% block content %}
<div class="row">
    <div class="col-12">
        <div id="chat-box" class="bg-light p-3 mb-3 rounded">
            {% include 'messages.html' %}
        </div>
        <div class="input-group">
            <input id="chat-input" type="text" class="form-control" placeholder="Type your message...">
            <div class="input-group-append">
                <button id="send-button" class="btn btn-primary">Send</button>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block script %}
<script>
$(function() {
    $('#send-button').click(function() {
        var input = $('#chat-input').val().trim();
        if (input != '') {
            $('#chat-box').append('<div class="p-2 mt-2 rounded bg-primary text-white">User: ' + input + '</div>');
            $('#chat-input').val('');
            // Use AJAX to send the input to the server and get a response
            $.ajax({
                url: '/chat/' + encodeURIComponent(input),
                type: 'GET',
                success: function(data) {
                    $('#chat-box').append('<div class="p-2 mt-2 rounded bg-secondary text-white">Bot: ' + data.response + '</div>');
                },
                error: function() {
                    $('#chat-box').append('<div class="p-2 mt-2 rounded bg-secondary text-white">Bot: Sorry, I am not able to respond at the moment.</div>');
                }
            });
        }
    });
});
</script>
{% endblock %}
```

<!-- ------------------------ -->
## Running the App
Duration: 2

1. Run your application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://localhost:8080`. You should see your chatbot interface.


<!-- ------------------------ -->
## Interacting with Your Chatbot
Duration: 2

1. Enter a message in the chat interface.
2. The chatbot will respond with a Shakespearean-style poem, humorously tailored to your message.


<!-- ------------------------ -->
## Conclusion
Duration: 1

Congratulations! You've just built and deployed a simple chatbot using Flask and Google Cloud's Vertex AI. This bot takes user input and generates creative, Shakespearean-style poems with a humorous twist.


<!-- ------------------------ -->
## What's Next?
Duration: 1

- Experiment with different model parameters to see how they affect the output.
- Try integrating this chatbot into a larger web application.
- Explore other capabilities of Vertex AI.
