def DNA_strand(dna):
    result = []
    for ch in dna:
        if ch == "A":
            result.append(ch.replace("A", "T"))
        if ch == "T":
            result.append(ch.replace("T", "A"))
        if ch == "C":
            result.append(ch.replace("C", "G"))
        if ch == "G":
            result.append(ch.replace("G", "C"))
    return "".join(result)






if __name__ == '__main__':
    print(DNA_strand("ATTGC"))