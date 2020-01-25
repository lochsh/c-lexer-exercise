import tokens


class Lexer:
    """
    C lexer

    Attributes:
        accum (str): string accumulating the text for the current token
        tokens (list): list of tokens lexed so far
    """

    def __init__(self):
        self.accum = ""
        self.tokens = []

    def step(self, state, char):
        """
        Step the lexer state machine, processing the next character

        Args:
            state (callable that takes a string): state function to run
            char (str): character to interpret
        """
        assert len(char) == 1
        return state(char)

    def done_accumulating(self):
        """Clear the accumulator, returning what it contained"""
        token_str = self.accum
        self.accum = ""
        return token_str

    def new_token(self, char):
        """
        Entry state: we are starting to lex a new token

        Args:
            char (str): character to interpret. Its value will decide which
                type of token we attempt to lex.

        Returns:
            next state to run

        Raises:
            RuntimeError if an unexpected character is received
        """
        if char.isspace():
            return self.new_token

        self.accum += char

        if char.isalpha():
            return self.accumulate_keyword_or_id
        elif char.isdigit():
            return self.accumulate_constant
        elif char == "'":
            return self.accumulate_string
        else:
            raise RuntimeError("State transition not implemented")

    def accumulate_keyword_or_id(self, char):
        """
        State for accumulating a keyword or identifier token

        Args:
            char (str): character to interpret. Its value will decide whether
                we continue or finish accumulating our token.

        Returns:
            next state to run
        """
        if char.isalnum():
            self.accum += char
            return self.accumulate_keyword_or_id

        token_str = self.done_accumulating()
        if token_str in tokens.keywords:
            self.tokens.append(tokens.Keyword(token_str))
        else:
            self.tokens.append(tokens.Identifier(token_str))

        return self.new_token(char)

    def accumulate_punctuator(self, char):
        """
        State for accumulating a punctuator token

        Args:
            char (str): character to interpret. Its value will decide whether
                we continue or finish accumulating our token.

        Returns:
            next state to run
        """
        raise RuntimeError("Not implemented")

    def accumulate_string(self, char):
        """
        State for accumulating a string literal token

        Args:
            char (str): character to interpret. Its value will decide whether
                we continue or finish accumulating our token.

        Returns:
            next state to run
        """
        raise RuntimeError("Not implemented")

    def accumulate_constant(self, char):
        """
        State for accumulating a constant token

        Args:
            char (str): character to interpret. Its value will decide whether
                we continue or finish accumulating our token.

        Returns:
            next state to run
        """
        raise RuntimeError("Not implemented")
