import json


def translate_en_to_cn(word, translate_path):
    translate_dict = json.load(open(translate_path, "r"))
    return translate_dict.get(word, word)


def translate_cn_to_en(word, translate_words_path):
    translate_dict = json.load(open(translate_words_path, "r"))
    translate_dict = {v: k for k, v in translate_dict.items()}
    return translate_dict.get(word, word)


variable_type = {"d": "number", "s": "text", "m": "signature"}


def translate_type(type):
    return variable_type.get(type, type)
