class Methods:
    def es_palindromo(nombre:str):
        '''verifica si una palabra es palindromo usando ::-1 si es igual a la misma en reversa'''
        respuesta = nombre.lower() == nombre[::-1].lower()
        print(respuesta)
        return respuesta

    def fizzbuzz(max_numero:int):
        '''fizzbuzz'''
        if not max_numero:
            return 'El numero no puede ser 0'
        else:
            numero = ['fizz' if numero % 3 == 0 else 'buzz' if numero % 5 == 0 else 'fizzbuzz' if numero % 3 == 0 and numero % 5 == 0 else numero  for numero in range(max_numero)]
            return {'numero': numero}