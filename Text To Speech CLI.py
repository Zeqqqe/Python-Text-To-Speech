import pyttsx3
import re
import time
import sys # Import the sys module

# --- Text-to-Speech Engine Setup ---
engine = pyttsx3.init()

# Store initial properties
initial_rate = engine.getProperty('rate')
initial_volume = engine.getProperty('volume')
initial_voice_id = engine.getProperty('voice')

# Global variables for current settings
current_rate = initial_rate
current_volume = initial_volume
current_voice_id = initial_voice_id

# Removed PITCH_MAP and current_pitch_ssml_tag

def list_available_voices():
    voices = engine.getProperty('voices')
    print("\n--- Available Voices ---")
    for i, voice in enumerate(voices):
        # On Windows, 'name' often contains the friendly name like "Microsoft David Desktop"
        # 'id' is the unique identifier.
        print(f"{i+1}. Name: {voice.name}")
        print(f"   ID: {voice.id}")
        print(f"   Gender: {voice.gender if voice.gender else 'Unknown'}, Age: {voice.age if voice.age else 'Unknown'}")
        print("------------------------")
    print("------------------------")

def speak_text(text):
    global engine, current_rate, current_volume, current_voice_id

    engine.setProperty('rate', current_rate)
    engine.setProperty('volume', current_volume)
    engine.setProperty('voice', current_voice_id)

    # No SSML prosody tag for pitch control needed anymore
    engine.say(text) # Speak the text directly
    engine.runAndWait()

def display_help():
    print("\n--- Text To Speech.py Commands ---")
    print("  /.rate <number>    : Sets speech speed (Words Per Minute, e.g., 170)")
    print("  /.volume <0.0-1.0> : Sets speech volume (e.g., 0.8)")
    # Removed /.pitch command from help
    print("  /.voice <name/ID>  : Changes voice (e.g., David, Zira, or a specific voice ID)")
    print("  /.reset            : Resets all speech parameters to defaults")
    print("  /.help             : Displays this list of commands")
    print("  text 'exit'        : Exits the program (type the word 'exit' without '/')")
    print("-----------------------------------\n")
    list_available_voices() # Optionally list voices when help is displayed

# --- Initial setup: Print only the instruction to run help ---
print("Text To Speech.py is Ready. Type your text to speak, or type '/.help' for commands.")
print("--------------------------------------------------------------------------")

# Main loop for user input
if __name__ == "__main__":
    try:
        while True:
            user_input = input("Enter text or command: ").strip()

            if not user_input:
                continue

            # Check if it's a command (starts with /.)
            if re.match(r"^\s*/\.(.+)", user_input):
                command_parts = re.match(r"^\s*/\.(.+)", user_input).group(1).strip().split(' ', 1)
                command = command_parts[0].lower()
                argument = command_parts[1].strip() if len(command_parts) > 1 else None

                if command == "help":
                    display_help()
                elif command == "rate":
                    try:
                        new_rate = int(argument)
                        if new_rate > 0:
                            current_rate = new_rate
                            print(f"Speech rate set to: {current_rate} WPM")
                        else:
                            print("Rate must be a positive number.")
                    except (ValueError, TypeError):
                        print(f"Usage: /.rate <number> (Current: {current_rate} WPM)")
                elif command == "volume":
                    try:
                        new_volume = float(argument)
                        if 0.0 <= new_volume <= 1.0:
                            current_volume = new_volume
                            print(f"Speech volume set to: {current_volume}")
                        else:
                            print("Volume must be between 0.0 and 1.0.")
                    except (ValueError, TypeError):
                        print(f"Usage: /.volume <number (0.0 to 1.0)> (Current: {current_volume})")
                # Removed elif command == "pitch": block
                elif command == "voice":
                    if argument:
                        found_voice = None
                        voices = engine.getProperty('voices')
                        for voice in voices:
                            # Check if argument matches name or ID (case-insensitive for name)
                            if argument.lower() in voice.name.lower() or argument == voice.id:
                                found_voice = voice
                                break
                        if found_voice:
                            current_voice_id = found_voice.id
                            print(f"Voice changed to: {found_voice.name}")
                        else:
                            print(f"Voice '{argument}' not found. Try one from the list above, or a partial name like 'David'.")
                    else:
                        list_available_voices()
                        print(f"Usage: /.voice <full or partial voice name/ID> (Current: {engine.getProperty('voice').name})")
                elif command == "reset":
                    # Reset speech parameters only
                    current_rate = initial_rate
                    current_volume = initial_volume
                    current_voice_id = initial_voice_id
                    # Removed current_pitch_ssml_tag reset
                    engine.setProperty('rate', initial_rate)
                    engine.setProperty('volume', initial_volume)
                    engine.setProperty('voice', initial_voice_id)
                    print("Speech parameters reset to initial defaults.")
                else:
                    print(f"Unknown command: /{command}. Type '/.help' for a list of commands.")
            else:
                # Regular text to speak
                if user_input.lower() == "exit":
                    print("Exiting Text To Speech.py.")
                    sys.exit() # Exit the script if the text "exit" is entered
                else:
                    speak_text(user_input)
    except KeyboardInterrupt:
        print("\nScript interrupted. Exiting cleanly.")
    finally:
        engine.stop() # Important to release resources
