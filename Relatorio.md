# Relatório
    As duas tabelas vem originalmente no formato csv, para facilitar a manipulação dos seus dados o programa leCSV.py foi usado para converter os arquivos csv em dat, nessa conversão apenas os campos UF, nome do município, NIS favorecido, nome favorecido e valor parcela foram considerados.

    Os testes foram realizados com duas versões das tabelas, uma reduzida, com 1.000.000 de entradas para cada, e uma com todas as entradas das tabelas de janeiro e fevereiro, com 13.601.764 e 13.693.912 entradas respectivamente.

## Resultado dos testes
### Conversão
Usando o módulo cProfile foram obtidas essas informações:
    Tabela de janeiro reduzida:![cProfileJan1](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Reduzidos/Convers%C3%A3o/cProfile_jan_01.png)![cProfileJan2](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Reduzidos/Convers%C3%A3o/cProfile_jan_02.png)![cProfileJan3](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Reduzidos/Convers%C3%A3o/cProfile_jan_03.png)

    Tabela de fevereiro reduzida:![cProfileFev1](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Reduzidos/Convers%C3%A3o/cProfile_fev_01.png)![cProfileFev2](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Reduzidos/Convers%C3%A3o/cProfile_fev_02.png) ![cProfileFev3](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Reduzidos/Convers%C3%A3o/cProfile_fev_03.png)

    Tabela de janeiro:![cProfileJan1](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Completos/Convers%C3%A3o/cProfile_jan_01.png)![cProfileJan2](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Completos/Convers%C3%A3o/cProfile_jan_02.png)![cProfileJan3](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Completos/Convers%C3%A3o/cProfile_jan_03.png)

    Tabela de fevereiro reduzida:![cProfileFev1](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Completos/Convers%C3%A3o/cProfile_fev_01.png)![cProfileFev2](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Completos/Convers%C3%A3o/cProfile_fev_02.png) ![cProfileFev3](https://raw.githubusercontent.com/viniciusDGuimaraes/BPlusTree/master/Testes/Completos/Convers%C3%A3o/cProfile_fev_03.png)

### Comparação com força bruta
    Devido ao tempo de execução para a comparação de duas tabelas com 1.000.000 de entradas, foi usada uma versão com 100.000 entradas da tabela de janeiro. A tabela de fevereiro continou com 1.000.000 de entradas para o teste reduzido e 13.693.912 para o teste completo.

    Os seguintes resultados foram obtidos com a tabela reduzida de fevereiro:
       ..* 99.422 entradas iguais;
       ..* 578 entradas únicas na tabela de janeiro;
       ..* 55.098 acessos em média;
       ..* 1 hora, 29 minutos e 2 segundos de tempo de execução.

    Os seguintes resultados foram obtidos com a tabela completa de fevereiro:
       ..* 99.422 entradas iguais;
       ..* 578 entradas únicas na tabela de janeiro;
       ..* 128.468 acessos em média;
       ..* 3 horas, 21 minutos e 53 segundos.

### Comparaçao usando busca binária
    Para usar a busca binária o programa ordenaDat.py foi usado para realizar a separação do arquivo 'BolsaFamiliaFev.dat' em diversos arquivos contendo 100.000 entradas e depois foi realizado o merge externo desses arquivos, gerando um único arquivo ordenado pelo valor do NIS.

    O arquivo reduzido de fevereiro levou 11.6 segundos para ordenar, e o arquivo completo levou 5 minutos e 43 segundos para ordenar.

    Os resultados da busca binária usando os arquivos reduzidos foram:
       ..* 994.174 entradas iguais;
       ..* 5.826 entradas únicas na tabela de janeiro;
       ..* 18 acessos em média;
       ..* 1 minuto e 23 segundos de tempo de execução.

    Os resultados da busca binária usando os arquivos completos foram:
       ..* 13.522.298 entradas iguais;
       ..* 79.466 entradas únicas na tabela de janeiro;
       ..* 22 acessos em média;
       ..* 26 minutos e 50 segundos de tempo de execução.

### Comparação com tabela hash
    Para indexar o arquivo 'BolsaFamiliaFev.dat' foi usado o programa CriaIndice.py, e a comparação entre as duas tabelas foi feita com uma versão adaptada do programa ProcuraIndice.py.

    A indexação do arquivo reduzido levou 12.1 segundos, e a indexação do arquivo completo levou 1 hora, 7 minutos e 45 segundos.

    Os resultados da busca com tabela hash usando os arquivos reduzidos foram:
       ..* 994.174 entradas iguais;
       ..* 5.826 entradas únicas na tabela de janeiro;
       ..* 1,497 acessos em média;
       ..* 18 segundos de tempo de execução.

    Os resultados da busca com tabela hash usando os arquivos completos foram:
       ..* 13.522.298 entradas iguais;
       ..* 79.466 entradas únicas na tabela de janeiro;
       ..* 1,496 acessos em média;
       ..* 4 minutos e 22 segundos de tempo de execução.

### Resultado
#### Arquivos reduzidos
     | Força bruta | Busca binária | Tabela hash
    --- | --- | --- | ---
    Tempo de execução | 1h29m2s | 1m23s | 18s
    Média de acessos | 55.098 | 18 | 1,497

    A busca com tabela hash foi a mais rápida e a com menor número de acessos entre os três métodos usados, levando 0,33% do tempo que o método de força bruta leva, e 21,68% do tempo que o método de busca binária leva.

#### Arquivos completos
     | Força bruta | Busca binária | Tabela hash
    --- | --- | --- | ---
    Tempo de execução | 3h21m53s | 26m50s | 4m22s
    Média de acessos | 128.468 | 22 | 1,496

    A busca com tabela hash foi a mais rápida e a com menor número de acessos entre os três métodos usados, levando 2,16% do tempo que o método de força bruta leva, e 16,27% do tempo que o método de busca binária leva.
