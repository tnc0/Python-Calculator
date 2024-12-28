def camelMatch(queries = ["FoeBac","FeoBac"], pattern = "FoBa", results = []):
    if(1 <= len(pattern) <= 100):
        print("")
    else:
        return False
    for word in queries:
        if(1 <= len(word) <= 100):
            print("")
        else:
            return False



    for word1 in queries:
        controlpattern = ""
        for character in word1:
            if(65 <= ord(character) <= 90):
                controlpattern += character
        if(pattern == controlpattern):
            results.append(True)
        else:
            results.append(False)
    return results

print(camelMatch())