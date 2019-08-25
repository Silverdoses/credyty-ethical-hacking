import pwdfinder
import logging


def test_password_finder():
    finder = pwdfinder.PasswordFinder()
    finder.load_samples(file_path='keylog.txt')
    logging.info('Contraseña calculada: {}'.format(finder.compute_password()))


if __name__ == '__main__':
    test_password_finder()
