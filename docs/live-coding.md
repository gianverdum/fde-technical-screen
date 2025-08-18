Live coding challange
Links:
Part 1: https://thoughtfulautomation.notion.site/FDE-Technical-Screen-12af43a78fa480af8d97c2fc9478cb18
Part 2: https://thoughtfulautomation.notion.site/FDE-Live-Coding-Interview-12af43a78fa480a99523f7a6a7fd3a7c
# FDE Live Coding Interview

### Objective

Our robotic arm's sorting function has been a great success in Thoughtful's robotic automation factory. Now, customers want to understand how their packages will be processed upfront. They have sent us CSV files with package details.

Your task is to analyze these packages, apply the sorting criteria using your existing function, and generate a comprehensive report. This report will show how their packages will be sorted and help them understand the efficiency and capacity of our robotic arm.

This challenge builds upon your initial sorting function, expanding its capabilities to meet real-world demand.

### Task Details

**Plan** (5 - 10 minutes)

- Read the instructions below and plan execution

**Data Ingestion** (15 - 20 minutes)

- Write code to read the data from `packages.csv` (below) and store it in an appropriate data structure for processing.
- Handle any data inconsistencies, errors, or missing values gracefully.

**Data Analysis and Reporting** (15 - 20 minutes)

- **Calculate Statistics**:
    - Total number of packages in the data artifact. This total is used in the statistics calculations for each stack.
    - Number and percentage of packages in each stack (`STANDARD`, `SPECIAL`, `REJECTED`).
    - Average, minimum, and maximum `Mass` and `Volume` for each stack.
- **Generate Summary Report**:
    - Display the statistics in a clear and organized format.
    - Ensure the report is easy to read and understand.

**Q&A** (5-10 mins)

- Spend a few minutes discussing potential improvements to the solution
    - How to handle extremely large datasets
    - Ways to enhance performance further
    - Additional features that could be added

### Guidance

- **Resources**: You are allowed to look up syntax and documentation as needed during the exercise.
- **Evaluation Criteria**: Your work will be assessed on:
    - Functionality
    - Code quality
    - Pragmatic choices

### Artifact

```python
Width,Height,Length,Mass
50,60,70,10
,None,50,5
200,100,50,25
150,150,150,30
60,80,100,-15
85,95,105,20
100,abc,100,40
20,30,40,0
95,105,115,24
100,100,100
45,55,65,12
-50,60,70,10
110,120,130,22
80,90,100,20,0
60,70,80,18
Width,Height,Length,Mass
140,150,160,35
70,80,90,15
,None,None,None
80,90,100,15
None,None,None,None
50,60,70,10
"100","100","100","40"
200,100,50,25
100,,100,40
30,40,50,5
150,150,150,30
55,65,75,14
60,80,100,15
90,100,110,26
100,100,100,40
85,80,75,14
20,30,40,8
70,65,60,12
90,95,100,20
55,50,45,10
65,75,85,16
,None,40,50,5
95,105,115,24
None,None,None,None
32,32,23ab,43
```


---------------


Suggested plan

Plano de execução (passo a passo, sem código)
1) Ingestão & Limpeza (15–20 min)

Ler o CSV de forma robusta (respeitar vírgulas, aspas).

Normalizar valores:

None (string), vazio → None.

Remover aspas, trim.

Tentar converter Width/Height/Length/Mass para float.

Validar:

Campos obrigatórios: para Volume, precisa de W, H, L.

Regras de negócio da sua função (ex.: valores > 0? limites?) — reaproveite.

Resultado de ingestão: lista de registros com:

width, height, length, mass, volume (ou None), stack, reject_reason (se houver).

Dica: trate cabeçalhos repetidos detectando linhas cujo primeiro campo seja "Width" e pule. Linhas com colunas sobrando: pegue apenas as quatro primeiras; se faltar, marque como rejeitado.

2) Classificação

Para cada registro “parseado”, chame a sua função de sorting para obter STANDARD | SPECIAL | REJECTED.

Se a classificação depender de volume/massa positivos, qualquer violação → REJECTED (com motivo).

3) Estatísticas (15–20 min)

Total = nº de linhas do artefato (inclua até as inválidas).

Para cada stack:

count e % = count / total.

Mass: média/min/máx considerando somente valores numéricos válidos.

Volume: idem (só quando calculável).

Se uma stack não tiver dados válidos para uma métrica, exiba “N/A”.

4) Relatório (output claro)

Seção Overview com Total.

Tabela por stack: count | % | Mass(avg/min/max) | Volume(avg/min/max)

Opcional: lista de motivos mais comuns de rejeição (top-N) — ajuda na leitura executiva.