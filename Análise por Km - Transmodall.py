#!/usr/bin/env python
# coding: utf-8

# # Importação das bibliotecas

# In[78]:


"""
1°) Importação do pandas como pd para trabalhar com dados.
"""
import pandas as pd
"""
2°) Importação do numpy como np para trabalhar com matrizes
"""
import numpy as np
"""
3°) Importação do matplotlib.pyplot como plt para fazer gráficos.
"""
import matplotlib.pyplot as plt
"""
4°) De matplotlib.ticker vamos importar o AutoMinorLocator e o MaxNLocator para trabalhar com os "ticks"
    dos gráficos.
"""
from matplotlib.ticker import AutoMinorLocator, MaxNLocator
from matplotlib.font_manager import FontProperties
"""
5°) Importação do seaborn e do plotly.express para gráficos
"""
import seaborn as sbn
import plotly.express as px
"""
6°) Análise exploratória otimizada
"""
from pandas_profiling import ProfileReport


# # Importação dos dados

# In[79]:


Dados = pd.read_csv("TRANSMODALL_CE_PLAN1 - Plan1.csv")
Dados.head()


# # Pré-processamento de dados

# In[80]:


Dados.dtypes


# In[81]:


Dados_faltantes = 100*(Dados.isnull().sum()/len(Dados["DISTÂNCIA"]))
Dados_faltantes


# In[82]:


Dados.columns


# In[83]:


Fretes_abaixo_do_gasto = Dados.loc[Dados["VALOR "] < Dados["GASTO"]]
Fretes_abaixo_do_gasto


# In[84]:


"""
Criação das fontes de texto
"""
Fonte1 = {"family": "serif", #Familia da fonte
          "weight": "bold", #Peso da fonte
          "color": "black", #cor da fonte
          "size": 12.4} #Tamanho da fonte
font2 = FontProperties(family = "Serif", weight = "bold", style = "normal", size = 11)
Fonte3 = {"family": "serif", #Familia da fonte
          "weight": "bold", #Peso da fonte
          "color": "black", #cor da fonte
          "size": 20.4}
"""
Alocando a figura
"""
fig, ax = plt.subplots(figsize = (9, 7))
"""
Plot do gráfico
"""
plt.scatter(2*Dados["DISTÂNCIA"], Dados["VALOR "], color = "purple", alpha = 0.5)
plt.plot(2*Dados["DISTÂNCIA"], Dados["GASTO"], label = "Função de gasto bruto", color = "red", linewidth = 0.15)
plt.scatter(2*Fretes_abaixo_do_gasto["DISTÂNCIA"], Fretes_abaixo_do_gasto["VALOR "], color = "darkred", linewidths = 3.1, label = "\nALMIRO AFONSO - RN\nANTONIO MARTINS - RN\nAPODI - RN\nÊRERE - CE")
plt.grid(False)
"""
Redefinição da grossura dos eixos e da cor dos mesmos
"""
for axis in ["left", "right", "top", "bottom"]:
  ax.spines[axis].set_linewidth(2)
  ax.spines[axis].set_color("black")
"""
Trabalha com os ticks do gráfico
"""  
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis = "both", direction = "in", labelcolor = "black", labelsize = 12.4)
ax.tick_params(which = "minor", direction = "in", width = 2, color = "black")
ax.tick_params(which = "major", direction = "in", color = "black", length=3.4, width = 2)
"""
Labels
"""
ax.set_ylabel("Valor do frete (R$)", fontdict = Fonte1)
ax.set_xlabel("Total percorrido (Km)", fontdict = Fonte1)
"""
Tudo em negrito
"""
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
"""
Fundo branco
"""
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
fig.patch.set_facecolor("white")
"""
Mostrar gráfico
"""
plt.legend(frameon = False, prop = font2)
plt.text(1280, 10200, "3 cidades do Rio Grande do Norte são prejuízos", rotation=0, fontdict = Fonte3, 
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   ))
plt.show()


# In[85]:


Dados["GASTO"]


# In[86]:


Dados["GASTO"] + Dados["VALOR "]*0.25


