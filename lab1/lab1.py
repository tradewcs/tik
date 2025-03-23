import wikipedia
import collections
import math
import matplotlib.pyplot as plt
import zipfile

from functions import calculate_entropy

page = "Linux"
languages = ["en", "uk", "zh"]

def get_wikipedia_text(title, language="en", num_content=-1):
    wikipedia.set_lang(language)
    page = wikipedia.page(title, auto_suggest=False)
    return page.content[:num_content]

def save_text_to_file(text, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def zip_file(file_path, zip_name):
     with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, arcname=file_path.split("/")[-1])




def graph_bit_entropy(filename):
    size = []
    entropy = []

    with open(filename, 'rb') as file:
        file_content = file.read()

        for i in range(200, len(file_content), 100):
            bits = ''.join(format(b, '08b') for b in file_content[:i])

            size.append(i)
            entropy.append(calculate_entropy(bits))
    
    plt.plot(size, entropy)
    plt.xlabel("size")
    plt.ylabel("entropy")
    plt.title(filename)
    plt.show()

def graph_entropy(language="en"):
    text = get_wikipedia_text(page, language)

    entropy = []
    symbols_count = list(range(200, len(text), 100))
    for i in symbols_count:
        entropy.append(calculate_entropy(text[:i]))
    
    plt.plot(symbols_count, entropy)
    plt.xlabel("symbols count")
    plt.ylabel("entropy")
    plt.title(language)
    plt.show()

if __name__ == "__main__":
    for l in languages:
        filename = page + '_' + l + '.txt' 
        # save_text_to_file(get_wikipedia_text(page, l), filename)
        # zip_file(filename, filename + '.zip')

        graph_bit_entropy(filename + '.zip')
        break

        # print(l, "-", calculate_entropy(get_wikipedia_text(page, l)))
        # graph_entropy(l)