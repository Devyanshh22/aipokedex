import requests
import json
import pandas as pd

# Replace with your Gemini API key
api_key = "YOUR_API_KEY"

# Function to fetch Pokémon data from the PokéAPI
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to process Pokémon data and extract relevant information
def process_pokemon_data(pokemon_data):
    pokemon_info = {}
    pokemon_info["name"] = pokemon_data["name"].capitalize()
    pokemon_info["types"] = [type["type"]["name"] for type in pokemon_data["types"]]
    pokemon_info["abilities"] = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
    pokemon_info["stats"] = {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon_data["stats"]}
    pokemon_info["moves"] = [move["move"]["name"] for move in pokemon_data["moves"]]
    return pokemon_info

# Function to interact with the user and provide information
def interact_with_user():
    while True:
        pokemon_name = input("Enter a Pokémon name (or 'quit' to exit): ")
        if pokemon_name.lower() == "quit":
            break

        pokemon_data = fetch_pokemon_data(pokemon_name)
        if pokemon_data:
            pokemon_info = process_pokemon_data(pokemon_data)
            print(json.dumps(pokemon_info, indent=4))
        else:
            print(f"Pokémon '{pokemon_name}' not found.")

# Main function
if __name__ == "__main__":
    interact_with_user()
