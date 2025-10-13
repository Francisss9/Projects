import csv
from datetime import date

def registar_dia(sono, gm, treino, book, trading, journal, cold_shower, hydration, nutrition, work):
    hoje = date.today().isoformat()
    
    with open("registro_diario.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Data", "Sono (horas)", "Ginásio", "Treino", "Leitura", 
                "Trading", "Análise de Mercado", "Banho Frio", 
                "Hidratação (litros)", "Nutrição", "Deveres"
            ])

        writer.writerow([
            hoje, sono, "Sim" if gm else "Não", "Sim" if treino else "Não", 
            "Sim" if book else "Não", "Sim" if trading else "Não",
            "Sim" if journal else "Não", "Sim" if cold_shower else "Não",
            hydration, "Sim" if nutrition else "Não", "Sim" if work else "Não"
        ])

