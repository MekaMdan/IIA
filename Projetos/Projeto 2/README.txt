Projeto 2 - IIA
Fernanda Macedo de Sousa - 170010058
Mariana Alencar do Vale - 160014522 

Descrição:

O programa foi implementado usando uma biblioteca que utiliza a lógica de probabilidade Bayesiana.
O arquivo knowledge_base.py possui a descrição da base de conhecimento do sistema especialista.
O arquivo input_reader.py é responsável pela leitura de sintomas do paciente pelo terminal.
O arquivo main.py é responsável por chamar o classificador. O classificador, por sua vez, 
chama a função de leitura e atribui o resultado à função de classificação. 
Uma vez determinada a classificação, o resultado final será apresentado no terminal.

Instalação:

Biblioteca de classificação utilizada: https://pypi.org/project/Bayesian/0.3.1/
Comando para instalação da biblioteca: pip install Bayesian==0.3.1

Execução do programa: python3 main.py