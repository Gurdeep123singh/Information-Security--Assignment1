#program that can encrypt and decrypyt using the Affine Cipher 

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
special_char=[' ',',','!','@','#','?','{','}','/',']','[','}','{','(',')','.']

encoded_index_list=[];

#encoded section 
# using (key1*index+key2)%26
def encoded_section(value,key1,key2):
    encoded_value="";
    
    count=0;
    for i in value:
        if i not in special_char:
            encoded_index=round((key1*list1.index(i))+key2)%26; 
            encoded_index_list.insert(count,encoded_index);
            count+=1;
            encoded_value+=list1[encoded_index];
        else:
            encoded_value+=i;    
    return encoded_value
    

#decoded section

## finding k inverse using kx%26==1
def finding_k_inverse(key1):
    flag=True;
    i=1;
    while(flag):
        output=(key1*i)%26;
        if(output==1):
            k_inverse=i;
            flag=False;
        i+=1; 
    return k_inverse     

# decoded section
def decoded_section(encoded_value,encoded_index_list,key1):      
    decoded_value="";
    
    k_inverse=finding_k_inverse(key1);
    count=0;
    
    #decoded index formula (index*k_inverse)%26
    for i in range(len(encoded_value)):
        #encoded_value has only alphabets
        if encoded_value[i] not in special_char:
            ans=encoded_index_list[i-count]-key2;
            
            #finding decoded index
            #if ans is-ve then adding with 26 to make +ve
            if(ans<0):
                decoded_index=26+ans;

                
            else:
                decoded_index=ans%26;
            decoded_index=(decoded_index*k_inverse)%26;    
            decoded_value+=list1[decoded_index];

        # encoded_value has not alphabets    
        else:
            decoded_value+=encoded_value[i]
            count+=1;    
    return decoded_value    

value=input("enter the code: ").lower();
key1=int(input("enter the key1: "));          #key1=7
key2=int(input("enter the key2: "));          #key2=2

# calling encoded and decoded section
encoded_value=encoded_section(value,key1,key2)
decoded_value=decoded_section(encoded_value,encoded_index_list,key1)

print("The encoded value is: "+encoded_value);
print("The decoded value is: "+decoded_value);