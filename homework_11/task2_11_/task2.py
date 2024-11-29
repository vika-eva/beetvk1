import json
import os
import re

file_phone = "phonebook2.json"

def load_contacts():
    if os.path.exists(file_phone):
        with open(file_phone, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(file_phone, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact_number(contacts):
    name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    number = input("Enter your number: ").strip()
    if len(number) > 12:
        print("Phone number should not exceed 10 digits.")
        return
    if not re.match(r'^\d+$', number):
        print("Phone number should contain only digits.")
        return
    city_state = input("Enter your city state: ")
    contacts[name] = {"name": name, "last_name": last_name, "number": number, "city_state": city_state}
    print(f"Contact '{name}' added.")



def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Last Name: {info['last_name']}")
        print(f"Phone: {info['phone']}")
        print(f"City State: {info['city_state']}\n")


def search_contact(contacts):
    search = input("Enter contact name to search: ").strip()
    if search in contacts:
        info = contacts[search]
        print(f"Name: {search}")
        print(f"Last Name: {info['last_name']}")
        print(f"Phone: {info['number']}")
        print(f"City State: {info['city_state']}")
    else:
        print("Contact not found.")


def search_contact_lastname(contacts):
    search = input("Enter your search last name: ")
    flag = True
    for search_contact in contacts:
        if contacts[search_contact]["last_name"] == search:
            print(contacts[search_contact]["last_name"])
            print(f"Name: {search_contact}")
            print(f"Last Name: {contacts[search_contact]['last_name']}, Phone: {contacts[search_contact]['number']}")
            #print(f"City State: {contacts[search_contact]['city_state']}")
            flag = False
    if flag:
        print("Contact not found.")



def search_phone(contacts):
    search = input("Enter your search phone number: ")
    flag = True
    for search_contact in contacts:
        if contacts[search_contact]["number"] == search:
            print(contacts[search_contact]["number"])
            print(f"Name: {search_contact}, last name: {contacts[search_contact]['last_name']}")
            flag = False
    if flag:
        print("Not found")


def search_city_state(contacts):
    search = input("Enter your search city state: ")
    flag = True
    for search_contact in contacts:
        if contacts[search_contact]["city_state"] == search:
            print(contacts[search_contact]["city_state"])
            print(f"Name: {search_contact}, last name: {contacts[search_contact]['last_name']}, Phone: {contacts[search_contact]['number']}")
            flag = False
    if flag:
        print("Not found")


def search_full_name():
    pass
    #search_contact(contacts)
    #search_contact_lastname(contacts)


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def update(contacts):
    search = input("Enter your search phone number: ")
    flag = True
    for search_contact in contacts:
        if contacts[search_contact]["number"] == search:
            print(contacts[search_contact]["number"])
            search1 = input("Enter your new phone number: ")
            contacts[search_contact]['number'] = search1
            print(f"Contact '{search_contact}' updated.")
            flag = False
    if flag:
        print("Contact not found")


def main_list_phone():
    print("hello, phonebook2 already to use")
    contacts = load_contacts()
    while True:
        print("Enter your command: \n"
              "1: add contact \n"
              "2: search name \n"
              "22: search last name \n"
              "23: search phone number \n"
              "24: search city/state \n"
              "25: search full name \n"
              "26: view contacts \n"
              "3: delete \n"
              "4: update \n"
              "5: exit \n")
        user_cmd = input("Enter your command: ")
        if user_cmd == "1":
            add_contact_number(contacts)
        elif user_cmd == "2":
            search_contact(contacts)
        elif user_cmd == "22":
            search_contact_lastname(contacts)
        elif user_cmd == "23":
            search_phone(contacts)
        elif user_cmd == "24":
            search_city_state(contacts)
        #elif user_cmd == "25":
        #    search_full_name(contacts)
        elif user_cmd == "26":
            view_contacts(contacts)
        elif user_cmd == "3":
            delete_contact(contacts)
        elif user_cmd == "4":
            update(contacts)
        elif user_cmd == "5":
            save_contacts(contacts)
            print("Contact save, bye")
            break
        else:
            print("Invalid command.")
            #with open("task_2/phonebook.json", "w", encoding="UTF-8") as file:
            #json.dump(list_phone, file, indent=4)
            #file.close()
            print("Thank you, phonebook closed")


main_list_phone()
