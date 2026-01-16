from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableMap

# Replace this with your actual OpenAI API key
api_key = "YOUR_API_KEY_HERE"

def generate_story(character_name, setting, theme):
    try:
        # Prompt template
        prompt_template = PromptTemplate.from_template(
            "Create a story with the following details:\n"
            "Main character: {character_name}\n"
            "Setting: {setting}\n"
            "Theme: {theme}\n"
            "Story:\n"
        )

        # Initialize the chat model
        model = init_chat_model(
            model="gpt-3.5-turbo",
            model_provider="openai",
            api_key=api_key
        )

        # Wrap the chain in a RunnableMap (prompt formatting + model invocation)
        chain = RunnableMap({
            "story": lambda inputs: model.invoke(
                prompt_template.format(
                    character_name=inputs["character_name"],
                    setting=inputs["setting"],
                    theme=inputs["theme"]
                )
            )
        })

        # Inputs
        inputs = {
            "character_name": character_name,
            "setting": setting,
            "theme": theme
        }

        # Invoke chain
        result = chain.invoke(inputs)
        return result["story"]

    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        return None


# =========================
# Test cases
# =========================
if __name__ == "__main__":
    tests = [
        ("Alice", "Magical Forest", "Friendship"),
        ("Bob", "Space Station", "Adventure"),
        ("Luna", "Underwater Kingdom", "Courage")
    ]

    for i, (character, setting, theme) in enumerate(tests, start=1):
        print(f"=== Test {i}: {character}, {setting}, {theme} ===")
        story = generate_story(character, setting, theme)
        if story:
            print(story)
        else:
            print("No story generated due to an error.")
        print("\n")
