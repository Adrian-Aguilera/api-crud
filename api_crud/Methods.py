class Methods:
    def es_palindromo(nombre:str):
        '''verifica si una palabra es palindromo usando ::-1 si es igual a la misma en reversa'''
        respuesta = nombre.lower() == nombre[::-1].lower()
        print(respuesta)
        return respuesta