# Dor nos músculos / Frequênca dor na articulação / Dor de cabeça
ALTA = 3
MEDIA = 2
BAIXA = 1

# Intensidade dor articular / coceira / discrasia / hipertrofia ganglionar
INTENSA = 3
MODERADA = 2
LEVE = 1
AUSENTE = 0

# Edema na articulação
EDEMA_RARO = 1
EDEMA_LEVE = 2
EDEMA_MODERADO = 3
EDEMA_INTENSO = 4

# Frequência do edema
EDEMA_FREQUENTE = 5
EDEMA_N_FREQUENTE = 6

# Acometimento Neurológico
ACOMETIMENTO_RARO = 0
ACOMETIMENTO_FREQ = 1

# Presença de conjuntivite
CONJUNTIVITE_AUSENTE = 0
CONJUNTIVITE = 1


def knowledge_base():
    return {
        'dengue': [
            {'grauDeFebre': 39, 'tempoDeFebre': 4, 'surgimentoManchas': 4, 'dorNosMusculos': ALTA, 'freqDorArticular': BAIXA,
             'IntensidadeDorArticular': LEVE, 'edemaArticulacao': EDEMA_RARO, 'freqEdemaArticulacao': EDEMA_N_FREQUENTE,
             'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': ALTA, 'coceira': LEVE, 'hipertrofiaGanglionar': LEVE,
             'discrasiaHemorragica': MODERADA, 'acometimentoNeurologico': ACOMETIMENTO_RARO},
            {'grauDeFebre': 40, 'tempoDeFebre': 5, 'surgimentoManchas': 4, 'dorNosMusculos': ALTA, 'freqDorArticular': BAIXA,
                'IntensidadeDorArticular': LEVE, 'edemaArticulacao': EDEMA_RARO, 'freqEdemaArticulacao': EDEMA_N_FREQUENTE,
                'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': ALTA, 'coceira': LEVE, 'hipertrofiaGanglionar': LEVE,
                'discrasiaHemorragica': MODERADA, 'acometimentoNeurologico': ACOMETIMENTO_RARO},
            {'grauDeFebre': 41, 'tempoDeFebre': 6, 'surgimentoManchas': 4, 'dorNosMusculos': ALTA, 'freqDorArticular': BAIXA,
                'IntensidadeDorArticular': LEVE, 'edemaArticulacao': EDEMA_RARO, 'freqEdemaArticulacao': EDEMA_N_FREQUENTE,
                'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': ALTA, 'coceira': LEVE, 'hipertrofiaGanglionar': LEVE,
                'discrasiaHemorragica': MODERADA, 'acometimentoNeurologico': ACOMETIMENTO_RARO},
            {'grauDeFebre': 42, 'tempoDeFebre': 7, 'surgimentoManchas': 4, 'dorNosMusculos': ALTA, 'freqDorArticular': BAIXA,
             'IntensidadeDorArticular': LEVE, 'edemaArticulacao': EDEMA_RARO, 'freqEdemaArticulacao': EDEMA_N_FREQUENTE,
             'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': ALTA, 'coceira': LEVE, 'hipertrofiaGanglionar': LEVE,
             'discrasiaHemorragica': MODERADA, 'acometimentoNeurologico': ACOMETIMENTO_RARO}
        ],
        'zika': [
            {'grauDeFebre': 37, 'tempoDeFebre': 0, 'surgimentoManchas': 1, 'dorNosMusculos': MEDIA, 'freqDorArticular': MEDIA,
             'IntensidadeDorArticular': LEVE, 'edemaArticulacao': EDEMA_LEVE, 'freqEdemaArticulacao': EDEMA_FREQUENTE,
             'conjuntivite': CONJUNTIVITE, 'dorDeCabeca': MEDIA, 'coceira': MODERADA, 'hipertrofiaGanglionar': LEVE,
             'discrasiaHemorragica': AUSENTE, 'acometimentoNeurologico': ACOMETIMENTO_FREQ},
            {'grauDeFebre': 38, 'tempoDeFebre': 1, 'surgimentoManchas': 2, 'dorNosMusculos': MEDIA, 'freqDorArticular': MEDIA,
                'IntensidadeDorArticular': MODERADA, 'edemaArticulacao': EDEMA_LEVE, 'freqEdemaArticulacao': EDEMA_FREQUENTE,
                'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': MEDIA, 'coceira': INTENSA, 'hipertrofiaGanglionar': LEVE,
                'discrasiaHemorragica': AUSENTE, 'acometimentoNeurologico': ACOMETIMENTO_FREQ},
            {'grauDeFebre': 38, 'tempoDeFebre': 2, 'surgimentoManchas': 2, 'dorNosMusculos': MEDIA, 'freqDorArticular': MEDIA,
             'IntensidadeDorArticular': MODERADA, 'edemaArticulacao': EDEMA_LEVE, 'freqEdemaArticulacao': EDEMA_FREQUENTE,
             'conjuntivite': CONJUNTIVITE, 'dorDeCabeca': MEDIA, 'coceira': INTENSA, 'hipertrofiaGanglionar': LEVE,
             'discrasiaHemorragica': AUSENTE, 'acometimentoNeurologico': ACOMETIMENTO_FREQ},
        ],
        'chikungunya': [
            {'grauDeFebre': 39, 'tempoDeFebre': 2, 'surgimentoManchas': 2, 'dorNosMusculos': BAIXA, 'freqDorArticular': ALTA,
             'IntensidadeDorArticular': MODERADA, 'edemaArticulacao': EDEMA_MODERADO, 'freqEdemaArticulacao': EDEMA_FREQUENTE,
             'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': MEDIA, 'coceira': LEVE, 'hipertrofiaGanglionar': MODERADA,
             'discrasiaHemorragica': LEVE, 'acometimentoNeurologico': ACOMETIMENTO_RARO},
            {'grauDeFebre': 41, 'tempoDeFebre': 3, 'surgimentoManchas': 5, 'dorNosMusculos': BAIXA, 'freqDorArticular': ALTA,
             'IntensidadeDorArticular': INTENSA, 'edemaArticulacao': EDEMA_INTENSO, 'freqEdemaArticulacao': EDEMA_FREQUENTE,
             'conjuntivite': CONJUNTIVITE, 'dorDeCabeca': MEDIA, 'coceira': LEVE, 'hipertrofiaGanglionar': MODERADA,
             'discrasiaHemorragica': LEVE, 'acometimentoNeurologico': ACOMETIMENTO_RARO
             },
            {'grauDeFebre': 42, 'tempoDeFebre': 3, 'surgimentoManchas': 4, 'dorNosMusculos': BAIXA, 'freqDorArticular': ALTA,
             'IntensidadeDorArticular': INTENSA, 'edemaArticulacao': EDEMA_INTENSO, 'freqEdemaArticulacao': EDEMA_FREQUENTE,
             'conjuntivite': CONJUNTIVITE_AUSENTE, 'dorDeCabeca': MEDIA, 'coceira': LEVE, 'hipertrofiaGanglionar': MODERADA,
             'discrasiaHemorragica': LEVE, 'acometimentoNeurologico': ACOMETIMENTO_RARO
             },
        ]
    }
