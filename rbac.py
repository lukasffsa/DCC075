class RBAC:
    def __init__(self):
        self.roles = {}          
        self.permissions = {}    
    
    def add_role(self, role_name, parents=None, children=None):
        """Adiciona uma função ao sistema RBAC"""
        if role_name not in self.roles:
            self.roles[role_name] = {'parents': [], 'children': []}
        
        if parents:
            for parent in parents:
                if parent in self.roles:
                    self.roles[role_name]['parents'].append(parent)
                    self.roles[parent]['children'].append(role_name)
                else:
                    raise ValueError(f"Parent role '{parent}' not found")
    
    def add_permission(self, permission, roles):
        """Adiciona uma permissão e associa a funções"""
        if permission not in self.permissions:
            self.permissions[permission] = set()
        
        for role in roles:
            if role in self.roles:
                self.permissions[permission].add(role)
            else:
                raise ValueError(f"Role '{role}' not found")
    
    def has_permission(self, role_name, permission):
        """Verifica se uma função tem uma permissão, considerando herança"""
        if permission not in self.permissions:
            return False
        
        # Verifica se a função tem a permissão diretamente
        if role_name in self.permissions[permission]:
            return True
        
        # Verifica herança: todas as funções pais recursivamente
        queue = self.roles[role_name]['parents'].copy()
        visited = set()
        
        while queue:
            current_role = queue.pop(0)
            if current_role in visited:
                continue
            visited.add(current_role)
            
            if current_role in self.permissions[permission]:
                return True
            
            # Adiciona os pais da função atual à fila
            queue.extend(self.roles[current_role]['parents'])
        
        return False

# Exemplo de uso similar ao código fornecido
if __name__ == "__main__":
    rbac = RBAC()
    
    # Adiciona funções
    rbac.add_role('user')
    rbac.add_role('admin', ['user'])
    rbac.add_role('superadmin', ['admin'])
    
    # Adiciona permissões
    rbac.add_permission('view', ['user'])
    rbac.add_permission('edit', ['admin'])
    rbac.add_permission('delete', ['superadmin'])
    
    # Testes
    print("user can view:", rbac.has_permission('user', 'view'))        
    print("admin can view:", rbac.has_permission('admin', 'view'))      
    print("admin can edit:", rbac.has_permission('admin', 'edit'))      
    print("superadmin can delete:", rbac.has_permission('superadmin', 'delete'))  
    print("user can edit:", rbac.has_permission('user', 'edit'))        
    print("user can delete:", rbac.has_permission('user', 'delete'))    

