import maya.cmds as mc

class AnimeCheck:
        def __init__(self):
            self.sel = ''
        
        def CreateCam(self,*args):
            axischeck = mc.radioButtonGrp('axis', q=True, sl=True)
            transcheck = mc.intSliderGrp('trans', q=True, v=True)
            parentcheck = mc.radioButtonGrp('parent', q=True, sl=True)
            
            if parentcheck == 0 or axischeck == 0:
                print('ERROR : Please select one of the buttons.')
                sys.exit()
            if self.sel == "":
                print('ERROR : Not Select target object.')
                sys.exit()
            cam = mc.camera(n='AnimeCheckCam')
            mc.matchTransform(cam,self.sel[0], pos=True)
            getx = mc.getAttr(cam,'.tx')
            gety = mc.getAttr(cam,'.ty')
            getz = mc.getAttr(cam,'.tz')
            if axischeck == 1:
                rotax = 0
                rotay = 90
                getx = getx + transcheck
            elif axischeck == 2:
                rotax = -90
                rotay = 0
                gety = gety + transcheck
            else:
                rotax = 0
                rotay = 0
                getz = getz + transcheck
            mc.select(cam)    
            mc.move(getx,gety,getz)
            mc.rotate(rotax,rotay,0)
            if parentcheck == 1:
                mc.parentConstraint(self.sel[0],cam[0], mo=True)
            else:
                mc.pointConstraint(self.sel[0],cam[0], mo=True)
            
        
        def SelectButton(self,*args):
            mc.select(mc.ls(sl=True,dag=True,typ='transform'))
            self.sel = mc.ls(sl=True)
        
        def MainMenu(self,*args):
            mc.window(t='AnimeCheckCamera',w=500)
            mc.columnLayout(adj=True)
            mc.radioButtonGrp('axis', l='Axis', la3=['X','Y','Z'], nrb=3)
            mc.intSliderGrp('trans', l='Distance to target', min=0, max=100, f=True)
            mc.radioButtonGrp('parent', l='Parent Type', la2=['Parent','Point'], nrb=2)
            mc.button(l='Select target object',c=self.SelectButton)
            mc.button(l='Create',c=self.CreateCam)
            mc.showWindow()       
                                  

a = AnimeCheck()
a.MainMenu()            