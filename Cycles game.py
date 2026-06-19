# Підключаю колораму для зміни кольору тексту в консолі
import colorama 

colorama.init(autoreset=True)
import random
CONCENTRATION = colorama.Fore.LIGHTBLUE_EX
FIGHT = colorama.Fore.LIGHTGREEN_EX
TEXT = colorama.Fore.WHITE
YOUR_MOVE = colorama.Back.GREEN
ENEMIES_MOVE = colorama.Back.RED
CHOICE_COLOR = colorama.Fore.MAGENTA
WIN = colorama.Fore.GREEN 
LOSE = colorama.Fore.RED
CHARACTERISTICS = colorama.Fore.CYAN
INPUT = colorama.Fore.BLUE
MISS = colorama.Fore.YELLOW
ENEMIES_MISS = colorama.Fore.GREEN
REFEREE = colorama.Back.YELLOW
BAD = colorama.Fore.BLACK

MKB_is_taken = False
lives = 3
strength = 5
fight_strength = 0
agility = 5
fight_agility = 0
hp = 40
max_hp = hp
defense = 0
enemies_strenght = 5
enemies_agility = 5
enemies_hp = 20
enemies_max_hp = enemies_hp
enemies_defense = 0
def battle(hp : int,enemies_hp : int, lives : int,agility : int, strength : int)  :
    fight_strength = strength
    fight_agility = agility
    print(f"{CHARACTERISTICS}Ваші характеристики : здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility},захист = {defense}.У вас в запасі {lives} життів")
    print(f"{BAD}Характеристики ворога : здоров'я = {enemies_hp}/{enemies_hp}, сила = {enemies_strenght},спритність = {enemies_agility},захист = {enemies_defense}.")
    fight = input(f"{FIGHT}Битва почалась!")
    while hp > 0 and enemies_hp > 0:
        dodge = random.randrange(fight_agility,200)
        hit = random.randrange(fight_strength-10,fight_strength)
        enemies_hit = random.randrange(0,enemies_strenght)
        enemies_dodge = random.randrange(enemies_agility,200)
        damage = enemies_hit - defense
        enemies_damage = hit - enemies_defense
        if agility >= enemies_agility:
            if  enemies_dodge > 190:
                print(f"{MISS}Ви промахнулися,з ким не буває")
            elif enemies_damage <= 0 :
                print(f"{MISS}Ви вдарили надто слабо і навіть не залишили подряпини")
            else:
                enemies_hp -= enemies_damage
                print(f"{YOUR_MOVE}Ви вдарили вашого ворога та завдали йому {enemies_damage} шкоди.")
                if enemies_hp <= 0:
                    print(f"{WIN}Ви перемогли!")
                    break
                else:
                    print(f"Здоров'я ворога: {enemies_hp}/{enemies_max_hp}")
            if fight_agility < agility + 10 or fight_strength < strength + 10:
                print("1 - зробити фокус на ворожі удари, 2 - зробити фокус на власні удари")
                battle_desision =input(f"{INPUT}Введіть номер вашого вибору ") 
                if battle_desision == "1" and fight_agility < agility + 10:
                    fight_agility += 1
                elif battle_desision == "1" and fight_agility >= agility + 10:
                    print(f"{CONCENTRATION}Ви повність сконцентрували вашу спритність")  
                    fight_strength += 1 
                elif battle_desision == "2" and fight_strength < strength + 10:
                    fight_strength += 1
                elif battle_desision == "2" and fight_strength >= strength + 10:
                    print(f"{CONCENTRATION}Ваша сила повністю сконцентрована") 
                    fight_agility +=1  
           
            if  dodge > 150 :
                print(f"{ENEMIES_MISS}Ви вчасно відійшли назад.Ворог промахнувся")
            elif damage <= 0:
                print(f"{WIN}Ваш ворог не завдав вам шкоди")
            else:
                hp -= damage
                print(f"{ENEMIES_MOVE}Вас вдарили та завдали {damage} шкоди.")
                if  hp > 0:
                    print(f"Ваше здоров'я: {hp}/{max_hp}")
                elif hp <=0 and lives > 0:
                    print(f"{MISS}Ви програли та використали 1 життя")
                    lives -= 1
                    hp = max_hp
                    print(f"У вас залишилось {lives} життів в запасі")
                elif hp <= 0 and lives == 0:
                    print(f"{LOSE}В вас не закінчилось життів та ви вмерли.Bye-bye")
                    quit()
            
        else:
            if  dodge > 150 :
                    print(f"{ENEMIES_MISS}Ви вчасно відійшли назад.Ворог промахнувся")
            elif damage <= 0:
                print(f"{WIN}Ваш ворог не завдав вам шкоди")
            else:
                hp -= damage
                print(f"{ENEMIES_MOVE}Вас вдарили та завдали {damage} шкоди.")
                if  hp > 0:
                    print(f"Ваше здоров'я: {hp}/{max_hp}")
                elif hp <=0 and lives > 0:
                    print("Ви програли та використали 1 життя")
                    lives -= 1
                    hp = max_hp
           
                    print(f"У вас залишилось {lives} життів в запасі")
                elif hp <= 0 and lives == 0:
                    print(f"{LOSE}У вас не залишилось життів та ви вмерли.Bye-bye")
                    quit()
            if  enemies_dodge > 150:
                print(f"{MISS}Ви промахнулися,з ким не буває")
            elif enemies_damage <= 0 :
                print(f"{MISS}Ви вдарили надто слабо і навіть не залишили подряпини")
            else:
                enemies_hp -= enemies_damage
                print(f"{YOUR_MOVE}Ви вдарили вашого ворога та завдали йому {enemies_damage} шкоди.")
                if enemies_hp <= 0:
                    print(f"{WIN}Ви перемогли!")
                    break
                else:
                    print(f"Здоров'я ворога: {enemies_hp}/{enemies_max_hp}")
            if fight_agility < agility + 10 or fight_strength < strength + 10:
                print("1 - зробити фокус на ворожі удари, 2 - зробити фокус на власні удари")
                battle_desision =input(f"{INPUT}Введіть номер вашого вибору ") 
                if battle_desision == "1" and fight_agility < agility + 10:
                    fight_agility += 1
                else:
                    print(f"{CONCENTRATION}Ви повність сконцентрували вашу спритність")  
                    fight_strength += 1 
                if battle_desision == "2" and fight_strength < strength + 10:
                    fight_strength += 1
                else:
                    print(f"{CONCENTRATION}Ваша сила повністю сконцентрована") 
                    fight_agility +=1  
    return hp, enemies_hp, lives,agility,strength

