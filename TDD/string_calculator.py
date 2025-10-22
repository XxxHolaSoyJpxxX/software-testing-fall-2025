# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring, missing-function-docstring, too-many-branches, unused-variable

import re


def add(numbers):
    if not numbers:
        return 0

    separators = [",", "\n"]

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        if len(parts) < 2:
            raise ValueError("Invalid input format for custom delimiter")
        delimiter_part = parts[0][2:]
        numbers = parts[1]
        separators = [re.escape(delimiter_part)]
    invalid_pattern = "|".join(
        [re.escape(s1) + re.escape(s2) for s1 in separators for s2 in separators]
    )
    if re.search(invalid_pattern, numbers):
        invalid_sequence = re.search(invalid_pattern, numbers).group()
        has_neg = bool(re.search(r"-\d+", numbers))
        ends_sep = any(numbers.endswith(sep) for sep in separators)
        if not has_neg and not ends_sep:
            return 0

    total = 0
    negatives = []
    errors = []

    if any(numbers.endswith(sep) for sep in separators):
        errors.append("Invalid input: ends with a separator")

    pattern = "|".join(separators)
    numbers_list = re.split(pattern, numbers)

    for num in numbers_list:
        num = num.strip()
        if not num:
            continue
        try:
            n = int(num)
            if n > 1000:
                continue
            if n < 0:
                negatives.append(str(n))
            else:
                total += n
        except ValueError:
            continue

    if negatives:
        errors.insert(0, "Negative number(s) are not allowed: " + " ".join(negatives))

    if errors:
        raise ValueError("\n".join(errors))

    return total
