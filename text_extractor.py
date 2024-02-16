def from_text_to_db(db_name, input = str, order = int):
    bad_chars = [';', ':', '!', "*"]
    text = input.replace("-\n", "")
    text = text.replace("\n", " ")
    for i in bad_chars:
        text = text.replace(i, "")
    
    return 0