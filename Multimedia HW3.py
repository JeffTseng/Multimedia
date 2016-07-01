import PIL.Image
import os
from Tkinter import *
import tkFileDialog 
import math
from scipy.fftpack import dct

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a
def lcm(a,b):
    return a * b /gcd(a, b) 
def manhattan (a,b):
    sum1=0
    for i in xrange(len(a)):
        sum1=sum1+abs(a[i]-b[i])
    return sum1
def manhattan1 (a,b):
    c=[]
    for i in xrange(len(a)):
        sum1=0
        for j in xrange(len(a[i])-1):
            sum1+=abs(a[i][j]-b[j])
        c.append([sum1,a[i][j+1]])
    return c
def image_open(filename):
    a=PIL.Image.open(filename)
    pixel=a.load()
    width, height = a.size
    return a,pixel,width, height

def image_save(param,result):
    param.save(result)
    
def image_show(filename):    
    a=PIL.Image.open(filename)
    a.show()

def average(IMAGE_NOW_FILENAME,grid):
    img,pixel,width, height=image_open(IMAGE_NOW_FILENAME)
    his=[]
    width1=lcm(width,grid)
    height1=lcm(height,grid)
    img=img.resize((width1,height1),PIL.Image.BILINEAR)
    pixel=img.load()
    for n in os.listdir(os.curdir+'/'+'dataset'):
        if(n.find(".jpg")!=-1):
            little = PIL.Image.open(os.curdir+'/'+'dataset'+'/'+n)
            little = little.resize( (width1/grid, height1/grid), PIL.Image.BILINEAR)
            d,e=little.size
            pixel1=little.load()
            sum1=0
            sum2=0
            sum3=0
            for i in xrange(d):
                for j in xrange(e):
                    f=list(pixel1[i,j])
                    sum1+=f[0]
                    sum2+=f[1]
                    sum3+=f[2]
            his.append([sum1/(d*e),sum2/(d*e),sum3/(d*e)])
    for i in range(0,width1,width1/grid):
        for j in range(0,height1,height1/grid):
            result=[]
            cropped_example = img.crop((i, j, i+width1/grid,j+height1/grid))
            pixel3=cropped_example.load()
            w,h=cropped_example.size
            total1=0
            total2=0
            total3=0
            for q in xrange(w):
                for s in xrange(h):
                    f=list(pixel3[q,s])
                    total1+=f[0]
                    total2+=f[1]
                    total3+=f[2]
            hist=[total1/(w*e),total2/(d*e),total3/(d*e)]
            for x in xrange(len(his)):
                result.append([manhattan(hist,his[x]),x])
            result=sorted(result)
            for n in os.listdir(os.curdir+'/'+'dataset'):
                if(n.find(".jpg")!=-1):
                    a=n.find('0')
                    b=n.find('.')
                    c=n[a:b]
                    if(int(c)==result[0][1]):
                        new = PIL.Image.open(os.curdir+'/'+'dataset'+'/'+n)
                        new=new.resize( (width1/grid, height1/grid), PIL.Image.BILINEAR )
                        pixel2=new.load()
                        break
            for x in range(0,width1/grid,1):
                for y in range(0,height1/grid,1):
                    a=list(pixel[x,y])
                    b=list(pixel2[x,y])
                    a=b
                    pixel[i+x,j+y]=tuple(a)
    img=img.resize((width,height),PIL.Image.BILINEAR)
    image_save(img,"Q1.jpg")
    
def histogram(IMAGE_NOW_FILENAME,grid):
    img,pixel,width, height=image_open(IMAGE_NOW_FILENAME)
    his=[]
    width1=lcm(width,grid)
    height1=lcm(height,grid)
    img=img.resize((width1,height1),PIL.Image.BILINEAR)
    pixel=img.load()
    for n in os.listdir(os.curdir+'/'+'dataset'):
        if(n.find(".jpg")!=-1):
            little = PIL.Image.open(os.curdir+'/'+'dataset'+'/'+n)
            little = little.resize( (width1/grid, height1/grid), PIL.Image.BILINEAR)
            com = little.histogram()
            his.append(com)
    for i in range(0,width1,width1/grid):
        for j in range(0,height1,height1/grid):
            result=[]
            cropped_example = img.crop((i, j, i+width1/grid,j+height1/grid))
            for x in xrange(len(his)):
                result.append([manhattan(cropped_example.histogram(),his[x]),x])
            result=sorted(result)
            for n in os.listdir(os.curdir+'/'+'dataset'):
                if(n.find(".jpg")!=-1):
                    a=n.find('0')
                    b=n.find('.')
                    c=n[a:b]
                    if(int(c)==result[0][1]):
                        new = PIL.Image.open(os.curdir+'/'+'dataset'+'/'+n)
                        new=new.resize( (width1/grid, height1/grid), PIL.Image.BILINEAR )
                        pixel2=new.load()
                        break
            for x in range(0,width1/grid,1):
                for y in range(0,height1/grid,1):
                    a=list(pixel[x,y])
                    b=list(pixel2[x,y])
                    a=b
                    pixel[i+x,j+y]=tuple(a)
    img=img.resize((width,height),PIL.Image.BILINEAR)
    image_save(img,"Q2.jpg")

