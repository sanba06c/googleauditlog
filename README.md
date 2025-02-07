# Google Admin SDK Reports API Script

This project contains a Python script that uses the Google Admin SDK Reports API to fetch and print the last 100 login events in a Google Workspace domain.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Google Workspace account with admin privileges.
- You have Python 3 installed on your machine.
- You have pip (Python package installer) installed.

## Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   Install Dependencies:

2. Install the required Python libraries using pip:
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

4. Enable the Admin SDK API:

Go to the Google Cloud Console.
Create a new project or select an existing project.
Enable the Admin SDK API for your project.
Create OAuth 2.0 credentials and download the {} credentials.json file.
Place the {} credentials.json file in the root directory of this project.

**Usage**
1. Run the Script:

Execute the script to fetch and print the last 100 login events:
python googleauditlog.py

2. Authentication:

The first time you run the script, it will open a browser window for you to authenticate with your Google account.
After authentication, the script will save the credentials to a file named token.json for future use.

**Script Overview**
The script performs the following tasks:

1. Imports necessary libraries and modules.
2. Defines the required OAuth 2.0 scopes.
3. Handles authentication and authorization.
4. Builds the service object for the Admin SDK Reports API.
5. Fetches and prints the last 100 login events in the domain.
**License**
This project is licensed under the MIT License. See the LICENSE file for details.
**Acknowledgements**
Google Admin SDK
Google API Python Client
