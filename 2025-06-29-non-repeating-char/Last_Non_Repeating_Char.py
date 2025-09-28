import argparse
def nonRepeat(str_to_test, debug=False):
    array_non_repeating = []
    str_to_test = str_to_test.lower()
    str_len = int(len(str_to_test))
    for i in range(0, str_len):\
        # Checks all other characters against current
        modified_str = str_to_test[:i]+str_to_test[i+1:]
        if str_to_test[i] not in modified_str:
            array_non_repeating.append(str_to_test[i])
    if len(array_non_repeating) == 0:
        return None
    if debug:
        print (f"List of non repeating characters\n{array_non_repeating}")
        print (f"Last character of \"{str_to_test}\" \nwas {array_non_repeating[-1]}")
    return array_non_repeating[-1]

                   

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--debug", action="store_true", default=False)
    args = parser.parse_args()
    if args.test:
        string_to_test = ["She borrowed the book from him many years ago and hasn't yet returned it",
                          "Nancy thought the best way to create a welcoming home was to line it with barbed wire",
                          "At that moment he wasn't listening to music, he was living an experience"]
        for sentence in string_to_test:
               non_repeat_char = nonRepeat(sentence, args.debug)
               print(non_repeat_char)
    else:
        print("Please enter string for nonRepeat:")
        string_to_test = input()
        non_repeat_char = nonRepeat(string_to_test, args.debug)
        print(non_repeat_char)

           
