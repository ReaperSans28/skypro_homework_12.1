from typing import Any, Dict, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], value_type: str) -> Generator[Dict[str, Any], None, None]:
    """
    Эта функция возвращает итератор, который выдает по очереди операции с указанной заданной валютой.
    """
    for b in transactions:
        if b.get("operationAmount", {}).get("currency", {}).get("code") == value_type:
            yield b


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Функция transaction_descriptions возвращает описание каждой операции по очереди.
    """
    for b in transactions:
        description = b.get("description")
        if description is not None:
            yield str(description)


def card_number_generator(first_numb: int, second_numb: int) -> Generator[str, None, None]:
    """
    card_number_generator создает номера карт в указанном диапазоне.
    """
    for b in range(first_numb, second_numb + 1):
        card = f"{b:0>16}"
        new_card = card[0:4] + " " + card[4:8] + " " + card[8:12] + " " + card[12:]
        yield new_card
