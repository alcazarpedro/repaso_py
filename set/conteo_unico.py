
def conteo (palabras:list) -> set:
    count_word = []
    for i in palabras:
        count_word.append(len(i))

    new_set = set(count_word)
    
    return new_set

palabras = ["manzana","mango","pera","durazno","jicama","pera"]
out = conteo(palabras)
print(out)
