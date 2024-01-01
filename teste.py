def gerar_escala(nota):
    nota = normalizar_nota(nota)

    acidentes_sharp = ["F#", "C#", "G#", "D#", "A#", "E#"]
    acidentes_flat = ["Bb", "Eb", "Ab", "Db", "Gb"]

    if nota in acidentes_sharp:
        return gerar_escala_com_acidente(nota, "#")
    elif nota in acidentes_flat:
        return gerar_escala_com_acidente(nota, "b")
    else:
        return gerar_escala_natural(nota)


def normalizar_nota(nota):
    notas_validas = [
        "C",
        "C#",
        "Db",
        "D",
        "D#",
        "Eb",
        "E",
        "F",
        "F#",
        "Gb",
        "G",
        "G#",
        "Ab",
        "A",
        "A#",
        "Bb",
        "B",
    ]
    nota = nota.capitalize()
    if nota not in notas_validas:
        raise ValueError("Nota inválida.")
    return nota


def gerar_escala_natural(nota):
    indice_nota = ["C", "D", "E", "F", "G", "A", "B"]
    indice_escala = ["M", "m", "m", "M", "M", "m", "dim"]

    index = indice_nota.index(nota)
    escala = []

    for i in range(7):
        nota_atual = indice_nota[index % 7]
        escala.append(nota_atual + indice_escala[i])
        index += 1

    return escala


def gerar_escala_com_acidente(nota, acidente):
    indice_nota = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    indice_escala = ["M", "m", "m", "M", "M", "m", "dim"]

    index = indice_nota.index(nota)
    escala = []

    for i in range(7):
        nota_atual = indice_nota[index % 12]
        if acidente in nota_atual:
            escala.append(nota_atual + indice_escala[i])
        else:
            escala.append(nota_atual.lower() + indice_escala[i])
        index += 1

    return escala


# Exemplo de uso:
try:
    nota_usuario = input("Informe a nota desejada: ").strip()
    escala = gerar_escala(nota_usuario)

    if escala:
        print(f'A escala de {nota_usuario} é: {", ".join(escala)}')
    else:
        print("Nota inválida.")
except ValueError as e:
    print(f"Erro: {e}")
