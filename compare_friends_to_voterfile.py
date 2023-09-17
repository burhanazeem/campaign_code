def find_person(last_name, first_name, voter_file):
    matching_records = []
    for record in voter_file:
        fields = record.split("|")
        if fields[2].strip().upper() == last_name.upper() and fields[3].strip().upper() == first_name.upper():
            matching_records.append(record)
    return matching_records

# Load voter file data from a text file
with open("49VOT_278256 (2).txt", "r") as f:
    voter_file = f.readlines()

# Load friends list from a text file
friends = []
with open("cambridge_friends_facebook.txt", "r") as f:
    for line in f:
        names = line.strip().split(" ")
        if len(names) >= 2:
            last_name = names[-1]
            first_name = names[0]
            friends.append({"last_name": last_name, "first_name": first_name})

# Find friends in the voter file
for friend in friends:
    matching_records = find_person(friend["last_name"], friend["first_name"], voter_file)
    if matching_records:
        print(f"Found records for {friend['first_name']} {friend['last_name']}:")
        for record in matching_records:
            print(record)
    else:
        print(f"No records found for {friend['first_name']} {friend['last_name']}.")
