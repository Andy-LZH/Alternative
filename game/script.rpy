# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define s = Character("苏千", color = "25A1DF")
define gui.text_font = "FZSJ-DQYBKSJW.TTF"

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。
    "刚醒来"
    image sOriginal = "suqian.png"
    image sFit = im.FactorScale("suqian.png", 0.28)
    show sFit at left

    s "啧，该死（头好痛，现在什么时间）诶 为什么我头上有绷带"

    s "看了看表十点？！！|猛然从床上坐起| 为什么没有人来喊我？"

    s "呵，这家伙一做实验就忘记喊我……"

    s "伸了个懒腰，一边打哈欠一边往前走 莱恩斯老师你又不喊我，老是迟到，我是很不好意思哒～～～"
    # 黑黑屏，换场景（莱恩斯实验室

    s "莱恩斯老......!!!!"
    # Made the first choice
    menu:
        "赶紧报警":
            jump gameMainOne

        "不报警":
            jump firstConsequence



label firstConsequence:
    "【警察 is watching you】你为什么不信任我们警察，缺少人与人之间信任的你，摸着你的良心回到开头再来一次"
    jump start
label gameMainOne:

    # 此处为游戏结尾。

    return
