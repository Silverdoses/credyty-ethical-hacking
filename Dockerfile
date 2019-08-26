FROM python:latest

RUN useradd credyty
USER credyty
WORKDIR /home/credyty

COPY keylog.txt .
COPY pwdfinder.py .
COPY tests/test_pwdfinder.py .
COPY tests/test_pwdfinder_verbose.py .
COPY tests/execute_tests.sh .

CMD ["sh", "execute_tests.sh"]