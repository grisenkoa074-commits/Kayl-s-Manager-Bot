import re

UNITS = {
    "с": 1, "сек": 1, "s": 1,
    "м": 60, "мин": 60, "m": 60,
    "ч": 3600, "час": 3600, "часа": 3600,
    "часов": 3600, "h": 3600,
    "д": 86400, "день": 86400, "дня": 86400,
    "дней": 86400, "d": 86400,
    "н": 604800, "нед": 604800, "w": 604800,
}


def parse_time(value: str) -> int | None:
    """Преобразует 2ч 30м в секунды."""

    value = value.lower().strip()

    matches = list(
        re.finditer(r"(\d+)\s*([а-яa-z]+)", value)
    )

    if not matches:
        return None

    if re.sub(r"(\d+)\s*([а-яa-z]+)", "", value).strip():
        return None

    total = 0

    for match in matches:
        amount = int(match.group(1))
        unit = match.group(2)

        if amount <= 0 or unit not in UNITS:
            return None

        total += amount * UNITS[unit]

    if 0 < total <= 366 * 86400:
        return total

    return None
