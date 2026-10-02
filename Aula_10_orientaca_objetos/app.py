from aluno import Aluno
from diciplina import Diciplina

#aulno 1
aluno1 = Aluno("joao", "123456", "Ciência da computação")
# print(aluno1.notas_por_disciplina)

# disciplina
dsa = Diciplina("Data Strucuters", "Álvaro")
model_lin = Diciplina("Modelagem Linear", "Rodolfo")
# print(model_lin.professor)
# model_lin.exibir_infos()

# matricular aluno
aluno1.matricular(dsa)
aluno1.matricular(model_lin)
# print(aluno1.disciplinas[0].professor)

# adicionar notas do aluno referente as disciplinas

aluno1.adicionar_nota(dsa, 10)
aluno1.adicionar_nota(dsa, 8)
aluno1.adicionar_nota(model_lin, 5)
aluno1.adicionar_nota(model_lin, 3)
print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(model_lin))