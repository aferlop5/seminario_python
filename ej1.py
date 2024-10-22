def analize(cadena):
    d={}

    d["num_lineas"]=len(cadena.splitlines())

    d["palabras"] = len(cadena.split())

    d["caracteres"] = len(cadena)

    d["palabras_unicas"] = {}

    lista_palabras = cadena.split()

    for palabra in set(lista_palabras):

        d["palabras_unicas"][palabra] = lista_palabras.count(palabra)


    d["caracteres_unicos"] = {}

    cadena_aux = cadena.replace("\n", "").replace(" ", "").lower()

    for caracter in set(cadena):

        d["caracteres_unicos"][caracter] = cadena_aux.count(caracter)
    
    return d

res = analize("Hola soy Manolo barraqueta")
print(res)

