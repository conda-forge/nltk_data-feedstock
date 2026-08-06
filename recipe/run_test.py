import sys
import nltk.data

# The recipe supports nltk >=3.4.4, which spans a resource rename: older nltk
# reads the punkt pickle and the unsuffixed tagger, while nltk >=3.9 resolves
# those to punkt_tab and the *_eng taggers. Assert both generations so a stale
# snapshot missing either one fails the build.
required = [
    "tokenizers/punkt/english.pickle",
    "tokenizers/punkt_tab/english/",
    "taggers/averaged_perceptron_tagger_eng/",
]

for resource in required:
    try:
        nltk.data.find(resource)
    except LookupError as e:
        print(f"NLTK data NOT found: {resource}")
        print(e)
        sys.exit(1)

print("NLTK data found")
