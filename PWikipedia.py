import wikipedia

class PWikipedia:
    def __init__(self, locale: str='ru'):
        wikipedia.set_lang(locale)

    def get_info(self, king_name: str):
        kpage = wikipedia.page(king_name)
        print(kpage.html())

pwikipedia = PWikipedia()
pwikipedia.get_info('Амогус')