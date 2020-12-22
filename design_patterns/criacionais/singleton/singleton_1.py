def singleton(clasz):
    instances = {}

    def get_class(*args,**kwargs):
        if clasz not in instances:
            instances[clasz] = clasz(*args,**kwargs)
        return instances[clasz]
    
    return get_class    


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == '__main__':
   as1 = AppSettings()
   as1.tema = 'O tema claro'
   print(as1.tema)

   as2 = AppSettings()
   print(as1.tema)



