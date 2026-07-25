from lackey import Pattern


def image(path, similarity=0.8):
    return Pattern(path).similar(similarity)