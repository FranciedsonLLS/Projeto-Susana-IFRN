from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required


from django.urls import reverse_lazy



from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User

from customauth.models import MyUser
from customauth.forms import UserChangeForm

#bot e grafico
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import codecs
import os
import re

# Create your views here.

#grafico

# parte do código do gráfico 
@login_required(login_url='auth.login') 
def graficoHipertensaoDiabetes(request):
    pacote = {}
    vetor = []
    a = 0
    for i in range(27):
        for mes in range(12):
            #mude o caminho de onde estao as tabelas
            df = pd.read_csv(f'C:/Users/marco/Downloads/EstadosFinal/estado{i+1}/hipertensao_diabetes/mes'+str(mes+1)+'.csv', encoding="mbcs") 
            df2 = df.max()
            df3 = df2.max()
            df4 = str(df3)
            df5 = df4.split(';')
            aux = len(df5)
            dff = df5[aux-1]
            vetor.append(dff)
            a  += 1
    pacote = {"chave": vetor}
    return render(request, 'grafico.html', pacote)

@login_required(login_url='auth.login') 
def graficoHipertensao(request):
    pacote = {}
    vetor = []
    a = 0
    for i in range(27):
        for mes in range(12):
            #mude o caminho de onde estao as tabelas
            df = pd.read_csv(f'C:/Users/marco/Downloads/divisao_estadual_hipertensao/estado{i+1}/mes'+str(mes+1)+'.csv', encoding="mbcs",on_bad_lines='skip') 
            df2 = df.max()
            df3 = df2.max()
            df4 = str(df3)
            df5 = df4.split(';')
            aux = len(df5)
            dff = df5[aux-1]
            vetor.append(dff)
            a  += 1
    pacote = {"chave": vetor}
    return render(request, 'grafico-hipertensao.html', pacote)

@login_required(login_url='auth.login') 
def graficoDiabetesTipo1(request):
    pacote = {}
    vetor = []
    a = 0
    for i in range(27):
        for mes in range(12):
            #mude o caminho de onde estao as tabelas
            df = pd.read_csv(f'C:/Users/marco/Downloads/regiao_saude_diabetes_tipo1/estado{i+1}/mes'+str(mes+1)+'.csv', encoding="mbcs",on_bad_lines='skip')  
            df2 = df.max()
            df3 = df2.max()
            df4 = str(df3)
            df5 = df4.split(';')
            aux = len(df5)
            dff = df5[aux-1]
            vetor.append(dff)
            a  += 1
    pacote = {"chave": vetor}
    return render(request, 'grafico-diabetes-t1.html', pacote)

@login_required(login_url='auth.login')
def graficoDiabetesTipo2(request):
    pacote = {}
    vetor = []
    a = 0
    for i in range(27):
        for mes in range(12):
            #mude o caminho de onde estao as tabelas
            df = pd.read_csv(f'C:/Users/marco/Downloads/regiao_saude_diabetes_tipo2/estado{i+1}/mes'+str(mes+1)+'.csv', encoding="mbcs",on_bad_lines='skip')  
            df2 = df.max()
            df3 = df2.max()
            df4 = str(df3)
            df5 = df4.split(';')
            aux = len(df5)
            dff = df5[aux-1]
            vetor.append(dff)
            a  += 1
    pacote = {"chave": vetor}
    return render(request, 'grafico-diabetes-t2.html', pacote)



    

#funções do bot
def estados(nome,driver):
    botao =  driver.find_element("name", nome)
    botao.click()

@login_required(login_url='auth.login') 
def seleciona(request):
    return render(request, "selecionar.html")

def campo(id, index,driver):
    select_element = driver.find_element(By.ID,id)
    select_object = Select(select_element)
    select_object.select_by_index(index)


#selecionando o conteudo das tabelas
def selecionador(id, index, deselect,driver):
    select_element = driver.find_element(By.ID,id)
    select_object = Select(select_element)
    select_object.select_by_index(index)
