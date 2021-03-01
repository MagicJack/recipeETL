import re

class qtyCleaner:

    def parseNumber(self, vstr):
        if vstr is None:
            return 1
        try:
            vstr = re.sub(r'(,|\n)', '', vstr)
            if '.' in vstr:
                return int(float(vstr)*10000)
            elif vstr == '':
                return 0
            else:
                return int(vstr)
        except Exception as e:
            print('error:', e)
            return 0


    _chiNum1 = [ "零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
    _chiNum2 = [ "０", "１", "２", "３", "４", "５", "６", "７", "８", "９" ]

    def _cvtNumChar(self, ch):
        if ch in self._chiNum1:
            return str(self._chiNum1.index(ch))
        if ch in self._chiNum2:
            return str(self._chiNum2.index(ch))
        return ch

    def _cvtNumStr(self, qtyStr):
        qtyStr = "".join([self._cvtNumChar(ch) for ch in qtyStr])
        if qtyStr[0]=='兩':
            qtyStr = '2'+qtyStr[1:]
        if qtyStr[0]=='約':
            qtyStr = qtyStr[1:]

        qtyStr = qtyStr.replace('¼', '0.25')
        qtyStr = qtyStr.replace('½', '0.5')
        qtyStr = qtyStr.replace('¾', '0.75')
        return qtyStr

    _rgx1 = re.compile(r'((?:[0-9]+\+)?[0-9]+[/.~\-+]?[0-9]*)\s*')
    def _splitUnit(self, qstr):
        au = self._rgx1.split(qstr)
        # au = re.split(r'((?:[0-9]+\+)?[0-9]+[/.~\-]?[0-9]*) *', qstr)
        if len(au) == 3:
            if '/' in au[1]:
                return [eval(au[1]), au[2]]
            elif '.' in au[1]:
                return [float(au[1]), au[2]]
            elif '-' in au[1] or '~' in au[1]:
                vals = re.split(r'[\-~]', au[1])
                return [eval(f'({vals[0]}0+{vals[1]}0)/20'), au[2]]
            elif '+' in au[1]:
                vals = re.split(r'\+', au[1])
                return [eval(f'{vals[0]}+{vals[1]}'), au[2]]
            else:
                return [int(au[1]), au[2]]
        elif qstr[0] == '半':
            return [0.5, qstr[1:]]
        else:
            return qstr


    def _replaceUnit(self, au):
        if isinstance(au, list):
            if au[1] in ['CC', 'cc', 'c.c', 'c.c.','C.C', 'mL', '毫升']:
                au[1] = 'ml'
            if au[1] in ['G', '克', '公克']:
                au[1] = 'g'
            if au[1] in ['大湯匙', '湯匙', '汤匙', '大匙', '甲匙', 'tbs', 'Tbs', 'tbsp', 'Tbsp', 'EL']:
                if not isinstance(au[0], str):
                    return [au[0]*15, 'g']
                else:
                    return au
            elif au[1] in ['小湯匙', '茶匙', '小匙', '丙匙', '匙', '茶匙tsp', 'TL']:
                if not isinstance(au[0], str):
                    return [au[0]*5, 'g']
                else:
                    return au
            elif au[1] in ['茶杯', '杯']:
                if not isinstance(au[0], str):
                    return [au[0]*240, 'ml']
                else:
                    return au
            elif au[1] in ['台兩', '兩']:
                if not isinstance(au[0], str):
                    return [au[0]*37.5, 'g']
                else:
                    return au
            return au
        else:
            return au


    # Class Method
    def clean(self, id, qtyStr, bVerb=False):
        # key: ingredent, value: qty. + unit string
        if bVerb: print(f'{id:>8}: {qtyStr} -> ', end='')
        if len(qtyStr) == 0:    return qtyStr
        qtyStr = self._cvtNumStr(qtyStr)
        qtyStr = qtyStr.replace('又', '+')
        qtyStr = qtyStr.replace('～', '~')
        qtyStr = qtyStr.replace('—', '-')
        qtyStr = qtyStr.replace('－', '-')
        qtyStr = qtyStr.replace(' - ', '-')
        qtyStr = qtyStr.replace(' ~ ', '~')
        if '分之' in qtyStr:
            qtyStr = re.sub(r'([0-9]+)分之([0-9]+) *', r'\2/\1', qtyStr)

        # if qtyStr == '1+1粒':
        #     print('1')
        try:
            qty_unit = self._replaceUnit(self._splitUnit(qtyStr))
        except Exception as er:
            qty_unit = qtyStr
            print(f'{id:>8}: qty-unit parse error.')
        if bVerb: print(f'{qty_unit}')
        return qty_unit

