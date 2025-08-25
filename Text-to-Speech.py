import pyttsx3
import re
import pyttsx3
import re
import sys
import subprocess
import shlex
from datetime import datetime
import os

# --- eSpeak Mode Functionality ---
def run_espeak_mode():
    """Launches the interactive session for the eSpeak engine."""
    print("\n--- eSpeak Mode Active ---")
    print("Features: Fast, highly customizable, robotic voice.")
    print("Type '/.help' for a list of eSpeak commands.")
    print("--------------------------")

    try:
        engine = pyttsx3.init(driverName='espeak')
    except Exception as e:
        print(f"Fatal Error: Failed to initialize pyttsx3 engine: {e}")
        return

    # --- Store Initial Default Properties ---
    initial_rate = engine.getProperty('rate')
    initial_pitch = engine.getProperty('pitch')
    initial_voice_id = "english"
    initial_amplitude = 100
    initial_word_gap = 0

    # --- Global variables for current settings ---
    current_rate = initial_rate
    current_pitch = initial_pitch
    current_voice_id = initial_voice_id
    current_amplitude = initial_amplitude
    current_word_gap = initial_word_gap

    def speak_advanced_espeak(text):
        safe_text = shlex.quote(text)
        command = (
            f"espeak -s {current_rate} "
            f"-p {current_pitch} "
            f"-v \"{current_voice_id}\" "
            f"-a {current_amplitude} "
            f"-g {current_word_gap} "
            f"{safe_text}"
        )
        try:
            subprocess.run(command, shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            error_message = e.stderr.decode('utf-8').strip()
            print(f"Error from espeak: {error_message}")

    def save_espeak(text):
        filename = datetime.now().strftime("tts_%Y-%m-%d_%H-%M-%S.wav")
        engine.setProperty('rate', current_rate)
        engine.setProperty('pitch', current_pitch)
        engine.setProperty('voice', current_voice_id)
        engine.setProperty('volume', current_amplitude / 200.0)
        
        print(f"Saving to '{filename}'...")
        engine.save_to_file(text, filename)
        engine.runAndWait()
        print("Save complete.")
        
    def display_espeak_help():
        print("\n--- eSpeak Mode Commands ---")
        print("  .s <text>            : Play and save audio.")
        print("  /.rate <num>         : Sets speed (e.g., 160).")
        print("  /.pitch <0-100>      : Sets pitch (e.g., 65).")
        print("  /.voice <ID>         : Changes voice ID (e.g., en-us+f3).")
        print("  /.amplitude <0-200>  : Sets volume/amplitude (e.g., 150).")
        print("  /.gap <num>          : Sets extra gap between words (x10ms).")
        print("  /.reset              : Resets all parameters.")
        print("  /.speak <text>       : Speaks text using all advanced parameters.")
        print("  exit                 : Return to the main menu.")
        print("--------------------------\n")
    
    # --- eSpeak Main Loop ---
    while True:
        try:
            user_input = input("eSpeak > ").strip()
            if user_input.lower() == 'exit':
                print("Returning to main menu...")
                break
            
            if user_input.lower().startswith('.s '):
                text_to_speak = user_input.split(' ', 1)[1]
                speak_advanced_espeak(text_to_speak)
                save_espeak(text_to_speak)
                continue
                
            match = re.match(r"^\s*/\.(?P<command>\w+)\s*(?P<argument>.*)", user_input, re.DOTALL)
            if match:
                command = match.group('command').lower()
                argument = match.group('argument').strip()
                if command == "help": display_espeak_help()
                elif command == "rate": current_rate = int(argument)
                elif command == "pitch": current_pitch = int(argument)
                elif command == "voice": current_voice_id = argument
                elif command == "amplitude": current_amplitude = int(argument)
                elif command == "gap": current_word_gap = int(argument)
                elif command == "reset":
                    current_rate, current_pitch, current_voice_id, current_amplitude, current_word_gap = \
                    initial_rate, initial_pitch, initial_voice_id, initial_amplitude, initial_word_gap
                    print("eSpeak parameters reset.")
                elif command == "speak":
                    if argument: speak_advanced_espeak(argument)
                else:
                    print(f"Unknown command: '/.{command}'.")
            else:
                speak_advanced_espeak(user_input)
        except (ValueError, IndexError):
            print("Invalid command or argument. Type '/.help' for syntax.")
        except KeyboardInterrupt:
            print("\nReturning to main menu...")
            break
        except EOFError:
            print("\nEnd of input received. Exiting.")
            return # Use return instead of break to exit the function


# --- Piper Mode Functionality ---
def run_piper_mode():
    """Launches the interactive session for the Piper engine."""
    print("\n--- Piper TTS Mode Active ---")
    print("Features: Realistic voice, slower synthesis.")
    print("Type 'exit' to return to the main menu.")
    print("-----------------------------")

    model_file = 'en_US-lessac-medium.onnx'

    def speak_piper(text):
        piper_command = ['piper', '--model', model_file, '--output_file', '-']
        aplay_command = ['aplay', '--rate', '22050', '--format', 'S16_LE', '--channels', '1', '--file-type', 'raw']
        
        try:
            piper_process = subprocess.Popen(piper_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            aplay_process = subprocess.Popen(aplay_command, stdin=piper_process.stdout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            piper_process.stdin.write(text.encode('utf-8'))
            piper_process.stdin.close()
            aplay_process.wait()
        except FileNotFoundError as e:
            print(f"Error: Command not found - {e.filename}. Make sure 'piper' and 'aplay' are installed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_piper(text):
        filename = datetime.now().strftime("tts_%Y-%m-%d_%H-%M-%S.wav")
        save_command = ['piper', '--model', model_file, '--output_file', filename]
        
        print(f"Saving to '{filename}'...")
        try:
            process = subprocess.Popen(save_command, stdin=subprocess.PIPE)
            process.communicate(input=text.encode('utf-8'))
            print("Save complete.")
        except FileNotFoundError as e:
            print(f"Error: Command not found - {e.filename}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # --- Piper Main Loop ---
    while True:
        try:
            user_input = input("Piper TTS > ").strip()
            if user_input.lower() == 'exit':
                print("Returning to main menu...")
                break
            
            if user_input.lower().startswith('.s '):
                text_to_speak = user_input.split(' ', 1)[1]
                speak_piper(text_to_speak)
                save_piper(text_to_speak)
                continue

            if user_input:
                speak_piper(user_input)
        except KeyboardInterrupt:
            print("\nReturning to main menu...")
            break
        except EOFError:
            print("\nEnd of input received. Exiting.")
            return


# --- Main Menu ---
if __name__ == "__main__":
    while True:
        try:
            print("\n╔═══════════════════════════════╗")
            print("║   zeqqe's Text-to-Speech CLI  ║")
            print("╠═══════════════════════════════╣")
            print("║ 1. eSpeak (Fast & Robotic)    ║")
            print("║ 2. Piper TTS (Realistic)      ║")
            print("║ q. Quit                       ║")
            print("╚═══════════════════════════════╝")
            
            choice = input("Select an engine: ").strip().lower()
            
            if choice == '1':
                run_espeak_mode()
            elif choice == '2':
                run_piper_mode()
            elif choice == 'q':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")
        except KeyboardInterrupt:
            print("\nExiting program.")
            break
        except EOFError:
            print("\nEnd of input received. Exiting.")
            break
