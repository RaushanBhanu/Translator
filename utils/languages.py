from googletrans import LANGUAGES

language_dict = {v.title(): k for k, v in LANGUAGES.items()}
language_names = sorted(language_dict.keys())
source_languages = ["Auto Detect"] + language_names