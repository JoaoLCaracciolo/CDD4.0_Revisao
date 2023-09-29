horaInicio = int(input("Digite a hora de inicio:"))
horaFim = int(input("Digite a hora de fim:"))

horaTotal = 0

if horaInicio >= horaFim:
    horaTotal = 24 - horaInicio + horaFim
else:
    horaTotal = horaFim - horaInicio

print(f"O jogo durou {horaTotal}H")
