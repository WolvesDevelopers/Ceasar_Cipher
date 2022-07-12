from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(new_text, new_shift, new_direction):
    end_text = ""
    for letter in new_text:
        
        position = alphabet.index(letter)

        if(new_direction == "encode"):
            new_position = position + new_shift
            if(new_position >= len(alphabet)):
                position = alphabet.index("a")
                new_position = (position - 1) + new_shift
            end_text += alphabet[new_position]
        
        
        elif(new_direction == "decode"):
            new_position = position - new_shift
            if(new_position >= len(alphabet)):
                position = alphabet.index("a")
                new_position = (position - 1) - new_shift
            end_text += alphabet[new_position]
        

    print(f"The {new_direction} text is {end_text}")




def run():
    access = True
    while access:
        try:
            print(logo)
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: type 'exit' to out of app:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            shift = shift % 26
            ceasar(new_text=text, new_shift=shift, new_direction= direction)
            restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
            if (restart == "no"):
                access = False
                print("Goodbye")
                
        except ValueError:
            print("Invalid value")
        
            

        



if __name__== '__main__':
    run()