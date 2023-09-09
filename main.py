import random

mean = {
    'a1':
    "to hit a door with your hand so that someone inside knows you are there",
    'a2':
    "a statement that you are willing to do something for someone or give someone something",
    'a3':
    'in the process of something such as a picture',
    'a4':
    'extremely valuable',
    'a5':
    'a copy of something such as a picture',
    'a6':
    'a tool for cutting wood or other materials, typically with a long thin steel blade',
    'a7':
    'very surprised and upset',
    'a8':
    'to make good or unfair use of',
    'a9':
    'worth a lot of money',
    'a10':
    'having a specific value',
    'a11':
    'up until the present or a specified time; by now or then',
    'a12':
    'an old object such as a piece of furniture or jewelry',
    'a13':
    'to fasten one thing to another',
    'a14':
    'can to have the ability to',
    'a15':
    "to be famous or known about by a lot of people because of something",
    'a16':
    'used when one feels very strongly compelled to do something',
    'a17':
    'to ask people to pay a particular amount of money for something',
    'a18':
    'to separate something by cutting it away from the main part',
    'a19':
    'someone who buys and sells a particular product',
    'a20':
    'used to emphasize what you are saying',
    'a21':
    'things such as chairs, beds, tables, and cupboards',
    'a22':
    'to succeed in doing or getting something you want',
    'a23':
    'listening or looking carefully',
    'a24':
    'to take air into your body and let it out',
    'a25':
    'a group of people with a particular skill who work together',
    'a26':
    'determined by conditions or circumstances that follow',
    'a27':
    'to pay someone to work for you',
    'a28':
    'not able to be seen',
    'a29':
    "to pay attention to someone or something, so that you know where they are or what is happening to them",
    'a30':
    'for or by oneself',
    'a31':
    'a person or thing that paces',
    'a32':
    'special, or more than usual',
    'a33':
    'the area beside a race track',
    'a34':
    "to put someone's or something's name on an official list",
    'a35':
    "some but not many",
    'a36':
    "to help someone, often when they are having problems",
    'a37':
    "the aim or result that you try to achieve",
    'a38':
    "for the reason that you have mentioned",
    'a39':
    "a group of people who have their own language and ways of living",
    'a40':
    'a metal cup or other object that someone gets for winning a game or race',
    'a41':
    'to use something a lot so that it no longer works, or can no longer be used'
}

word = {
    'a1_a': 'knock',
    'a2_a': 'offer',
    'a3_a': "on one's way",
    'a4_a': 'priceless',
    'a5_a': 'reproduction',
    'a6_a': 'saw',
    'a7_a': 'shocked',
    'a8_a': 'take advantage of',
    'a9_a': 'valuable',
    'a10_a': 'worth',
    'a11_a': 'yet',
    'a12_a': 'antique',
    'a13_a': 'attach',
    'a14_a': 'be able to',
    'a15_a': 'be known for',
    'a16_a': "can't help -ing",
    'a17_a': 'charge',
    'a18_a': 'cut off',
    'a19_a': 'dealer',
    'a20_a': 'exactly',
    'a21_a': 'furniture',
    'a22_a': 'achieve',
    'a23_a': 'attention',
    'a24_a': 'breath',
    'a25_a': 'crew',
    'a26_a': 'depending on',
    'a27_a': 'hire',
    'a28_a': 'invisible',
    'a29_a': 'keep track of',
    'a30_a': "on one's own",
    'a31_a': 'pacer',
    'a32_a': 'particular',
    'a33_a': 'pit',
    'a34_a': 'register',
    'a35_a': 'several',
    'a36_a': 'support',
    'a37_a': 'target',
    'a38_a': 'therefore',
    'a39_a': 'tribe',
    'a40_a': 'trophy',
    'a41_a': 'wear out'
}

keys = list(mean.keys())

# 키 리스트를 무작위로 섞기
random.shuffle(keys)

# 새로운 딕셔너리 생성
shuffled_mean = {key: mean[key] for key in keys}
count = 0
num = 1
# 섞인 딕셔너리 출력
# print(shuffled_mean)
for key, value in shuffled_mean.items():
  mean_input = input(str(num) + "." + value + "\n")
  word_key = key + "_a"
  num = num + 1
  if mean_input == word.get(word_key):
    print(word.get(word_key))
    print("-----------------------------------")
    count = count + 1
  else:
    print("wrong")
    print(word.get(word_key))
    print("---------------------------------------")

print("finished")
print(count)
