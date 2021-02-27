class transSyn():
    # 用於 英翻中 並刪除重覆, 故需要多個 '譯名'
    # 1st: 用於 英翻中 (無中文)
    # 2nd~: 用於 刪除重覆, 即直接將英文刪除.
    # 之後 還要用 typoSyn 將用詞統一
    Synonym = {
        # 品牌
        'bocconcini':   ['博康奇尼'],
        'havarti':      ['哈瓦蒂'],
        'havati':       ['哈瓦蒂'],
        'mascarpone':   ['馬斯卡彭', '馬斯卡朋'],
        'mozzarella':   ['莫札瑞拉'],
        'ricotta':      ['瑞可達起司'],
        'tabasco':      ['塔巴斯科'],
        'Ankang':       ['AK安康'],
        'special k':        ['家樂氏'],
        'specialk':         ['家樂氏'],
        'mozzarella cheese':['莫札瑞拉起司'],
        'mozzarellachease': ['莫札瑞拉起司'],
        # 食材
        # 'cream cheese': ['奶油乳酪'],
        'almond meal':  ['杏仁'],
        'almond':       ['杏仁'],
        'almond flour': ['杏仁粉'],
        'apple cider vinegar':  ['蘋果醋'],
        'apple vinegar':        ['蘋果醋'],
        'apple':        ['蘋果'],
        'arborio rice': ['阿柏里歐米'],
        'arborio':      ['阿柏里歐'],
        'avocado oil':  ['酪梨油'],
        'avocado':      ['酪梨'],
        'avocados':     ['酪梨'],
        'baking powder':['泡打粉'],
        'baking soda':  ['蘇打粉'],
        'bay leave':    ['月桂葉'],
        'beet':         ['甜菜'],
        'beetroot':     ['甜菜根'],
        'blue cheese':  ['藍莓芝士'],
        'broad beans':  ['蠶豆'],
        'cannellini bean':  ['白腰豆'],
        'cherrytomato': ['櫻桃茄'],
        'cooking spray':['烹飪噴霧'],
        'cheese':       ['起司', '起士'],
        'cottage':      ['茅屋芝士'],
        'couscous':     ['庫斯庫斯', '小米'],
        'creamcheese':  ['奶油乳酪', '忌廉起司', '忌廉芝士'],
        'cumin':        ['孜然'],
        'double espresso':  ['義式濃縮咖啡'],
        'egg':              ['雞蛋', '蛋'],
        'garbanzo bean':    ['鷹嘴豆'],
        'ghee':             ['酥油', '無水奶油'],
        'green apple':      ['青蘋果'],
        'green onions':     ['綠蔥'],
        'hersheys cocoa':   ['無糖純可可粉'],     # 去品牌名
        'hummus':       ['鷹嘴豆泥'],
        'ketchup':      ['番茄醬'],
        'lemon juice':  ['檸檬汁'],
        'lemon':        ['檸檬'],
        'mustard':  ['芥末'],
        'paprika':  ['甜椒粉', '紅甜椒粉', '煙燻紅椒粉'],
        'pasta':    ['義大利麵'],
        'persil':   ['巴西里', '巴西裏', '巴西裡'],
        'salsa sauce':  ['莎莎醬'],
        'salt':         ['鹽'],
        'sour cream':   ['酸奶油', '酸奶'],
        'sourcream':    ['酸奶油', '酸忌廉'],
        'stevia':       ['甜菊'],
        'sugar':        ['糖'],
        'tomato':       ['番茄'],
        'sweet marsala wine':   ['瑪薩拉酒', '甜馬沙拉酒'],
        'unsalted butter':  ['無鹽奶油'],
        'walnut':           ['核桃'],
        'whipping cream':   ['淡奶油'],
        'young coconut':    ['椰青'],
        'olive oil':        ['橄欖油'],
        'meat masala':      ['瑪撒拉香料'],
        'masala':           ['瑪撒拉'],
        'marsala wine':     ['馬沙拉酒'],
        'mazurella cheese': ['馬自瑞拉起司'],
        'zucchini':         ['櫛瓜', '翠玉瓜'],
        'boiled potato':    ['熟馬鈴薯', '熟薯'],
        'greek':            ['希臘'],
        'worcestershire':   ['伍斯特辣醬'],
        'water':    ['水'],
        'vinegar':  ['醋'],
        'sungold':  ['黃金'],
        'swedish shrimp':   ['瑞典蝦'],
        'seaweed':  ['海苔'],
        'applejuice':   ['蘋果果汁'],
        'black pepper': ['黑胡椒', '黑椒'],
        'blackpepper':  ['黑胡椒'],
        'orbalsamic':   ['or義大利香黑'],
        # '': [''],
        # '': [''],
        # '': [''],
        # '': [''],
    }

