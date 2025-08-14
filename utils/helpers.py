def clean_text(text):
    try:
        return text.replace("\n", " ").strip() 
    except Exception as e:
        print(f"Error: {repr(e)}")