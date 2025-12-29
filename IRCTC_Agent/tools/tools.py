from dotenv import load_dotenv
import os
import requests

load_dotenv()
irctc_api_key = os.getenv("IRCTC_API_KEY_2")
irctc_api_host = os.getenv("IRCTC_API_HOST_2")

url = "https://irctc-api2.p.rapidapi.com/"

def api_call(endpoint: str, params: dict):
    """Generic API call function."""
    print(f"Calling API endpoint: {endpoint} with params: {params}")
    headers = {
        "x-rapidapi-key": irctc_api_key,
        "x-rapidapi-host": irctc_api_host
    }
    try: 
        response = requests.get(url + endpoint, headers=headers, params=params)
        print(f"API response status: {response.status_code}")
        if response.status_code == 429:
            return "Error: Rate limit exceeded for IRCTC API. Cant make more calls right now."
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return "Error: Unable to fetch data from IRCTC API."
    
def call_tool(tool_name: str, params: dict):
    """Call the specified tool with parameters."""
    print(f"Calling tool: {tool_name} with params: {params}")
    if tool_name == "get_trains_between_stations":
        return get_trains_between_stations(
            source=params.get("source"),
            destination=params.get("destination"),
            date=params.get("date")
        )
    elif tool_name == "get_train_schedule":
        return get_train_schedule(
            train_number=params.get("train_number")
        )
    elif tool_name == "get_seat_availability":
        # return get_seat_availability(
        #     train_number=params.get("train_number"),
        #     date=params.get("date"),
        #     class_code=params.get("class_code"),
        #     source=params.get("source"),
        #     destination=params.get("destination"),
        #     quota=params.get("quota")
        # )
        return get_trains_between_stations(
            source=params.get("source"),
            destination=params.get("destination"),
            date=params.get("date")
        )
    elif tool_name == "get_fare":
        return get_fare(
            train_number=params.get("train_number"),
            source=params.get("source"),
            destination=params.get("destination")
        )
    elif tool_name == "get_pnr_status":
        return get_pnr_status(
            pnr_number=params.get("pnr_number")
        )
    elif tool_name == "get_live_train_status":
        return get_live_train_status(
            train_number=params.get("train_number")
        )
    elif tool_name == "get_trains_by_station":
        return get_trains_by_station(
            station_code=params.get("station_code")
        )
    elif tool_name == "get_station_code":
        return get_station_name_from_code(
            station_code=params.get("station_code")
        )
    else:
        return "Error: Tool not found."

def get_trains_between_stations(source: str, destination: str, date: str = None):
    """Fetch trains between two stations."""
    querystring = {"source": source, "destination": destination, "date": date}
    response = api_call("trainAvailability", querystring)
    return response

def get_train_schedule(train_number: str):
    """Fetch the schedule of a specific train."""
    querystring = {"trainNo": train_number}
    response = api_call("v1/getTrainSchedule", querystring)
    return response

def get_seat_availability(train_number: str, date: str, class_code: str, source: str, destination: str, quota: str = "GN"):
    """Check seat availability for a specific train."""
    querystring = {
        "trainNo": train_number,
        "fromStationCode": source,
        "toStationCode": destination,
        "date": date,
        "classType": class_code,
        "quota": quota
    }
    response = api_call("v2/checkSeatAvailability", querystring)
    return response

def get_fare(train_number: str, source: str, destination: str):
    """Get fare details for a specific train."""
    querystring = {
        "trainNo": train_number,
        "fromStationCode": source,
        "toStationCode": destination
    }
    response = api_call("v2/getFare", querystring)
    return response

def get_pnr_status(pnr_number: str):
    """Get the status of a PNR number."""
    querystring = {"pnrNumber": pnr_number}
    response = api_call("v3/getPNRStatus", querystring)
    return response

def get_live_train_status(train_number: str):
    """Get the live status of a train using its train number."""
    querystring = {"trainNumber": train_number, "startDay":"0"}
    response = api_call("liveTrain", querystring)
    return response

def get_trains_by_station(station_code: str):
    """Fetch trains arriving or departing from a specific station."""
    querystring = {"stationCode": station_code}
    response = api_call("v3/getTrainsByStation", querystring)
    return response

def get_station_name_from_code(station_code: str):
    """Get the station name from a given station code."""
    querystring = {"code": station_code}
    response = api_call("stationSearch", querystring)
    return response