# Personalized Story Generator:

# This project will take inputs like character names, settings, and themes from the user and generate a unique 
# sotry  using a text geenration model like GPT-3.5.

# Steps to create a project:

# Set up environment
# Collect user inputs
# Generate story using AI model
# Display the generated story 

# user_input.py

def get_user_inputs():
    print('Welcome to the Personalized Story Generator!')
    character_name = input("Enter the main character's name: ")
    setting = input("Enter the setting of the sotry: ")
    theme = input("Enter the theme of the sotry (e.g., adventure, mystery): ")
    return character_name, setting, theme