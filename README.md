# Atividade: Models e Admin no Django

## Objetivo
Desenvolver um sistema para gerenciar um estoque de produtos e expandi-lo com categorias e fornecedores, utilizando o Django Admin.

---

## Parte 1: Gerenciamento de Produtos

### **1. Modelo de Produto**
Cada produto deve conter as seguintes informações:
- **Nome do produto**: (String, obrigatório)
- **Código do produto**: (String, único, obrigatório)
- **Descrição**: (Texto longo, opcional)
- **Preço**: (Decimal com 2 casas decimais)
- **Quantidade em estoque**: (Número inteiro)
- **Data de criação**: (Registrada automaticamente)

### **2. Configuração no Django Admin**
- Exiba na listagem os campos: `código`, `nome`, `preço`, `quantidade em estoque` e `data de criação`.
- Permita a **busca** do produto pelos campos `código` ou `nome`.
- Permita a **filtragem** por `data de criação`.
- Ordene os produtos por `data de criação` em **ordem decrescente**.
- Cadastre pelo menos **5 produtos** usando o Django Admin.

---



## Parte 2: Trabalhando com Exibição de Dados e Relacionamentos

### **1. Expansão do Sistema**
#### **Novos Modelos:**
- **Categoria:**
  - Estruture os atributos de acordo com as informações que você considera necessárias.
- **Fornecedor:**
  - Defina os atributos importantes para caracterizar um fornecedor.

#### **Relacionamentos:**
- Relacione **Produto** e **Categoria** com um relacionamento **muitos para muitos**:
  - Um produto pode pertencer a várias categorias.
  - Uma categoria pode conter vários produtos.
- Relacione **Produto** e **Fornecedor** com um relacionamento **muitos para um**:
  - Um produto deve ter um único fornecedor.
  - Um fornecedor pode fornecer vários produtos.

### **2. Configuração no Django Admin**
- Registre os modelos **Categoria** e **Fornecedor** no Django Admin.
- Adicione ao menos:
  - **5 produtos** (se já cadastrados, não é necessário repetir).
  - **3 categorias**.
  - **2 fornecedores**.

### **3. Criação de Páginas**
- **Listagem de Modelos:**
  - Crie uma página para listar cada modelo (Produtos, Categorias e Fornecedores).
- **Detalhes do Produto:**
  - Crie uma página de detalhes que exiba todas as informações de um produto específico.

---

## Envio da Atividade
- A atividade deve ser enviada via **GitHub**.
- Siga os passos abaixo para versionar seu trabalho:
  1. Crie uma **nova branch** para as alterações realizadas nesta atividade.
  2. Suba o código para o repositório GitHub.
  3. Envie o **link do repositório** e o **nome da branch** utilizada.

---

