from abc import ABC, abstractmethod
from errores import *


class ReglaCifrado(ABC):
    def __init__(self, token: int):
        self.token: int = token
        self.numeros: list = []
        self.no_ascii: list = []

    @abstractmethod
    def mensaje_valido(self, mensaje: str) -> bool:
        pass

    @abstractmethod
    def encriptar(self, mensaje: str) -> bool:
        pass

    @abstractmethod
    def desencriptar(self, mensaje: str) -> bool:
        pass

    def encontrar_numeros_mensaje(self, mensaje: str) -> list:
        for i, c in enumerate(mensaje):
            if c.isdigit():
                self.numeros.append(i)
        return self.numeros
    def encontrar_no_ascii_mensaje(self, mensaje: str) -> list:
        for i, c in enumerate(mensaje):
            if ord(c) > 127:
                self.no_ascii.append(i)
        return self.no_ascii


class Cifrador:
    def __init__(self, agente: ReglaCifrado):
        self.agente = agente

    def encriptar(self, mensaje: str) -> str:
        pass

    def desencriptar(self, mensaje: str) -> str:
        pass


class ReglaCifradoTraslacion (ReglaCifrado):
    def __init__(self):
        super().__init__()

    def cifrar(self, mensaje: str, token: int):
        if not self.mensaje_valido(mensaje):
            raise MensajeNoValido ("El mensaje no cumple con las validaciones")


    def mensaje_valido(self, mensaje: str) -> bool:
        if self.encontrar_numeros_mensaje(mensaje):
            raise ContieneNumero("No se puede, tiene un número")
        if not self.encontrar_no_ascii_mensaje(mensaje):
            raise ContieneNoAscii("No contiene letras del alfabeto ni caracteres especiales")
        if len(mensaje) == 1 and mensaje == " ":
            raise SinLetras("El mensaje no contiene letras")
        mensaje = mensaje.lower()
        if all(char in '@_#$%' for char in mensaje):
            raise ContieneNoAscii("El mensaje contiene caracteres especiales")

class ReglaCifradoNumerico (ReglaCifrado):
    def __init__(self):
        super().__init__()
    def mensaje_valido(self, mensaje: str) -> bool:
        if self.encontrar_numeros_mensaje(mensaje):
            raise ContieneNumero("No se puede, tiene un número")
        if '  ' in mensaje:
            raise DobleEspacio("El mensaje contiene dos espacios")
        if mensaje.startswith(' ') or mensaje.endswith(' '):
            raise ContieneNoAscii("El mensaje empieza o termina con espacio")
        mensaje = mensaje.lower()