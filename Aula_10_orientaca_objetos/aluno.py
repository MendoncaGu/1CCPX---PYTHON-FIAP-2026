from diciplina import Diciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplina = {}

    def matricular(self, disciplina: Diciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Diciplina, nota: float):
        self.notas_por_disciplina[disciplina.nome].append(nota)

    def calcular_media_d(self, d: Diciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        return sum(notas) / len(notas)


