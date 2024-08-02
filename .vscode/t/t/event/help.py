import pprint as p
def rise_help(error=None):
    "if command not in app return rise_help"
    var:str="""
    {}
    ------------------------
    add            add file or folder in src app
    config         configriution add and remove
    get            get file or porject from app 
    init           add inition .src in dirctory
    set            set file or folder in app if item in app
    ========================================================
    plise run command [ src help ] show all commands
    
    ....!
    exmpel
    src <? ['add' 'config' 'get' 'init' 'set' > [ -a , -c  -g -i -s ]
    
    
  
    """.format(error)
    print(var)