#caso o select seja multiple colocar true
    if deselect:
       select_object.deselect_by_index(0)


#selecionar tabelade acordo com o index(so precisa mudar os numeros para mudar o conteudo baixado)


#clicar no botao
def clicker_by_name(nome,driver):    
    botao =  driver.find_element("name", nome)
    botao.click()


def bot(request, v1, v2):
    driver = webdriver.Chrome("chromedriver.exe")
    aux = 0
    if v1 == v2:
        aux = v1

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://datasus.saude.gov.br/acesso-a-informacao/hipertensao-e-diabetes-hiperdia/")
    if v1 == v2:
        for i in range(1):
            estados("radiobutton",driver)
            campo("mySelect", v1+i,driver)
            for col in range (3):
                for con in range (4):
                    if aux == 4 and con > 0 or aux ==4 and col > 0:
                        break
                    if aux == 23 and con > 0 or aux ==23 and col > 0:
                        break

                    for mes in range (12):
                        selecionador("L", 0, False,driver)
                        selecionador("C", (col+1), False,driver)       
                        if con == 0:   
                            selecionador("I", (con), False,driver) 
                        else:
                            selecionador("I", (con), True,driver)
                        if i+v1 == 1 or i+v1 == 4 or i+v1 == 17 or i+v1 == 20 or i+v1 == 22:
                            selecionador("A", (27+mes), True,driver)
                        elif i+v1 == 7:
                            selecionador("A", (7+mes), True,driver)
                        elif i+v1 == 23:
                            selecionador("A", (26+mes), True,driver)
                        else:
                            selecionador("A", (28+mes), True,driver)

                        time.sleep(1)   
                        clicker_by_name("mostre",driver)
                        time.sleep(1)
                        if aux == 23 and col == 0 and con == 2:
                            driver.back()
                            driver.refresh()
                            break
                        while True:
                            try:
                                driver.find_element(By.XPATH,"//tbody//tr//td[@class='botao_opcao']").click()
                                time.sleep(1)
                                break
                            except:
                                time.sleep(10)
                                driver.refresh()
                        time.sleep(4)
                        #mude o nome do usuario para pegar a sua pasta de downloads
                        caminho = "C://Users//marco//Downloads"
                        lista_arquivos = os.listdir(caminho)
                        lista_datas = []
                        for arquivo in lista_arquivos:
                        # descobrir a data desse arquivo
                            if ".csv" in arquivo:
                                data = os.path.getmtime(f"{caminho}/{arquivo}")
                                lista_datas.append((data, arquivo))
                                lista_datas.sort(reverse=True)
                                ultimo_arquivo = lista_datas[0]
                                #mude o nome do usuario para pegar a sua pasta de downloads em todos os ifs abaixo
                                if col == 0 and con == 0:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(v1+i)+'_regiao_saude_hipertensao_mes'+str(12-mes)+'.csv')
                                if col == 0 and con == 1:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_regiao_saude_diabetes_tipo1_mes'+str(12-mes)+'.csv')
                                if col == 0 and con == 2:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_regiao_saude_diabetes_tipo2_mes'+str(12-mes)+'.csv')
                                if col == 0 and con == 3:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_regiao_saude_hipertensao_diabetes_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 0:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_hipertensao_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 1:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_diabetes_tipo1_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 2:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_diabetes_tipo2_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 3:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_hipertensao_diabetes_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 0:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_hipertensao_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 1:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_diabetes_tipo1_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 2:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_diabetes_tipo2_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 3:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_hipertensao_diabetes_mes'+str(12-mes)+'.csv')
                                break
                        time.sleep(4)
                        driver.back()
                        driver.refresh()
            driver.get("https://datasus.saude.gov.br/acesso-a-informacao/hipertensao-e-diabetes-hiperdia/")


    else: 
        for i in range(v2-v1+1):
            estados("radiobutton",driver)
            campo("mySelect", v1+i,driver)
            for col in range (3):
                for con in range (4):
                    if i+v1 == 4 and con > 0 or i+v1 == 4 and col > 0:
                        break
                    if i+v1 == 23 and con > 0 or i+v1 ==23 and col > 0:
                        break
                    for mes in range (12):
                        selecionador("L", 0, False,driver)
                        selecionador("C", (col+1), False,driver)       
                        if con == 0:   
                            selecionador("I", (con), False,driver) 
                        else:
                            selecionador("I", (con), True,driver)
                        if i+v1 == 1 or i+v1 == 4 or i+v1 == 17 or i+v1 == 20 or i+v1 == 22:
                            selecionador("A", (27+mes), True,driver)
                        elif i+v1 == 7:
                            selecionador("A", (7+mes), True,driver)
                        elif i+v1 == 23:
                            selecionador("A", (26+mes), True,driver)
                        else:
                            selecionador("A", (28+mes), True,driver)

                        time.sleep(1)   
                        clicker_by_name("mostre",driver)
                        time.sleep(1)
                        while True:
                            try:
                                driver.find_element(By.XPATH,"//tbody//tr//td[@class='botao_opcao']").click()
                                time.sleep(1)
                                break
                            except:
                                time.sleep(10)
                                driver.refresh()
                        #mude o nome do usuario para pegar a sua pasta de downloads
                        caminho = "C://Users//marco//Downloads"
                        lista_arquivos = os.listdir(caminho)
                        lista_datas = []
                        for arquivo in lista_arquivos:
                        # descobrir a data desse arquivo
                            if ".csv" in arquivo:
                                data = os.path.getmtime(f"{caminho}/{arquivo}")
                                lista_datas.append((data, arquivo))
                                lista_datas.sort(reverse=True)
                                ultimo_arquivo = lista_datas[0]
                                #mude o nome do usuario para pegar a sua pasta de downloads em todos os ifs abaixo
                                if col == 0 and con == 0:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(v1+i)+'_regiao_saude_hipertensao_mes'+str(12-mes)+'.csv')
                                if col == 0 and con == 1:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_regiao_saude_diabetes_tipo1_mes'+str(12-mes)+'.csv')
                                if col == 0 and con == 2:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_regiao_saude_diabetes_tipo2_mes'+str(12-mes)+'.csv')
                                if col == 0 and con == 3:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_regiao_saude_hipertensao_diabetes_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 0:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_hipertensao_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 1:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_diabetes_tipo1_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 2:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_diabetes_tipo2_mes'+str(12-mes)+'.csv')
                                if col == 1 and con == 3:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_macrorregiao_saude_hipertensao_diabetes_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 0:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_hipertensao_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 1:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_diabetes_tipo1_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 2:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_diabetes_tipo2_mes'+str(12-mes)+'.csv')
                                if col == 2 and con == 3:
                                    os.rename(f'C:/Users/marco/Downloads/{ultimo_arquivo[1]}', f'C:/Users/marco/Downloads/estado'+str(i+v1)+'_divisao_administradual_hipertensao_diabetes_mes'+str(12-mes)+'.csv')
                                break
                        time.sleep(4)
                        driver.back()
                        driver.refresh()
            driver.get("https://datasus.saude.gov.br/acesso-a-informacao/hipertensao-e-diabetes-hiperdia/")




def home(request, LoginRequiredMixin):
    return render(request, LoginRequiredMixin, "index.html")


def Equipe(request):
    return render(request, "nossotime.html")
    

# VIEWS DE USUARIO #








def index (request):
    return render(request,'index.html')


def escolhaGrafico (request):
    return render(request,'escolha-grafico.html')




@login_required(login_url='auth.login')
def edit_profile(request, pk):
    user = MyUser.objects.get(pk=pk)
    if user.id == request.user.id:
        form = UserChangeForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        return render(request, 'edit_profile.html', {'form': form})
    return redirect('index')
    
        
