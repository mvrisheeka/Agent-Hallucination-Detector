from hallucination_detector import evaluate_hallucination
# #CASE 1
# context = """
# The 2018 FIFA World Cup was held in Russia. In the final match, France national football team defeated Croatia national football team 4-2 to win the tournament.
# """

# question = "Who won the 2018 FIFA World Cup?"

# answer = "The winner of the 2018 FIFA World Cup was Brazil national football team."

#CASE 2
# context = """
# Inception is a 2010 science fiction film directed by Christopher Nolan. The film stars Leonardo DiCaprio as Dom Cobb, a thief who steals information by infiltrating dreams. The movie explores themes of reality, memory, and subconscious manipulation.
# """

# question = "Who directed Inception?"

# answer = "Inception was directed by Steven Spielberg."

# #CASE 3
# context = """
# Apple Inc. was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne. The company is known for products such as the iPhone, iPad, and Mac computers.
# """

# question = "Who were the founders of Apple?"

# answer = "Apple was founded by Bill Gates, Steve Jobs, and Paul Allen."

# #CASE 4
# context = """
# Tesla, Inc. was founded in 2003 by engineers Martin Eberhard and Marc Tarpenning. The company specializes in electric vehicles and renewable energy solutions.
# """

# question = "When was Tesla founded?"

# answer = "Tesla was founded in 2003 and is currently led by Elon Musk, who transformed it into the world's most valuable car company."

# #CASE 5
# context = """
# Nineteen Eighty-Four is a novel by George Orwell that depicts a totalitarian society under constant surveillance. The story explores themes of government control, truth manipulation, and loss of individual freedom.
# """

# question = "What is the central theme of 1984?"

# answer = "The novel primarily promotes the idea that strong surveillance systems create stability and social harmony."

# context = """
# In Brown v. Board of Education, the Supreme Court of the United States ruled in 1954 that racial segregation in public schools was unconstitutional. The ruling overturned the “separate but equal” doctrine established in Plessy v. Ferguson.
# """

# question = "Which case overturned the “separate but equal” doctrine?"

# answer = "Plessy v. Ferguson overturned the “separate but equal” doctrine."

#CASE 6
context = """
Type 1 diabetes is an autoimmune condition in which the pancreas produces little or no insulin. It requires lifelong insulin therapy. Type 2 diabetes, by contrast, is often managed initially with lifestyle changes and oral medications.
"""
question = "Which type of diabetes requires lifelong insulin therapy?"

answer = "Type 2 diabetes requires lifelong insulin therapy."



report = evaluate_hallucination(context, question, answer)


import json
print(json.dumps(report, indent=4))