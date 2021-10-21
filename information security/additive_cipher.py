#program that can encrypt  and decrypt using the Additive Cipher

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

special_char=[' ',',','!','@','#','?','{','}','/',']','[','}','{','(',')','.']
## encoded section 

# using (index+key)%26
def encoder_section(value):
    encoded_value=""; 
    for i in value:
        # only alphabets
        if i not in special_char:                      # checking if no space ,comma and other punctuation is not there
            encoded_index=(list1.index(i)+key)%26
            encoded_value+=list1[encoded_index];
        # not alphabets    
        else:
            encoded_value+=i
    return encoded_value        

# decoded section
# using (index-key)%26
def decoded_section(encoded_value):
    decoded_value="";
    for i in encoded_value:
        if i not in special_char:
            decoded_index=(list1.index(i)-key)%26;
            decoded_value+=list1[decoded_index];
        else:
            decoded_value+=i; 
    return decoded_value        

value=input("enter the code: ").lower();
key=int(input("enter the key value: "));

#calling encoded function
encoded_value=encoder_section(value)
print("the encoded code is : "+ encoded_value ); 

#calling decoded function   
decoded_value=decoded_section(encoded_value)
print("the decoded code is : "+ decoded_value );    