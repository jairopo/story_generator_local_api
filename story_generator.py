import requests
import json

# API models url
models_url = ["http://127.0.0.1:5000/v1/completions", ""]

# Model names
models_name = [
    "Qwen/Qwen2.5-1.5B-Instruct",
    "TheBloke/Mistral-7B-v0.1-GGUF",
]

headers = {"Content-Type": "application/json"}

def get_user_features():
    """Ask the user for the necessary features."""
    print("Let's create a story! To continue, you must complete some important features for the story. To end the program, call the main character 'end'")
    main_character = input("Main character's name: ")
    secondary_character = input("Secondary character's name: ")
    location = input("Story location: ")
    action = input("Important action that must happen: ")
    
    print("\nSelect the creativity level for the story:")
    print("a High")
    print("b Medium")
    print("c Low")
    creativity_level = input("Choose an option (a/b/c): ").lower()
    
    # Get the temperature selected. Medium creativity if input is invalid.
    temperature = {"a": 0.9, "b": 0.7,"c": 0.3}.get(creativity_level, 0.7)  
    
    # Return the features
    return main_character, secondary_character, location, action, temperature

def get_story_prompt(main_character, secondary_character, location, action):
    """Generates a story using the given parameters"""
    prompt = (
        f"Write an engaging and creative story with the following elements:\n"
        f"- Main character: {main_character}\n"
        f"- Secondary character: {secondary_character}\n"
        f"- Location: {location}\n"
        f"- Important action: {action}"
    )
    return prompt
    
    
while True:
    # User input
    main_character, secondary_character, locataion, action, temperature = get_user_features()
    # Check if the user wants to end
    if main_character.lower() == 'end': break
    body = {"prompt": get_story_prompt(main_character, secondary_character, locataion, action), "temperature": temperature, "max_new_tokens": 300}

    # Create story using both models
    for i, url in enumerate(models_url):
        response = requests.post(url, headers=headers, json=body)
        message_response = json.loads(response.content.decode("utf-8"))
        assistant_message = message_response["choices"][0]["text"]
        print(f"{models_name[i]} story:")
        print(assistant_message)
        print()




""" while True:
    user_message = input("> ")
    if user_message == "bye": break
    body = {"prompt": user_message, "max_tokens": 10}
    response = requests.post(url, headers=headers, json=body)
    message_response = json.loads(response.content.decode("utf-8"))
    assistant_message = message_response["choices"][0]["text"]
    print(assistant_message) """



