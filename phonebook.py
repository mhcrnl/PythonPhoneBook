import sys
import os
"""
    Python program that will support creating, retrieving, updating and
    deleting Phonebook entries consisting of a name and a phone number.
    $ python phonebook.py create 'test1' => creaza o fila txt in directorul
        curent
"""
def create_phonebook(phonebook_name):
    """Create a new phonebook
    Args:
        phonebook_name (str): numele agendei care va fi creata
    """
    filename = '%s.txt' % phonebook_name
    if os.path.exists(filename):
        print "Fila exista!"
        quit()
    with open(filename, 'w') as f:
        pass
    
def add_entry(name, number, phonebook_name):
    """Add a new name and number to the given phonebook
    Args:
        name (str): numele contactului de adaugat
        number (str): numarul de telefon al contactului
        phonebook_name (str): numele agendei in care se adauga
    """
    filename = '%s.txt' % phonebook_name
    with open(filename, 'a') as f:
        f.write('%s\t%s' % (name, number))
        f.write('\n') #adauga o linie noua
 
def update_entry(name, new_number, phonebook_name):
    """Modificarea numarului de telefon al unui contact cu nume dat
    Args:
        name (str): numele contactului al carui numar de tel va fi modificat
        new_number (str): noul numar de telefon adaugat contactului
        phonebook_name (str): numele agendei 
    """
    pass
   
def remove_entry(name, phonebook_name):
    """Sterge un contact cu numele dat din agenda specificata
    Args:
        name (str): numele contactului de sters
        phonebook_name (str): numele agendei
    """
    pass
    
def lookup_name(name, phonebook_name):
    """Cauta contactul dupa nume in agenda specificata
    Args:
        name (str): numele de cautat
        phonebook_name (str): numele agendei
    """
    filename = '%s.txt' % phonebook_name
    with open(filename, 'r') as f:
        for line in f:
            entry_name, entry_number = line.strip().split('\t')
            if entry_name == name:
                print entry_name, entry_number
                
def lookup_number(number, phonebook_name):
    """Cauta contactul dupa numar in agenda specificata
    Args:
        numar (str): numarul de cautat
        phonebook_name (str): numele agendei
    """
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
        if len(args) != 3:
            print("Introduceti nume, numar de telefon, nume agenda")
            quit() 
        name = args.pop(0)
        number = args.pop(0)
        phonebook_name = args.pop(0)
        add_entry(name, number, phonebook_name)
        
    elif command == 'update':
        if len(args) != 3:
            print("Introduceti nume, numar de telefon, nume agenda")
            quit() 
        name, new_number, phonebook_name = args
        update_entry(name, new_number, phonebook_name)
        
    elif command == 'remove':
        if len(args) != 2:
            print "Introduceti numele contactului si agendei!"
            quit()
        name, phonebook_name = args
        remove_name(name, phonebook_name)
        
    elif command == 'lookup':
        if len(args) != 2:
            print "Introduceti numele contactului si agendei!"
            quit()
        name, phonebook_name = args
        lookup_name(name, phonebook_name)
        
    elif command == 'reverse-lookup':
        if len(args) != 2:
            print "Introduceti numarul contactului si agendei!"
            quit()
        number, phonebook_name = args
        lookup_number(number, phonebook_name)
        
    else:
        print "Comanda gresita!" 
        
    
    
    
