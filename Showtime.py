try:
    import requests
    from tkinter import *
    from tkinter import ttk
    import tkinter.messagebox as msg
    from PIL import ImageTk, Image
    import logging
    import webbrowser
except:
    msg.showerror("Status - [Fatal]","Packages/Libraries not installed!!")
    exit()    

try:
    import imdb
    #from imdb import IMDbDataAccessError
except:
    msg.showerror("Status - [Fatal]","imdb package not found, install using \npip install IMDbPY ")
    exit()   

logging.disable(logging.CRITICAL)

def style_init():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabelframe",background='#134E5C')
    style.configure("red.Horizontal.TProgressbar", foreground='green', background='green')

def keyword_search():
    global kwordprogbar,kwordprogbarlbl
    kwordprogbarlbl=ttk.Label(kwordl,text="Progress: ",background="#134E5C",foreground="white")
    kwordprogbarlbl.grid(row=5,column=0)
    kwordprogbar=ttk.Progressbar(kwordl,style="red.Horizontal.TProgressbar",orient="horizontal",length=200,mode="determinate")
    kwordprogbar.grid(row=5,column=1,pady=20,columnspan=3)
    kwordprogbar['value']=20
    keyword_string=""
    keyword_movie_string=""
    if(kword.get()==""):
        msg.showerror("Status - [Error]","Enter a keyword!!")
        kwordprogbar.destroy()
        kwordprogbarlbl.destroy()
        r7.focus()
    else:
        try:
            kwordprogbar['value']=40
            inst=imdb.IMDb()
            kwordprogbar['value']=60
            all_keyword=inst.search_keyword(kword.get())
            kwordprogbar['value']=80
            all_keyword_movie=inst.get_keyword(kword.get())
            kwordprogbar['value']=100
        except:    
            msg.showerror("Status - [Error]","Check your Connection!!")
            kwordprogbar.destroy()
            kwordprogbarlbl.destroy()
        else:
            if(len(all_keyword)==0):
                txtkword.configure(state='normal')
                txtkword.replace('1.0','end',"No Keywords Found !!\n1. Try to be more Specific")
                txtkword.configure(state='disabled')
            else:    
                for i in range(len(all_keyword)):
                    keyword_string+=all_keyword[i]
                    keyword_string+=("\n")
                txtkword.configure(state='normal')    
                txtkword.replace('1.0','end',keyword_string)
                txtkword.configure(state='disabled')

            if(len(all_keyword_movie)==0):
                txtkwordmovie.configure(state='normal')
                txtkwordmovie.replace('1.0','end',"No Movies Found !!\n1. Try to be more Specific \n2. Search Movies based on Keywords from left panel")
                txtkwordmovie.configure(state='disabled')
            else:
                for i in range(len(all_keyword_movie)):
                    keyword_movie_string+=str(i+1)+"."+all_keyword_movie[i]['title']+" - tt"+all_keyword_movie[i].movieID
                    keyword_movie_string+=("\n")
                txtkwordmovie.configure(state='normal')
                txtkwordmovie.replace('1.0','end',keyword_movie_string)
                txtkwordmovie.configure(state='disabled')
            
