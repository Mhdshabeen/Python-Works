

def flat_list(*args):

    flat=[]

    for arg in args:

        if isinstance(arg,int):

            flat.append(arg)

        elif isinstance(arg,list):

            flat.extend(flat_list(*arg))

    return flat



print(flat_list(1,2,[3,4],[5,[6,7]]))