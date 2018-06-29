import wx

class  Ventana_Ejemplo(wx.Frame):
    def __init__(self,parent,title):
        super(Ventana_Ejemplo,self).__init__(parent,title="segunda ventana",size=(200,200))
       # self.SetPosition((10,10))
        self.Show(True)
        
#modularizando el codigo
if __name__== '__main__':
    app=wx.App()
    Ventana_Ejemplo(None,title='nueva ventana Hola Andy')
    app.MainLoop()


#creacion de objeto
#estilo=style
#frame=wx.Frame(None,-1,'Primer ventana',style=wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX)#contenedor padre none aaasigna un id -1
#frame=wx.Frame(None,-1,'Primer ventana',size=(400,400))
#frame.Show()

#app.MainLoop()#crea un ciclo infinito:acceder a algunos elementos