def keyword():
    global r7
    try:
        if(r7.state()=="normal"):
            r7.focus()
    except:        
        r7=Toplevel(root)
        r7.title("Search By Keyword")
        r7.resizable(False,False)
        r7.iconbitmap("icon.ico")
        img=ImageTk.PhotoImage(Image.open("back3.jpg"))
        global kwordl
        kwordl=ttk.Label(r7,image=img)
        kwordl.photo=img
        kwordl.pack(fill='both',expand='yes')
        relkwordlbl=ttk.Label(r7,text="Related Keywords",background="#134E5C",foreground="white")
        mf8=ttk.Labelframe(kwordl,padding='3 3 12 12',labelwidget=relkwordlbl)
        mf8.grid(row=6,column=0,sticky=('N E W S'))
        mf8.rowconfigure(0,weight=1)
        mf8.columnconfigure(0,weight=1)
        movkwordlbl=ttk.Label(r7,text="Movies based on Keywords",background="#134E5C",foreground="white")
        mf9=ttk.Labelframe(kwordl,padding='3 3 12 12',labelwidget=movkwordlbl)
        mf9.grid(row=6,column=1,sticky=('N E W S'))
        mf9.rowconfigure(0,weight=1)
        mf9.columnconfigure(0,weight=1)
        srchkwordlbl=ttk.Label(r7,text="Search Keyword",background="#134E5C",foreground="white")
        mf10=ttk.Labelframe(kwordl,padding='3 3 12 12',labelwidget=srchkwordlbl)
        mf10.grid(row=4,column=0,columnspan=3)
        mf10.rowconfigure(0,weight=1)
        mf10.columnconfigure(0,weight=1)
        global kword
        kword=StringVar()
        ttk.Label(mf10,text="Enter Keyword: ",background="#134E5C",foreground="white").grid(row=2,column=0,padx=20)
        e=ttk.Entry(mf10,textvariable=kword,width=30)
        e.grid(row=2,column=1,padx=20)
        e.focus()
        Button(mf10,text="Search",command=keyword_search,bg="#004080",fg="white").grid(row=2,column=2,padx=20)
        global txtkword,txtkwordmovie
        txtkword=Text(mf8,width=30,height=10,borderwidth=5,relief='sunken')
        txtkword.grid(row=4,column=2)
        sb8=ttk.Scrollbar(mf8,orient="vertical",command=txtkword.yview)
        sb8.grid(row=4,column=3,sticky="ns")
        txtkword['yscrollcommand']=sb8.set
        txtkword.insert('1.0',"Results Here.......")
        txtkword.configure(state='disabled')
        txtkwordmovie=Text(mf9,width=40,height=10,borderwidth=5,relief='sunken',wrap='word')
        txtkwordmovie.grid(row=2,column=2)
        sb9=ttk.Scrollbar(mf9,orient="vertical",command=txtkwordmovie.yview)
        sb9.grid(row=2,column=3,sticky="ns")
        txtkwordmovie['yscrollcommand']=sb9.set
        txtkwordmovie.insert('1.0',"Results Here.......")
        txtkwordmovie.configure(state='disabled')

        r7.bind('<Return>',lambda e: keyword_search())

        for child in kwordl.winfo_children():
            child.grid_configure(padx=5,pady=5)

def bot100cleanup():
    botprogbar.destroy()
    botprogbarlbl.destroy()
    root.geometry("400x250")
    r6.destroy() 

def bot100():
    root.geometry("400x280")
    global botprogbar,botprogbarlbl
    botprogbarlbl=ttk.Label(rootl,text="Progress: ",background="#134E5C",foreground="white")
    botprogbarlbl.grid(row=19,column=2)
    botprogbar=ttk.Progressbar(rootl,style="red.Horizontal.TProgressbar",orient="horizontal",length=200,mode="determinate")
    botprogbar.grid(row=19,column=3,pady=20,columnspan=3)
    botprogbar['value']=20
    try:
        botprogbar['value']=40
        inst=imdb.IMDb()
        botprogbar['value']=60
        bot=inst.get_bottom100_movies()
        botprogbar['value']=100
    except:
        msg.showerror("Status - [Error]","Check your Connection!!")
        botprogbar.destroy()
        botprogbarlbl.destroy()
        root.geometry("400x250")
    else:
        global r6
        r6=Toplevel(root)
        r6.title("Bottom 100 Movies")
        r6.resizable(False,False)
        r6.iconbitmap("icon.ico")
        bot100lbl=ttk.Label(r6,text="Bottom 100 Movies",background="#134E5C",foreground="white")
        mf7=ttk.Labelframe(r6,padding='3 3 12 12',labelwidget=bot100lbl)
        mf7.grid(row=0,column=0,sticky=('N E W S'))
        mf7.columnconfigure(0,weight=1)
        mf7.columnconfigure(0,weight=1)
        bot100str=""
        global txtbot100
        txtbot100=Text(mf7,width=50,height=10,borderwidth=5,relief='sunken',wrap='word',background="#004080",foreground="#ffff00")
        txtbot100.grid(row=4,column=2)
        sb7=ttk.Scrollbar(mf7,orient="vertical",command=txtbot100.yview)
        sb7.grid(row=4,column=3,sticky="ns")
        txtbot100['yscrollcommand']=sb7.set
        for i in range(len(bot)):
            bot100str+=str(i+1)+"."+bot[i]['title']+" - tt"+bot[i].movieID
            bot100str+=("\n")
        txtbot100.insert('1.0',bot100str)
        txtbot100.configure(state='disabled')

        r6.protocol("WM_DELETE_WINDOW",bot100cleanup)