def layout(IMAGE_NOW_FILENAME,grid):
    img,pixel,width, height=image_open(IMAGE_NOW_FILENAME)
    com=[]
    width1=lcm(width,grid)
    height1=lcm(height,grid)
    img=img.resize((width1,height1),PIL.Image.BILINEAR)
    pixel=img.load()
    for n in os.listdir(os.curdir+'/'+'dataset'):
        if(n.find(".jpg")!=-1):
            his=[]
            img1 = PIL.Image.open(os.curdir+'/'+'dataset'+'/'+n)
            re=img1.resize((width1/grid,height1/grid), PIL.Image.BILINEAR)
            re=re.resize((lcm(width1/grid,8), lcm(height1/grid,8)), PIL.Image.BILINEAR )
            r,t=re.size
            pixel1=re.load()
            for l in range(0,r,r/8):
                for m in range(0,t,t/8):
                    total1=0
                    total2=0
                    total3=0
                    for o in range(l,l+r/8,1):
                        for p in range(m,m+t/8,1):
                            a=list(pixel1[o,p])
                            total1+=a[0]
                            total2+=a[1]
                            total3+=a[2]
                    total1/=(r*t/64)
                    total2/=(r*t/64)
                    total3/=(r*t/64)
                    R=0.299*(total1) + 0.587*(total2) + 0.114*(total3)
                    G= -0.1687 * (total1) - 0.3313 * (total2) + 0.5 * (total3) + 128;
                    B=0.5 * (total1) - 0.4187 * (total2) - 0.0813 *(total3) + 128;
                    z=[R,G,B]
                    g=list((dct(z,norm='ortho')))
                    his+=g
            com.append(his+[n])
    for i in range(0,width1,width1/grid):
        for j in range(0,height1,height1/grid):
            result=[]
            crop_example=img.crop((i,j,i+width1/grid,j+height1/grid))
            crop_example=crop_example.resize( (lcm(width1/grid,8), lcm(height1/grid,8)), PIL.Image.BILINEAR )
            w,h=crop_example.size
            pixel4=crop_example.load()
            hist=[]
            for l in range(0,w,w/8):
                for m in range(0,h,h/8):
                    sum1=0
                    sum2=0
                    sum3=0
                    for o in range(l,l+w/8,1):
                        for p in range(m,m+h/8,1):
                            a=list(pixel4[o,p])
                            sum1+=a[0]
                            sum2+=a[1]
                            sum3+=a[2]
                    sum1/=(w*h/64)
                    sum2/=(w*h/64)
                    sum3/=(w*h/64)
                    Y=0.299*(sum1) + 0.587*(sum2) + 0.114*(sum3)
                    CB= -0.1687 * (sum1) - 0.3313 * (sum2) + 0.5 * (sum3) + 128;
                    CR=0.5 * (sum1) - 0.4187 * (sum2) - 0.0813 *(sum3) + 128;
                    z=[Y,CB,CR]
                    g=list((dct(z,norm='ortho')))
                    hist+=g
            result=manhattan1(com,hist)
            result=sorted(result)
            new = PIL.Image.open(os.curdir+'/'+'dataset'+'/'+result[0][1])
            new=new.resize( (width1/grid, height1/grid), PIL.Image.BILINEAR)
            pixel2=new.load()
            for x in range(0,width1/grid,1):
                for y in range(0,height1/grid,1):
                    a=list(pixel[x,y])
                    b=list(pixel2[x,y])
                    a=b
                    pixel[i+x,j+y]=tuple(a)
    img=img.resize((width,height),PIL.Image.BILINEAR)
    image_save(img,"Q3.jpg")


IMAGE_NOW_FILENAME = ""



class GUIDemo(Frame):
    static_grid=10 
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
 
    def createWidgets(self):
        self.load = Button(self)
        self.load["text"] = "Load"
        self.load.grid(row=2, column=0)
        self.load["command"] =  self.loadMethod
        
        self.average = Button(self)
        self.average["text"] = "average"
        self.average.grid(row=2, column=1)
        self.average["command"] =  self.averageMethod
        
        self.histogram = Button(self)
        self.histogram["text"] = "histogram"
        self.histogram.grid(row=2, column=2)
        self.histogram["command"] =  self.histogramMethod
        
        self.layout = Button(self)
        self.layout["text"] = "layout"
        self.layout.grid(row=2, column=3)
        self.layout["command"] =  self.layoutMethod
        
        self.layout = Button(self)
        self.layout["text"] = "show"
        self.layout.grid(row=2, column=4)
        self.layout["command"] =  self.showMethod

        self.displayText = Label(self)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=3, column=0, columnspan=7)
 
    def loadMethod(self):
        self.displayText["text"] = "This is Load button."

        ftypes = [('Python files', '*.py'), ('Image files','*.jpg'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        global IMAGE_NOW_FILENAME
        
        if fl != '':
            IMAGE_NOW_FILENAME = fl
            print "load ",IMAGE_NOW_FILENAME
            a,pixel,width, height = image_open(fl)
        return IMAGE_NOW_FILENAME
    def histogramMethod(self):
        self.displayText["text"] = "This is histogram button."
        histogram(IMAGE_NOW_FILENAME,self.static_grid)
        print "I will show you the mosaic photo using color histogram method"
    def averageMethod(self):
        self.displayText["text"] = "This is average button."
        average(IMAGE_NOW_FILENAME,self.static_grid)
        print "I will show you the mosaic photo using RGB average method"
    def layoutMethod(self):
        self.displayText["text"] = "This is layout button."
        layout(IMAGE_NOW_FILENAME,self.static_grid)
        print "I will show you the mosaic photo using color layout method"
    def showMethod(self):
        self.displayText["text"] = "This is show button."
        image_show(IMAGE_NOW_FILENAME)
if __name__ == '__main__':
    print "Please input grid you want to cut."
    grid=raw_input()
    root = Tk()
    app = GUIDemo(master=root)
    app.static_grid=int(grid)
    app.mainloop()
