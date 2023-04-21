import random


def get_random_word(words):
    return random.choice(words)


names = ['Boyan', 'Sava', 'Kalina','Vader', 'Batman']
places = ['Mustafar', 'Vidin', 'Other side', 'Kathmandu', 'Bangalore']
verbs = ['shoots', 'drinks', 'procrastinates', 'contemplates', 'laughs']
nouns = ['Jedi', 'lift off', 'lake', 'cake', 'movie', '']
adverbs = ['eagerly', 'calmly', 'furiously', 'happily', 'badly']
details = ['by the ocean', 'in the vacuum of space', 'from the terrace', 'near the park', 'through a straw']
print('Greetings! This is your first randomly generated message. :) ')
print()
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f'{random_name} from {random_place} {random_verb} {random_noun} {random_adverb} {random_detail}')
    input('Click [Enter] to continue.')


