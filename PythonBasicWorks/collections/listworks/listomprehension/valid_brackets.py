# WAP to check the given bracket pairs are valid or not



input=")"

symbol_table={"<":">",
              "[":"]",
              "{":"}",
              "(":")"
              }

symbol_stack=[]

top=-1

is_valid= True

for symbol in input: #

    if symbol in symbol_table: #(
        
        top+=1

        symbol_stack.append(symbol) #(

    else:

        if len(symbol_stack)<1:

            is_valid=False

            break


        current_symbol=symbol_stack[top] # (

        current_symbol_closing=symbol_table.get(current_symbol) # )

        if symbol==current_symbol_closing:

            symbol_stack.pop()

            top-=1

        else:

            is_valid=False

            break

if len(symbol_stack)!=0:

    is_valid=False

print(is_valid)









        

        