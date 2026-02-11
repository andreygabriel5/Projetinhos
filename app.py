import sqlite3 as sql
from datetime import *



with sql.connect("Banco") as conn:

    banco = conn.cursor()
 
    banco.execute("""CREATE TABLE IF NOT EXISTS Agendamento(

            id INTEGER PRIMARY KEY AUTOINCREMENT,            
            horario datetime NOT NULL      
                  
            );

""") 
    agen = False
    horario = input("Digite o horario: ")+":00"
    print(horario)
    data = date.today()
    horario_formatado = str(f"{data} {horario}")
    #banco.execute("DROP TABLE Agendamento")
    banco.execute("SELECT * FROM Agendamento;")
    dados = banco.fetchall()
    
    for i in dados:
        if horario_formatado in i:
            print("Horario já está agendado")
            agen = True
            
    if not agen: banco.execute(f"INSERT INTO Agendamento (horario) VALUES (?)",(horario_formatado,))
    
    
    for i in dados:
        print(f"ID: {i[0]} || Horario : {i[1]}")
    
   