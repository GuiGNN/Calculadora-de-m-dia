#Use uma lista para a função

def media(value : list):
    
    quantia = 0
    completo = 0

    for x in value:
        if type(x) is not int:
            print("Operação interrompida, possui valores não numéricos dentro da lista")
            print(f"""Valor {x}, tipo {type(x)}""")
            return 0
        ''
        completo += x
        quantia += 1

    return completo


#Exemplo de execução
lista = [1, 2, 3, 4, 5, 6]
mediaa = media(lista)
print(mediaa)