# In[ ]:





# In[87]:


Fretes_abaixo_do_esperado = Dados.loc[Dados["VALOR "] < Dados["GASTO"] + Dados["VALOR "]*0.25]
Fretes_abaixo_do_esperado


# In[88]:


Fretes_abaixo_do_esperado.shape


# In[89]:


"""
Criação das fontes de texto
"""
Fonte1 = {"family": "serif", #Familia da fonte
          "weight": "bold", #Peso da fonte
          "color": "black", #cor da fonte
          "size": 12.4} #Tamanho da fonte
font2 = FontProperties(family = "Serif", weight = "bold", style = "normal", size = 12.4)
Fonte3 = {"family": "serif", #Familia da fonte
          "weight": "bold", #Peso da fonte
          "color": "black", #cor da fonte
          "size": 20.4}
"""
Alocando a figura
"""
fig, ax = plt.subplots(figsize = (9, 7))
"""
Plot do gráfico
"""
plt.scatter(2*Dados["DISTÂNCIA"], Dados["VALOR "], color = "purple", alpha = 0.5, label = "Fretes acima do esperado")
#plt.plot(2*Dados["DISTÂNCIA"], Dados["GASTO"] + Dados["VALOR "]*0.25, label = "Função de gasto bruto", color = "black", linewidth = 2)
plt.scatter(2*Fretes_abaixo_do_esperado["DISTÂNCIA"], Fretes_abaixo_do_esperado["VALOR "], color = "darkred", linewidths = 3.1, label = "Fretes abaixo do esperado")
plt.grid(False)
"""
Redefinição da grossura dos eixos e da cor dos mesmos
"""
for axis in ["left", "right", "top", "bottom"]:
  ax.spines[axis].set_linewidth(2)
  ax.spines[axis].set_color("black")
"""
Trabalha com os ticks do gráfico
"""  
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis = "both", direction = "in", labelcolor = "black", labelsize = 12.4)
ax.tick_params(which = "minor", direction = "in", width = 2, color = "black")
ax.tick_params(which = "major", direction = "in", color = "black", length=3.4, width = 2)
"""
Labels
"""
ax.set_ylabel("Valor do frete (R$)", fontdict = Fonte1)
ax.set_xlabel("Total percorrido (Km)", fontdict = Fonte1)
"""
Tudo em negrito
"""
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
"""
Fundo branco
"""
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
fig.patch.set_facecolor("white")
"""
Mostrar gráfico
"""
plt.legend(frameon = False, prop = font2)
plt.text(1200, 10000, "38 cidades estão abaixo do valor esperado", rotation=0, fontdict = Fonte3, 
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1, 1, 1),
                   fc=(1, 1, 1),
                   ))
plt.show()


# In[90]:


Dados.shape


# In[91]:


Lista_numbers = []
for i in range(0, 71):
    Lista_numbers.append("Acima do esperado")
for i in range(0, 39):
    Lista_numbers.append("Abaixo do esperado")
Lista_numbers = pd.DataFrame(Lista_numbers)  
"""
Criação da primeira fonte por meio de um dicionário;
Precisamos definir um dicionário passando 4 parâmetros;
family, weight, color e size
"""
font1 = {"family": "serif", "weight": "bold", "color": "black", "size":15}
"""
Criação da segunda fonte por meio da FontProperties()
Também passamos alguns parâmetros, como family, weight, style e size.
"""
font2 = FontProperties(family = "Serif", weight = "bold", style = "normal", size = 15)
"""
Definição das cores do gráfico de pizza.
"""
colors_pie = ["purple", "darkred"]
"""
Criando um "local" para alocar a nossa figura
"""
fig, ax = plt.subplots(figsize = (9, 6))
"""
Plot do gráfico do tipo "pie".
"""
Lista_numbers[0].value_counts().plot(kind = "pie", # Tipo de gráfico
                                     autopct = "%1.1f%%", # Mostrar porcentagens no gráfico
                                     shadow = True, # Sombreamento 
                                     explode = [0.02, 0.05], # Separamento entre as partes
                                     textprops = {"family": "serif", # Definição da fonte para os textos
                                                  "weight": "bold", 
                                                  "color": "white", 
                                                  "fontsize":13},
                                     colors = colors_pie) # cores do gráfico
