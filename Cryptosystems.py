import time
class Affine:
	def __init__(self):
		pass

	def char_num(self,message,a,b):
		message=message.upper()
		temp_alpha_num=[]
		encrypted_message=""
		for i in message:
			if i.isalpha() == False:
	                    #if the character is not an alphabet
				temp_alpha_num.append(i)
			else:
	                    #if the character is an alphabet use the affine encrption function
	                    #f(X)=(aX+b)mod26 
				temp_alpha_num.append(((a*(ord(i)-65)+b)%26))

		for i in temp_alpha_num:
			if  type(i)==str:
				encrypted_message+=i
			else:
				encrypted_message+=chr(i+65)

		return encrypted_message

	def encrypt(self,message,a,b):

		if type(message) == str:
			return self.char_num(message,a,b)
		else:	
			return -1

	def decrypt(self,message,a,b):
        
		if type(message)== str:
			return self.char_numDcrypt(message,a,b)
		else:
			return -1

	def char_numDcrypt(self,message,a,b):

		message=message.upper()
		temp_alpha_num=[]
		decrypted_message=""
		inverseModuloList={1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 15:7, 17:23, 19:11, 21:5, 23:17, 25:25}
		for i in message:
			if i.isalpha() == False:
	                    #if the character is not an alphabet
				temp_alpha_num.append(i)
			else:
	                    #if the character is an alphabet, decrypt using the inverse
	                    #modulo to get a bijective mapping of all the characters
				temp_alpha_num.append((inverseModuloList[a]*((ord(i)-65)-b))%26)

		#finally decrypt with original mapping
		for i in temp_alpha_num:
			if  type(i)==str:
				decrypted_message+=i
			else:
				decrypted_message+=chr(i+65)

		return decrypted_message



class Transposition:

    def __init__(self):
        pass

    def encrypt(self,msg,key):
        if type(key)==str:            #To handle keys of type string
            key = self.toNumber(key)

        msg = msg.upper()             
        word = []
        i = 1
        tmp = []
        encryptedMessage = ""

        for char in msg:            #This loop creates a block of letter with each block having length same as length of the key
            if char==" ":
                continue
            tmp.append(char)
            if i==len(key):
                word.append(tmp)
                tmp = []
                i = 0

            if char!=" ":   
                i+=1
        word.append(tmp)

        if len(word[-1])==0:   #Here we are handling empty strings if occurred
            word.pop()

        if len(word[-1])<len(key):    #Here we are adding *'s for last blocks with incomplete length
            for k in range(len(key)-len(word[-1])):
                word[-1].append("*")

        for item in word:           #Here is where the real encryption occurs with changing places of letter in each block with same pattern according to the key we were provided with
            tmp = []+item
            for index1 in range(len(item)):
                item[int(key[index1])-1] = tmp[index1]

        for item in word:
            for char in item:
                encryptedMessage += char
        return encryptedMessage     #The encrypted message is in a string of numbers format as was illustrated in our text book


    def decrypt(self,msg,key):
        if type(key)==str:            #To handle keys of type string
            key = self.toNumber(key)
 
        msg = msg.upper()               #Same processes happen here as the encryption 
        word = []
        i = 1
        tmp = []
        decryptedMessage = ""
        for char in msg:
            if char==" ":
                continue
            tmp.append(char)
            if i==len(key):
                word.append(tmp)
                tmp = []
                i = 0
            i+=1
        word.append(tmp)

        if len(word[-1])==0:
            word.pop()
        if len(word[-1])<len(key):
            for k in range(len(key)-len(word[-1])):
                word[-1].append("*")

        for item in word:                          #Here is the real difference with the encryption where the opposite process of encryption occurs
            tmp = []+item
            for index1 in range(len(item)):
                item[index1] = tmp[int(key[index1])-1]   #Here particularly

        for item in word:
            for char in item:
                if char!="*":
                    decryptedMessage += char
        return decryptedMessage



    def toNumber(self,word):    # This function converts strings to list of number based the order of the letters in the word
        count = 0
        key = []
        for i in range(len(word)):
            for j in range(len(word)):
                if word[i]>=word[j]:
                    count += 1
            key.append(count)
            count = 0

        return key
            


