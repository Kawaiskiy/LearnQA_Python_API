class Ex10:

    phrase = input("Set the phrase: ")

    assert len(phrase) <= 15, f"Input phrase length more than 15 symbols: {len(phrase)}"
    print(f"Input phrase length: {len(phrase)}")