"""
Definição de um fundo branco.
"""
fig.patch.set_facecolor("white")
"""
Definindo o título do gráfico
"""
ax.set_title("Acima x Abaixo do esperado", fontdict = font1)
"""
Propriedades da legenda da figura
"""
ax.legend(frameon = False, prop = font2, labelcolor = "black", bbox_to_anchor = [0.1, 1])
"""
Definição do label do eixo y
"""
ax.set_ylabel("")
"""
Mostrar gráfico
"""
plt.show()


# In[92]:


Lista_de_estados = []
for c in Dados["CIDADE "]:
    if "RN" in c:
        Lista_de_estados.append("RN")
    if "CE" in c:
        Lista_de_estados.append("CE")
    if "PB" in c:
        Lista_de_estados.append("PB")
Lista_de_estados        


# In[93]:


Lista_de_estados = pd.DataFrame(Lista_de_estados)
Lista_de_estados


# In[94]:


"""
Criação da primeira fonte por meio de um dicionário;
Precisamos definir um dicionário passando 4 parâmetros;
family, weight, color e size
"""
font1 = {"family": "serif", "weight": "bold", "color": "black", "size":15}
"""
Criação da segunda fonte por meio da FontProperties()
Também passamos alguns parâmetros, como family, weight, style e size.
"""
font2 = FontProperties(family = "Serif", weight = "bold", style = "normal", size = 15)
"""
Definição das cores do gráfico de pizza.
"""
colors_pie = ["purple", "darkred", "red"]
"""
Criando um "local" para alocar a nossa figura
"""
fig, ax = plt.subplots(figsize = (9, 6))
"""
Plot do gráfico do tipo "pie".
"""
Lista_de_estados[0].value_counts().plot(kind = "pie", # Tipo de gráfico
                                     autopct = "%1.1f%%", # Mostrar porcentagens no gráfico
                                     shadow = True, # Sombreamento 
                                     explode = [0.02, 0.05, 0.10], # Separamento entre as partes
                                     textprops = {"family": "serif", # Definição da fonte para os textos
                                                  "weight": "bold", 
                                                  "color": "white", 
                                                  "fontsize":13},
                                     colors = colors_pie) # cores do gráfico
"""
Definição de um fundo branco.
"""
fig.patch.set_facecolor("white")
"""
Definindo o título do gráfico
"""
ax.set_title("Estados abaixo do esperado", fontdict = font1)
"""
Propriedades da legenda da figura
"""
ax.legend(frameon = False, prop = font2, labelcolor = "black", bbox_to_anchor = [0.1, 1])
"""
Definição do label do eixo y
"""
ax.set_ylabel("")
"""
Mostrar gráfico
"""
plt.show()


# In[95]:


Fretes_acima_do_esperado = Dados.loc[Dados["GASTO"] + Dados["VALOR "]*0.25 <= Dados["VALOR "]]
Fretes_acima_do_esperado


# In[96]:


Lista_de_cidades_acima_do_esperado = []
for c in Dados["CIDADE "]:
    if "CE" in c:
        Lista_de_cidades_acima_do_esperado.append("CE")
    if "RN" in c:    
        Lista_de_cidades_acima_do_esperado.append("RN")
    if "PB" in c:
        Lista_de_cidades_acima_do_esperado.append("PB")
    if "PI" in c:
        Lista_de_cidades_acima_do_esperado.append("PI")
Lista_de_cidades_acima_do_esperado = pd.DataFrame(Lista_de_cidades_acima_do_esperado)        


# In[97]:


