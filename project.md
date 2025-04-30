# Sistema de Controle de Clientes Django

## Modelo de Cliente
### Dados Pessoais
- Nome
- Sobrenome
- CPF
- Gênero
- Estado Civil
- Telefone
- Email
- Hora e Data de Cadastro

### Dados de Endereço
- Rua / Avenidas
- Número
- Complemento (ex: apto, bloco)
- Bairro
- Cidade
- Estado
- CEP

## Requisitos

### Painel Administrativo
- Listagem de clientes mostrando nome, sobrenome e cidade
- Filtro por nome e sobrenome
- Mínimo 15 clientes cadastrados
- Data e horário do cadastro (com Timezone configurado)

### Interface do Sistema
1. **Lista de Clientes**
    - Tabela com Nome, Sobrenome e Cidade
    - Links clicáveis nos nomes

2. **Página de Detalhes**
    - Exibição detalhada de todos os dados do cliente
    - Link de retorno para lista de clientes
