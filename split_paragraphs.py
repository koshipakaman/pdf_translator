from rules import is_noise

def concat_sentences(sentences):

    all_words = []

    for sentence in sentences:

        words = sentence.split()
        for word in words: all_words.append(word)

    return " ".join(all_words)
        
def split_paragraphs(lines):
    
    # lines = text.splitlines()
    paragraphs, paragraph = [], []

    for line in lines:

        if line == '':

            if len(paragraph) == 0:
                continue

            else:
                paragraph = concat_sentences(paragraph)
                paragraphs.append(paragraph)
                paragraph = []

        else:
            paragraph.append(line) 

    return paragraphs


def labeling(lines):

    # lines = text.splitlines()
    out = []
    for line in lines:

        if line == "":
            out.append(line)
            continue

        if is_noise(line):
            out.append("# " + line)

        else:
            out.append(line)

    return out


def save_paragraphs(paragraphs, filepath):

    with open(filepath, "w") as f:

        for paragraph in paragraphs:
            
            f.write("\n\n")
            f.write(paragraph + "\n")


if __name__ == "__main__":

    l = ['In contrast, traditional generative models for graphs (e.g.,Barabási-Albert ',
         'model, Kronecker graphs, exponential random graphs, and stochastic block ',
         ]
    print(concat(l))
