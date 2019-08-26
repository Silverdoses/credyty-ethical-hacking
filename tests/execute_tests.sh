#!/bin/sh
# Ejecuta el test con información detallada y luego
# el test simple para medir con mayor precisión el
# tiempo de ejecución.

python test_pwdfinder_verbose.py & process_id=$!
wait $process_id

echo ''
python test_pwdfinder.py
