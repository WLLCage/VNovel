# script.rpy — Пролог демо (v2)
define narrator = Character(None)

define y  = Character("Янас",    color="#d8d8ff")
define eg = Character("Егор",    color="#ffd8d8")
define zh = Character("Жека",    color="#d8ffd8")
define ru = Character("Руфа",    color="#fff0b3")
define dk = Character("Даня",    color="#b3f0ff")
define sv = Character("Сава",    color="#e6e6e6")
define vi = Character("Виталя",  color="#ffe6b3")
define to = Character("Тоха",    color="#f0b3ff")
define ts = Character("Тос",     color="#c8c8c8")
define le = Character("Лёха",    color="#ffb3d9")

# Вводятся на пьянке
define bu = Character("Буга",    color="#ffd1a8")
define sh = Character("Шкарик",  color="#b3ffda")
define vo = Character("Вова",    color="#b3d9ff")
define sa = Character("Саня",    color="#b3ffb3")

# Опционально (если хочешь вводить раньше Монголии)
define na = Character("Намжил",  color="#d1c4ff")

# NVL для "чата"
define vk = Character(None, kind=nvl, what_color="#ffffff")

default met_sanya = False

define audio.bgm_morning = "audio/bgm/bgm_morning_01.ogg"
define audio.bgm_school  = "audio/bgm/bgm_school_01.ogg"
define audio.bgm_party   = "audio/bgm/bgm_party_01.ogg"
define audio.bgm_ominous = "audio/bgm/bgm_ominous_01.ogg"

define audio.sfx_alarm      = "audio/sfx/sfx_alarm_01.ogg"
define audio.sfx_toothbrush = "audio/sfx/sfx_toothbrush_01.ogg"
define audio.sfx_kettle     = "audio/sfx/sfx_kettle_01.ogg"
define audio.sfx_school_bell= "audio/sfx/sfx_school_bell_01.ogg"
define audio.sfx_vk_ping    = "audio/sfx/sfx_vk_ping_01.ogg"
define audio.sfx_gate       = "audio/sfx/sfx_gate_01.ogg"
define audio.sfx_pour       = "audio/sfx/sfx_pour_01.ogg"
define audio.sfx_laughter   = "audio/sfx/sfx_laughter_01.ogg"
define audio.sfx_stove_click= "audio/sfx/sfx_stove_click_01.ogg"
define audio.sfx_gas_hiss   = "audio/sfx/sfx_gas_hiss_01.ogg"
define audio.sfx_fall       = "audio/sfx/sfx_fall_01.ogg"

# BG
image bg bedroom   = "images/bg/bg_bedroom_morning_01.jpg"
image bg bathroom  = "images/bg/bg_bathroom_01.jpg"
image bg kitchen   = "images/bg/bg_kitchen_breakfast_01.jpg"
image bg street    = "images/bg/bg_street_to_school_01.jpg"
image bg hall      = "images/bg/bg_school_hall_01.jpg"
image bg classroom = "images/bg/bg_classroom_01.jpg"

image bg egor_yard    = "images/bg/bg_egor_house_yard_01.jpg"
image bg egor_living  = "images/bg/bg_egor_house_livingroom_01.jpg"
image bg egor_kitchen = "images/bg/bg_egor_house_kitchen_01.jpg"

# CG
image cg stove = "images/cg/cg_stove_gas_01.jpg"

# UI
image phone = "gui/phone_overlay.png"

# Sprites (для демо достаточно neutral; остальные эмоции подключишь позже)
image yanas   = "images/char/ch_yanas_neutral.png"
image egor    = "images/char/ch_egor_neutral.png"
image zheka   = "images/char/ch_zheka_neutral.png"
image rufa    = "images/char/ch_rufa_neutral.png"
image danya   = "images/char/ch_danya_neutral.png"
image sava    = "images/char/ch_sava_neutral.png"
image vitalya = "images/char/ch_vitalya_neutral.png"
image toha    = "images/char/ch_toha_neutral.png"
image tos     = "images/char/ch_tos_neutral.png"
image lekha   = "images/char/ch_lekha_neutral.png"

image buga    = "images/char/ch_buga_neutral.png"
image shkarik = "images/char/ch_shkarik_neutral.png"
image vova    = "images/char/ch_vova_neutral.png"
image sanya   = "images/char/ch_sanya_neutral.png"
image namzhil = "images/char/ch_namzhil_neutral.png"

