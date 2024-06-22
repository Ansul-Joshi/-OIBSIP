import winsound
import time

def play_sound(frequency, duration):
    """
    Play a sound at a specific frequency and duration using the winsound.Beep function.
    
    Args:
    frequency (int): Frequency of the sound in Hertz.
    duration (int): Duration of the sound in milliseconds.
    """
    winsound.Beep(frequency, duration)

def beatbox():
    frequencies = {
        "C4": 262,
        "D4": 294,
        "E4": 330,
        "F4": 349,
        "G4": 392,
        "A4": 440,
        "B4": 494,
        "C5": 523,
        "D5": 587,
        "E5": 659,
        "F5": 698,
        "G5": 784,
        "A5": 880,
        "B5": 988,
        "C6": 1047
    }

    happy_birthday = [
        ("G4", 500), ("G4", 500), ("A4", 1000), ("G4", 1000), ("C5", 1000), ("B4", 2000),
        ("G4", 500), ("G4", 500), ("A4", 1000), ("G4", 1000), ("D5", 1000), ("C5", 2000),
        ("G4", 500), ("G4", 500), ("G5", 1000), ("E5", 1000), ("C5", 1000), ("B4", 1000), ("A4", 1000),
        ("F5", 500), ("F5", 500), ("E5", 1000), ("C5", 1000), ("D5", 1000), ("C5", 2000)
    ]

    for note, duration in happy_birthday:
        frequency = frequencies[note]
        play_sound(frequency, duration)
        time.sleep(0.1)

if __name__ == "__main__":
    beatbox()
