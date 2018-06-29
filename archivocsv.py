import csv
#doc=open("archivow.csv","w")
#doc_csv_w=csv.writer(doc)

#lista=[["andrea",99836],["uno",1000],["DOS",20000],["RES",4000],["CUATRO",5000]]
#for x in lista:
#    doc_csv_w.writerow(x)
#    
#doc_csv_w.writerow(lista)
#doc.close()

#leer archivos

doc2=open("archivow.csv","r")

doc_csv=csv.reader(doc2)

for(nombre,numero) in doc_csv:
    print nombre,numero

doc2.close()
