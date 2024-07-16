import random
import typing


class Unit:
    lessons: int
    idx: int

    def __init__(self, lessons: int, idx: int):
        self.lessons = lessons
        self.idx = idx

    @staticmethod
    def from_dict(data: dict, idx: int):
        return Unit(data["lessons"], idx)


class Section:
    name: str
    units: typing.List[Unit]

    def __init__(self, name: str, units: typing.List[Unit]):
        self.name = name
        self.units = units

    @staticmethod
    def from_dict(data: dict):
        units = []
        for idx, unit in enumerate(data["units"]):
            units.append(Unit.from_dict(unit, idx))
        return Section(data["name"], units)


class LessonSelection(typing.NamedTuple):
    section: Section
    unit: Unit
    lesson: int


class Language:
    name: str
    sections: typing.List[Section]

    def __init__(self, name: str, sections: typing.List[Section]):
        self.name = name
        self.sections = sections

    @staticmethod
    def from_dict(data: dict):
        sections = []
        for section in data["sections"]:
            sections.append(Section.from_dict(section))
        return Language(data["name"], sections)

    def get_random_lesson(self) -> typing.Optional[LessonSelection]:
        lessons = []
        for section in self.sections:
            for unit in section.units:
                if unit.lessons > 0:
                    for lesson_index in range(unit.lessons):
                        lessons.append(LessonSelection(section, unit, lesson_index))

        if not lessons:
            return None

        print(f"Choosing from {len(lessons)} lessons")
        lesson = random.choice(lessons)
        return lesson
