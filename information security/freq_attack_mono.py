# program that can perform a letter frequency attack on any monoalphabetic substitution cipher without human intervention. Your software should produce possible plain text in rough order of likelihood. It would be good if your user interface allows user to specify " Give me top 10 possible plain texts"

special_char=[' ',',','!','@','#','?','{','}','/',']','[','}','{','(',')','.']

def making_plain_text(user_input, size):
	
	freq_list= [0] * 26
	freq_sorted_list = [0] * 26
	used_alphabets = [0] * 26
	
	# making freq list 
	for i in range(size):
		# only alphabets allowed and calculating index using ascii-65
		if user_input[i] != ' ':
			freq_list[ord(user_input[i]) - 65] += 1;
			freq_sorted_list[ord(user_input[i]) - 65] += 1;
            	
	code = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
	
	# sorting the freq list in descending order
	freq_sorted_list.sort(reverse = True)
	
	# converting 1 decoded code into 10 plain text using sorted_freq_list and calculate key as 10 times
	for i in range(10):
		plaintext=""
		ch = -1
		for j in range(len(freq_list)):
			# checking sorted freq list and freq list values are to be same with same asciicode-65 and alphabet not to be used more than 1 time
			if freq_sorted_list[i] == freq_list[j] and used_alphabets[j] !=1:
				used_alphabets[j] = 1
				ch = j
				break
			
		if ch == -1:
			break

		key = ord(code[i]) - 65
		key = key - ch
		
		for k in range(size):
             
            # Insert whitespaces as it is
			if user_input[k] in special_char:
				plaintext += user_input[k]
				continue
			
            
			y = ord(user_input[k]) - 65
			y += key

			# if y is -ve  then adding 26
			if y < 0:
				y += 26
			#else subtracting 26	
			if y > 25:
				y -= 26

			#converting into character	   
			plaintext += chr(y + 65)
             
        
		print(plaintext)
	

user_input = "B TJNQMF NFTTBHF"
size = len(user_input)

# Function Call
making_plain_text(user_input, size)


