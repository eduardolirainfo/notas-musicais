NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {
    'maior': (0, 2, 4, 5, 7, 9, 11),
    'menor': (0, 2, 3, 5, 7, 8, 10),
    'diminuta': (0, 1, 3, 4, 6, 8, 10),
}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera  uma escala a partir de uma tonica e uma tonalidade

    Parameters:
        tonica: Nota de referencia da escala
        tonalidade: Tonalidade da escala
    Returns:
        Um dicionario com as notas e os graus da escala
    Raises:
        ValueError: Se a nota não existir
        KeyError: Se a tonalidade não existir ou não estiver implementada
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escala('A', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    tonica = tonica.upper()
    try:
        intervalos = ESCALAS[tonalidade]
        tonica_posicao = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(
            f'Essa nota não existe, tente uma das seguintes: {NOTAS}'
        )
    except KeyError:
        raise KeyError(
            'Essa escala não existe ou ainda não foi implementada.'
            f' Tente uma dessas: {list(ESCALAS.keys())}'
        )

    temp = []
    for intervalo in intervalos:
        nota = (tonica_posicao + intervalo) % 12
        temp.append(NOTAS[nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
