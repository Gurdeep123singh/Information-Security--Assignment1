#program that can encrypt and Decrypt using a 2 X 2 Hill Cipher.

import numpy as np;

list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," "];

# taking input form user
code=input("enter the code: ").lower();

# making index list of characters inputted by user    
code_list=[list1.index(i) for i in code];

# if code length is odd then add space index
if (len(code)%2!=0):
    code_list.append(list1.index(" "))

# making key matrix of 2x2 using user input
def making_key_matrix():
    print("enter the key for 2X2 matrix: ");
    key_matrix=[];
    print("Enter values: ")
    for i in range(2):
        a=[]
        for j in range(2):
            a.append(int(input()));
        key_matrix.append(a); 
    return key_matrix

key_matrix=making_key_matrix()

encoded_code="";

#multiplication matrix code using index with key_matrix
def multiplication_matrix_with_key(code_list,code,key_matrix):

    while(len(code_list)!=0):
        matrix=[];

        for i in range(2):
            a=[];
            for j in range(1):
                a.append(code_list[j]);
                
                del code_list[j];
            matrix.append(a);


        
        for i in range(2):
            
            for j in range(1):
                code+=list1[(key_matrix[i][j]*matrix[j][j]+key_matrix[i][j+1]*matrix[j+1][j])%27];
    return code;            

# encoded code
encoded_code=multiplication_matrix_with_key(code_list,encoded_code,key_matrix)
print("the encoded code: "+encoded_code);            

#decoded section


#inverse block
# finding determinant inverse using kx%26==1
def finding_det_inverse(determinant_key_matrix):

    flag=True;
    i=1;
    while(flag):
        output=(determinant_key_matrix*i)%27;
        if(output==1):
            det_inverse=i;
            flag=False;
        i+=1;
    return det_inverse   

#multiplying determinant inverse with adjoint key_matrix
def making_k_inverse_matrix(key_matrix,determinant_key_matrix):       

    det_inverse=finding_det_inverse(determinant_key_matrix) 
    k_inverse=[];
    for i in range(2):
        a=[]
        for j in range(2):
            key_matrix[i][j]=key_matrix[i][j]*det_inverse;
            a.append(key_matrix[i][j]%27);
        k_inverse.append(a);    
    return k_inverse

# finding decoded section and calling inverse block
def decoded_section(key_matrix,encoded_code):
    
    determinant_key_matrix=round(np.linalg.det(key_matrix));

    for i in range(2):
        for j in range(2):
            if(i!=j):
                key_matrix[i][j]=key_matrix[i][j]*-1;

    for i in range(2):
        for j in range(2):
            if(key_matrix[i][j]<0):
                key_matrix[i][j]=key_matrix[i][j]+27;  
                    

    for i in range(2):
        for j in range(2):
            if(i==j==0):
                a=key_matrix[i][j];
            if(i==j==1):
                key_matrix[0][0]=key_matrix[i][j];
                key_matrix[i][j]=a;

        




    code_list=[list1.index(i) for i in encoded_code];



    decoded_code=""

    k_inverse=making_k_inverse_matrix(key_matrix,determinant_key_matrix)

    decoded_code=multiplication_matrix_with_key(code_list,decoded_code,k_inverse)


    print("the decoded code: "+decoded_code);            


#calling decoded section
decoded_section(key_matrix,encoded_code) 