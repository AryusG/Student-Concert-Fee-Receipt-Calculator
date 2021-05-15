from pre_exam_concert_data import student_data, with_accompaniment_costs, no_accompaniment_costs

# Variables
final_cost = 0
audience_ticket = 10


print("Pre-Exam Concerts\n")

for i in range(2):
    new_dictionary = {}

    performer_name = input("Name of performer: ")
    new_dictionary['Performer name'] = performer_name

    performer_instrument = input("What instrument are you going to play?: ")
    new_dictionary['Instrument'] = performer_instrument

    student_data.append(new_dictionary)


# performer_grade = int(input("Current grade (level): "))
# audience_count = int(input("How many audience members?: "))
# requires_accompaniment = input("Does performer need accompaniment? Type 'y' for yes or 'n' for no: ")  # boolean



print(student_data)
