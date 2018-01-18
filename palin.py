import pdb
class my_class:

    @staticmethod
    def is_palin(some_string):
            #pdb.set_trace()
            st = some_string.lower()
            st = ''.join(c for c in st if c.isalnum())
            for ct in range(len(st)/2):
                if st[ct] != st[-ct -1]:
                    return False
            return True

    @staticmethod
    def get_unique_words(some_string):
        return(set(some_string.split()))

l_str = 'taco cat'
print('is '+l_str+' palin:',my_class.is_palin(l_str))

l_str2 = '123 123 12  '
print('get unique words:',my_class.get_unique_words(l_str2))