label start:
    jump prologue

label prologue:
    # СЦЕНА 1 — Утро
    play music bgm_morning fadein 1.5
    scene bg bedroom with fade
    play sound sfx_alarm
    narrator "Будильник не звонил. Он просто настаивал."
    show yanas at center
    y "Янас Рал. Новенький. Так меня записали в журнал."
    y "Свалиться в середину учебного года — как зайти в кино на сороковой минуте."
    hide yanas with dissolve

    scene bg bathroom with fade
    play sound sfx_toothbrush
    narrator "Я чищу зубы и репетирую нейтральное лицо."
    narrator "Нейтральное лицо — мой главный предмет."

    scene bg kitchen with fade
    play sound sfx_kettle
    narrator "Завтрак — это когда ты ешь, чтобы не думать. Сегодня не получилось."

    scene bg street with fade
    narrator "По дороге в школу я успел придумать десять вариантов, как всё пойдёт плохо."
    narrator "Школа оказалась изобретательнее."

    # СЦЕНА 2 — Коридор (первые знакомства)
    stop music fadeout 1.0
    play music bgm_school fadein 1.5
    scene bg hall with fade
    narrator "Коридор шумел так, будто репетировал жизнь."
    narrator "Я ещё не знал, что этот шум — мой будущий отряд."

    show zheka at left
    zh "Жека. Если кто начнёт ломать мораль — я скажу. Иногда громко."
    narrator "Он посмотрел на меня так, будто проверял, где у меня граница."
    hide zheka with dissolve

    show rufa at right
    ru "Руфа. Если тебе станет плохо — говори. Я стоматолог, но… не придирайся к специализации."
    narrator "Он произнёс это как заботу и угрозу одновременно."
    hide rufa with dissolve

    show danya at left
    dk "Даня. Если понадобится что-то достать — можно попробовать."
    narrator "Он говорил очень просто. И от этого было надёжно."
    hide danya with dissolve

    show vitalya at right
    vi "Виталя. Я тут… просто живу. Если что — не нервничай."
    narrator "Это было сказано так, будто нервничать — нарушение дисциплины."
    hide vitalya with dissolve

    show sava at left
    sv "Сава. Я обычно в кадре недолго. Но если появляюсь — значит момент важный."
    narrator "Он сказал это и сам себе кивнул. Как будто поставил отметку."
    hide sava with dissolve

    play sound sfx_school_bell
    narrator "Звонок прозвучал, как стартовый пистолет."

    # СЦЕНА 3 — Класс (дознакомство)
    scene bg classroom with fade
    narrator "Класс смотрел на меня дружно. Я чувствовал себя ошибкой в Excel."
    show yanas at center
    y "Доброе утро."
    hide yanas with dissolve

    narrator "Учитель истории поднял голову и начал делать вид, что всё по плану."

    show egor at left
    eg "Егор. У меня дома можно собираться. Дом — частный, шум — общий."
    narrator "Он сказал это так, будто приглашение уже подписано печатью."
    hide egor with dissolve

    show toha at right
    to "Тоха. Если что — я за закон. В смысле… за понятие закона."
    narrator "Он произнёс это так, будто закон — живое существо."
    hide toha with dissolve

    show tos at left
    ts "Тос. Я обычно молчу. Но если пошутил — значит доверяю."
    narrator "Он кивнул. Это выглядело как договор."
    hide tos with dissolve

    show lekha at right
    le "Лёха. Я серьёзный. Не потому что хочу — потому что так вышло."
    narrator "Его спокойствие было не позой. Скорее — выученной формой."
    hide lekha with dissolve

    narrator "И так, почти без объявления, у меня появились имена."

    # СЦЕНА 4 — Урок истории: ввод про Унгерна
    narrator "История началась с того, что нас попросили слушать внимательно."
    narrator "В такие моменты обычно происходит что-то, о чём потом жалеют."

    narrator "Учитель говорил о гражданской войне и о том, как иногда один человек превращается в целую проблему."
    narrator "Имя проблемы звучало длинно, но в пересказах его сокращали до одного слова: барон."
    narrator "Барон Унгерн где-то в Монголии собирал вокруг себя войну, мистику и дисциплину."
    narrator "А ещё — слухи. Слухи всегда приходят раньше армии."

    # СЦЕНА 5 — Чат «Нижний Флекс»
    play sound sfx_vk_ping
    show phone at truecenter
    narrator "Телефон вибрировал в кармане так, будто хотел сбежать."
    narrator "Меня добавили в беседу."

    nvl clear
    vk "{b}Беседа: Нижний Флекс{/b}"
    vk "{b}Жека:{/b} Новенький добавлен. Янас Рал. Не ломаем."
    vk "{b}Егор:{/b} Сегодня у меня сбор. Чевапчичи будут."
    vk "{b}Тоха:{/b} Во сколько? Я после школы."
    vk "{b}Руфа:{/b} Я могу заехать в магаз. Только без цирка."
    vk "{b}Даня:{/b} Я по пути. Если что — докину напитки."
    vk "{b}Виталя:{/b} Я рядом. Но я трезво оцениваю только то, что не происходит."
    vk "{b}Сава:{/b} Я появлюсь, если будет повод."
    vk "{b}Буга:{/b} Я на тачке. Если надо — закину кого."
    vk "{b}Шкарик:{/b} Я возьму колонку. Будет культурно. Почти."
    vk "{b}Вова:{/b} Я подскочу. У меня сегодня режим «не трогаем реальность»."
    vk "{b}Егор:{/b} И Саню позову. Он не из школы, но без него не то."
    # vk "{b}Намжил:{/b} Подъеду, если будет уважение к мясу."
    nvl clear

    hide phone
    narrator "В беседе всё звучало так, будто это обычный четверг."
    narrator "Я ещё не знал, что обычные четверги — это ловушка."

    # СЦЕНА 6 — Приход к Егору (частный дом)
    stop music fadeout 1.0
    play music bgm_party fadein 1.5
    scene bg egor_yard with fade
    play sound sfx_gate
    narrator "Дом Егора стоял отдельно, как человек, который уже всё понял."
    narrator "Калитка скрипнула и впустила нас так, будто тоже участвует."

    scene bg egor_living with fade
    narrator "Внутри пахло специями, деревом и уверенностью, что «всё будет нормально»."
    narrator "Эта уверенность — главный алкоголь страны."

    # Ввод тех, кто не в школе
    show buga at left
    bu "О, новенький. Я Буга. Если что — я руками могу. И машиной."
    narrator "Он сказал это без пафоса. От этого звучало серьёзно."
    hide buga with dissolve

    show shkarik at right
    sh "Я Шкарик. Музыку поставлю так, что даже стены согласятся."
    narrator "Он улыбнулся. Улыбка была как предупреждение."
    hide shkarik with dissolve

    show vova at left
    vo "Вова. Слышал, ты новый. Норм. Мы тут как патч на жизнь — иногда лечит, иногда ломает."
    narrator "Он сказал это спокойно. Будто так и надо."
    hide vova with dissolve

    show sanya at right
    sa "О, новенький! Я Саня. Я не из школы, но я из вашей проблемы."
    $ met_sanya = True
    hide sanya with dissolve

    play sound sfx_pour
    narrator "Пластиковые стаканчики звучали торжественнее, чем должны."
    play sound sfx_laughter
    narrator "Кто-то смеялся. Это было похоже на репетицию будущей катастрофы."

    # СЦЕНА 7 — Кухня, плита, газ
    scene bg egor_kitchen with fade
    stop music fadeout 1.0
    play music bgm_ominous fadein 1.0
    narrator "Егор жарил чевапчичи так сосредоточенно, будто сдавал экзамен."

    show egor at left
    eg "Ща будет. Главное — не трогать плиту."
    narrator "Это всегда плохая фраза."
    hide egor with dissolve

    play sound sfx_stove_click
    narrator "Щелчок."
    play sound sfx_gas_hiss
    narrator "Шипение было тихим. Настолько тихим, что его можно было принять за шутку."

    show cg stove with dissolve
    narrator "На секунду мне показалось, что воздух стал тяжелее."
    hide cg stove with dissolve

    narrator "Слова в гостиной стали далёкими. Потом — плоскими."
    play sound sfx_fall
    scene black with fade
    stop music fadeout 1.5
    narrator "Тьма пришла без предупреждения."
    narrator "И почему-то пахла газом."
    narrator "..."
    narrator "Дальше будет Иркутск. Только не этот."
    return
