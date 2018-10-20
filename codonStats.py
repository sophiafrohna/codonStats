import sys
from random import randrange
#makes a dictionary with the correct info from the chart
def chart(co):
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    if co[0] == "c" and co[1] == "c" or co == "proline":
        infoDict = { 
            'name' : "Proline",
            'codedBy' : "either \"ccu\", \"ccc\", \"cca\", or \"ccg\"",
            'status' : "conditionally essential",
            'funFacts' : ["It's found in high concentrations in collagen.", "Its formula is C5H9NO2.".translate(SUB)]
        }
    elif co[0] == "c" and co[1] == "u" or co == "uua" or co == "uug" or co == "leucine":
        infoDict = {
            'name' : "Leucine",
            'codedBy' : "either \"uua\", \"uug\", \"cuu\", \"cuc\", \"cua\", or \"cug\"",
            'status' : "essential",
            'funFacts' : ["It's present in all living species, from humans to bacteria.", "Its formula is C6H13NO2.".translate(SUB)]
        }
    elif co[0] == "a" and co[1] == "c" or co == "threonine":
        infoDict = {
            'name' : "Threonine",
            'codedBy' : "either \"acu\", \"acc\", \"aca\", or \"acg\"",
            'status' : "essential",
            'funFacts' : ["It's abundant in human plasma.", "It's been used to alleviate anxiety and mild depression.", "Its formula is C4H9NO3.".translate(SUB)]
        }
    elif co[0] == "g" and co[1] == "g" or co == "glycine":
        infoDict = {
            'name' : "Glycine",
            'codedBy' : "either \"ggu\", \"ggc\", \"gga\", or \"ggg\"",
            'status' : "conditionally essential",
            'funFacts' : ["It's odorless, with a sweet taste.", "Its formula is C2H5NO2.".translate(SUB)]
        }
    elif co[0] == "c" and co[1] == "g" or co == "aga" or co == "agg" or co == "arginine":
        infoDict = {
            'name' : "Arginine",
            'codedBy' : "either \"aga\" or \"agg\"",
            'status' : "conditionally essential",
            'funFacts' : ["It helps dispose of ammonia.", "It's important to the healing of wounds.", "Its formula is C6H14N4O2.".translate(SUB)]
        }
    elif co[0] == "g" and co[1] == "c" or co == "alanine":
        infoDict = {
            'name' : "Alanine",
            'codedBy' : "either \"gcu\", \"gcc\", \"gca\", or \"gcg\"",
            'status' : "nonessential",
            'funFacts' : ["It's one of the most widely used amino acids in protein construction.", "Its formula is C3H7NO2.".translate(SUB)]
        }
    elif co[0] == "g" and co[1] == "u" or co == "valine":
        infoDict = {
            'name' : "Valine",
            'codedBy' : "either \"guu\", \"guc\", \"gua\", or \"gug\"",
            'status' : "essential",
            'funFacts' : ["When valine is mistakenly coded instead of glutamic acid in\nthe hemoglobin gene, sickle cell disease occurs.", "Its formula is C5H11NO2.".translate(SUB)]
        }
    elif co == "agu" or co == "agc" or co == "serine":
        infoDict = {
            'name' : "Serine",
            'codedBy' : "either \"cuu\", \"cuc\", \"cua\", \"cug\", \"agu\", or \"agc\"",
            'status' : "conditionally essential",
            'funFacts' : ["It has shown to play a significant role in brain development and function.", "Its formula is C3H7NO3.".translate(SUB)]
        }
    elif co == "cau" or co == "cac" or co == "histidine":
        infoDict = {
            'name' : "Histidine",
            'codedBy' : "either \"cau\" or \"cac\"",
            'status' : "essential",
            'funFacts' : ["It's important for the upkeep of myelin sheaths.", "It's named after its role in the production of histamine.", "Its formula is C6H9N3O2.".translate(SUB)]
        }
    elif co == "uau" or co == "uac" or co == "tyrosine":
        infoDict = {
            'name' : "Tyrosine",
            'codedBy' : "either \"uau\" or \"uac\"",
            'status' : "conditionally essential",
            'funFacts' : ["Its formula is C9H11NO3.".translate(SUB)]
        }
    elif co == "uaa" or co == "uag" or co == "uga" or co == "stop":
        infoDict = {
            'name' : "STOP",
            'codedBy' : "either \"uaa\", \"uag\", or \"uga\"",
            'status' : "conditionally essential",
            'extra' : "This codon is unique, because it encodes the direction \"STOP\". \nThere is no associated amino acid.",
            'funFacts' : ["If this codon is accidentally coded in the case of a single\nneucleotide polymorphism, it results in a premature stop codon,\nor \"nonsense\" codon, which can cause a protein to be incomplete\nand nonfunctional. Cystic fibrosis, for example, is caused by a\nnonsense codon in the CFTR gene.", "The three stop codons each have nicknames:\namber (uag), ochre (uaa), and opal (uga).", "The codon bias towards stop is likely because it reduces resource waste on nonfunctional proteins."]
        }
    elif co[0] == "a" and co[1] == "u" and co[2] != "g" or co == "isoleucine":
        infoDict = {
            'name' : "Isoleucine",
            'codedBy' : "either \"auu\", \"auc\", or \"aua\"",
            'status' : "essential",
            'funFacts' : ["When it's heated to decomposition, it emits toxic\nfumes of nitric oxide.", "Its formula is C6H13NO2.".translate(SUB)]
        }
    elif co == "aau" or co == "aac" or co == "asparagine":
        infoDict = {
            'name' : "Asparagine",
            'codedBy' : "either \"aau\" or \"aac\"",
            'status' : "nonessential",
            'funFacts' : ["It's one of the most common natural amino acids on earth.", "It was first isolated in 1806 from asparagus juice,\nhence the name \"asparagine\".", "Its formula is C4H8N2O3.".translate(SUB)]
        }
    elif co == "aaa" or co == "aag" or co == "lysine":
        infoDict = {
            'name' : "Lysine",
            'codedBy' : "either \"aaa\" or \"aag\"",
            'status' : "essential",
            'funFacts' : ["It seems to be active against herpes simplex viruses,\nlikely due to the viral need for the amino acid arginine,\nwhich lysine competes with.", "Its formula is C6H14N2O2.".translate(SUB)]
        }
    elif co == "ugu" or co == "ugc" or co == "cysteine":
        infoDict = {
            'name' : "Cysteine",
            'codedBy' : "either \"ugu\" or \"ugc\"",
            'status' : "conditionally essential",
            'funFacts' : ["It's one of only two proteinogenic amino acids to contain suflur,\nthe second being methionine.", "It's unique among the twenty natural amino acids, as it\ncontains a thiol group, which can undergo redox reactions.", "Its formula is C3H7NO2S.".translate(SUB)]
        }
    elif co == "caa" or co == "cag" or co == "glutamine":
        infoDict = {
            'name' : "Glutamine",
            'codedBy' :  "either \"caa\" or \"cag\"",
            'status' : "conditionally essential",
            'funFacts' : ["It's the most abundant free amino acid in human blood.", "Its formula is C5H10N2O3.".translate(SUB)]
        }
    elif co == "gau" or co == "gac" or co == "aspartic acid":
        infoDict = {
            'name' : "Aspartic acid",
            'codedBy' : "either \"gau\" or \"gac\"",
            'status' : "nonessential",
            'funFacts' : ["It's been noted to have a sour taste.", "Its formula is C4H7NO4.".translate(SUB)]
        }
    elif co == "uuu" or co == "uuc" or co == "phenylalanine":
        infoDict = {
            'name' : "Phenylalanine",
            'codedBy' : "either \"uuu\" or \"uuc\"",
            'status' : "essential",
            'funFacts' : ["At sufficiently high levels, it acts as a neurotoxin.", "Its formula is C9H11NO2.".translate(SUB)]
        }
    elif co == "gaa" or co == "gag" or co == "glutamic acid":
        infoDict = {
            'name' : "Glutamic acid",
            'codedBy' : "either \"gaa\" or \"gag\"",
            'status' : "nonessential",
            'funFacts' : ["Because of its role in synaptic plasticity, it'ss believed to be involved in cognitive functions like learning and memory.", "It's said to have an umami, sour taste.", "Its formula is C5H9NO4.".translate(SUB)]
        }
    elif co == "ugg" or co == "tryptophan":
        infoDict = {
            'name' : "Tryptophan",
            'codedBy' : "\"ugg\" alone",
            'status' : "essential",
            'funFacts' : ["It's a natural sedative and precursor to serotonin.", "The body's need for tryptophan decreases with age.", "Its formula is C9H11NO2.".translate(SUB)]
        }
    elif co == "aug" or co == "start" or co == "methionine":
        infoDict = {
            'name' : "Methionine",
            'codedBy' : "\"aug\" alone",
            'status' : "essential",
            'extra' : "Methionine is unique, because it encodes the direction \"START\".",
            'funFacts' : ["It's one of only two proteinogenic amino acids to contain suflur,\nthe second being cysteine.", "It's been noted to taste sulfurous.", "The absence of codon bias towards methionine likely\nreduces resource waste on nonfunctional proteins.", "Its formula is C5H11NO2S.".translate(SUB)]
        }
    return infoDict

