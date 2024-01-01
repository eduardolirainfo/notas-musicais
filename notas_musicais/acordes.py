from notas_musicais.escalas import NOTAS, escala


def _menor(cifra):
    nota, _ = cifra.split("m")
    if "+" in cifra:
        tonica, terca, quinta = triade(nota, "menor")
        notas = [tonica, terca, semitom(quinta, intervalo=1)]
        graus = ["I", "III-", "V+"]
    else:
        notas = triade(nota, "menor")
        graus = ["I", "III-", "V"]
    return notas, graus


def semitom(nota, *, intervalo):
    pos = NOTAS.index(nota) + intervalo
    return NOTAS[pos % 12]


def triade(nota, tonalidade):
    """
    Gera triades a partir de uma tônica e uma tonalidade.

    Parameters:
        nota: Uma nota da qual se deseja obter um acorde
        tonalidade: Tonalidade na qual será formado o acorde

    Returns:
        A tríade do acorde referente a nota e a tonalidade

    Examples:
        >>> triade('C', 'maior')
        ['C', 'E', 'G']

        >>> triade('C', 'menor')
        ['C', 'D#', 'G']
    """
    graus = (0, 2, 4)
    notas_da_escala, _ = escala(nota, tonalidade).values()
    return [notas_da_escala[grau] for grau in graus]


def acorde(cifra):
    """
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

        >>> acorde('C°')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}

        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}

        >>> acorde('Cm+')
        {'notas': ['C', 'D#', 'G#'], 'graus': ['I', 'III-', 'V+']}
    """

    if "m" in cifra and "dim" not in cifra:
        notas, graus = _menor(cifra)
    elif "°" in cifra or "dim" in cifra:
        case = cifra.split("°")
        if len(case) > 1:
            nota, _ = cifra.split("°")
        else:
            nota, _ = cifra.split("dim")
        tonica, terca, quinta = triade(nota, "menor")
        notas = [tonica, terca, semitom(quinta, intervalo=-1)]
        graus = ["I", "III-", "V-"]
    elif "+" in cifra or "aug" in cifra:
        case = cifra.split("+")
        if len(case) > 1:
            nota, _ = cifra.split("+")
        else:
            nota, _ = cifra.split("aug")
        tonica, terca, quinta = triade(nota, "maior")
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ["I", "III", "V+"]
    else:
        notas = triade(cifra, "maior")
        graus = ["I", "III", "V"]
    return {"notas": notas, "graus": graus}