class typoSyn():
    # 注意1: 不會處理字尾空白. 意思是有時必需加空白才會拿掉
    typoDict = {
        '塔巴斯科辣椒醬': ['tabasco醬', 'tabasco辣醬', 'tabasco辣椒調味醬', 'tabasco'],
        '奶油乳酪': ['乳酪cream cheese', '乳脂cream cheese', '忌廉起司', '忌廉芝士', 'cream cheese'],
        '酸奶油': ['酸忌廉'],
        '異麥芽寡糖粉': ['vitafiber異麥芽寡糖粉'],
        '膳食纖維粉': ['vitafiber'],
        '牛番茄': ['大肉茄番茄'],
        '奶酪乾': ['jerky 起司'],
        '家樂氏原味香脆麥米片': ['家樂氏麥米片', '家樂氏原味米麥片', '家樂氏原味麥米片', '家樂氏香脆麥米片原味', '家樂氏香脆麥米片'],
        '義大利香黑醋': ["義大利黑醋", "balsamico", "香油酢(balsamic vinegar)", "balsamic 醋",
                "balsamico 葡萄酒醋", "義大利香黑醋", "巴薩米克黑醋", "義式香醋balsamic",
                "巴沙米可醋 balsamic vinegar", "balsamico紅酒醋", "黑醋 balsamic vinegar",
                "義式黑醋", "巴薩米可醋balsamic", "義式黑醋", "巴薩米克醋balsamic", 'balsamique',
                "黑醋balsamic", "balsamic醬", "紅酒醋(balsamic)", "balsamico(紅酒醋)",
                "義大利甜醋balsamicvinegar", 'balsamic vinegar'],
        '巴薩米克': ["巴薩米克(balsamico)", "巴沙米可", "巴沙米克", "巴沙米哥", "巴塞米",
                "巴撒米可", "巴撒米克", "巴薩米可", "巴薩米克", "巴薩米"],
        '香芹': ['香草 parsley', '香草 parsley', '歐芹', '歐芹parsley', '香芹parsley', '香菜parsley'],
        '莫札瑞拉':['馬扎瑞拉', '馬自瑞拉', '馬芝瑞拉', '馬茲瑞拉', '馬茲摩拉', '馬茲羅拉', '馬蘇里拉',
                '莫扎瑞拉', '莫左瑞拉', '莫札瑞拉', '莫札雷拉', '莫拉瑞拉', '莫茲瑞拉', '莫薩里拉',
                '瑪芝瑞拉', '瑪茲瑞拉'],
        '黃金奇異果': ['zespri sun gold奇異果'],
        '低卡可樂': ['zero 可樂'],
        '藜麥': ['quinoa藜米'],
        '帕馬森乾酪': ['Parmigiano起司'],
        'OmniPork ': ['omnipork'],
        'MyProtein ': ['myprotein ', 'myprotein'],
        # '低卡可樂': ['zero', '纖維可樂'],
        # '汽水': ['雪碧'],
        '起司': ['起士', '芝士'],
        '小卷': ['小捲'],
        '帆立貝': ['凡立貝'],
        '燻雞': ['燻g'],
        '春捲': ['春卷'],
        '綠捲': ['綠卷'],
        '蘿蔓': ['羅曼', '蘿曼'], 
        '蘿美': ['羅美', '美蘿心'],
        '芫荽': ['芫茜', '鹽須'],
        '番茄': ['蕃茄', '西紅柿'],
        '番荽': ['蕃荽', '胡妥', '胡荽'],
        # '梨子': ['雪梨'],
        # '檸檬': ['青寧', '台灣好田'],
        # '芒果': ['青芒'],
        # '草莓': ['士多啤梨'],
        # '柚子': ['文旦'],
        # '奇異果': ['猕猴桃'],
        '苜宿芽': ['暮宿芽', '目蓿芽'],
        '蔓越莓': ['蔓越梅', '蔓樾莓', '蔓岳莓'],
        '核桃': ['胡桃'],
        # '杏仁': ['南北杏', '南杏'],
        '葵花籽': ['葵花子'],
        '大麻籽': ['大麻子'],
        # '亞麻': ['胡麻'],
        '亞麻籽': ['亞麻子'],
        '奇亞籽': ['奇亞子', '奇芽籽', '奇芽子', '奇牙籽', '奇牙子'],
        '奧勒岡': ['奧利岡', '俄力岡'],
        # '穀片': ['穀物片'],
        '庫斯庫斯': ['庫司庫司'],
        '玉米': ['玉蜀黍'],
        '番薯': ['蕃薯', '甘薯', '甘藷', '地瓜', '沙葛'],
        '蒔蘿': ['洋茴香'],
        '車前': ['前車'],
        '芥末': ['芥苿'],
        '芥末籽': ['芥末子', '芥末仔'],
        '莎莎醬': ['salsa醬'],
        '馬斯卡彭': ['馬斯卡朋', '馬斯卡邦'],
        '凱撒': ['凱薩', '凱薩琳'],
        '鹽': ['塩', '盬', '塩巴', '鹽巴'],
        '煉乳': ['煉奶', '練奶', '炼奶'],
        '橄欖': ['橄榄', '橄㰖', '橄欄'],
        '薄菏': ['簿荷', '薄盒'],
        '藍莓': ['藍黴'],
        '煙燻': ['煙熏'],
        '荸薺': ['荸齊'],
        '蒟蒻': ['蒟篛'],
        '巴西里': ['巴西利', '巴西裏', '巴西裡'],
        '蘇打': ['梳打'],
        '花椰菜': ['西蘭花'],
        '香吉士': ['香桔士'],
        '蛤蜊': ['蛤蠣', '蛤利', '蛤仔'],
    }

    def __init__(self):
        self._lookup = {}
        for item, values in self.typoDict.items():
            # if '起司' == item:
            #     print('1')
            for val in values:
                self._lookup[val.lower()] = item
        self._lookup = sorted(self._lookup.items(), key=lambda x:len(x[0]), reverse=True)

    def replaceTypo(self, value):
        # if '焦糖乳清' in value:
        #     print('1')
        lowerV = value.lower()
        count = 0
        while True:
            for typo, key in self._lookup:
                if typo in lowerV:
                    lowerV = lowerV.replace(typo, key)
                    count += 1
            else:
                break
        if count > 0:
            return lowerV
        return value

