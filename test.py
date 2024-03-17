# %%
#!pip install numpy
#!pip install matplotlib
#!pip install pandas
#!pip install openpyxl
#instal IPhython.display module
#!pip install IPython





# %% [markdown]
# # Določanje volumetričnega koeficienta prenosa kisika v bioreaktorju
# ## Razplinjevalna metoda
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
razpl = pd.read_excel("Kisik_razpl.xlsx")
#razpl to numpy array
razpl = razpl.to_numpy()
print(razpl)

din=pd.read_excel("Kisik_din.xlsx")
din = din.to_numpy()
print(din)


# %%
#print(din[2 , :])

#plot grapf for razpl
plt.figure(1)
plt.plot(razpl[0:,0], razpl[0:,1])
plt.xlabel('Čas [min]')
plt.ylabel('pO2 [%]')
plt.title('Sprememba pO2 v času pri metodi razplinjevanja.')
plt.show()


# %%
def zoomin(graf, x1, x2,step,naslov):
    #plot grapf for razpl
    razpl_1param = graf[x1:x2:step,:]
    #convert to numpy
    razpl_1param = np.array(razpl_1param)
    razpl_1param 
    #write to excel
    df = pd.DataFrame(razpl_1param)
    df.to_excel('razpl_1param.xlsx', index=False)

    #print(razpl_1param)
    plt.figure(1)
    plt.plot(razpl_1param[:,0], razpl_1param[:,1])
    plt.xlabel('Čas [min]')
    plt.ylabel('pO2 [%]')
    plt.title(naslov)
    plt.show()

    return razpl_1param

razpl_1param = zoomin(razpl, 130, 200,10, 'Sprememba pO2 v času pri metodi razplinjevanja za parametre 1')
razpl_1param = np.column_stack((razpl_1param, np.zeros(razpl_1param.shape[0])*1))
razpl_1param = np.column_stack((razpl_1param, np.zeros(razpl_1param.shape[0])*1))


# %%
#add collum to razpl_1param
#razpl_1param = np.column_stack((razpl_1param, np.zeros(razpl_1param.shape[0])))
def naklon(tabela):
    
    for i in range(tabela.shape[0]-1):
        tabela[i,2] = tabela[i+1,0] - tabela[0,0]

    for i in range(tabela.shape[0]-1):
        #logaritem
        tabela[i,3] = np.log( (100 - tabela[0,1]) / (100 - tabela[i,1]) )

    #print(tabela)
    df = pd.DataFrame(tabela)
    #name first column 'čas[min]'
    df.columns = ['čas[min]', 'pO2[%]', 't2-t1[min]', 'ln((Cal-Cal1)/(Cal-Cal2))']
    display(df)
    return tabela

razpl_1param = naklon(razpl_1param)

# %%
#plot grapf for razpl_1param third and fourth coloumn
def grafnaklon(tabela, naslov):
    
    plt.figure(1)       
    plt.plot(tabela[1:-1,2], tabela[1:-1,3], 'ro')
    plt.xlabel('t2-t1 [min]')
    plt.ylabel('ln((Cal-Cal1)/(Cal-Cal2))')
    plt.title(naslov)
    #red dots for data
    #write equation for trendline on graph
    x = tabela[1:-1,2]
    y = tabela[1:-1,3]
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b)
    #write text of equation of trendline
    plt.text(4.0, 0.5, 'y = ' + str(round(m, 3)) + 'x + ' + str(round(b, 3)), fontsize=12)
    plt.show()

grafnaklon(razpl_1param, 'Grafična določitev kL*a z razplinjevalno metodo pri parametrih 1.')




# %% [markdown]
# Razplinjevanje za 2 parametre

# %%
razpl_2param=zoomin(razpl, 300, 330,5, 'Sprememba pO2 v času pri metodi razplinjevanja za parametre 2')
razpl_2param=np.column_stack((razpl_2param, np.zeros(razpl_2param.shape[0])))
razpl_2param=np.column_stack((razpl_2param, np.zeros(razpl_2param.shape[0])))
razpl_2param=naklon(razpl_2param)

grafnaklon(razpl_2param, 'Grafična določitev kL*a z razplinjevalno metodo pri parametrih 2.')


# %% [markdown]
# ## Razplinjevalna metoda za parametre 3.
# 

