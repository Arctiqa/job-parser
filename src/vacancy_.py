class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self):
        return f'Vacancy({self.title}, {self.description}, {self.salary}, {self.description})'

    def __str__(self):
        return f'{self.title} ({self.salary}): {self.description}'
