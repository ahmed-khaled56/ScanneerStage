def is_simple_grammar(grammar):
    """
    Checks if the grammar is simple:
    1. Every rule is CFG.
    2. No ε (epsilon) rules are allowed.
    3. Selection sets for each non-terminal's rules must not overlap.
    """
    selection_sets = {}

    for non_terminal, rules in grammar.items():
        current_selection_set = set()
        
        for rule in rules:
            if rule == 'ε':  # Check for epsilon
                print(f"Rule '{non_terminal} -> ε' violates the no-ε rule.")
                return False

            # Check CFG format: terminals followed by at most one non-terminal
            non_terminal_count = sum(1 for char in rule if char.isupper())
            if non_terminal_count > 1 and not rule[-1].isupper():
                print(f"Rule '{non_terminal} -> {rule}' violates CFG format.")
                return False

            # Check for overlapping selection sets
            first_symbol = rule[0]  # Use the first symbol of the rule as the selection indicator
            if first_symbol in current_selection_set:
                print(f"Selection set overlap detected for '{non_terminal}' on symbol '{first_symbol}'.")
                return False
            current_selection_set.add(first_symbol)

        selection_sets[non_terminal] = current_selection_set

    return True


def recursive_descent_parser(grammar, input_string, start_symbol):
    """
    Recursive Descent Parsing logic to check if the input string matches the grammar.
    """
    stack = [start_symbol]
    pointer = 0
    input_length = len(input_string)

    while stack:
        top = stack.pop()

        if pointer >= input_length:
            return False  # Input string still unmatched but stack is not empty

        current_input = input_string[pointer]

        if top.isupper():  # Non-terminal
            matched = False
            for rule in grammar[top]:
                if rule and rule[0] == current_input:  # Matching rules based on the current input
                    stack.extend(reversed(rule))  # Push the rule to the stack (in reverse)
                    matched = True
                    break
            if not matched:
                return False
        elif top == current_input:  # Terminal match
            pointer += 1
        else:
            return False  # Terminal mismatch

    return pointer == input_length  # Accepted if all input is matched


def main():
    while True:
        print("\n👇 Grammars 👇")
        grammar = {}
        non_terminals = ["S", "B"]  # Fixed two non-terminals as per requirement
        print("Enter grammar rules for the following non-terminals:")
        for nt in non_terminals:
            grammar[nt] = []
            for i in range(1, 3):  # Two rules for each non-terminal
                rule = input(f"Enter rule number {i} for non-terminal '{nt}': ").strip()
                grammar[nt].append(rule)

        # Check if the grammar is simple
        if not is_simple_grammar(grammar):
            print("The Grammar isn't simple ❌.\nTry again.")
            continue

        print("The Grammar is simple ✅")

        while True:  # Loop to check multiple sequences
            input_string = input("Enter the sequence string to be checked: ").strip()
            start_symbol = "S"  # Start symbol is assumed to be 'S'
            accepted = recursive_descent_parser(grammar, input_string, start_symbol)

            # Display results
            print(f"The input String: {list(input_string)}")
            print(f"Your input String is {'Accepted ✅' if accepted else 'Rejected ❌'}.")

            # Ask user whether to input another string or go back
            print("\n========================================")
            print("1-Another String.\n2-Another Grammar.\n3-Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "2":
                break  # Return to grammar input
            elif choice == "3":
                print("Exiting the program. Goodbye!")
                return
            elif choice != "1":
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()