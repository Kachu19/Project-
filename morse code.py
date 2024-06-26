import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import time

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

ONE_UNIT = 0.5
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT
PATH = 'morse_sound_files/'


class MorseCodeTranslatorGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Alphabet to Morse Code Translator")
        self.root.geometry("400x300")

        self.label = ttk.Label(root, text="Enter Message:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root, width=40)
        self.entry.pack(pady=5)

        self.translate_button = ttk.Button(root, text="Translate", command=self.translate)
        self.translate_button.pack(pady=5)

    def verify(self, string):
        keys = CODE.keys()
        for char in string:
            if char.upper() not in keys and char != ' ':
                messagebox.showerror('Error', 'The character ' + char + ' cannot be translated to Morse Code')
                return False
        return True

    def translate(self):
        msg = self.entry.get()
        if not self.verify(msg):
            return

        pygame.init()
        for char in msg:
            if char == ' ':
                print(' ' * 7)
                time.sleep(SEVEN_UNITS)
            else:
                print(CODE[char.upper()])
                pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
                pygame.mixer.music.play()
                time.sleep(THREE_UNITS)

        print('\n\nTranslation complete!')


def main():
    root = tk.Tk()
    app = MorseCodeTranslatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