print("Вітаю! Ви потрапили на міжгалактичну арену, на якій сотні досвідчених воїнів борються між собою,\nщоб набратися нових навичок і, звичайно ж, заробити трохи грошей.")
username = input("Введіть ім'я вашого персонажу ")
print(f"Ласкаво просимо,{username}")
print(f"{CHOICE_COLOR}Чи бажаєте ви пройти туторіал?")
print(f"{CHOICE_COLOR}1:Так")
print(f"{CHOICE_COLOR}2:Ні")
decision1 = input(f"{INPUT}Введіть номер вашого вибору ")
if decision1 == "1":
    print(f"{TEXT}Тоді, перейдемо до бази. У вас є 3 життя, після втрати яких вас відправлять назад на вашу жалюгідну планету,\nа також 4 основні характеристики: здоров'я, спритність, сила і захист.")
    print("Поки ваше здоров'я більше 0 (тобто вам ще не набили морду) ви б'єтеся з ворогом.")
    print("Після того як ваше здоров'я опускається до 0, ви витрачаєте одне життя і повністю відновлюєте здоров'я. Це типу 3 разове безсмертя")
    print("Далі йде спритність - теж доволі важлива річ.\nПо перше,у кого більше спритності той робить перший удар.\nПо друге,від спритності залежить ваш шанс не отримати шкоди від атаки противника")
    print("За кожні 20 спритності шанс не отримати шкоди від атаки ворога додаткові збільшується на 1")
    print("Сила ж вимірює скільки ворожого здоров'я ви можете вибити вашим удару.\nЧим вона вища - тим більше ви можете завдати шкоди")
    print("Захист - навпаки зменшує отримувану вами шкоду.Чим її більше - тим менше здоров'я в вас будуть віднімати удари ворога")
    print("Під час бою ви також можете вибрати так званий «акцент».\nЯкщо обраний вамий акцент спрямований на ворожі удари, то ваша спритність трохи збільшится,\nа якщо на ваші удари, то збільшится вже сила")
    print("Арена це дуже зручне місце для військового навчання,\nоскільки на ній є купа терепортів у різні локації,\nв яких ви можете прокачати ту чи іншу характеристику.")
    print("Туторіал завершен(мяу)")

