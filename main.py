"""
sql-automation-starter
----------------------

Script para executar consultas SQL básicas em um banco de dados SQLite e
exportar os resultados para CSV. Caso o banco de dados ou tabela não
existam, ele cria uma tabela de exemplo com alguns registros.
"""

import argparse
import csv
import os
import sqlite3
from pathlib import Path
from typing import Iterable, List, Tuple


def ensure_sample_data(conn: sqlite3.Connection) -> None:
    """Cria tabela e insere dados de exemplo se ainda estiver vazia."""
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    # Verifica se há dados
    cur.execute("SELECT COUNT(*) FROM sales")
    count = cur.fetchone()[0]
    if count == 0:
        sample_data = [
            ("caderno", 10, 5.50),
            ("caneta", 20, 2.00),
            ("lapis", 15, 1.50),
            ("caderno", 5, 5.50),
            ("borracha", 8, 0.75),
        ]
        cur.executemany(
            "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data
        )
        conn.commit()


def run_query(conn: sqlite3.Connection, query: str) -> Tuple[List[str], List[Tuple]]:
    """Executa a consulta SQL e retorna cabeçalhos e linhas."""
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    headers = [description[0] for description in cur.description]
    return headers, rows


def export_to_csv(headers: List[str], rows: Iterable[Tuple], output_file: Path) -> None:
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Executa consultas SQL básicas em SQLite e exporta os resultados.")
    parser.add_argument("--db-file", default="data.db", help="Arquivo do banco de dados SQLite a ser utilizado")
    parser.add_argument("--output-file", default="output.csv", help="Arquivo CSV de saída para os resultados")
    parser.add_argument(
        "--query-file",
        default="",
        help="Arquivo .sql contendo a consulta a ser executada (opcional)",
    )
    args = parser.parse_args()
    db_path = Path(args.db_file)
    query_path = Path(args.query_file) if args.query_file else None

    conn = sqlite3.connect(db_path)
    try:
        ensure_sample_data(conn)
        if query_path and query_path.exists():
            query = query_path.read_text(encoding="utf-8")
        else:
            # Consulta padrão: soma das quantidades por produto
            query = "SELECT product, SUM(quantity) AS total_quantity, SUM(quantity * price) AS total_value FROM sales GROUP BY product"
        headers, rows = run_query(conn, query)
    finally:
        conn.close()
    export_to_csv(headers, rows, Path(args.output_file))
    print(f"Consulta executada e resultados salvos em {args.output_file}")


if __name__ == "__main__":
    main()
