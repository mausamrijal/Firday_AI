import pyfiglet
import speech_recognition as sr
import google.generativeai as genai
import os
import subprocess
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Display Friday AI text design
def display_welcome():
    ascii_art = pyfiglet.figlet_format("Friday AI", font="slant")
    print(ascii_art)
    print("Welcome to Friday AI! Your personal assistant.")
    engine.say("Welcome to Friday AI! Your personal assistant.")
    engine.runAndWait()

# Initialize Gemini AI
def initialize_gemini():
    genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your Gemini API key
    model = genai.GenerativeModel('gemini-pro')
    return model

# Voice-to-text function
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            return None

# Execute bash commands safely
def execute_bash_command(command):
    dangerous_commands = ["rm", "shutdown", "reboot", "dd", "mkfs", "fdisk"]
    for dangerous in dangerous_commands:
        if dangerous in command:
            print(f"Warning: This command ({command}) may be dangerous.")
            confirmation = input("Are you sure you want to proceed? (yes/no): ").strip().lower()
            if confirmation != "yes":
                print("Command execution aborted.")
                return
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        engine.say("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")
        engine.say("There was an error executing the command.")
    engine.runAndWait()

# Main function
def main():
    display_welcome()
    model = initialize_gemini()

    while True:
        print("\nWhat can I do for you?")
        engine.say("What can I do for you?")
        engine.runAndWait()

        user_input = listen_to_user()
        if not user_input:
            continue

        # Ask Gemini AI for the action
        response = model.generate_content(f"Perform the following task on a computer: {user_input}. Only provide the bash command to execute. Do not explain.")
        command = response.text.strip()

        print(f"Generated command: {command}")
        engine.say(f"Executing command: {command}")
        engine.runAndWait()

        # Execute the command
        execute_bash_command(command)

        # Ask if the user wants to continue
        print("\nDo you want to continue? (yes/no)")
        engine.say("Do you want to continue?")
        engine.runAndWait()

        continue_input = listen_to_user()
        if continue_input and continue_input.strip().lower() != "yes":
            print("Goodbye!")
            engine.say("Goodbye!")
            engine.runAndWait()
            break

if __name__ == "__main__":
    main()