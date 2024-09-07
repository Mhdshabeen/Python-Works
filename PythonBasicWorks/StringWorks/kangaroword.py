# write a prgm to check the given word is kangaroo word or not


def is_kangarooword(parentword,childword):

    sorted_parentword=sorted(parentword)

    sorted_childword=sorted(childword)

    for char in sorted_childword:

        if sorted_childword.count(char)==sorted_parentword.count(char):

            return True
        else:

            return False

    
        
print(is_kangarooword("benten","tenn"))