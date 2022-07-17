import json


# Функция которая загрузит данные из файла


def load_candidates_from_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# Функция которая выведет кандидатов по айди

def get_candidate(candidate_id: int) -> dict:
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


# Функция которая возвращает кандидатов по имени
def get_candidates_by_name(candidate_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result

#Функция которая ищет кандидатов по скилу


def get_candidate_by_skill(skill_name: str) -> list[dict]:
    result = []
    for candidate in load_candidates_from_json():
        # исп сплит так как навыки указаны через запятую
        if skill_name in candidate['skills'].lower().split(', '):
            # если скил есть у кандидата то добавляем кандидата в список
            result.append(candidate)
    return result


