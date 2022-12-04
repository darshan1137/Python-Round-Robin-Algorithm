# process_dictionary = {
#     "p1": 5,
#     "p2": 3,
#     "p3": 8,
#     "p4": 6
# }
process_dictionary = {}
no_of_process = int(input("Enter number of process: "))

for value in range(1, no_of_process+1):
    temp_p = "p"+str(value)
    temp_b = int(input(f"Enter Burst time of {temp_p}: "))
    process_dictionary[temp_p] = temp_b

store_list = []
process_table = {}
total_waiting_time = 0

quantam_time = int(input("Enter Quantam Time: "))
total_tat = 0

is_on = True

# for i in range(0, len(process_dictionary)):
while is_on:
    for i in process_dictionary:
        if process_dictionary.get(i) == 0:
            pass
        else:
            if quantam_time < process_dictionary.get(i):
                # print(i + ": 3")
                process_dictionary[i] = process_dictionary.get(i)-quantam_time
                total_tat += quantam_time
                store_list.append((i, quantam_time, total_tat))
            else:
                # print(i + ": " + str(process_dictionary.get(i)))
                total_tat += process_dictionary[i]
                store_list.append((i, process_dictionary[i], total_tat))
                process_dictionary[i] = 0

            x = process_dictionary.values()
            if sum(x) == 0:
                is_on = False

# print(total_tat)
# print(store_list)
# print("----------------------------------------------------------------------------------------------")
# print("Process Table\n")
print("\n----------------------------------------------------")
print("{:<8} {:<12} {:<13} {:<13}".format('Process','Burst Time','Waiting Time','Turn Around Time'))
print("----------------------------------------------------")


def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value[0] == item_to_find:
            indices.append(idx)
    return indices

# print(find_indices(store_list, "p1"))

for i in process_dictionary:
    burst_time = 0
    turn_around_time = 0
    waiting_time = 0

    indices = find_indices(store_list, i)
    for val in indices:
        burst_time += store_list[val][1]
    turn_around_time = store_list[indices[-1]][2]
    waiting_time = turn_around_time - burst_time

    process_table[i] = (burst_time, waiting_time, turn_around_time)
    total_waiting_time += waiting_time

for k, v in process_table.items():
    lang, perc, change = v
    print ("{:<8} {:<12} {:<13} {:<13}".format(k, lang, perc, change))

print(f"\nAverage Waiting time = Total Waiting time / Number of Process ")
print(f"                     = {str(total_waiting_time)} / {str(len(process_table))}")
print(f"                     = {str(round(total_waiting_time/no_of_process,2))} milliseconds")

print(f"\nAverage turn around time = Total Turn Around Time / Number of Process ")
print(f"                     = {str(total_tat)} / {str(len(process_table))}")
print(f"                     = {str(round(total_tat/no_of_process, 2))} milliseconds")



