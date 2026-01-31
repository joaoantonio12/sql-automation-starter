# sql-automation-starter

## Problema

Automatizar consultas SQL básicas em um banco de dados local é uma necessidade comum em tarefas de análise, mas muitas pessoas se intimidam com o setup de servidores ou linguagens específicas. Uma solução simples, usando apenas bibliotecas padrão do Python e SQLite, pode acelerar a criação de relatórios e a validação de dados.

## Solução

**sql-automation-starter** fornece um script em Python que cria (se necessário) um banco de dados SQLite local com dados de exemplo, executa consultas pré‑definidas ou personalizadas e exporta os resultados para um arquivo CSV. É ideal para demonstrações, aprendizado ou automação inicial de relatórios sem depender de bancos de dados externos.

## Como rodar

1. Tenha o Python 3.11 ou superior instalado.
2. Clone este repositório ou copie os arquivos para sua máquina.
3. (Opcional) Crie um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate    # Windows
   ```
4. Não há dependências externas; as bibliotecas padrão do Python são suficientes.
5. Execute o script para gerar um arquivo de exemplo e produzir relatórios:

   ```bash
   python main.py --db-file banco.db --output-file relatorio.csv
   ```

   Para executar uma consulta personalizada, forneça um arquivo SQL:

   ```bash
   python main.py --db-file banco.db --output-file relatorio.csv --query-file consultas.sql
   ```

## Exemplo de uso

Ao rodar sem `--query-file`, o script irá:

- Criar a tabela `sales` se ela não existir.
- Inserir alguns registros de exemplo (produto, quantidade e valor).
- Executar um `SELECT` de soma de quantidades por produto.
- Exportar o resultado para `relatorio.csv`.

## Limitações

- O banco de dados SQLite é armazenado no arquivo especificado. Para bancos relacionais mais robustos (PostgreSQL, MySQL) será necessário adaptar o código.
- As consultas de exemplo são simples; não há tratamento de injeção de SQL ou optimizações avançadas.
- O script sobrescreve o arquivo de saída sem confirmação prévia.

## Próximos passos

- Adicionar suporte a parâmetros nas consultas via arquivo `.sql`.
- Permitir múltiplas consultas e exportação de várias tabelas.
- Implementar geração de gráficos simples a partir dos resultados exportados.
