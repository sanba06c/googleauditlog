import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/admin.reports.audit.readonly"]


def main():
  """Shows basic usage of the Admin SDK Reports API.
  Prints the time, email, and name of the last 100 login events in the domain.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  service = build("admin", "reports_v1", credentials=creds)

  # Call the Admin SDK Reports API
  print("Getting the last 10 login events")
  results = (
      service.activities()
      .list(userKey="all", applicationName="login", maxResults=100)
      .execute()
  )
  activities = results.get("items", [])

  if not activities:
    print("No logins found.")
  else:
    print("Logins:")
    for activity in activities:
      print(
          "{0}: {1} ({2})".format(
              activity["id"]["time"],
              activity["actor"]["email"],
              activity["events"][0]["name"],
          )
      )

 # Call the mobile Reports API
def main():
  """Shows basic usage of the Admin SDK Reports API.
  Prints the time, email, and name of the last 100 login events in the domain.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  service = build("admin", "reports_v1", credentials=creds)

  # Call the Admin SDK Reports API
  print("Getting the last 100 login events")
  results = (
    service.activities()
    .list(userKey="all", applicationName="login", maxResults=100)
    .execute()
  )
  activities = results.get("items", [])

  if not activities:
    print("No logins found.")
  else:
    print("Logins:")
    for activity in activities:
      print(
        "{0}: {1} ({2})".format(
          activity["id"]["time"],
          activity["actor"]["email"],
          activity["events"][0]["name"],
        )
      )

  # Call the mobile Reports API
  print("Getting the last 100 mobile events")
  results = (
    service.activities()
    .list(
      userKey="all",
      applicationName="mobile",
      maxResults=100
    )
    .execute()
  )
  activities = results.get("items", [])

  if not activities:
    print("No mobile events found.")
  else:
    print("Mobile events:")
    for activity in activities:
      print(
        "{0}: {1} ({2})".format(
          activity["id"]["time"],
          activity["actor"]["email"],
          activity["events"][0]["name"],
        )
      )


if __name__ == "__main__":
  main()