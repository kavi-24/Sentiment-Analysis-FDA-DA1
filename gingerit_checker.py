from gingerit.gingerit import GingerIt

def spell_checker(text: str) -> str:
    corrected_text = GingerIt().parse(text)
    return corrected_text['result']

if __name__ == "__main__":
    text = input("Enter a sentence >>: ")
    corrected_text = GingerIt().parse(text)
    print(corrected_text['result'])