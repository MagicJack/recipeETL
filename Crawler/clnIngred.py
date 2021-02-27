import re
from typoSyn import *

class ingCleaner():
    def __init__(self):
        pass

    _typoDict = typoSyn()
    _transDict = transSyn()

    _cnChar = list("仼优兰刴发咸国圣块坚塩头姜嫰岛庄徳择掦无柠榄殻温湿炼猕现瑶盐筛籮类緑红绿苹荀荞葱蓝蔴蕯虾记调辢过选酱针铃铝铺锦门韮须饺马鱼鲍鲜鳯鸡麦黄黒龙⽔")
    # 你 should change '姜'->'薑', '籮'->'蘿', '荀'->'筍' manually, and add '⽔'->'水' manually, if run convertZ.exe to generate twChar
    _twChar = list("任優蘭剁發鹹國聖塊堅鹽頭薑嫩島莊德擇揚無檸欖殼溫濕煉獼現瑤鹽篩蘿類綠紅綠蘋筍蕎蔥藍麻薩蝦記調辣過選醬針鈴鋁鋪錦門韭須餃馬魚鮑鮮鳳雞麥黃黑龍水")

    _cn2twWord = {
        '豆乾': '豆干',
        '魚乾': '魚干',
        '梅乾': '梅干',
        '菜乾': '菜干',
        '肉乾': '肉干',
        '乾果': '干果',
        '干貝': '乾貝',
        '葡萄乾': '葡萄干',
        '芥末': '芥苿',
        '豆豉': '豆鼓',
        '伍斯特辣醬': '喼汁',
        '豬鍵子': '豬𦟌肉',
        '牛鍵': '牛𦟌肉',
        '豬鍵': '豬𦟌',
        '牛鍵': '牛𦟌',
        # '伊籐': '伊藤',
        '蘿蔔': '萝卜',
        '菠蘿': '菠萝',
        '麵粉': '面粉',
        '麵包': '面包',
        '龍鬚麵': '龍須面',
        }

    _ChiSym1 = [
        '（','［','〔','﹝','【','「','＜','〈','《','『',
        '）','］','〕','﹞','】','」','＞','〉','》','』',
        '／','％','’','　','＊','*','•','◆','￼',
        ':', '；', ',', '，' ]
    _ChiSym2 = [
        '(', '[', '[', '[', '[', '[', '[', '[', '[', '[',
        ')', ']', ']', ']', ']', ']', ']', ']', ']', ']',
        '/', '%', "'", ' ',  '',  '',  '',  '', '',
        '：', '：', '、', '、' ]

    # 可以直接刪掉名字的品牌
    _brandList = [
        'bodykey',
        'bragg',
        # "mozzarella",
        'iherb',
        'costco',
        'classico',
        'pb2',
        'myprotein',
        'sweet relish',
        'granola',
        'zespri',
        'spark shake',
        'sparkshake',
        'real salt',
        's&b',
        's&b ',
        'redlentil',
    ]

    # (...)?xxx(...)
    _rgx1 = re.compile(r'([(\[].*?[)\]])?\s*(.+?)\s*([(\[].*?[)\]])')
    # (...)xxx(...)?
    _rgx2 = re.compile(r'([(\[].*?[)\]])\s*(.+)\s*([(\[].*?[)\]])?')
    # Clean 'xx(~', '~)xx'
    _rgx3 = re.compile(r'^((?:7|7-|7-ELEVEN)11|7-ELEVEN)\s?', re.I)
    _rgx4 = re.compile(r'(.+[：︰～]|[a-j1-9][.:\-])\s*(.+)', re.I)
    _rgx5 = re.compile(r'(.+)\s*\(.*')
    _rgx6 = re.compile(r'.+\)\s*(.+)')
    _rgx7 = re.compile(r'([\u3001\u4e00-\u9fa5\uFF01-\uFF5E]+)')
    # _rgx8 = re.compile(r'\(?([a-z][a-z& ]+)\)', re.I)
    _rgx8 = re.compile(r'([a-z][a-z2& ]+)', re.I)
    # _rgx9 = re.compile(r'\(?\s*([a-z][a-z2& ]+)(?:購|網購入|已醃好的)?\)?', re.I)
    _rgx9 = re.compile(r'\((?:[\u4e00-\u9fa5]*)?\s*([a-z][a-z2& ]+)(?:[\u4e00-\u9fa5]*)?\)', re.I)


    # Class Method
    def cleanIng(self, id, vstr, bVerb=False, nClean=4):

        def _parseCnChar(ch):
            if ch in self._cnChar:
                return self._twChar[self._cnChar.index(ch)]
            return ch

        def _parseCnWord(line):
            line = "".join([_parseCnChar(ch) for ch in line]).strip()
            for twW, cnW in self._cn2twWord.items():
                if cnW in line:
                    line = line.replace(cnW, twW)
                    break
            # Run twice in case there're 2 cnWords
            for twW, cnW in self._cn2twWord.items():
                if cnW in line:
                    line = line.replace(cnW, twW)
                    break
            return line


        def _parseChiSym(ch):
            if ch in self._ChiSym1:
                return self._ChiSym2[self._ChiSym1.index(ch)]
            return ch

        def _replaceMore(idx, rstr, vstr):
            # if vstr.find(word) > vstr.find('(') > 0 :
            if idx > vstr.find('(') > 0:
                return self._rgx9.sub(rstr, vstr)
            else:
                return self._rgx8.sub(rstr, vstr)

        def _transEngChi(vstr):
            if '牛番茄or大番茄tomato' in vstr:
                print('1')
            s = 0
            idx = 0
            while True:
                mat = self._rgx8.search(vstr[s:])
                if not mat:     break

                s += mat.end(0)
                word = mat.group(1).strip().lower()
                # if '牛番茄or大番茄tomato' in vstr:
                #     print('1')
                idx += mat.start(0)
                if word in self._brandList:
                    # return self._rgx9.sub('', vstr)
                    return _replaceMore(idx, '', vstr)
                if word in self._transDict.Synonym:
                    trans = self._transDict.Synonym[word]
                    for tran in trans:
                        if tran in vstr:
                            return _replaceMore(idx, '', vstr)
                    else:
                        # return self._rgx9.sub(trans[0], vstr)
                        return _replaceMore(idx, trans[0], vstr)
                # return vstr
                # words = self._rgx8.split(vstr)
                
                # vstr = " ".join(words[:-1])
                # print(f'{id:>8}, {vstr}')
            return vstr
        # if ' ' not in vstr:
        #     # [1:-1] are used to avoid spaces @ Start and End
        #     vstr = " ".join(re.split(self._rgx7, vstr)[1:-1])


        # Regex executer with log flag
        def _doRegex(rgx, vstr, bVerb=False):
            mat = rgx.match(vstr)
            if mat:
                if bVerb: print(f"{id:>8}, {mat.groups()}")
            return mat


        ## 處理程序
        # Part0: 簡中 --> 繁中
        def _cleanIng0(vstr):
            # 處理符號含全型半型...
            vstr = "".join([_parseChiSym(ch) for ch in vstr]).strip()
            vstr = _parseCnWord(vstr)
            # 英轉中, 刪 食材字串 裡的重覆
            vstr = _transEngChi(vstr)
            return vstr

        # Part1: 處理有 () 的
        def _cleanIng1(vstr):
            mat = _doRegex(self._rgx1, vstr, bVerb)
            if mat: return mat.group(2)
            mat = _doRegex(self._rgx2, vstr, bVerb)
            if mat: return mat.group(2)

            return vstr

        # Part2: 處理 奇奇怪怪 的
        def _cleanIng2(vstr):
            vstr = self._rgx3.sub('[7-11] ', vstr)
            vstr = re.sub(r'^(.) {1,3}(.)$', r'\1\2', vstr)

            mat = _doRegex(self._rgx4, vstr, bVerb)
            if mat: return mat.group(2)
            mat = _doRegex(self._rgx5, vstr, bVerb)
            if mat: return mat.group(1)
            mat = _doRegex(self._rgx6, vstr, bVerb)
            if mat: return mat.group(1)

            return vstr


        # 處理符號含全型半型, 簡中 --> 繁中...
        nClean -= 1
        if nClean < 0:      return vstr
        vstr = _cleanIng0(vstr)
        # Part1: 處理有 () 的
        nClean -= 1
        if nClean < 0:      return vstr
        vstr = _cleanIng1(vstr)
        # Part2: 處理 奇奇怪怪 的
        nClean -= 1
        if nClean < 0:      return vstr
        vstr = _cleanIng2(vstr)
        # 錯別字合併 類似 食材字串
        nClean -= 1
        if nClean < 0:      return vstr
        return self._typoDict.replaceTypo(vstr.strip())


    # Class Method
    _skipA = 0
    _skipB = 0
    def checkSkip(self, id, food, qty, bVerb=False):
        if not "、" in food:
            return False
        # if "、" in qty:
        if "少許" in qty:
            if bVerb: print(f"{id:>8}, {food}, {qty}")
            self._skipA += 1
            return True
        elif "適量" in qty:
            if bVerb: print(f"{id:>8}, {food}, {qty}")
            self._skipB += 1
            return True
        return False

    # Class Method
    def getSkip(self):
        return self._skipA, self._skipB
