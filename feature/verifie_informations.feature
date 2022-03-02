Funcionalidade: Consultar Ganho/Perda de cobertura arbôrea de uma área
    "A partir do site de geografia
    entro seleciono uma área baseado na long e lat
    coleto informações dessa área." 

   Cenario: Tem informaçoes presentes? com base no desenho no mapa por cliques 
     Dado  Entro no site globalforest (com interface grafica)
      Quando Configuro RADD no menu esquerdo opcao Forest Change
        E Clico botao de analise presente ao lado do menu esquerdo
        E Clico botao de começar a desenhar ou fazer upload da forma
        E soluçao temporaria, para erro que acontece aqui
        E Clico botao de começar a desenhar ou fazer upload da forma
        E Desenho no mapa com base na long e lat
      Entao Verifica se ganho/perda de cobertura arborea estão presentes
    
    Cenario: Tem informaçoes presentes? com base no desenho no mapa por cliques 
     Dado  Entro no site globalforest (sem interface grafica)
      Quando Configuro RADD no menu esquerdo opcao Forest Change
        E Clico botao de analise presente ao lado do menu esquerdo
        E Clico botao de começar a desenhar ou fazer upload da forma
        E soluçao temporaria, para erro que acontece aqui
        E Clico botao de começar a desenhar ou fazer upload da forma
        E Desenho no mapa com base na long e lat
      Entao Verifica se ganho/perda de cobertura arborea estão presentes

    Cenario: Informaçoes presentes? com base no upload de um shape
      Dado Entro no site globalforest (com interface grafica)  
        Quando Configuro RADD no menu esquerdo opcao Forest Change
          E Clico botao de analise presente ao lado do menu esquerdo 
          E Coloco o arquivo com a forma
        Entao Verifica se ganho/perda de cobertura arborea estão presentes com base em um shape

   