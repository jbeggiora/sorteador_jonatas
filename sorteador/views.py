import random
from django.shortcuts import render, redirect

# Configuração de Segurança (AppSec)
LIMITE_PARTICIPANTES = 50 

def sorteador_view(request):
    # Inicializa as listas na sessão se não existirem
    if 'lista_nomes' not in request.session:
        request.session['lista_nomes'] = []
    if 'sorteados' not in request.session:
        request.session['sorteados'] = []
    
    ultimo_sorteado = None
    aviso = None

    if request.method == "POST":
        # BLOCO: ADICIONAR NOMES
        if 'adicionar' in request.POST:
            novo_nome = request.POST.get('nome', '').strip()
            # Criamos uma cópia da lista para garantir a mutabilidade
            lista_atual = list(request.session.get('lista_nomes', []))
            
            # Validações de Segurança
            if len(lista_atual) >= LIMITE_PARTICIPANTES:
                aviso = {'texto': f"Erro: Limite de {LIMITE_PARTICIPANTES} nomes atingido!", 'tipo': 'error'}
            elif len(novo_nome) > 30:
                aviso = {'texto': "Erro: Nome muito longo!", 'tipo': 'error'}
            elif novo_nome and not novo_nome.replace(" ", "").isalpha():
                aviso = {'texto': "Erro: Use apenas letras!", 'tipo': 'error'}
            elif novo_nome in lista_atual:
                aviso = {'texto': f"Erro: '{novo_nome}' já está na lista!", 'tipo': 'error'}
            elif novo_nome:
                lista_atual.append(novo_nome)
                # Salvamento explícito
                request.session['lista_nomes'] = lista_atual
                request.session.modified = True 
                aviso = {'texto': f"{novo_nome} adicionado com sucesso!", 'tipo': 'success'}

        # BLOCO: SORTEAR
        elif 'sortear_um' in request.POST:
            lista = list(request.session.get('lista_nomes', []))
            if lista:
                escolhido = random.choice(lista)
                lista.remove(escolhido)
                
                sorteados = list(request.session.get('sorteados', []))
                sorteados.insert(0, escolhido)
                
                # Atualiza sessão
                request.session['lista_nomes'] = lista
                request.session['sorteados'] = sorteados
                request.session.modified = True
                ultimo_sorteado = escolhido

        # BLOCO: RESETAR
        elif 'resetar' in request.POST:
            request.session['lista_nomes'] = []
            request.session['sorteados'] = []
            request.session.modified = True
            return redirect('/')

    return render(request, "sorteador.html", {
        "lista_nomes": request.session.get('lista_nomes', []),
        "sorteados": request.session.get('sorteados', []),
        "ultimo_sorteado": ultimo_sorteado,
        "aviso": aviso,
        "limite": LIMITE_PARTICIPANTES
    })