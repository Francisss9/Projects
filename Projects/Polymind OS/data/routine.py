from core.logger import registar_dia

def main():
    sono = float(input("Horas de sono: ")).strip().replace(',', '.')
    if sono < 7.0:
        print("Lembra-te de dormir pelo menos 7 horas por dia.")
    elif sono > 9.0:
        print("Dormir mais de 9 horas pode ser contraproducente.")
    
    gm = float(input("Disseste bom dia a alguém hoje (s/n): ")).strip().lower() == 's'
    if gm:
        print("Excelente! Dizer bom dia é uma ótima forma de começar o dia com energia positiva.")
    else:
        print("Tenta dizer bom dia a alguém todos os dias, é uma forma simples de espalhar positividade e manter consistência.")


    treino = float(input("Treinaste hoje (s/n): ")).strip().lower() == 's'
    if not treino:
        print("Lembra-te de treinar pelo menos 5 vezes por semana.")
    

    hydration = float(input("Litros de água: ")).replace(',', '.')
    if hydration < 2.0:
        print("Lembra-te de beber pelo menos 2 litros de água por dia.")
    elif hydration > 4.0:
        print("Beber mais de 4 litros de água pode ser excessivo.")
    else:
        print("Ótimo, continua assim, a tua hidratação é como o combustível de um carro, sem ele o carro não anda!")


    book = float(input("Leste hoje (s/n): ")).strip().lower() == 's'
    if book:
        print("Excelente! A leitura é uma ótima forma de relaxar e aprender.")
    else:
        print("Tenta ler pelo menos 20 minutos por dia, é muito benéfico para a tua mente.")

    
    trading = float(input("Fizeste trading hoje (s/n): ")).strip().lower() == 's'
    if trading:
        print("Bom trabalho! O trading é a tua tarefa principal todos os dias, é a tua skill!.")
    else:
        print("Lembra-te de praticar trading diariamente, é importante para o teu desenvolvimento.")

    
    journal = float(input("Já analisaste o mercado hoje? (s/n): ")).strip().lower() == 's'
    if journal:
        print("Excelente! Analisar o mercado é crucial para o teu sucesso no trading.")
    else:
        print("Tenta fazer uma análise de mercado diariamente, é fundamental para a tua evolução.")

    
    cold_shower = float(input("Tomaste um banho frio hoje (s/n): ")).strip().lower() == 's'
    if cold_shower:
        print("Bom trabalho! Banhos frios ajudam a melhorar a circulação e a energia.")
    else:
        print("Tenta tomar um banho frio diariamente, é ótimo para a tua saúde e bem-estar e também para manteres a tua consistência.")


    nutrition = float(input("Comeste bem e tomaste os suplementos hoje (s/n): ")).strip().lower() == 's'
    if nutrition:
        print("Excelente! Uma boa nutrição é fundamental para o teu desempenho.")
    else:
        print("Lembra-te de cuidar da tua alimentação e tomar os suplementos necessários, é essencial para a tua saúde e performance.")
    

    work = float(input("Fizeste o teu dever de hoje (s/n): ")).strip().lower() == 's'
    if work:
        print("Bom trabalho! Cumprir os teus deveres é importante para a tua disciplina e sucesso.")
    else:
        print("Tenta cumprir os teus deveres diariamente, é fundamental para a tua disciplina e sucesso.")
    


    registar_dia(sono, gm, treino, book, trading, journal, cold_shower, hydration, nutrition, work)



if __name__ == "__main__":
    main()
# This code is part of a daily routine tracker that prompts the user for various health and productivity-related inputs.