def top250cleanup():
    topprogbar.destroy()
    topprogbarlbl.destroy()
    root.geometry("400x250")
    r5.destroy() 

def top250():
    root.geometry("400x280")
    global topprogbar,topprogbarlbl
    topprogbarlbl=ttk.Label(rootl,text="Progress: ",background="#134E5C",foreground="white")
    topprogbarlbl.grid(row=18,column=2)
    topprogbar=ttk.Progressbar(rootl,style="red.Horizontal.TProgressbar",orient="horizontal",length=200,mode="determinate")
    topprogbar.grid(row=18,column=3,pady=20,columnspan=3)
    topprogbar['value']=20
    try:
        #logger = logging.getLogger('imdbpy')
        #logger.disabled = True
        topprogbar['value']=40
        inst=imdb.IMDb()
        topprogbar['value']=60
        top=inst.get_top250_movies()
        topprogbar['value']=100   
    except:
        msg.showerror("Status - [Error]","Check your Connection!!")
        topprogbar.destroy()
        topprogbarlbl.destroy()
        root.geometry("400x250") 
    else:
        global r5
        r5=Toplevel(root)
        r5.title("Top 250 Movies")
        r5.resizable(False,False)
        r5.iconbitmap("icon.ico")
        top250lbl=ttk.Label(r5,text="Top 250 Movies",background="#134E5C",foreground="white")
        mf6=ttk.Labelframe(r5,padding='3 3 12 12',labelwidget=top250lbl)
        mf6.grid(row=0,column=0,sticky=('N E W S'))
        mf6.columnconfigure(0,weight=1)
        mf6.columnconfigure(0,weight=1)
        top250str=""
        txttop250=Text(mf6,width=50,height=10,borderwidth=5,relief='sunken',wrap='word',background="#004080",foreground="#ffff00")
        txttop250.grid(row=4,column=2)
        sb6=ttk.Scrollbar(mf6,orient="vertical",command=txttop250.yview)
        sb6.grid(row=4,column=3,sticky="ns")
        txttop250['yscrollcommand']=sb6.set
        for i in range(len(top)):
            top250str+=str(i+1)+"."+top[i]['title']+" - tt"+top[i].movieID
            top250str+=("\n")
        txttop250.insert('1.0',top250str)
        txttop250.configure(state='disabled')

        r5.protocol("WM_DELETE_WINDOW",top250cleanup)

def searchid():
    global movidprogbar,movidprogbarlbl
    movidprogbarlbl=ttk.Label(movidl,text="Progress: ",background="#134E5C",foreground="white")
    movidprogbarlbl.grid(row=2,column=2)
    movidprogbar=ttk.Progressbar(movidl,style="red.Horizontal.TProgressbar",orient="horizontal",length=200,mode="determinate")
    movidprogbar.grid(row=2,column=3,pady=20)
    movidprogbar['value']=20
    movstr=""
    if(sname.get()==""):
        msg.showerror("Status - [Error]","Enter a Movie name!!")
        movidprogbar.destroy()
        movidprogbarlbl.destroy()
        r4.focus()
    else:
        try:
            movidprogbar['value']=40
            inst=imdb.IMDb()
            movidprogbar['value']=60
            search=inst.search_movie(sname.get())
            movidprogbar['value']=100
        except:    
            msg.showerror("Status - [Error]","Check your Connection!!")
            movidprogbar.destroy()
            movidprogbarlbl.destroy()
        else:
            if(len(search)==0):
                txtmovieid.configure(state='normal')
                txtmovieid.replace('1.0','end',"No Movies Found!! \n1. Check if Movie name is Correct")
                txtmovieid.configure(state='disabled')
            else:    
                for i in range(len(search)):
                    movid=search[i].movieID
                    movstr+=search[i]['title'] + " : " +"tt"+movid
                    movstr+=("\n")
                txtmovieid.configure(state='normal')    
                txtmovieid.replace('1.0','end',movstr)
                txtmovieid.configure(state='disabled')

