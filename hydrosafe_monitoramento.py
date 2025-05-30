# Aluno: [Seu Nome Aqui]
# RM: [Seu RM Aqui]
# Projeto: HydroSafe - Simulador de Monitoramento de Enchentes
# Disciplina: Computational Thinking Using Python

def input_dados():
    """
    Coleta os dados do nível do rio nos últimos 10 dias.
    Os dados são inseridos manualmente para simular sensores.
    """
    print("Digite os níveis de água (em metros) para os últimos 10 dias:")
    niveis = []
    for i in range(1, 11):
        while True:
            try:
                nivel = float(input(f"Dia {i}: "))
                if nivel < 0:
                    print("O nível não pode ser negativo. Tente novamente.")
                    continue
                niveis.append(nivel)
                break
            except ValueError:
                print("Entrada inválida. Digite um número.")
    return niveis

def analisar_nivel(nivel):
    """
    Classifica o nível de risco com base na altura da água.
    """
    if nivel < 1.0:
        return "Baixo"
    elif 1.0 <= nivel <= 2.0:
        return "Médio"
    else:
        return "Alto"

def emitir_alerta(niveis):
    """
    Emite um alerta para cada nível informado.
    """
    print("\n--- ALERTAS DE RISCO ---")
    for i, nivel in enumerate(niveis):
        risco = analisar_nivel(nivel)
        if risco == "Alto":
            print(f"Dia {i+1}: Nível = {nivel:.2f}m -> RISCO ALTO! ⚠️ Ação imediata recomendada.")
        elif risco == "Médio":
            print(f"Dia {i+1}: Nível = {nivel:.2f}m -> Risco Médio. Monitoramento necessário.")
        else:
            print(f"Dia {i+1}: Nível = {nivel:.2f}m -> Risco Baixo. Situação estável.")

def gerar_relatorio(niveis):
    """
    Gera um relatório estatístico dos dados inseridos.
    """
    max_nivel = max(niveis)
    min_nivel = min(niveis)
    media = sum(niveis) / len(niveis)
    dia_critico = niveis.index(max_nivel) + 1

    print("\n--- RELATÓRIO FINAL ---")
    print(f"Nível máximo: {max_nivel:.2f}m no dia {dia_critico}")
    print(f"Nível mínimo: {min_nivel:.2f}m")
    print(f"Média dos níveis: {media:.2f}m")
    dias_risco_alto = sum(1 for n in niveis if n > 2.0)
    print(f"Dias com risco alto: {dias_risco_alto} de {len(niveis)}")

def main():
    print("===== HydroSafe - Monitoramento de Enchentes =====")
    niveis = input_dados()
    emitir_alerta(niveis)
    gerar_relatorio(niveis)

# Execução do programa
if __name__ == "__main__":
    main()
