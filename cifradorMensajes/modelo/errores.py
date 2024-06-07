from abc import ABC
class ErrorContenido(Exception):
    def __init__(self, detalles: str):
        pass


class ContieneNumero(ErrorContenido):
    def __init__(self):
        pass


class ContieneNoAscii(ErrorContenido):
    def __init__(self):
        pass


class ErrorFormato(Exception):
    def __init__(self):
        pass

class DobleEspacio(ErrorFormato):
    def __init__(self):
        pass

class SinLetras(ErrorFormato):
    def __init__(self):
        pass

class NoTrim(ErrorFormato):
    def __init__(self):
        pass

class MensajeNoValido(Exception):
    pass