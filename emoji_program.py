from emoji_data import emoji_dict
def add_emojis_to_text(text):
    words = text.split()
    new_words = []
    for word in words:
        if word.lower() in emoji_dict:
            new_words.append(word + emoji_dict[word.lower()])
        else:
            new_words.append(word)
    return "".join(new_words)
  
if __name__ == "__main__":
    text = "I play basketball and I like trees"
    text_with_emojis = add_emojis_to_text(text)
    print(text_with_emojis)
