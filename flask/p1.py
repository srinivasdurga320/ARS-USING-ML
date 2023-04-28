import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
def calculate(user_input):
  if(isinstance(user_input,str)):
    z=user_input
  else:
    z=str(user_input)
  user_input=z
  user_input=user_input.lower()
  s=[]
  if user_input[0]=='\'' or user_input[0] == '\"':
    try:
      result_string = user_input[1:-1]
      if 'x' in result_string:
        result_string=result_string.replace('x','*')
        result = eval(result_string)
        s.append(str(result))
        return s
      else:
        result = eval(result_string)
        s.append(str(result))
        return s
    except:
      return "Invalid input"
  elif 'x' in user_input:
    user_input=user_input.replace('x','*')
    result = eval(user_input)
    s.append(str(result))
    return s
  else:
    try:
      result = eval(user_input)
      s.append(str(result))
      return s
    except:
      words = word_tokenize(user_input)
      pos_tags = nltk.pos_tag(words)
      # total=[word for word, pos in pos_tags if pos.startswith('N') or pos =='JJ'or pos=='JJS' or pos =='VBG' or pos=='VB' or pos=='CD']
      keywords = [word for word, pos in pos_tags if pos.startswith('N') or pos =='JJ'or pos=='JJS' or pos =='VBG' or pos=='VB']
      numbers = [word for word, pos in pos_tags if pos == 'CD']
      numbers=convert_numbers(numbers)
      my_dict = {'mean': find_mean, 'mode': find_mode, 'median': find_median,'hcf':find_gcf,'gcd':find_gcf,'gcf':find_gcf,'lcm':find_lcm}
      # my_dict1 = { 'mode': find_mode1}
      if(len(keywords)==0):
         s.append("Please provide sufficient information")
         return s
      else:
        for keyword in keywords:
          if keyword in my_dict:
            try:
              x=my_dict[keyword](numbers[0])
              s.append(keyword + " of the given numbers is: "+ str(x))
            except IndexError as er:
              y="We are not trained this type of models "+str(user_input)
              s.append(y)
              return s
              # x=my_dict1[keyword](keywords)
              # s.append(keyword + " of the given numbers is: "+ str(x))
          else:
            # y="The model was not trained for this type of problems"
            # s.append(y)
            pass
        return s
    
def convert_numbers(numbers):
  int_list = []
  for str_values in numbers:
    int_values = []
    for value in str_values.split(','):
        int_value = eval(value)
        int_values.append(int_value)
    int_list.append(int_values)
  return int_list
def find_lcm(values):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    result = values[0]
    for value in values[1:]:
        result = result * value // gcd(result, value)
    return result

def find_gcf(numbers):
    gcf = None
    for i in range(min(numbers), 0, -1):
        if all(num % i == 0 for num in numbers):
            gcf = i
            break
    return gcf

from statistics import StatisticsError, mode
def find_mode(numbers):
    try:
        if(len(numbers)!=0):
          mode_value = mode(numbers)
          return int(mode_value)
        else:
          return "we can't perform on text" 
    except StatisticsError:
        return "There is no unique mode for this list."
    
def find_mean(numbers):
    if len(numbers) == 0:
        return None
    else:
        mean_value = sum(numbers) / len(numbers)
        return mean_value
    
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        # If the list has an even number of elements, take the average of the middle two
        mid = length // 2
        median_value = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # If the list has an odd number of elements, take the middle element
        median_value = sorted_numbers[length // 2]
    return median_value
