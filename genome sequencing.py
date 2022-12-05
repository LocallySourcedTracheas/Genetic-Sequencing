#Vanessa Junco
#COP2500 002
#Final Project
#11/20/22


#make a file that writes lines of DNA
#read the file
#make result

#REQUIREMENTS

#Input (Using the input command or using keyboard/mouse listener in pygame.
#Output (text, turtle, or something on the screen in pyGame)
#Variables
#If Statements
#Loops (For or While)
#Functions
#Lists
#Strings
 
import random

def menu():
    print("1. DNA Pairing")
    print("2. RNA Pairing")
    print("3. Exit")
    choice = int(input("What do you choose? (Enter a number)\n"))
    return choice


def dna_key(string):
    dna = [*string]
    sequence = []

    x = 0

    for x in range(len(dna)):
        
        if("A" in dna[x]):
            sequence.append("T")
        if("G" in dna[x]):
            sequence.append("C")
        if("C" in dna[x]):
            sequence.append("G")
        if("T" in dna[x]):
            sequence.append("A")

           
    new_sequence = ""
    return(new_sequence.join(sequence))


    
def rna_key(string):
    rna = [*string]
    sequence = []

    x = 0

    for x in range(len(rna)):
        
        if("A" in rna[x]):
            sequence.append("U")
        if("G" in rna[x]):
            sequence.append("C")
        if("C" in rna[x]):
            sequence.append("G")
        if("U" in rna[x]):
            sequence.append("A")

           
    new_sequence = ""
    return(new_sequence.join(sequence))


def dna_file(lines):
    sequence = []
    y = 0

    for x in range(lines):

        y = random.randint(0, 3)
            
        if(y == 0):
            sequence.append("A")
            
        if(y == 1):
            sequence.append("C")
            
        if(y == 2):
            sequence.append("G")
            
        if(y == 3):
            sequence.append("T")

    new_sequence = ""
    return new_sequence.join(sequence)
                

def rna_file(lines):
    sequence = []
    y = 0

    for x in range(lines):

        y = random.randint(0, 3)
            
        if(y == 0):
            sequence.append("A")
            
        if(y == 1):
            sequence.append("C")
            
        if(y == 2):
            sequence.append("G")
            
        if(y == 3):
            sequence.append("U")

    new_sequence = ""
    return new_sequence.join(sequence)


def main():
    fw = open("DNA_Sequence.txt","w")
    rw = open("RNA_Sequence.txt","w")

    print()
    print("Welcome to UCF Genome Sequencing Checker for BSC2010")
    print("This program will provide students a randomly generated string of DNA /RNA bases and the DNA pairing answer key")
    print("Students provide the amount of bases they want to practice with, should formulate their solution, and check their responses.")
    print()
    
    option = menu()

    
    while(option != 3):

        if(option == 1):
            x = int(input("How many bases of DNA do you want to pair."))
            fw.write(dna_file(x))
            fw.close()
            
            fw = open("DNA_Sequence.txt","r")
            j = fw.readline()
            p = str(dna_key(j))
            
            gw = open("DNA_Pair.txt", "w")
            gw.write(p)
            gw.close()
            
            print()
            print("DNA_Sequence file has been generated with the", x ,"random DNA bases.")
            print("DNA_Pair file has been generated with the", x ,"pair DNA bases.")
            print()

            
        if(option == 2):
            x = int(input("How many bases of DNA do you want to pair."))
            rw.write(rna_file(x))
            rw.close()
            
            rw = open("RNA_Sequence.txt","r")
            j = rw.readline()
            p = str(rna_key(j))
            
            gw = open("RNA_Pair.txt", "w")
            gw.write(p)
            gw.close()
            
            print()
            print("RNA_Sequence file has been generated with the", x ,"random RNA bases.")
            print("RNA_Pair file has been generated with the", x ,"pair RNA bases.")
            print()
            
        option = menu()
        
    fw.close()
    rw.close()
    
main()