"""
Criação da primeira fonte por meio de um dicionário;
Precisamos definir um dicionário passando 4 parâmetros;
family, weight, color e size
"""
font1 = {"family": "serif", "weight": "bold", "color": "black", "size":15}
"""
Criação da segunda fonte por meio da FontProperties()
Também passamos alguns parâmetros, como family, weight, style e size.
"""
font2 = FontProperties(family = "Serif", weight = "bold", style = "normal", size = 15)
"""
Definição das cores do gráfico de pizza.
"""
colors_pie = ["purple", "darkred", "red", "gray"]
"""
Criando um "local" para alocar a nossa figura
"""
fig, ax = plt.subplots(figsize = (9, 6))
"""
Plot do gráfico do tipo "pie".
"""
Lista_de_cidades_acima_do_esperado[0].value_counts().plot(kind = "pie", # Tipo de gráfico
                                     autopct = "%1.1f%%", # Mostrar porcentagens no gráfico
                                     shadow = True, # Sombreamento 
                                     explode = [0.02, 0.05, 0.10, 0.10], # Separamento entre as partes
                                     textprops = {"family": "serif", # Definição da fonte para os textos
                                                  "weight": "bold", 
                                                  "color": "white", 
                                                  "fontsize":13},
                                     colors = colors_pie) # cores do gráfico
"""
Definição de um fundo branco.
"""
fig.patch.set_facecolor("white")
"""
Definindo o título do gráfico
"""
ax.set_title("Estados acima do esperado", fontdict = font1)
"""
Propriedades da legenda da figura
"""
ax.legend(frameon = False, prop = font2, labelcolor = "black", bbox_to_anchor = [0.1, 1])
"""
Definição do label do eixo y
"""
ax.set_ylabel("")
"""
Mostrar gráfico
"""
plt.show()


# In[98]:


# 5 MELHORES FRETES
Fretes_super_faturado = Dados.loc[Dados["GASTO"] + Dados["VALOR "]*0.5 <= Dados["VALOR "]]
Fretes_super_faturado


# In[99]:


Fretes_super_faturado.describe()
# Melhor Frete - São Gonçalo do Amarante


# In[100]:


Dados.describe()


# In[101]:


Pior_frete = Dados.loc[Dados["VALOR/KM"] == 5.149813]
Pior_frete


# In[102]:


# 5 piores Fretes
cinco_piores_Fretes = Dados.loc[Dados["VALOR "] < Dados["GASTO"] + Dados["VALOR "]*0.05]
cinco_piores_Fretes


# In[103]:


font1 = {"family": "serif", "weight": "bold", "color": "gray", "size":13}
"""
Criação da segunda fonte por meio da FontProperties()
Também passamos alguns parâmetros, como family, weight, style e size.
"""
font2 = FontProperties(family = "Serif", weight = "bold", style = "normal", size = 13)
"""
Criando um "local" para alocar a nossa figura
"""
fig, ax = plt.subplots(figsize = (12,9))
"""
plot de gráfico usando o seaborn
"""
sbn.countplot(cinco_piores_Fretes["VALOR/KM"],
              hue = cinco_piores_Fretes["CIDADE "],
              palette = ["gray", "red", "darkred", "orange", "blue"], # Cores
              saturation = 1) # Saturação das cores
"""
Definição de linewidth e da cor para as bordas do gráfico
"""
for axis in ["left", "right", "top", "bottom"]:
    ax.spines[axis].set_linewidth(2.4) # Definindo o linewidth das bordas do gráfico
    ax.spines[axis].set_color("gray") # Definindo a cor das bordas do gráfico
"""
Trabalhando com os ticks no gráfico 
"""    
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 13, left = True, bottom = True, top = False, right = False)
ax.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.3)
ax.tick_params(which = "minor", direction = "in", color = "gray", length = 4, width = 2, bottom = False)
"""
Mostrar tudo que é de texto em negrito.
"""
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
"""
Definição de um fundo branco.
"""
fig.patch.set_facecolor("white")
"""
Propriedades da legenda da figura
"""
plt.legend(frameon = False, prop = font2, labelcolor = "gray")
ax.set_xlabel("")
ax.set_ylabel("Número de pessoas", fontdict = font1)
"""
Mostrar gráfico
"""
plt.show()


# In[104]:


Fretes_super_faturado

