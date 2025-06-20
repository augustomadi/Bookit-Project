#!/usr/bin/env python
"""
Script para automatizar correções de linting comuns no projeto Django.
"""
import os
import re
from pathlib import Path


def fix_trailing_whitespace(file_path):
    """Remove espaços em branco no final das linhas."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove trailing whitespace
    fixed_content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Adiciona newline no final se não existir
    if not fixed_content.endswith('\n'):
        fixed_content += '\n'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)


def fix_imports(file_path):
    """Organiza imports em ordem correta."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Separa imports de outras linhas
    import_lines = []
    other_lines = []
    in_imports = False
    
    for line in lines:
        if line.strip().startswith(('import ', 'from ')):
            import_lines.append(line)
            in_imports = True
        elif in_imports and line.strip() == '':
            import_lines.append(line)
        else:
            if in_imports and line.strip() != '':
                in_imports = False
            other_lines.append(line)
    
    # Organiza imports
    if import_lines:
        # Separa imports por tipo
        stdlib_imports = []
        third_party_imports = []
        local_imports = []
        
        for line in import_lines:
            if line.strip() == '':
                continue
            if line.strip().startswith('from .') or line.strip().startswith('from ..'):
                local_imports.append(line)
            elif any(pkg in line for pkg in ['django', 'rest_framework', 'django_filters']):
                third_party_imports.append(line)
            else:
                stdlib_imports.append(line)
        
        # Reconstrói imports organizados
        organized_imports = []
        if stdlib_imports:
            organized_imports.extend(sorted(stdlib_imports))
            organized_imports.append('\n')
        if third_party_imports:
            organized_imports.extend(sorted(third_party_imports))
            organized_imports.append('\n')
        if local_imports:
            organized_imports.extend(sorted(local_imports))
            organized_imports.append('\n')
        
        # Reconstrói o arquivo
        fixed_lines = organized_imports + other_lines
    else:
        fixed_lines = lines
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)


def add_docstrings(file_path):
    """Adiciona docstrings básicas onde estão faltando."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Adiciona docstring para módulos
    if not content.strip().startswith('"""') and not content.strip().startswith("'''"):
        module_name = Path(file_path).stem
        docstring = f'"""Módulo {module_name}."""\n\n'
        content = docstring + content
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    """Executa todas as correções automáticas."""
    # Diretórios para processar
    dirs_to_process = ['propriedades', 'reservas', 'reservaHospedagens']
    
    for dir_name in dirs_to_process:
        if os.path.exists(dir_name):
            for root, dirs, files in os.walk(dir_name):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        print(f"Processando: {file_path}")
                        
                        try:
                            fix_trailing_whitespace(file_path)
                            fix_imports(file_path)
                            add_docstrings(file_path)
                        except Exception as e:
                            print(f"Erro ao processar {file_path}: {e}")
    
    print("Correções automáticas concluídas!")


if __name__ == '__main__':
    main() 