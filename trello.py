import requests
import argparse
import json

# Trello API credentials
API_KEY = "trello_api_key"
TOKEN = "trello_token"
BASE_URL = "https://api.trello.com/1"

def get_board_lists(board_id):
    url = f"{BASE_URL}/boards/{board_id}/lists"
    params = {"key": API_KEY, "token": TOKEN}
    response = requests.get(url, params=params)
    return response.json()

def get_label_id(board_id, label_name):
    url = f"{BASE_URL}/boards/{board_id}/labels"
    params = {"key": API_KEY, "token": TOKEN}
    response = requests.get(url, params=params)
    labels = response.json()
    for label in labels:
        if label["name"].lower() == label_name.lower():
            return label["id"]
    return None

def add_card(list_id, name, desc, label_id):
    url = f"{BASE_URL}/cards"
    params = {
        "key": API_KEY,
        "token": TOKEN,
        "idList": list_id,
        "name": name,
        "desc": desc,
        "idLabels": label_id if label_id else ""
    }
    response = requests.post(url, params=params)
    return response.json()

def add_comment(card_id, comment):
    url = f"{BASE_URL}/cards/{card_id}/actions/comments"
    params = {"key": API_KEY, "token": TOKEN, "text": comment}
    requests.post(url, params=params)

def main():
    parser = argparse.ArgumentParser(description="Add a Trello card to a specific list with labels and a comment.")
    parser.add_argument("--board_id", required=True, help="Trello Board ID")
    parser.add_argument("--list_name", required=True, help="Name of the list/column to add the card to")
    parser.add_argument("--card_name", required=True, help="Name of the card")
    parser.add_argument("--description", default="", help="Card description")
    parser.add_argument("--label", help="Label name")
    parser.add_argument("--comment", help="Comment to add to the card")
    
    args = parser.parse_args()
    
    lists = get_board_lists(args.board_id)
    list_id = next((lst["id"] for lst in lists if lst["name"].lower() == args.list_name.lower()), None)
    
    if not list_id:
        print("Error: List not found on board.")
        return
    
    label_id = get_label_id(args.board_id, args.label) if args.label else None
    
    card = add_card(list_id, args.card_name, args.description, label_id)
    
    if "id" in card:
        print(f"Card '{args.card_name}' added successfully.")
        if args.comment:
            add_comment(card["id"], args.comment)
            print("Comment added to the card.")
    else:
        print("Error adding card.")

if __name__ == "__main__":
    main()