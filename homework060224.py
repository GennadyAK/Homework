#1
def spec(x: int) -> bool:
    z = set(str(x))
    print(z)
    if z <= {'0', '1', '2', '3', '4', '5'}:
        return "Число специальное"
    else:
        return "Число не специальное"


#2(не мое)
def counter(array: str) -> int:
    vowels = 'aeiou'
    res = []
    for word in array.split():
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
        if count > 3:
            res.append(word)
    return len(res)

#2.1
def vowel_count_gt_three(word: str) -> bool:
    vowels, vowels_count = 'aeiou', 0
    for letter in word.lower():
        if letter in vowels:
            vowel_count += 1
    return vowel_count > 3

def counter(array: str) -> int:
    vowels = 'aeiou'
    res = [word for word in array.split() for vowel_count_gt_three(word)]
    word_count = len(res)
    return word_count


#3
import random
from random import randint

def password():
    return ''.join([random.choice(chr(randint(48, 57)) +
                                  chr(randint(65, 90)) +
                                  chr(randint(97, 122))) for _ in range(randint(8, 15))])

print(password())


#4*
from random import choice

NAMES = ["Alex", "John", "Bob", "Ted"]
NUMBERS = ["+124", "+15834", "+18542", "+38949"]

CRED = NAMES + NUMBERS

def gen_contact_list(count: int) -> list:
    contacts = []
    for _ in range(count):
        contacts.append({"Name": choice(NAMES), "Phone": choice(NUMBERS)})
    return contacts

def call(contact_list: list[dict], cred: str) -> str or Exception:
    for contact in contact_list:
        if cred in (contact["Name"], contact["Phone"]):
            return f"Call {contact["Name"]} {contact["Phone"]}"
    return ValueError("Contact not found")

print(call(contact_list=gen_contact_list(3), cred=choice(CRED)))
