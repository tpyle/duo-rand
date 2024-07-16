import argparse
import pathlib

import yaml

import db


def parse_args():
    parser = argparse.ArgumentParser(
        description="A tool for finding a random lesson in Duolingo"
    )
    parser.add_argument("language", type=str, help="The name of the language")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Finding a random lesson in {args.language}")
    language = args.language
    language_path = pathlib.Path("db") / f"{language}.yaml"
    if not language_path.exists():
        language_path = pathlib.Path("db") / f"{language}.yml"
    if not language_path.exists():
        print(f"Language {language} not found")
        return

    print(f"Language {language} found at {language_path}")

    # Load the language data
    with open(language_path) as f:
        language_data = yaml.safe_load(f)

    lang = db.Language.from_dict(language_data)

    lesson = lang.get_random_lesson()

    if not lesson:
        print("No lessons found")
        return
    else:
        print(
            f"Random lesson: {lesson.section.name} - Unit {lesson.unit.idx + 1} - Lesson {lesson.lesson + 1}"
        )


if __name__ == "__main__":
    main()
