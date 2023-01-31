import collections

def delDuplicate ( dList ):
    '''Esta funcion recibe una lista y la ordena usando el metodo set
        dList : list
        return : list
    '''
    
    cleanList = list(set(dList) )
    
    return cleanList

def delConcatDuplicate ( list1, list2 ):
    '''Esta funcion recibe dos listas, las concatena y las ordena usando el metodo set para regresar solo una lista sin duplicados
        list1 : list
        list2 : list
        return : list
    '''
    cleanConcatList = list(set(list1 + list2) )
    
    return cleanConcatList

def delDuplicateInter ( list1, list2 ):
    '''Esta funcion recibe dos listas y retorna sus intersecciones usando el metodo set
        list1 : list
        list2 : list
        return : list
    '''
    inteseptionList = list(set(list1).intersection(list2))
    
    return inteseptionList

def delAfromB ( list1, list2 ):
    '''Esta funcion recibe dos listas y retorna sus los valores dentro de A que no estan en B usando el metodo set junto a difference
        list1 : list
        list2 : list
        return : list
    '''
    differenceList = list(set(list1).difference(set(list2)))
    
    return differenceList

def delCommon ( list1, list2 ):
    '''Esta funcion recibe dos listas y retorna sus diferencias usando el metodo set junto a symmetric_difference
        list1 : list
        list2 : list
        return : list
    '''
    differenceList = list(set(list1).symmetric_difference(set(list2)))
    
    return differenceList

def main( text1,text2 ):
    '''Esta funcion recibe un nombre de archivo y lo abre en modo de lectura e imrime 
        Las palabras que están en ambas listas sin repetir ninguna
        Las palabras que se repiten en ambas listas
        Las palabras que están en la primera lista y no están en la segunda
        Las palabras que están en la segunda lista y no en la primera
        Las palabras que están en la primera lista y en la segunda, pero no en amabas
        
        text : String
        return : null
    '''
    file1 = open(text1, 'r')
    lines1 = file1.readlines()
    file2 = open(text2, 'r')
    lines2 = file2.readlines()

    print("delDuplicate\n")
    print(delDuplicate( lines1 + lines2 ))
    print("\n\ndelConcatDuplicate\n")
    print(delConcatDuplicate( lines1, lines2 ))
    print("\n\ndelDuplicateInter\n")
    print(delDuplicateInter( lines1, lines2 ))
    print("\n\ndelAfromB\n")
    print(delAfromB( lines1 , lines2 ))
    print("\n\ndelCommon\n")
    print(delCommon( lines1 , lines2 ))
    



text1 ="demofile1.txt"
text2 ="demofile2.txt"
main(text1, text2)

