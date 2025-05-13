class ControleAcesso:
    def __init__(self):
        self.funcoes = {}          
        self.permissoes = {}       
    
    def adicionar_funcao(self, nome_funcao, funcoes_pais=None, funcoes_filhas=None):
        """Cadastra uma nova função na hierarquia de acesso"""
        if nome_funcao not in self.funcoes:
            self.funcoes[nome_funcao] = {'pais': [], 'filhos': []}
        
        if funcoes_pais:
            for funcao_pai in funcoes_pais:
                if funcao_pai in self.funcoes:
                    self.funcoes[nome_funcao]['pais'].append(funcao_pai)
                    self.funcoes[funcao_pai]['filhos'].append(nome_funcao)
                else:
                    raise ValueError(f"Função pai '{funcao_pai}' não encontrada")
    
    def adicionar_permissao(self, permissao, funcoes):
        """Registra uma permissão e vincula às funções especificadas"""
        if permissao not in self.permissoes:
            self.permissoes[permissao] = set()
        
        for funcao in funcoes:
            if funcao in self.funcoes:
                self.permissoes[permissao].add(funcao)
            else:
                raise ValueError(f"Função '{funcao}' não existe")
    
    def verificar_permissao(self, nome_funcao, permissao):
        """Checa se uma função possui determinada permissão, incluindo herança"""
        if permissao not in self.permissoes:
            return False
        
        if nome_funcao in self.permissoes[permissao]:
            return True
        
        fila = self.funcoes[nome_funcao]['pais'].copy()
        verificados = set()
        
        while fila:
            funcao_atual = fila.pop(0)
            if funcao_atual in verificados:
                continue
            verificados.add(funcao_atual)
            
            if funcao_atual in self.permissoes[permissao]:
                return True
            
            fila.extend(self.funcoes[funcao_atual]['pais'])
        
        return False

# TESTE

if __name__ == "__main__":
    sistema_acesso = ControleAcesso()
    
    sistema_acesso.adicionar_funcao('usuario')
    sistema_acesso.adicionar_funcao('administrador', ['usuario'])
    sistema_acesso.adicionar_funcao('superadmin', ['administrador'])
    
    sistema_acesso.adicionar_permissao('visualizar', ['usuario'])
    sistema_acesso.adicionar_permissao('editar', ['administrador'])
    sistema_acesso.adicionar_permissao('excluir', ['superadmin'])
    
    print("Usuário pode visualizar:", sistema_acesso.verificar_permissao('usuario', 'visualizar'))        
    print("Administrador pode visualizar:", sistema_acesso.verificar_permissao('administrador', 'visualizar'))      
    print("Administrador pode editar:", sistema_acesso.verificar_permissao('administrador', 'editar'))      
    print("Superadmin pode excluir:", sistema_acesso.verificar_permissao('superadmin', 'excluir'))  
    print("Usuário pode editar:", sistema_acesso.verificar_permissao('usuario', 'editar'))        
    print("Usuário pode excluir:", sistema_acesso.verificar_permissao('usuario', 'excluir'))