print(f"{TEXT}І так, ви тільки-но вступаєте на величезну площу космічного корабля - місця, у центрі якого розташована та сама арена")
print(f"{CHARACTERISTICS}Ваші характеристики : здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility},захист = {defense}.У вас в запасі {lives} життів")
print(f"Якщо чесно,{username}, твої базові характеристики не дуже вражають, тож пропоную перед першим вашим боєм їх трохи підкачати")
print("У вас є вибір:")
print(f"{CHOICE_COLOR}1:Відправитися у локацію, де постійно літають стріли (прокачує спритність)")
print(f"{CHOICE_COLOR}2:Відправитись у битву проти робота-мішені(прокачує силу)")
print(f"{CHOICE_COLOR}3:Піти у кімнату з арсеналом і поцупити там щось")
print(f"{CHOICE_COLOR}4:Піти у місцеве кафе та чогось там поїсти")
decision2 = input(f"{INPUT}Введіть номер вашого вибору ")
if decision2 == "1":
    print(f"{TEXT}Ви увійшли до телепорту та потрапили за адресою.\nУ ваше плече одразу ж прилетіла стріла.\nОбернувшися ви побачили що портал додому перемістився на 100 метрів вперед")
    print(f"{CHOICE_COLOR}Вам потрібно обрати тактику")
    print(f"{CHOICE_COLOR}1:Бігти вперед скільки вистачить сили")
    print(f"{CHOICE_COLOR}2:Зпробувати пройти акуратно")
    decision2_ = input(f"{INPUT}Введіть номер вашого вибору ")
    if decision2_ == "1":
        print(f"{MISS}Ви бігли не обертаючись назад і вже за 15 секунд повернулися на локацію.\nПрийшовши в лікарню вам сказали, що рани не великі й лікування не потребують")
        hp -= 10
        agility +=1
    elif decision2_ == "2":
        print(f"{WIN}Ви пересувалися по пів метра за секунду та за увесь час отримали 6 стріл.\nПроте, це випробування непогано покращило вашу концентрацію.\nВи повернулися на базу та підлікувалися у місцевій лікарні")
        agility += 10
     
if decision2 == "2":   
    print(f"{TEXT}Ви увійшли до порталу та побачили перед собою монікен.\nНатиснувши на кнопку в нього на голові ви ввімкнули його й одразу ж дістали по морді.\nБій почався")
    hp -= 5
    hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
    strength += 5
    print("Що ж, можна сказати що це був вступний бій.\nЗавдяки ньому ваші силові навички зросли")
    print("Не буду розповідати про те, що монікен зламав вам руку,\nпросто скажу що ви пішли в лікарню підлікуватися")
    hp = max_hp
if decision2 == "3":
    print(f"{TEXT}Ви пройшли половину корабля і нарешті знайшли арсенальну.")
    print("В очі вам кинулися дві блискучі дрібнички:\nзачарований залізний меч, який на вигляд може вбити будь-кого за один удар,\nа також срібний перстень, яка нічим не виділяється.")
    print(f"{CHOICE_COLOR}Що ви вкрадете?")
    print(f"{CHOICE_COLOR}1:Меч, що дає вам безмежну силу та могутність(будь ласка,{username},не втрачай такої можливості)")
    print(f"{CHOICE_COLOR}2:Перстень,просто перстень")
    decision2__ = input(f"{INPUT}Введіть номер вашого вибору ")
    if decision2__ == "1":
        print(f"{LOSE}Щойно ви взяли цей меч могутності, ви одразу відчули, що щось тут не так.\nМабуть я переплутав і він був не зачарований а проклятий.Ну,буває")
        strength = -9999
        lives -= 3
    else:
        print(f"{WIN}Як тільки ви наділи перстень то відчули небувалу легкість і життєрадісність. Щось явно змінилося...")    
        lives += 3