#grabs essential state from dictionary
def essence(state):
    if state == "essential":
        return("An essential amino acid cannot be produced by the human body. \nIt instead must be obtained as a nutrient from food.")
    elif state == "nonessential":
        return("A nonessential amino acid is produced by the human body. \nIt does not need to be obtained as a nutrient from food.")
    else:
        return("A conditionally essential amino acid is usually produced by the human body, \nexcept in times of stress or illness. \nDuring these times, it instead must be obtained as a nutrient from food.")

#grabs essential state NOT from dictionary -- unused but good data
def isEssential(acid):
    essential = list(("histidine", "isoleucine", "leucine", "lysine", "methionine", "phenylalanine", "threonine", "tryptophan", "valine"))
    condEssential = list(("arginine", "cysteine", "glutamine", "tyrosine", "glycine", "proline", "serine"))
    nonEssential = list(("alanine", "asparagine", "aspartic acid", "glutamic acid"))

    if acid in essential:
        return "essential"
    elif acid in condEssential:
        return "conditionally essential"
    elif acid in nonEssential:
        return "nonessential"

def funFactGrabber(infoDict):
    liss = infoDict['funFacts']
    ind = randrange(0, len(liss))
    fact = liss[ind]
    return fact

#prints... everything
def printStuff(data):
    rep = True
    print("\n---" + data['name'].upper() + "---")
    print(f"This amino acid is called {data['name']}. \nIt can be coded by {data['codedBy']}.\n")
    more = (input("Would you like more information on this amino acid?\n")).lower()
    if more == "exit":
        sys.exit()
    print("")
    while rep == True:
        if more == "yes" or more == "y":
            rep = False
            print(f"{data['name']} is {data['status']}.")
            print(essence(data['status']) + "\n")
            if 'extra' in data: #checks if the acid requires additional info to be printed
                print(data['extra'] + "\n")
            print(testBias(data))
            if 'funFacts' in data:
                print("Fun fact: " + funFactGrabber(data) + "\n")
        elif more == "no" or more == "n":
            rep = False
            noth()
        else:
            rep = True
            more = input("Please enter one of the following: y/n/yes/no.\n")
            if more == "exit":
                sys.exit()
            print("")
        
