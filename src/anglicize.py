__version__ = "0.0.0"


_mapping = None


BOTH = {
    "A": "ÂĂǍÄÀÁĀẴẪÃÅȦȀĄÆƏ",
    "C": "ÇĆĈĊČÇȻĆÇ",
    "D": "ĎḒĐÐ",
    "E": "ÈÉÊËĘËĒĖ",
    "G": "ĞĢ",
    "I": "ÎÏĪÍĲĮ",
    "K": "Ķ",
    "L": "ŁĻⱢ",
    "N": "ŃÑŅŇ",
    "O": "ÖŐÔÓÒṌṎŒØÕ",
    "S": "ȘŞŠ",
    "T": "ȚŢ",
    "P": "Þ",
    "U": "ÜŰÛÙÚŪŲ",
    "Y": "ŸÝ",
    "Z": "ŹŻŽ",
}

LOWER = {
    "s": "ß",
    "i": "ᶧıi",
}

UPPER = {"I": "ᵻIİ"}


def build_mapping(both, lower=None, upper=None):
    mapping = {}
    for latin, to_replace in both.items():
        lat_lowered = latin.lower()
        for char in to_replace:
            mapping[char] = latin
            mapping[char.lower()] = lat_lowered
    if lower:
        for latin, to_replace in lower.items():
            for char in to_replace:
                mapping[char] = latin
    if upper:
        for latin, to_replace in upper.items():
            for char in to_replace:
                mapping[char] = latin
    return mapping


def get_mapping():
    global _mapping
    if _mapping is None:
        _mapping = str.maketrans(build_mapping(BOTH, LOWER, UPPER))
    return _mapping


def anglicize(text):
    mapping = get_mapping()
    return text.translate(mapping)
