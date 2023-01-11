MALE = True
FEMALE = False

class Human:
    def __init__(self, name: str, gender: bool, year: int, father=None, mother=None, husband=None, wife=None):
        self.name = name
        self.gender = gender
        self.father = father
        self.mother = mother
        self.husband = husband
        self.wife = wife
        self.year_born = year
        self.status = 'ok'

    def get_age(self, year: int) -> int:
        return year - self.year_born

    def alive(self) -> bool:
        return (self.status == 'ok')

    def die(self) -> None:
        self.status = 'die'

class Throne:
    def __init__(self, first_king_name: str, year: int):
        # public
        self.kings = list()
        self.kings.append(Human(first_king_name, MALE))
        # private
        self.__king_ptr = 0
        self.__year = year

    def __get_king(self):
        return self.kings[self.__king_ptr]

    def __find_king(self, name: str) -> Human:
        for ind, king in enumerate(self.kings):
            if king.name == name:
                return ind 

    def __get_new_king(self, king: Human, gender: bool|None):
        max_age = -1
        max_child = None
        for king_ in self.kings:
            if king_.father == king:
                if gender != None or king_.gender == gender:
                    age = king_.get_age(self.__year)
                    if age > max_age and king_.alive():
                        max_child = king_
                        max_age = age
        return max_child

    def marry(self, husband_name: str, wife_name: str) -> None:
        h_id = self.find_king(husband_name)
        self.kings.append(Human(wife_name, FEMALE, husband=self.kings[h_id]))
        self.kings[h_id].wife = self.kings[-1] 
    
    def new_born(self, name: str, gender: bool) -> None:
        self.kings.append(Human(name, gender, self.__get_king(), self.__get_king().wife))
    
    def die(self, name: str):
        king_ptr = self.__find_king(name)
        self.kings[king_ptr].die()
        if king_ptr == self.__king_ptr:
            new_king = self.__get_new_king(name)
            self.__king_ptr = self.__find_king(new_king.name)

    def simulate(self) -> None:
        ...