def movieid():
    global r4
    try:
        if(r4.state()=="normal"):
            r4.focus()
    except:        
        r4=Toplevel(root)
        r4.title("Search Movie Id")
        r4.resizable(False,False)
        r4.iconbitmap("icon.ico")
        img=ImageTk.PhotoImage(Image.open("back3.jpg"))
        global movidl
        movidl=ttk.Label(r4,image=img)
        movidl.photo=img
        movidl.pack(fill='both',expand='yes')
        srchmnamelbl=ttk.Label(r4,text="Search Movie Name",background="#134E5C",foreground="white")
        mf5=ttk.Labelframe(movidl,padding='3 3 12 12',labelwidget=srchmnamelbl)
        mf5.grid(row=0,column=2,sticky=('N E W S'),padx=20,pady=10,columnspan=4)
        mf5.rowconfigure(0,weight=1)
        mf5.columnconfigure(0,weight=1)
        midlbl=ttk.Label(r4,text="Movie ID",background="#134E5C",foreground="white")
        mf11=ttk.Labelframe(movidl,padding='3 3 12 12',labelwidget=midlbl)
        mf11.grid(row=4,column=2,sticky="nwes",padx=20,pady=10,columnspan=4)
        mf11.rowconfigure(0,weight=1)
        mf11.columnconfigure(0,weight=1)
        global sname
        sname=StringVar()
        ttk.Label(mf5,text="Enter Movie Name: ",background="#134E5C",foreground="white").grid(row=2,column=1,padx=10)
        e=ttk.Entry(mf5,textvariable=sname,width=30)
        e.grid(row=2,column=2,padx=10)
        e.focus()
        Button(mf5,text="Search",command=searchid,bg="#004080",fg="white").grid(row=2,column=3,padx=10)
        global txtmovieid
        txtmovieid=Text(mf11,width=50,height=10,borderwidth=5,relief='sunken',wrap='word')
        txtmovieid.grid(row=4,column=2)
        sb5=ttk.Scrollbar(mf11,orient="vertical",command=txtmovieid.yview)
        sb5.grid(row=4,column=3,sticky='ns')
        txtmovieid['yscrollcommand']=sb5.set
        txtmovieid.insert('1.0',"Results Here.......")
        txtmovieid.configure(state='disabled')
        r4.bind('<Return>',lambda e: searchid())
    
def features():
    pass

def about():
    global r3
    r3=Toplevel(root)
    r3.title("About ShowTime v2.0.1")
    #r3.geometry("300x400")
    r3.resizable(False,False)
    r3.iconbitmap("icon.ico")
    mf4=ttk.Frame(r3,padding='3 3 12 12')
    mf4.pack(fill="both",expand="yes")
    mf4.rowconfigure(0,weight=1)
    mf4.columnconfigure(0,weight=1)
    l=ttk.Label(mf4,background="#004080")
    l.pack(fill="both",expand="yes")
    ttk.Label(l,text="Created by : Hrithik Raj",foreground="white",background="#004080",font=("Arial Black",16)).grid(row=2,column=0,columnspan=3)
    img=ImageTk.PhotoImage(Image.open("icon.ico"))
    l2=ttk.Label(l,background="#004080",image=img)
    l2.photo=img
    l2.grid(row=4,column=0,)
    ttk.Label(l,text="Name : ShowTime",foreground="white",background="#004080",font=("Calibri",16)).grid(row=4,column=1,sticky="w")
    ttk.Label(l,text="Version : v2.0.1",foreground="white",background="#004080",font=("Calibri",16)).grid(row=6,column=1,sticky="w")
    ttk.Separator(l,orient="horizontal").grid(row=8,column=0,sticky="ew",columnspan=4)
    ttk.Label(l,text="Email : hrithikraj137@gmail.com",foreground="white",background="#004080",font=("Calibri",16)).grid(row=10,column=1,columnspan=3,sticky="w")
    abtlbl=ttk.Label(l,text="Github : https://github.com/Cyborg117",foreground="white",background="#004080",font=("Calibri",16),cursor="hand1")
    abtlbl.grid(row=12,column=1,columnspan=3,sticky="w")
    abtlbl.bind('<1>',lambda e: webbrowser.open("https://github.com/Cyborg117"))
    for child in l.winfo_children():
        child.grid_configure(pady=10)

