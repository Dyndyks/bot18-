from handlers.mat_handler.spisok_mat import tup_mat


class ObrabotkaMat():
    chat = {}

    @classmethod
    def set_chat(cls, chat_id: int, razr: bool):
        '''Добавление и измениния на разрешение обработки мата для чата'''
        cls.chat[chat_id] = razr

    @staticmethod
    def proverka(text: str):
        '''Метод проверяет есть ли мат в тексте'''
        lst_text = [''.join([b.lower() for b in word if b not in ('?,.:')]) for word in text.split()]
        for word in lst_text:
            if word in tup_mat:
                return True
        return False
    
    @staticmethod
    def red_text(text: str):
        '''Скрывает мат в тексте'''
        lst_text = [''.join([b.lower() for b in word if b not in ('?,.:')]) for word in text.split()]
        text = ''.join([text.replace(word, f'<tg-spoiler>{word}</tg-spoiler>') for word in lst_text if word in tup_mat])
        return text
