import sys
import nltk.data

try:
    sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
    print("NLTK data found")
except Exception as e:
    print("NLTK data NOT found:")
    print(e)
    sys.exit(1)

# nltk >=3.9 resolves the punkt pickle to punkt_tab, and pos_tag to the
# *_eng taggers, so check those explicitly to catch a stale data snapshot.
try:
    nltk.data.find("tokenizers/punkt_tab/english/")
    nltk.data.find("taggers/averaged_perceptron_tagger_eng/")
    print("NLTK pickle-free data found")
    sys.exit(0)
except Exception as e:
    print("NLTK pickle-free data NOT found:")
    print(e)
    sys.exit(1)
