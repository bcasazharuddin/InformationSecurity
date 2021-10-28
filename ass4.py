# Write a program that can perform a letter frequency attack on an monoalphabetic cipher without human intervention.Your software should produce possible plain text in rough order of likelihood .it would be good if your user interface allow user to specify 'Give me top 10 possible plain  texts '.
import copy
def frequency_attack(S, N):
  
  plaintext = [None] * 10
  
  freq = [0] * 26
  
  freqSorted = [None] * 26

  used = [0] * 26
  
  for i in range(N):
      if S[i] != ' ':
          freq[ord(S[i]) - 65] += 1
  # Copy the frequency array        
  freqSorted=copy.deepcopy(freq)
  # Sort the array in descending order
  freqSorted.sort(reverse = True)
  # T Stores the string formed from concatanating the english letter in the decreasing frequency in the
  # english language    
  T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
 
  for i in range(10):
      ch = -1
      
      for j in range(26):
          if freqSorted[i] == freq[j] and used[j] == 0:
              used[j] = 1
              ch = j
              break
      if ch == -1:
          break
      # Store the numerical equivalent of letter
      # at ith index of array letter_frequency
      x = ord(T[i]) - 65
      # Calculate the probable shift used
      # in monoalphabetic cipher
      x = x - ch
      # Temporary string to generate one
      # plaintext at a time
      curr = ""
      # Generate the probable ith plaintext
      # string using the shift calculated above
      for k in range(N):
          # Insert whitespaces as it is
          if S[k] == ' ':
              curr += " "
              continue
          # Shift the kth letter of the
          # cipher by x
          y = ord(S[k]) - 65
          y += x
          if y < 0:
              y += 26
          if y > 25:
              y -= 26
          # Add the kth calculated/shifted
          # letter to temporary string    
          curr += chr(y + 65)
      plaintext[i] = curr
  return plaintext
def menu():
    encrypted_word = input("\nEnter the encrypted message: ")
    print("\nFirst 10 possible plain texts are : ")
    text_list=frequency_attack(encrypted_word,len(encrypted_word))
    print(*text_list,sep='\n')

menu()
