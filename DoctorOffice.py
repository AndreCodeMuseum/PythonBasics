# Add patients to the line, call them when the doctor is ready to consult them. Also, a patient in urgency as the next to be called by the doctor

listNames = []

while True:
    print()
    patientNames = input("Patient: ")
    addUrgencyCall = input("Add, Urgency or Consult? ")
 
    print()
    if addUrgencyCall == "Add":
        listNames.append(patientNames)

    if addUrgencyCall == "Urgency":
        listNames.insert(0,patientNames)

    elif addUrgencyCall == "Consult":
        print(listNames[0], "It's your turn!!")
        del listNames[0]

    if patientNames == '':
        break
     
    for itens,i in enumerate(listNames,1):
        print(f"{itens} {i} " )
      
