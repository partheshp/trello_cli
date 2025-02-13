## Trello CLI

This is a command-line tool for adding a Trello card to a specified list on a Trello board, including optional labels and comments.

### Setup
1. Obtain your Trello API Key and Token from https://trello.com/app-key
2. Replace `your_api_key` and `your_api_token` in the script.
3. Install required dependencies:
   ```sh
   pip install requests
   ```

### Usage
Run the script from the command line:
```sh
python trello_cli.py --board_id <BOARD_ID> --list_name "To Do" --card_name "New Task" --description "This is a test card" --label "Urgent" --comment "Needs to be done ASAP"
```

### Next Development steps
1. Implement Robust Error Handling
  - Invalid API key or token (401 Unauthorized).
  - Board, list, or label not found (404 Not Found).
  - Rate limits exceeded (429 Too Many Requests).
     
2. Support Multiple Labels per Card
  - Accept multiple labels as input (e.g., comma-separated values).
  - Fetch and match multiple label IDs from the board.
  - Include all matched labels when creating the card.

3. Fetch Board ID Dynamically from Board Name
  - Allowing them to enter a board name instead of an ID.
  - Making an API request to fetch available boards and match the name to an ID.
  - Handling cases where multiple boards have similar names.
 
4. Secure API Credentials
  - Using environment variables to store API credentials.
  - Creating a configuration file (e.g., ```.env``` or ```config.json```) and reading API keys securely.
  - Allowing users to input API credentials interactively if not set.
    
5. Improve CLI User Experience
  - Add better argument validation to prevent incorrect inputs (e.g., empty card names).
  - Display a confirmation message before performing API calls.
  - Provide an option to list available boards, lists, and labels interactively.

6. Add Logging & Debugging Support
  - Introduce logging to record API interactions and errors for debugging.
  - Allow users to enable a debug mode that prints detailed request/response data.
 
