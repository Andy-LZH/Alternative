# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define s = Character("苏千", color = "25A1DF")
define pb = Character("警官B", color = "25A1DF")
define zhongyuan = Character("中原警官", color = "25A1DF")
define boya = Character("博雅警官", color = "25A1DF")
define cheyangzi = Character("车佯子", color = "25A1DF")
define ailunsi = Character("艾伦斯", color = "25A1DF")

define gui.text_font = "FZSJ-DQYBKSJW.TTF"

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。
    "刚醒来"
    image s_original = "suqian.png"
    image s_fit = im.FactorScale("suqian.png", 0.28)
    show s_fit at left

    s "啧，该死（头好痛，现在什么时间）诶 为什么我头上有绷带"

    s "看了看表十点？！！|猛然从床上坐起| 为什么没有人来喊我？"

    s "呵，这家伙一做实验就忘记喊我……"

    s "伸了个懒腰，一边打哈欠一边往前走 莱恩斯老师你又不喊我，老是迟到，我是很不好意思哒～～～"
    # 黑黑屏，换场景（莱恩斯实验室

    s "莱恩斯老......!!!!"
    #  Made the first choice
    menu:
        "赶紧报警":
            jump gameMainOne

        "不报警":
            jump firstConsequence



label first_consequence:
    "【警察 is watching you】你为什么不信任我们警察，缺少人与人之间信任的你，摸着你的良心回到开头再来一次"
    jump start


label gameMainOne:
    # 警方进入实验室

    scene




    pb "死者，莱恩斯，年龄34，生前是一名科学家，目前与其助手苏千同住"

    "中原警官掏出打火机，正想点上他的手卷烟"

    s "【上前阻止】警官先生，在这种场合抽烟好像不大好吧～～"

    zhongyuan "啊，真是非常的抱歉啊！对了，苏先生，然后要麻烦你了，要请你配合我们调查一下时间线了。"

    s "没问题。警官先生，不要这样生分嘛，叫我小苏就好啦【苏千把手搁在警官的肩上，笑着说】"

    zhongyuan "好..好啊，小苏，小苏蛮亲切的【神情有些尴尬的微笑】"

    # 黑屏换场景 apply fade
    boya "苏千先生，请问你这几天都在哪里，见过什么人？"

    s "好的好的。【挠头】啊，我这几天都在外地，额…"

    pb "请务必如实回答！"

    s "该死的，我想不起来了…"

    pb "想不起来？我不接受这个回答，请你好好配合调查。"

    s "我真的…（呃，头好痛，要裂开了）真的不记得了。"

    pb  "苏千先生！你这是在逃避回答，我…"

    zhongyuan "好了博源,别说了。【关切地看了一眼苏千】老师刚刚去世，想必小苏心里也不舒服，别逼他了。我去看看现场，你先搜寻一下房子吧。"

    pb " 好的，前辈！"

    s "谢谢了。"

    # 黑屏，换场景（莱恩斯实验室

    zhongyuan "【碎碎念】蹬脚残留血迹，可能是推搡撞到或者被人从背后袭击，用椅子砸死…这么深的伤，凶手看起来力气不小呢"

    pb "报告，前辈，屋里整洁，没有值钱物品失窃。门锁窗锁完好，可能是熟人作案。"

    zhongyuan "熟人啊…小苏，除了你。还有人有这房子的钥匙吗？"

    s "有。车佯子，也是老师的学生。"

    zhongyuan "博源，把车佯子叫来。尸体送去尸检。"

    pb "遵命，前辈！"

    menu:
        "苏千开门":
            jump game_main_one_b


        "警察开门":
            jump game_main_two_b


label game_main_one_b:
    cheyangzi "千学长,你没事吧？？"



label game_main_two_b:
