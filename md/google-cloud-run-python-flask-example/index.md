summary: Google Cloud Run example using Python Flask
id: google-cloud-run-python-flask-example
categories: python
tags: beginner
status: Published 
authors: Anubhav Singh
feedback Link: https://xprilion.com/codelabs/
analytics account: G-NKJL65V2YL


# Google Cloud Run example using Python Flask

<!-- ------------------------ -->
## Overview 
Duration: 1

Hey there!

This codelab will walk you through the process of creating a simple "Hello World" application using Python Flask and deploying it to Google Cloud Run.

<!-- ------------------------ -->
## Requirements
Duration: 2

In order to follow this codelab, you'll need the following:

1. A Google Cloud Platform account.
2. Google Cloud CLI installed and initialized.
3. Python installed locally.

<!-- ------------------------ -->
## Setting Up Your Google Cloud Account
Duration: 10

1. Head over to [Google Cloud Platform](https://console.cloud.google.com/) and create an account.
2. Enable billing
3. Create a new project, let's name it `project-x`.

<!-- ------------------------ -->
## Install Google Cloud CLI
Duration: 5

Follow the official guide to install the Google Cloud CLI: [Installing Google Cloud SDK](https://cloud.google.com/sdk/docs/install).

<!-- ------------------------ -->
## Create and Run the Flask Application
Duration: 15

1. Set up a new directory for your project:
   ```bash
   mkdir hello-world-cloud-run
   cd hello-world-cloud-run
   ```

2. Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install Flask:
   ```bash
   pip install Flask
   ```

4. Create a file named `main.py` with the following content:
   ```python
   from flask import Flask
   import os

   app = Flask(__name__)

   @app.route('/')
   def hello_world():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
   ```

<!-- ------------------------ -->
## Running the App Locally
Duration: 2

1. Run your application locally:
   ```bash
   python main.py
   ```

2. Open your web browser and go to `http://localhost:8080`. You should see the "Hello, World!" message.

<!-- ------------------------ -->
## Deploy to Google Cloud Run
Duration: 5

1. Generate the requirements.txt file

    ```bash
    pip list --format=freeze > requirements.txt
    ```

2. Deploy your application to Google Cloud Run:
   ```bash
   gcloud run deploy
   ```

2. Wait for the deployment to complete. You will receive a URL where your application is live.

<!-- ------------------------ -->
## Conclusion
Duration: 1

Congratulations! You've just built and deployed a simple application on Google Cloud Run using Python and Flask!

<!-- ------------------------ -->
## What's Next?
Duration: 1

- Experiment with adding more routes and functionalities to your Flask application.
- Learn more about managing and monitoring your applications on Google Cloud Run.
- Explore other Google Cloud services that can enhance your application.
