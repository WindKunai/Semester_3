"""**Part2:** Read the phonebook CSV file and store the key/value data in the hashtable object created in the “My_HashTable class”, hashtable size is : max_size =4096

* take phone column as the key
* take the name column as the value

 (10 p)
"""

import csv

hash_table = MyHashTable()

with open('Phonebook.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        phone_number = row['phone']
        name = row['name']
        hash_table.insert(phone_number, name)

# write your code here