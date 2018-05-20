import sys
import os
"""
    Python program that will support createng, retrieving, updating and
    deleting Phonebook entries consisting of a name and a phone number.
    $ python phonebook.py create 'test1' => creaza o fila txt in directorul
        curent
"""
def create_phonebook(phonebook_name):
    """Create a new phonebook"""
    filename = '%s.txt' % phonebook_name
    if os.path.exists(filename):
        print "Fila exista!"
        quit()
    with open(filename, 'w') as f:
        pass
    
def add_entry(name, number, phonebook_name):
    """Add a new name and number to the given phonebook"""
    with open(filename, 'a') as f:
        f.write('%s\t%s' % (name, number))
        f.write('\n') #adauga o linie noua
    pass
    
if __name__ == '__main__':
    args = sys.argv[:]
    script = args.pop(0)
    if not args:
        print("Numar insuficient de argumente.")
        quit()
    command = args.pop(0)
    
    if command == 'create':
        if len(args) != 1:
            print("Numele agendei trebuie specificat")
            quit()
        phonebook_name = args.pop(0)
        create_phonebook(phonebook_name)
        
    elif command == 'add':
        name = args.pop(0)
        number = args.pop(0)
        phonebook_name = args.pop(0)
        add_entry(name, number, phonebook_name)
    
    