def getdatacleanup():
    dataprogbar.destroy()
    dataprogbarlbl.destroy()
    root.geometry("400x250")
    r2.destroy() 

def getdata():
    if(mname.get()=="" and mid.get()==""):
        msg.showerror("Status - [Error]","Enter at least a Movie name OR ID")
    else:
        root.geometry("400x280")
        global dataprogbar,dataprogbarlbl
        dataprogbarlbl=ttk.Label(rootl,text="Progress: ",background="#134E5C",foreground="white")
        dataprogbarlbl.grid(row=20,column=2)
        dataprogbar=ttk.Progressbar(rootl,style="red.Horizontal.TProgressbar",orient="horizontal",length=200,mode="determinate")
        dataprogbar.grid(row=20,column=3,pady=20,columnspan=3)
        dataprogbar['value']=20
        
        file=open("keyfile.txt","r")
        api_key=file.read()
        file.close()
        try:
            dataprogbar['value']=50
            url="http://www.omdbapi.com/?apikey="+api_key+"&i="+mid.get()+"&t="+mname.get()
            dataprogbar['value']=70
            response=requests.get(url)
            dataprogbar['value']=90
            data=response.json()
            dataprogbar['value']=100
                                              
        except Exception as e:
            msg.showerror("Status - [Error]","Check Your Connection!!!")
            dataprogbar.destroy()
            dataprogbarlbl.destroy()
            root.geometry("400x250")

        else:
            response_status=data['Response']
            if(response_status=="True"):
                global r2
                r2=Toplevel(root)
                r2.title("ShowTime V2.0.0 | Hrithik Raj")
                r2.iconbitmap("icon.ico")
                #r2.geometry("1000x500")
                r2.resizable(False,False)
                mf2=ttk.Frame(r2,padding='3 3 12 12')
                mf2.grid(row=0,column=0,sticky=('N E W S'))
                mf2.columnconfigure(0,weight=1)
                mf2.columnconfigure(0,weight=1)
                mf3=ttk.Frame(r2,padding='3 3 12 12')
                mf3.grid(row=0,column=2,sticky=('N E W S'))
                mf3.columnconfigure(0,weight=1)
                mf3.columnconfigure(0,weight=1)

                posterurl=data['Poster']
                if(posterurl=="N/A"):
                    l=ttk.Label(mf2,text="No Image Available.")
                    l.grid(row=1,column=0)
                else:
                    response2=requests.get(posterurl)
                    file = open("iposter.gif", "wb")
                    file.write(response2.content)
                    file.close()

                    img=ImageTk.PhotoImage(Image.open("iposter.gif"))
                    l=ttk.Label(mf2,image=img)
                    l.photo=img
                    l.grid(row=1,column=0)
                
                try:
                    title.set(data['Title'])
                except:
                    title.set("N/A")
                try:        
                    runtime.set(data['Runtime'])
                except:
                    runtime.set("N/A")
                try:        
                    release_date.set(data['Released'])
                except:
                    release_date.set("N/A")    
                try:
                    production.set(data['Production'])
                except:
                    production.set("N/A")
                try:
                    rated.set(data['Rated'])
                except:
                    rated.set("N/A")
                try:        
                    writers.set(data['Writer'])
                except:
                    writers.set("N/A")
                try:        
                    actors.set(data['Actors'])
                except:
                    actors.set("N/A")
                try:        
                    awards.set(data['Awards'])
                except:
                    awards.set("N/A")    
                try:
                    boxoffice.set(data['BoxOffice'])
                except:
                    boxoffice.set("N/A")
                try:
                    director.set(data['Director'])
                except:
                    director.set("N/A")
                try:        
                    genre.set(data['Genre'])
                except:
                    genre.set("N/A")  
                try:      
                    plot.set(data['Plot'])
                except:
                    plot.set("Unavailable")    
                try:
                    metascore.set(data['Metascore'])
                except:
                    metascore.set("Score Unavailable")    
                try:
                    metacritic.set(data['Ratings'][2]['Value'])
                except:
                    metacritic.set("Score Unavailable")
                try:
                    rt_rating.set(data['Ratings'][1]['Value'])
                except:
                    rt_rating.set("Score Unavailable")
                try:
                    imdb_rating.set(data['imdbRating']+str(" on ")+data['imdbVotes']+str(" Votes"))
                except:
                    imdb_rating.set("Score Unavailable")
                try:    
                    imd_rating.set(data['Ratings'][0]['Value'])
                except:
                    imd_rating.set("Score Unavailable")

                l=ttk.Label(mf3,background="#004080")
                l.pack(fill="both",expand="yes")
                    
                ttk.Label(l,text="DETAILS\t",font=('Arial Black',20,'underline'),background="#004080",foreground="white").grid(row=0,column=3)
                ttk.Label(l,text="Title: ",background="#004080",foreground="white").grid(row=1,column=3)
                ttk.Label(l,textvariable=title,background="#004080",foreground="white").grid(row=1,column=4)
                ttk.Label(l,text="Release Date: ",background="#004080",foreground="white").grid(row=2,column=3)
                ttk.Label(l,textvariable=release_date,background="#004080",foreground="white").grid(row=2,column=4)
                ttk.Label(l,text="Actors: ",background="#004080",foreground="white").grid(row=3,column=3)
                ttk.Label(l,textvariable=actors,background="#004080",foreground="white").grid(row=3,column=4)
                ttk.Label(l,text="Writers: ",background="#004080",foreground="white").grid(row=4,column=3)
                ttk.Label(l,textvariable=writers,background="#004080",foreground="white").grid(row=4,column=4)
                ttk.Label(l,text="Directors: ",background="#004080",foreground="white").grid(row=5,column=3)
                ttk.Label(l,textvariable=director,background="#004080",foreground="white").grid(row=5,column=4)
                ttk.Label(l,text="Production: ",background="#004080",foreground="white").grid(row=6,column=3)
                ttk.Label(l,textvariable=production,background="#004080",foreground="white").grid(row=6,column=4)
                ttk.Label(l,text="Runtime: ",background="#004080",foreground="white").grid(row=7,column=3)
                ttk.Label(l,textvariable=runtime,background="#004080",foreground="white").grid(row=7,column=4)
                ttk.Label(l,text="Rating: ",background="#004080",foreground="white").grid(row=8,column=3)
                ttk.Label(l,textvariable=rated,background="#004080",foreground="white").grid(row=8,column=4)
                ttk.Label(l,text="Awards: ",background="#004080",foreground="white").grid(row=9,column=3)
                ttk.Label(l,textvariable=awards,background="#004080",foreground="white").grid(row=9,column=4)
                ttk.Label(l,text="Box Office: ",background="#004080",foreground="white").grid(row=10,column=3)
                ttk.Label(l,textvariable=boxoffice,background="#004080",foreground="white").grid(row=10,column=4)
                ttk.Label(l,text="Genre: ",background="#004080",foreground="white").grid(row=11,column=3)
                ttk.Label(l,textvariable=genre,background="#004080",foreground="white").grid(row=11,column=4)
                
                ttk.Label(l,text="Plot: ",background="#004080",foreground="white").grid(row=12,column=3)
                if(plot.get()=="Unavailable" or plot.get()=="N/A"):
                    plot1=plot.get()
                    ttk.Label(l,text=plot1,background="#004080",foreground="white").grid(row=12,column=4)
                else: 
                    plot1=plot.get()[0:int(len(plot.get())/2)]
                    plot2=plot.get()[int(len(plot.get())/2):len(plot.get())]
                    ttk.Label(l,text=plot1,background="#004080",foreground="white").grid(row=12,column=4)
                    ttk.Label(l,text=plot2,background="#004080",foreground="white").grid(row=13,column=4)
                
                ttk.Label(l,text="RATINGS\t",font=('Arial Black',20,'underline'),background="#004080",foreground="white").grid(row=14,column=3)
                ttk.Label(l,text="IMDB: ",background="#004080",foreground="white").grid(row=15,column=3)
                ttk.Label(l,textvariable=imdb_rating,background="#004080",foreground="white").grid(row=15,column=4)
                ttk.Label(l,text="Metascore: ",background="#004080",foreground="white").grid(row=16,column=3)
                ttk.Label(l,textvariable=metascore,background="#004080",foreground="white").grid(row=16,column=4)
                ttk.Label(l,text="Rotten Tomatoes: ",background="#004080",foreground="white").grid(row=17,column=3)
                ttk.Label(l,textvariable=rt_rating,background="#004080",foreground="white").grid(row=17,column=4)
                ttk.Label(l,text="Metacritic: ",background="#004080",foreground="white").grid(row=18,column=3)
                ttk.Label(l,textvariable=metacritic,background="#004080",foreground="white").grid(row=18,column=4)
                ttk.Label(l,text="Internet Movie Database: ",background="#004080",foreground="white").grid(row=19,column=3)
                ttk.Label(l,textvariable=imd_rating,background="#004080",foreground="white").grid(row=19,column=4)

                r2.protocol("WM_DELETE_WINDOW",getdatacleanup)
            else:
                errmsg=data['Error']
                msg.showerror("Status - [Error]",errmsg)
                dataprogbar.destroy()
                dataprogbarlbl.destroy()
                root.geometry("400x250")

