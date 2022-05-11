# Single Responsibility Principle

class MyTasks:
    def __init__(self):
        self.tasks = {}
        self.number = 0

    def add_task(self, task):
        self.number += 1
        self.tasks[self.number] = task

    def __str__(self):
        return f'{self.tasks}'

class SaveToFile:
    @staticmethod
    def save_to_file(filename, tasks):
        with open(filename, "w") as f:
            f.write(str(tasks))

t = MyTasks()
t.add_task('I want to code')
t.add_task('I want to jump')
print(t.tasks)

s = SaveToFile()
s.save_to_file('newtasklist.txt', t.tasks)