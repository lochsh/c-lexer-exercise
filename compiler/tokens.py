keywords = [
        # Storage class specifiers
        "auto", "extern", "register", "static",

        # Type qualifiers
        "const", "restrict", "volatile",

        # Control
        "break", "case", "continue", "default", "do", "else", "for",
        "goto", "if", "return", "switch", "while",

        # Type specifiers
        "char", "double", "float", "int", "long",
        "short", "signed", "unsigned", "void",

        # Struct, union, enumeration
        "enum", "struct", "union",

        # Function specifiers
        "inline",

        # others
        "sizeof", "typedef",
]

punctuators = [
        "[", "]", "(", ")", "{", "}",
        ".", "->", "++", "--", "&",
        "*", "+", "-", "~", "!",
        "/", "%", "<<", ">>", "<", ">", "<=", ">=",
        "==", "!=", "^", "|", "&&", "||", "?",
        ":", ";", "...", "=", "*=", "/=", "%=", "+=",
        "-=", "<<=", ">>=", "&=", "^=", "|=", ",", "#", "##",
        # Digraphs,
        "<:", ":>", "<%", "%>", "%:", "%:%:",
        # Trigraphs,
        "??=", "??/", "??'", "??(", "??)", "??!", "??<", "??>", "??-",
]


complete_punctuator_chars = ["[", "]", "(", ")", "{", "}", ";", ","]

possibly_incomplete_punctuator_chars = [
        ".", "|", ":", "!", "-", "+",
        "=", "*", "/", "!", "?", "<",
        ">", "#", "&", "|", "^", "%",
]

punctuator_chars = [
        *complete_punctuator_chars,
        *possibly_incomplete_punctuator_chars
]


class Keyword:

    def __init__(self, keyword_string):
        if keyword_string not in keywords:
            raise RuntimeError(f"{keyword_string} is not a keyword")

        self.value = keyword_string


class Identifier:

    def __init__(self, token_string):
        self.value = token_string


class StringLiteral:

    def __init__(self, literal_value):
        self.value = literal_value


class Constant:

    def __init__(self, constant_value):
        self.value = constant_value


class Punctuator:

    def __init__(self, punctuator_string):
        if punctuator_string not in punctuators:
            raise RuntimeError(f"{punctuator_string} is not a punctuator")
        self.value = punctuator_string
