#!/bin/bash
set -euo pipefail

# Compila módulos Python para verificar sintaxe
python -m compileall .

# Executa consulta padrão em um banco temporário
python main.py --db-file tmp_test.db --output-file tmp_output.csv

echo "Verificação concluída com sucesso. Resultado salvo em tmp_output.csv"
