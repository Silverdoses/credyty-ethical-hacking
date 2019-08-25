import logging
import time
import functools


class PasswordFinder:

    def __init__(self):
        """
        Define una variable de clase con las muestras previamente
        convertidas a una lista de Python.

        Define una variable de clase con una lista de mensajes para debugging.
        """
        self.sequences = None
        self.messages = {
            'no_change': '',
            'swap': ' => (Reubicado)',
            'add': ' [+] (Añadido)'
        }

    def measure_time(method):
        """
        Decorador para medición de tiempo que tarda un método
        en ejecutarse.

        Returns:
            wrapper: Función extendida.

        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            start = time.time()
            function = method(self, *args, **kwargs)
            end = time.time()
            logging.info('Método {} - Tiempo de ejecución: {:.2f} ms'.format(method.__name__, (end - start)*1000))
            return function

        return wrapper

    @measure_time
    def load_samples(self, file_path):
        """
        Carga un archivo de texto que contiene las combinaciones
        proporcionadas en el problema, separadas por saltos de línea.

        A cada combinación se le realiza preprocesamiento para eliminar
        espacios y saltos de línea que puedan afectar el cálculo.

        Args:
            file_path: Ruta del archivo de texto a procesar

        Returns:

        """
        lines = open(file_path, mode='r').readlines()
        self.sequences = [line.strip() for line in lines]

        logging.debug('Lista de combinaciones: {}'.format(self.sequences))

    @measure_time
    def compute_password(self):
        """
        El siguiente algoritmo toma una serie de muestras de N dígitos
        e intenta calcular la contraseña más corta que corresponda a dicho
        conjunto de secuencias, mediante una serie de iteraciones.

        En el caso específico del problema planteado, las muestras constan
        de 3 dígitos.


        Returns:
            password: Contraseña calculada por el algoritmo

        """
        sequences = set(self.sequences)  # Elimina las combinaciones repetidas.
        password = ''

        for sequence in sequences:
            logging.debug('[*] Secuencia: {}'.format(sequence))

            start = 0  # Guarda la posición del último dígito iterado para cada secuencia.

            for digit in sequence:
                before_start, after_start = password[:start], password[start:]

                # Caso 1 - El dígito existe en la contraseña y se encuentra en posición correcta.
                if digit in after_start:
                    position = after_start.find(digit)
                    start += position
                    msg = self.messages.get('no_change')

                # Caso 2 - El dígito existe en la contraseña pero es necesario reubicarlo para la actual secuencia
                elif digit in before_start:
                    new_position = start + 1
                    password = password[:new_position] + digit + password[new_position:]
                    old_position = before_start.find(digit)
                    password = password[:old_position] + password[old_position+1:]
                    msg = self.messages.get('swap')

                # Caso 3 - El dígito aún no existe en la contraseña. Se añade a la última posición.
                else:
                    password += digit
                    start = len(password)
                    msg = self.messages.get('add')

                logging.debug('Dígito: {} -  Contraseña calculada: {}{}'.format(digit, password, msg))

        return password
