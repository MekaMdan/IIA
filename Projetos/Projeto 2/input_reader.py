def symptoms():
    grausDeFebre = int(input("Em que grau está a sua febre? "))
    tempoDeFebre = int(input("Há quanto você está com febre? "))
    surgimentoManchas = int(input("Em qual dia de doença surgiram as manchas?"))
    dorNosMusculos = int(input(
        "Qual o nível da dor nos músculos? (1-baixa, 2-média, 3-alta) "))
    freqDorArticular = int(input(
        "Qual a frequência de dor articular? (1-baixa, 2-média, 3-alta) "))
    intensidadeDorArticular = int(input(
        "Qual a intensidade de dor articular? (1-leve, 2-moderada, 3-intensa) "))
    freqEdemaArticulacao = int(input(
        "Qual a frequência de edema da articulação? (5-frequente, 6-não frequente) "))
    edemaArticulacao = int(input(
        "Qual a intensidade de dor do edema? (1-leve, 2-moderado, 3-intenso) "))
    conjuntivite = int(input("Teve conjuntivite? (0-não, 1-sim) "))
    dorDeCabeca = int(input(
        "Qual a frequência e intensidade da dor de cabeça? (1-baixa, 2-média, 3-alta)? "))
    coceira = int(input(
        "Qual a intensidade da coceira? (1-leve, 2-moderada, 3-intensa)? "))
    hipertrofiaGanglionar = int(input(
        "Qual a situação da hipertrofia ganglionar? (1-leve, 2-moderada, 3-intensa)? "))
    discrasiaHemorragica = int(input(
        "Qual a situação da discrasia hemorrágica? (0-ausente, 1-leve, 2-moderada)? "))
    acometimentoNeurologico = int(input(
        "Apresenta acometimento neurológico? (0-não 1-sim)?"))

    return {'grauDeFebre': grausDeFebre, 'tempoDeFebre': tempoDeFebre, 'surgimentoManchas': surgimentoManchas, 'dorNosMusculos': dorNosMusculos, 'freqDorArticular': freqDorArticular,
            'IntensidadeDorArticular': intensidadeDorArticular, 'edemaArticulacao': edemaArticulacao, 'freqEdemaArticulacao': freqEdemaArticulacao,
            'conjuntivite': conjuntivite, 'dorDeCabeca': dorDeCabeca, 'coceira': coceira, 'hipertrofiaGanglionar': hipertrofiaGanglionar,
            'discrasiaHemorragica': discrasiaHemorragica, 'acometimentoNeurologico': acometimentoNeurologico}
