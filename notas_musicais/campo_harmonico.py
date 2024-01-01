def campo_harmonico(nota):
    """
    Gera o campo harmônico de uma nota.
    Args: 
        nota: Nota que será gerado o campo harmônico.
    Returns:
        Uma lista com as notas do campo harmônico.
    Raises:
        KeyError: Caso a nota não exista.
    Examples:
        >>> campo_harmonico('C', 'maior')
        ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bb']
        >>> campo_harmonico('C#', 'maior')
        ['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m', 'Cb']
        >>> campo_harmonico('D', 'maior')
        ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#b']
        >>> campo_harmonico('Eb', 'maior')
        ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Db']
        >>> campo_harmonico('E', 'maior')
        ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#b']
        >>> campo_harmonico('F', 'maior')
        ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim']
        >>> campo_harmonico('F#', 'maior')
        ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'Fb']
        >>> campo_harmonico('G', 'maior')
        ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#b']
        >>> campo_harmonico('Ab', 'maior')
        ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim']
        >>> campo_harmonico('A', 'maior')
        ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim']
        >>> campo_harmonico('Bb', 'maior')
        ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim']
        >>> campo_harmonico('B', 'maior')
        ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim']
    """
    notas = {
        'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bb'],
        'C#': ['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m', 'Cb'],
        'D': ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#b'],
        'Eb': ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Db'],
        'E': ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#b'],
        'F': ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Eb'],
        'F#': ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'Fb'],
        'G': ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#b'],
        'Ab': ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gb'],
        'A': ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#b'],
        'Bb': ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Ab'],
        'B': ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#b']
    }

    # Verifica se a nota está no dicionário
    if nota in notas:
        # Retorna o campo harmônico da nota
        return notas[nota]
    else:
        # Retorna uma lista vazia
        return []