elif decision2 == "4":
    print(f"{TEXT}Ви підійшли до кафе та побачили у меню лише 2 позиції.\n{CHOICE_COLOR}Що будете їсти?")
    print(f"{CHOICE_COLOR}1:Бабл ті зі смаком води ")
    print(f"{CHOICE_COLOR}2:Воду зі смаком бабл ті")
    decision2___ = input(f"{INPUT}Введіть номер вашого вибору ")
    if decision2___ == "1":
        print(f"{WIN}Ви спробували напій та відчули смак звичайної води.\nПрактично, без зайвих коментаріїв")
        hp += 10
        max_hp = hp
        strength += 3
        agility += 3
    else :
        print(f"{LOSE}]Цей напій - це гірше що ви колись коштували у своєму житті.На смак як жаба змішана с ураном")
        hp -= 20
print(f"{CHARACTERISTICS}Ваші характеристики : здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility},захист = {defense}.У вас в запасі {lives} життів")
print(f"Щож настав ваш час виходити на ринг.\nНу що,{username}, ти готовий?")
print(f"{CHOICE_COLOR}1:Так")
print(f"{CHOICE_COLOR}2:Ні")
decision3= input(f"{INPUT}Введіть номер вашого вибору ")
while decision3 == "2":
    print(f"{TEXT}Добре, я почекаю.\nНу що, готовий?")
    print(f"{CHOICE_COLOR}1:Так")
    print(f"{CHOICE_COLOR}2:Ні")
    decision3= input(f"{INPUT}Введіть номер вашого вибору ")
print(f"{TEXT}Ви вийшли на арену і побачили сотні місць для спостерігачів.\nПрийшовши на середену арени, ви тільки но побачили вашого ворога - це була свиня в обладунках🤨.")
print("Що ж, і таке буває, але вже підзно відступати.Час битися")
print(f"{REFEREE}Рефері: ласкаво просимо на міжзоряну арену. місце,де ви побачите бої воїнів із різних куточків нашого світу")
print(f"{REFEREE}Це те самі місце,де ви побачите бої воїнів із різних всесвітів")
print(f"{REFEREE}Час представити вам наших сьогоднішніх бійців.")
print(f"{REFEREE}Праворуч від вас - Великий містер Хряк, воїн який переміг цілих 0 разів за останні 0 боїв.")
print(f"{REFEREE}Зліва ж - наш новий боєць, який щойно ступив на шлях світової зірки: {username}")
print(f"{REFEREE}Іііііі ми починаємо цей бій під ваші оплески!")
enemies_hp = 30
enemies_hp = enemies_max_hp
enemies_agility = 0
enemies_strenght = 10
enemies_defense = 5
hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
if lives >= 3:
    print(f"{REFEREE}і з цієї битви переможцем виходить {username}!")
elif lives < 3:
    print(f"{REFEREE}і з цієї битви переможцем виходить {username}!")   
    print(f"(P.S Я навіть не уявляв собі наскільки ти слабкий)") 
