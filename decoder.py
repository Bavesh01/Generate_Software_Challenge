'''
Special operations
'''
def repeat(decoded, index):
  decoded[index] += decoded[index-1]

def reverse(decoded, index):
  decoded[index] = decoded[index][::-1]

def encrypt(decoded, index):
  decoded[index] = ''.join([str(int(c)*2)[-1] for c in decoded[index]])

'''
dictionary for special characters and their operations
'''
special = {
  '!' : lambda d, i : repeat(d, i), 
  '^' : lambda d, i : reverse(d, i-1),
  '%' : lambda d, i : encrypt(d, i-1),
}

# Functions for special characters
def add_special(char, function):
  special[char] = function

def rem_special(char):
  del special[char]

'''
decodes the barcode formatted data
'''
def decode(code):

  # Code checks 
  if code == '':
    return ''
  assert code != '#'
  assert code[0] == '#'
  assert code[-1] == '#'

  # Split code into blocks
  blocks = code.split('#')[:-1]
  # Create decoded format
  decoded = ['' for _ in range(len(blocks))]

  '''
  EDGE CASES:
  0. empty string
  1. invalid strings
  2. Spl characters in first block
  ------
  3. Repeated characters
  4. Non hash nesting
  '''  

  # Analyze by data block
  for i in range(len(blocks)):
    data = blocks[i]

    # Analyze by each character
    for j in range(len(data)):
      mychr = data[j]
      
      # Add to the decoded block if numeric
      if mychr.isnumeric():
        decoded[i] += mychr
      
      # Perform special operation otherwise
      elif mychr in special.keys():
        special[mychr](decoded, i)
      
      # Non-numeric non-special character raises exception
      else:
        raise Exception('Unrecognized character')
  return ''.join(decoded)

print(decode('#12#34!#59^#67%#'))
print(decode('#0%#1%#2%#3%#4%#5%#6%#7%#8%#9%#'))
