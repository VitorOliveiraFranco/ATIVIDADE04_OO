# questão 1
class Livro:
    
    livros=[]
    
    def __init__(self, titulo, autor, ano_publicado):    
        self.titulo=titulo
        self.autor=autor
        self.ano_publicado=ano_publicado
        self.disponivel=True

        Livro.livros.append(self)

# questão 2
    def __str__(self):
        return f'{self.titulo} {self.autor} {self.ano_publicado}'
    
# questão 3 
    @property
    def emprestar(self):
        self.disponivel=False
        return self.disponivel
    
#questão 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis=[livro for livro in Livro.livros if livro.ano_publicado == ano and livro.disponivel]
        for livro in livros_disponiveis:
                print(livro)
        # print(livro_publicado)

        
    