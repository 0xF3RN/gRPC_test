import random


random_text = {
    1:"Ты сидишь и думаешь что это паста ,но как это может быть пастой, если это даже съесть нельзя, а вот это уже паста: Ингредиенты 450г спагетти; соль - по вкусу; 200г бекона; 2 столовые ложки оливкового масла; 3 яичных желтка; 100г мелко натёртого пармезана; молотый чёрный перец - по вкусу.",
    2:"Это я - твой единственный зритель. Я на протяжении многих лет создавал иллюзию того, что тебя смотрят много людей, но это был я. Сейчас напишу это сообщение со всех аккаунтов.",
    3:"Модер, дочитай до конца, перед тем как навести на меня курсор, чтобы забанить. У меня такие связи в Роскомнадзоре, что могу по одному клику весь ваш твитч вырубить нахуй. Также не трогай моих друзей, которые скопируют это сообщение.",
    4:"deadinside✓emo✓drain✓epileptic✓paranoid✓toxic✓bipolar✓depressed✓tilted✓antisocial✓sad✓broken✓aggressive✓psycho✓apathetic✓broken-hearted✓"
}

def get_data():
    return [{"id":random.randint(1,100), 'text':random_text[random.randint(1,4)]},]