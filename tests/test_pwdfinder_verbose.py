import pwdfinder
import logging

logging.basicConfig(format="'%(asctime)s - %(levelname)s - %(message)s'", level=logging.DEBUG)


def test_password_finder_verbose():
    finder = pwdfinder.PasswordFinder()
    finder.load_samples(file_path='keylog.txt')
    logging.info('Contraseña calculada: {}'.format(finder.compute_password()))


if __name__ == '__main__':
    logging.info('Prueba con nivel de log detallado')
    test_password_finder_verbose()
