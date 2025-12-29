# IRCTC AI Agent Chatbot

## Overview
The IRCTC AI Agent is a Python-based application designed to assist users in navigating the Indian Railway Catering and Tourism Corporation (IRCTC) services. This agent leverages AI to provide a seamless experience for booking tickets, checking train schedules, and obtaining information related to railway services.

## Features
- **Train Information**: Get details about trains between two stations.
- **Train Schedules**: Retrieve real-time train schedules and timings.
- **Live Train Status**: Check the live running status of trains.
- **Seat Availability**: Inquire about seat availability on specific trains.
- **Fare Enquiry**: Get fare information for different train classes.
- **PNR Status**: Check the status of your PNR.
- **General Information**: Understand Indian Railway rules and explanations.

## Limitations
- The AI Agent does **not** book tickets or modify bookings.
- It does **not** guarantee seat confirmation.
- It does **not** access private IRCTC systems.
- For ticket booking, users are redirected to the official IRCTC website.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd IRCTC_Agent
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```bash
python main.py
```

## Directory Structure
```
IRCTC_Agent/
│
├── main.py               # Main application file
├── Readme.md             # Project documentation
├── prompts/              # Directory containing prompt files
│   └── system_prompt.md   # System prompt for the AI agent
└── tools/                # Directory containing tool schemas and implementations
    ├── tool_schemas.py
    └── tools.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.


## Acknowledgments
- [IRCTC](https://www.irctc.co.in) for providing the railway services.
- OpenAI for the AI models used in this project.

## Important Notes
- The AI Agent strictly adheres to accuracy rules and will not invent or guess any train timings, availability, fares, or PNR status.
- If a tool fails or returns no data, the agent will clearly state that the information is unavailable.
- For ticket booking requests, the agent will guide users to the official IRCTC website.