class Calculadora:
    def __init__(self):
        self.__estado = 0

    def __verificar_entero(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El operando debe ser un número entero.")

    def sumar(self, operando):
        self.__verificar_entero(operando)
        self.__estado = operando + self.__estado

    def restar(self, operando):
        self.__verificar_entero(operando)
        self.__estado = operando - self.__estado

    def multiplicar(self, operando):
        self.__verificar_entero(operando)
        self.__estado = operando * self.__estado

    def dividir(self, operando):
        self.__verificar_entero(operando)
        if operando == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        self.__estado = operando // self.__estado

    def set(self, valor):
        self.__verificar_entero(valor)
        self.__estado = valor

    def reset(self):
        self.__estado = 0

    def get_resultado(self):
        return self.__estado

    def run(self):
        print("Bienvenido a la calculadora entera.")
        while True:
            try:

                operacion = input("Ingrese una operación (sumar, restar, multiplicar, dividir, set, reset, salir): ").strip().lower()

                
                if operacion == "salir":
                    print("Saliendo de la calculadora.")
                    break

                if operacion == "reset":
                    self.reset()
                    print(f"Estado interno restablecido a: {self.get_resultado()}")
                    continue

                if operacion == "set":
                    valor = int(input("Ingrese el valor para establecer el estado interno: "))
                    self.set(valor)
                    print(f"Estado interno establecido a: {self.get_resultado()}")
                    continue

                operando = int(input("Ingrese un número entero: "))

                if operacion == "sumar":
                    self.sumar(operando)
                elif operacion == "restar":
                    self.restar(operando)
                elif operacion == "multiplicar":
                    self.multiplicar(operando)
                elif operacion == "dividir":
                    self.dividir(operando)
                else:
                    print("Operación no reconocida. Intente de nuevo.")
                    continue

                print(f"Resultado actual: {self.get_resultado()}")

            except ValueError as ve:
                print(f"Error: {ve}")
            except ZeroDivisionError as zde:
                print(f"Error: {zde}")
            except Exception as e:
                print(f"Se produjo un error inesperado: {e}")
