#program that can perform a letter frequency attack on an additive cipher without human intervention. Your software should produce possible plain text in rough order of likelihood. It would be good if your user interface allows user to specify " Give me top 10 possible plain texts"

#freq list with len 26 containing 0 
freq_list=[0]*26;

#this list has to made sorted with len 26 containing 0 
freq_list_sorted=[0]*26;

#used alphabet for making key list with len 26 containing 0 
used_alphabet=[None]*26


list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

special_char=[' ',',','!','@','#','?','{','}','/',']','[','}','{','(',')','.']

# most freq letter in world
most_freq_used='E'

#freq calculator using ascii code as a index in freq_list
def freq_calculator(code):
    for ch in code:
        if ch not in special_char:
            freq_list[ord(ch)-65]+=1;
            freq_list_sorted[ord(ch)-65]+=1;

freq_list_sorted.sort(reverse=True);

# converting 1 decoded code into 10 plain text using sorted_freq_list and calculate key as 10 times
def conversion_to_plain_text(code):
    for j in range(10):
        plain_text=""
        for i in range(len(freq_list_sorted)):
            # checking sorted freq list and freq list values are to be same with same asciicode-65 and alphabet not to be used more than 1 time
            if freq_list_sorted[j]==freq_list[i] and used_alphabet[i]!=1:
                key=i-(ord(most_freq_used)-65)
                used_alphabet[i]=1;
        # now formatting decoded string into plain text
        for ch in code:
            if ch not in special_char:
              plain_text+=list1[(ord(ch)-key)%26];
            else:
                plain_text+=ch;    
        print(plain_text)                 

#given code
code="cahdajlkjlakfjflsdsjf nsmnnf,afnamfa fkdjfdklsfjdskf ekjoeroerepo mcz,,mxnxzmcnxcjnadoidjwoa n,amnas,dnasmdnwiejwioejekfdjkfdjfdff anankajdadkjawpw ajlkja kdajda skasjdaksdeowieqepq mcnxmbvbkfa fnmfndoafkpwuoru"
# converting code to upper case and then calling
freq_calculator(code.upper());
conversion_to_plain_text(code.upper())

    



                

