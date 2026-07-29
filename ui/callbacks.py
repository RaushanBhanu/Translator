import asyncio

from tkinter import END, messagebox
from googletrans import LANGUAGES
from services.translator_service import translate
from utils.languages import language_dict


def translate_text(app):

    text = app.input_text.get("1.0", END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    destination = app.target_lang.get()

    if not destination:
        messagebox.showwarning("Warning", "Select target language.")
        return

    destination_code = language_dict[destination]

    try:

        if app.source_lang.get() == "Auto Detect":

            result = asyncio.run(
                translate(
                    text=text,
                    dest=destination_code,
                )
            )

            detected = LANGUAGES.get(
                result.src,
                result.src,
            ).title()

        else:

            source_code = language_dict[app.source_lang.get()]

            result = asyncio.run(
                translate(
                    text=text,
                    src=source_code,
                    dest=destination_code,
                )
            )

            detected = app.source_lang.get()

        app.output_text.config(state="normal")
        app.output_text.delete("1.0", END)
        app.output_text.insert(END, result.text)
        app.output_text.config(state="disabled")

        app.detected_label.config(text=f"Detected Language: {detected}")

    except Exception as e:
        messagebox.showerror(
            "Translation Error",
            str(e),
        )


def clear_text(app):

    app.input_text.delete("1.0", END)

    app.output_text.config(state="normal")
    app.output_text.delete("1.0", END)
    app.output_text.config(state="disabled")

    app.detected_label.config(text="Detected Language: -")


def swap_languages(app):

    if app.source_lang.get() == "Auto Detect":
        return

    source = app.source_lang.get()
    target = app.target_lang.get()

    app.source_lang.set(target)
    app.target_lang.set(source)

    translated = app.output_text.get(
        "1.0",
        END,
    ).strip()

    if translated:

        original = app.input_text.get(
            "1.0",
            END,
        )

        app.input_text.delete("1.0", END)
        app.input_text.insert(END, translated)

        app.output_text.config(state="normal")
        app.output_text.delete("1.0", END)
        app.output_text.insert(END, original)
        app.output_text.config(state="disabled")
