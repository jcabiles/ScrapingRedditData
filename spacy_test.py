import spacy
import textacy.extract
import praw

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
text = """
Ranchers might want to consider painting "zebra stripes" on their livestock. According to a new study published in PLoS ONE, the measure reduces the number of biting flies on cows by more than half.

Biting flies are one of the great banes of cows worldwide. The irritating insects cause cows to graze less, eat less, sleep less, and also to bunch together into tightly clumped groups, which stresses the animals and leads to more injuries. The damage done by biting flies equates to roughly $2.2 billion in yearly economic losses for the U.S. cattle industry.

Seeking a potential solution to this situation, a team of Japanese researchers cleverly applied lessons from research on zebras. Animal scientists have long pondered the function of zebras' dsitinct stripes, and a growing consensus now suggests that they deter insects, possibly by confusing bugs' motion detection systems that control approach and landing.

And so, the researchers painted six Japanese Black cows with black-and-white stripes, which took just five minutes per cow. They then observed the cows for three days, taking high-resolution images of them at regular intervals to count the insects on the animals and also recording any fly-repelling behaviors like leg stamping, tail flicking, and skin twitching. The same cows were also observed for three days with painted-on black stripes (to see if it was the paint chemicals, not the coloring, that repelled flies) and and with no stripes at all.

The apparent effects of the stripes were remarkable. The number of biting flies observed on zebra-striped cows was less than half the number seen on unpainted cows and far less than cows painted with black stripes. Moreover, zebra-striping reduced fly-repelling behaviors by about 20%, indicating that the cows were less bothered by the insects.


Number of biting flies on legs and body (a) and the frequency of total fly-repelling behaviors (b) of the experimental cows. Unpainted = CONT / Striped = B&W / Black Stripes = B

The cattle industry commonly sprays pesticides to combat biting flies, but the researchers say that painting stripes with non-toxic materials could be cheaper, healthier for livestock, and better for the environment.

The study should first be replicated with a much larger sample size and different breeds of cows, however.

"More effective techniques to ensure the persistence of black-and-white stripes on livestock during the biting fly season (3–4 months) may be necessary in order to apply this method to animal production sites," the researchers also write.

Should the impressive results of this study be confirmed, this could truly prove to be an inspirational and ingenious translation of a seemingly mundane scientific finding to make the world a better, more humane, and healthier place.

Source: Kojima T, Oishi K, Matsubara Y, Uchiyama Y, Fukushima Y, Aoki N, et al. (2019) Cows painted with zebra-like striping can avoid biting fly attack. PLoS ONE 14(10): e0223447.
"""

# Parse the document with spaCy
doc = nlp(text)

# Define topic
topic = "stripes"

# Extract semi-structured statements
statements = textacy.extract.semistructured_statements(doc, topic)

# Print the results
print(f"Here are the things I know about {topic} based on the text provided")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {fact}")