agility += 5
strength += 5
print(f"Мої привітання {username}, ти виграв свій перший реальний бій\n(гірше я нічого не бачив).\nАле незважаючи на це твої характеристики непогано так підвищилися")   
print(f"{TEXT}Так як я сьогодні добрий можеш перепочити,полікуватися йдемо далі.\nВпереді тебе чекає ще 2 етапи першої частини турніру,\nпісля чого в тебе буде ще купа часу підготуватися до 2 частини ")
hp = max_hp
print(f"{CHARACTERISTICS}Ваші характеристики : здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility},захист = {defense}.У вас в запасі {lives} життів")
print(f"Все, час на відпочинок вийшов - переходимо знову до тренування.{CHOICE_COLOR}\nКуди підемо?")
print(f"{CHOICE_COLOR}1:Піти у портал зі стежкою перешкод (прокачує спритність)")
print(f"{CHOICE_COLOR}2:Піти у портал до брата містера Хряка який хоче вам помститися та 'поспілкуватися' з ним ")
print(f"{CHOICE_COLOR}3:Довіриться мені, зав'язати в очі й увійти в третій портал, над яким висить вивіска:\n{BAD}«Обережно, небезпечно!»")
decision4= input(f"{INPUT}Введіть номер вашого вибору ")
if decision4 == "1":
    print("Ви увійшли до порталу та побачили довжезну дорогу з шипами, пилами, сокирами і навіть гейзерами з лавою.")
    print("Пройшовши половину шляху ви втратили половину здоров'я(як перфекціонічно).\nІ несподівано, просто з неба, перед вами з'являється лоза,\nяка по всій довжині оснащена колючками")
    print("Судячи з прогнозів, якщо ви продовжите йти, то помрете прямо перед виходом.\nНе забувайте, що навіть якщо у вас ще є життя, після смерті ви все одно повернетеся на початок випробування.\nМоже це ваш шанс?")
    print(f"{CHOICE_COLOR}1:Піднятися по лозі(якщо ви доторкнетесь до вершини зони випробування, то повернетеся на базу) ")
    print(f"{CHOICE_COLOR}2:Продовжити йти далі")
    decision4_ = input(f"{INPUT}Введіть номер вашого вибору ")
    if decision4_ == "1":
        print("Ви взялися за лосу та одразу відчули біль від колючок, але шляху назад уже немає.\n Ви піднімалися по колючій лозі близько півгодини,\nваші долоні змішалися з вашою кров'ю і виглядали як варення")
        print("Коли ви нарешті доторкнулися до неба ви миттєво телепортулися на корабель.")
        print(f"{LOSE}Після такого, ви лежали у відключці пів дня, а коли прокинулися зрозуміли, що ваші нервові рецептори повністю стерлися,{WIN}тепер ви майже не відчуваєте біль.")
        hp = hp//2
        defense = 20
    else:
        print(f"{MISS}Сподіваючись на краще майбутнє ви продовжили йти.Використовую всі ваші можливості ви йшли дуже обережно и всеж таки дійшли до кінця з {hp/10} здоров'я ")
        print("Після того як ви увійшли у телепорт на базу то перепочили хвилин 10, пішли відлікувалися(лікарі вже не хочуть вас бачити)")
        hp = max_hp
        print(f"{WIN}Не дивлячись на те, що ви майже потрапили в цикл нескінченних смертей, ви потужно покращили вашу спритність")
        agility += 20
elif decision4 == "2":
    print(f"{TEXT}Ви зайшли в телепорт та одразу ж побачили перед собою величезну чорну свиню з білим хвостиком.\nНе встигнувши нічого сказати, свиня обматехрюкала вас і бій почався")    
    enemies_hp = 150
    enemies_max_hp = enemies_hp
    enemies_strenght= 30
    enemies_agility = 0
    enemies_defense = 0
    hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
    print("Ви перемогли нагле свинорило,проте вирішили його не добивати.\nВаші удари стали сильнішими.Ви знову пішлу у лікарьню(це раз десятий десь,так?)і підлікувалися")
    strength += 10
    hp = max_hp
elif decision4 == "3":
    print("Ви зав'язали очі,увійшли в портал і відчули знайоме відчуття.\nЦе була ваша рідна планета")
    print(f"Друже, так як я задовбався з тобою наньчитися,\nя думаю що краще тобі відпочити від арени.\n{WIN}Бувай!.{BAD}Після цього телепорт зник")
    quit()
print(f"{CHARACTERISTICS}Ваші характеристики : здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility},захист = {defense}.У вас в запасі {lives} життів")
print(f"{TEXT}Що ж, в тебе вже доволі непогані характеристики,\nпроте я вважаю що мати побільше здоров'я теж було б непогано")
print("Піди до кімнати алхімії,там ти можешь обміняти невелику кількість характеристик на здоров'я")
print("Ви підійшли до алхімії і побачили верстак обміну характеристик")
print("На ньому написно : поклади руку на символ на верстаку.Ти отримаєшь 5 здоров'я, проте втратишь 1 силу та спритність")
decison_trade = input("1- продовжити обмін 2 - закінчити")
while decison_trade == "1":
    hp += 5
    max_hp = hp
    strength -= 1
    agility -= 1
    print(f"{CHARACTERISTICS} здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility}")
    if agility == 0 or strength == 0:
        break
    decison_trade = input("1- продовжити обмін 2 - закінчити ")