class RSA:
    def __init__(self):
        pass 


    def toSeqNums(self,message):  #This function converts the message to a seqeunce of numbers or represents the message in number
        seqNums = ""
        for char in message:
            if char==" ":
                continue
            tmp = ord(char)
            if tmp<10:
                seqNums = seqNums+"0"+str(tmp)
            else:
                seqNums += str(tmp)
        return seqNums




    def encrypt(self,message,n,e):
        message = message.upper()
        block = self.blockOf(n)
        seqNums = self.toSeqNums(message)
        blocked_message = []
        encryptedMessage = ""
        index2 = 0
        if block==0:                    #Here the message is blocked in to pieces
            tmp = seqNums[index2:index2+block]
            index2+=block
            blocked_message.append(tmp)

        else: 
            for i in range(len(seqNums)//block) :
                tmp = seqNums[index2:index2+block]
                index2+=block
                blocked_message.append(tmp)

        #Now encryption starts
        for m in blocked_message:
            m = int(m)
            tmp = (m**e)%n
            encryptedMessage += str(tmp) + " "

        return encryptedMessage

    def decrypt(self,message,n,d):
        blocked_message = message.split(" ")
        decryptedMessage = ""
        for em in blocked_message:
            if em=="":
                continue
            em = int(em)
            tmp = (em**d)%n
            char = chr(tmp)
            decryptedMessage += char
        return decryptedMessage

    def blockOf(self,n):         #This function determines the length of the block based on the number 2N where 2N is the largest digit in which 2525...25 does not exceed n
                                 # which is the taken from our text book
        num = "25"
        while True:
            if n<25:
                return 2

            if n>=int(num) and n<=(int(num+"25")):
                return len(num)
            num += "25"



def main():             #The main dunction is self explanatory
    while True:
        time.sleep(1)

        inp1 = input("""
************************************************************************
Use the following instructions:
Enter: 
    1 to use affine encryption
    2 to use transposition encryption
    3 to use RSA encryption
    0 to exit
************************************************************************
\n >>""")

        if inp1=="0":
            break

        elif inp1=="1":
            affineTester = Affine()
            inp2 = input("Do you want to encrypt a message or decrypt? 1 to encrypt 2 to decrypt: \n>> ")
            if inp2=="1":
                message = input("\nEnter your plaintext message:\n >>  ")
                print(""" f(X)=(aX+b)mod26 
	For affine encryption function to be a bijection,
	  gcd(a,26)=1, and 'a' is a positive integer less than 26,
	    so the possible values for 'a' are odd numbers below 26 except 13""")
                a = int(input("\nEnter 'a' for the formula:\n>>  "))
                b = int(input("\nEnter 'b' for the formula:\n>>  "))
                encMsg = affineTester.encrypt(message,a,b)
                time.sleep(1)
                print("\nThe encrypted message using affine encryption is: ", encMsg)
                time.sleep(2)

            elif inp2=="2":
                message = input("\nEnter your encrypted message: \n>> ")
                print(""" f(X)=(aX+b)mod26 
	  For affine encryption function to be a bijection,
	  gcd(a,26)=1, and 'a' is a positive integer less than 26,
	    so the possible values for 'a' are odd numbers below 26 except 13""")
                a = int(input("\nEnter 'a' for the formula:\n>>  "))
                b= int(input("\nEnter 'b' for the formula:\n>>  "))

                encMsg = affineTester.decrypt(message,a,b)
                time.sleep(1)
                print("\nThe decrypted message using affine encryption is: ", encMsg)
                time.sleep(2)


        elif inp1=="2":
            transTester = Transposition()
            inp2 = input("\nDo you want to encrypt a message or decrypt? 1 to encrypt 2 to decrypt: \n>>")
            if inp2=="1":
                message = input("\nEnter your plaintext message: \n>>")
                key = input("\nEnter the key as a word or as a list of numbers separated by a whitespaces:\n>>  ")
                try:
                    if type(eval(key[0]))==int:
                        key = key.split(" ")
                except:
                    key = key

                encMsg = transTester.encrypt(message,key)
                time.sleep(1)
                print("\nThe encrypted message using transposition encryption is: ", encMsg)
                time.sleep(2)

            elif inp2=="2":
                message = input("\nEnter your encrypted message: \n>>")
                key = input("\nEnter the key as a word or as a list of numbers separated by whitespaces:\n>>  ")
                try:
                    if type(eval(key[0]))==int:
                        key = key.split(" ")
                except:
                    key = key

                encMsg = transTester.decrypt(message,key)
                time.sleep(1)
                print("\nThe decrypted message using transposition encryption is: ", encMsg)
                time.sleep(2)

        elif inp1=="3":
            rsaTester = RSA()
            inp2 = input("\nDo you want to encrypt a message or decrypt? 1 to encrypt 2 to decrypt: \n>> ")
            if inp2=="1":
                message = input("Enter your plaintext message: ")
                inp = input("\nEnter the public keys n and e separated by a white space (For example public key of p(n,e) = p(133,29) and its private key p(n,d)=p(133,41)): \n>> ")
                inp = inp.split(" ")
                n = int(inp[0])
                e = int(inp[1])

                encMsg = rsaTester.encrypt(message,n,e)
                time.sleep(1)
                print("\nThe encrypted message using RSA encryption is: ", encMsg)
                time.sleep(2)

            elif inp2=="2":
                message = input("\nEnter your encrypted message: ")
                inp = input("\nEnter the private keys n and d separated by a white space (For example public key of p(n,e) = p(133,29) and its private key p(n,d)=p(133,41)): \n>> ")
                inp = inp.split(" ")
                n = int(inp[0])
                d = int(inp[1])
                encMsg = rsaTester.decrypt(message,n,d)
                time.sleep(1)
                print("\nThe decrypted message using RSA encryption is: ", encMsg)
                time.sleep(2)

main()
