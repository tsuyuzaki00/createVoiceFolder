import os

class Fatulox():
    def __init__(self):
        self._seex_list=["r","k","g","s","z","t","d","f","b","n","m","p"]
        self._seboex_list=["y","w"]
        self._boex_list=["e","c","a","o","u"]
        self._hceex_list=["x"]
        self._taxox_list=["-","+","=","!"]
        self._tyouox_list=["--","++","==","!!","-+","-=","-!","+-","+=","+!","=-","=+","=!","!-","!+","!="]
        self._userName="user"

    #Single Function
    def kctugouox_create_list(self,prefix_list,suffix_list):
        kctugouTaxgo_list=[]
        for prefix in prefix_list:
            for suffix in suffix_list:
                kctugouTaxgo_list.append(prefix+suffix)
        return kctugouTaxgo_list
    
    #Private Function
    def _hceex_create_list(self):
        hceexTaxox_list=self.kctugouox_create_list(self._hceex_list,self._taxox_list)
        hceexTyouox_list=self.kctugouox_create_list(self._hceex_list,self._tyouox_list)
        hceex_list=hceexTaxox_list+hceexTyouox_list
        return hceex_list
    
    def _boex_create_list(self,getBoex="e"):
        taxox_list=self.kctugouox_create_list([getBoex],self._taxox_list)

        fkgouox_list=[]
        bohceex_list=self._boex_list+self._hceex_list

        for bohceex in bohceex_list:
            kctgouox_list=self.kctugouox_create_list([getBoex],bohceex)
            fkgouox_list=fkgouox_list+kctgouox_list
        eTyouox_list=self.kctugouox_create_list(fkgouox_list,self._tyouox_list)

        boex_list=taxox_list+eTyouox_list
        return boex_list

    def _seex_create_list(self):
        fkgouox_list=[]
        for _seboex in self._seboex_list:
            kctgouox_list=self.kctugouox_create_list(self._seex_list,_seboex)
            fkgouox_list=fkgouox_list+kctgouox_list

        seex_list=self._seboex_list+self._seex_list+fkgouox_list
        return seex_list

    def _folder_create_dicts(self):
        folder_dicts=[]

        _hceex_list=self._hceex_create_list()
        _hceex_dict={"x":_hceex_list}
        folder_dicts.append(_hceex_dict)

        for _boex in self._boex_list:
            boex_list=self._boex_create_list(getBoex=_boex)
            boex_dict={_boex:boex_list}
            folder_dicts.append(boex_dict)
        
        seex_list=self._seex_create_list()
        for seex in seex_list:
            for _boex in self._boex_list:
                boex_list=self._boex_create_list(getBoex=_boex)
                fkgou_list=self.kctugouox_create_list(seex,boex_list)
                seex_dict={seex+_boex:fkgou_list}
                folder_dicts.append(seex_dict)
        return folder_dicts

    def _folder_create_func(self,folder_dicts,userName="user"):
        keyCount=0
        valueCount=0
        userFolder=os.path.join(os.path.dirname(__file__),userName)
        for folder_dict in folder_dicts:
            for key, values in folder_dict.items():
                for value in values:
                    oto_folder=os.path.join(userFolder,str(keyCount).zfill(3)+"_"+key,str(valueCount).zfill(5)+"_"+value)
                    os.makedirs(oto_folder,exist_ok=True)
                    valueCount=valueCount+1
                keyCount=keyCount+1

    #Summary Function
    #Setting Function
    def setUserName(self,variable):
        self._userName=variable
        return self._userName
    def getUserName(self):
        return self._userName
    
    #Public Function
    def createFolder(self):
        folder_dicts=self._folder_create_dicts()
        self._folder_create_func(folder_dicts,userName=self._userName)

def main():
    oto=Fatulox()
    oto.setUserName("suzuki")
    oto.createFolder()

main()