# %%
razpl_3param=zoomin (razpl, 380, 400,2, 'Sprememba pO2 v času pri metodi razplinjevanja za parametre 3')
razpl_3param=np.column_stack((razpl_3param, np.zeros(razpl_3param.shape[0])))
razpl_3param=np.column_stack((razpl_3param, np.zeros(razpl_3param.shape[0])))
razpl_3param=naklon(razpl_3param)
grafnaklon(razpl_3param, 'Grafična določitev kL*a z razplinjevalno metodo pri parametrih 3.')


# %% [markdown]
# ## Razplinjevalna metoda za parametre 4.

# %%
razpl_4param=zoomin (razpl, 465, 490,3, 'Sprememba pO2 v času pri metodi razplinjevanja za parametre 4')
razpl_4param=np.column_stack((razpl_4param, np.zeros(razpl_4param.shape[0])))
razpl_4param=np.column_stack((razpl_4param, np.zeros(razpl_4param.shape[0])))
razpl_4param=naklon(razpl_4param)
grafnaklon(razpl_4param, 'Grafična določitev kL*a z razplinjevalno metodo pri parametrih 4.')   


# %% [markdown]
# 

# %% [markdown]
# ## Dinamična metoda z mikroorganizmi parametri 1.

# %%
#plot grapf for din
plt.figure(1)
plt.plot(din[0:,0], din[0:,1])
plt.xlabel('Čas [min]')
plt.ylabel('pO2 [%]')
plt.title('Sprememba pO2 v času pri dinamični metodi z mikroorganizmi.')
plt.show()

#plot grapf for din
plt.figure(2)
#put indexes of din x axis
x = np.arange(0, din.shape[0])
plt.plot(x, din[0:,1])



plt.xlabel('Čas [min]')
plt.ylabel('pO2 [%]')
plt.title('Sprememba pO2 v času pri dinamični metodi z mikroorganizmi.')
plt.show()

# %%
def naklon_max(tabela,max):
    
    for i in range(tabela.shape[0]-1):
        tabela[i,2] = tabela[i+1,0] - tabela[0,0]

    for i in range(tabela.shape[0]-1):
        #logaritem
        tabela[i,3] = np.log( (max - tabela[0,1]) / (max - tabela[i,1]) )

    #print(tabela)
    df = pd.DataFrame(tabela)
    #name first column 'čas[min]'
    df.columns = ['čas[min]', 'pO2[%]', 't2-t1[min]', 'ln((Cal-Cal1)/(Cal-Cal2))']
    display(df)
    return tabela


# %%
din_1param=zoomin(din, 180, 230,5, 'Sprememba pO2 v času pri dinamični metodi z mikroorganizmi za parametre 1')
din_1param=np.column_stack((din_1param, np.zeros(din_1param.shape[0])))
din_1param=np.column_stack((din_1param, np.zeros(din_1param.shape[0]))) 
din_1param=naklon_max(din_1param,80)
grafnaklon(din_1param, 'Grafična določitev kL*a z dinamično metodo pri parametrih 1.')


# %% [markdown]
# ## Dinamična metoda z mikroorganizmi pri parametrih 2.
# 

# %%
din_2param=zoomin(din, 390, 410,2, 'Sprememba pO2 v času pri dinamični metodi z mikroorganizmi za parametre 2')
din_2param=np.column_stack((din_2param, np.zeros(din_2param.shape[0])))
din_2param=np.column_stack((din_2param, np.zeros(din_2param.shape[0])))

din_2param=naklon_max(din_2param,91)
grafnaklon(din_2param, 'Grafična določitev kL*a z dinamično metodo pri parametrih 2.')



# %% [markdown]
# ## Dinamična metoda z mikroorganizmi pri parametrih 3.

# %%
din_3param=zoomin(din, 450, 470,2, 'Sprememba pO2 v času pri dinamični metodi z mikroorganizmi za parametre 3')
din_3param=np.column_stack((din_3param, np.zeros(din_3param.shape[0])))
din_3param=np.column_stack((din_3param, np.zeros(din_3param.shape[0])))
din_3param=naklon_max(din_3param,91)
grafnaklon(din_3param, 'Grafična določitev kL*a z dinamično metodo pri parametrih 3.')



