def process_input(input_words):
    combined_words = "".join(input_words)
    unique_characters = sorted(set(combined_words), key=lambda x: (-combined_words.count(x), x.lower()))
    return "".join(unique_characters)

input_words = input("Masukkan kata-kata dalam format ['kata1', 'kata2', ...]: ")
input_words = input_words.replace('"', "").replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")

output = process_input(input_words)
print(output)
