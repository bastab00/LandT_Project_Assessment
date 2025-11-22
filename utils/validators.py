def input_nonempty(prompt: str) -> str:
    while True:
        v = input(prompt).strip()
        if v:
            return v
        print("Input cannot be empty.")

def input_int(prompt: str, min_val=None, max_val=None):
    v = input(prompt).strip()
    if not v.isdigit():
        return None
    n = int(v)
    if min_val is not None and n < min_val:
        return None
    if max_val is not None and n > max_val:
        return None
    return n

def validate_subject(sub: str) -> bool:
    return sub.replace(" ", "").isalpha()
