from datetime import date
from DB import DB


testdb = DB()


data = [
    ('21458', 'test', 'test', date(2022, 1, 5), 'THIES', 'Masculin', 'Malienne', '0', 'dessin', '1')
]
#stmt = "INSERT INTO candidat (numero_table, prenom_s, nom, date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epreuve_facultative, aptitude_sportive) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"

#testdb.insertmany(stmt, data)
sql='SELECT * FROM candidat'
print(testdb.fetch(sql))