def maingui():
    global root
    root=Tk()
    root.title("Showtime v2.0.1 | Hrithik Raj")
    root.geometry("400x250")
    root.resizable(False,False)
    root.iconbitmap("icon.ico")
    #root.attributes("-alpha",0.7)

    mainframe=ttk.Frame(root,padding='3 3 12 12',borderwidth=2,relief='sunken')
    mainframe.pack(fill='both',expand='yes')
    mainframe.rowconfigure(0,weight=1)
    mainframe.columnconfigure(0,weight=1)    
    style_init()

    img=ImageTk.PhotoImage(Image.open("back.jpg"))
    global rootl
    rootl=ttk.Label(mainframe,image=img)
    rootl.photo=img
    rootl.pack(fill='both',expand='yes')

    global mname,mid,runtime,release_date,production,rated,writers,actors,awards
    global boxoffice,director,genre,plot,metascore,imdb_rating,imd_rating
    global rt_rating,metacritic,title
    mname=StringVar()
    mid=StringVar()

    title=StringVar()
    runtime=StringVar()
    release_date=StringVar()
    production=StringVar()
    rated=StringVar()
    writers=StringVar()
    actors=StringVar()
    awards=StringVar()
    boxoffice=StringVar()
    director=StringVar()
    genre=StringVar()
    plot=StringVar()
    metascore=StringVar()
    imdb_rating=StringVar()
    imd_rating=StringVar()
    rt_rating=StringVar()
    metacritic=StringVar()

    ttk.Label(rootl,text="Enter Movie Name: ",background="#134E5C",foreground="white").grid(row=2,column=2)
    e=ttk.Entry(rootl,textvariable=mname,width=30)
    e.grid(row=2,column=3,columnspan=4)
    e.focus()
    ttk.Label(rootl,text="OR",background="#134E5C",foreground="white").grid(row=4,column=2)
    ttk.Label(rootl,text="Enter Movie Id: ",background="#134E5C",foreground="white").grid(row=6,column=2)
    ttk.Entry(rootl,textvariable=mid,width=30).grid(row=6,column=3,columnspan=4)

    Button(rootl,text="Get Data",command=getdata,width=10,bg="#004080",fg="white",activebackground="yellow").grid(row=14,column=2,sticky="s")
    Button(rootl,text="Movie Id",command=movieid,width=10,bg="#004080",fg="white",activebackground="yellow").grid(row=14,column=3,sticky="s")
    Button(rootl,text="Top 250",command=top250,width=10,bg="#004080",fg="white",activebackground="yellow").grid(row=16,column=2,sticky="s")
    Button(rootl,text="Bottom 100",command=bot100,width=10,bg="#004080",fg="white",activebackground="yellow").grid(row=16,column=3,sticky="s")
    Button(rootl,text="keyword",command=keyword,width=10,bg="#004080",fg="white",activebackground="yellow").grid(row=14,column=4,sticky="s")
    Button(rootl,text="About",command=about,width=10,bg="#004080",fg="white",activebackground="yellow").grid(row=16,column=4,sticky="s")
    
    root.bind('<Return>',lambda e: getdata())

    for child in rootl.winfo_children():
        child.grid_configure(padx=5,pady=10)

    root.mainloop()

