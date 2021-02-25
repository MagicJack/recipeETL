import re
from typoSyn import *

class ingCleaner():
    _typoDict = typoSyn()
    _chiNum1 = [
        "（","［","﹝","【","「","＜","〈","《","『",
        "）","］","】","」","＞","〉","》","』","／",
        "％","’","　","＊","*","•","◆","￼",
        ":", "；", ",", "，" ]
    _chiNum2 = [
        "(", "[", "[", "[", "[", "[", "[", "[", "[",
        ")", "]", "]", "]", "]", "]", "]", "]", "/",
        "%", "'", " ",  "",  "",  "",  "", "",
        "：", "：", "、", "、" ]

    # (...)?xxx(...)
    _rgx1 = re.compile(r'([(\[].*?[)\]])?\s*(.+?)\s*([(\[].*?[)\]])')
    # (...)xxx(...)?
    _rgx2 = re.compile(r'([(\[].*?[)\]])\s*(.+)\s*([(\[].*?[)\]])?')
    # Clean 'xx(~', '~)xx'
    _rgx3 = re.compile(r'^((?:7|7-|7-ELEVEN)11|7-ELEVEN)\s?', re.I)
    _rgx4 = re.compile(r'(.+[：︰～]|[a-j1-9][.:\-])\s*(.+)', re.I)
    _rgx5 = re.compile(r'(.+)\s*\(.*')
    _rgx6 = re.compile(r'.+\)\s*(.+)')

    def cleanIng(self, id, vstr, bVerb=False):
        def _parseChiNum(ch):
            if ch in self._chiNum1:
                return self._chiNum2[self._chiNum1.index(ch)]
            return ch

        def _doRegex(rgx, vstr, bVerb=False):
            mat = re.match(rgx, vstr)
            if mat:
                if bVerb: print(f"{id:>8}, {mat.groups()}")
            return mat

        def _cleanIng2(vstr):
            # 處理符號含全型半型...
            vstr = "".join([_parseChiNum(ch) for ch in vstr])

            # 處理有 () 的
            mat = _doRegex(self._rgx1, vstr, bVerb)
            if mat: return mat.group(2)
            mat = _doRegex(self._rgx2, vstr, bVerb)
            if mat: return mat.group(2)

            return vstr

        def _cleanIng3(vstr):
            # 處理 奇奇怪怪 的
            vstr = re.sub(self._rgx3, '[7-11] ', vstr)
            vstr = re.sub(r'^(.) {1,3}(.)$', r'\1\2', vstr)

            mat = _doRegex(self._rgx4, vstr, bVerb)
            if mat: return mat.group(2)
            mat = _doRegex(self._rgx5, vstr, bVerb)
            if mat: return mat.group(1)
            mat = _doRegex(self._rgx6, vstr, bVerb)
            if mat: return mat.group(1)

            return vstr

        vstr = _cleanIng2(vstr)
        vstr = _cleanIng3(vstr)
        return  self._typoDict.replaceTypo(vstr.strip())


    skipA = 0
    skipB = 0
    def checkSkip(self, id, food, qty, bVerb=False):
        if not "、" in food:
            return False
        # if "、" in qty:
        if "少許" in qty:
            if bVerb: print(f"{id:>8}, {food}, {qty}")
            self.skipA += 1
            return True
        elif "適量" in qty:
            if bVerb: print(f"{id:>8}, {food}, {qty}")
            self.skipB += 1
            return True
        return False

    def getSkip(self):
        return self.skipA, self.skipB
