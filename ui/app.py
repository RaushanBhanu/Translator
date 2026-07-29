import tkinter as tk
from tkinter import ttk

from ui.callbacks import (
    clear_text,
    swap_languages,
    translate_text,
)

from utils.languages import (
    language_names,
    source_languages,
)


class TranslatorApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Google Translator")
        self.root.geometry("760x600")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):

        tk.Label(
            self.root,
            text="Google Translator",
            font=("Arial", 18, "bold"),
        ).pack(pady=10)

        tk.Label(
            self.root,
            text="Enter Text",
        ).pack()

        self.input_text = tk.Text(
            self.root,
            width=80,
            height=8,
        )

        self.input_text.pack(pady=5)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.source_lang = ttk.Combobox(
            frame,
            values=source_languages,
            width=28,
            state="readonly",
        )

        self.source_lang.set("Auto Detect")

        self.source_lang.grid(
            row=0,
            column=0,
            padx=10,
        )

        ttk.Button(
            frame,
            text="⇄",
            command=lambda: swap_languages(self),
        ).grid(
            row=0,
            column=1,
        )

        self.target_lang = ttk.Combobox(
            frame,
            values=language_names,
            width=28,
            state="readonly",
        )

        self.target_lang.set("Hindi")

        self.target_lang.grid(
            row=0,
            column=2,
            padx=10,
        )

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        ttk.Button(
            button_frame,
            text="Translate",
            command=lambda: translate_text(self),
        ).grid(
            row=0,
            column=0,
            padx=10,
        )

        ttk.Button(
            button_frame,
            text="Clear",
            command=lambda: clear_text(self),
        ).grid(
            row=0,
            column=1,
            padx=10,
        )

        self.detected_label = tk.Label(
            self.root,
            text="Detected Language: -",
            font=("Arial", 11, "italic"),
        )

        self.detected_label.pack(pady=5)

        tk.Label(
            self.root,
            text="Translated Text",
        ).pack()

        self.output_text = tk.Text(
            self.root,
            width=80,
            height=8,
            state="disabled",
        )

        self.output_text.pack(pady=5)

    def run(self):
        self.root.mainloop()
