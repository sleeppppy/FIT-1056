class Lesson:
    def __init__(self, lesson_id, title, content):
        self.lesson_id = lesson_id
        self.title = title
        self.content = content
        self.type = "lesson"

    def display_lesson(self):
        print("Displaying content")

if __name__ == "__main__":
    pass