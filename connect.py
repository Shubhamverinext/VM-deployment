import requests

# Defining the API URL
API_URL = "http://20.51.219.224:80/receive_json"

# Sample JSON data to send
sample_json_data = {
    "CaseDescription": "Kevin Johnson DOI 9/28/2023 Swift Transportation Phila PA Injury back damage CL was working driving an 18 wheeler and was hit and injured by another commercial truck. CL injured his back and had back surgery that was diagnosed as L4 L5 damage. CL lost time form work and loss of income. Still seeing doctors and taking pain meds. Damages CL uses cane and suffers from limited mobility",
    "PrimaryCaseType": "Workers Compensation",
    "SecondaryCaseType": "Automobile Accident",
    "CaseRating": "Tier 3",
    "CaseState": "PA Pennsylvania",
    "IsWorkersCompensation": "Yes",
    "Confidence(%)": "90%",
    "Explanation": "The description indicates that the client was driving an 18 wheeler for work when he was hit and injured by another commercial truck. This falls under the Workers Compensation primary case type. The fact that the injury was caused by an automobile accident makes the secondary case type Automobile Accident. The injury is described as L4 L5 damage, which requires surgery, putting it in Tier 4. The incident happened in Philadelphia, PA, so the case state is PA Pennsylvania. The description also specifies that the client was working at the time, so this is a Workers Compensation case. The confidence level is high due to the clear description of the incident and the identification of the state.\n\nThe case rating is Tier 3 and case types are Workers Compensation and Automobile Accident, which fall under the 'Any' category. Therefore, according to the handling rules for the state, the recommended handling firm is 'REFER TO PA SECTION'.",
    "HandlingFirm": "REFER TO PA SECTION",
    "CaseId": "2b64a078-a54e-430d-a226-a05f21448723"
}

# Token obtained from the /token endpoint
access_token =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcxNzc2ODIzOH0.ed7WyXdkBBoDrmcOZgyx2C061wZ922bPalaHskAuvm0"

# Sending POST request to the API with access token in headers
try:
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.post(API_URL, json=sample_json_data, headers=headers)

    if response.status_code == 200:
        print("JSON data sent successfully.")
    else:
        print(f"Failed to send JSON data. Status code: {response.status_code}")
        
except Exception as e:
    print(f"An error occurred: {e}")