#prints all info for every acid alphabetically
def printAllStuff():
    acids = ["proline", "leucine", "threonine", "glycine", "arginine", "alanine", "valine", "serine", "histidine", "tyrosine", "stop", "isoleucine", "asparagine", "lysine", "cysteine", "glutamine", "aspartic acid", "phenylalanine", "glutamic acid", "tryptophan", "start", "methionine"]
    acids = sorted(acids)
    for thing in acids:
        data = chart(thing)
        print("\n---" + data['name'].upper() + "---")
        print(f"This amino acid is called {data['name']}. \nIt can be coded by {data['codedBy']}.\n")
        print("")
        print(f"{data['name']} is {data['status']}.")
        print(essence(data['status']) + "\n")
        if 'extra' in data:
            print(data['extra'] + "\n")
        print(testBias(data))
        funSet = data['funFacts']
        for i in range (0, len(funSet)):
            print(funSet[i])
        print("\n")

#ensures a valid input and explains what went wrong with an invalid one
def checkString(codo):
    rep = True
    allowedBases = set("augc")
    allowedAcids = list(("proline", "leucine", "threonine", "glycine", "arginine", "alanine", "valine", "serine", "histidine", "tyrosine", "stop", "isoleucine", "asparagine", "lysine", "cysteine", "glutamine", "aspartic acid", "phenylalanine", "glutamic acid", "tryptophan", "start", "methionine"))
    while rep == True:
        if codo == "exit":
            sys.exit()
        elif len(codo) != 3 and codo not in allowedAcids:
            codo = input("\nPlease enter a single codon or a human amino acid.\n")
            if codo == "exit":
                sys.exit()
        elif (codo[0] not in allowedBases or codo[1] not in allowedBases or codo[2] not in allowedBases) and (codo not in allowedAcids):
            codo = input("\nPlease enter either a proteinogenic human amino acid or a codon consisting\nof only RNA bases.\n")
            if codo == "exit":
                sys.exit()
        else:
            print("\nYou entered: " + codo)
            rep = False
            return codo

#checks roughly how many codons code for a given acid
def testBias(am):
    span = len(am['codedBy'])
    if span < 12:
        return "This amino acid can only be encoded by one codon, and is therefore\nfree from codon bias.\n"
    else:
        return "Most amino acids, including this one, can be encoded by more than one codon.\nHowever, these options are not treated equally within actual genomes.\nCertain genomes have highly biased frequencies of synonymous codons.\nThis phenomenon is called codon usage bias.\n"

def noth():
    repp = input("Enter another? (y/n)\n")
    if repp == "exit":
        sys.exit()
    if repp == "yes" or repp == "y":
        glue()
    print("\nThank you. Shutting down.\n")
    sys.exit()

#puts it all together
def glue():
    entry = input("\nEnter a codon or amino acid.\n")
    if entry == "all":
        printAllStuff()
    elif entry == "exit":
        sys.exit()
    else:
        entry = checkString(entry)
        data = chart(entry)
        printStuff(data)
        noth()

def main():
    print("\nWelcome to codonStats.py!")
    glue()

#runs main
if __name__ == "__main__":
    main()