print("Обмін закінчено")
print(f"{TEXT}Твое друге тренування закінчено і вже скоро ти зустрінешся з твоїм новий супротивником")
print("Але перед цим, заглянь в арсенальну, перед другим боєм тобі видадуть екіпіровку ")
print("Ви знайшли арсенальну і у вас одразу спитали ваше ім'я")
decison_name = input("Введіть ваше ім'я, на яке ви реєструвалися ")
if decison_name == username:
    print(f"{WIN}Після того,як ви сказали своє ім'я вам видали стандартне знаряддя:залізний шолом, броня і меч")
    defense += 15
    strength += 10
else:
    print(f"{LOSE}Так як ім'я своє ти не підтвердив, то знаряддя тобі не дали({BAD}ідіот)")
print(f"{TEXT}Прийшовши на арену, кількість глядачів збільшилася у 2 рази,\nневже люди так люблять дивитя як 2 чоловіка лупасять один одного?")
print(f"І так,{username},ти на середині арени дивишся в так звані очі механизованого самурая")
print(f"{REFEREE}Рефері: ласкаво просимо на другий бій міжзоряної арени")
print(f"{REFEREE}В цей раз  нашого колишнього новачка зіткнуло з справжнім раритетним воїном")
print(f"{REFEREE}Час представити вам наших сьогоднішніх бійців.")
print(f"{REFEREE}Праворуч від вас - робот-самурай,\nреліквія,що бере участь в наших битвах вже 1000 років.")
print(f"{REFEREE}Зліва ж - наш боєць,якого ми вже бачили\n і який захопив наші серця з першої битви - {username}")
print(f"{REFEREE}Пані та панове, ми починаємо цей бій!")
enemies_hp = 200
enemies_max_hp = enemies_hp
enemies_strenght = 30
enemies_agility = 15
enemies_defense = 15
hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
strength += 20
agility += 5
defense += 5
print("Під час бою,ви поцупили нарукавники у самурая\nі крім бойового досвіду підвищили свій захист")
print(f"{CHARACTERISTICS}Ваші характеристики : здоров'я = {hp}/{max_hp}, сила = {strength},спритність = {agility},захист = {defense}.У вас в запасі {lives} життів")
print("Після битви ви як зазвичай пішли підлікуватися, на що вам сказали смокчи лапу")
print("Здається, безкоштовна медецина закінчилася.Тепер прийдется знаходити самому де можна підлікуватися.")
print(f"Настав час вашого третього тренування.\n{CHOICE_COLOR}Куди підемо наостанок?")
print(f"{CHOICE_COLOR}1:Піти у клуб 'Легенди про мавпячого короля'\n2:Піти у кафе перекусити")
decison_5 = input(f"{INPUT}Введіть номер вашого вибору  ")
if decison_5 == "1":
    print("Ви прийшли на прослуховування легенди про якогось короля мавп і його посох.\nПерша година історії була дуже нудною і ви вже хотіли піти,\nяк раптом на п'єдесталі, що стояв посередині клубу, з'явився посох")
    print("Це був справжній посох короля мавп - зброя, що дає небувалу силу.\nПроте,посох охоронявся трьома солдатами.\nНезважаючи на це, ви зобов'язані отримати посох")
    print("Ви різко встали підійшли до солдатів та побачили бій")
    enemies_hp = 50
    enemies_max_hp = enemies_hp
    enemies_strenght = 30
    enemies_defense = 20
    enemies_agility = 10
    hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
    print("Проте не треба відволікатися, це лише перший солдат")
    enemies_hp = 50
    enemies_strenght = 30
    enemies_defense = 20
    enemies_agility = 10
    hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
    print("Залишився останній")
    enemies_hp = 50
    enemies_strenght = 30
    enemies_defense = 20
    enemies_agility = 10
    hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
    print(f"{WIN}Хоч ви й розполохали всю публіку, зате стародавній посох тепер у вас")
    MKB_is_taken = True
