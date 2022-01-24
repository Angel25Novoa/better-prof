#pip install better-profanity
from better_profanity import profanity

custom_words = ["Hola", "piece"]

text = "you piece of sHit"

censored_text = profanity.censor(text, "%")

print(censored_text)

result = profanity.contains_profanity(text)

print(result)

profanity.load_censor_words(custom_words)

censored_text1 = profanity.censor(text)

print(censored_text1)

