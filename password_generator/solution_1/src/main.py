from abc import ABC, abstractmethod
import random
import string 

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass    


class PinGenerator(PasswordGenerator):
    def __init__(self, length=8):
        self.length = length
        
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])
    

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length=8, include_numbers=False, include_symbols=False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation
       
    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])
 
    
class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self,
                 number_of_words=4,
                 separator='-',
                 capitalization=False,
                 vocabulary=None
    ):
        if vocabulary is None:
            vocabulary = ['library', 'bench', 'desk', 'board']
                
        self.vocabulary = vocabulary
        self.number_of_words = number_of_words
        self.capitalization = capitalization
        self.separator = separator
            
    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        return self.separator.join(password_words)
    
if __name__ == "__main__":
    r_p_obj = RandomPasswordGenerator()
    m_p_obj = MemorablePasswordGenerator()
    p_p_obj = PinGenerator()
    print(r_p_obj.generate())
    print(m_p_obj.generate())
    print(p_p_obj.generate())
    