else:
    print("По дорозі в кафе ви встрітили людину одягнену в красивий і елегантний костюм, а також з валізою в руці.\nВона підійшла до вас, відкрила валізу та дістала звідти")
    print(f"булочку і дивний напій,після чого запропонувала їх вам, але ви можете вибрати тільки одне.{CHOICE_COLOR}\nЩо ви візьмете?")
    print(f"{CHOICE_COLOR}1:Булочку\n2:Напій\n3:Я в ці ігри вже грав")
    decison_5_ =  input(f"{INPUT}Введіть номер вашого вибору  ")
    if decison_5_ == "1":
        print(f"Ви взяли булочку,після чого людина щиро вам посміхнулася та пішла далі.\n{WIN}Після того як ви її скуштували,одразу відчули незвичайне насичення")
        hp += 100
    elif decison_5_ == "2":
        print(f"Ви взяли напій,після чого людина ехидно вам посміхнулася і пішла далі.\n{LOSE}Скуштувавши його ви відчули сильну нудоту і біль у животі.\nПісля кількох хвилин пекельного болю ви прийшли до тями і зрозуміли,\nщо дуже даремно взяли цей напток.")    
        lives -= 1
    elif decision1 == "3":
        print(f"{MISS}Людина дивно на вас подивилася на пішла далі.")
    print("Нарешті ви дійшли до кафе і побачили що в меню є лише 1 страва:\nсмажений кабанчик ")  
    print("Так як хотілося їсти дуже сильно,тимпач це безкоштовно,\nви поласували цим делікатесом та знатно наїлися")  
    hp += 30
    strength += 15
print("Ось і підішла кінцівка вашого бійцівського життя.Ви в останнє виходите на арену та чуєте гомін глядачів")
print(f"{REFEREE}Рефері: ласкаво просимо на останній  бій  першої частини міжзоряної арени")
print(f"{REFEREE}В цій битві, наш вже професіональний воїн{username} буде битися проти лютого воїна з планети під назвою 'Лофу Сяньчжоу'")
print(f"{REFEREE}Час представити вам наших сьогоднішніх бійців.")
print(f"{REFEREE}Праворуч від вас - Хулей, стародавня потвора,\nщо тереризувала населення своєї планети тисячоліттями")
print(f"{REFEREE}Зліва ж від нас, вже усім відомий - {username}")
print(f"{REFEREE}І так, я хочу проголосити, наш останній бій!")
if MKB_is_taken == False:
    print(f"{BAD}Дивлячись в очі величезному вовкодаву,вы вперше за останній час відчули страх.\nВаші ноги затремтіли,а руки не піддавались контролю")
    decision_scared = input(f"{BAD}У тебе є вибір 1: вмерти 2: вмерти")
    repeat = 0
    while  True:
        decision_death = input(f"{LOSE}Ти здохнеш!")
        repeat += 1
        if repeat == 10:
            break
    decision = input(f"{TEXT}Аууу, ти ще довго зібрався труситися?\nПройшов стільки боїв,а залишился таким же дохликом.\nЕх, нічого без мене не можешь")
    print("Прийдется мені віддати тобі трохи моєї сили")    
    hp += 300
    max_hp = hp
    strength += 50
    print(f"{MISS}Вас переповнює рішучість")
    false_decision = input("Ваші характеристики...")
    print("А накой чорт тобі твої характеристики?Все в тебе чіназес")
    enemies_hp = 500
    enemies_max_hp = enemies_hp
    enemies_strenght = 50
    enemies_agility = 10
    enemies_defense = 10
    hp,enemies_hp,lives,agility,strength = battle(hp,enemies_hp,lives,agility,strength)
    print(f"{WIN}Після вашої перемоги половина глядачів зірвали своє горло.\nЦе було незабутньо")
else:
    print("Лише одним ударом магічного посоха ви не залишили від вовкодава і пилинки")
    print(f"На арені настала хвилина мовчання,всі були в шоці\nПроте факт залишається фактом,\n{WIN}Ти,{username},переможець!")
print(f"На цій щасливій ноті і закінчилася перша частина вашої історії.Я буду сумувати за тобою,{username}🥲🥲🥲")