from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And( 
    # TODO
    Or(Not(And(AKnight, AKnave)),AKnight),
    Or(And(AKnight, AKnave),AKnave),

    # XOR knight knave condition
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    #A says
    Biconditional(And(AKnave,BKnave),AKnight),
   
    
    #B Says Nothing = false    
    
    # XOR knight knave condition
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(And(Not(BKnight),BKnave),And(Not(BKnave),BKnight))

    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # A says:
    Biconditional(AKnight, Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    # B says:
    Biconditional(BKnight, Or(And(AKnave,BKnight),And(AKnave,BKnight))),
    

    # XOR knight knave condition
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(And(Not(BKnight),BKnave),And(Not(BKnave),BKnight))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Or(Biconditional(AKnight,AKnight), Biconditional(AKnave,Or(AKnave,AKnight))),
    # B says "A said 'I am a knave'."
    Biconditional(BKnight,Biconditional(AKnave,AKnave)),
    # B says "C is a knave."
    Biconditional(BKnight,CKnave),
    # C says "A is a knight."
    Biconditional(CKnight,AKnight),

     # XOR knight knave condition
    Or(And(Not(AKnight),AKnave),And(Not(AKnave),AKnight)),
    Or(And(Not(BKnight),BKnave),And(Not(BKnave),BKnight)),
    Or(And(Not(CKnight),CKnave),And(Not(CKnave),CKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
