import re

if __name__ == '__main__':
    text = 'This is first occurrence of phone. Now phone appears a second time'
    print(re.search('phone',text)) # match object returned. Only first match

    match = re.search('phone',text)
    print(f'The index of first match is {match.span()}')
    print(f'The start index of first match is {match.start()}')
    print(f'The end index of first match is {match.end()}')
    print(f'The found match is {match.group()}')

    all_matches = re.findall('phone',text) # List of all matches
    print(f'List of all matches is {all_matches}')

    # To iterate through all matches
    print(f'Finding for "phone" in "{text}"')
    for match in re.finditer('phone',text):
        print(f'Match found at {match.span()}')

    # Identify for patterns
    # Character	    Description	        Example Pattern Code	Example Match
    # \d	        A digit	            file_\d\d	            file_25
    # \w	        Alphanumeric	    \w-\w\w\w	            A-b_1
    # \s	        White space	        a\sb\sc	                a b c
    # \D	        A non digit	        \D\D\D	                ABC
    # \W	        Non-alphanumeric	\W\W\W\W\W	            *-+=)
    # \S	        Non-whitespace	    \S\S\S\S	            Yoyo

    #   Quantifiers
    #     Character	Description	                Example Pattern Code	Example Match
    #       +	    Occurs one or more times	Version \w-\w+	        Version A-b1_1
    #       {3}	    Occurs exactly 3 times	    \D{3}	                abc
    #       {2,4}	Occurs 2 to 4 times	        \d{2,4}	                123
    #       {3,}	Occurs 3 or more	        \w{3,}	                anycharacters
    #       \*	    Occurs zero or more times	A\*B\*C*	            AAACC
    #       ?	    Once or none	            plurals?	            plural

    new_text = 'My phone number is 954-333-2234'
    phone_match = re.search(r'\d{3}-\d{3}-\d{4}',new_text)
    print(f'Match found in {phone_match.group()}')

    # We can use groups for any general task that involves grouping together
    # regular expressions (so that we can later break them down).

    phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    phone_match_result = re.search(phone_pattern,new_text)

    print(f'Phone match result group is {phone_match_result.group()}')

    #Note that group indexing starts at 1 group(0) returns everything same like group()
    for i in range(0,len(phone_match_result.groups())+1):
        print(f'Phone match result group {i} is {phone_match_result.group(i)}')

    # Additional Regex Syntax

    # | to combine using OR
    cd_match = re.findall(r'cat|dog','This sentence has a cat and dog')
    print(f'The search found result {len(cd_match) > 0}')
    print(f'Match found for word {cd_match}')

    # . as wild card
    print('Find using wild card .')
    print(re.findall(r'.inu','Names are Vinu,Manu,Jinu,Minu'))
    print(re.findall(r'..art','Let see what all gets picked from art cart start and Stewart'))

    # Starts with using ^
    print('Starts with using ^')
    print(re.findall(r'^\d','2 is a number'))
    # Ends with using $
    print('Ends with using $')
    print(re.findall(r'\d$','The number is 3'))
    print('Exclusion')
    print(re.findall(r'[^\d]','The number is 3'))
    print(re.findall(r'[^\d]+','The number is 3 and another number is 6'))
    print(" ".join(re.findall(r'[^.!?]+','This is a sentence! But there are punctuations.Can we remove it?')))

