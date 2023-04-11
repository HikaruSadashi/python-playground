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
    with open(fileName, 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            patientId = int(fields[0])
            if patientId not in patients:
                patients[patientId] = []
            visitData = [
                fields[1],  # date
                float(fields[2]),  # temperature
                int(fields[3]),  # heart rate
                int(fields[4]),  # respiratory rate
                int(fields[5]),  # systolic blood pressure
                int(fields[6]),  # diastolic blood pressure
                int(fields[7]),  # oxygen saturation
            ]
            patients[patientId].append(visitData)
    return patients


def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    if patientId != 0:
        # display data for a single patient
        if patientId in patients:
            visits = patients[patientId]
            print(f"Patient ID: {patientId}")
            for visit in visits:
                print(f"\tDate: {visit[0]}, Temperature: {visit[1]}, Heart Rate: {visit[2]}, Respiratory Rate: {visit[3]}, Systolic BP: {visit[4]}, Diastolic BP: {visit[5]}, Oxygen Saturation: {visit[6]}")
        else:
            print(f"Patient ID {patientId} not found")
    else:
        # display data for all patients
        for patientId, visits in patients.items():
            print(f"Patient ID: {patientId}")
            for visit in visits:
                print(f"\tDate: {visit[0]}, Temperature: {visit[1]}, Heart Rate: {visit[2]}, Respiratory Rate: {visit[3]}, Systolic BP: {visit[4]}, Diastolic BP: {visit[5]}, Oxygen Saturation: {visit[6]}")


def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    if patientId == 0:  # display stats for all patients
        num_patients = len(patients)
        total_temps = 0
        total_hr = 0
        total_rr = 0
        total_sbp = 0
        total_dbp = 0
        total_o2sat = 0
        total_visits = 0

        for visits in patients.values():
            for visit in visits:
                total_temps += visit[1]
                total_hr += visit[2]
                total_rr += visit[3]
                total_sbp += visit[4]
                total_dbp += visit[5]
                total_o2sat += visit[6]
                total_visits += 1

        avg_temp = total_temps / total_visits
        avg_hr = total_hr / total_visits
        avg_rr = total_rr / total_visits
        avg_sbp = total_sbp / total_visits
        avg_dbp = total_dbp / total_visits
        avg_o2sat = total_o2sat / total_visits

        print(f"Average temperature: {avg_temp:.2f}")
        print(f"Average heart rate: {avg_hr:.2f}")
        print(f"Average respiratory rate: {avg_rr:.2f}")
        print(f"Average systolic blood pressure: {avg_sbp:.2f}")
        print(f"Average diastolic blood pressure: {avg_dbp:.2f}")
        print(f"Average oxygen saturation: {avg_o2sat:.2f}")

    else:  # display stats for a single patient
        visits = patients.get(patientId, [])
        if not visits:
            print(f"No visits found for patient with ID {patientId}")
            return

        num_visits = len(visits)
        total_temps = 0
        total_hr = 0
        total_rr = 0
        total_sbp = 0
        total_dbp = 0
        total_o2sat = 0

        for visit in visits:
            total_temps += visit[1]
            total_hr += visit[2]
            total_rr += visit[3]
            total_sbp += visit[4]
            total_dbp += visit[5]
            total_o2sat += visit[6]

        avg_temp = total_temps / num_visits
        avg_hr = total_hr / num_visits
        avg_rr = total_rr / num_visits
        avg_sbp = total_sbp / num_visits
        avg_dbp = total_dbp / num_visits
        avg_o2sat = total_o2sat / num_visits

        print(f"Patient ID: {patientId}")
        print(f"Number of visits: {num_visits}")
        print(f"Average temperature: {avg_temp:.2f}")
        print(f"Average heart rate: {avg_hr:.2f}")
        print(f"Average respiratory rate: {avg_rr:.2f}")
        print(f"Average systolic blood pressure: {avg_sbp:.2f}")
        print(f"Average diastolic blood pressure: {avg_dbp:.2f}")
        print(f"Average oxygen saturation: {avg_os:.2f}")


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
    with open(fileName, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            patientId = int(data[0])
            visitData = [data[i] for i in range(1, len(data))]
            if patientId not in patients:
                patients[patientId] = [visitData]
            else:
                patients[patientId].append(visitData)
    return patients

def writePatientsToFile(patients, fileName):
    """
    Writes patient data to a plaintext file.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to write data from.
    fileName: The name of the file to write patient data to.
    """
    with open(fileName, 'w') as file:
        for patientId, visits in patients.items():
            for visit in visits:
                visitData = ','.join([str(patientId)] + visit) + '\n'
                file.write(visitData)

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    newVisit = [date, str(temp), str(hr), str(rr), str(sbp), str(dbp), str(spo2)]
    if patientId not in patients:
        patients[patientId] = [newVisit]
    else:
        patients[patientId].append(newVisit)
    writePatientsToFile(patients, fileName)

def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """

    # Display data for all patients if patientId is not specified
    if patientId == 0:
        for patient_id, visits in patients.items():
            print(f"Patient ID: {patient_id}")
            for visit in visits:
                print(f"\tDate: {visit[0]}, Temperature: {visit[1]}, Heart Rate: {visit[2]}, "
                      f"Respiratory Rate: {visit[3]}, Systolic Blood Pressure: {visit[4]}, "
                      f"Diastolic Blood Pressure: {visit[5]}, Oxygen Saturation: {visit[6]}")
    # Display data for a specific patient
    elif patientId in patients:
        visits = patients[patientId]
        print(f"Patient ID: {patientId}")
        for visit in visits:
            print(f"\tDate: {visit[0]}, Temperature: {visit[1]}, Heart Rate: {visit[2]}, "
                  f"Respiratory Rate: {visit[3]}, Systolic Blood Pressure: {visit[4]}, "
                  f"Diastolic Blood Pressure: {visit[5]}, Oxygen Saturation: {visit[6]}")
    # Patient not found in the dictionary
    else:
        print(f"Patient with ID {patientId} not found.")





def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    for patient_id, visits_list in patients.items():
        for visit in visits_list:
            visit_year = int(visit[0].split("-")[0])
            visit_month = int(visit[0].split("-")[1])
            if year is not None and visit_year != year:
                continue
            if month is not None and visit_month != month:
                continue
            visits.append((patient_id, visit))
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    for patient_id, visits in patients.items():
        for visit in visits:
            # Check if vital signs are outside normal range
            temp = visit[1]
            hr = visit[2]
            rr = visit[3]
            sbp = visit[4]
            dbp = visit[5]
            spo2 = visit[6]

            if temp > 100.4 or temp < 95.0:
                followup_patients.append(patient_id)
                break

            if hr > 100 or hr < 60:
                followup_patients.append(patient_id)
                break

            if rr > 20 or rr < 12:
                followup_patients.append(patient_id)
                break

            if sbp > 130 or sbp < 90 or dbp > 80 or dbp < 60:
                followup_patients.append(patient_id)
                break

            if spo2 < 95:
                followup_patients.append(patient_id)
                break

    # Remove duplicates from the list
    followup_patients = list(set(followup_patients))
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    # Remove the patient from the dictionary
    if patientId in patients:
        del patients[patientId]
        print(f"All visits of patient {patientId} have been deleted.")
    else:
        print(f"No visits found for patient {patientId}.")

    # Save the updated patient data to the file
    with open(filename, 'w') as file:
        for patientId, visits in patients.items():
            file.write(f"{patientId}\n")
            for visit in visits:
                file.write(",".join(str(val) for val in visit) + "\n")





###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()