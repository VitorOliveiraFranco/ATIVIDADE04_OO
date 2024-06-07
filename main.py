from modelos.livro01 import Livro

# questão 2
harry_potter_e_a_pedra_filosofal=Livro('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997)
a_sociedade_do_anel=Livro('A Sociedade do Anel', 'J.R.R. Tolkien', 1997)
# print(harry_potter_e_a_pedra_filosofal)
# print(a_sociedade_do_anel)

# questão 3
# print(harry_potter_e_a_pedra_filosofal.emprestar)
# print(a_sociedade_do_anel.emprestar)

Livro.verificar_disponibilidade(1997)