Tools = [
    {
        "name": "get_trains_between_stations",
        "description": "Fetch trains between two stations using their station codes.",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "description": "The station name of the source station."
                },
                "destination": {
                    "type": "string",
                    "description": "The station name of the destination station."
                },
                "date": {
                    "type": "string",
                    "description": "The date of journey in DD-MM-YYYY format."
                }
            },
            "required": ["source", "destination", "date"]
        }
    },
    {
        "name": "get_train_schedule",
        "description": "Fetch the schedule of a specific train using its train number.",
        "parameters": {
            "type": "object",
            "properties": {
                "train_number": {
                    "type": "string",
                    "description": "The train number."
                }
            },
            "required": ["train_number"]
        }
    },
    {
        "name": "get_seat_availability",
        "description": "Check seat availability for a specific train on a given date.",
        "parameters": {
            "type": "object",
            "properties": {
                # "train_number": {
                #     "type": "string",
                #     "description": "The train number."
                # },
                "date": {
                    "type": "string",
                    "description": "The date of journey in DD-MM-YYYY format."
                },
                # "class_code": {
                #     "type": "string",
                #     "description": "The class code (e.g., SL, 3A, 2A)."
                # },
                "source": {
                    "type": "string",
                    "description": "The station code of the source station."
                },
                "destination": {
                    "type": "string",
                    "description": "The station code of the destination station."
                 },
                # "quota": {
                #     "type": "string",
                #     "description": "The quota code (e.g., GN for General, TL for Tatkal)."
                # }
            },
            "required": ["date", "source", "destination"]
        }
    },
    {
        "name": "get_fare",
        "description": "Get fare details for a specific train between two stations.",
        "parameters": {
            "type": "object",
            "properties": {
                "train_number": {
                    "type": "string",
                    "description": "The train number."
                },
                "source": {
                    "type": "string",
                    "description": "The station code of the source station."
                },
                "destination": {
                    "type": "string",
                    "description": "The station code of the destination station."
                }
            },
            "required": ["train_number", "source", "destination"]
        }
    },
    {
        "name": "get_pnr_status",
        "description": "Get the status of a PNR number.",
        "parameters": {
            "type": "object",
            "properties": {
                "pnr_number": {
                    "type": "string",
                    "description": "The PNR number."
                }
            },
            "required": ["pnr_number"]
        }
    },
    {
        "name": "get_live_train_status",
        "description": "Get the live status of a train using its train number.",
        "parameters": {
            "type": "object",
            "properties": {
                "train_number": {
                    "type": "string",
                    "description": "The train number."
                }
            },
            "required": ["train_number"]
        }
    },
    {
        "name": "get_trains_by_station",
        "description": "Fetch trains arriving or departing from a specific station.",
        "parameters": {
            "type": "object",
            "properties": {
                "station_code": {
                    "type": "string",
                    "description": "The station code."
                }
            },
            "required": ["station_code"]
        }
    },
    {
        "name": "get_station_name_from_code",
        "description": "Get the station name from a given station code.",
        "parameters": {
            "type": "object",
            "properties": {
                "station_code": {
                    "type": "string",
                    "description": "The station code."
                }
            },
            "required": ["station_code"]
        }
    }

]

def get_tools():
    tools = []
    for tool in Tools:
        tools.append({"type": "function", "function": tool})
    return tools

def get_tool_names():
    return [tool["name"] for tool in Tools]