def key_verify():
    try:
        progbar['value']=20
        keyurl="http://www.omdbapi.com/?apikey="+key.get()+"&t=interstellar"
        progbar['value']=40
        response=requests.get(keyurl)
        progbar['value']=60
        data=response.json()
        progbar['value']=80
        resp_val=data['Response']
        progbar['value']=100
    except:
        msg.showerror("Status - [Error]","Check your Connection")
        key.set("")
        progbar['value']=0
    else:
        if(resp_val=="True"):
            msg.showinfo("SUCCESS","Key Verified successfully!!!")
            file=open("keyfile.txt","w")
            file.write(key.get())
            file.close()
            keyroot.destroy()
            maingui()
        else:
            errmsg=data['Error']
            msg.showerror("Status - [Error]",errmsg)
            key.set("")
            progbar['value']=0
            keyent.focus()
    
def key_check():
    global keyroot
    keyroot=Tk()
    keyroot.title("Key Verification") 
    keyroot.geometry("300x300")
    keyroot.iconbitmap("icon.ico")
    keyroot.resizable(False,False)
    
    global key
    key=StringVar()
    mainframe=ttk.Frame(keyroot,padding='3 3 12 12')
    mainframe.pack(fill="both",expand="yes")
    mainframe.rowconfigure(0,weight=1)
    mainframe.columnconfigure(0,weight=1)

    img=ImageTk.PhotoImage(Image.open("back3.jpg"))
    l=ttk.Label(mainframe,image=img)
    l.photo=img
    l.pack(fill="both",expand="yes")
    
    ttk.Label(l,text="Enter your API Key: ",background="#002240",foreground="white").grid(row=2,column=2)
    global keyent
    keyent=ttk.Entry(l,textvariable=key)
    keyent.grid(row=2,column=3)
    keyent.focus()
    Button(l,text="Verify Key",command=key_verify,background="#002240",foreground="white").grid(row=4,column=2)
    ttk.Label(l,text="Progress........",background="#002240",foreground="white").grid(row=7,column=2)
    global progbar
    progbar=ttk.Progressbar(l,orient="horizontal",length=200,mode="determinate")
    progbar.grid(row=8,column=2,columnspan=4)
    keyroot.bind('<Return>',lambda e: key_verify())
    for child in l.winfo_children():
        child.grid_configure(padx=10,pady=10)
    keyroot.mainloop()    

try:
    file=open("keyfile.txt","r")
except:
    key_check()
else:
    keyfiledata=file.read()
    if(len(keyfiledata)==0):
        key_check()
    else:
        maingui()
