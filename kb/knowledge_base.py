from .utils import *
from .logic import *


class KB:
    """A knowledge base to which you can tell and ask sentences.
    To create a KB, first subclass this class and implement
    tell, ask_generator, and retract. Why ask_generator instead of ask?
    The book is a bit vague on what ask means --
    For a Propositional Logic KB, ask(P & Q) returns True or False, but for an
    FOL KB, something like ask(Brother(x, y)) might return many substitutions
    such as {x: Cain, y: Abel}, {x: Abel, y: Cain}, {x: George, y: Jeb}, etc.
    So ask_generator generates these one at a time, and ask either returns the
    first one or returns False."""

    def __init__(self, sentence=None):
        if sentence:
            self.tell(sentence)

    def tell(self, sentence):
        """Add the sentence to the KB."""
        raise NotImplementedError

    def ask(self, query):
        """Return a substitution that makes the query true, or, failing that, return False."""
        return first(self.ask_generator(query), default=False)

    def ask_generator(self, query):
        """Yield all the substitutions that make query true."""
        raise NotImplementedError

    def retract(self, sentence):
        """Remove sentence from the KB."""
        raise NotImplementedError


class PropKB(KB):
    """A KB for propositional logic. Inefficient, with no indexing."""

    def __init__(self, sentence=None):
        super().__init__(sentence)
        self.clauses = []

    def tell(self, sentence):
        """Add the sentence's clauses to the KB."""
        self.clauses.extend(conjuncts(to_cnf(sentence)))

    def ask_generator(self, query):
        """Yield the empty substitution {} if KB entails query; else no results."""
        if tt_entails(Expr("&", *self.clauses), query):
            yield {}

    def ask_if_true(self, query):
        """Return True if the KB entails query, else return False."""
        for _ in self.ask_generator(query):
            return True
        return False

    def retract(self, sentence):
        """Remove the sentence's clauses from the KB."""
        for c in conjuncts(to_cnf(sentence)):
            if c in self.clauses:
                self.clauses.remove(c)


# ______________________________________________________________________________


class WumpusKB(PropKB):
    """
    Create a Knowledge Base that contains the a temporal "Wumpus physics" and temporal rules with time zero.
    """

    def __init__(self):
        super().__init__()
        self.symbol = set()
        for x in range(1, 5):
            for y in range(1, 5):
                self.symbol.add(expr(f"P{x}{y}"))
                self.symbol.add(expr(f"W{x}{y}"))
                self.symbol.add(expr(f"B{x}{y}"))
                self.symbol.add(expr(f"S{x}{y}"))
                self.symbol.add(expr(f"G{x}{y}"))
        print(self.symbol.__len__())
        self.tell(expr("~W11"))
        self.tell(expr("~P11"))
        for x in range(1, 5):
            for y in range(1, 5):
                adj = adjust_coords(x, y)
                b = []
                s = []
                not_b = []
                not_s = []
                for px, py in adj:
                    b.append(f"P{px}{py}")
                    s.append(f"W{px}{py}")
                    not_b.append(f"~P{px}{py}")
                    not_s.append(f"~W{px}{py}")
                self.tell(expr(f"B{x}{y} <=> ({' | '.join(b)})"))
                self.tell(expr(f"S{x}{y} <=> ({' | '.join(s)})"))
                # print(f"B{x}{y} <=> ({' | '.join(b)})")
                # print(f"S{x}{y} <=> ({' | '.join(s)})")
                self.tell(expr(f"~B{x}{y} <=> ({' & '.join(not_b)})"))
                self.tell(expr(f"~S{x}{y} <=> ({' & '.join(not_s)})"))
                # self.tell(expr(f"W{x}{y} ==> (S{x}{y})"))
                # self.tell(expr(f"P{x}{y} ==> (B{x}{y})"))

    def ask_if_true(self, query):
        return pl_resolution(self, query)

    def dpll_satisfiable(self) -> dict | bool:
        return dpll(self.clauses, self.symbol, {})
