
 
import subprocess
import platform

def announce_customer(customer, desk):
    message = f"{customer}, please proceed to {desk}."
    print(message)

    # Windows voice (SAPI)
    if platform.system() == "Windows":
        subprocess.call(['PowerShell', '-Command', f'Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{message}")'])
    else:
        # Fallback for Mac/Linux (requires 'say' or 'espeak')
        subprocess.call(['say', message])







