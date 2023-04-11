from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    ####################### MY CODE HERE

    # use built in open function and the given filename
    myFile = open(fileName, 'r') 

    # iterate on every line in the file
    for line in myFile:

        # split the line string at every comma to a new list/arr
        dataArr = line.strip().split(',')

        # the first element in the data array is our ID
        patientIdNum = int(dataArr[0])
        
        # If the recorded data point is for a new ID we create a new one
        if patientIdNum not in patients:
            patients[patientIdNum] = []
        
        # Extract the list of fields from our data array into a list
        patientDataList = [
            dataArr[1],  
            float(dataArr[2]),  
            int(dataArr[3]),  
            int(dataArr[4]),  
            int(dataArr[5]), 
            int(dataArr[6]), 
            int(dataArr[7]),  
        ]

        # Append our list
        patients[patientIdNum].append(patientDataList)

    #######################
    return patients

def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #######################

    # If the ID chosen is 0, which means display all patients and their data
    if patientId != 0:
        
        # check if the ID exists first
        if patientId in patients:

            #create a visits list from the patients dictionary
            visits = patients[patientId]

            # iterate over the visits and display them in the right format
            print(f"Patient ID: {patientId}")
            for visit in visits:
                print(f" Visit Date: {visit[0]}")
                print(f"  Temperature: {visit[1]}")
                print(f"  Heart Rate: {visit[2]}")
                print(f"  Respiratory Rate: {visit[3]}")
                print(f"  Systolic BP: {visit[4]}")
                print(f"  Diastolic BP: {visit[5]}")
                print(f"  Oxygen Saturation: {visit[6]}")
        else:
            print(f"Patient ID {patientId} not found")
    else:

        # Iterate over every single visit item in the patients dictionary
        for patientId, visits in patients.items():

            # iterate over the visits and display them in the right format
            print(f"Patient ID: {patientId}")
            for visit in visits:
                print(f" Visit Date: {visit[0]}")
                print(f"  Temperature: {visit[1]}")
                print(f"  Heart Rate: {visit[2]}")
                print(f"  Respiratory Rate: {visit[3]}")
                print(f"  Systolic BP: {visit[4]}")
                print(f"  Diastolic BP: {visit[5]}")
                print(f"  Oxygen Saturation: {visit[6]}")
    #######################



# testing
patients = readPatientsFromFile('patients.txt')
#print(patients)

# Displaying patient 1
displayPatientData(patients, 0)

print("SECOND TEST:")
# Displaying patient 2
#patientIdInt = 2
#displayPatientData(patients, patientIdInt)