class groupSyn():
    # 別名 或 同一類食材
    Synonym = [
        "蔘鬚",
        "黃耆",
        "熟地",
        "甘草",
        "枸杞",

        "伏特加",
        "白蘭地",
        "威士忌",
        "低卡可樂",
        "可樂",
        "汽水",
       ["優格"],
        "養樂多",
        "冰淇淋",
       ["黃布丁", "布丁"],

        "海鮮",
        "小卷",
        "軟絲",
        "牡蠣",
        "干貝",
        "扇貝",
        "昆布",
        "明太子",
        "火鍋料",
       ["魚翅", "北海翅"],
       ["鮭魚", "鱒澳鱸"],
       ["鰻魚", "蒲燒鰻"],

       ["小卷", "小管", "鎖管", "中卷", "透抽"],
       ["牡蠣", "蚵仔", "生蠔", "蠔"],
       ["干貝", "瑤柱", "帶子粒"],
       ["鮮貝", "帶子", "沙插", "騷蛤"],
       ["扇貝", "凡立貝", "帆立貝"],
        "漢堡排",
        "排骨",
        "叉燒",
       ["豬肉", "火鍋片"],
       ["雞胸肉", "金豐盛", "燻雞"],
        "雞蛋",
       ["高蛋白", "protein"],
       ["羊肉", "羊排"],
        "肉乾",

       ["麵", "雁门清高黑苦荞全麦龙须面"],
       ["麵包", "漢堡包", "軟法", "餐包", "銀絲卷", "三文治方", "新英格蘭堡", "義美馬芬堡", "馬芬堡", "義美馬芬"],
        "饅頭",

       ["麵皮", "餛飩皮"],
       ["春捲皮"],
       ["塔皮", "派皮"],

       ["乾酪", "帕馬森"],
       ["乳酪", "起司", "瑞可達", "博康奇尼", "莫札瑞拉", "馬斯卡彭", "布拉塔", "哈瓦蒂"],
       ["無鹽奶油", "忌廉", "動鮮"],
       ["鮮奶油"],
       ["淡奶油"],
       ["低脂起司", "低脂莫札瑞拉"],
       ["奶油"],
       ['酥油', '無水奶油'],

       ["餅乾", "OREO", "洋芋片", "樂事原味波卡", "浪味仙", "奇多"],
       ["巧克力", "Hersheys", "COCO"],

       ["蔬菜", "綠橡木葉", "時蔬", "冰山綠火焰", "韭黃", "青花苔", "大陸妹", "花椰菜", "過貓"],
        "綠卷",
        "豆芽菜",
        "九層塔",
        "胡蘿蔔",
       ["蘿蔓", "蘿美"],
        "羅望子",
       ["豆芽菜", "銀芽"],
       ["九層塔", "蘿勒"],
       ["胡蘿蔔", "紅蘿絲", "紅蘿蔔", "甘荀"],

       ["香菜", "芫荽"],
       ["洋香菜", "番荽"],

       ["大番茄", "牛番茄"],
       ["小番茄", "車厘茄", "聖女番茄", "櫻桃茄"],
        "蘋果",
       ["鳳梨", "蘿菠"],
        "草莓",
        "梨子",
        "榴槤",
        "檸檬",
        "櫻桃",
        "波羅蜜",
        "芒果",
        "李子",
        "柚子",
        "桑葚",
        "石榴",
        "奇異果",
        "酪梨",
        "栗子",
        "蔓越梅",

       ["果乾", "蔓越梅乾"],
       ["梅子", "烏梅", "梅乾"],

        "堅果",
        "葵花籽",
        "核桃",
        "杏仁",
        "大麻籽",
        "亞麻籽",
        "奇亞籽",
       ["麥片", "穀片"],

       ['小米', '庫斯庫斯'],
        "玉米",
        "甘薯",
        "荸薺",
        "菱角",
        "蓮藕",
        "蓮子",
        "芋頭",
        "天貝",
        "千張",
        "洋芋",
       ["蒟蒻絲", "魔芋面", "魔芋麵", "芋絲", "蒟蒻", "寒天"],
       ["辣木", "青汁"],
       ["洋芋", "馬鈴薯"],
       ["白木耳", "銀耳", "雪耳"],

        "鷹嘴豆",
        "蠶豆",

        "蒔蘿",
       ["食用花", "花片", "茉莉", "鼠尾草"],
        "甜菊",
        "梔子花",
        "香蜂草", 
        "斑蘭",
        "薄菏",
        "番紅花",
       ["香莢蘭", "雲呢拿"],

       ["發粉", "泡打粉"],
        "尾冬骨",
       ["明膠", "洋菜", "吉利丁", "果凍粉", "膠粉"],
       ["木耳", "銀耳"],
        "松茸",
        "松露",
        "玉子燒",
        "紅珊瑚",
       ["發泡錠","維他命C"],
        "腐皮",

        "奧勒岡",
       ["車前子", "洋車前"],
       ["香料", "葛縷子", "葫蘆巴", "香莢蘭"],
       ["孜然", "小茴香"],
        "茴香",
        "香茅",
        "紫蘇",
        "月桂",
        "八角", 
        "蒔蘿",
        "丁香",
        "卡菲萊姆葉",

        "山葵",
        "辣根",

       ["美乃滋", "KEPIE"],
        "莎莎醬",

       ["調味料", "滷汁包", "風味料", "鮮味炒手", "自然鮮", "滷包"],
       ["高湯塊", "麻辣鍋底"],
       ["味精", "味素"],
       ["醋", "巴薩米克醋", "義大利香黑醋"],
       ["醬料", "老乾媽"],
       ["醬油", "滷汁"],
       ["山葵", "綠芥末", "wasabi", "哇沙米"],
        "蔭豉",
        "破布子",
        "龍眼蜜",
        ]

    def __init__(self):
        self.dict = {}
        # dicN = {}
        for item in self.Synonym:
            if isinstance(item, list):
                self.dict[item[0]] = item[:]
                ## Todo: 字串長的先作, 再作短字串
                # for i in item:
                #     ilen = str(len(i)).zfill(2)
                #     if not ilen in dicN:
                #         dicN[ilen]=[[i,item[0]]]
                #     else:
                #         dicN[ilen].append([i,item[0]])
            else:
                self.dict[item] = [item]
        # self.dicN = [dicN[i] for i in keys()]


    def lookup(self, item, values):
        for sym in values:
            if sym == item:
                return True, False
            elif sym in item:
                return True, True
        else:
            return False, False
    
    def lookups(self, item, item_norm):
        for key, values in self.dict.items():
            bFind, bAppend = self.lookup(item_norm, values)
            if bFind:
                if bAppend or item_norm != item:
                    self.dict[key].append(item)
                # if item_norm != item:
                #     print('1')
                break
        else:
            print('NG', item)
